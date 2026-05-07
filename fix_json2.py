import json, copy

with open("lichsudang/file1_fixed.json", encoding="utf-8") as f:
    raw = json.load(f)

qs = raw["questions"]

def fix(i, **kwargs):
    for k, v in kwargs.items():
        qs[i][k] = v

# ── i=142: 3 options, D is "Ð). Tắt cả đều đúng." embedded in i=143 question
qs[142]["options"].append("D. Tắt cả đều đúng.")

# ── i=143: remove "Ð). Tắt cả đều đúng. " prefix from question
qs[143]["question"] = "4Nên kinh tế Việt Nam hiện nay là nên kinh tế:"

# ── i=148: D option is cut; continuation is start of i=149's question
cont_D = qs[149]["question"].split("4Nội dung")[0].strip()  # "quyền, thống nhất và..."
qs[148]["options"][-1] = qs[148]["options"][-1] + " " + cont_D
# ── i=149: fix question, fix C (cut off), add D
qs[149]["question"] = "4Nội dung nào sau đây được quy định trong Hiền pháp Nước Cộng hòa xã hội chủ nghĩa Việt Nam năm 2013 về chế độ chính trị:"
cont_C149 = qs[150]["question"].split("4Dại hội")[0].strip()  # "các cơ quan nhà nước..."
# Also split off "I„ Tất cả các đáp án." from cont_C149
if "I„" in cont_C149:
    cont_C149 = cont_C149[:cont_C149.index("I„")].strip()
elif "I. " in cont_C149:
    cont_C149 = cont_C149[:cont_C149.index("I. ")].strip()
qs[149]["options"][-1] = qs[149]["options"][-1] + " " + cont_C149
qs[149]["options"].append("D. Tất cả các đáp án.")

# ── i=150: fix question (remove continuation prefix)
qs[150]["question"] = "4Đại hội đại biểu toàn quốc lần thứ mấy của Đảng Cộng sản Việt Nam đã xác định \"Nền kinh tế thị trường định hướng xã hội chủ nghĩa ở Việt Nam là nền kinh tế vận hành đầy đủ, đồng bộ theo các quy luật của kinh tế thị trường, đồng thời đảm bảo định hướng xã hội chủ nghĩa, phù hợp với từng giai đoạn phát triển của đất nước\":"

# ── i=160: option C is cut; continuation is in i=161 question
cont_C160 = qs[161]["question"].split("3,..")[0].strip()  # "trong các đơn vị..."
qs[160]["options"][-1] = qs[160]["options"][-1] + " " + cont_C160
# ── i=161: fix question
qs[161]["question"] = "3..Chọn câu SAI khi nói về nền kinh tế kế hoạch hóa tập trung bao cấp?"

# ── i=225: fix C (append "Lênin"), add D
qs[225]["options"][-1] = qs[225]["options"][-1] + " Lênin"
qs[225]["options"].append("D. Tuyên bỏ của mặt trận Việt Minh")
# ── i=226: fix question (remove "Lênin D - Tuyên bỏ của mặt trận Việt Minh " prefix)
qs[226]["question"] = "Tính chắt xã hội Việt Nam thời kỳ Pháp thuộc là:"

# ── i=228: 7 options → split into 2 questions
# Q1 D = "D. Hội Việt Nam cách mạng thanh niên" (strip embedded text after it)
q228 = qs[228]
d_text = q228["options"][3]
d_clean = d_text[:d_text.index("Một")].strip() if "Một" in d_text else d_text
embedded_q = d_text[d_text.index("Một"):].strip() if "Một" in d_text else ""
q228["options"] = q228["options"][:3] + [d_clean]
# Extract "A. Vua Hàm Nghỉ." from embedded_q
# embedded_q = "Một trong những lãnh tụ của phong trào Cần Vương (1855 ~ 1896) là: A Vua Hàm Nghỉ."
if "A " in embedded_q:
    q_text = embedded_q[:embedded_q.index(" A ")].strip() if " A " in embedded_q else embedded_q
    a_opt = "A. " + embedded_q[embedded_q.index(" A ") + 3:].strip() if " A " in embedded_q else ""
elif ": A" in embedded_q:
    idx = embedded_q.index(": A")
    q_text = embedded_q[:idx].strip()
    a_opt = "A. " + embedded_q[idx+3:].strip()
else:
    q_text = embedded_q
    a_opt = ""
