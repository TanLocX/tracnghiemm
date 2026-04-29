"""
Tổng hợp và phân loại câu hỏi trắc nghiệm Lịch Sử Đảng theo 4 gói CLO.

Cách dùng:
  python classify_clo.py

Khi có dữ liệu mới:
  - Thêm file .json vào folder lichsudang/ (cùng cấu trúc: {question, options, answer})
  - Chạy lại script này — nó tự đọc tất cả file và phân loại lại

Output: 4 file trong lichsudang/clo/
  goi1_CLO1.json  — Kiến thức cơ bản (40% đề thi, rút 20 câu/đề)
  goi2_CLO2.json  — Phân tích thành tựu, hạn chế (20%, rút 10 câu)
  goi3_CLO3.json  — Liên hệ thực tiễn (20%, rút 10 câu)
  goi4_CLO4.json  — Tin vào đường lối, học tập, rèn luyện (20%, rút 10 câu)
"""

import json
import os
import re
import sys

LICHSUDANG_DIR = os.path.join(os.path.dirname(__file__), "lichsudang")
OUTPUT_DIR = os.path.join(LICHSUDANG_DIR, "clo")

# ── Từ khóa phân loại ──────────────────────────────────────────────────────────

# CLO3: Liên hệ thực tiễn — ưu tiên cao nhất vì từ khóa rõ ràng
CLO3_KEYWORDS = [
    "hiện nay", "ngày nay", "hiện tại", "hiện đại", "đương đại",
    "bài học", "kinh nghiệm", "rút ra", "liên hệ", "vận dụng",
    "đổi mới", "hội nhập", "công nghiệp hóa", "hiện đại hóa",
    "thực tiễn", "thực tế", "ứng dụng", "phát huy",
    "xây dựng đất nước", "phát triển đất nước", "giai đoạn hiện",
    "thế kỷ 21", "thế kỷ xxi", "cách mạng 4.0", "chuyển đổi số",
]

# CLO4: Thái độ, niềm tin vào Đảng
CLO4_KEYWORDS = [
    "vai trò lãnh đạo", "sứ mệnh lịch sử", "tính đúng đắn",
    "tính sáng suốt", "niềm tin", "tin tưởng", "tin vào",
    "tại sao đảng", "vì sao đảng", "tầm quan trọng của đảng",
    "bản chất của đảng", "mục tiêu của đảng", "lý tưởng",
    "đạo đức cách mạng", "phẩm chất", "bản lĩnh",
    "học tập và làm theo", "nêu gương", "xây dựng đảng",
    "chỉnh đốn đảng", "phòng chống tham nhũng", "tự phê bình",
    "đại đoàn kết", "khối đại đoàn kết", "đồng thuận xã hội",
]

# CLO2: Phân tích thành tựu, hạn chế
CLO2_KEYWORDS = [
    "thành tựu", "thành công", "kết quả", "thắng lợi",
    "hạn chế", "yếu kém", "sai lầm", "thiếu sót", "khuyết điểm",
    "ý nghĩa", "ý nghĩa lịch sử", "tác động", "ảnh hưởng",
    "đặc điểm", "tính chất", "đặc trưng",
    "so sánh", "phân biệt", "khác nhau", "giống nhau",
    "nguyên nhân", "lý do", "vì sao", "tại sao",
    "nội dung chính", "chủ trương", "đường lối",
    "phân tích", "đánh giá", "nhận xét",
]

# CLO1: Kiến thức cơ bản (default nếu không khớp CLO nào trên)
# — Câu hỏi về sự kiện, ngày tháng, tên người, địa điểm, văn kiện cụ thể


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def classify(question: str, options: list) -> int:
    """Trả về số gói CLO (1-4)."""
    text = normalize(question + " " + " ".join(options))

    if any(kw in text for kw in CLO3_KEYWORDS):
        return 3
    if any(kw in text for kw in CLO4_KEYWORDS):
        return 4
    if any(kw in text for kw in CLO2_KEYWORDS):
        return 2
    return 1


def load_all_questions() -> list[dict]:
    all_qs = []
    for fname in os.listdir(LICHSUDANG_DIR):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(LICHSUDANG_DIR, fname)
        with open(fpath, encoding="utf-8") as f:
            data = json.load(f)
        qs = data.get("questions", data) if isinstance(data, dict) else data
        if isinstance(qs, list):
            print(f"  Đọc {fname}: {len(qs)} câu")
            all_qs.extend(qs)
    return all_qs


def deduplicate(questions: list[dict]) -> list[dict]:
    seen = set()
    unique = []
    for q in questions:
        key = normalize(q.get("question", ""))[:120]
        if key and key not in seen:
            seen.add(key)
            unique.append(q)
    return unique


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 55)
    print("TỔNG HỢP & PHÂN LOẠI CÂU HỎI THEO MA TRẬN CLO")
    print("=" * 55)

    print("\n[1] Đọc tất cả file JSON trong lichsudang/...")
    all_qs = load_all_questions()
    print(f"  Tổng cộng: {len(all_qs)} câu (chưa lọc trùng)")

    print("\n[2] Loại bỏ câu trùng lặp...")
    unique_qs = deduplicate(all_qs)
    print(f"  Còn lại: {len(unique_qs)} câu duy nhất")

    print("\n[3] Phân loại theo CLO...")
    groups = {1: [], 2: [], 3: [], 4: []}
    for q in unique_qs:
        clo = classify(q.get("question", ""), q.get("options", []))
        groups[clo].append(q)

    clo_meta = {
        1: ("goi1_CLO1.json", "CLO1 - Kiến thức cơ bản về đường lối lãnh đạo của Đảng",
            "Gói 1 — CLO1 (40% đề thi, mỗi đề rút 20 câu)"),
        2: ("goi2_CLO2.json", "CLO2 - Phân tích thành tựu, hạn chế qua từng thời kỳ",
            "Gói 2 — CLO2 (20% đề thi, mỗi đề rút 10 câu)"),
        3: ("goi3_CLO3.json", "CLO3 - Liên hệ thực tiễn chính trị - xã hội hiện nay",
            "Gói 3 — CLO3 (20% đề thi, mỗi đề rút 10 câu)"),
        4: ("goi4_CLO4.json", "CLO4 - Tin vào đường lối, học tập và rèn luyện",
            "Gói 4 — CLO4 (20% đề thi, mỗi đề rút 10 câu)"),
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n[4] Lưu file output...\n")
    for clo_num, (fname, section, note) in clo_meta.items():
        qs = groups[clo_num]
        output = {
            "section": section,
            "note": note,
            "total": len(qs),
            "questions": qs,
        }
        fpath = os.path.join(OUTPUT_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f"  CLO{clo_num}: {len(qs):4d} câu  →  lichsudang/clo/{fname}")

    print("\n" + "=" * 55)
    print("HOÀN THÀNH!")
    print(f"  Tổng unique: {len(unique_qs)} câu")
    print(f"  Output: lichsudang/clo/")
    print()
    print("Khi có dữ liệu mới:")
    print("  1. Thêm file .json vào lichsudang/")
    print("  2. Chạy lại: python classify_clo.py")
    print("=" * 55)


if __name__ == "__main__":
    main()
