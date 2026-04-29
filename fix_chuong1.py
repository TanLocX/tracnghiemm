import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")

filepath = r"c:\vscode\code\TN_MMT\lichsudang\chuong1.json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Sửa câu 128 (index 127): chỉ giữ lại 4 options đúng, đáp án A. 1930
data[127]["options"] = ["A. 1930", "B. 1931", "C. 1936", "D. 1938"]
data[127]["answer"] = "A. 1930"

# Tạo câu 129 bị mất
cau129 = {
    "chapter": 1,
    "question": "Câu 129: So với Cương lĩnh chính trị đầu tiên của Đảng, Luận cương chính trị (10 - 1930) không có sự khác biệt về…",
    "options": [
        "A. lực lượng cách mạng",
        "B. phạm vi, quy mô",
        "C. mối quan hệ giữa nhiệm vụ dân tộc - dân chủ",
        "D. phương hướng chiến lược của cách mạng"
    ],
    "answer": "D. phương hướng chiến lược của cách mạng"
}

# Chèn câu 129 vào sau index 127
data.insert(128, cau129)

# Đánh số lại toàn bộ câu hỏi
for i, q in enumerate(data):
    q["question"] = re.sub(r'^Câu\s*\d+\s*[:\.]?\s*', f'Câu {i+1}: ', q["question"])

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Hoàn tất! Tổng: {len(data)} câu.")
