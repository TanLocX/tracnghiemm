import fitz
import pytesseract
from PIL import Image
import io
import os
import cv2
import numpy as np
import json
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'c:\vscode\code\TN_MMT'

def extract_answers():
    pdf_path = r'C:\Users\Admin\Downloads\LSD\file1.pdf'
    doc = fitz.open(pdf_path)
    
    results = []
    
    # Just test on the first 3 pages
    for i in range(min(3, len(doc))):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes('png')
        
        img_pil = Image.open(io.BytesIO(img_bytes))
        img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        
        # Detect red pixels
        # Red in BGR can be around (0, 0, 255)
        # We will create a mask for red
        b, g, r = cv2.split(img_cv)
        # R > 150, R > G + 40, R > B + 40
        red_mask = (r > 150) & (r > g + 40) & (r > b + 40)
        
        # Calculate how many red pixels are in the page
        num_red = np.sum(red_mask)
        print(f"Page {i+1}: {num_red} red pixels")
        
        # If there are a lot of red pixels, answers might be red.
        # Let's get OCR data
        data = pytesseract.image_to_data(img_pil, lang='vie', output_type=pytesseract.Output.DICT)
        
        opt_re = re.compile(r"^[_ \-\*]*([A-D])[.):]", re.IGNORECASE)
        
        current_options = []
        for j in range(len(data['text'])):
            text = data['text'][j].strip()
            conf = int(data['conf'][j])
            if conf > 30 and text:
                m = opt_re.match(text)
                if m:
                    x, y, w, h = data['left'][j], data['top'][j], data['width'][j], data['height'][j]
                    
                    # Look at the whole line (approximate by expanding w)
                    # We can look at the right of the option letter
                    line_roi = img_cv[max(0, y-5):min(img_cv.shape[0], y+h+5), max(0, x):min(img_cv.shape[1], x+600)]
                    if line_roi.size == 0: continue
                    
                    b_roi, g_roi, r_roi = cv2.split(line_roi)
                    red_mask_roi = (r_roi > 150) & (r_roi > g_roi + 40) & (r_roi > b_roi + 40)
                    red_ratio = np.sum(red_mask_roi) / (line_roi.shape[0] * line_roi.shape[1])
                    
                    # Boldness check (density of dark pixels)
                    gray_roi = cv2.cvtColor(line_roi, cv2.COLOR_BGR2GRAY)
                    _, thresh_roi = cv2.threshold(gray_roi, 150, 255, cv2.THRESH_BINARY_INV)
                    black_ratio = np.sum(thresh_roi == 255) / (line_roi.shape[0] * line_roi.shape[1])
                    
                    current_options.append({
                        'letter': m.group(1).upper(),
                        'text': text,
                        'red_ratio': red_ratio,
                        'black_ratio': black_ratio,
                        'y': y
                    })
                    
        # Group options by y proximity (rough clustering for a question)
        if current_options:
            print(f"Options found on page {i+1}:")
            for opt in current_options:
                print(f"  {opt['letter']} - red: {opt['red_ratio']:.4f}, black: {opt['black_ratio']:.4f}")

if __name__ == '__main__':
    extract_answers()
