import json

with open("lichsudang/file2.json", encoding="utf-8") as f:
    raw = json.load(f)

qs = raw["questions"]
filled = 0
skipped = 0

for q in qs:
    ans = q.get("answer", "").strip()
    if not ans or len(ans) > 1:
        # already full text or empty — skip
        skipped += 1
        continue

    letter = ans.upper()  # "a" -> "A"
    match = None
    for opt in q.get("options", []):
        if opt.startswith(letter + ".") or opt.startswith(letter + " "):
            match = opt
            break

    if match:
        q["answer"] = match
        filled += 1
    else:
        skipped += 1

with open("lichsudang/file2.json", "w", encoding="utf-8") as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

import sys
sys.stdout.reconfigure(encoding='utf-8')
print(f"Filled: {filled}, Skipped/unchanged: {skipped}")
