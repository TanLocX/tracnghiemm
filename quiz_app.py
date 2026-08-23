import flet as ft
import random
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# ── Flet Compatibility Patches ──────────────────────────────
if not hasattr(ft, "colors"):
    ft.colors = ft.Colors
if not hasattr(ft, "icons"):
    ft.icons = ft.Icons
# ─────────────────────────────────────────────────────────────

# ============================================================
# LOAD CÂU HỎI TỪ THƯ MỤC questions/ & MÔN HỌC
# ============================================================

def _parse_txt(filepath: str) -> tuple[str, list[dict]]:
    """
    Đọc file .txt với định dạng:
        [Tên bộ đề]
        Câu hỏi đầu tiên?
        a. Đáp án A
        b. Đáp án B
        => a
    """
    with open(filepath, encoding="utf-8") as f:
        raw = f.read()

    lines = raw.splitlines()
    section_name = os.path.splitext(os.path.basename(filepath))[0]

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        m = re.match(r"^\[(.+)\]$", stripped)
        if m:
            section_name = m.group(1).strip()
        elif not stripped.startswith("="):
            section_name = stripped
        break

    questions: list[dict] = []
    current_q: str | None = None
    current_opts: list[tuple[str, str]] = []

    opt_re  = re.compile(r"^([a-dA-D])[.)]\s+(.+)$")
    ans_re  = re.compile(r"^=>\s*(.+)$")
    skip_re = re.compile(r"^[=\[#*-]{3,}")

    def flush(ans_raw: str):
        nonlocal current_q, current_opts
        if not current_q or not current_opts:
            current_q = None
            current_opts = []
            return
        opt_map = {letter.lower(): text for letter, text in current_opts}
        opts    = [text for _, text in current_opts]
        ans_raw_stripped = ans_raw.strip()
        if ans_raw_stripped.lower() in opt_map:
            answer = opt_map[ans_raw_stripped.lower()]
        else:
            ans_clean = re.sub(r"^[a-dA-D][.)]\s*", "", ans_raw_stripped)
            answer = ans_clean if ans_clean in opts else opts[0]
        questions.append({"question": current_q, "options": opts, "answer": answer})
        current_q = None
        current_opts = []

    for line in lines:
        line_s = line.strip()
        if not line_s or skip_re.match(line_s):
            continue

        m_ans = ans_re.match(line_s)
        if m_ans:
            flush(m_ans.group(1))
            continue

        m_opt = opt_re.match(line_s)
        if m_opt:
            if current_q is None:
                continue
            current_opts.append((m_opt.group(1), m_opt.group(2).strip()))
            continue

        clean = re.sub(r"^(câu\s+\d+\s*[:.]?\s*)", "", line_s, flags=re.IGNORECASE)
        if clean:
            current_q = clean

    return section_name, questions


def _parse_json(filepath: str) -> tuple[str, list[dict]]:
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    section_name = os.path.splitext(os.path.basename(filepath))[0]
    if isinstance(data, list):
        return section_name, data
    section_name = data.get("section", section_name)
    return section_name, data.get("questions", [])


def _extract_pdf_text(filepath: str) -> str:
    try:
        import pdfplumber
        lines = []
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text = page.extract_text(x_tolerance=2, y_tolerance=2)
                if text:
                    lines.append(text)
        return "\n".join(lines)
    except ImportError:
        pass

    try:
        from pypdf import PdfReader
        reader = PdfReader(filepath)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except ImportError:
        raise ImportError(
            "Cần cài thư viện PDF:\n"
            "  pip install pdfplumber\n"
            "hoặc\n"
            "  pip install pypdf"
        )


def _parse_pdf(filepath: str) -> tuple[str, list[dict]]:
    raw_text = _extract_pdf_text(filepath)
    import tempfile
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".txt", delete=False
    ) as tmp:
        tmp.write(raw_text)
        tmp_path = tmp.name

    try:
        section_name, questions = _parse_txt(tmp_path)
    finally:
        os.unlink(tmp_path)

    if not questions:
        return os.path.splitext(os.path.basename(filepath))[0], []

    if len(section_name) > 60 or section_name.isdigit():
        section_name = os.path.splitext(os.path.basename(filepath))[0]

    return section_name, questions


CHUONG_META = {
    1: ("Chương 1", "Đảng ra đời và lãnh đạo giành chính quyền (1930–1945)", "#38BDF8"),
    2: ("Chương 2", "Lãnh đạo kháng chiến, giải phóng dân tộc (1945–1975)", "#34D399"),
    3: ("Chương 3", "Lãnh đạo quá độ lên CNXH và Đổi mới (1975–nay)", "#FBBF24"),
    4: ("Ôn tập", "Bối cảnh xâm lược & phong trào yêu nước (1858–1929)", "#C084FC"),
    5: ("Ôn tập", "Đảng ra đời & lãnh đạo giành chính quyền (1930–1945)", "#22D3EE"),
    6: ("Ôn tập", "Kháng chiến chống Pháp & chống Mỹ (1945–1975)", "#FB923C"),
    11: ("Bổ sung C1", "Các mốc sự kiện bổ sung – Chương 1 (1919–1945)", "#F472B6"),
    12: ("Bổ sung C2", "Các mốc sự kiện bổ sung – Chương 2 (1945–1975)", "#A7F3D0"),
    13: ("Bổ sung C3", "Các mốc sự kiện bổ sung – Chương 3 (1975–nay)", "#FDE68A"),
}


def load_chuong_data(subject_dir: str) -> dict[int, list[dict]]:
    result = {}
    import re as _re
    if not os.path.isdir(subject_dir):
        return result
    for fname in sorted(os.listdir(subject_dir)):
        if not fname.endswith(".json"):
            continue
        m = _re.match(r"chuong(\d+)\.json", fname, _re.IGNORECASE)
        if m:
            ch_num = int(m.group(1))
        else:
            m = _re.match(r"bosungc(\d+).*\.json", fname, _re.IGNORECASE)
            if m:
                ch_num = 10 + int(m.group(1))
            else:
                continue
        fpath = os.path.join(subject_dir, fname)
        try:
            with open(fpath, encoding="utf-8") as f:
                data = json.load(f)
            qs = data if isinstance(data, list) else data.get("questions", [])
            for q in qs:
                q["chuong"] = ch_num
            result.setdefault(ch_num, []).extend(qs)
        except Exception as e:
            print(f"[WARN] Không đọc được {fname}: {e}")
    return result


