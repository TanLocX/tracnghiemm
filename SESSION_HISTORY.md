# 📜 TỔNG KẾT & LỊCH SỬ PHIÊN LÀM VIỆC (SESSION LOG)

> **Dự án:** Ứng dụng Trắc Nghiệm Ôn Tập & Khảo Sát Kiến Thức (Flet Python GUI)  
> **Repository:** `https://github.com/TanLocX/tracnghiemm.git`  
> **Nhánh:** `main`  
> **Ngày cập nhật:** 23/08/2026  

---

## 1. 📂 CẤU TRÚC KHO DỮ LIỆU CÂU HỎI

Hệ thống hỗ trợ nạp câu hỏi tự động từ các định dạng `.json`, `.txt` (cú pháp đáp án `=> a`), và file `.pdf`:

| Thư mục môn học | Nội dung & Quy mô | Ghi chú |
| :--- | :--- | :--- |
| `phapluat/` | **295 câu hỏi** (`pl1.json`: 100 câu, `pl2.json`: 100 câu, `pl_kt.json`: 95 câu) | Đã chuẩn hóa JSON từ các file txt thô `pl1.txt`, `pl2.txt`, `pl_kt.txt` và `da_pl1.txt`. |
| `mangmaytinh/` | **741 câu hỏi** (16 bộ đề JSON/TXT) | Bộ câu hỏi Mạng Máy Tính phong phú, phân bổ theo đề thi. |
| `lichsudang/` | Các chương ôn tập CLO & bổ sung | Phân chia rõ ràng: Chương 1, Chương 2, Chương 3, Ôn tập, Bổ sung. |

---

## 2. 🚀 CÁC TÍNH NĂNG ĐÃ NÂNG CẤP & HOÀN THIỆN

### 🎨 2.1. Giao diện Hiện Đại (Glassmorphism & Sleek Dark UI)
- Toàn bộ GUI được thiết kế lại theo tiêu chuẩn hiện đại, card bán trong suốt, bo góc mềm mại, đổ bóng nổi.
- Hiệu ứng màu sắc phản hồi trực quan khi chọn đáp án:
  - 🟢 **Xanh Emerald** khi trả lời đúng.
  - 🔴 **Đỏ Crimson** khi trả lời sai, kèm hiển thị đáp án đúng và khung **Giải thích chi tiết (💡)** nếu có.

### 🗺️ 2.2. Bản Đồ Câu Hỏi Trực Tiếp Bên Phải (Right Sidebar Question Map)
- Lưới ô số tương tác `[1]..[N]` hiển thị **cố định ở cột bên phải** màn hình khi làm bài.
- Màu sắc trực quan theo trạng thái từng câu:
  - 🟢 **Đúng** (Xanh) | 🔴 **Sai** (Đỏ) | ⚪ **Chưa làm** (Xám) | 🔵 **Đang làm** (Viền sáng).
- Click vào bất kỳ ô số nào để nhảy nhanh đến câu đó mà **không bị mất trạng thái câu đã chọn trước đó**.
- Chân sidebar có thanh thống kê: Số câu đã làm `/` Tổng số câu & Tỷ lệ chính xác thời gian thực.

### 📊 2.3. Dashboard Lịch Sử Học Tập & Thống Kê (History Analytics)
- Tự động ghi nhận lịch sử vào `history.json` khi hoàn thành bài thi.
- Tab **"Lịch sử"** tại màn hình chính hiển thị:
  - Tổng số lần làm bài.
  - Độ chính xác trung bình (%).
  - Tổng số câu hỏi đã ôn tập.
  - Danh sách từng lần làm bài (ngày giờ, môn học, số câu đúng/tổng, tỷ lệ %).
  - Nút **Xóa lịch sử** để reset khi muốn ôn lại từ đầu.
- Đã có cơ chế bảo vệ (`history_saved`) chống ghi trùng lặp khi bấm lọc câu hỏi ở màn hình kết quả.

