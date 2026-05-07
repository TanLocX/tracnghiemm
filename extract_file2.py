import fitz
import pytesseract
from PIL import Image
import io
import os
import json
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'c:\vscode\code\TN_MMT'

def process_file2():
    pdf_path = r'C:\Users\Admin\Downloads\LSD\file2.pdf'
    out_path = r'c:\vscode\code\TN_MMT\lichsudang\file2.json'
    
    doc = fitz.open(pdf_path)
    
    all_text = ""
    # Process only pages 1 to 5 (index 0 to 4)
    num_pages_to_process = min(5, len(doc))
    print(f"Bắt đầu OCR {num_pages_to_process} trang đầu tiên của file2...")
    
    for i in range(num_pages_to_process):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        img = Image.open(io.BytesIO(pix.tobytes('png')))
        text = pytesseract.image_to_string(img, lang='vie')
        all_text += text + "\n"
        print(f"Đã xử lý trang {i+1}/{num_pages_to_process}")

    lines = all_text.splitlines()
    questions = []
    
    current_q_text = []
    current_opts = []
    current_ans = ""
    
    opt_re = re.compile(r"^[_ \-\*]*([A-D])[.):,]\s*(.*)", re.IGNORECASE)
    
    def flush():
        nonlocal current_q_text, current_opts, current_ans
        q = " ".join(current_q_text).strip()
        # Clean up question text (remove multiple spaces, etc)
        q = re.sub(r'\s+', ' ', q)
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
        # Ignore headers/footers if any
        if line.lower().startswith("chương") or line.lower().startswith("phần"): 
            continue
            
        m = opt_re.match(line)
        if m:
            if state == "Q":
                state = "O"
            letter = m.group(1).upper()
            text = m.group(2).strip()
            opt_str = f"{letter}. {text}"
            current_opts.append(opt_str)
            
            # Simple check if answer is marked with _ or - (from OCR)
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
        "section": "file2_page1_to_5",
        "questions": questions
    }
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
        
    print(f"Hoàn thành! Đã tìm thấy {len(questions)} câu hỏi.")
    print(f"Đã lưu tại: {out_path}")

if __name__ == '__main__':
    process_file2()
