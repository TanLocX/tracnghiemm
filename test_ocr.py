import fitz
import pytesseract
from PIL import Image
import io
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'c:\vscode\code\TN_MMT'

doc = fitz.open(r'C:\Users\Admin\Downloads\LSD\file1.pdf')
page = doc[1]
pix = page.get_pixmap(dpi=150)
img = Image.open(io.BytesIO(pix.tobytes('png')))
text = pytesseract.image_to_string(img, lang='vie')
print(text[:1000])
