import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

filepath = r"c:\vscode\code\TN_MMT\lichsudang\917_cau_trac_nghiem.json"

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

chapters = {1: [], 2: [], 3: []}
for q in data:
    ch = q.get("chapter")
    if ch in chapters:
        chapters[ch].append(q)

for ch, questions in chapters.items():
    out_path = rf"c:\vscode\code\TN_MMT\lichsudang\chuong{ch}.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Chương {ch}: {len(questions)} câu → {out_path}")
