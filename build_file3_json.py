
import re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Đọc text layer đã trích xuất
with open(r'c:\vscode\code\TN_MMT\lichsudang\file3_textlayer.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

# Xóa các dòng rác (header page, fanpage)
lines = raw.splitlines()
cleaned_lines = []
for line in lines:
    stripped = line.strip()
    # Bỏ qua dòng trống, dòng PAGE, dòng Fanpage
    if not stripped:
        continue
    if stripped.startswith('--- PAGE'):
        continue
    if 'Fanpage:' in stripped or 'Tailieudethi.vn' in stripped:
        continue
    # Bỏ các dòng nhiễu cuối trang (chỉ chứa số hoặc ký tự đặc biệt)
    if re.match(r'^[\|\d\s]+$', stripped):
        continue
    cleaned_lines.append(stripped)

cleaned_text = '\n'.join(cleaned_lines)

# Tách thành các block câu hỏi theo pattern "Câu N."
# Thêm ký tự đặc biệt ở đầu mỗi câu để dễ tách
blocks = re.split(r'(?=Câu \d+\.)', cleaned_text)
blocks = [b.strip() for b in blocks if b.strip()]

questions = []

for block in blocks:
    # Bỏ những block không phải câu hỏi
    if not re.match(r'Câu \d+\.', block):
        continue

    # Lấy số câu
    m = re.match(r'Câu (\d+)\.(.*)', block, re.DOTALL)
    if not m:
        continue

    q_num = int(m.group(1))
    rest = m.group(2).strip()

    # Tách nội dung câu hỏi và các đáp án
    # Đáp án bắt đầu bằng "A.\n", "B.\n", "C.\n", "D.\n"
    # hoặc "A. text" trên cùng một dòng
    # Split tại các đáp án A, B, C, D
    option_pattern = re.compile(r'\n([A-D])\.\n', re.MULTILINE)

    # Tìm vị trí đầu tiên của đáp án
    first_option = re.search(r'\n([A-D])\.\n', '\n' + rest)
    
    if first_option:
        question_text = rest[:first_option.start()].strip()
        options_part = rest[first_option.start():].strip()
    else:
        # Thử tìm kiểu A. text trên cùng dòng
        first_option2 = re.search(r'\n[A-D]\. ', '\n' + rest)
        if first_option2:
            question_text = rest[:first_option2.start()].strip()
            options_part = rest[first_option2.start():].strip()
        else:
            question_text = rest.strip()
            options_part = ''

    # Parse các đáp án
    # Tách theo pattern: ký tự A/B/C/D theo sau là ".\n" hoặc ". "
    # Kết hợp cả hai dạng
    option_entries = re.split(r'\n(?=[A-D]\.\n|[A-D]\. )', '\n' + options_part)
    
    options = []
    for entry in option_entries:
        entry = entry.strip()
        if not entry:
            continue
        # Dạng 1: "A.\nNội dung"
        m2 = re.match(r'^([A-D])\.\n(.+)', entry, re.DOTALL)
        if m2:
            letter = m2.group(1)
            content = m2.group(2).strip().replace('\n', ' ')
            options.append(f'{letter}. {content}')
            continue
        # Dạng 2: "A. Nội dung"
        m3 = re.match(r'^([A-D])\. (.+)', entry, re.DOTALL)
        if m3:
            letter = m3.group(1)
            content = m3.group(2).strip().replace('\n', ' ')
            options.append(f'{letter}. {content}')
            continue

    # Làm sạch question_text
    question_text = question_text.replace('\n', ' ').strip()
    # Xóa phần "là:" hoặc "là:\n" ở cuối câu hỏi nếu bị rơi ra
    # (đây là một phần câu hỏi hợp lệ, giữ lại)

    questions.append({
        "question": question_text,
        "options": options,
        "answer": ""
    })

# Lưu JSON trước
output_path = r'c:\vscode\code\TN_MMT\lichsudang\file3_fixed.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Total questions parsed: {len(questions)}")
for i, q in enumerate(questions[:5]):
    print(f"\n--- Q{i+1} ---")
    print("Q:", q['question'][:80])
    for opt in q['options']:
        print(' ', opt)
    print('Answer:', repr(q['answer']))

print(f"\nSaved to {output_path}")