new_q228 = {
    "question": q_text,
    "options": ([a_opt] if a_opt else []) + q228["options"][4:] if len(q228["options"]) > 4 else [],
    "answer": ""
}
# q228 already trimmed; remove extra options
extra_228 = q228["options"][4:] if len(q228["options"]) > 4 else []
qs[228]["options"] = qs[228]["options"][:4]
new_q228 = {
    "question": q_text,
    "options": ([a_opt] if a_opt else []) + extra_228,
    "answer": ""
}

# ── i=229: 7 options → split
q229 = qs[229]
d229 = q229["options"][3]
# "D. Phan Bội Châu. Người chủ trương..."
if ". Người" in d229:
    d_clean229 = d229[:d229.index(". Người") + 1].strip()
    emb229 = d229[d229.index(". Người") + 2:].strip()
else:
    d_clean229 = d229
    emb229 = ""
# emb229 = "Người chủ trương dùng chủ trương cái cách, đòi Pháp trả độc lập cho Việt Nam là: A› Phan Chu Trinh."
if ": A" in emb229:
    idx229 = emb229.index(": A")
    q_text229 = emb229[:idx229].strip()
    a_opt229 = "A. " + emb229[idx229+3:].strip().lstrip("›").strip()
elif "A›" in emb229:
    idx229 = emb229.index("A›")
    q_text229 = emb229[:idx229].strip().rstrip(":").strip()
    a_opt229 = "A. " + emb229[idx229+2:].strip()
else:
    q_text229 = emb229
    a_opt229 = ""
extra_229 = q229["options"][4:]
qs[229]["options"] = [q229["options"][0], q229["options"][1], q229["options"][2], d_clean229]
new_q229 = {
    "question": q_text229,
    "options": ([a_opt229] if a_opt229 else []) + extra_229,
    "answer": ""
}

# ── i=230: 3 options, A has embedded B
# ["A. V.LLênin. L Lê Hồng Phong", "C. Nguyễn Ái Quốc.", "D. Trần Phú."]
qs[230]["options"] = [
    "A. V.I.Lênin.",
    "B. Lê Hồng Phong",
    "C. Nguyễn Ái Quốc.",
    "D. Trần Phú."
]

# ── i=231: 7 options → split
q231 = qs[231]
d231 = q231["options"][3]
# "D. Tháng 12 — 1923 Đảng Cộng sản Việt Nam ra đời..."
if "1923 " in d231:
    split_idx = d231.index("1923 ") + 4
    d_clean231 = d231[:split_idx].strip()
    emb231 = d231[split_idx:].strip()
else:
    d_clean231 = d231
    emb231 = ""
# emb231 = "Đảng Cộng sản Việt Nam ra đời là sản phẩm của sự kết hợp các yếu tô: . ChQ nghĩa Mác-Lênin..."
# option A is embedded: ". ChQ nghĩa Mác-Lênin, phong trào công nhân, phong trào yêu nước"
a_opt231 = ""
if ". Ch" in emb231:
    idx = emb231.index(". Ch")
    q_text231 = emb231[:idx].strip().rstrip(":")
    a_opt231 = "A. Ch" + emb231[idx + 4:].strip()
else:
    q_text231 = emb231
extra_231 = q231["options"][4:]
qs[231]["options"] = [q231["options"][0], q231["options"][1], q231["options"][2], d_clean231]
new_q231 = {
    "question": q_text231 + ":",
    "options": ([a_opt231] if a_opt231 else []) + extra_231,
    "answer": ""
}

# ── i=233: 7 options → split
q233 = qs[233]
d233 = q233["options"][3]
# "D. Hội nghị trung ương 9, khóa I Hội nghị thành lập Đảng..."
if "khóa I " in d233:
    split_idx = d233.index("khóa I ") + 6
    d_clean233 = d233[:split_idx].strip()
    emb233 = d233[split_idx:].strip()
else:
    d_clean233 = d233
    emb233 = ""
# emb233 = "Hội nghị thành lập Đảng (năm 1930) diễn ra ở đâu /do ai chủ trì: A„ Ở quảng Châu/ Do Lê Hỏng Phong chủ trì"
a_opt233 = ""
if ": A" in emb233:
    idx = emb233.index(": A")
    q_text233 = emb233[:idx].strip()
    a_opt233 = "A. " + emb233[idx+3:].strip().lstrip("„").strip()
else:
    q_text233 = emb233
extra_233 = q233["options"][4:]
qs[233]["options"] = [q233["options"][0], q233["options"][1], q233["options"][2], d_clean233]
new_q233 = {
    "question": q_text233,
    "options": ([a_opt233] if a_opt233 else []) + extra_233,
    "answer": ""
}

