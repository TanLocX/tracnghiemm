# Tóm tắt dự án TN_MMT

## Tổng quan
Dự án là một ứng dụng thi trắc nghiệm (Quiz App) đa nền tảng được phát triển bằng ngôn ngữ Python sử dụng framework **Flet**. Ứng dụng hỗ trợ người dùng làm bài tập trắc nghiệm cho nhiều môn học khác nhau (hiện tại có "Lịch sử Đảng" và "Mạng Máy Tính"), đọc dữ liệu câu hỏi từ các định dạng linh hoạt như `.json`, `.txt` và `.pdf`.

## Cấu trúc dự án
- **`quiz_app.py`**: Mã nguồn chính của chương trình. Chứa toàn bộ logic xử lý:
  - Cấu hình và hiển thị giao diện người dùng (UI) bằng Flet.
  - Các hàm parser để đọc và trích xuất câu hỏi từ file `.txt`, `.json` và file `.pdf` (sử dụng thư viện `pdfplumber` hoặc `pypdf`).
  - Quản lý trạng thái bài thi, kiểm tra đáp án, hiển thị kết quả và luyện tập lại câu sai.
- **`requirements.txt`**: Khai báo các thư viện phụ thuộc bao gồm `flet`, `flet-web`, và `pdfplumber`.
- **`lichsudang/`**: Thư mục dữ liệu chứa các câu hỏi trắc nghiệm của môn **Lịch sử Đảng**. Các file `.json` được chia theo từng chương (chương 1, 2, 3...) và các phần bổ sung sự kiện lịch sử.
- **`mangmaytinh/`**: Thư mục dữ liệu chứa các câu hỏi trắc nghiệm của môn **Mạng Máy Tính**. Bao gồm các file dữ liệu được phân chia cụ thể theo chủ đề: mô hình OSI, TCP/IP, mạng cục bộ, internet, IP header,...
- **`pl1.txt` / `pl2.txt`**: File dữ liệu thô hoặc tài liệu dạng text.
- **`Procfile`**: Cấu hình khởi chạy để hỗ trợ deploy ứng dụng lên các nền tảng đám mây (như Heroku).

## Các tính năng nổi bật
1. **Quản lý môn học động**: Ứng dụng tự động quét các thư mục con (như `lichsudang`, `mangmaytinh`) để nhận diện môn học và nạp các bộ câu hỏi.
2. **Đa dạng nguồn dữ liệu**: Có thể soạn câu hỏi trong file `json` chuẩn, hoặc chỉ cần soạn trong file text `.txt` theo cú pháp quy định (có ký hiệu đáp án đúng là `=> a`), thậm chí hỗ trợ trích xuất câu hỏi từ PDF.
3. **Phân chia phạm vi ôn tập**: Người dùng có thể chọn làm bài thi tổng hợp, làm theo từng chương (có biểu tượng icon từng chương riêng biệt) hoặc một đoạn số lượng câu hỏi nhất định (ví dụ: từ câu 1 - 50).
4. **Trải nghiệm làm bài trực quan**: 
   - Đảo ngẫu nhiên câu hỏi và đáp án (Shuffle).
   - Giao diện Dark mode hiện đại với màu sắc dễ phân biệt.
   - Thống kê kết quả sau khi hoàn thành.
   - Tùy chọn làm lại các câu hỏi đã chọn sai để củng cố kiến thức.

## Cách sử dụng
Để khởi chạy hệ thống ở môi trường local, thực hiện các lệnh sau:
```bash
pip install -r requirements.txt
python quiz_app.py
```
