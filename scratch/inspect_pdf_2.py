import fitz

pdf_path = r"C:\Users\Admin\Desktop\lsdd\917 câu trắc nghiệm LSĐ 2026.pdf"
doc = fitz.open(pdf_path)

output_file = "scratch/pdf_sample2.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for i in range(min(10, doc.page_count)):
        page = doc[i]
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        text = s["text"].strip()
                        if text:
                            # Print text if color is not black or if it's bold and starts with A,B,C,D
                            if s["color"] != 0 or s["flags"] != 4:
                                # We only care about options
                                if text.startswith("A.") or text.startswith("B.") or text.startswith("C.") or text.startswith("D."):
                                    f.write(f"Page {i} | Text: '{text[:50]}' | Font: {s['font']} | Color: {s['color']} | Flags: {s['flags']}\n")
                                    
    f.write("\n\nChecking last 5 pages for answers:\n")
    for i in range(max(0, doc.page_count - 5), doc.page_count):
        f.write(f"--- PAGE {i} ---\n")
        f.write(doc[i].get_text()[:500] + "\n...")