def load_questions(dir_path: str) -> tuple[list[dict], list[dict]]:
    all_q: list[dict] = []
    sections: list[dict] = []

    if not os.path.isdir(dir_path):
        return all_q, sections

    parsers = {".json": _parse_json, ".txt": _parse_txt, ".pdf": _parse_pdf}

    for fname in sorted(os.listdir(dir_path)):
        ext = os.path.splitext(fname)[1].lower()
        if ext not in parsers:
            continue
        if fname.upper().startswith("HUONG_DAN"):
            continue
        fpath = os.path.join(dir_path, fname)
        try:
            section_name, qs = parsers[ext](fpath)
            for q in qs:
                q["section"] = section_name
            if qs:
                all_q.extend(qs)
                sections.append({
                    "key":   section_name,
                    "label": f"{section_name} ({len(qs)} câu)",
                    "count": len(qs),
                    "filename": fname
                })
        except Exception as e:
            print(f"[WARN] Không đọc được {fname}: {e}")

    return all_q, sections


# ============================================================
# MODERN DESIGN SYSTEM & COLOR PALETTE
# ============================================================
BG_MAIN       = "#0B0F19"       # Deep Cosmic Dark
BG_SURFACE    = "#111827"       # Surface Base
BG_CARD       = "#162032"       # Glass Card Base
BG_CARD_HOVER = "#1E2C44"       # Interactive Hover
BG_CARD_ALT   = "#0F172A"       # Inner Card Base

BORDER_SUBTLE = "#223147"       # Subtle border
BORDER_ACTIVE = "#6366F1"       # Indigo border focus

PRIMARY       = "#6366F1"       # Electric Indigo
PRIMARY_LIGHT = "#818CF8"       # Indigo Light
PRIMARY_DARK  = "#4F46E5"       # Indigo Dark
SECONDARY     = "#8B5CF6"       # Vivid Purple
ACCENT        = "#06B6D4"       # Cyber Cyan
ACCENT_LIGHT  = "#38BDF8"       # Sky Blue

TEXT_MAIN     = "#F8FAFC"       # Bright White
TEXT_MUTED    = "#94A3B8"       # Slate Muted
TEXT_DIM      = "#64748B"       # Slate Dim

SUCCESS       = "#10B981"       # Emerald Green
SUCCESS_BG    = "#064E3B"       # Dark Emerald
SUCCESS_LIGHT = "#34D399"       # Light Emerald

ERROR         = "#F43F5E"       # Rose Red
ERROR_BG      = "#881337"       # Dark Rose
ERROR_LIGHT   = "#FB7185"       # Light Rose

WARNING       = "#F59E0B"       # Amber Orange
WARNING_LIGHT = "#FBBF24"       # Light Amber

OPT_COLORS  = ["#38BDF8", "#34D399", "#FBBF24", "#F472B6"]
OPT_LETTERS = ["A", "B", "C", "D"]


