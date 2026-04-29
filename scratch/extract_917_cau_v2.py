import fitz
import re
import json

pdf_path = r"C:\Users\Admin\Desktop\lsdd\917 câu trắc nghiệm LSĐ 2026.pdf"
doc = fitz.open(pdf_path)

full_text = ""
for page in doc:
    full_text += page.get_text() + "\n"

parts = full_text.split("GỢI Ý ĐÁP ÁN")

chapters_data = []

question_pattern = re.compile(r'(Câu\s+(\d+)\s*:.*?)(?=Câu\s+\d+\s*:|$)', re.DOTALL)
options_pattern = re.compile(r'\n\s*([A-D])\s*\.(.*?)(?=\n\s*[A-D]\s*\.|$)', re.DOTALL)
answer_pattern = re.compile(r'Câu\s+(\d+)\s*\n\s*([A-D])')

q_texts = [parts[0]]
a_texts = []

for i in range(1, 4):
    if i < len(parts):
        part = parts[i]
        split_match = re.search(r'Câu\s+1\s*:', part)
        if split_match:
            idx = split_match.start()
            a_texts.append(part[:idx])
            q_texts.append(part[idx:])
        else:
            a_texts.append(part)

for chap_idx in range(len(a_texts)):
    q_text = q_texts[chap_idx]
    a_text = a_texts[chap_idx]
    
    # Parse answers
    answers = {}
    for m in answer_pattern.finditer(a_text):
        answers[m.group(1)] = m.group(2)
        
    # Parse questions
    q_matches = question_pattern.finditer(q_text)
    questions = []
    for q_match in q_matches:
        q_block = q_match.group(1).strip()
        q_num = q_match.group(2)
        
        first_opt_match = re.search(r'\n\s*A\s*\.', q_block)
        if first_opt_match:
            q_only_text = q_block[:first_opt_match.start()].strip()
            opts_text = q_block[first_opt_match.start():]
        else:
            q_only_text = q_block
            opts_text = ""
            
        opt_matches = options_pattern.finditer(opts_text)
        options_list = []
        options_dict = {}
        for opt in opt_matches:
            opt_letter = opt.group(1)
            opt_text = opt.group(2).strip()
            opt_text = " ".join(opt_text.split())
            options_list.append(f"{opt_letter}. {opt_text}")
            options_dict[opt_letter] = f"{opt_letter}. {opt_text}"
            
        q_only_text = " ".join(q_only_text.split())
        
        correct_ans_letter = answers.get(q_num)
        correct_ans_text = options_dict.get(correct_ans_letter, "") if correct_ans_letter else ""
        
        questions.append({
            "chapter": chap_idx + 1,
            "question": q_only_text,
            "options": options_list,
            "answer": correct_ans_text
        })
        
    chapters_data.extend(questions)

with open(r"c:\vscode\code\TN_MMT\lichsudang\917_cau_trac_nghiem.json", "w", encoding="utf-8") as f:
    json.dump(chapters_data, f, ensure_ascii=False, indent=4)

print(f"Total extracted: {len(chapters_data)}")
missing = [q for q in chapters_data if not q["answer"]]
print(f"Missing answers: {len(missing)}")
if missing:
    print("Example missing:", missing[0])
