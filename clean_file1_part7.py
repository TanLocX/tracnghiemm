import json

clean_questions = [
    # 224
    {
        "question": "Cương lĩnh xây dựng đất nước trong thời kỳ quá độ lên chủ nghĩa xã hội được thông qua trong Đại hội nào của Đảng?",
        "options": [
            "A. Đại hội VI",
            "B. Đại hội VII",
            "C. Đại hội VIII",
            "D. Đại hội IX"
        ],
        "answer": "B. Đại hội VII"
    },
    # 225
    {
        "question": "Văn kiện nào dưới đây đã giúp Nguyễn Ái Quốc tìm thấy con đường cứu nước?",
        "options": [
            "A. Bản yêu sách 8 điểm của nhân dân An Nam",
            "B. Cương lĩnh chính trị đầu tiên của Đảng",
            "C. Sơ thảo lần thứ nhất Luận cương về vấn đề dân tộc và thuộc địa của Lênin",
            "D. Tuyên bố của mặt trận Việt Minh"
        ],
        "answer": "C. Sơ thảo lần thứ nhất Luận cương về vấn đề dân tộc và thuộc địa của Lênin"
    },
    # 226
    {
        "question": "Tính chất xã hội Việt Nam thời kỳ Pháp thuộc là:",
        "options": [
            "A. Xã hội phong kiến.",
            "B. Xã hội tư bản.",
            "C. Xã hội thuộc địa nửa phong kiến.",
            "D. Xã hội phong kiến nửa thực dân."
        ],
        "answer": "C. Xã hội thuộc địa nửa phong kiến."
    },
    # 227
    {
        "question": "Mâu thuẫn chủ yếu của xã hội Việt Nam đầu thế kỷ 20 là mâu thuẫn giữa:",
        "options": [
            "A. Nhân dân Việt Nam với địa chủ phong kiến.",
            "B. Công nhân Việt Nam với tư sản Việt Nam.",
            "C. Công nhân Việt Nam với tư sản Pháp.",
            "D. Dân tộc Việt Nam với thực dân Pháp và tay sai phản động."
        ],
        "answer": "D. Dân tộc Việt Nam với thực dân Pháp và tay sai phản động."
    },
    # 228
    {
        "question": "Tháng 6/1925 Nguyễn Ái Quốc đã thành lập tổ chức:",
        "options": [
            "A. Hội Liên hiệp các dân tộc thuộc địa.",
            "B. Hội Liên hiệp các dân tộc bị áp bức Á Đông",
            "C. Hội Việt Nam thanh niên cách mạng đồng chí hội",
            "D. Hội Việt Nam cách mạng thanh niên"
        ],
        "answer": "D. Hội Việt Nam cách mạng thanh niên"
    },
    # 229
    {
        "question": "Một trong những lãnh tụ của phong trào Cần Vương (1885-1896) là:",
        "options": [
            "A. Vua Hàm Nghi.",
            "B. Phan Bội Châu.",
            "C. Phan Chu Trinh.",
            "D. Hoàng Hoa Thám."
        ],
        "answer": "A. Vua Hàm Nghi."
    },
    # 230
    {
        "question": "Người chủ trương dùng biện pháp bạo động, dựa vào Nhật để đánh Pháp là:",
        "options": [
            "A. Nguyễn An Ninh",
            "B. Phan Chu Trinh.",
            "C. Hoàng Hoa Thám.",
            "D. Phan Bội Châu."
        ],
        "answer": "D. Phan Bội Châu."
    },
    # 231
    {
        "question": "Người chủ trương dùng cải cách, đòi Pháp trả độc lập cho Việt Nam là:",
        "options": [
            "A. Phan Chu Trinh.",
            "B. Phan Bội Châu.",
            "C. Hoàng Hoa Thám.",
            "D. Nguyễn An Ninh"
        ],
        "answer": "A. Phan Chu Trinh."
    },
    # 232
    {
        "question": "Người nêu quan điểm (vào cuối năm 1920): \"Muốn cứu nước và giải phóng dân tộc không có con đường nào khác con đường cách mạng vô sản.\" là:",
        "options": [
            "A. V.I.Lênin.",
            "B. Lê Hồng Phong",
            "C. Nguyễn Ái Quốc.",
            "D. Trần Phú."
        ],
        "answer": "C. Nguyễn Ái Quốc."
    },
    # 233
    {
        "question": "Nguyễn Ái Quốc đã bỏ phiếu tán thành gia nhập Quốc tế Cộng sản và tham gia thành lập Đảng Cộng sản Pháp vào thời gian:",
        "options": [
            "A. Tháng 10-1920",
            "B. Tháng 12-1920",
            "C. Tháng 12-1921",
            "D. Tháng 12-1923"
        ],
        "answer": "B. Tháng 12-1920"
    },
    # 234
    {
        "question": "Đảng Cộng sản Việt Nam ra đời là sản phẩm của sự kết hợp các yếu tố:",
        "options": [
            "A. Chủ nghĩa Mác-Lênin, phong trào công nhân, phong trào yêu nước",
            "B. Chủ nghĩa Mác và phong trào công nhân",
            "C. Chủ nghĩa Mác-Lênin, phong trào công nhân, phong trào nông dân",
            "D. Chủ nghĩa Mác-Lênin, phong trào yêu nước"
        ],
        "answer": "A. Chủ nghĩa Mác-Lênin, phong trào công nhân, phong trào yêu nước"
    },
    # 235
    {
        "question": "Tác phẩm nào của Nguyễn Ái Quốc, được xuất bản năm 1927, đã chỉ ra phương hướng chiến lược, sách lược của cách mạng giải phóng dân tộc Việt Nam?",
        "options": [
            "A. Bản án chế độ thực dân Pháp",
            "B. Đường kách mệnh",
            "C. Chánh cương vắn tắt",
            "D. Sửa đổi lối làm việc."
        ],
        "answer": "B. Đường kách mệnh"
    },
    # 236
    {
        "question": "Hội nghị đánh dấu hoàn thiện chuyển hướng chỉ đạo chiến lược 1939-1945 là:",
        "options": [
            "A. Hội nghị trung ương 6, khóa I",
            "B. Hội nghị trung ương 7, khóa I",
            "C. Hội nghị trung ương 8, khóa I",
            "D. Hội nghị trung ương 9, khóa I"
        ],
        "answer": "C. Hội nghị trung ương 8, khóa I"
    },
    # 237
    {
        "question": "Hội nghị thành lập Đảng (năm 1930) diễn ra ở đâu / do ai chủ trì?",
        "options": [
            "A. Ở Quảng Châu / Do Lê Hồng Phong chủ trì",
            "B. Ở Hương Cảng / Do Nguyễn Ái Quốc chủ trì",
            "C. Ở Tân Trào / Do Hà Huy Tập chủ trì",
            "D. Ở Hà Nội / Do Trường Chinh chủ trì"
        ],
        "answer": "B. Ở Hương Cảng / Do Nguyễn Ái Quốc chủ trì"
    },
    # 238
    {
        "question": "Hội nghị thành lập Đảng (tháng 1/1930) đã lấy tên Đảng là:",
        "options": [
            "A. Đảng Lao động Việt Nam",
            "B. Đảng Cộng sản Đông Dương",
            "C. Đảng Cộng sản Việt Nam",
            "D. Đảng Xã hội Việt Nam"
        ],
        "answer": "C. Đảng Cộng sản Việt Nam"
    },
    # 239
    {
        "question": "Cương lĩnh đầu tiên (Cương lĩnh tháng 2) của Đảng, xác định phương hướng chiến lược của Cách mạng Việt Nam là:",
        "options": [
            "A. Cách mạng giành độc lập dân tộc, dân chủ nhân dân, tiến tới xã hội đại đồng",
            "B. Làm tư sản dân quyền cách mạng và thổ địa cách mạng để đi tới xã hội cộng sản",
            "C. Làm cách mạng dân chủ chia ruộng đất cho dân cày, tiến tới độc lập, tự do",
            "D. Cách mạng cộng sản"
        ],
        "answer": "B. Làm tư sản dân quyền cách mạng và thổ địa cách mạng để đi tới xã hội cộng sản"
    },
    # 240
    {
        "question": "Người soạn Cương lĩnh chính trị đầu tiên của Đảng là:",
        "options": [
            "A. Trần Phú",
            "B. Nguyễn Ái Quốc",
            "C. Lê Hồng Phong",
            "D. Hà Huy Tập"
        ],
        "answer": "B. Nguyễn Ái Quốc"
    },
    # 241
    {
        "question": "Hội nghị toàn quốc của Đảng Cộng sản Đông Dương họp ở Tân Trào diễn ra vào thời gian nào?",
        "options": [
            "A. 15-19/8/1945",
            "B. 13-15/8/1945",
            "C. 16/8/1945",
            "D. 17/8/1945"
        ],
        "answer": "B. 13-15/8/1945"
    },
    # 242
    {
        "question": "Văn kiện nào đã nhấn mạnh: \"Vấn đề thổ địa là cốt lõi của cách mạng tư sản dân quyền\"?",
        "options": [
            "A. Luận cương chính trị",
            "B. Cương lĩnh tháng 2",
            "C. Chính cương vắn tắt",
            "D. Sách lược vắn tắt"
        ],
        "answer": "A. Luận cương chính trị"
    },
    # 243
    {
        "question": "Hội nghị Ban chấp hành Trung ương Đảng lần thứ nhất (10-1930), lấy tên Đảng và bầu Tổng Bí thư là:",
        "options": [
            "A. Đảng Lao động Đông Dương / Nguyễn Ái Quốc là Tổng Bí thư",
            "B. Đảng Lao động Việt Nam / Lê Hồng Phong là Tổng Bí thư",
            "C. Đảng Cộng sản Việt Nam / Hà Huy Tập là Tổng Bí thư",
            "D. Đảng Cộng sản Đông Dương / Trần Phú là Tổng Bí thư"
        ],
        "answer": "D. Đảng Cộng sản Đông Dương / Trần Phú là Tổng Bí thư"
    },
    # 244
    {
        "question": "Luận cương chính trị tháng 10-1930 xác định mâu thuẫn chủ yếu ở Đông Dương là:",
        "options": [
            "A. Các dân tộc Đông Dương với đế quốc Pháp và phong kiến, địa chủ, tay sai đế quốc",
            "B. Nhân dân Đông Dương chủ yếu là dân cày với địa chủ phong kiến và chủ nghĩa đế quốc.",
            "C. Thợ thuyền, dân cày và các phần tử lao khổ với địa chủ, phong kiến, và tư bản đế quốc",
            "D. Công nhân, nông dân, trí thức Đông Dương với đế quốc Pháp và tay sai, phản động"
        ],
        "answer": "A. Các dân tộc Đông Dương với đế quốc Pháp và phong kiến, địa chủ, tay sai đế quốc"
    },
    # 245
    {
        "question": "Luận cương chính trị tháng 10-1930 xác định \"cái cốt của cách mạng tư sản dân quyền\" là:",
        "options": [
            "A. Vấn đề dân tộc.",
            "B. Vấn đề thổ địa.",
            "C. Vấn đề giành chính quyền.",
            "D. Vấn đề dân chủ."
        ],
        "answer": "B. Vấn đề thổ địa."
    },
    # 246
    {
        "question": "Về lực lượng cách mạng, Luận cương Chính trị tháng 10-1930 xác định:",
        "options": [
            "A. Tất cả các dân tộc ở Đông Dương.",
            "B. Mọi giai cấp, tầng lớp chống đế quốc Pháp.",
            "C. Giai cấp vô sản và dân cày",
            "D. Giai cấp công nhân; nông dân; binh lính và trí thức yêu nước."
        ],
        "answer": "C. Giai cấp vô sản và dân cày"
    },
    # 247
    {
        "question": "Địa điểm và thời gian diễn ra Đại hội lần thứ nhất của Đảng Cộng sản Đông Dương:",
        "options": [
            "A. Macao / Tháng 3 năm 1935",
            "B. Hương Cảng / Tháng 3 năm 1930",
            "C. Tân Trào / Tháng 8 năm 1945",
            "D. Bắc Thái / Tháng 5 năm 1951"
        ],
        "answer": "A. Macao / Tháng 3 năm 1935"
    },
    # 248
    {
        "question": "Về phương pháp cách mạng, Luận cương 10/1930 xác định theo con đường:",
        "options": [
            "A. Vũ trang bạo động",
            "B. Trường kỳ mai phục",
            "C. Chiến tranh du kích",
            "D. Đấu tranh nghị trường"
        ],
        "answer": "A. Vũ trang bạo động"
    },
    # 249
    {
        "question": "Hội nghị Trung ương của Đảng mở đầu cho chủ trương chuyển hướng chỉ đạo chiến lược giai đoạn năm 1939-1945 là:",
        "options": [
            "A. Hội nghị Trung ương lần thứ 6 - tháng 11/1939",
            "B. Hội nghị Trung ương lần thứ 7 - tháng 11/1940",
            "C. Hội nghị Trung ương lần thứ 8 - tháng 5/1941",
            "D. Hội nghị Trung ương lần thứ 9 - tháng 8/1945"
        ],
        "answer": "A. Hội nghị Trung ương lần thứ 6 - tháng 11/1939"
    },
    # 250
    {
        "question": "Nội dung chủ trương chuyển hướng chỉ đạo chiến lược giai đoạn năm 1939-1945:",
        "options": [
            "A. Đưa nhiệm vụ đấu tranh giai cấp lên hàng đầu",
            "B. Quyết định tiến hành Tổng khởi nghĩa",
            "C. Quyết định thành lập chiến khu Việt Bắc",
            "D. Đưa vấn đề giải phóng dân tộc lên hàng đầu"
        ],
        "answer": "D. Đưa vấn đề giải phóng dân tộc lên hàng đầu"
    },
    # 251
    {
        "question": "Nguyễn Ái Quốc về nước khi nào và chủ trì Hội nghị Trung ương Đảng lần mấy?",
        "options": [
            "A. Ngày 28-01-1939 / Chủ trì Hội nghị TW 6 (tháng 11/1939)",
            "B. Ngày 28-01-1941 / Chủ trì Hội nghị TW lần 8 (tháng 5/1941)",
            "C. Ngày 28-01-1942 / Chủ trì Hội nghị TW lần 7 (tháng 11/1940)",
            "D. Ngày 28-01-1943 / Chủ trì Hội nghị TW lần 9 (tháng 11/1944)."
        ],
        "answer": "B. Ngày 28-01-1941 / Chủ trì Hội nghị TW lần 8 (tháng 5/1941)"
    },
    # 252
    {
        "question": "Ý nghĩa của sự chuyển hướng chỉ đạo chiến lược đối với sự thành công của Cách mạng tháng 8/1945:",
        "options": [
            "A. Đổi tên Đảng",
            "B. Lực lượng vũ trang và các căn cứ cách mạng được xây dựng",
            "C. Giải quyết mục tiêu số 1 của cách mạng Việt Nam",
            "D. Quyết định tổng khởi nghĩa"
        ],
        "answer": "C. Giải quyết mục tiêu số 1 của cách mạng Việt Nam"
    },
    # 253
    {
        "question": "Từ năm 1940 nhân dân Việt Nam chịu cảnh \"một cổ hai tròng\", đó gồm 2 kẻ thù:",
        "options": [
            "A. Pháp và Mỹ",
            "B. Pháp và Tưởng Giới Thạch",
            "C. Nhật và Pháp",
            "D. Nhật và Tưởng Giới Thạch"
        ],
        "answer": "C. Nhật và Pháp"
    },
    # 254
    {
        "question": "Sự kiện nào tạo nên cuộc khủng hoảng chính trị ở Đông Dương dẫn đến phong trào kháng Nhật cứu nước?",
        "options": [
            "A. Nhật đầu hàng Đồng Minh",
            "B. Nhật đảo chính Pháp",
            "C. Nhật nhảy vào Đông Dương",
            "D. Nạn đói 1945"
        ],
        "answer": "B. Nhật đảo chính Pháp"
    },
    # 255
    {
        "question": "Trong chỉ thị \"Nhật - Pháp bắn nhau và hành động của chúng ta\" (12/3/1945), Ban Thường vụ TW Đảng xác định thời cơ tổng khởi nghĩa:",
        "options": [
            "A. Đã chín muồi",
            "B. Chưa chín muồi",
            "C. Nhanh chóng chín muồi",
            "D. Đã trôi qua"
        ],
        "answer": "B. Chưa chín muồi"
    },
    # 256
    {
        "question": "Trong chỉ thị \"Nhật - Pháp bắn nhau và hành động của chúng ta\", Ban Thường vụ TW Đảng xác định kẻ thù của nhân dân Đông Dương lúc này là:",
        "options": [
            "A. Phát xít Nhật và Pháp",
            "B. Phát xít Nhật",
            "C. Phát xít Pháp",
            "D. Thực dân Pháp và tay sai"
        ],
        "answer": "B. Phát xít Nhật"
    },
    # 257
    {
        "question": "Câu nói \"Dù phải đốt cháy cả dãy Trường Sơn cũng phải giành cho được độc lập\" của Hồ Chí Minh được nói vào thời gian:",
        "options": [
            "A. Tháng 8/1945",
            "B. Tháng 9/1950",
            "C. Tháng 1/1954",
            "D. Tháng 1/1968"
        ],
        "answer": "A. Tháng 8/1945"
    },
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_idx = 224
for i in range(len(clean_questions)):
    data['questions'][start_idx + i] = clean_questions[i]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully cleaned questions {start_idx} to {start_idx + len(clean_questions) - 1}!")
print(f"Total questions cleaned: {len(clean_questions)}")
