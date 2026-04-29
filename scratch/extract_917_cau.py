import fitz
import re
import json

pdf_path = r"C:\Users\Admin\Desktop\lsdd\917 câu trắc nghiệm LSĐ 2026.pdf"
doc = fitz.open(pdf_path)

# Extract all text
full_text = ""
for page in doc:
    full_text += page.get_text() + "\n"

# The text has questions and then "GỢI Ý ĐÁP ÁN" at the end.
# Let's split them.
parts = full_text.split("GỢI Ý ĐÁP ÁN")
main_content = parts[0]
answer_key_text = "GỢI Ý ĐÁP ÁN" + parts[1] if len(parts) > 1 else ""

# 1. Parse Answer Key
# Answer key format: 
# Câu 1
# C
# Câu 11
# A
answers = {}
# Regex to find "Câu X" followed by an option "A" or "B" or "C" or "D"
matches = re.finditer(r'Câu\s+(\d+)\s*\n\s*([A-D])', answer_key_text)
for match in matches:
    q_num = match.group(1)
    ans = match.group(2)
    answers[q_num] = ans

# 2. Parse Questions
questions_data = []

# Regex to find questions. 
# Matches "Câu X:" or "Câu X :"
# Then captures everything until the next "Câu Y:" or end of string.
question_pattern = re.compile(r'(Câu\s+(\d+)\s*:.*?)(?=Câu\s+\d+\s*:|$)', re.DOTALL)
q_matches = question_pattern.finditer(main_content)

for q_match in q_matches:
    q_block = q_match.group(1).strip()
    q_num = q_match.group(2)
    
    # Split the block into the question text and options
    # Usually options start with A., B., C., D. (with or without spaces)
    # Let's use regex to find A., B., C., D.
    # Note: Sometimes options might be multi-line.
    options_pattern = re.compile(r'\n\s*([A-D])\s*\.(.*?)(?=\n\s*[A-D]\s*\.|$)', re.DOTALL)
    
    # Find the start of the first option to extract the question text
    first_opt_match = re.search(r'\n\s*A\s*\.', q_block)
    if first_opt_match:
        q_text = q_block[:first_opt_match.start()].strip()
        opts_text = q_block[first_opt_match.start():]
    else:
        q_text = q_block
        opts_text = ""
    
    # Parse options
    opt_matches = options_pattern.finditer(opts_text)
    options_list = []
    options_dict = {}
    for opt in opt_matches:
        opt_letter = opt.group(1)
        opt_text = opt.group(2).strip()
        # Clean up newlines in option text
        opt_text = " ".join(opt_text.split())
        options_list.append(f"{opt_letter}. {opt_text}")
        options_dict[opt_letter] = f"{opt_letter}. {opt_text}"
    
    # Clean up question text (remove newlines inside text)
    q_text = " ".join(q_text.split())
    
    # Determine correct answer text
    correct_ans_letter = answers.get(q_num)
    correct_ans_text = options_dict.get(correct_ans_letter, "") if correct_ans_letter else ""
    
    question_obj = {
        "question": q_text,
        "options": options_list,
        "answer": correct_ans_text
    }
    questions_data.append(question_obj)

# Save to JSON
output_path = r"c:\vscode\code\TN_MMT\lichsudang\917_cau_trac_nghiem.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions_data, f, ensure_ascii=False, indent=4)

print(f"Total questions found: {len(questions_data)}")
print(f"Total answers found in key: {len(answers)}")
print(f"Saved to {output_path}")

# Check for mismatches
missing_answers = [q for q in questions_data if not q["answer"]]
print(f"Questions missing answers: {len(missing_answers)}")

