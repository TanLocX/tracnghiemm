import fitz
import json
import sys

# Force utf-8 encoding for stdout if needed, but we'll write to a file instead.
pdf_path = r"C:\Users\Admin\Desktop\lsdd\917 câu trắc nghiệm LSĐ 2026.pdf"
doc = fitz.open(pdf_path)

output_file = "scratch/pdf_sample.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for i in range(min(2, doc.page_count)):
        page = doc[i]
        f.write(f"--- PAGE {i} ---\n")
        f.write(page.get_text() + "\n")
        
        # Also let's inspect the blocks to see fonts and colors
        f.write(f"--- PAGE {i} FONT INFO ---\n")
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        text = s["text"].strip()
                        if text:
                            # print first 50 chars of text, with color and font
                            color = hex(s["color"])
                            flags = s["flags"]
                            font = s["font"]
                            f.write(f"Text: '{text[:50]}' | Font: {font} | Color: {color} | Flags: {flags}\n")
