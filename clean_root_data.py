import os
import json
import re

BASE_DIR = r"c:\vscode\code\TN_MMT\lichsudang"

def clean_text(text):
    if not isinstance(text, str): 
        return text
    # Xóa khối "GỢI Ý ĐÁP ÁN..." bị dính vào cuối chuỗi do lỗi từ phần mềm đọc PDF
    if " GỢI Ý ĐÁP ÁN " in text:
        text = text.split(" GỢI Ý ĐÁP ÁN ")[0]
    # Xóa các số trang bị dính ở cuối (khoảng trắng + 2 hoặc 3 chữ số tận cùng)
    text = re.sub(r'\s+\d{2,3}$', '', text)
    return text

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    is_list = isinstance(data, list)
    questions = data if is_list else data.get("questions", [])
    
    new_questions = []
    for q in questions:
        q["question"] = clean_text(q.get("question", ""))
        q["answer"] = clean_text(q.get("answer", ""))
        
        new_opts = []
        fused_q = None
        
        for opt in q.get("options", []):
            opt_cl = clean_text(opt)
            # Phát hiện lỗi gộp Câu 131 và 132 (hoặc các câu tương tự)
            match = re.search(r'(.*?)\s+(Câu \d+:.*)', opt_cl)
            if match and len(q.get("options", [])) > 4:
                new_opts.append(match.group(1).strip())
                fused_q = match.group(2).strip()
            else:
                new_opts.append(opt_cl)
                
        if fused_q and len(new_opts) >= 8:
            # Tách riêng 2 câu bị gộp
            q1 = {"question": q["question"], "options": new_opts[:4], "answer": "B. chưa xác định được mâu thuẫn chủ yếu trong xã hội Đông Dương thuộc địa"}
            q2 = {"question": fused_q, "options": new_opts[4:8], "answer": "B. Cuối năm 1930"}
            new_questions.extend([q1, q2])
        else:
            q["options"] = new_opts
            new_questions.append(q)
            
    if is_list:
        data = new_questions
    else:
        data["questions"] = new_questions
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Đã làm sạch file: {os.path.basename(filepath)}")

if __name__ == "__main__":
    for fn in os.listdir(BASE_DIR):
        if fn.endswith(".json"):
            process_file(os.path.join(BASE_DIR, fn))