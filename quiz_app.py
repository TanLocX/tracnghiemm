import flet as ft
import random
import json
import os
import re
import sys
import datetime
import inspect

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# ── Flet Compatibility Patches ──────────────────────────────
if not hasattr(ft, "colors"):
    ft.colors = ft.Colors
if not hasattr(ft, "icons"):
    ft.icons = ft.Icons

_orig_dropdown_init = ft.Dropdown.__init__
_dd_params = set(inspect.signature(_orig_dropdown_init).parameters.keys())

def _patched_dropdown_init(self, *args, **kwargs):
    if "on_change" in kwargs and "on_change" not in _dd_params:
        kwargs["on_select"] = kwargs.pop("on_change")
    elif "on_select" in kwargs and "on_select" not in _dd_params:
        kwargs["on_change"] = kwargs.pop("on_select")
    _orig_dropdown_init(self, *args, **kwargs)

ft.Dropdown.__init__ = _patched_dropdown_init
# ─────────────────────────────────────────────────────────────

# ============================================================
# LOAD CÂU HỎI TỪ THƯ MỤC questions/ & MÔN HỌC
# ============================================================

def _parse_txt(filepath: str) -> tuple[str, list[dict]]:
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
# LỊCH SỬ HỌC TẬP (HISTORY)
# ============================================================
HISTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "history.json")

