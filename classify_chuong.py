"""
Phân loại câu hỏi Lịch Sử Đảng theo chương giáo trình:

  Nhập môn  — Đối tượng, chức năng, nhiệm vụ, phương pháp nghiên cứu
  Chương 1  — Đảng ra đời và lãnh đạo giành chính quyền (1930–1945)
  Chương 2  — Lãnh đạo kháng chiến, giải phóng dân tộc (1945–1975)
  Chương 3  — Quá độ lên CNXH và Đổi mới (1975–nay)

Chạy lại bất cứ lúc nào có dữ liệu mới:
  python classify_chuong.py
"""

import json, os, re, sys

LICHSUDANG_DIR = os.path.join(os.path.dirname(__file__), "lichsudang")
OUTPUT_DIR     = os.path.join(LICHSUDANG_DIR, "chuong")

# ── Nhập môn ──────────────────────────────────────────────────────────────────
INTRO_KW = [
    "đối tượng nghiên cứu", "đối tượng của môn", "chức năng của môn",
    "nhiệm vụ của môn", "phương pháp nghiên cứu", "phương pháp học tập",
    "ý nghĩa của việc học", "mục đích học", "môn học lịch sử đảng",
    "học tập lịch sử đảng", "nghiên cứu lịch sử đảng",
    "lịch sử đảng là môn", "nội dung môn học",
]

# ── Chương 3: Từ 1975 đến nay — kiểm trước Chương 2 vì có từ khóa rõ ──────────
CH3_KW = [
    "đổi mới", "công nghiệp hóa", "hiện đại hóa", "hội nhập quốc tế",
    "kinh tế thị trường", "nền kinh tế nhiều thành phần",
    "đại hội vi", "đại hội vii", "đại hội viii", "đại hội ix",
    "đại hội x", "đại hội xi", "đại hội xii", "đại hội xiii",
    "từ năm 1975", "từ 1975", "sau năm 1975", "sau giải phóng",
    "xây dựng chủ nghĩa xã hội", "quá độ lên chủ nghĩa xã hội",
    "chủ nghĩa xã hội ở việt nam", "thời kỳ đổi mới",
    "bảo vệ tổ quốc xhcn", "bảo vệ tổ quốc xã hội chủ nghĩa",
    "cương lĩnh 1991", "cương lĩnh 2011",
    "hiện nay", "ngày nay", "hiện tại",
]

# ── Chương 1: 1930–1945 ────────────────────────────────────────────────────────
CH1_KW = [
    "ra đời của đảng", "thành lập đảng", "thành lập đảng cộng sản",
    "hội nghị thành lập đảng", "tháng 2/1930", "tháng 2 năm 1930",
    "ngày 3/2/1930", "ngày 3 tháng 2", "3-2-1930",
    "cương lĩnh đầu tiên", "cương lĩnh tháng 2",
    "cương lĩnh chính trị đầu tiên",
    "xô viết nghệ tĩnh", "phong trào 1930", "phong trào 1931",
    "mặt trận việt minh", "mặt trận dân tộc thống nhất",
    "khởi nghĩa bắc sơn", "khởi nghĩa nam kỳ", "binh biến đô lương",
    "hội nghị trung ương 8", "hội nghị tw8",
    "cách mạng tháng tám", "tổng khởi nghĩa tháng 8",
    "tháng 8/1945", "tháng 8 năm 1945",
    "tuyên ngôn độc lập", "2/9/1945",
    "phong trào cách mạng 1936", "mặt trận dân chủ",
    "nguyễn ái quốc thành lập", "hội việt nam cách mạng thanh niên",
    "đông dương cộng sản đảng", "an nam cộng sản đảng",
    "đông dương cộng sản liên đoàn",
    "luận cương tháng 10", "luận cương chính trị",
    "trần phú", "cao trào cách mạng 1945",
    "cướp chính quyền", "giành chính quyền",
]

# ── Chương 2: 1945–1975 ────────────────────────────────────────────────────────
CH2_KW = [
    "kháng chiến chống pháp", "kháng chiến chống thực dân pháp",
    "kháng chiến chống mỹ", "chống đế quốc mỹ",
    "điện biên phủ", "chiến dịch điện biên",
    "hiệp định giơnevơ", "hiệp định genève", "hiệp định 1954",
    "hiệp định paris", "hiệp định paris 1973",
    "giải phóng miền nam", "thống nhất đất nước",
    "tổng tiến công 1975", "chiến dịch hồ chí minh",
    "xây dựng miền bắc xhcn", "xây dựng miền bắc",
    "đường lối kháng chiến", "toàn quốc kháng chiến",
    "lời kêu gọi toàn quốc", "toàn quốc kháng chiến 1946",
    "chiến dịch biên giới", "chiến dịch tây bắc",
    "cải cách ruộng đất", "cải tạo công thương nghiệp",
    "đại hội ii", "đại hội iii", "đại hội iv", "đại hội v",
    "hội nghị 15", "nghị quyết 15", "đồng khởi",
    "mặt trận giải phóng miền nam", "mặt trận dân tộc giải phóng",
    "tổng tiến công tết mậu thân", "mậu thân 1968",
    "chính phủ cách mạng lâm thời",
    "bảo vệ chính quyền cách mạng", "diệt giặc đói", "diệt giặc dốt",
]