### 🎨 2.4. Hệ Thống 4 Theme & Bộ Chỉnh Cỡ Chữ Thời Gian Thực
- **4 Theme Preset thời thượng:**
  1. 🌙 *Deep Midnight* (Tối sang trọng, mặc định).
  2. 🌊 *Ocean Teal* (Xanh đại dương công nghệ).
  3. ⚡ *Cyberpunk Neon* (Tím neon huyền ảo).
  4. ☀️ *Clean Light* (Sáng sủa, thanh lịch).
- **Bộ chỉnh cỡ chữ:** 2 nút `A-` và `A+` ở thanh tiêu đề trên cùng giúp tăng/giảm cỡ chữ nhanh chóng từ 80% đến 135%.

### 🎯 2.5. Phân Đoạn Làm Bài Linh Hoạt (20 câu & 50 câu)
- Trong cả **Ôn theo chương** và **Danh sách bộ đề thi**:
  - 📌 **20 câu:** `Câu 1–20`, `Câu 21–40`, `Câu 41–60`, `Câu 61–80`, v.v.
  - 📌 **50 câu:** `Câu 1–50`, `Câu 51–100`, `Câu 101–150`, v.v.
  - 📌 **Toàn bộ:** Làm tất cả câu hỏi của môn/chương/đề đó.
- Có tùy chọn **Xáo trộn câu hỏi ngẫu nhiên** (Shuffle).

---

## 3. 🛠️ CÁC LỖI TƯƠNG THÍCH FLET ĐÃ ĐƯỢC KHẮC PHỤC

| Lỗi gặp phải | Nguyên nhân trên Flet mới | Cách khắc phục trong `quiz_app.py` |
| :--- | :--- | :--- |
| `Row.__init__() got an unexpected keyword argument 'main_axis_alignment'` | `ft.Row` trên Flet mới nhận tham số `alignment` thay vì `main_axis_alignment`. | Thay toàn bộ bằng `alignment=ft.MainAxisAlignment.CENTER`. |
| `Text.__init__() got an unexpected keyword argument 'line_height'` | `ft.Text` không còn hỗ trợ `line_height`. | Bỏ tham số `line_height` khỏi tất cả các `ft.Text`. |
| `Dropdown.__init__() got an unexpected keyword argument 'on_change'` | Flet chuyển sự kiện của `Dropdown` thành `on_select`. | Thêm hàm monkey-patch tự động ánh xạ `on_change` ⇄ `on_select` ở đầu file. |
| `colors` và `icons` viết hoa/thường | Flet chuyển `colors` -> `Colors`, `icons` -> `Icons`. | Gán `ft.colors = ft.Colors` và `ft.icons = ft.Icons`. |
| Lặp bản ghi lịch sử | Mỗi lần bấm chip lọc câu hỏi (Tất cả / Câu đúng / Câu sai) ở màn hình kết quả sẽ gọi lại `show_result()`. | Đặt cờ `state["history_saved"] = True` sau khi lưu lần đầu, và reset về `False` khi bắt đầu bài thi mới. |

---

## 4. 💻 HƯỚNG DẪN KHỞI CHẠY DỰ ÁN

### Yêu cầu môi trường:
- Python 3.10+
- Các thư viện cần thiết:
```bash
pip install flet pdfplumber pypdf
```

### Chạy ứng dụng:
```bash
python quiz_app.py
```

---

## 5. 📌 DANH SÁCH COMMIT ĐÃ PUSH LÊN GITHUB

- `6c65e3e`: Revamp GUI with Modern Glassmorphism & Dark UI design
- `3a9c85a`: Fix Flet compatibility: remove line_height from Text controls
- `d692831`: Add Quick-Jump Question Map, History Analytics Dashboard, and Theme & Font Scalers
- `a679d07`: Fix Flet Dropdown compatibility: auto map on_change to on_select
- `70e0e29`: Display Question Map as persistent right sidebar during quiz
- `72e7096`: Ensure quiz history is accurately saved once per session
- `5ee2601`: Add 20-question batch ranges (1-20, 21-40, 41-60, etc.) alongside 50-question ranges
- `c1a1135`: Add .gitignore for python cache and local files
