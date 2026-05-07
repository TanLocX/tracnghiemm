import json

with open("lichsudang/file1.json", encoding="utf-8") as f:
    raw = json.load(f)

data = raw["questions"]

# Merge rule:
# - New group starts when options[0] starts with "A."
# - Continuation when options[0] starts with "B.", "C.", or "D."
# - The "question" field of a continuation = end of previous option text

reconstructed = []
current = None

for obj in data:
    opts = obj.get("options", [])
    question = obj.get("question", "").strip()

    if not opts:
        if current is not None:
            current["question"] += " " + question
        continue

    first_opt = opts[0]

    if first_opt.startswith("A."):
        if current is not None:
            reconstructed.append(current)
        current = {
            "question": question,
            "options": list(opts),
            "answer": obj.get("answer", "")
        }
    else:
        # Continuation: question text is end of previous option
        if current is None:
            current = {"question": question, "options": list(opts), "answer": ""}
        else:
            if current["options"] and question:
                current["options"][-1] = current["options"][-1] + " " + question
            current["options"].extend(opts)
            # keep existing answer if already set
            if not current.get("answer") and obj.get("answer"):
                current["answer"] = obj["answer"]

if current is not None:
    reconstructed.append(current)

raw["questions"] = reconstructed

with open("lichsudang/file1_fixed.json", "w", encoding="utf-8") as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

# Summary
total = len(reconstructed)
no_answer = sum(1 for q in reconstructed if not q["answer"])
wrong_opts = [(i,q) for i,q in enumerate(reconstructed) if len(q["options"]) != 4]

import sys
sys.stdout.reconfigure(encoding='utf-8')
print(f"Total questions: {total}")
print(f"Missing answers: {no_answer}")
print(f"Questions with != 4 options: {len(wrong_opts)}")
for i, q in wrong_opts[:20]:
    print(f"  i={i} opts={len(q['options'])} q={q['question'][:60]}")
