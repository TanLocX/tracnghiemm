import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")

filepath = r"c:\vscode\code\TN_MMT\lichsudang\chuong3.json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# === Bước 1: Sửa câu 113 (index 112) ===
q113 = data[112]
q113["options"] = ["A. Đại hội VII", "B. Đại hội VIII", "C. Đại hội IX", "D. Đại hội X"]
q113["answer"] = "D. Đại hội X"

# === Bước 2: Tạo câu 114 bị mất ===
cau114 = {
    "chapter": 3,
    "question": "Câu 114: Nhận thức về kinh tế thị trường thời kỳ đổi mới có sự thay đổi căn bản và sâu sắc khi cho rằng kinh tế thị trường không phải là cái riêng có của chủ nghĩa tư bản, mà nó còn tồn tại trong thời kỳ quá độ lên chủ nghĩa xã hội. Lập luận nào dưới đây là minh chứng chắc chắn nhất cho nhận thức trên.",
    "options": [
        "A. Kinh tế thị trường đã có mầm mống từ trong xã hội nô lệ",
        "B. Kinh tế thị trường đã hình thành trong xã hội phong kiến",
        "C. Kinh tế thị trường có lịch sử phát triển lâu dài, nhưng biểu hiện rõ rệt nhất trong chủ nghĩa tư bản đến mức chi phối toàn bộ cuộc sống con người trong xã hội đó",
        "D. Kinh tế thị trường vừa có thể liên hệ với chế độ tư hữu, vừa có thể liên hệ với chế độ công hữu và phục vụ cho chúng"
    ],
    "answer": "B. Kinh tế thị trường đã hình thành trong xã hội phong kiến"
}

# Chèn câu 114 vào sau index 112
data.insert(113, cau114)

# === Bước 3: Cập nhật đáp án câu 114-315 theo ảnh ===
correct_from_114 = [
    'B','B','A','B','D','D','D',              # 114-120
    'C','A','C','C','B','A','B','D','C','A',  # 121-130
    'A','C','B','C','A','B','A','A','B','B',  # 131-140
    'A','B','C','A','A','D','D','B','B','B',  # 141-150
    'B','D','C','C','D','D','C','C','C','A',  # 151-160
    'D','D','B','A','B','D','D','A','B','C',  # 161-170
    'D','B','B','A','A','A','D','A','D','D',  # 171-180
    'D','B','A','D','B','B','B','D','B','A',  # 181-190
    'C','B','B','D','D','A','A','B','C','C',  # 191-200
    'C','B','A','B','C','C','D','A','C','C',  # 201-210
    'D','C','C','D','D','D','C','D','A','B',  # 211-220
    'B','D','C','A','C','A','D','C','C','B',  # 221-230
    'B','D','C','A','A','B','D','D','A','A',  # 231-240
    'C','C','C','C','B','C','D','B','A','B',  # 241-250
    'D','C','D','B','B','C','A','B','D','B',  # 251-260
    'D','A','A','C','C','C','D','C','D','C',  # 261-270
    'B','D','C','C','D','B','C','A','D','B',  # 271-280
    'B','C','D','C','C','D','D','B','D','A',  # 281-290
    'C','D','C','B','D','C','B','C','D','D',  # 291-300
    'C','B','D','A','D','B','B','D','A','B',  # 301-310
    'A','D','C','B','B',                      # 311-315
]

fixed = 0
errors = []
for i, letter in enumerate(correct_from_114):
    idx = 113 + i  # câu 114 = index 113
    if idx >= len(data):
        errors.append(f"Index {idx} vượt quá file ({len(data)} câu)")
        continue
    q = data[idx]
    matched = next((opt for opt in q['options'] if opt.strip().upper().startswith(letter + '.')), None)
    if matched:
        q['answer'] = matched.strip()
        fixed += 1
    else:
        errors.append(f"Câu {idx+1}: không tìm thấy option {letter}")

# === Bước 4: Đánh số lại ===
for i, q in enumerate(data):
    q['question'] = re.sub(r'^Câu\s*\d+\s*[:\.]?\s*', f'Câu {i+1}: ', q['question'])

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Tổng câu: {len(data)}")
print(f"Đã sửa {fixed} đáp án.")
if errors:
    print("Lỗi:")
    for e in errors: print(" ", e)
