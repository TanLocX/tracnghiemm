"""
Cần cài đặt thư viện trước khi chạy: 
pip install google-genai
"""
import json
import os
import sys
import time

# Đảm bảo Terminal Windows in được tiếng Việt không bị lỗi font
sys.stdout.reconfigure(encoding="utf-8")

try:
    from google import genai
except ImportError:
    print("Lỗi: Không tìm thấy thư viện 'google-genai'.\nVui lòng mở Terminal và chạy lệnh:\n    pip install google-genai")
    sys.exit(1)

# Cấu hình API key (Bạn có thể lấy miễn phí tại Google AI Studio)
# Nhớ thay thế "YOUR_API_KEY_HERE" bằng API Key thật của bạn!
API_KEY = "AIzaSyCIrDNiyiu6hOl6NP7DVghTQcWiypEw5Nc"

if API_KEY == "YOUR_API_KEY_HERE":
    print("Lỗi: Bạn chưa thay API Key. Hãy lấy khóa ở https://aistudio.google.com/ và dán vào biến API_KEY.")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)

def fix_answers(filepath):
    print(f"Đang xử lý file: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    is_list = isinstance(data, list)
    questions = data if is_list else data.get("questions", [])

    # Tăng số câu mỗi lô lên 30 để tiết kiệm số lần gọi API, tránh giới hạn và chạy nhanh hơn
    batch_size = 30
    # Duyệt qua toàn bộ số câu hỏi trong file
    for i in range(0, len(questions), batch_size):
        batch = questions[i:i+batch_size]
        
        prompt = "Bạn là giảng viên chuyên môn Lịch sử Đảng Cộng sản Việt Nam.\n"
        prompt += "Hãy chọn đáp án ĐÚNG NHẤT về mặt lịch sử cho các câu hỏi sau.\n"
        prompt += "Chỉ trả về MỘT mảng JSON duy nhất chứa các chuỗi là toàn bộ nội dung của phương án đúng (phải copy chính xác 100% text của một trong các options).\n\n"
        
        for idx, q in enumerate(batch):
            prompt += f"Câu {i+idx+1}: {q.get('question')}\n"
            for opt in q.get('options', []):
                prompt += f"- {opt}\n"
            prompt += "\n"
            
        prompt += 'Format trả về bắt buộc (Ví dụ minh họa):\n[\n  "C. Đáp án đúng của câu đầu tiên",\n  "B. Đáp án đúng của câu thứ hai"\n]'
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash-lite',
                    contents=prompt
                )
                text = response.text
                
                # Lọc lấy mảng JSON từ kết quả trả về
                start = text.find('[')
                end = text.rfind(']') + 1
                
                if start != -1 and end != -1:
                    answers = json.loads(text[start:end])
                    if len(answers) == len(batch):
                        for j, ans in enumerate(answers):
                            questions[i+j]['answer'] = ans
                            print(f"  [Sửa OK] Câu {i+j+1}: -> {ans[:60]}...")
                        
                        # Lưu ngay vào file sau mỗi lô thành công để đề phòng chương trình bị ngắt đột ngột
                        with open(filepath, 'w', encoding='utf-8') as f:
                            json.dump(data, f, ensure_ascii=False, indent=2)
                            
                        break # Sửa thành công thì thoát vòng lặp thử lại
                    else:
                        print(f"  [Cảnh báo] Lần gửi {i}: Số đáp án trả về không khớp số câu hỏi.")
                else:
                    print(f"  [Lỗi] Không parse được JSON từ LLM ở batch {i}")
                    
            except Exception as e:
                error_msg = str(e)
                print(f"  [Ngoại lệ] Lỗi ở lô {i} (Lần thử {attempt + 1}/{max_retries}): {error_msg}")
                if attempt < max_retries - 1:
                    wait_time = 5
                    if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                        print("  [Cảnh báo] Đạt giới hạn API miễn phí (15 request/phút). Đang đợi 60 giây để khôi phục...")
                        wait_time = 60
                    time.sleep(wait_time)
                else:
                    print(f"  [Bỏ qua] Lô {i} thất bại hoàn toàn.")
            
        time.sleep(5) # Dừng 5 giây giữa các lô để an toàn không vượt mức 15 request/phút

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"\nHoàn tất! Đã kiểm tra toàn bộ {len(questions)} câu và lưu đè lên file gốc: {filepath}")

if __name__ == "__main__":
    target_file = r"c:\vscode\code\TN_MMT\lichsudang\chuong\chuong1_1930_1945.json"
    fix_answers(target_file)