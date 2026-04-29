import json, sys
sys.stdout.reconfigure(encoding="utf-8")

correct = [
    "B","C","B","B","A","B","D","A","A","B",  # 1-10
    "D","B","A","A","C","B","A","A","A","D",  # 11-20
    "C","C","C","B","D","C","B","B","A","A",  # 21-30
    "D","D","D","C","B","D","C","B","A","D",  # 31-40
    "C","C","B","A","C","B","B","D","A","B",  # 41-50
    "C","B","A","C","B","B","D","A","B","A",  # 51-60
    "D","C","A","C","A","D","C","B","B","D",  # 61-70
    "C","B","D","D","B","C","A","D","C","B",  # 71-80
    "D","D","B","A","C","B","A","C","D","D",  # 81-90
    "B","C","A","C","A","D","B","D","D","C",  # 91-100
    "C","C","D","D","D","B","D","D","B","D",  # 101-110
    "B","A","B","D","B","B","B","C","B","C",  # 111-120
    "B","A","A","A","A","D","D","D","D","B",  # 121-130
    "A","B","A","D","C","B","A","B","C","C",  # 131-140
    "B","A","B","D","C","B","D","D","D","D",  # 141-150
    "B","C","D","D","D","B","C","D","D","A",  # 151-160
    "C","B","A","A","D","B","D","D","C","A",  # 161-170
    "A","C","D","D","B","A","C","B","D","D",  # 171-180
    "C","A","C","B","D","B","A","D","D","B",  # 181-190
    "A","A","B","D","A","A","A","A","C","C",  # 191-200
    "C","B","D","C","D","D","C","A","D","C",  # 201-210
    "A","C","C","A","C","C","A","D","B","A",  # 211-220
    "A","D","C","C","C","A","D","C","D","B",  # 221-230
    "B","C","C","C","C","A","B","D","C","A",  # 231-240
    "B","A","B","B","C","D","D","C","A","A",  # 241-250
    "B","D","D","C","C","B","A","B","A","B",  # 251-260
    "A","D","A","A","D","C","C","A","C","D",  # 261-270
    "B","D","C","D","B","A","B","B","D","D",  # 271-280
    "D","A","D","D","C","B","B","D","B","B",  # 281-290
    "A","D","B","C","C","D","A","D","B","C",  # 291-300
    "C","D","B","A",                          # 301-304
]

filepath = r"c:\vscode\code\TN_MMT\lichsudang\chuong2.json"
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
        print(f"Câu {num:<4} {exp:<6} {got:<6} {raw[:60]}")
else:
    print("Tất cả đáp án khớp!")

print(f"\nTổng: {len(data)} câu trong JSON, {len(correct)} câu đúng từ ảnh.")
