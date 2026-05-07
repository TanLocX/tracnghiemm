import fitz
import pytesseract
from PIL import Image
import io
import os
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'c:\vscode\code\TN_MMT'

def analyze():
    pdf_path = r'C:\Users\Admin\Downloads\LSD\file1.pdf'
    doc = fitz.open(pdf_path)
    
    # Analyze page 1 (index 1) which probably has questions
    page = doc[1]
    pix = page.get_pixmap(dpi=150)
    img_bytes = pix.tobytes('png')
    
    img_pil = Image.open(io.BytesIO(img_bytes))
    img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    
    # Get tesseract data
    data = pytesseract.image_to_data(img_pil, lang='vie', output_type=pytesseract.Output.DICT)
    
    # We want to see if any text is red or bold
    n_boxes = len(data['text'])
    for i in range(n_boxes):
        if int(data['conf'][i]) > 60:
            text = data['text'][i].strip()
            if not text: continue
            
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            
            # extract ROI
            roi = img_cv[y:y+h, x:x+w]
            if roi.size == 0: continue
            
            # calculate average color of dark pixels (text)
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
            
            # coordinates of text pixels
            text_pixels = roi[thresh == 255]
            if len(text_pixels) > 0:
                avg_color = np.mean(text_pixels, axis=0) # B, G, R
                
                # Check if it's red: R is significantly higher than B and G
                b, g, r = avg_color
                is_red = r > 150 and r > b + 50 and r > g + 50
                
                if is_red:
                    print(f"RED TEXT: '{text}', RGB: ({r:.0f}, {g:.0f}, {b:.0f})")
                elif text in ['A.', 'B.', 'C.', 'D.']:
                    # Calculate boldness: ratio of text pixels to area of character
                    ratio = len(text_pixels) / (w * h)
                    print(f"Option: '{text}', boldness ratio: {ratio:.3f}, RGB: ({r:.0f}, {g:.0f}, {b:.0f})")

if __name__ == '__main__':
    analyze()
