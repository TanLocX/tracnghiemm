import json

with open("lichsudang/file1_fixed.json", encoding="utf-8") as f:
    raw = json.load(f)

qs = raw["questions"]

# ─── i=147: D option cut at "có chủ"; continuation is i=148's question prefix
qs[147]["options"][3] = (
    "D. Nước Cộng hoà xã hội chủ nghĩa Việt Nam là một nước độc lập, có chủ "
    "quyền, thống nhất và toàn vẹn lãnh thổ, bao gồm đất liền, hải đảo, vùng biển và vùng trời."
)

# ─── i=148: fix question + fix C (append continuation) + add D
qs[148]["question"] = (
    "4Nội dung nào sau đây được quy định trong Hiến pháp Nước Cộng hòa "
    "xã hội chủ nghĩa Việt Nam năm 2013 về chế độ chính trị:"
)
qs[148]["options"][2] = (
    "C. Quyền lực nhà nước là thống nhất, có sự phân công, phối hợp, kiềm soát "
    "giữa các cơ quan nhà nước trong việc thực hiện các quyền lập pháp, hành pháp, tư pháp."
)
qs[148]["options"].append("D. Tất cả các đáp án.")

# ─── i=149: fix question + options (currently scrambled by previous script)
qs[149]["question"] = (
    "4Đại hội đại biểu toàn quốc lần thứ mấy của Đảng Cộng sản Việt Nam đã xác định "
    "\"Nền kinh tế thị trường định hướng xã hội chủ nghĩa ở Việt Nam là nền kinh tế vận hành "
    "đầy đủ, đồng bộ theo các quy luật của kinh tế thị trường, đồng thời đảm bảo định hướng "
    "xã hội chủ nghĩa, phù hợp với từng giai đoạn phát triển của đất nước\":"
)
qs[149]["options"] = [
    "A. Đại hội VI (1986).",
    "B. Đại hội X (2006).",
    "C. Đại hội XI (2011).",
    "D. Đại hội XII (2016)."
]

# ─── i=150: fix question (currently has wrong question text for its options)
qs[150]["question"] = "4Nội dung nào sau đây được quy định trong Hiến pháp Nước Cộng hòa xã hội chủ nghĩa Việt Nam năm 2013:"

# ─── i=229: add missing B, C, D options (Cần Vương question)
qs[229]["options"] = [
    "A. Vua Hàm Nghi.",
    "B. Phan Bội Châu.",
    "C. Phan Chu Trinh.",
    "D. Hoàng Hoa Thám."
]

# ─── i=234: fix option A ("ChQ" → "Chủ")
qs[234]["options"][0] = "A. Chủ nghĩa Mác-Lênin, phong trào công nhân, phong trào yêu nước"

with open("lichsudang/file1_fixed.json", "w", encoding="utf-8") as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

import sys
sys.stdout.reconfigure(encoding='utf-8')
wrong = [(i,q) for i,q in enumerate(qs) if len(q['options']) != 4]
print(f"Total: {len(qs)}, Questions with wrong option count: {len(wrong)}")
for i,q in wrong:
    print(f"  i={i} opts={len(q['options'])} q={q['question'][:70]}")