def load_history() -> list[dict]:
    if not os.path.isfile(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_history_record(record: dict):
    history = load_history()
    history.insert(0, record)
    history = history[:50]
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[WARN] Không lưu được history: {e}")

def clear_all_history():
    try:
        if os.path.isfile(HISTORY_FILE):
            os.remove(HISTORY_FILE)
    except Exception as e:
        print(f"[WARN] Không xóa được history: {e}")


# ============================================================
# THEME SYSTEM (4 PRESETS)
# ============================================================
THEMES = {
    "midnight": {
        "name": "Deep Midnight 🌙",
        "bg_main": "#0B0F19",
        "bg_surface": "#111827",
        "bg_card": "#162032",
        "bg_card_alt": "#0F172A",
        "bg_hover": "#1E2C44",
        "border_subtle": "#223147",
        "primary": "#6366F1",
        "primary_light": "#818CF8",
        "secondary": "#8B5CF6",
        "accent": "#06B6D4",
        "text_main": "#F8FAFC",
        "text_muted": "#94A3B8",
        "success": "#10B981",
        "success_bg": "#064E3B",
        "success_light": "#34D399",
        "error": "#F43F5E",
        "error_bg": "#881337",
        "error_light": "#FB7185",
        "warning": "#F59E0B",
        "warning_light": "#FBBF24",
    },
    "ocean": {
        "name": "Ocean Teal 🌊",
        "bg_main": "#05151D",
        "bg_surface": "#09222E",
        "bg_card": "#0E2F3F",
        "bg_card_alt": "#071B24",
        "bg_hover": "#154257",
        "border_subtle": "#1B475D",
        "primary": "#0EA5E9",
        "primary_light": "#38BDF8",
        "secondary": "#06B6D4",
        "accent": "#2DD4BF",
        "text_main": "#F0FDF4",
        "text_muted": "#94A3B8",
        "success": "#10B981",
        "success_bg": "#064E3B",
        "success_light": "#34D399",
        "error": "#F43F5E",
        "error_bg": "#881337",
        "error_light": "#FB7185",
        "warning": "#F59E0B",
        "warning_light": "#FBBF24",
    },
    "cyberpunk": {
        "name": "Cyberpunk Neon ⚡",
        "bg_main": "#0F071A",
        "bg_surface": "#1A0E2E",
        "bg_card": "#261342",
        "bg_card_alt": "#140A24",
        "bg_hover": "#351B5C",
        "border_subtle": "#412170",
        "primary": "#D946EF",
        "primary_light": "#F0ABFC",
        "secondary": "#8B5CF6",
        "accent": "#06B6D4",
        "text_main": "#FAF5FF",
        "text_muted": "#A8A29E",
        "success": "#10B981",
        "success_bg": "#064E3B",
        "success_light": "#34D399",
        "error": "#F43F5E",
        "error_bg": "#881337",
        "error_light": "#FB7185",
        "warning": "#F59E0B",
        "warning_light": "#FBBF24",
    },
    "light": {
        "name": "Clean Light ☀️",
        "bg_main": "#F1F5F9",
        "bg_surface": "#E2E8F0",
        "bg_card": "#FFFFFF",
        "bg_card_alt": "#F8FAFC",
        "bg_hover": "#E2E8F0",
        "border_subtle": "#CBD5E1",
        "primary": "#2563EB",
        "primary_light": "#3B82F6",
        "secondary": "#7C3AED",
        "accent": "#0284C7",
        "text_main": "#0F172A",
        "text_muted": "#64748B",
        "success": "#16A34A",
        "success_bg": "#DCFCE7",
        "success_light": "#22C55E",
        "error": "#DC2626",
        "error_bg": "#FEE2E2",
        "error_light": "#EF4444",
        "warning": "#D97706",
        "warning_light": "#F59E0B",
    },
}

OPT_COLORS  = ["#38BDF8", "#34D399", "#FBBF24", "#F472B6"]
OPT_LETTERS = ["A", "B", "C", "D"]


# ============================================================
# MAIN APPLICATION
# ============================================================
def main(page: ft.Page):
    page.title = "Trắc Nghiệm Ôn Tập & Khảo Sát Kiến Thức"
    page.window.width = 1120
    page.window.height = 790
    page.window.min_width = 880
    page.window.min_height = 620
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
        "user_answers": {},
        "history_saved": False,
        "mode": "all",
        "num_questions": 20,
        "limit_choice": "all",  # "20", "40", "50", "all"
        "clo_data": initial_clo,
        "shuffle": True,
        "review_filter": "all",
        "theme_key": "midnight",
        "font_scale": 1.0,
        "welcome_tab": "quiz",
    }

    def T():
        return THEMES[state["theme_key"]]

    def fs(base_size: int) -> int:
        return max(10, int(base_size * state["font_scale"]))

    # ── TOP BAR COMMON CONTROLS ─────────────────────────────
    def make_top_settings_bar(on_refresh_callback):
        theme_options = [ft.dropdown.Option(k, v["name"]) for k, v in THEMES.items()]
        
        def on_theme_change(e):
            val = e.control.value
            if val in THEMES:
                state["theme_key"] = val
                page.bgcolor = T()["bg_main"]
                on_refresh_callback()

        def change_font(delta):
            state["font_scale"] = round(max(0.8, min(1.35, state["font_scale"] + delta)), 2)
            on_refresh_callback()

        theme_dd = ft.Dropdown(
            value=state["theme_key"],
            options=theme_options,
            on_change=on_theme_change,
            bgcolor=T()["bg_card_alt"],
            color=T()["text_main"],
            border_color=T()["border_subtle"],
            focused_border_color=T()["primary"],
            width=180,
            text_size=12,
            content_padding=ft.padding.symmetric(horizontal=10, vertical=4),
        )

        font_minus_btn = ft.IconButton(
            icon=ft.Icons.TEXT_FIELDS_ROUNDED,
            icon_size=16,
            icon_color=T()["text_muted"],
            tooltip="Giảm cỡ chữ (A-)",
            on_click=lambda _: change_font(-0.1),
        )
        font_plus_btn = ft.IconButton(
            icon=ft.Icons.FORMAT_SIZE_ROUNDED,
            icon_size=20,
            icon_color=T()["text_main"],
            tooltip="Tăng cỡ chữ (A+)",
            on_click=lambda _: change_font(0.1),
        )

        return ft.Row(
            spacing=8,
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                theme_dd,
                ft.Container(
                    bgcolor=T()["bg_card_alt"],
                    border_radius=8,
                    border=ft.border.all(1, T()["border_subtle"]),
                    padding=ft.padding.symmetric(horizontal=4),
                    content=ft.Row(spacing=0, controls=[font_minus_btn, font_plus_btn]),
                ),
            ],
        )

    # ── NAVIGATION & VIEWS ──────────────────────────────────
    def show_welcome():
        page.clean()
        page.bgcolor = T()["bg_main"]
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

        badge_palette = [T()["accent"], T()["success_light"], T()["warning_light"], "#C084FC", "#F472B6", "#38BDF8"]
        BATCH_SEC = 50
        sec_range_rows = {}

        radio_col_controls = [
            ft.Container(
                bgcolor=T()["bg_card_alt"],
                border_radius=12,
                border=ft.border.all(1, T()["border_subtle"]),
                padding=ft.padding.symmetric(horizontal=16, vertical=10),
                content=ft.Row(
                    spacing=12,
                    controls=[
                        ft.Radio(
                            value="all",
                            label=f"Toàn bộ kho câu hỏi ({len(questions_db)} câu)",
                            label_style=ft.TextStyle(color=T()["text_main"], size=fs(15), weight=ft.FontWeight.W_500),
                            fill_color={ft.ControlState.SELECTED: T()["primary"], ft.ControlState.DEFAULT: T()["text_muted"]},
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
                                bgcolor=T()["primary"] if ck == k else T()["bg_card_alt"],
                                color=T()["text_main"] if ck == k else T()["text_muted"],
                                padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                text_style=ft.TextStyle(size=fs(12), weight=ft.FontWeight.W_500),
                                shape=ft.RoundedRectangleBorder(radius=12),
                                side=ft.BorderSide(1, T()["primary"] if ck == k else T()["border_subtle"]),
                            )
                            chip.update()
                    chip = ft.ElevatedButton(
                        rl,
                        style=ft.ButtonStyle(
                            bgcolor=T()["primary"] if rk == "all" else T()["bg_card_alt"],
                            color=T()["text_main"] if rk == "all" else T()["text_muted"],
                            padding=ft.padding.symmetric(horizontal=12, vertical=6),
                            text_style=ft.TextStyle(size=fs(12), weight=ft.FontWeight.W_500),
                            shape=ft.RoundedRectangleBorder(radius=12),
                            side=ft.BorderSide(1, T()["primary"] if rk == "all" else T()["border_subtle"]),
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
                        ft.Text("Chọn phạm vi làm bài:", size=fs(12), color=T()["text_muted"]),
                        ft.Row(spacing=6, controls=chips, wrap=True),
                    ]),
                )
                sec_range_rows[sec["key"]] = {"container": range_container, "state": batch_state, "chips": chip_refs}

            sec_card_content = [
                ft.Radio(
                    value=sec["key"],
                    label=sec["label"],
                    label_style=ft.TextStyle(color=T()["text_main"], size=fs(14), weight=ft.FontWeight.W_500),
                    fill_color={ft.ControlState.SELECTED: T()["primary"], ft.ControlState.DEFAULT: T()["text_muted"]},
                )
            ]
            if range_container:
                sec_card_content.append(range_container)

            radio_col_controls.append(
                ft.Container(
                    bgcolor=T()["bg_card_alt"],
                    border_radius=12,
                    border=ft.border.all(1, T()["border_subtle"]),
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
                    bgcolor=T()["bg_card_alt"],
                    color=T()["text_main"],
                    border_color=T()["border_subtle"],
                    focused_border_color=T()["primary"],
                    width=170,
                    text_size=fs(13),
                    content_padding=ft.padding.symmetric(horizontal=10, vertical=4),
                    disabled=True,
                )
                selected_ref = {"value": False}
                card_ref = ft.Ref[ft.Container]()

                def make_toggle(ch=ch_num, sr=selected_ref, cr=card_ref, col=color, d=dd):
                    def toggle(e):
                        sr["value"] = not sr["value"]
                        cr.current.border = ft.border.all(1.5, T()["primary"] if sr["value"] else T()["border_subtle"])
                        cr.current.bgcolor = T()["bg_hover"] if sr["value"] else T()["bg_card_alt"]
                        d.disabled = not sr["value"]
                        cr.current.update()
                        d.update()
                    return toggle

                card = ft.Container(
                    ref=card_ref,
                    bgcolor=T()["bg_card_alt"],
                    border_radius=14,
                    border=ft.border.all(1, T()["border_subtle"]),
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
                                    ft.Text(tag, size=fs(15), weight=ft.FontWeight.BOLD, color=color),
                                    ft.Text(label, size=fs(12), color=T()["text_muted"], max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
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

            # Limit choice
            limit_val = state.get("limit_choice", "all")
            if limit_val == "20":
                limit_num = 20
            elif limit_val == "40":
                limit_num = 40
            elif limit_val == "50":
                limit_num = 50
            else:
                limit_num = 99999

            if selections:
                start_quiz_clo(selections, limit_num)
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
                start_quiz(radio_val, limit_num, batch_val)

        # ── HISTORY TAB CONTENT ──
        history_list = load_history()
        history_cards = []

        total_sessions = len(history_list)
        avg_score_pct = (sum(h["pct"] for h in history_list) / total_sessions) if total_sessions > 0 else 0
        total_questions_done = sum(h["total"] for h in history_list)

        for h in history_list:
            hpct = h.get("pct", 0)
            hcolor = T()["success"] if hpct >= 80 else (T()["warning"] if hpct >= 60 else T()["error"])
            hcard = ft.Container(
                bgcolor=T()["bg_card_alt"],
                border_radius=12,
                border=ft.border.all(1, T()["border_subtle"]),
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(spacing=12, controls=[
                            ft.Container(
                                width=36, height=36,
                                border_radius=10,
                                bgcolor=f"{hcolor}22",
                                alignment=ft.Alignment(0, 0),
                                content=ft.Text(f"{int(hpct)}%", size=fs(12), color=hcolor, weight=ft.FontWeight.BOLD),
                            ),
                            ft.Column(spacing=2, controls=[
                                ft.Text(h.get("subject_label", h.get("subject", "")), size=fs(14), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                                ft.Text(f"{h.get('timestamp', '')} • {h.get('mode_label', 'Bộ đề')}", size=fs(11), color=T()["text_muted"]),
                            ]),
                        ]),
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=12, vertical=4),
                            bgcolor=T()["bg_card"],
                            border_radius=8,
                            border=ft.border.all(1, T()["border_subtle"]),
                            content=ft.Text(f"{h.get('score', 0)} / {h.get('total', 0)} câu", size=fs(13), color=T()["text_main"], weight=ft.FontWeight.W_500),
                        ),
                    ],
                ),
            )
            history_cards.append(hcard)

        def do_clear_history():
            clear_all_history()
            show_welcome()

        history_content_view = ft.Container(
            width=740,
            padding=ft.padding.all(20),
            border_radius=20,
            bgcolor=T()["bg_card"],
            border=ft.border.all(1, T()["border_subtle"]),
            content=ft.Column(
                spacing=16,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Container(
                                padding=ft.padding.all(12),
                                bgcolor=T()["bg_card_alt"],
                                border_radius=12,
                                border=ft.border.all(1, T()["border_subtle"]),
                                width=210,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2, controls=[
                                    ft.Text(str(total_sessions), size=fs(22), color=T()["primary_light"], weight=ft.FontWeight.BOLD),
                                    ft.Text("Lần làm bài", size=fs(12), color=T()["text_muted"]),
                                ]),
                            ),
                            ft.Container(
                                padding=ft.padding.all(12),
                                bgcolor=T()["bg_card_alt"],
                                border_radius=12,
                                border=ft.border.all(1, T()["border_subtle"]),
                                width=210,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2, controls=[
                                    ft.Text(f"{avg_score_pct:.1f}%", size=fs(22), color=T()["success_light"], weight=ft.FontWeight.BOLD),
                                    ft.Text("Độ chính xác TB", size=fs(12), color=T()["text_muted"]),
                                ]),
                            ),
                            ft.Container(
                                padding=ft.padding.all(12),
                                bgcolor=T()["bg_card_alt"],
                                border_radius=12,
                                border=ft.border.all(1, T()["border_subtle"]),
                                width=210,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2, controls=[
                                    ft.Text(str(total_questions_done), size=fs(22), color=T()["accent"], weight=ft.FontWeight.BOLD),
                                    ft.Text("Tổng số câu đã ôn", size=fs(12), color=T()["text_muted"]),
                                ]),
                            ),
                        ],
                    ),
                    ft.Divider(color=T()["border_subtle"], height=1),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("Lịch sử làm bài gần đây:", size=fs(15), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                            *(
                                [
                                    ft.TextButton(
                                        "Xóa lịch sử",
                                        icon=ft.Icons.DELETE_SWEEP_ROUNDED,
                                        style=ft.ButtonStyle(color=T()["error_light"]),
                                        on_click=lambda _: do_clear_history(),
                                    )
                                ]
                                if history_list else []
                            ),
                        ],
                    ),
                    ft.Container(
                        height=280,
                        content=ft.Column(
                            spacing=8,
                            scroll=ft.ScrollMode.AUTO,
                            controls=history_cards if history_cards else [
                                ft.Container(
                                    padding=ft.padding.all(30),
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Text("Chưa có lịch sử làm bài nào. Hãy bắt đầu ôn tập ngay!", color=T()["text_muted"], size=fs(14)),
                                )
                            ],
                        ),
                    ),
                ],
            ),
        )

        active_tab = state["welcome_tab"]

        def switch_tab(tab_name):
            state["welcome_tab"] = tab_name
            show_welcome()

        # Helper for Question Limit Pill Buttons
        limit_opts = [("20", "20 câu"), ("40", "40 câu"), ("50", "50 câu"), ("all", "Toàn bộ")]
        def make_limit_chip(lkey, llabel):
            is_active = (state.get("limit_choice", "all") == lkey)
            def _click_limit(e):
                state["limit_choice"] = lkey
                show_welcome()
            return ft.ElevatedButton(
                llabel,
                style=ft.ButtonStyle(
                    bgcolor=T()["primary"] if is_active else T()["bg_card_alt"],
                    color=T()["text_main"] if is_active else T()["text_muted"],
                    padding=ft.padding.symmetric(horizontal=14, vertical=6),
                    text_style=ft.TextStyle(size=fs(12), weight=ft.FontWeight.BOLD if is_active else ft.FontWeight.W_500),
                    shape=ft.RoundedRectangleBorder(radius=10),
                    side=ft.BorderSide(1, T()["primary"] if is_active else T()["border_subtle"]),
                ),
                on_click=_click_limit,
            )

        page.add(
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=[T()["bg_main"], T()["bg_surface"]],
                ),
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=16,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Container(
                            width=740,
                            padding=ft.padding.only(top=4),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row(spacing=6, controls=[
                                        ft.ElevatedButton(
                                            "Luyện tập",
                                            icon=ft.Icons.MENU_BOOK_ROUNDED,
                                            style=ft.ButtonStyle(
                                                bgcolor=T()["primary"] if active_tab == "quiz" else T()["bg_card"],
                                                color=T()["text_main"] if active_tab == "quiz" else T()["text_muted"],
                                                padding=ft.padding.symmetric(horizontal=16, vertical=8),
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                            ),
                                            on_click=lambda _: switch_tab("quiz"),
                                        ),
                                        ft.ElevatedButton(
                                            f"Lịch sử ({total_sessions})",
                                            icon=ft.Icons.INSIGHTS_ROUNDED,
                                            style=ft.ButtonStyle(
                                                bgcolor=T()["primary"] if active_tab == "history" else T()["bg_card"],
                                                color=T()["text_main"] if active_tab == "history" else T()["text_muted"],
                                                padding=ft.padding.symmetric(horizontal=16, vertical=8),
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                            ),
                                            on_click=lambda _: switch_tab("history"),
                                        ),
                                    ]),
                                    make_top_settings_bar(show_welcome),
                                ],
                            ),
                        ),

                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=24, vertical=10),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=8,
                                controls=[
                                    ft.Container(
                                        width=68, height=68,
                                        border_radius=20,
                                        gradient=ft.LinearGradient(
                                            begin=ft.Alignment(-1, -1),
                                            end=ft.Alignment(1, 1),
                                            colors=[T()["primary"], T()["secondary"]],
                                        ),
                                        content=ft.Icon(ft.Icons.SCHOOL_ROUNDED, size=36, color=T()["text_main"]),
                                        alignment=ft.Alignment(0, 0),
                                        shadow=ft.BoxShadow(
                                            spread_radius=1, blur_radius=20,
                                            color=f"{T()['primary']}66", offset=ft.Offset(0, 6)
                                        ),
                                    ),
                                    ft.Text(
                                        "HỆ THỐNG ÔN TẬP TRẮC NGHIỆM",
                                        size=fs(22),
                                        weight=ft.FontWeight.BOLD,
                                        color=T()["text_main"],
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Container(
                                        bgcolor=f"{T()['accent']}1A",
                                        border_radius=16,
                                        border=ft.border.all(1, f"{T()['accent']}55"),
                                        padding=ft.padding.symmetric(horizontal=14, vertical=4),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=6,
                                            controls=[
                                                ft.Icon(ft.Icons.LOCAL_LIBRARY_ROUNDED, size=16, color=T()["primary_light"]),
                                                ft.Text(
                                                    f"{subject_dirs[state['subject']]['label']} • {len(questions_db)} câu hỏi khả dụng",
                                                    size=fs(13), color=T()["primary_light"], weight=ft.FontWeight.W_500
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),

                        *(
                            [
                                ft.Container(
                                    width=740,
                                    padding=ft.padding.all(24),
                                    border_radius=20,
                                    bgcolor=T()["bg_card"],
                                    border=ft.border.all(1, T()["border_subtle"]),
                                    shadow=ft.BoxShadow(spread_radius=0, blur_radius=24, color="#00000055", offset=ft.Offset(0, 8)),
                                    content=ft.Column(
                                        spacing=16,
                                        controls=[
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Row(spacing=8, controls=[
                                                        ft.Icon(ft.Icons.FOLDER_SPECIAL_ROUNDED, color=T()["primary_light"], size=20),
                                                        ft.Text("Môn học:", size=fs(15), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                                                    ]),
                                                    ft.Dropdown(
                                                        value=state["subject"],
                                                        options=subj_options,
                                                        on_change=on_subject_change,
                                                        bgcolor=T()["bg_card_alt"],
                                                        color=T()["text_main"],
                                                        border_color=T()["border_subtle"],
                                                        focused_border_color=T()["primary"],
                                                        width=260,
                                                        text_size=fs(14),
                                                        content_padding=ft.padding.symmetric(horizontal=12, vertical=8),
                                                    ),
                                                ],
                                            ),
                                            ft.Divider(color=T()["border_subtle"], height=1),

                                            *(
                                                [
                                                    ft.Row(spacing=8, controls=[
                                                        ft.Icon(ft.Icons.LIST_ALT_ROUNDED, color=T()["secondary"], size=20),
                                                        ft.Text("Ôn theo từng chương:", size=fs(15), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                                                    ]),
                                                    ft.Column(spacing=8, controls=[r["card"] for r in clo_rows]),
                                                    ft.Divider(color=T()["border_subtle"], height=1),
                                                    ft.Row(spacing=8, controls=[
                                                        ft.Icon(ft.Icons.LAYERS_ROUNDED, color=T()["accent"], size=20),
                                                        ft.Text("Hoặc chọn theo bộ đề thi:", size=fs(15), color=T()["text_main"], weight=ft.FontWeight.BOLD),
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
                                                        ft.Icon(ft.Icons.LAYERS_ROUNDED, color=T()["accent"], size=20),
                                                        ft.Text("Danh sách bộ đề ôn tập:", size=fs(15), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                                                    ]),
                                                    ft.Container(
                                                        height=260,
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

                                            ft.Divider(color=T()["border_subtle"], height=1),
                                            # Number of Questions Selector (20 câu / 40 câu / 50 câu / Toàn bộ)
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Row(spacing=8, controls=[
                                                        ft.Icon(ft.Icons.TUNE_ROUNDED, color=T()["primary_light"], size=20),
                                                        ft.Text("Số lượng câu / 1 lần làm:", size=fs(14), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                                                    ]),
                                                    ft.Row(spacing=6, controls=[make_limit_chip(k, l) for k, l in limit_opts]),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),

                                ft.Container(
                                    width=740,
                                    padding=ft.padding.symmetric(horizontal=12),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                bgcolor=T()["bg_card"],
                                                border_radius=14,
                                                border=ft.border.all(1, T()["border_subtle"]),
                                                padding=ft.padding.symmetric(horizontal=14, vertical=6),
                                                content=ft.Checkbox(
                                                    label="Xáo trộn câu hỏi ngẫu nhiên",
                                                    value=state["shuffle"],
                                                    label_style=ft.TextStyle(color=T()["text_main"], size=fs(14)),
                                                    fill_color={ft.ControlState.SELECTED: T()["primary"], ft.ControlState.DEFAULT: T()["border_subtle"]},
                                                    check_color=T()["text_main"],
                                                    on_change=lambda e: state.update({"shuffle": e.control.value}),
                                                ),
                                            ),
                                            ft.Row(spacing=12, controls=[
                                                ft.OutlinedButton(
                                                    "Thoát",
                                                    icon=ft.Icons.CLOSE_ROUNDED,
                                                    style=ft.ButtonStyle(
                                                        color=T()["error_light"],
                                                        side=ft.BorderSide(1, T()["error_bg"]),
                                                        padding=ft.padding.symmetric(horizontal=20, vertical=16),
                                                        shape=ft.RoundedRectangleBorder(radius=14),
                                                        text_style=ft.TextStyle(size=fs(14), weight=ft.FontWeight.W_500),
                                                    ),
                                                    on_click=lambda _: page.window.close(),
                                                ),
                                                ft.ElevatedButton(
                                                    "BẮT ĐẦU ÔN TẬP",
                                                    icon=ft.Icons.ROCKET_LAUNCH_ROUNDED,
                                                    disabled=len(questions_db) == 0,
                                                    style=ft.ButtonStyle(
                                                        bgcolor={ft.ControlState.DEFAULT: T()["primary"], ft.ControlState.HOVERED: T()["secondary"]},
                                                        color=T()["text_main"],
                                                        padding=ft.padding.symmetric(horizontal=36, vertical=16),
                                                        shape=ft.RoundedRectangleBorder(radius=14),
                                                        text_style=ft.TextStyle(size=fs(15), weight=ft.FontWeight.BOLD, letter_spacing=0.5),
                                                        elevation=4,
                                                        shadow_color=f"{T()['primary']}88",
                                                    ),
                                                    on_click=lambda _: handle_start(),
                                                ),
                                            ]),
                                        ],
                                    ),
                                ),
                            ]
                            if active_tab == "quiz" else
                            [history_content_view]
                        ),
                        ft.Container(height=20),
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
        state["user_answers"] = {}
        state["history_saved"] = False
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
        state["user_answers"] = {}
        state["history_saved"] = False
        state["num_questions"] = len(pool)
        show_quiz()

    def start_quiz_clo(selections: list[tuple], num: int = 99999):
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
        chosen = pool[:min(num, len(pool))]
        state["questions"] = chosen
        state["current"] = 0
        state["score"] = 0
        state["selected"] = None
        state["answered"] = False
        state["results"] = []
        state["user_answers"] = {}
        state["history_saved"] = False
        state["mode"] = "chuong"
        state["num_questions"] = len(chosen)
        show_quiz()

    # ── QUIZ SCREEN ─────────────────────────────────────────
    def show_quiz():
        page.clean()
        page.bgcolor = T()["bg_main"]
        q_index = state["current"]
        q = state["questions"][q_index]
        total = state["num_questions"]
        
        if "shuffled_options" not in q:
            opts = q["options"][:]
            if state["shuffle"]:
                random.shuffle(opts)
            q["shuffled_options"] = opts
        else:
            opts = q["shuffled_options"]

        effective_answer = q["answer"]

        prev_ans = state["user_answers"].get(q_index)
        if prev_ans:
            state["answered"] = True
            state["selected"] = prev_ans["chosen"]
        else:
            state["answered"] = False
            state["selected"] = None

        progress_val = (q_index + 1) / total
        
        badge_palette = [T()["accent"], T()["success_light"], T()["warning_light"], "#C084FC", "#F472B6", "#38BDF8"]
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

        top_bar = ft.Container(
            padding=ft.padding.symmetric(horizontal=20, vertical=12),
            bgcolor=T()["bg_surface"],
            border=ft.border.only(bottom=ft.BorderSide(1, T()["border_subtle"])),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton(
                        "Quay về",
                        icon=ft.Icons.ARROW_BACK_ROUNDED,
                        style=ft.ButtonStyle(
                            bgcolor=T()["bg_card"],
                            color=T()["text_main"],
                            padding=ft.padding.symmetric(horizontal=12, vertical=6),
                            shape=ft.RoundedRectangleBorder(radius=10),
                            side=ft.BorderSide(1, T()["border_subtle"]),
                        ),
                        on_click=lambda _: show_welcome(),
                    ),
                    ft.Row(spacing=8, controls=[
                        ft.Container(
                            bgcolor=T()["bg_card"],
                            border_radius=10,
                            border=ft.border.all(1, T()["border_subtle"]),
                            padding=ft.padding.symmetric(horizontal=14, vertical=6),
                            content=ft.Text(f"Câu {q_index + 1} / {total}", size=fs(13), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                        ),
                        ft.Container(
                            bgcolor=f"{T()['success_bg']}88",
                            border_radius=10,
                            border=ft.border.all(1, T()["success"]),
                            padding=ft.padding.symmetric(horizontal=14, vertical=6),
                            content=ft.Text(f"Đúng: {state['score']}", size=fs(13), color=T()["success_light"], weight=ft.FontWeight.BOLD),
                        ),
                    ]),
                    make_top_settings_bar(show_quiz),
                ],
            ),
        )

        progress_container = ft.ProgressBar(
            value=progress_val,
            bgcolor=T()["bg_card_alt"],
            color=T()["primary"],
            height=4,
        )

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
                        content=ft.Text(_badge_label, size=fs(12), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                        bgcolor=f"{_badge_color}33",
                        border=ft.border.all(1, _badge_color),
                        padding=ft.padding.symmetric(horizontal=12, vertical=4),
                        border_radius=12,
                    ),
                    ft.Text(f"Tiến độ: {int(progress_val * 100)}%", size=fs(12), color=T()["text_muted"]),
                ],
            ),
        ]

        if q_header_text:
            question_content_controls.append(
                ft.Container(
                    bgcolor=f"{T()['primary']}18",
                    border_radius=10,
                    border=ft.border.all(1, f"{T()['primary']}44"),
                    padding=ft.padding.symmetric(horizontal=12, vertical=6),
                    content=ft.Text(q_header_text, size=fs(14), color=T()["primary_light"], weight=ft.FontWeight.BOLD),
                )
            )

        question_content_controls.append(
            ft.Text(
                q_body_text,
                size=fs(17),
                color=T()["text_main"],
                weight=ft.FontWeight.W_500,
            )
        )

        feedback_container = ft.Container(visible=False)
        
        next_btn = ft.ElevatedButton(
            "Câu tiếp theo →" if q_index + 1 < total else "Hoàn thành & Xem kết quả 🎉",
            icon=ft.Icons.NAVIGATE_NEXT_ROUNDED if q_index + 1 < total else ft.Icons.TASK_ALT_ROUNDED,
            visible=state["answered"],
            style=ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: T()["primary"], ft.ControlState.HOVERED: T()["secondary"]},
                color=T()["text_main"],
                padding=ft.padding.symmetric(horizontal=24, vertical=14),
                shape=ft.RoundedRectangleBorder(radius=12),
                text_style=ft.TextStyle(size=fs(14), weight=ft.FontWeight.BOLD),
                elevation=4,
            ),
            on_click=lambda _: next_question(),
        )

        skip_btn = ft.OutlinedButton(
            "Bỏ qua →",
            visible=not state["answered"],
            style=ft.ButtonStyle(
                color=T()["text_muted"],
                side=ft.BorderSide(1, T()["border_subtle"]),
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
                shape=ft.RoundedRectangleBorder(radius=12),
                text_style=ft.TextStyle(size=fs(13)),
            ),
            on_click=lambda _: next_question(),
        )

        prev_btn = ft.OutlinedButton(
            "← Câu trước",
            visible=q_index > 0,
            style=ft.ButtonStyle(
                color=T()["text_muted"],
                side=ft.BorderSide(1, T()["border_subtle"]),
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
                shape=ft.RoundedRectangleBorder(radius=12),
                text_style=ft.TextStyle(size=fs(13)),
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

            ans_record = {
                "question": q["question"],
                "chosen": chosen,
                "correct": correct,
                "ok": ok,
                "explanation": q.get("explanation", "")
            }
            state["user_answers"][q_index] = ans_record
            state["results"] = [state["user_answers"][i] for i in sorted(state["user_answers"].keys())]

            show_quiz()

        for idx, opt in enumerate(opts):
            letter = OPT_LETTERS[idx % len(OPT_LETTERS)]
            letter_color = OPT_COLORS[idx % len(OPT_COLORS)]

            badge_circle = ft.Container(
                width=32, height=32,
                border_radius=8,
                bgcolor=f"{letter_color}22",
                border=ft.border.all(1, letter_color),
                alignment=ft.Alignment(0, 0),
                content=ft.Text(letter, size=fs(14), color=letter_color, weight=ft.FontWeight.BOLD),
            )

            status_icon = ft.Container(visible=False)

            is_already_chosen = prev_ans and (opt.strip().lower() == prev_ans["chosen"].strip().lower())
            is_correct_opt = prev_ans and (opt.strip().lower() == effective_answer.strip().lower())

            card_bg = T()["bg_card_alt"]
            card_border = ft.border.all(1, T()["border_subtle"])
            card_opacity = 1.0
            text_col = T()["text_main"]

            if prev_ans:
                if is_correct_opt:
                    card_bg = T()["success_bg"]
                    card_border = ft.border.all(2, T()["success"])
                    status_icon.content = ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, color=T()["success_light"], size=22)
                    status_icon.visible = True
                elif is_already_chosen and not prev_ans["ok"]:
                    card_bg = T()["error_bg"]
                    card_border = ft.border.all(2, T()["error"])
                    status_icon.content = ft.Icon(ft.Icons.CANCEL_ROUNDED, color=T()["error_light"], size=22)
                    status_icon.visible = True
                else:
                    card_opacity = 0.5
                    text_col = T()["text_muted"]

            card = ft.Container(
                bgcolor=card_bg,
                border_radius=14,
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
                border=card_border,
                opacity=card_opacity,
                content=ft.Row(
                    spacing=14,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        badge_circle,
                        ft.Text(opt, size=fs(15), color=text_col, expand=True),
                        status_icon,
                    ],
                ),
                on_click=lambda e, o=opt: select_option(o),
                ink=True,
                animate=ft.Animation(150, ft.AnimationCurve.EASE_OUT) if hasattr(ft, "Animation") else ft.animation.Animation(150, ft.AnimationCurve.EASE_OUT),
            )
            option_cards.append(card)

        if prev_ans:
            ok = prev_ans["ok"]
            explanation_text = q.get("explanation", "")
            feedback_controls = []
            if ok:
                feedback_controls.append(
                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, color=T()["success_light"], size=22),
                            ft.Text("Chính xác! Chúc mừng bạn.", color=T()["success_light"], size=fs(16), weight=ft.FontWeight.BOLD),
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
                                    ft.Icon(ft.Icons.CANCEL_ROUNDED, color=T()["error_light"], size=22),
                                    ft.Text("Chưa chính xác!", color=T()["error_light"], size=fs(16), weight=ft.FontWeight.BOLD),
                                ],
                            ),
                            ft.Text(f"Đáp án đúng: {effective_answer}", color=T()["warning_light"], size=fs(15), weight=ft.FontWeight.W_500),
                        ],
                    )
                )
            if explanation_text:
                feedback_controls.append(
                    ft.Container(
                        margin=ft.margin.only(top=6),
                        padding=ft.padding.all(12),
                        bgcolor=f"{T()['bg_card_alt']}AA",
                        border_radius=8,
                        border=ft.border.all(1, T()["border_subtle"]),
                        content=ft.Column(
                            spacing=4,
                            controls=[
                                ft.Row(spacing=6, controls=[
                                    ft.Icon(ft.Icons.LIGHTBULB_ROUNDED, color=T()["warning_light"], size=16),
                                    ft.Text("Giải thích chi tiết:", size=fs(13), color=T()["warning_light"], weight=ft.FontWeight.BOLD),
                                ]),
                                ft.Text(explanation_text, size=fs(13), color=T()["text_muted"]),
                            ],
                        ),
                    )
                )
            feedback_container.content = ft.Container(
                bgcolor=f"{T()['success_bg']}33" if ok else f"{T()['error_bg']}33",
                border_radius=12,
                border=ft.border.all(1, T()["success"] if ok else T()["error"]),
                padding=ft.padding.all(14),
                content=ft.Column(spacing=6, controls=feedback_controls),
            )
            feedback_container.visible = True

        def next_question():
            if state["current"] + 1 >= state["num_questions"]:
                show_result()
            else:
                state["current"] += 1
                show_quiz()

        def prev_question():
            if state["current"] > 0:
                state["current"] -= 1
                show_quiz()

        # ── SIDEBAR QUESTION MAP GRID ──
        grid_buttons = []
        for i in range(total):
            ans_info = state["user_answers"].get(i)
            if i == q_index:
                btn_bg = T()["primary"]
                btn_color = T()["text_main"]
                border_s = ft.BorderSide(2, T()["accent"])
            elif ans_info:
                if ans_info["ok"]:
                    btn_bg = T()["success_bg"]
                    btn_color = T()["success_light"]
                    border_s = ft.BorderSide(1, T()["success"])
                else:
                    btn_bg = T()["error_bg"]
                    btn_color = T()["error_light"]
                    border_s = ft.BorderSide(1, T()["error"])
            else:
                btn_bg = T()["bg_card_alt"]
                btn_color = T()["text_muted"]
                border_s = ft.BorderSide(1, T()["border_subtle"])

            def make_direct_jump(target_i=i):
                def _jump(e):
                    state["current"] = target_i
                    show_quiz()
                return _jump

            btn = ft.Container(
                width=38, height=38,
                border_radius=9,
                bgcolor=btn_bg,
                border=ft.border.all(border_s.width, border_s.color),
                alignment=ft.Alignment(0, 0),
                ink=True,
                on_click=make_direct_jump(),
                content=ft.Text(str(i + 1), size=fs(12), color=btn_color, weight=ft.FontWeight.BOLD),
            )
            grid_buttons.append(btn)

        sidebar_map = ft.Container(
            width=270,
            bgcolor=T()["bg_card"],
            border_radius=18,
            border=ft.border.all(1, T()["border_subtle"]),
            padding=ft.padding.all(16),
            content=ft.Column(
                spacing=12,
                controls=[
                    ft.Row(
                        spacing=6,
                        controls=[
                            ft.Icon(ft.Icons.GRID_VIEW_ROUNDED, color=T()["primary_light"], size=20),
                            ft.Text("Bản đồ câu hỏi", size=fs(14), weight=ft.FontWeight.BOLD, color=T()["text_main"]),
                        ],
                    ),
                    ft.Row(
                        spacing=8,
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            ft.Row(spacing=3, controls=[
                                ft.Container(width=10, height=10, border_radius=3, bgcolor=T()["success"]),
                                ft.Text("Đúng", size=fs(11), color=T()["text_muted"]),
                            ]),
                            ft.Row(spacing=3, controls=[
                                ft.Container(width=10, height=10, border_radius=3, bgcolor=T()["error"]),
                                ft.Text("Sai", size=fs(11), color=T()["text_muted"]),
                            ]),
                            ft.Row(spacing=3, controls=[
                                ft.Container(width=10, height=10, border_radius=3, bgcolor=T()["border_subtle"]),
                                ft.Text("Chưa làm", size=fs(11), color=T()["text_muted"]),
                            ]),
                        ],
                    ),
                    ft.Divider(color=T()["border_subtle"], height=1),
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            spacing=0,
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Row(
                                    wrap=True,
                                    spacing=6,
                                    run_spacing=6,
                                    controls=grid_buttons,
                                )
                            ],
                        ),
                    ),
                    ft.Divider(color=T()["border_subtle"], height=1),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(f"Đã làm: {len(state['user_answers'])} / {total}", size=fs(11), color=T()["text_muted"]),
                            ft.Text(f"Tỷ lệ: {(state['score'] / max(1, len(state['user_answers'])) * 100):.0f}%", size=fs(11), color=T()["primary_light"], weight=ft.FontWeight.BOLD),
                        ],
                    ),
                ],
            ),
        )

        # ── QUIZ SCREEN LAYOUT (2-Column Layout) ──
        page.add(
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=[T()["bg_main"], T()["bg_surface"]],
                ),
                content=ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        top_bar,
                        progress_container,
                        ft.Container(
                            expand=True,
                            padding=ft.padding.symmetric(horizontal=20, vertical=14),
                            content=ft.Row(
                                expand=True,
                                spacing=16,
                                controls=[
                                    # Main Quiz Arena (Left Column)
                                    ft.Container(
                                        expand=True,
                                        bgcolor=T()["bg_card"],
                                        border_radius=18,
                                        border=ft.border.all(1, T()["border_subtle"]),
                                        padding=ft.padding.all(20),
                                        content=ft.Column(
                                            expand=True,
                                            spacing=14,
                                            controls=[
                                                ft.Column(spacing=10, controls=question_content_controls),
                                                ft.Divider(color=T()["border_subtle"], height=1),
                                                ft.Column(
                                                    spacing=10,
                                                    controls=option_cards,
                                                    scroll=ft.ScrollMode.AUTO,
                                                    expand=True,
                                                ),
                                                feedback_container,
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
                                    # Question Map Sidebar (Right Column)
                                    sidebar_map,
                                ],
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
        page.bgcolor = T()["bg_main"]
        total = state["num_questions"]
        results = [state["user_answers"][i] for i in sorted(state["user_answers"].keys())]
        state["results"] = results
        score = sum(1 for r in results if r["ok"])
        state["score"] = score
        pct = (score / total * 100) if total > 0 else 0

        if not state.get("history_saved"):
            now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            subj_lbl = subject_dirs.get(state["subject"], {}).get("label", state["subject"])
            history_record = {
                "subject": state["subject"],
                "subject_label": subj_lbl,
                "timestamp": now_str,
                "score": score,
                "total": total,
                "pct": round(pct, 1),
                "mode_label": "Theo chương" if state["mode"] == "chuong" else "Bộ đề thi",
            }
            save_history_record(history_record)
            state["history_saved"] = True

        if pct >= 85:
            grade_color = T()["success"]
            grade_title = "XUẤT SẮC! 🎉"
            grade_sub = "Bạn đã nắm rất vững kiến thức phần này."
            grade_icon = ft.Icons.WORKSPACE_PREMIUM_ROUNDED
        elif pct >= 65:
            grade_color = T()["accent"]
            grade_title = "KẾT QUẢ KHÁ TỐT! 👍"
            grade_sub = "Bạn đã hiểu hầu hết nội dung, hãy ôn lại câu sai nhé."
            grade_icon = ft.Icons.THUMB_UP_ROUNDED
        elif pct >= 50:
            grade_color = T()["warning"]
            grade_title = "ĐẠT YÊU CẦU 📝"
            grade_sub = "Cần ôn tập thêm các khái niệm và câu hỏi tình huống."
            grade_icon = ft.Icons.FACT_CHECK_ROUNDED
        else:
            grade_color = T()["error"]
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
            color = T()["success"] if is_ok else T()["error"]
            bg_color = f"{T()['success_bg']}44" if is_ok else f"{T()['error_bg']}44"

            ans_details = []
            if is_ok:
                ans_details.append(
                    ft.Row(
                        spacing=6,
                        controls=[
                            ft.Text("Đáp án đã chọn:", size=fs(13), color=T()["text_muted"]),
                            ft.Text(r["chosen"], size=fs(13), color=T()["success_light"], weight=ft.FontWeight.BOLD, expand=True),
                        ],
                    )
                )
            else:
                ans_details.extend([
                    ft.Row(
                        spacing=6,
                        controls=[
                            ft.Text("Bạn đã chọn:", size=fs(13), color=T()["text_muted"]),
                            ft.Text(r["chosen"], size=fs(13), color=T()["error_light"], weight=ft.FontWeight.BOLD, expand=True),
                        ],
                    ),
                    ft.Row(
                        spacing=6,
                        controls=[
                            ft.Text("Đáp án đúng:", size=fs(13), color=T()["text_muted"]),
                            ft.Text(r["correct"], size=fs(13), color=T()["success_light"], weight=ft.FontWeight.BOLD, expand=True),
                        ],
                    ),
                ])

            if r.get("explanation"):
                ans_details.append(
                    ft.Container(
                        padding=ft.padding.all(8),
                        bgcolor=T()["bg_card_alt"],
                        border_radius=8,
                        content=ft.Text(
                            f"💡 {r['explanation']}",
                            size=fs(12),
                            color=T()["text_muted"],
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
                                    size=fs(14),
                                    color=T()["text_main"],
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
                    colors=[T()["bg_main"], T()["bg_surface"]],
                ),
                padding=ft.padding.symmetric(horizontal=24, vertical=20),
                content=ft.Column(
                    expand=True,
                    spacing=16,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[make_top_settings_bar(show_result)],
                        ),
                        ft.Container(
                            bgcolor=T()["bg_card"],
                            border_radius=18,
                            border=ft.border.all(1, T()["border_subtle"]),
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
                                                    ft.Text(grade_title, size=fs(20), color=grade_color, weight=ft.FontWeight.BOLD),
                                                    ft.Text(grade_sub, size=fs(13), color=T()["text_muted"]),
                                                    ft.Container(
                                                        width=240,
                                                        content=ft.ProgressBar(
                                                            value=pct / 100,
                                                            bgcolor=T()["bg_card_alt"],
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
                                        bgcolor=T()["bg_card_alt"],
                                        border_radius=14,
                                        border=ft.border.all(1, T()["border_subtle"]),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=2,
                                            controls=[
                                                ft.Text(f"{score} / {total}", size=fs(28), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                                                ft.Text(f"Tỷ lệ: {pct:.1f}%", size=fs(14), color=T()["primary_light"], weight=ft.FontWeight.W_500),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),

                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=12,
                            controls=[
                                ft.OutlinedButton(
                                    "Thi lại toàn bộ",
                                    icon=ft.Icons.REFRESH_ROUNDED,
                                    style=ft.ButtonStyle(
                                        color=T()["primary_light"],
                                        side=ft.BorderSide(1, T()["primary"]),
                                        padding=ft.padding.symmetric(horizontal=20, vertical=14),
                                        shape=ft.RoundedRectangleBorder(radius=12),
                                        text_style=ft.TextStyle(size=fs(14), weight=ft.FontWeight.W_500),
                                    ),
                                    on_click=lambda _: start_quiz(state["mode"], state["num_questions"]),
                                ),
                                *(
                                    [
                                        ft.ElevatedButton(
                                            f"Làm lại câu sai ({wrong_count})",
                                            icon=ft.Icons.REPLAY_CIRCLE_FILLED_ROUNDED,
                                            style=ft.ButtonStyle(
                                                bgcolor=T()["error"],
                                                color=T()["text_main"],
                                                padding=ft.padding.symmetric(horizontal=24, vertical=14),
                                                shape=ft.RoundedRectangleBorder(radius=12),
                                                text_style=ft.TextStyle(size=fs(14), weight=ft.FontWeight.BOLD),
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
                                        bgcolor=T()["primary"],
                                        color=T()["text_main"],
                                        padding=ft.padding.symmetric(horizontal=24, vertical=14),
                                        shape=ft.RoundedRectangleBorder(radius=12),
                                        text_style=ft.TextStyle(size=fs(14), weight=ft.FontWeight.BOLD),
                                    ),
                                    on_click=lambda _: show_welcome(),
                                ),
                            ],
                        ),

                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Chi tiết bài làm:", size=fs(16), color=T()["text_main"], weight=ft.FontWeight.BOLD),
                                ft.Row(
                                    spacing=6,
                                    controls=[
                                        ft.ElevatedButton(
                                            f"Tất cả ({len(results)})",
                                            style=ft.ButtonStyle(
                                                bgcolor=T()["primary"] if review_filter_val == "all" else T()["bg_card"],
                                                color=T()["text_main"] if review_filter_val == "all" else T()["text_muted"],
                                                padding=ft.padding.symmetric(horizontal=12, vertical=4),
                                                text_style=ft.TextStyle(size=fs(12)),
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                            ),
                                            on_click=lambda _: set_filter("all"),
                                        ),
                                        ft.ElevatedButton(
                                            f"Câu sai ({wrong_count})",
                                            style=ft.ButtonStyle(
                                                bgcolor=T()["error"] if review_filter_val == "wrong" else T()["bg_card"],
                                                color=T()["text_main"] if review_filter_val == "wrong" else T()["text_muted"],
                                                padding=ft.padding.symmetric(horizontal=12, vertical=4),
                                                text_style=ft.TextStyle(size=fs(12)),
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                            ),
                                            on_click=lambda _: set_filter("wrong"),
                                        ),
                                        ft.ElevatedButton(
                                            f"Câu đúng ({score})",
                                            style=ft.ButtonStyle(
                                                bgcolor=T()["success"] if review_filter_val == "correct" else T()["bg_card"],
                                                color=T()["text_main"] if review_filter_val == "correct" else T()["text_muted"],
                                                padding=ft.padding.symmetric(horizontal=12, vertical=4),
                                                text_style=ft.TextStyle(size=fs(12)),
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                            ),
                                            on_click=lambda _: set_filter("correct"),
                                        ),
                                    ],
                                ),
                            ],
                        ),

                        ft.Container(
                            expand=True,
                            bgcolor=T()["bg_card"],
                            border_radius=14,
                            border=ft.border.all(1, T()["border_subtle"]),
                            padding=ft.padding.all(14),
                            content=ft.Column(
                                controls=review_cards if review_cards else [
                                    ft.Container(
                                        alignment=ft.Alignment(0, 0),
                                        padding=ft.padding.all(30),
                                        content=ft.Text("Không có câu hỏi nào trong danh mục lọc này.", color=T()["text_muted"], size=fs(14)),
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
