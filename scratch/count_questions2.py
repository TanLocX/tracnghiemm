import fitz
import re

pdf_path = r"C:\Users\Admin\Desktop\lsdd\917 câu trắc nghiệm LSĐ 2026.pdf"
doc = fitz.open(pdf_path)

full_text = ""
for page in doc:
    full_text += page.get_text() + "\n"

print("Doc length:", len(full_text))

for m in re.finditer(r'GỢI Ý ĐÁP ÁN', full_text):
    print("Answer Key at:", m.start())

last_qs = []
prev_num = 0
for m in re.finditer(r'Câu\s+(\d+)\s*:', full_text):
    num = int(m.group(1))
    if num < prev_num:
        last_qs.append((prev_num, m.start()))
    prev_num = num
last_qs.append((prev_num, -1))

print("Resets at:", last_qs)
