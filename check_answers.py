import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

# Đáp án đúng từ ảnh (index 0 = câu 1)
correct = [
    "C","D","C","C","B","A","D","A","D","D",  # 1-10
    "D","C","C","B","B","B","B","C","B","A",  # 11-20
    "C","D","A","C","A","B","A","D","B","B",  # 21-30
    "D","D","B","A","C","C","B","B","C","C",  # 31-40
    "B","C","D","B","A","D","C","A","B","C",  # 41-50
    "A","B","D","A","C","B","A","C","A","A",  # 51-60
    "B","C","D","A","A","C","D","C","B","B",  # 61-70
    "A","C","D","A","C","D","C","A","C","B",  # 71-80
    "B","B","B","A","B","C","C","C","B","A",  # 81-90
    "D","A","D","D","D","C","B","B","C","B",  # 91-100
    "A","C","D","A","C","A","B","D","B","B",  # 101-110
    "C","C","B","B","C","C","B","C","D","B",  # 111-120
    "A","D","B","C","A","B","C","A","D","A",  # 121-130
    "B","B","A","C","C","D","A","A","C","C",  # 131-140
    "C","B","D","A","D","D","B","A","D","C",  # 141-150
    "A","A","C","B","D","B","B","D","B","D",  # 151-160
    "B","B","B","B","A","A","C","D","A","A",  # 161-170
    "C","D","D","A","C","C","D","A","B","A",  # 171-180
    "C","B","B","A","B","C","B","B","D","C",  # 181-190
    "B","C","A","B","B","D","A","B","B","C",  # 191-200
    "D","B","A","C","B","D","A","A","A","D",  # 201-210
    "D","B","C","B","A","D","B","A","A","C",  # 211-220
    "C","B","C","A","A","C","B","A","A","B",  # 221-230
    "B","D","A","A","C","C","C","C","C","D",  # 231-240
    "A","C","A","B","B","A","B","D","D","A",  # 241-250
    "D","D","C","C","D","D","A","C","A","D",  # 251-260
    "B","C","C","C","B","A","B","C","A","A",  # 261-270
    "C","C","D","D","D","B","C","A",          # 271-278
]

filepath = r"c:\vscode\code\TN_MMT\lichsudang\chuong1.json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

errors = []
for i, q in enumerate(data):
    json_answer_raw = q.get("answer", "").strip()
    json_letter = json_answer_raw[0].upper() if json_answer_raw else "?"
    expected = correct[i] if i < len(correct) else "?"
    if json_letter != expected:
        errors.append((i+1, expected, json_letter, json_answer_raw))

if errors:
    print(f"Tìm thấy {len(errors)} câu sai đáp án:\n")
    print(f"{'Câu':<6} {'Đúng':<6} {'JSON':<6} Đáp án trong JSON")
    print("-" * 60)
    for num, exp, got, raw in errors:
        print(f"Câu {num:<4} {exp:<6} {got:<6} {raw}")
else:
    print("Tất cả đáp án khớp!")

print(f"\nTổng: {len(data)} câu trong JSON, {len(correct)} câu đúng từ ảnh.")
