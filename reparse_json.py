import os
import json
import re

def process():
    txt_path = r'c:\vscode\code\TN_MMT\lichsudang\file1.txt'
    out_path = r'c:\vscode\code\TN_MMT\lichsudang\file1.json'
    
    with open(txt_path, "r", encoding="utf-8") as f:
        all_text = f.read()

    lines = all_text.splitlines()
    questions = []
    
    current_q_text = []
    current_opts = []
    current_ans = ""
    
    # regex matches:
    # A, B. C) d: ạ, u, e.
    # It allows any letter from A-F, plus U, E, and 'ạ'
    opt_re = re.compile(r"^[_ \-\*]*([A-Fa-fUuạeE])[.,):]\s*(.*)", re.IGNORECASE)
    
    def flush():
        nonlocal current_q_text, current_opts, current_ans
        q = " ".join(current_q_text).strip()
        if q and current_opts:
            questions.append({
                "question": q,
                "options": current_opts,
                "answer": current_ans
            })
        current_q_text = []
        current_opts = []
        current_ans = ""

    state = "Q"
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Ignore page numbers or noise
        if re.match(r"^\d+$", line) or re.match(r"^[éèeE]\d+$", line):
            continue
            
        if line.lower().startswith("chương ") or line.lower().startswith("phần "): 
            continue
            
        if line.startswith("ANSWER:"):
            ans_letter = line.replace("ANSWER:", "").strip().upper()
            for opt in current_opts:
                if opt.startswith(ans_letter):
                    current_ans = opt
            continue
            
        m = opt_re.match(line)
        if m:
            if state == "Q":
                state = "O"
            letter = m.group(1).upper()
            if letter == 'Ạ': letter = 'A'
            if letter == 'U': letter = 'A' # often 'u' is a typo for 'a'
            if letter == 'E': letter = 'C' # often 'e' is a typo for 'c'
            
            text = m.group(2).strip()
            opt_str = f"{letter}. {text}"
            current_opts.append(opt_str)
            
            # detect marked answer
            first_word = line.split()[0]
            if "_" in first_word or "-" in first_word:
                current_ans = opt_str
        else:
            if state == "O":
                flush()
                state = "Q"
            current_q_text.append(line)
            
    flush()
    
    out_data = {
        "section": "file1",
        "questions": questions
    }
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
        
    print(f"Đã xử lý lại text và tạo JSON mới. Tìm thấy {len(questions)} câu hỏi.")

if __name__ == '__main__':
    process()