# ── i=242: 9 options → split into 3 questions
# options:
# [0] "A. Tất cả các dân tộc ở Đông Dương."
# [1] "B. Mọi giai cấp, tẳng lớp chống đế quốc Pháp. , Giai cấp vô sản và dân cày"
# [2] "D. Giai cấp Công nhân; Nông dân; binh lính và trí thức yêu nước. Về phương pháp cách mạng, Luận cương 10/1930 xác định theo con đường: A Võ trang bạo động"
# [3] "B. Trường kỳ mai phục"
# [4] "C. . Chiến tranh du kích"
# [5] "D. Đầu tranh nghị trường Địa điểm và thời gian diễn ra Đại hội lần thứ nhất của Đảng Cộng sản Đông Dương: A Ma cao /Tháng 3 năm 1935"
# [6] "B. . Hương cáng /Tháng 3 năm 1936"
# [7] "C. Tân trào /Tháng 8 năm 1945"
# [8] "D. Bắc thải/Tháng 5 năm 1951"
q242 = qs[242]
opts242 = q242["options"]

# Q1: fix B (split off ", Giai cấp vô sản và dân cày"), add C, fix D
b1_text = opts242[1]
if " , " in b1_text:
    b1_clean, c1_rest = b1_text.split(" , ", 1)
    c1 = "C. " + c1_rest.strip()
else:
    b1_clean = b1_text
    c1 = ""
# fix D (split off embedded Q2)
d1_text = opts242[2]
if ". Về " in d1_text:
    d1_clean = d1_text[:d1_text.index(". Về ") + 1].strip()
    emb_q2 = d1_text[d1_text.index(". Về ") + 2:].strip()
else:
    d1_clean = d1_text
    emb_q2 = ""
# Q2 embedded: "Về phương pháp cách mạng, Luận cương 10/1930 xác định theo con đường: A Võ trang bạo động"
a_q2 = ""
if ": A " in emb_q2:
    idx_q2 = emb_q2.index(": A ")
    q2_text = emb_q2[:idx_q2].strip()
    a_q2 = "A. " + emb_q2[idx_q2 + 4:].strip()
else:
    q2_text = emb_q2

# Q3 from opts242[5] D: split embedded Q3
d2_text = opts242[5]
if "Địa điểm" in d2_text:
    d2_clean = d2_text[:d2_text.index("Địa điểm")].rstrip().rstrip("D.").strip()
    if not d2_clean.startswith("D."):
        d2_clean = "D. " + d2_clean.lstrip(". ")
    emb_q3 = d2_text[d2_text.index("Địa điểm"):].strip()
else:
    d2_clean = d2_text
    emb_q3 = ""
# Q3: "Địa điểm và thời gian diễn ra Đại hội lần thứ nhất của Đảng Cộng sản Đông Dương: A Ma cao /Tháng 3 năm 1935"
a_q3 = ""
if ": A " in emb_q3:
    idx_q3 = emb_q3.index(": A ")
    q3_text = emb_q3[:idx_q3].strip()
    a_q3 = "A. " + emb_q3[idx_q3 + 4:].strip()
else:
    q3_text = emb_q3

# Set Q1
qs[242]["options"] = [opts242[0], b1_clean, c1, d1_clean]

# Build Q2
new_q242_2 = {
    "question": q2_text,
    "options": ([a_q2] if a_q2 else []) + [opts242[3], opts242[4], d2_clean],
    "answer": ""
}
# Build Q3
new_q242_3 = {
    "question": q3_text,
    "options": ([a_q3] if a_q3 else []) + [opts242[6], opts242[7], opts242[8]],
    "answer": ""
}

# ── Now insert the new questions in reverse order (to preserve indices)
# All insertions: after i=242 insert Q2,Q3; after i=233 insert new; after i=231 insert new;
# after i=229 insert new; after i=228 insert new
# Do in REVERSE index order so earlier insertions don't shift later ones
insertions = sorted([
    (228, new_q228),
    (229, new_q229),
    (231, new_q231),
    (233, new_q233),
    (242, new_q242_2),
    (242, new_q242_3),
], key=lambda x: -x[0])

for idx, new_q in insertions:
    qs.insert(idx + 1, new_q)

raw["questions"] = qs

with open("lichsudang/file1_fixed.json", "w", encoding="utf-8") as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

import sys
sys.stdout.reconfigure(encoding='utf-8')
total = len(qs)
wrong = [(i,q) for i,q in enumerate(qs) if len(q['options']) != 4]
print(f"Total: {total}, Wrong option count: {len(wrong)}")
for i,q in wrong:
    print(f"  i={i} opts={len(q['options'])} q={q['question'][:60]}")