# ============================================================
# MAIN APPLICATION
# ============================================================
def main(page: ft.Page):
    page.title = "Trắc Nghiệm Ôn Tập & Khảo Sát Kiến Thức"
    page.bgcolor = BG_MAIN
    page.window.width = 980
    page.window.height = 760
    page.window.min_width = 780
    page.window.min_height = 580
    page.padding = 0

    def on_window_event(e):
        if e.data in ("close", "destroy"):
            os._exit(0)
    page.window.on_event = on_window_event

    page.fonts = {
        "Roboto": "https://fonts.gstatic.com/s/roboto/v32/KFOmCnqEu92Fr1Mu4mxK.woff2"
    }
    page.theme = ft.Theme(font_family="Roboto")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    subject_dirs = {}
    ignore_dirs = {".git", "__pycache__", ".vscode", "assets"}
    
    for d in os.listdir(base_dir):
        dp = os.path.join(base_dir, d)
        if os.path.isdir(dp) and d not in ignore_dirs and not d.startswith("."):
            valid_files = [
                f for f in os.listdir(dp) 
                if f.endswith(('.json', '.txt', '.pdf')) and not f.upper().startswith("HUONG_DAN")
            ]
            if valid_files:
                if d == "mangmaytinh":
                    label = "Mạng Máy Tính"
                elif d == "phapluat":
                    label = "Pháp Luật Đại Cương"
                elif d == "lichsudang":
                    label = "Lịch Sử Đảng"
                else:
                    label = d.replace("_", " ").title()
                subject_dirs[d] = {"path": dp, "label": label}
            
    if not subject_dirs:
        subject_dirs["questions"] = {"path": os.path.join(base_dir, "questions"), "label": "Mạng Máy Tính"}

    initial_subj = "phapluat" if "phapluat" in subject_dirs else sorted(list(subject_dirs.keys()))[0]
    initial_q, initial_s = load_questions(subject_dirs[initial_subj]["path"])
    initial_clo = load_chuong_data(subject_dirs[initial_subj]["path"])

    # ── STATE ──────────────────────────────────────────────
    state = {
        "subject": initial_subj,
        "questions_db": initial_q,
        "sections_db": initial_s,
        "questions": [],
        "current": 0,
        "score": 0,
        "selected": None,
        "answered": False,
        "results": [],
        "mode": "all",
        "num_questions": 20,
        "clo_data": initial_clo,
        "shuffle": True,
        "review_filter": "all",
    }

    # ── NAVIGATION & VIEWS ──────────────────────────────────
    def show_welcome():
        page.clean()
        mode_ref = ft.Ref[ft.RadioGroup]()
        
        def on_subject_change(e):
            new_subj = e.control.value
            if new_subj != state["subject"]:
                state["subject"] = new_subj
                q, s = load_questions(subject_dirs[new_subj]["path"])
                state["questions_db"] = q
                state["sections_db"] = s
                state["clo_data"] = load_chuong_data(subject_dirs[new_subj]["path"])
                show_welcome()

        questions_db = state["questions_db"]
        sections_db = state["sections_db"]
        clo_data = state["clo_data"]

        badge_palette = [ACCENT_LIGHT, SUCCESS_LIGHT, WARNING_LIGHT, "#C084FC", "#F472B6", "#38BDF8"]
        BATCH_SEC = 50
        sec_range_rows = {}

        radio_col_controls = [
            ft.Container(
                bgcolor=BG_CARD_ALT,
                border_radius=12,
                border=ft.border.all(1, BORDER_SUBTLE),
                padding=ft.padding.symmetric(horizontal=16, vertical=10),
                content=ft.Row(
                    spacing=12,
                    controls=[
                        ft.Radio(
                            value="all",
                            label=f"Toàn bộ kho câu hỏi ({len(questions_db)} câu)",
                            label_style=ft.TextStyle(color=TEXT_MAIN, size=15, weight=ft.FontWeight.W_500),
                            fill_color={ft.ControlState.SELECTED: PRIMARY, ft.ControlState.DEFAULT: TEXT_MUTED},
                        ),
                    ],
                ),
            )
        ]

        for i, sec in enumerate(sections_db):
            count = sec["count"]
            batch_state = {"value": "all"}
            chip_refs = {}
            range_container = None

            if count > BATCH_SEC:
                range_opts = [("all", f"Toàn bộ ({count})")]
                for s in range(0, count, BATCH_SEC):
                    e_idx = min(s + BATCH_SEC, count)
                    range_opts.append((str(s), f"Câu {s+1}–{e_idx}"))

                def _make_chip(rk, rl, bs=batch_state, cr=chip_refs):
                    def _on_click(e, k=rk):
                        bs["value"] = k
                        for ck, chip in cr.items():
                            chip.style = ft.ButtonStyle(
                                bgcolor=PRIMARY if ck == k else BG_CARD_ALT,
                                color=TEXT_MAIN if ck == k else TEXT_MUTED,
                                padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                text_style=ft.TextStyle(size=12, weight=ft.FontWeight.W_500),
                                shape=ft.RoundedRectangleBorder(radius=12),
                                side=ft.BorderSide(1, PRIMARY if ck == k else BORDER_SUBTLE),
                            )
                            chip.update()
                    chip = ft.ElevatedButton(
                        rl,
                        style=ft.ButtonStyle(
                            bgcolor=PRIMARY if rk == "all" else BG_CARD_ALT,
                            color=TEXT_MAIN if rk == "all" else TEXT_MUTED,
                            padding=ft.padding.symmetric(horizontal=12, vertical=6),
                            text_style=ft.TextStyle(size=12, weight=ft.FontWeight.W_500),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            side=ft.BorderSide(1, PRIMARY if rk == "all" else BORDER_SUBTLE),
                        ),
                        on_click=_on_click,
                    )
                    cr[rk] = chip
                    return chip

                chips = [_make_chip(rk, rl) for rk, rl in range_opts]
                range_container = ft.Container(
                    visible=False,
                    padding=ft.padding.only(left=28, top=4, bottom=6),
                    content=ft.Column(spacing=4, controls=[
                        ft.Text("Chọn phạm vi làm bài:", size=12, color=TEXT_MUTED),
                        ft.Row(spacing=6, controls=chips, wrap=True),
                    ]),
                )
                sec_range_rows[sec["key"]] = {"container": range_container, "state": batch_state, "chips": chip_refs}

            sec_card_content = [
                ft.Radio(
                    value=sec["key"],
                    label=sec["label"],
                    label_style=ft.TextStyle(color=TEXT_MAIN, size=14, weight=ft.FontWeight.W_500),
                    fill_color={ft.ControlState.SELECTED: PRIMARY, ft.ControlState.DEFAULT: TEXT_MUTED},
                )
            ]
            if range_container:
                sec_card_content.append(range_container)

            radio_col_controls.append(
                ft.Container(
                    bgcolor=BG_CARD_ALT,
                    border_radius=12,
                    border=ft.border.all(1, BORDER_SUBTLE),
                    padding=ft.padding.symmetric(horizontal=16, vertical=10),
                    content=ft.Column(spacing=4, controls=sec_card_content),
                )
            )

        def _on_radio_change(e):
            new_val = e.control.value
            for sk, data in sec_range_rows.items():
                data["container"].visible = (sk == new_val)
                data["container"].update()

        clo_rows: list[dict] = []
        ch_icons = {
            1: ft.Icons.HISTORY_EDU_ROUNDED,
            2: ft.Icons.FLAG_ROUNDED,
            3: ft.Icons.ACCOUNT_BALANCE_ROUNDED,
            4: ft.Icons.AUTO_STORIES_ROUNDED,
            5: ft.Icons.MILITARY_TECH_ROUNDED,
            6: ft.Icons.EMOJI_EVENTS_ROUNDED
        }

        if clo_data:
            BATCH = 50
            def make_batch_options(count: int):
                opts = [ft.dropdown.Option("all", f"Tất cả ({count} câu)")]
                for s in range(0, count, BATCH):
                    e = min(s + BATCH, count)
                    opts.append(ft.dropdown.Option(str(s), f"Câu {s+1}–{e}"))
                return opts

            for ch_num, (tag, label, color) in CHUONG_META.items():
                count = len(clo_data.get(ch_num, []))
                if count == 0:
                    continue
                dd = ft.Dropdown(
                    value="all",
                    options=make_batch_options(count),
                    bgcolor=BG_CARD_ALT,
                    color=TEXT_MAIN,
                    border_color=BORDER_SUBTLE,
                    focused_border_color=PRIMARY,
                    width=170,
                    text_size=13,
                    content_padding=ft.padding.symmetric(horizontal=10, vertical=4),
                    disabled=True,
                )
                selected_ref = {"value": False}
                card_ref = ft.Ref[ft.Container]()

                def make_toggle(ch=ch_num, sr=selected_ref, cr=card_ref, col=color, d=dd):
                    def toggle(e):
                        sr["value"] = not sr["value"]
                        cr.current.border = ft.border.all(1.5, PRIMARY if sr["value"] else BORDER_SUBTLE)
                        cr.current.bgcolor = BG_CARD_HOVER if sr["value"] else BG_CARD_ALT
                        d.disabled = not sr["value"]
                        cr.current.update()
                        d.update()
                    return toggle

                card = ft.Container(
                    ref=card_ref,
                    bgcolor=BG_CARD_ALT,
                    border_radius=14,
                    border=ft.border.all(1, BORDER_SUBTLE),
                    padding=ft.padding.symmetric(horizontal=14, vertical=10),
                    on_click=make_toggle(),
                    ink=True,
                    content=ft.Row(
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                width=40, height=40,
                                border_radius=10,
                                bgcolor=f"{color}22",
                                content=ft.Icon(ch_icons.get(ch_num, ft.Icons.BOOK_ROUNDED), color=color, size=22),
                                alignment=ft.Alignment(0, 0),
                            ),
                            ft.Column(
                                spacing=2, expand=True,
                                controls=[
                                    ft.Text(tag, size=15, weight=ft.FontWeight.BOLD, color=color),
                                    ft.Text(label, size=12, color=TEXT_MUTED, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                                ],
                            ),
                            dd,
                        ],
                    ),
                )
                clo_rows.append({"ch": ch_num, "selected_ref": selected_ref, "dd": dd, "card": card})

        subj_options = [ft.dropdown.Option(k, v["label"]) for k, v in subject_dirs.items()]

        def handle_start():
            selections = []
            if clo_data:
                selections = [(r["ch"], r["dd"].value) for r in clo_rows if r["selected_ref"]["value"]]

            if selections:
                start_quiz_clo(selections)
            else:
                if not questions_db:
                    dlg = ft.AlertDialog(
                        title=ft.Text("Không có câu hỏi"),
                        content=ft.Text("Không tìm thấy câu hỏi nào trong bộ đề này."),
                        actions=[ft.TextButton("OK", on_click=lambda e: (setattr(dlg, "open", False), page.update()))],
                    )
                    page.overlay.append(dlg)
                    dlg.open = True
                    page.update()
                    return
                radio_val = mode_ref.current.value if mode_ref.current else "all"
                batch_val = "all"
                if radio_val in sec_range_rows:
                    batch_val = sec_range_rows[radio_val]["state"]["value"]
                start_quiz(radio_val, 99999, batch_val)

        # ── WELCOME SCREEN LAYOUT ──
        page.add(
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=[BG_MAIN, BG_SURFACE],
                ),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Container(height=16),
                        # Hero Header
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=24, vertical=16),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=8,
                                controls=[
                                    ft.Container(
                                        width=76, height=76,
                                        border_radius=22,
                                        gradient=ft.LinearGradient(
                                            begin=ft.Alignment(-1, -1),
                                            end=ft.Alignment(1, 1),
                                            colors=[PRIMARY, SECONDARY],
                                        ),
                                        content=ft.Icon(ft.Icons.SCHOOL_ROUNDED, size=40, color=TEXT_MAIN),
                                        alignment=ft.Alignment(0, 0),
                                        shadow=ft.BoxShadow(
                                            spread_radius=1, blur_radius=20,
                                            color=f"{PRIMARY}66", offset=ft.Offset(0, 6)
                                        ),
                                    ),
                                    ft.Text(
                                        "HỆ THỐNG ÔN TẬP TRẮC NGHIỆM",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color=TEXT_MAIN,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Container(
                                        bgcolor=f"{ACCENT}1A",
                                        border_radius=16,
                                        border=ft.border.all(1, f"{ACCENT}55"),
                                        padding=ft.padding.symmetric(horizontal=14, vertical=4),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=6,
                                            controls=[
                                                ft.Icon(ft.Icons.LOCAL_LIBRARY_ROUNDED, size=16, color=ACCENT_LIGHT),
                                                ft.Text(
                                                    f"{subject_dirs[state['subject']]['label']} • {len(questions_db)} câu hỏi khả dụng",
                                                    size=13, color=ACCENT_LIGHT, weight=ft.FontWeight.W_500
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),

                        # Main Settings Card
                        ft.Container(
                            width=740,
                            padding=ft.padding.all(24),
                            border_radius=20,
                            bgcolor=BG_CARD,
                            border=ft.border.all(1, BORDER_SUBTLE),
                            shadow=ft.BoxShadow(spread_radius=0, blur_radius=24, color="#00000055", offset=ft.Offset(0, 8)),
                            content=ft.Column(
                                spacing=18,
                                controls=[
                                    # Môn học row
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Row(spacing=8, controls=[
                                                ft.Icon(ft.Icons.FOLDER_SPECIAL_ROUNDED, color=PRIMARY_LIGHT, size=20),
                                                ft.Text("Môn học:", size=15, color=TEXT_MAIN, weight=ft.FontWeight.BOLD),
                                            ]),
                                            ft.Dropdown(
                                                value=state["subject"],
                                                options=subj_options,
                                                **( {"on_select": on_subject_change} if "on_select" in getattr(ft.Dropdown.__init__, "__code__").co_varnames else {"on_change": on_subject_change} ),
                                                bgcolor=BG_CARD_ALT,
                                                color=TEXT_MAIN,
                                                border_color=BORDER_SUBTLE,
                                                focused_border_color=PRIMARY,
                                                width=260,
                                                text_size=14,
                                                content_padding=ft.padding.symmetric(horizontal=12, vertical=8),
                                            ),
                                        ],
                                    ),
                                    ft.Divider(color=BORDER_SUBTLE, height=1),

                                    # Bộ đề / Chương
                                    *(
                                        [
                                            ft.Row(spacing=8, controls=[
                                                ft.Icon(ft.Icons.LIST_ALT_ROUNDED, color=SECONDARY, size=20),
                                                ft.Text("Ôn theo từng chương:", size=15, color=TEXT_MAIN, weight=ft.FontWeight.BOLD),
                                            ]),
                                            ft.Column(spacing=8, controls=[r["card"] for r in clo_rows]),
                                            ft.Divider(color=BORDER_SUBTLE, height=1),
                                            ft.Row(spacing=8, controls=[
                                                ft.Icon(ft.Icons.LAYERS_ROUNDED, color=ACCENT_LIGHT, size=20),
                                                ft.Text("Hoặc chọn theo bộ đề thi:", size=15, color=TEXT_MAIN, weight=ft.FontWeight.BOLD),
                                            ]),
                                            ft.Container(
                                                height=220,
                                                content=ft.RadioGroup(
                                                    ref=mode_ref,
                                                    value="all",
                                                    on_change=_on_radio_change,
                                                    content=ft.Column(
                                                        spacing=8,
                                                        controls=radio_col_controls,
                                                        scroll=ft.ScrollMode.AUTO,
                                                    ),
                                                ),
                                            ),
                                        ]
                                        if clo_data else
                                        [
                                            ft.Row(spacing=8, controls=[
                                                ft.Icon(ft.Icons.LAYERS_ROUNDED, color=ACCENT_LIGHT, size=20),
                                                ft.Text("Danh sách bộ đề ôn tập:", size=15, color=TEXT_MAIN, weight=ft.FontWeight.BOLD),
                                            ]),
                                            ft.Container(
                                                height=280,
                                                content=ft.RadioGroup(
                                                    ref=mode_ref,
                                                    value="all",
                                                    on_change=_on_radio_change,
                                                    content=ft.Column(
                                                        spacing=8,
                                                        controls=radio_col_controls,
                                                        scroll=ft.ScrollMode.AUTO,
                                                    ),
                                                ),
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                        ),

                        # Options & Start
                        ft.Container(
                            width=740,
                            padding=ft.padding.symmetric(horizontal=12),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        bgcolor=BG_CARD,
                                        border_radius=14,
                                        border=ft.border.all(1, BORDER_SUBTLE),
                                        padding=ft.padding.symmetric(horizontal=14, vertical=6),
                                        content=ft.Checkbox(
                                            label="Xáo trộn câu hỏi ngẫu nhiên",
                                            value=state["shuffle"],
                                            label_style=ft.TextStyle(color=TEXT_MAIN, size=14),
                                            fill_color={ft.ControlState.SELECTED: PRIMARY, ft.ControlState.DEFAULT: BORDER_SUBTLE},
                                            check_color=TEXT_MAIN,
                                            on_change=lambda e: state.update({"shuffle": e.control.value}),
                                        ),
                                    ),
                                    ft.Row(spacing=12, controls=[
                                        ft.OutlinedButton(
                                            "Thoát",
                                            icon=ft.Icons.CLOSE_ROUNDED,
                                            style=ft.ButtonStyle(
                                                color=ERROR_LIGHT,
                                                side=ft.BorderSide(1, ERROR_BG),
                                                padding=ft.padding.symmetric(horizontal=20, vertical=16),
                                                shape=ft.RoundedRectangleBorder(radius=14),
                                                text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_500),
                                            ),
                                            on_click=lambda _: page.window.close(),
                                        ),
                                        ft.ElevatedButton(
                                            "BẮT ĐẦU ÔN TẬP",
                                            icon=ft.Icons.ROCKET_LAUNCH_ROUNDED,
                                            disabled=len(questions_db) == 0,
                                            style=ft.ButtonStyle(
                                                bgcolor={ft.ControlState.DEFAULT: PRIMARY, ft.ControlState.HOVERED: SECONDARY},
                                                color=TEXT_MAIN,
                                                padding=ft.padding.symmetric(horizontal=36, vertical=16),
                                                shape=ft.RoundedRectangleBorder(radius=14),
                                                text_style=ft.TextStyle(size=15, weight=ft.FontWeight.BOLD, letter_spacing=0.5),
                                                elevation=4,
                                                shadow_color=f"{PRIMARY}88",
                                            ),
                                            on_click=lambda _: handle_start(),
                                        ),
                                    ]),
                                ],
                            ),
                        ),
                        ft.Container(height=30),
                    ],
                ),
            )
        )
        page.update()

    def start_quiz(mode: str, num: int, batch: str = "all"):
        if mode == "chuong":
            pool = state["questions"][:]
        elif mode == "all":
            pool = state["questions_db"][:]
        else:
            pool = [q for q in state["questions_db"] if q["section"] == mode]
        if batch != "all":
            start_idx = int(batch)
            pool = pool[start_idx:start_idx + 50]
        if state["shuffle"]:
            random.shuffle(pool)
        chosen = pool[:min(num, len(pool))]
        state["questions"] = chosen
        state["current"] = 0
        state["score"] = 0
        state["selected"] = None
        state["answered"] = False
        state["results"] = []
        state["mode"] = mode
        state["num_questions"] = len(chosen)
        show_quiz()

    def start_retry_wrong():
        wrong_texts = {r["question"] for r in state["results"] if not r["ok"]}
        pool = [q for q in state["questions"] if q["question"] in wrong_texts]
        if not pool:
            return
        if state["shuffle"]:
            random.shuffle(pool)
        state["questions"] = pool
        state["current"] = 0
        state["score"] = 0
        state["selected"] = None
        state["answered"] = False
        state["results"] = []
        state["num_questions"] = len(pool)
        show_quiz()

    def start_quiz_clo(selections: list[tuple]):
        if not selections:
            selections = [(ch, "all") for ch in state["clo_data"].keys()]
        pool = []
        for ch_num, batch_val in selections:
            qs = state["clo_data"].get(ch_num, [])[:]
            if batch_val != "all":
                start = int(batch_val)
                qs = qs[start:start + 50]
            pool.extend(qs)
        if state["shuffle"]:
            random.shuffle(pool)
        state["questions"] = pool
        state["current"] = 0
        state["score"] = 0
        state["selected"] = None
        state["answered"] = False
        state["results"] = []
        state["mode"] = "chuong"
        state["num_questions"] = len(pool)
        show_quiz()

    # ── QUIZ SCREEN ─────────────────────────────────────────
    def show_quiz():
        page.clean()
        q_index = state["current"]
        q = state["questions"][q_index]
        total = state["num_questions"]
        opts = q["options"][:]
        if state["shuffle"]:
            random.shuffle(opts)
        effective_answer = q["answer"]

        state["selected"] = None
        state["answered"] = False

        progress_val = (q_index + 1) / total
        
        # Section / Chuong Badge Info
        badge_palette = [ACCENT_LIGHT, SUCCESS_LIGHT, WARNING_LIGHT, "#C084FC", "#F472B6", "#38BDF8"]
        _ch_num = q.get("chuong")
        if _ch_num is not None and _ch_num in CHUONG_META:
            _badge_label = CHUONG_META[_ch_num][0]
            _badge_color = CHUONG_META[_ch_num][2]
        else:
            _sec_label = q.get("section", "")
            _sec_keys = [s["key"] for s in state["sections_db"]]
            _idx = _sec_keys.index(_sec_label) if _sec_label in _sec_keys else 0
            _badge_label = _sec_label
            _badge_color = badge_palette[_idx % len(badge_palette)]

        # Top Bar
        top_bar = ft.Container(
            padding=ft.padding.symmetric(horizontal=24, vertical=14),
            bgcolor=BG_SURFACE,
            border=ft.border.only(bottom=ft.BorderSide(1, BORDER_SUBTLE)),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton(
                        "Quay về",
                        icon=ft.Icons.ARROW_BACK_ROUNDED,
                        style=ft.ButtonStyle(
                            bgcolor=BG_CARD,
                            color=TEXT_MAIN,
                            padding=ft.padding.symmetric(horizontal=14, vertical=8),
                            shape=ft.RoundedRectangleBorder(radius=10),
                            side=ft.BorderSide(1, BORDER_SUBTLE),
                        ),
                        on_click=lambda _: show_welcome(),
                    ),
                    ft.Container(
                        bgcolor=BG_CARD,
                        border_radius=12,
                        border=ft.border.all(1, BORDER_SUBTLE),
                        padding=ft.padding.symmetric(horizontal=16, vertical=8),
                        content=ft.Row(spacing=8, controls=[
                            ft.Icon(ft.Icons.FORMAT_LIST_NUMBERED_ROUNDED, size=16, color=PRIMARY_LIGHT),
                            ft.Text(f"Câu {q_index + 1} / {total}", size=14, color=TEXT_MAIN, weight=ft.FontWeight.BOLD),
                        ]),
                    ),
                    ft.Container(
                        bgcolor=f"{SUCCESS_BG}88",
                        border_radius=12,
                        border=ft.border.all(1, SUCCESS),
                        padding=ft.padding.symmetric(horizontal=16, vertical=8),
                        content=ft.Row(spacing=8, controls=[
                            ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, size=16, color=SUCCESS_LIGHT),
                            ft.Text(f"Đúng: {state['score']}", size=14, color=SUCCESS_LIGHT, weight=ft.FontWeight.BOLD),
                        ]),
                    ),
                ],
            ),
        )

        progress_container = ft.ProgressBar(
            value=progress_val,
            bgcolor=BG_CARD_ALT,
            color=PRIMARY,
            height=5,
        )

        # Question Title Parsing
        raw_q_text = q["question"]
        q_lines = raw_q_text.split("\n")
        if len(q_lines) > 1:
            q_header_text = q_lines[0].strip()
            q_body_text = "\n".join(q_lines[1:]).strip()
        else:
            q_header_text = None
            q_body_text = raw_q_text.strip()

        question_content_controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Container(
                        content=ft.Text(_badge_label, size=12, color=TEXT_MAIN, weight=ft.FontWeight.BOLD),
                        bgcolor=f"{_badge_color}33",
                        border=ft.border.all(1, _badge_color),
                        padding=ft.padding.symmetric(horizontal=12, vertical=4),
                        border_radius=12,
                    ),
                    ft.Text(f"Tiến độ: {int(progress_val * 100)}%", size=12, color=TEXT_MUTED),
                ],
            ),
        ]

        if q_header_text:
            question_content_controls.append(
                ft.Container(
                    bgcolor=f"{PRIMARY}18",
                    border_radius=10,
                    border=ft.border.all(1, f"{PRIMARY}44"),
                    padding=ft.padding.symmetric(horizontal=12, vertical=6),
                    content=ft.Text(q_header_text, size=14, color=PRIMARY_LIGHT, weight=ft.FontWeight.BOLD),
                )
            )

        question_content_controls.append(
            ft.Text(
                q_body_text,
                size=18,
                color=TEXT_MAIN,
                weight=ft.FontWeight.W_500,
            )
        )

        feedback_container = ft.Container(visible=False)
        
        next_btn = ft.ElevatedButton(
            "Câu tiếp theo →" if q_index + 1 < total else "Hoàn thành & Xem kết quả 🎉",
            icon=ft.Icons.NAVIGATE_NEXT_ROUNDED if q_index + 1 < total else ft.Icons.TASK_ALT_ROUNDED,
            visible=False,
            style=ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: PRIMARY, ft.ControlState.HOVERED: SECONDARY},
                color=TEXT_MAIN,
                padding=ft.padding.symmetric(horizontal=28, vertical=16),
                shape=ft.RoundedRectangleBorder(radius=12),
                text_style=ft.TextStyle(size=15, weight=ft.FontWeight.BOLD),
                elevation=4,
            ),
            on_click=lambda _: next_question(),
        )

        skip_btn = ft.OutlinedButton(
            "Bỏ qua →",
            visible=not state["answered"],
            style=ft.ButtonStyle(
                color=TEXT_MUTED,
                side=ft.BorderSide(1, BORDER_SUBTLE),
                padding=ft.padding.symmetric(horizontal=18, vertical=14),
                shape=ft.RoundedRectangleBorder(radius=12),
                text_style=ft.TextStyle(size=14),
            ),
            on_click=lambda _: next_question(),
        )

        prev_btn = ft.OutlinedButton(
            "← Câu trước",
            visible=q_index > 0,
            style=ft.ButtonStyle(
                color=TEXT_MUTED,
                side=ft.BorderSide(1, BORDER_SUBTLE),
                padding=ft.padding.symmetric(horizontal=18, vertical=14),
                shape=ft.RoundedRectangleBorder(radius=12),
                text_style=ft.TextStyle(size=14),
            ),
            on_click=lambda _: prev_question(),
        )

        option_cards = []

        def select_option(chosen: str):
            if state["answered"]:
                return
            state["answered"] = True
            state["selected"] = chosen
            correct = effective_answer
            ok = (chosen.strip().lower() == correct.strip().lower())

            if ok:
                state["score"] += 1

            state["results"].append({
                "question": q["question"],
                "chosen": chosen,
                "correct": correct,
                "ok": ok,
                "explanation": q.get("explanation", "")
            })

            for card, opt in zip(option_cards, opts):
                is_this_correct = (opt.strip().lower() == correct.strip().lower())
                is_this_chosen = (opt.strip().lower() == chosen.strip().lower())
                
                badge_circle = card.content.controls[0]
                label_text = card.content.controls[1]
                status_icon_container = card.content.controls[2]

                if is_this_correct:
                    card.bgcolor = SUCCESS_BG
                    card.border = ft.border.all(2, SUCCESS)
                    badge_circle.bgcolor = SUCCESS
                    badge_circle.content.color = TEXT_MAIN
                    status_icon_container.content = ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, color=SUCCESS_LIGHT, size=22)
                    status_icon_container.visible = True
                    label_text.color = TEXT_MAIN
                    label_text.weight = ft.FontWeight.BOLD
                elif is_this_chosen and not ok:
                    card.bgcolor = ERROR_BG
                    card.border = ft.border.all(2, ERROR)
                    badge_circle.bgcolor = ERROR
                    badge_circle.content.color = TEXT_MAIN
                    status_icon_container.content = ft.Icon(ft.Icons.CANCEL_ROUNDED, color=ERROR_LIGHT, size=22)
                    status_icon_container.visible = True
                    label_text.color = TEXT_MAIN
                else:
                    card.bgcolor = BG_CARD_ALT
                    card.border = ft.border.all(1, BORDER_SUBTLE)
                    card.opacity = 0.5
                    label_text.color = TEXT_MUTED

                card.update()

            explanation_text = q.get("explanation", "")
            feedback_controls = []
            
            if ok:
                feedback_controls.append(
                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, color=SUCCESS_LIGHT, size=22),
                            ft.Text("Chính xác! Chúc mừng bạn.", color=SUCCESS_LIGHT, size=16, weight=ft.FontWeight.BOLD),
                        ],
                    )
                )
            else:
                feedback_controls.append(
                    ft.Column(
                        spacing=4,
                        controls=[
                            ft.Row(
                                spacing=8,
                                controls=[
                                    ft.Icon(ft.Icons.CANCEL_ROUNDED, color=ERROR_LIGHT, size=22),
                                    ft.Text("Chưa chính xác!", color=ERROR_LIGHT, size=16, weight=ft.FontWeight.BOLD),
                                ],
                            ),
                            ft.Text(f"Đáp án đúng: {correct}", color=WARNING_LIGHT, size=15, weight=ft.FontWeight.W_500),
                        ],
                    )
                )

            if explanation_text:
                feedback_controls.append(
                    ft.Container(
                        margin=ft.margin.only(top=6),
                        padding=ft.padding.all(12),
                        bgcolor=f"{BG_CARD_ALT}AA",
                        border_radius=8,
                        border=ft.border.all(1, BORDER_SUBTLE),
                        content=ft.Column(
                            spacing=4,
                            controls=[
                                ft.Row(spacing=6, controls=[
                                    ft.Icon(ft.Icons.LIGHTBULB_ROUNDED, color=WARNING_LIGHT, size=16),
                                    ft.Text("Giải thích chi tiết:", size=13, color=WARNING_LIGHT, weight=ft.FontWeight.BOLD),
                                ]),
                                ft.Text(explanation_text, size=13, color=TEXT_MUTED),
                            ],
                        ),
                    )
                )

            feedback_container.content = ft.Container(
                bgcolor=f"{SUCCESS_BG}33" if ok else f"{ERROR_BG}33",
                border_radius=12,
                border=ft.border.all(1, SUCCESS if ok else ERROR),
                padding=ft.padding.all(14),
                content=ft.Column(spacing=6, controls=feedback_controls),
            )
            feedback_container.visible = True
            feedback_container.update()

            next_btn.visible = True
            next_btn.update()
            skip_btn.visible = False
            skip_btn.update()

        for idx, opt in enumerate(opts):
            letter = OPT_LETTERS[idx % len(OPT_LETTERS)]
            letter_color = OPT_COLORS[idx % len(OPT_COLORS)]

            badge_circle = ft.Container(
                width=32, height=32,
                border_radius=8,
                bgcolor=f"{letter_color}22",
                border=ft.border.all(1, letter_color),
                alignment=ft.Alignment(0, 0),
                content=ft.Text(letter, size=14, color=letter_color, weight=ft.FontWeight.BOLD),
            )

            status_icon = ft.Container(visible=False)

            card = ft.Container(
                bgcolor=BG_CARD_ALT,
                border_radius=14,
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
                border=ft.border.all(1, BORDER_SUBTLE),
                content=ft.Row(
                    spacing=14,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        badge_circle,
                        ft.Text(opt, size=15, color=TEXT_MAIN, expand=True),
                        status_icon,
                    ],
                ),
                on_click=lambda e, o=opt: select_option(o),
                ink=True,
                animate=ft.Animation(150, ft.AnimationCurve.EASE_OUT) if hasattr(ft, "Animation") else ft.animation.Animation(150, ft.AnimationCurve.EASE_OUT),
            )
            option_cards.append(card)

        def next_question():
            if state["current"] + 1 >= state["num_questions"]:
                show_result()
            else:
                state["current"] += 1
                show_quiz()

        def prev_question():
            if state["current"] > 0:
                if state["answered"]:
                    last = state["results"].pop() if state["results"] else None
                    if last and last["ok"]:
                        state["score"] = max(0, state["score"] - 1)
                state["current"] -= 1
                show_quiz()

        # ── QUIZ SCREEN LAYOUT ──
        page.add(
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=[BG_MAIN, BG_SURFACE],
                ),
                content=ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        top_bar,
                        progress_container,
                        # Question & Options Scrollable Card Area
                        ft.Container(
                            expand=True,
                            padding=ft.padding.symmetric(horizontal=24, vertical=16),
                            content=ft.Container(
                                expand=True,
                                bgcolor=BG_CARD,
                                border_radius=18,
                                border=ft.border.all(1, BORDER_SUBTLE),
                                padding=ft.padding.all(24),
                                content=ft.Column(
                                    expand=True,
                                    spacing=16,
                                    controls=[
                                        ft.Column(spacing=12, controls=question_content_controls),
                                        ft.Divider(color=BORDER_SUBTLE, height=1),
                                        ft.Column(
                                            spacing=10,
                                            controls=option_cards,
                                            scroll=ft.ScrollMode.AUTO,
                                            expand=True,
                                        ),
                                        feedback_container,
                                        # Bottom Action Bar
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                prev_btn,
                                                ft.Row(spacing=10, controls=[skip_btn, next_btn]),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
            )
        )
        page.update()

    # ── RESULT SCREEN ────────────────────────────────────────
    def show_result():
        page.clean()
        total = state["num_questions"]
        score = state["score"]
        pct = (score / total * 100) if total > 0 else 0
        results = state["results"]

        if pct >= 85:
            grade_color = SUCCESS
            grade_title = "XUẤT SẮC! 🎉"
            grade_sub = "Bạn đã nắm rất vững kiến thức phần này."
            grade_icon = ft.Icons.WORKSPACE_PREMIUM_ROUNDED
        elif pct >= 65:
            grade_color = ACCENT_LIGHT
            grade_title = "KẾT QUẢ KHÁ TỐT! 👍"
            grade_sub = "Bạn đã hiểu hầu hết nội dung, hãy ôn lại câu sai nhé."
            grade_icon = ft.Icons.THUMB_UP_ROUNDED
        elif pct >= 50:
            grade_color = WARNING
            grade_title = "ĐẠT YÊU CẦU 📝"
            grade_sub = "Cần ôn tập thêm các khái niệm và câu hỏi tình huống."
            grade_icon = ft.Icons.FACT_CHECK_ROUNDED
        else:
            grade_color = ERROR
            grade_title = "CẦN ÔN TẬP THÊM 💡"
            grade_sub = "Hãy đọc lại tài liệu và làm lại các câu bị sai."
            grade_icon = ft.Icons.MENU_BOOK_ROUNDED

        review_filter_val = state.get("review_filter", "all")

        filtered_results = []
        for i, r in enumerate(results):
            if review_filter_val == "wrong" and r["ok"]:
                continue
            if review_filter_val == "correct" and not r["ok"]:
                continue
            filtered_results.append((i + 1, r))

        review_cards = []
        for q_num, r in filtered_results:
            is_ok = r["ok"]
            icon = ft.Icons.CHECK_CIRCLE_ROUNDED if is_ok else ft.Icons.CANCEL_ROUNDED
            color = SUCCESS if is_ok else ERROR
            bg_color = f"{SUCCESS_BG}44" if is_ok else f"{ERROR_BG}44"

            ans_details = []
            if is_ok:
                ans_details.append(
                    ft.Row(
                        spacing=6,
                        controls=[
                            ft.Text("Đáp án đã chọn:", size=13, color=TEXT_MUTED),
                            ft.Text(r["chosen"], size=13, color=SUCCESS_LIGHT, weight=ft.FontWeight.BOLD, expand=True),
                        ],
                    )
                )
            else:
                ans_details.extend([
                    ft.Row(
                        spacing=6,
                        controls=[
                            ft.Text("Bạn đã chọn:", size=13, color=TEXT_MUTED),
                            ft.Text(r["chosen"], size=13, color=ERROR_LIGHT, weight=ft.FontWeight.BOLD, expand=True),
                        ],
                    ),
                    ft.Row(
                        spacing=6,
                        controls=[
                            ft.Text("Đáp án đúng:", size=13, color=TEXT_MUTED),
                            ft.Text(r["correct"], size=13, color=SUCCESS_LIGHT, weight=ft.FontWeight.BOLD, expand=True),
                        ],
                    ),
                ])

            if r.get("explanation"):
                ans_details.append(
                    ft.Container(
                        padding=ft.padding.all(8),
                        bgcolor=BG_CARD_ALT,
                        border_radius=8,
                        content=ft.Text(
                            f"💡 {r['explanation']}",
                            size=12,
                            color=TEXT_MUTED,
                        ),
                    )
                )

            item = ft.Container(
                bgcolor=bg_color,
                border_radius=12,
                border=ft.border.all(1, f"{color}66"),
                padding=ft.padding.all(14),
                content=ft.Column(
                    spacing=6,
                    controls=[
                        ft.Row(
                            spacing=10,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                ft.Icon(icon, color=color, size=20),
                                ft.Text(
                                    f"Câu {q_num}: {r['question']}",
                                    size=14,
                                    color=TEXT_MAIN,
                                    weight=ft.FontWeight.W_500,
                                    expand=True,
                                ),
                            ],
                        ),
                        ft.Container(
                            padding=ft.padding.only(left=30),
                            content=ft.Column(spacing=4, controls=ans_details),
                        ),
                    ],
                ),
            )
            review_cards.append(item)

        def set_filter(f_val):
            state["review_filter"] = f_val
            show_result()

        wrong_count = total - score

        page.add(
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=[BG_MAIN, BG_SURFACE],
                ),
                padding=ft.padding.symmetric(horizontal=24, vertical=20),
                content=ft.Column(
                    expand=True,
                    spacing=16,
                    controls=[
                        # Hero Score Banner Card
                        ft.Container(
                            bgcolor=BG_CARD,
                            border_radius=18,
                            border=ft.border.all(1, BORDER_SUBTLE),
                            padding=ft.padding.all(20),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Row(
                                        spacing=16,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                width=68, height=68,
                                                border_radius=18,
                                                bgcolor=f"{grade_color}22",
                                                border=ft.border.all(1.5, grade_color),
                                                content=ft.Icon(grade_icon, size=36, color=grade_color),
                                                alignment=ft.Alignment(0, 0),
                                            ),
                                            ft.Column(
                                                spacing=4,
                                                controls=[
                                                    ft.Text(grade_title, size=20, color=grade_color, weight=ft.FontWeight.BOLD),
                                                    ft.Text(grade_sub, size=13, color=TEXT_MUTED),
                                                    ft.Container(
                                                        width=240,
                                                        content=ft.ProgressBar(
                                                            value=pct / 100,
                                                            bgcolor=BG_CARD_ALT,
                                                            color=grade_color,
                                                            height=6,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    ft.Container(
                                        padding=ft.padding.symmetric(horizontal=24, vertical=12),
                                        bgcolor=BG_CARD_ALT,
                                        border_radius=14,
                                        border=ft.border.all(1, BORDER_SUBTLE),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=2,
                                            controls=[
                                                ft.Text(f"{score} / {total}", size=28, color=TEXT_MAIN, weight=ft.FontWeight.BOLD),
                                                ft.Text(f"Tỷ lệ: {pct:.1f}%", size=14, color=PRIMARY_LIGHT, weight=ft.FontWeight.W_500),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),

                        # Action Buttons Row
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=12,
                            controls=[
                                ft.OutlinedButton(
                                    "Thi lại toàn bộ",
                                    icon=ft.Icons.REFRESH_ROUNDED,
                                    style=ft.ButtonStyle(
                                        color=PRIMARY_LIGHT,
                                        side=ft.BorderSide(1, PRIMARY),
                                        padding=ft.padding.symmetric(horizontal=20, vertical=14),
                                        shape=ft.RoundedRectangleBorder(radius=12),
                                        text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_500),
                                    ),
                                    on_click=lambda _: start_quiz(state["mode"], state["num_questions"]),
                                ),
                                *(
                                    [
                                        ft.ElevatedButton(
                                            f"Làm lại câu sai ({wrong_count})",
                                            icon=ft.Icons.REPLAY_CIRCLE_FILLED_ROUNDED,
                                            style=ft.ButtonStyle(
                                                bgcolor=ERROR,
                                                color=TEXT_MAIN,
                                                padding=ft.padding.symmetric(horizontal=24, vertical=14),
                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                text_style=ft.TextStyle(size=14, weight=ft.FontWeight.BOLD),
                                            ),
                                            on_click=lambda _: start_retry_wrong(),
                                        )
                                    ]
                                    if wrong_count > 0 else []
                                ),
                                ft.ElevatedButton(
                                    "Về trang chủ",
                                    icon=ft.Icons.HOME_ROUNDED,
                                    style=ft.ButtonStyle(
                                        bgcolor=PRIMARY,
                                        color=TEXT_MAIN,
                                        padding=ft.padding.symmetric(horizontal=24, vertical=14),
                                        shape=ft.RoundedRectangleBorder(radius=12),
                                        text_style=ft.TextStyle(size=14, weight=ft.FontWeight.BOLD),
                                    ),
                                    on_click=lambda _: show_welcome(),
                                ),
                            ],
                        ),

                        # Review Header with Filter Chips
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Chi tiết bài làm:", size=16, color=TEXT_MAIN, weight=ft.FontWeight.BOLD),
                                ft.Row(
                                    spacing=6,
                                    controls=[
                                        ft.ElevatedButton(
                                            f"Tất cả ({total})",
                                            style=ft.ButtonStyle(
                                                bgcolor=PRIMARY if review_filter_val == "all" else BG_CARD,
                                                color=TEXT_MAIN if review_filter_val == "all" else TEXT_MUTED,
                                                padding=ft.padding.symmetric(horizontal=12, vertical=4),
                                                text_style=ft.TextStyle(size=12),
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                            ),
                                            on_click=lambda _: set_filter("all"),
                                        ),
                                        ft.ElevatedButton(
                                            f"Câu sai ({wrong_count})",
                                            style=ft.ButtonStyle(
                                                bgcolor=ERROR if review_filter_val == "wrong" else BG_CARD,
                                                color=TEXT_MAIN if review_filter_val == "wrong" else TEXT_MUTED,
                                                padding=ft.padding.symmetric(horizontal=12, vertical=4),
                                                text_style=ft.TextStyle(size=12),
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                            ),
                                            on_click=lambda _: set_filter("wrong"),
                                        ),
                                        ft.ElevatedButton(
                                            f"Câu đúng ({score})",
                                            style=ft.ButtonStyle(
                                                bgcolor=SUCCESS if review_filter_val == "correct" else BG_CARD,
                                                color=TEXT_MAIN if review_filter_val == "correct" else TEXT_MUTED,
                                                padding=ft.padding.symmetric(horizontal=12, vertical=4),
                                                text_style=ft.TextStyle(size=12),
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                            ),
                                            on_click=lambda _: set_filter("correct"),
                                        ),
                                    ],
                                ),
                            ],
                        ),

                        # Scrollable Detailed Question Review Area
                        ft.Container(
                            expand=True,
                            bgcolor=BG_CARD,
                            border_radius=14,
                            border=ft.border.all(1, BORDER_SUBTLE),
                            padding=ft.padding.all(14),
                            content=ft.Column(
                                controls=review_cards if review_cards else [
                                    ft.Container(
                                        alignment=ft.Alignment(0, 0),
                                        padding=ft.padding.all(30),
                                        content=ft.Text("Không có câu hỏi nào trong danh mục lọc này.", color=TEXT_MUTED, size=14),
                                    )
                                ],
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                expand=True,
                            ),
                        ),
                    ],
                ),
            )
        )
        page.update()

    show_welcome()


if __name__ == "__main__":
    if "PORT" in os.environ:
        port = int(os.environ["PORT"])
        ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=port, host="0.0.0.0")
    else:
        ft.app(target=main)
