import fitz
import pytesseract
from PIL import Image
import io
import os
import json
import re
import sys

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'c:\vscode\code\TN_MMT'

def process():
    pdf_path = r'C:\Users\Admin\Downloads\LSD\file1.pdf'
    out_dir = r'c:\vscode\code\TN_MMT\lichsudang'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    out_path = os.path.join(out_dir, 'file1.json')
    txt_path = os.path.join(out_dir, 'file1.txt')
    
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Lỗi khi mở file PDF: {e}")
        sys.exit(1)
        
    all_text = ""
    print(f"Bắt đầu OCR {len(doc)} trang...")
    for i in range(len(doc)):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        img = Image.open(io.BytesIO(pix.tobytes('png')))
        text = pytesseract.image_to_string(img, lang='vie')
        all_text += text + "\n"
        if (i+1) % 10 == 0:
            print(f"Đã xử lý {i+1}/{len(doc)} trang")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(all_text)

    lines = all_text.splitlines()
    questions = []
    
    current_q_text = []
    current_opts = []
    current_ans = ""
    
    opt_re = re.compile(r"^[_ \-\*]*([A-D])[.):]\s*(.*)", re.IGNORECASE)
    
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
            # detect marked answer (like _D. or -A.)
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
        
    print(f"Hoàn thành! Đã tìm thấy {len(questions)} câu hỏi.")
    print(f"Đã lưu tại: {out_path}")

if __name__ == '__main__':
    process()
