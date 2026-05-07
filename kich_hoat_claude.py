import schedule
import time
from datetime import datetime
# Giả sử Antigravity đã được cài đặt và cấu hình sẵn tài khoản Pro Team của bạn
# từ antigravity import ClaudeClient 

def job():
    print(f"[{datetime.now()}] Bắt đầu khởi động Opus 4.6...")
    
    # Đoạn code tương tác với Antigravity/Claude
    # client = ClaudeClient(token="YOUR_TEAM_TOKEN") 
    # response = client.send_message(model="opus-4.6", prompt="Văn bản của bạn ở đây")
    
    print("Đã gửi tin nhắn thành công!")
    return schedule.CancelJob # Chỉ chạy một lần duy nhất

# Lên lịch đúng 10:00 sáng nay
schedule.every().day.at("10:00").do(job)

print("Hệ thống đã sẵn sàng. Bạn có thể đi ngủ, tôi sẽ trực máy.")

while True:
    schedule.run_pending()
    time.sleep(60) # Kiểm tra mỗi phút một lần