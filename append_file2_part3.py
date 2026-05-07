import json

new_questions = [
    {
      "question": "Đại hội đại biểu lần thứ mấy của Đảng chủ trương “tập trung sức phát triển nông nghiệp coi nông nghiệp là mặt trận hàng đầu”?",
      "options": [
        "A. Đại hội lần thứ III (9/1960).",
        "B. Đại hội lần thứ IV (12/1976).",
        "C. Đại hội lần thứ V (3/1982).",
        "D. Đại hội lần thứ VI (12/1986)."
      ],
      "answer": ""
    },
    {
      "question": "Đại hội V (3/1982) chỉ đạo phát triển công nghiệp nặng trong giai đoạn này cần làm có mức độ, vừa sức, nhằm phục vụ thiết thực, hiệu quả cho ngành nào?",
      "options": [
        "A. Nông nghiệp.",
        "B. Xuất nhập khẩu.",
        "C. Nông nghiệp và công nghiệp nhẹ.",
        "D. Thương nghiệp và tiểu thủ công nghiệp."
      ],
      "answer": ""
    },
    {
      "question": "Đại hội lần thứ mấy Đảng ta đã xác định: “Ưu tiên phát triển công nghiệp nặng một cách hợp lý trên cơ sở phát triển nông nghiệp và công nghiệp nhẹ, kết hợp xây dựng công nghiệp và nông nghiệp thành một cơ cấu kinh tế công - nông nghiệp”?",
      "options": [
        "A. Đại hội lần thứ III (9/1960).",
        "B. Đại hội lần thứ IV (12/1976).",
        "C. Đại hội lần thứ V (3/1982).",
        "D. Đại hội lần thứ VI (12/1986)."
      ],
      "answer": ""
    },
    {
      "question": "Tại Đại hội nào Đảng ta xác định nhiệm vụ chung của chặng đường đầu tiên là: “Ổn định mọi mặt tình hình kinh tế - xã hội, tiếp tục xây dựng những tiền đề cần thiết cho việc đẩy mạnh CNH trong chặng đường tiếp theo”?",
      "options": [
        "A. Đại hội IV",
        "B. Đại hội V",
        "C. Đại hội VI",
        "D. Đại hội VII"
      ],
      "answer": ""
    },
    {
      "question": "Nội dung chính của CNH XHCN trong những năm còn lại của chặng đường đầu tiên của thời kỳ quá độ là được Đại hội VI xác định là:",
      "options": [
        "A. Đẩy nhanh tiến độ xây dựng cơ sở vật chất kỹ thuật cho CNXH",
        "B. Mở rộng quan hệ hợp tác với khối SEV",
        "C. Thực hiện cho bằng được ba chương trình mục tiêu: lương thực, thực phẩm, hàng tiêu dùng, hàng xuất khẩu.",
        "D. Đẩy mạnh cải tạo XHCN, xóa các thành phần kinh tế phi XHCN."
      ],
      "answer": ""
    },
    {
      "question": "Khái niệm được coi là bước đột phá mới trong nhận thức: “CNH, HĐH là quá trình chuyển đổi căn bản, toàn diện các hoạt động sản xuất, kinh doanh, dịch vụ và quản lý kinh tế, xã hội từ sử dụng lao động thủ công là chính sang sử dụng một cách phổ biến sức lao động với công nghệ, phương tiện và phương pháp tiên tiến, hiện đại dựa trên sự phát triển công nghiệp và tiến bộ khoa học công nghệ, tạo ra năng suất lao động xã hội cao”... được đưa ra trong văn kiện của Đảng?",
      "options": [
        "A. Đại hội lần thứ VI (12/1986)",
        "B. Đại hội lần thứ VII (6/1991)",
        "C. Hội nghị TW lần thứ VII khoá VII (1/1994)",
        "D. Đại hội lần thứ VIII (6/1996)"
      ],
      "answer": ""
    },
    {
      "question": "Mục tiêu cụ thể về đẩy mạnh CNH, HĐH gắn liền với phát triển kinh tế tri thức để sớm đưa nước ta ra khỏi tình trạng kém phát triển được Đảng ta chính thức nêu tại:",
      "options": [
        "A. Đại hội lần thứ IV (12/1976).",
        "B. Đại hội lần thứ VI (12/1986).",
        "C. Đại hội lần thứ VII (6/1991).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Nội dung nào dưới đây không đúng với quan điểm CNH, HĐH mà Đảng đề ra tại Đại hội lần thứ VIII (6/1996)?",
      "options": [
        "A. Giữ vững độc lập tự chủ đi đôi với mở rộng quan hệ hợp tác quốc tế, đa phương hóa, đa dạng hóa các quan hệ đối ngoại.",
        "B. Lực lượng tiến hành CNH là của nhà nước và các doanh nghiệp Nhà nước.",
        "C. Phát huy nguồn lực con người là yếu tố cơ bản cho sự phát triển nhanh và bền vững.",
        "D. Khoa học, công nghệ là động lực của CNH, HĐH."
      ],
      "answer": ""
    },
    {
      "question": "Tại Đại hội nào Đảng ta nhận định \"nhiệm vụ chuẩn bị tiền đề cho công nghiệp hóa đã cơ bản hoàn thành cho phép chuyển sang thời kỳ đẩy mạnh công nghiệp hóa, hiện đại hóa đất nước\":",
      "options": [
        "A. Đại hội lần thứ IV (12/1976).",
        "B. Đại hội lần thứ VI (12/1986).",
        "C. Đại hội lần thứ VII (6/1991).",
        "D. Đại hội lần thứ VIII (6/1996)."
      ],
      "answer": ""
    },
    {
      "question": "Mục tiêu \"cố gắng phấn đấu đến năm 2020 đưa Việt Nam cơ bản trở thành một nước công nghiệp theo hướng hiện đại\":",
      "options": [
        "A. Đại hội lần thứ VI (12/1986).",
        "B. Đại hội lần thứ VII (6/1991).",
        "C. Đại hội lần thứ X (4/2006).",
        "D. Đại hội lần thứ XI (1/2011)."
      ],
      "answer": ""
    },
    {
      "question": "Năm nào là mốc phấn đấu đưa đất nước ta cơ bản trở thành một nước công nghiệp theo hướng hiện đại?",
      "options": [
        "A. 2015",
        "B. 2020",
        "C. 2030",
        "D. 2050"
      ],
      "answer": ""
    },
    {
      "question": "Đại hội nào Đảng ta xác định: “Phải coi kinh tế tri thức là yếu tố quan trọng của nền kinh tế và CNH, HĐH”",
      "options": [
        "A. Đại hội lần thứ VII (6/1991).",
        "B. Đại hội lần thứ VIII (6/1996).",
        "C. Đại hội lần thứ IX (4/2001).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Sự khác biệt cơ bản giữa kinh tế thị trường định hướng xã hội chủ nghĩa với kinh tế thị trường tư bản chủ nghĩa ở chỗ?",
      "options": [
        "A. Bảo đảm vai trò quản lý, điều tiết nền kinh tế của Nhà nước pháp quyền xã hội chủ nghĩa dưới sự lãnh đạo của Đảng.",
        "B. Bảo đảm vai trò quản lý, điều tiết nền kinh tế của Nhà nước pháp quyền.",
        "C. Bảo đảm sự tồn tại của nhiều thành phần kinh tế.",
        "D. Là nền kinh tế hội nhập với kinh tế thế giới."
      ],
      "answer": ""
    },
    {
      "question": "Theo tư duy mới của Đảng từ đại hội VI (1986), kinh tế thị trường chỉ đối lập với:",
      "options": [
        "A. Kinh tế tự nhiên tự cấp, tự túc.",
        "B. Kinh tế tư bản chủ nghĩa.",
        "C. Kinh tế trong thời kỳ quá độ lên chủ nghĩa xã hội.",
        "D. Kinh tế xã hội chủ nghĩa."
      ],
      "answer": ""
    },
    {
      "question": "Quan điểm của Đảng :“Nền kinh tế thị trường định hướng XHCN là mô hình kinh tế tổng quát của nước ta trong thời kỳ quá độ lên CNXH” được xác định từ:",
      "options": [
        "A. Đại hội VI",
        "B. Đại hội VII",
        "C. Đại hội VIII",
        "D. Đại hội IX"
      ],
      "answer": ""
    },
    {
      "question": "Quan điểm: \"Kinh tế thị trường định hướng XHCN là một kiểu tổ chức kinh tế, vừa tuân theo quy luật của kinh tế thị trường, vừa dựa trên cơ sở và chịu sự dẫn dắt, chi phối bởi các nguyên tắc và bản chất của CNXH\" được xác định tại:",
      "options": [
        "A. Đại hội VI",
        "B. Đại hội VIII",
        "C. Đại hội IX",
        "D. Đại hội X"
      ],
      "answer": ""
    },
    {
      "question": "Nội dung nào dưới đây được đề ra trong Chỉ thị số 100 - CT/TW của Đảng (13/1/1981)?",
      "options": [
        "A. Mở rộng khoán sản phẩm đến nhóm lao động và người lao động trong hợp tác xã nông nghiệp.",
        "B. Đổi mới cơ chế kinh tế nông nghiệp: thực hiện cơ chế khoán sản phẩm cuối cùng đến nhóm hộ và hộ xã viên.",
        "C. Mở rộng hình thức trả lương sản phẩm và vận dụng hình thức tiền thưởng trong các đơn vị sản xuất kinh doanh của nhà nước."
      ],
      "answer": ""
    },
    {
      "question": "Chọn câu SAI khi nói về nền kinh tế kế hoạch hóa tập trung bao cấp?",
      "options": [
        "A. Nhà nước bao cấp qua giá.",
        "B. Nhà nước bao cấp qua chế độ tem phiếu.",
        "C. Nhà nước bao cấp theo chế độ cấp phát vốn.",
        "D. Các hình thức bao cấp trên đã ngừng thực hiện ở năm 1975."
      ],
      "answer": ""
    },
    {
      "question": "Việc duy trì cơ chế tập trung bao cấp của Đảng ta có nguyên nhân chủ yếu từ?",
      "options": [
        "A. Hoàn cảnh chiến tranh.",
        "B. Nhận thức không đầy đủ về những đặc trưng của thời kỳ quá độ lên chủ nghĩa xã hội.",
        "C. Tư duy độc lập dân tộc gắn với chủ nghĩa xã hội.",
        "D. Quan hệ với các nước trong hệ thống xã hội chủ nghĩa."
      ],
      "answer": ""
    },
    {
      "question": "Tại đại hội nào Đảng ta đã xác định cơ chế vận hành của nền kinh tế ở nước ta là “cơ chế thị trường có sự quản lý của Nhà nước bằng pháp luật, chính sách và các công cụ khác\"?",
      "options": [
        "A. Đại hội lần thứ VI (12/1986).",
        "B. Đại hội lần thứ VII (6/1991).",
        "C. Đại hội lần thứ IX (4/2001).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Đại hội nào đã xác định: Kinh tế thị trường định hướng xã hội chủ nghĩa là một kiểu tổ chức kinh tế vừa tuân theo quy luật của kinh tế thị trường vừa dựa trên cơ sở và chịu sự dẫn dắt chi phối bởi các nguyên tắc và bản chất của chủ nghĩa xã hội?",
      "options": [
        "A. Đại hội lần thứ VII (6/1991).",
        "B. Đại hội lần thứ VIII (6/1996).",
        "C. Đại hội lần thứ IX (4/2001).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Kinh tế thị trường có mầm mống từ trong xã hội nào?",
      "options": [
        "A. Phong kiến",
        "B. Tư bản chủ nghĩa",
        "C. Chiếm hữu nô lệ",
        "D. Xã hội chủ nghĩa."
      ],
      "answer": ""
    },
    {
      "question": "Theo tư duy mới, kinh tế thị trường chỉ đối lập với?",
      "options": [
        "A. Kinh tế tự nhiên tự cấp, tự túc.",
        "B. Kinh tế tư bản chủ nghĩa.",
        "C. Kinh tế trong thời kỳ quá độ lên chủ nghĩa xã hội.",
        "D. Kinh tế XHCN."
      ],
      "answer": ""
    },
    {
      "question": "Một trong những đặc trưng của nền kinh tế thị trường định hướng XHCN là?",
      "options": [
        "A. Gồm nhiều thành phần kinh tế.",
        "B. Gồm nhiều thành phần kinh tế, trong đó kinh tế nhà nước giữ vai trò chủ đạo.",
        "C. Gồm nhiều thành phần kinh tế, trong đó kinh tế tư nhân giữ vai trò chủ đạo.",
        "D. Gồm nhiều thành phần kinh tế, trong đó kinh tế tư bản nhà nước giữ vai trò chủ đạo."
      ],
      "answer": ""
    },
    {
      "question": "Nền kinh tế thị trường định hướng XHCN thực hiện nhiều hình thức phân phối thu nhập, trong đó?",
      "options": [
        "A. Phân phối bình quân là hình thức chủ yếu.",
        "B. Phân phối theo kết quả lao động là hình thức chủ yếu."
      ],
      "answer": ""
    }
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['questions'].extend(new_questions)
data['section'] = 'file2_page1_to_15'

with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully appended {len(new_questions)} questions from pages 11-15!")
