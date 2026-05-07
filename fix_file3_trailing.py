
import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\vscode\code\TN_MMT\lichsudang\file3_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Xóa phần văn bản thừa ở cuối đáp án D cuối cùng
# Thường là phần đầu của câu hỏi kế tiếp bị rơi vào
# hoặc phần cuối câu hỏi bị rơi vào đáp án D
trailing_noise_pattern = re.compile(
    r'\s*(nào\?|là:|là\s*:|gì\?|gì:|vì:|tại:|bộ"\?|hơn\.|hơn\?)\s*$'
)

fixed_count = 0
for q in data:
    # Xóa đuôi thừa ở đáp án cuối (D)
    if q['options'] and len(q['options']) == 4:
        last_opt = q['options'][-1]
        cleaned = trailing_noise_pattern.sub('', last_opt).strip()
        if cleaned != last_opt:
            q['options'][-1] = cleaned
            fixed_count += 1

    # Xóa đuôi thừa ở câu hỏi
    q['question'] = q['question'].strip()

print(f"Fixed {fixed_count} options with trailing noise")
print(f"Total: {len(data)} questions")

# In kiểm tra một số câu có sửa
for i, q in enumerate(data[:10]):
    print(f"\n[Q{i+1}] {q['question'][:70]}")
    for opt in q['options']:
        print(f"  {opt[:70]}")

# Lưu lại
with open(r'c:\vscode\code\TN_MMT\lichsudang\file3_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nFile saved successfully.")
