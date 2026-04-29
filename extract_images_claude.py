"""
Dùng Claude API vision để đọc ảnh trắc nghiệm và xuất ra JSON.
Đáp án đúng được nhận biết qua chữ IN ĐẬM trong ảnh.

Cài đặt: pip install anthropic
Cần set biến môi trường: ANTHROPIC_API_KEY
"""

import anthropic
import base64
import json
import os
import sys
import time

IMG_DIR = r"C:\Users\Admin\Desktop\lsdd\anh"
OUTPUT_JSON = r"C:\vscode\code\TN_MMT\lichsudang\lsdd_from_images.json"

SYSTEM_PROMPT = """Bạn là công cụ trích xuất câu hỏi trắc nghiệm từ ảnh.
Nhiệm vụ: đọc ảnh và trả về CHÍNH XÁC các câu hỏi trắc nghiệm dưới dạng JSON.

Quy tắc nhận biết đáp án đúng:
- Đáp án đúng được IN ĐẬM (bold) hoặc gạch chân trong ảnh
- Trả về đúng nội dung văn bản, không thêm bớt

Trả về JSON theo đúng format sau (không có markdown, không có giải thích):
[
  {
    "question": "Nội dung câu hỏi",
    "options": ["A. Đáp án A", "B. Đáp án B", "C. Đáp án C", "D. Đáp án D"],
    "answer": "<Điền text của phương án đúng vào đây>"
  }
]

Lưu ý:
 - NẾU ảnh không rõ chữ in đậm/gạch chân, hãy VẬN DỤNG KIẾN THỨC LỊCH SỬ ĐẢNG CỘNG SẢN VN để tự giải. Tuyệt đối không chọn bừa phương án A.
- "answer" phải là chuỗi khớp chính xác với một phần tử trong "options"
- Nếu ảnh có nhiều câu hỏi, trả về tất cả trong mảng
- Chỉ trả về JSON thuần, không có text khác"""


def encode_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def extract_questions_from_image(client: anthropic.Anthropic, img_path: str) -> list[dict]:
    img_data = encode_image(img_path)
    ext = os.path.splitext(img_path)[1].lower()
    media_type = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": img_data,
                    }
                },
                {
                    "type": "text",
                    "text": "Trích xuất tất cả câu hỏi trắc nghiệm trong ảnh này."
                }
            ]
        }]
    )

    raw = response.content[0].text.strip()

    # Bỏ markdown code block nếu có
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    return json.loads(raw)


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Lỗi: Chưa set ANTHROPIC_API_KEY")
        print("Chạy lệnh: set ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    files = sorted([
        f for f in os.listdir(IMG_DIR)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ])

    print(f"Tìm thấy {len(files)} ảnh trong {IMG_DIR}")
    print("Bắt đầu xử lý...\n")

    all_questions = []
    errors = []

    for i, fname in enumerate(files, 1):
        img_path = os.path.join(IMG_DIR, fname)
        print(f"[{i:3d}/{len(files)}] {fname} ... ", end="", flush=True)

        try:
            qs = extract_questions_from_image(client, img_path)
            all_questions.extend(qs)
            print(f"OK ({len(qs)} câu)")
        except json.JSONDecodeError as e:
            print(f"PARSE ERROR: {e}")
            errors.append(fname)
        except Exception as e:
            print(f"ERROR: {e}")
            errors.append(fname)
            # Đợi nếu bị rate limit
            if "rate_limit" in str(e).lower() or "529" in str(e):
                print("  Rate limit — đợi 30 giây...")
                time.sleep(30)

    # Lưu kết quả
    output = {
        "section": "Lịch Sử Đảng Cộng Sản Việt Nam",
        "questions": all_questions
    }

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*50}")
    print(f"Hoàn thành!")
    print(f"  Tổng câu hỏi: {len(all_questions)}")
    print(f"  Ảnh lỗi:      {len(errors)}")
    print(f"  Lưu tại:      {OUTPUT_JSON}")

    if errors:
        print(f"\nCác ảnh lỗi cần xử lý lại:")
        for f in errors:
            print(f"  - {f}")


if __name__ == "__main__":
    main()
