import json

with open(r'c:\vscode\code\TN_MMT\lichsudang\file4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']

# Sửa index 6 (câu 7) — PDF bị lỗi option b → viết thành "c." nên bị gộp với câu 8
qs[6] = {
    "question": "Trong nghiên cứu Lịch sử Đảng Cộng sản Việt Nam, khi xem xét, đối chiếu các hiện tượng lịch sử trong hình thức tổng quát nhằm mục đích vạch ra bản chất, quy luật, khuynh hướng chung trong sự vận động của sự vật thì đó là cách nghiên cứu dựa trên:",
    "options": [
        "A. Phương pháp lịch sử",
        "B. Phương pháp chọn lọc",
        "C. Phương pháp làm việc nhóm",
        "D. Phương pháp logic"
    ],
    "answer": "D. Phương pháp logic"
}

# Chèn câu 8 vào đúng vị trí index 7
cau8 = {
    "question": "Cần phải coi trọng phương pháp tổng kết thực tiễn lịch sử gắn với nghiên cứu lý luận trong nghiên cứu Lịch sử Đảng Cộng sản Việt Nam để:",
    "options": [
        "A. Làm rõ kinh nghiệm, bài học, quy luật phát triển của cách mạng Việt Nam",
        "B. Làm hài lòng người dân trong quá trình lãnh đạo cách mạng của Đảng",
        "C. Dễ dàng thống kê những thành tựu mà Đảng đạt được trong lãnh đạo cách mạng",
        "D. Chứng tỏ sự linh hoạt trong các bước đề ra đường lối, chủ trương của Đảng"
    ],
    "answer": "A. Làm rõ kinh nghiệm, bài học, quy luật phát triển của cách mạng Việt Nam"
}

qs.insert(7, cau8)

data['questions'] = qs

with open(r'c:\vscode\code\TN_MMT\lichsudang\file4.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done. Tong cau: {len(qs)}")
