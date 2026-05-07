import fitz
import json
import re

doc = fitz.open(r'C:\Users\Admin\Downloads\LSD\file4.pdf')

# Gom toàn bộ text
all_text = ''
for i in range(len(doc)):
    all_text += doc[i].get_text()

# Chuẩn hóa: gộp dòng bị xuống dòng giữa câu
# Thay \n không phải đầu option/câu hỏi mới bằng dấu cách
lines = all_text.split('\n')
merged = []
for line in lines:
    line = line.strip()
    if not line:
        merged.append('')
        continue
    # Đầu câu hỏi: số + dấu chấm
    if re.match(r'^\d+\.', line):
        merged.append('\n' + line)
    # Đầu option: a. b. c. d.
    elif re.match(r'^[abcd]\.', line):
        merged.append('\n' + line)
    else:
        # Nối vào dòng trước
        if merged:
            merged[-1] = merged[-1] + ' ' + line
        else:
            merged.append(line)

text = '\n'.join(merged)

# Parse từng câu hỏi
questions = []
# Pattern: số thứ tự + nội dung, rồi a. b. c. d.
pattern = re.compile(
    r'(\d+)\.\s+(.*?)\s*\na\.\s+(.*?)\s*\nb\.\s+(.*?)\s*\nc\.\s+(.*?)\s*\nd\.\s+(.*?)(?=\n\d+\.|\Z)',
    re.DOTALL
)

for m in pattern.finditer(text):
    num = int(m.group(1))
    question = re.sub(r'\s+', ' ', m.group(2)).strip()
    opt_a = re.sub(r'\s+', ' ', m.group(3)).strip()
    opt_b = re.sub(r'\s+', ' ', m.group(4)).strip()
    opt_c = re.sub(r'\s+', ' ', m.group(5)).strip()
    opt_d = re.sub(r'\s+', ' ', m.group(6)).strip()

    questions.append({
        "question": question,
        "options": [
            f"A. {opt_a}",
            f"B. {opt_b}",
            f"C. {opt_c}",
            f"D. {opt_d}"
        ],
        "answer": ""
    })

print(f"Trich xuat duoc {len(questions)} cau")

# Lưu JSON
data = {"section": "file4", "questions": questions}
with open(r'c:\vscode\code\TN_MMT\lichsudang\file4.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nDa luu file4.json voi {len(questions)} cau")
