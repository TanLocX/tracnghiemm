import fitz
import re

pdf_path = r"C:\Users\Admin\Desktop\lsdd\917 câu trắc nghiệm LSĐ 2026.pdf"
doc = fitz.open(pdf_path)

full_text = ""
for page in doc:
    full_text += page.get_text() + "\n"

# count GỢI Ý ĐÁP ÁN
goi_y = re.findall(r'GỢI Ý ĐÁP ÁN', full_text)
print("Total 'GỢI Ý ĐÁP ÁN' matches:", len(goi_y))

# Let's see the sequence of "Câu \d+:" to find when it resets
matches = re.finditer(r'Câu\s+(\d+)\s*:', full_text)
prev_num = 0
resets = []
for m in matches:
    num = int(m.group(1))
    if num < prev_num:
        resets.append((prev_num, num))
    prev_num = num

print("Resets at (prev -> new):", resets)
