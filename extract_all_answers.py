import fitz
import pytesseract
from PIL import Image
import io
import os
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'c:\vscode\code\TN_MMT'

def extract_all():
    pdf_path = r'C:\Users\Admin\Downloads\LSD\file1.pdf'
    doc = fitz.open(pdf_path)
    
    all_answers = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes('png')
        
        img_pil = Image.open(io.BytesIO(img_bytes))
        img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        
        data = pytesseract.image_to_data(img_pil, lang='vie', output_type=pytesseract.Output.DICT)
        
        options_data = []
        for i in range(len(data['text'])):
            text = data['text'][i].strip()
            conf = int(data['conf'][i])
            
            # Use regex to match A., B., C., D. properly
            import re
            m = re.match(r"^[_ \-\*]*([A-D])[.):,]", text, re.IGNORECASE)
            if conf > 30 and m:
                letter = m.group(1).upper()
                x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                
                roi = gray[max(0, y-5):min(gray.shape[0], y+h+5), max(0, x):min(gray.shape[1], x+800)]
                if roi.size == 0: continue
                
                _, thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                text_pixels = roi[thresh == 255]
                
                if len(text_pixels) > 0:
                    avg_intensity = np.mean(text_pixels)
                    coords = cv2.findNonZero(thresh)
                    if coords is not None:
                        rx, ry, rw, rh = cv2.boundingRect(coords)
                        actual_area = rw * rh
                        boldness = len(text_pixels) / actual_area if actual_area > 0 else 0
                    else:
                        boldness = 0
                    
                    options_data.append({
                        'letter': letter,
                        'y': y,
                        'intensity': avg_intensity,
                        'boldness': boldness
                    })
        
        # Group options into questions (difference in y < 200)
        if not options_data: continue
        options_data.sort(key=lambda x: x['y'])
        
        questions = []
        current_q = [options_data[0]]
        
        for opt in options_data[1:]:
            if opt['y'] - current_q[-1]['y'] < 150:
                current_q.append(opt)
            else:
                questions.append(current_q)
                current_q = [opt]
        if current_q:
            questions.append(current_q)
            
        for q in questions:
            if len(q) < 2: continue # Ignore isolated letters
            
            # Find the best option: darkest intensity or highest boldness
            # Normalize
            intensities = np.array([o['intensity'] for o in q])
            boldnesses = np.array([o['boldness'] for o in q])
            
            # The correct answer has significantly lower intensity
            best_idx = np.argmin(intensities)
            
            # If the difference is very small, fallback to boldness
            if len(intensities) > 1:
                sorted_int = np.sort(intensities)
                if sorted_int[1] - sorted_int[0] < 10:
                    best_idx = np.argmax(boldnesses)
            
            ans = q[best_idx]['letter']
            all_answers.append(ans)
            
        if (page_num + 1) % 10 == 0:
            print(f"Processed {page_num + 1}/{len(doc)} pages. Found {len(all_answers)} answers so far.")
            
    print(f"Done! Total answers found: {len(all_answers)}")
    
    with open('c:/vscode/code/TN_MMT/lichsudang/extracted_answers.txt', 'w') as f:
        f.write(",".join(all_answers))

if __name__ == '__main__':
    extract_all()
