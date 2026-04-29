import json
import re
import sys

# Đảm bảo in tiếng Việt ra Terminal không bị lỗi
sys.stdout.reconfigure(encoding="utf-8")

filepath = r"c:\vscode\code\TN_MMT\lichsudang\917_cau_trac_nghiem.json"
filepath = r"c:\vscode\code\TN_MMT\lichsudang\chuong\917_cau_trac_nghiem.json"

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Xử lý cả 2 dạng file: file là một danh sách, hoặc file là một object chứa danh sách câu hỏi
questions = data if isinstance(data, list) else data.get("questions", [])
for i, q in enumerate(questions):
    old_q = q.get("question", "")
    # Xóa số thứ tự bị lộn xộn cũ và thay bằng số thứ tự tuần tự
    new_q = re.sub(r'^\s*(Câu\s*\d+\s*[:\.\-]\s*|\d+\s*[\.\:\-]\s*)', f'Câu {i+1}: ', old_q, flags=re.IGNORECASE)
    q["question"] = new_q

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Hoàn tất! Đã tự động đánh số lại từ 1 đến {len(questions)} cho file JSON.")