# ── Năm → Chương (fallback khi không có từ khóa rõ) ───────────────────────────
def year_to_chuong(text: str) -> int | None:
    years = [int(y) for y in re.findall(r"\b(1[89]\d{2}|20\d{2})\b", text)]
    if not years:
        return None
    y_min, y_max = min(years), max(years)
    if y_max >= 1976:
        return 3
    if y_max >= 1946:
        return 2
    if y_max >= 1930 or y_min >= 1920:
        return 1
    return None


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def classify(question: str, options: list) -> int:
    text = normalize(question + " " + " ".join(options))

    if any(kw in text for kw in INTRO_KW):
        return 0
    if any(kw in text for kw in CH3_KW):
        return 3
    if any(kw in text for kw in CH1_KW):
        return 1
    if any(kw in text for kw in CH2_KW):
        return 2

    y = year_to_chuong(text)
    if y is not None:
        return y

    return 1  # default: Chương 1 (kiến thức nền)


def load_all_questions() -> list[dict]:
    all_qs = []
    for fname in os.listdir(LICHSUDANG_DIR):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(LICHSUDANG_DIR, fname)
        try:
            with open(fpath, encoding="utf-8") as f:
                data = json.load(f)
            qs = data.get("questions", data) if isinstance(data, dict) else data
            if isinstance(qs, list):
                print(f"  {fname}: {len(qs)} câu")
                all_qs.extend(qs)
        except Exception as e:
            print(f"  [WARN] {fname}: {e}")
    return all_qs


def deduplicate(questions: list[dict]) -> list[dict]:
    seen, unique = set(), []
    for q in questions:
        key = normalize(q.get("question", ""))[:120]
        if key and key not in seen:
            seen.add(key)
            unique.append(q)
    return unique


CHUONG_META = {
    0: ("chuong0_nhapmom.json",
        "Nhập môn — Đối tượng, chức năng, nhiệm vụ, phương pháp nghiên cứu",
        "#80DEEA"),
    1: ("chuong1_1930_1945.json",
        "Chương 1 — Đảng ra đời và lãnh đạo giành chính quyền (1930–1945)",
        "#64B5F6"),
    2: ("chuong2_1945_1975.json",
        "Chương 2 — Lãnh đạo kháng chiến, giải phóng dân tộc (1945–1975)",
        "#81C784"),
    3: ("chuong3_1975_nay.json",
        "Chương 3 — Lãnh đạo quá độ lên CNXH và Đổi mới (1975–nay)",
        "#FFB74D"),
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 58)
    print("PHÂN LOẠI CÂU HỎI THEO CHƯƠNG GIÁO TRÌNH LỊCH SỬ ĐẢNG")
    print("=" * 58)

    print("\n[1] Đọc tất cả file JSON trong lichsudang/...")
    all_qs = load_all_questions()
    print(f"  Tổng: {len(all_qs)} câu (chưa lọc trùng)")

    print("\n[2] Loại bỏ câu trùng...")
    unique = deduplicate(all_qs)
    print(f"  Còn: {len(unique)} câu duy nhất")

    print("\n[3] Phân loại theo chương...")
    groups = {0: [], 1: [], 2: [], 3: []}
    for q in unique:
        ch = classify(q.get("question", ""), q.get("options", []))
        groups[ch].append(q)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("\n[4] Lưu file...\n")
    for ch, (fname, section, _color) in CHUONG_META.items():
        qs = groups[ch]
        out = {"section": section, "total": len(qs), "questions": qs}
        with open(os.path.join(OUTPUT_DIR, fname), "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        label = "Nhập môn" if ch == 0 else f"Chương {ch}"
        print(f"  {label}: {len(qs):4d} câu  →  lichsudang/chuong/{fname}")

    print("\n" + "=" * 58)
    print(f"XONG! Tổng {len(unique)} câu → lichsudang/chuong/")
    print("Khi có dữ liệu mới: thêm .json vào lichsudang/ rồi chạy lại")
    print("=" * 58)


if __name__ == "__main__":
    main()
