import re
import json

def parse_raw():
    with open(r'c:\vscode\code\TN_MMT\lichsudang\file2_raw.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    questions = []
    
    current_q = []
    current_opts = []
    
    # Matches "A.", "B,", "C.", "D,"
    opt_re = re.compile(r"^([A-D])[.,:;]\s*(.*)", re.IGNORECASE)
    # Matches "2,", "3.", etc.
    q_re = re.compile(r"^\d+[,.]\s*(.*)")
    
    def flush():
        if current_q and current_opts:
            q_text = " ".join(current_q).strip()
            # Clean up extra spaces
            q_text = re.sub(r'\s+', ' ', q_text)
            
            cleaned_opts = []
            for opt in current_opts:
                opt_text = " ".join(opt['lines']).strip()
                opt_text = re.sub(r'\s+', ' ', opt_text)
                cleaned_opts.append(f"{opt['letter'].upper()}. {opt_text}")
                
            questions.append({
                "question": q_text,
                "options": cleaned_opts,
                "answer": ""
            })
            
    for line in lines:
        line = line.strip()
        if not line: continue
        if line.startswith("--- PAGE"): continue
        if line.isdigit(): continue # Page numbers
        
        opt_match = opt_re.match(line)
        q_match = q_re.match(line)
        
        if q_match and len(current_opts) > 0:
            # We hit a new question!
            flush()
            current_q = [line]
            current_opts = []
        elif q_match and len(current_opts) == 0:
            # First line of the first question, or a question after some garbage
            current_q.append(line)
        elif opt_match:
            letter = opt_match.group(1).upper()
            text = opt_match.group(2).strip()
            current_opts.append({'letter': letter, 'lines': [text]})
        else:
            # Continuation line
            if len(current_opts) > 0:
                # Continuation of the last option
                current_opts[-1]['lines'].append(line)
            else:
                # Continuation of the question
                current_q.append(line)
                
    flush()
    
    # Fix typos manually or via script later
    from fix_typos import fix_typos
    for q in questions:
        q['question'] = fix_typos(q['question'])
        q['options'] = [fix_typos(opt) for opt in q['options']]
        
    out_data = {
        "section": "file2_page1_to_5",
        "questions": questions
    }
    
    with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
        
    print(f"Extracted {len(questions)} questions.")

if __name__ == '__main__':
    parse_raw()
