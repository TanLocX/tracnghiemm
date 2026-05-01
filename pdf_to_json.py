"""
Đọc file PDF trắc nghiệm và xuất ra file JSON cùng thư mục.

Cài đặt:
    pip install pdfplumber

Cách dùng:
    python pdf_to_json.py <file.pdf> [tên_bộ_đề]
    python pdf_to_json.py de_thi.pdf "Đề thi MMT"

Cách nhận biết đáp án đúng (theo thứ tự ưu tiên):
    1. Text in đậm trong option (fontname chứa "Bold")
    2. Text bôi vàng / highlight màu vàng trong option
    3. Dòng "Đáp án: A" / "ĐA: B" / "=> C" phía sau các option
    4. Để trống nếu không tìm được — tự điền sau
"""

import json
import os
import re
import sys


# ── Trích xuất text + metadata (bold, highlight) từ PDF ─────────────────────

def extract_rich_lines(pdf_path: str) -> list[dict]:
    """
    Trả về list các dòng, mỗi dòng là dict:
        {
            "text": str,
            "bold": bool,       # có ký tự nào in đậm không
            "highlighted": bool # có ký tự nào bôi vàng không
        }
    """
    try:
        import pdfplumber
    except ImportError:
        raise ImportError("Cần cài: pip install pdfplumber")

    rich_lines = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Lấy vùng highlight màu vàng từ annotations
            highlight_rects = []
            annots = page.annots or []
            for annot in annots:
                if annot.get("data", {}).get("Subtype") == "Highlight":
                    rect = annot.get("data", {}).get("Rect")
                    if rect:
                        highlight_rects.append(rect)

            # Lấy từng ký tự với font info
            chars = page.chars

            # Nhóm ký tự theo dòng (dựa trên tọa độ y)
            lines_map: dict[float, list] = {}
            for ch in chars:
                y = round(ch["top"], 1)
                lines_map.setdefault(y, []).append(ch)

            for y in sorted(lines_map):
                ch_list = sorted(lines_map[y], key=lambda c: c["x0"])
                text = "".join(c["text"] for c in ch_list).strip()
                if not text:
                    continue

                # Kiểm tra bold: fontname thường chứa "Bold" hoặc "-B"
                is_bold = any(
                    "bold" in (c.get("fontname") or "").lower() or
                    c.get("fontname", "").endswith("-B") or
                    c.get("fontname", "").endswith(",Bold")
                    for c in ch_list
                )

                # Kiểm tra highlight vàng: ký tự nằm trong vùng highlight
                is_highlighted = False
                if highlight_rects:
                    for c in ch_list:
                        cx, cy = c["x0"], c["top"]
                        for rect in highlight_rects:
                            x0, y0, x1, y1 = rect
                            if x0 <= cx <= x1 and y0 <= cy <= y1:
                                is_highlighted = True
                                break
                        if is_highlighted:
                            break

                # Fallback: detect màu vàng qua non-stroking color của ký tự
                if not is_highlighted:
                    for c in ch_list:
                        color = c.get("non_stroking_color")
                        if color and _is_yellow(color):
                            is_highlighted = True
                            break

                rich_lines.append({
                    "text": text,
                    "bold": is_bold,
                    "highlighted": is_highlighted,
                })

    return rich_lines


def _is_yellow(color) -> bool:
    """Kiểm tra màu có phải vàng không (RGB hoặc CMYK)."""
    if isinstance(color, (list, tuple)):
        if len(color) == 3:
            r, g, b = color
            return r > 0.7 and g > 0.7 and b < 0.4
        if len(color) == 4:
            c, m, y, k = color
            return c < 0.2 and m < 0.2 and y > 0.6 and k < 0.2
    return False


# ── Parse thành danh sách câu hỏi ───────────────────────────────────────────

def parse_questions(rich_lines: list[dict]) -> list[dict]:
    question_re = re.compile(
        r"^(?:Câu\s*\d+\s*[:.)]\s*|Q\d+\s*[:.)]\s*|\d+\s*[.)]\s*)(.+)",
        re.IGNORECASE,
    )
    option_re = re.compile(r"^([A-Fa-f])[.)]\s+(.+)")
    answer_re = re.compile(
        r"^(?:đáp\s*án(?:\s*đúng)?|ĐA|=>|answer)\s*[:.]\s*([A-Fa-f])",
        re.IGNORECASE,
    )

    questions = []
    current_q = None
    current_opts: list[dict] = []  # {letter, text, bold, highlighted}
    explicit_ans = ""

    def flush():
        nonlocal current_q, current_opts, explicit_ans
        if not current_q or not current_opts:
            current_q = None
            current_opts = []
            explicit_ans = ""
            return

        opts_list = [f"{o['letter']}. {o['text']}" for o in current_opts]
        opt_map = {o["letter"]: o["text"] for o in current_opts}

        # Ưu tiên 1: option có bold hoặc highlight
        answer = ""
        for o in current_opts:
            if o["bold"] or o["highlighted"]:
                answer = f"{o['letter']}. {o['text']}"
                break

        # Ưu tiên 2: dòng đáp án tường minh
        if not answer and explicit_ans:
            letter = explicit_ans.upper()
            if letter in opt_map:
                answer = f"{letter}. {opt_map[letter]}"

        questions.append({
            "question": current_q,
            "options": opts_list,
            "answer": answer,
        })
        current_q = None
        current_opts = []
        explicit_ans = ""

    for line in rich_lines:
        text = line["text"]
        bold = line["bold"]
        highlighted = line["highlighted"]

        if not text:
            continue

        m_ans = answer_re.match(text)
        if m_ans:
            explicit_ans = m_ans.group(1)
            continue

        m_opt = option_re.match(text)
        if m_opt and current_q is not None:
            current_opts.append({
                "letter": m_opt.group(1).upper(),
                "text": m_opt.group(2).strip(),
                "bold": bold,
                "highlighted": highlighted,
            })
            continue

        m_q = question_re.match(text)
        if m_q:
            flush()
            current_q = m_q.group(1).strip()
            continue

        if current_q and not current_opts:
            current_q += " " + text

    flush()
    return questions


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python pdf_to_json.py <file.pdf> [tên_bộ_đề]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.isfile(pdf_path):
        print(f"Không tìm thấy file: {pdf_path}")
        sys.exit(1)

    section_name = (
        sys.argv[2] if len(sys.argv) > 2
        else os.path.splitext(os.path.basename(pdf_path))[0]
    )

    print(f"Đang đọc: {pdf_path}")
    rich_lines = extract_rich_lines(pdf_path)
    questions = parse_questions(rich_lines)

    total = len(questions)
    missing = sum(1 for q in questions if not q["answer"])
    print(f"Tìm được {total} câu hỏi")
    if missing:
        print(f"  ⚠ {missing} câu chưa xác định được đáp án — cần điền thủ công")

    out = {"section": section_name, "questions": questions}
    out_path = os.path.splitext(pdf_path)[0] + ".json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Đã lưu: {out_path}")


if __name__ == "__main__":
    main()
