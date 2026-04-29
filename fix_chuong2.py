import json, sys
sys.stdout.reconfigure(encoding="utf-8")

# {index (0-based): đáp án đúng (chữ cái)}
fixes = {
    115: "C",  # Câu 116
    116: "D",  # Câu 117
    155: "C",  # Câu 156
    203: "A",  # Câu 204
    223: "A",  # Câu 224
    233: "A",  # Câu 234
    252: "A",  # Câu 253
}

filepath = r"c:\vscode\code\TN_MMT\lichsudang\chuong2.json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for idx, letter in fixes.items():
    q = data[idx]
    # Tìm option khớp với chữ cái đúng
    matched = next((opt for opt in q["options"] if opt.strip().upper().startswith(letter + ".")), None)
    if matched:
        old = q["answer"]
        q["answer"] = matched.strip()
        print(f"Câu {idx+1}: '{old[:50]}' → '{matched.strip()[:50]}'")
    else:
        print(f"Câu {idx+1}: Không tìm thấy option {letter}!")

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nHoàn tất!")
