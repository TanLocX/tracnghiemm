import fitz
import pytesseract
from PIL import Image
import io
import os
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'c:\vscode\code\TN_MMT'

def analyze_page():
    pdf_path = r'C:\Users\Admin\Downloads\LSD\file1.pdf'
    doc = fitz.open(pdf_path)
    
    page = doc[1] # Page 2
    pix = page.get_pixmap(dpi=150)
    img_bytes = pix.tobytes('png')
    
    img_pil = Image.open(io.BytesIO(img_bytes))
    img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    
    data = pytesseract.image_to_data(img_pil, lang='vie', output_type=pytesseract.Output.DICT)
    
    options_data = []
    
    # We will find the bounding boxes of the letters, then extend the box to the right to get the whole line
    for i in range(len(data['text'])):
        text = data['text'][i].strip()
        conf = int(data['conf'][i])
        
        if conf > 30 and text in ['A.', 'B.', 'C.', 'D.', 'A,', 'B,', 'C,', 'D,']:
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            
            # ROI for the entire line: from x to end of image, with same y and h
            roi = gray[max(0, y-5):min(gray.shape[0], y+h+5), max(0, x):min(gray.shape[1], x+800)]
            if roi.size == 0: continue
            
            # Apply Otsu's thresholding to get text pixels
            _, thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            
            # Erosion to compute stroke width roughly or just measure ratio
            text_pixels = roi[thresh == 255]
            if len(text_pixels) > 0:
                # Average intensity of the text pixels (lower means darker text)
                avg_intensity = np.mean(text_pixels)
                
                # Ratio of text pixels to the bounding box of the actual text
                # Find bounding box of all text in ROI
                coords = cv2.findNonZero(thresh)
                if coords is not None:
                    rx, ry, rw, rh = cv2.boundingRect(coords)
                    actual_area = rw * rh
                    boldness = len(text_pixels) / actual_area if actual_area > 0 else 0
                else:
                    boldness = 0
                
                options_data.append({
                    'letter': text,
                    'y': y,
                    'intensity': avg_intensity,
                    'boldness': boldness
                })
                
    options_data.sort(key=lambda x: x['y'])
    
    print("Found options (Whole Line):")
    for opt in options_data:
        print(f"{opt['letter']:<3} | y: {opt['y']:<4} | Avg Intensity: {opt['intensity']:>5.1f} | Boldness Ratio: {opt['boldness']:.3f}")

if __name__ == '__main__':
    analyze_page()
