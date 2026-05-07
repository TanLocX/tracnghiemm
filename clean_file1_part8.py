import json

clean_questions = [
    # 258
    {
        "question": "Chọn đáp án đúng điền vào chỗ trống, trong Thư kêu gọi của Hồ Chí Minh (8/1945), gửi đồng bào và chiến sỹ cả nước: \"Giờ quyết định cho vận mệnh dân tộc ta đã đến, Toàn quốc đồng bào hãy đứng dậy, ..........\"",
        "options": [
            "A. Đem mọi lực lượng giải phóng đất nước ta",
            "B. Đem sức ta mà tự giải phóng cho ta",
            "C. Đem toàn lực mà tự giải phóng cho dân",
            "D. Đem sức người, sức của giải phóng đất nước ta"
        ],
        "answer": "B. Đem sức ta mà tự giải phóng cho ta"
    },
    # 259
    {
        "question": "Yếu tố khách quan nào đã góp phần tạo nên \"thời cơ ngàn năm có một\"?",
        "options": [
            "A. Nhật đảo chính Pháp",
            "B. Đức đầu hàng Đồng Minh",
            "C. Mỹ ném 2 quả bom nguyên tử xuống Nhật",
            "D. Phát xít Nhật đầu hàng Đồng Minh"
        ],
        "answer": "D. Phát xít Nhật đầu hàng Đồng Minh"
    },
    # 260
    {
        "question": "Trong Cách mạng tháng 8, lực lượng khởi nghĩa đã giành được chính quyền ở Hà Nội vào thời gian:",
        "options": [
            "A. Ngày 15/8/1945",
            "B. Ngày 19/8/1945",
            "C. Ngày 23/8/1945",
            "D. Ngày 25/8/1945"
        ],
        "answer": "B. Ngày 19/8/1945"
    },
    # 261
    {
        "question": "Khởi nghĩa giành chính quyền trong Cách mạng tháng 8 ở Huế diễn ra vào:",
        "options": [
            "A. Ngày 20/8/1945",
            "B. Ngày 22/8/1945",
            "C. Ngày 23/8/1945",
            "D. Ngày 24/8/1945"
        ],
        "answer": "C. Ngày 23/8/1945"
    },
    # 262
    {
        "question": "Khởi nghĩa giành chính quyền trong Cách mạng tháng 8 ở Sài Gòn diễn ra vào:",
        "options": [
            "A. Ngày 15/8/1945",
            "B. Ngày 19/8/1945",
            "C. Ngày 23/8/1945",
            "D. Ngày 25/8/1945"
        ],
        "answer": "D. Ngày 25/8/1945"
    },
    # 263
    {
        "question": "Lời tuyên bố của Hồ Chí Minh: \"Toàn thể dân tộc Việt Nam quyết đem tất cả tinh thần và lực lượng để giữ vững quyền tự do độc lập ấy\", được trích trong:",
        "options": [
            "A. Cương lĩnh đầu tiên của Đảng (năm 1930)",
            "B. Tuyên ngôn Độc lập (năm 1945)",
            "C. Lời kêu gọi toàn quốc kháng chiến 19-12-1946",
            "D. Hiến pháp đầu tiên của nước Việt Nam Dân chủ Cộng hòa"
        ],
        "answer": "B. Tuyên ngôn Độc lập (năm 1945)"
    },
    # 264
    {
        "question": "Sự kiện chấm dứt chiến tranh thế giới thứ hai ở Châu Âu:",
        "options": [
            "A. Nhật đảo chính Pháp",
            "B. Đức đầu hàng Đồng Minh",
            "C. Mỹ ném 2 quả bom nguyên tử xuống Nhật",
            "D. Phát xít Nhật đầu hàng Đồng Minh"
        ],
        "answer": "B. Đức đầu hàng Đồng Minh"
    },
    # 265
    {
        "question": "Tình cảnh nước ta sau Cách mạng tháng Tám được ví với hình ảnh:",
        "options": [
            "A. Phôi thai",
            "B. \"Ngàn cân treo sợi tóc\"",
            "C. Trứng nước",
            "D. Nếm mật nằm gai"
        ],
        "answer": "B. \"Ngàn cân treo sợi tóc\""
    },
    # 266
    {
        "question": "Ngày 25/11/1945 Ban Chấp hành Trung ương Đảng ra chỉ thị:",
        "options": [
            "A. Nhật - Pháp bắn nhau và hành động của chúng ta",
            "B. Kháng chiến, kiến quốc",
            "C. Hòa để tiến",
            "D. Toàn quốc kháng chiến"
        ],
        "answer": "B. Kháng chiến, kiến quốc"
    },
    # 267
    {
        "question": "Chỉ thị \"Kháng chiến, kiến quốc\" của Đảng xác định đâu là kẻ thù chính của Việt Nam?",
        "options": [
            "A. Nhật",
            "B. Đức",
            "C. Mỹ",
            "D. Pháp"
        ],
        "answer": "D. Pháp"
    },
    # 268
    {
        "question": "Quân Pháp đã mở cuộc tấn công chiếm đóng Hải Phòng, Lạng Sơn, đổ bộ lên Đà Nẵng vào thời gian nào?",
        "options": [
            "A. Tháng 11 năm 1945",
            "B. Tháng 11 năm 1946",
            "C. Tháng 11 năm 1947",
            "D. Tháng 11 năm 1948"
        ],
        "answer": "B. Tháng 11 năm 1946"
    },
    # 269
    {
        "question": "Đường lối kháng chiến chống thực dân Pháp của Đảng và Lời kêu gọi toàn quốc kháng chiến của Hồ Chí Minh ra đời vào thời gian nào?",
        "options": [
            "A. Tháng 12 năm 1945",
            "B. Tháng 12 năm 1946",
            "C. Tháng 2 năm 1947",
            "D. Tháng 5 năm 1948"
        ],
        "answer": "B. Tháng 12 năm 1946"
    },
    # 270
    {
        "question": "Trong đường lối kháng chiến chống thực dân Pháp (12/1946) của Đảng, phương châm kháng chiến của ta là:",
        "options": [
            "A. Kháng chiến toàn dân; Toàn diện; Lâu dài; Dựa vào sức mình là chính",
            "B. Kháng chiến trường kỳ; Toàn diện; Quyết liệt; Dựa vào sức mình và giúp đỡ quốc tế",
            "C. Kháng chiến toàn quốc; Toàn diện; Bền bỉ; Dựa vào nhân dân và giúp đỡ quốc tế",
            "D. Kháng chiến toàn lực; Toàn diện; Sáng tạo; Dựa vào đoàn kết toàn dân tộc"
        ],
        "answer": "A. Kháng chiến toàn dân; Toàn diện; Lâu dài; Dựa vào sức mình là chính"
    },
    # 271
    {
        "question": "Ngày 19/12/1946 Ban Thường vụ Trung ương Đảng họp hội nghị mở rộng tại làng Vạn Phúc, Hà Đông đã quyết định:",
        "options": [
            "A. Chấp nhận những yêu sách trong Tối hậu thư của Pháp",
            "B. Tiếp tục hòa hoãn để chuẩn bị lực lượng",
            "C. Phát động cuộc kháng chiến chống Thực dân Pháp trong cả nước",
            "D. Tiến hành Tổng khởi nghĩa"
        ],
        "answer": "C. Phát động cuộc kháng chiến chống Thực dân Pháp trong cả nước"
    },
    # 272
    {
        "question": "Cuộc kháng chiến của nhân dân ta chống xâm lược Pháp (lần thứ 2), hiệu lệnh bằng \"Lời kêu gọi toàn quốc kháng chiến của Hồ Chủ tịch\", được phát trên đài tiếng nói Việt Nam vào thời gian nào:",
        "options": [
            "A. Rạng sáng ngày 19/12/1946",
            "B. Rạng sáng ngày 20/12/1946",
            "C. Rạng sáng ngày 21/12/1946",
            "D. Rạng sáng ngày 22/12/1946"
        ],
        "answer": "A. Rạng sáng ngày 19/12/1946"
    },
    # 273
    {
        "question": "Những văn kiện nào sau đây thể hiện nội dung đường lối kháng chiến chống thực dân Pháp của Đảng (tháng 12/1946):",
        "options": [
            "A. Chỉ thị Toàn dân chiến đấu của Trung ương Đảng",
            "B. Tuyên ngôn độc lập của Hồ Chủ tịch",
            "C. Tác phẩm: \"Chiến đấu trong vòng vây\" của Đại tướng Võ Nguyên Giáp",
            "D. Tác phẩm: \"Kháng chiến nhất định thắng lợi\" của Tổng Bí thư Trường Chinh"
        ],
        "answer": "A. Chỉ thị Toàn dân chiến đấu của Trung ương Đảng"
    },
    # 274
    {
        "question": "Tháng 2 năm 1951, Đại hội đại biểu lần thứ II của Đảng Cộng sản Đông Dương, tại tỉnh Tuyên Quang, đã ra Nghị quyết quan trọng:",
        "options": [
            "A. Xây dựng chiến khu cách mạng",
            "B. Xây dựng lực lượng, chuẩn bị khởi nghĩa vũ trang",
            "C. Chia tách Đảng Cộng sản Đông Dương thành 3 Đảng để lãnh đạo cách mạng 3 nước",
            "D. Đề ra đường lối Chiến tranh du kích, trường kỳ kháng chiến"
        ],
        "answer": "C. Chia tách Đảng Cộng sản Đông Dương thành 3 Đảng để lãnh đạo cách mạng 3 nước"
    },
    # 275
    {
        "question": "Đại hội II của Đảng diễn ra vào thời gian nào và đổi tên là:",
        "options": [
            "A. Tháng 2/1930, lấy tên là Đảng Cộng sản Việt Nam",
            "B. Tháng 8/1945, lấy tên là Đảng Cách mạng Việt Nam",
            "C. Tháng 2/1951, lấy tên là Đảng Lao động Việt Nam",
            "D. Tháng 7/1954, lấy tên là Đảng Cộng sản Việt Nam"
        ],
        "answer": "C. Tháng 2/1951, lấy tên là Đảng Lao động Việt Nam"
    },
    # 276
    {
        "question": "Hiệp định về chấm dứt chiến tranh, lập lại hòa bình ở Đông Dương, được ký kết ở địa điểm và thời gian:",
        "options": [
            "A. Pari (Pháp), ngày 27/01/1953",
            "B. Giơnevơ (Thụy Sĩ), ngày 21/07/1954",
            "C. Bruxen (Bỉ), ngày 27/01/1955",
            "D. Hà Nội (Việt Nam), ngày 27/01/1972"
        ],
        "answer": "B. Giơnevơ (Thụy Sĩ), ngày 21/07/1954"
    },
    # 277
    {
        "question": "Thắng lợi làm thất bại âm mưu \"đánh nhanh thắng nhanh\" của thực dân Pháp là thắng lợi của chiến dịch:",
        "options": [
            "A. Điện Biên Phủ",
            "B. Biên giới",
            "C. Khe Sanh",
            "D. Việt Bắc"
        ],
        "answer": "D. Việt Bắc"
    },
    # 278
    {
        "question": "Thắng lợi của quân và dân ta đánh dấu chúng ta đã giành được quyền chủ động trên chiến trường chính Bắc Bộ:",
        "options": [
            "A. Điện Biên Phủ",
            "B. Biên giới",
            "C. Ấp Bắc",
            "D. Việt Bắc"
        ],
        "answer": "B. Biên giới"
    },
    # 279
    {
        "question": "Hội nghị Trung ương lần thứ 15 của Đảng (tháng 1/1959), đề ra hai nhiệm vụ chiến lược gồm:",
        "options": [
            "A. Cách mạng xã hội chủ nghĩa ở miền Bắc và cách mạng dân tộc dân chủ nhân dân ở miền Nam",
            "B. Cách mạng bảo vệ Tổ quốc ở miền Bắc và cách mạng giải phóng dân tộc ở miền Nam",
            "C. Cách mạng dân chủ nhân dân ở miền Bắc và cách mạng giành chính quyền ở miền Nam",
            "D. Cách mạng dân chủ xã hội ở miền Bắc và cách mạng dân chủ nhân dân ở miền Nam"
        ],
        "answer": "A. Cách mạng xã hội chủ nghĩa ở miền Bắc và cách mạng dân tộc dân chủ nhân dân ở miền Nam"
    },
    # 280
    {
        "question": "Đại hội lần thứ III của Đảng được diễn ra ở đâu và vào thời gian:",
        "options": [
            "A. Ở Hương Cảng, vào tháng 5/1945",
            "B. Ở Tân Trào, vào tháng 3/1950",
            "C. Ở Việt Bắc, vào tháng 7/1954",
            "D. Ở Hà Nội, vào tháng 9/1960"
        ],
        "answer": "D. Ở Hà Nội, vào tháng 9/1960"
    },
    # 281
    {
        "question": "Hội nghị TW Đảng lần thứ 11 và lần thứ 12 đã dựa trên bối cảnh lịch sử nào để đề ra đường lối kháng chiến chống Mỹ, cứu nước trên cả nước:",
        "options": [
            "A. Mỹ gây chiến tranh cục bộ ở miền Nam và đưa chiến tranh phá hoại ra miền Bắc",
            "B. Mỹ gây chiến tranh đặc biệt ở miền Nam và gây hấn ở vịnh Bắc Bộ",
            "C. Mỹ gây chiến tranh đơn phương ở miền Nam và leo thang bắn phá miền Bắc",
            "D. Mỹ thực hiện \"Việt Nam hóa chiến tranh\" ở miền Nam và âm mưu đánh ra miền Bắc"
        ],
        "answer": "B. Mỹ gây chiến tranh đặc biệt ở miền Nam và gây hấn ở vịnh Bắc Bộ"
    },
    # 282
    {
        "question": "Hội nghị TW Đảng lần thứ 11 (3/1965) và lần thứ 12 (12/1965) đã đề ra đường lối:",
        "options": [
            "A. Kháng chiến chống Mỹ, giải phóng miền Nam",
            "B. Kháng chiến chống Mỹ ở miền Nam, bảo vệ miền Bắc XHCN",
            "C. Kháng chiến chống Mỹ, cứu nước trên cả nước",
            "D. Kháng chiến chống Mỹ, thống nhất đất nước"
        ],
        "answer": "C. Kháng chiến chống Mỹ, cứu nước trên cả nước"
    },
    # 283
    {
        "question": "Thắng lợi nào có ý nghĩa chuyển cách mạng Miền Nam từ thế giữ gìn lực lượng sang tiến công:",
        "options": [
            "A. Ấp Bắc",
            "B. Vạn Tường",
            "C. Đồng Khởi",
            "D. Điện Biên Phủ trên không"
        ],
        "answer": "C. Đồng Khởi"
    },
    # 284
    {
        "question": "Sau khi Chiến tranh \"đơn phương\" thất bại, đế quốc Mỹ đã chuyển sang chiến lược:",
        "options": [
            "A. Chiến tranh cục bộ",
            "B. Chiến tranh Việt Nam hóa",
            "C. Chiến tranh đặc biệt",
            "D. Chiến tranh phá hoại"
        ],
        "answer": "C. Chiến tranh đặc biệt"
    },
    # 285
    {
        "question": "Chiến lược chiến tranh ở Việt Nam mà theo đó, Mỹ trực tiếp đổ quân ồ ạt vào Miền Nam là:",
        "options": [
            "A. Chiến tranh đặc biệt (1961 - 1965)",
            "B. Chiến tranh cục bộ (1965 - 1968)",
            "C. Việt Nam hóa chiến tranh (1969 - 1975)",
            "D. Chiến tranh đơn phương"
        ],
        "answer": "B. Chiến tranh cục bộ (1965 - 1968)"
    },
    # 286
    {
        "question": "Thắng lợi nào đã buộc Mỹ chấp thuận ngồi đàm phán với chúng ta ở hội nghị Paris:",
        "options": [
            "A. Điện Biên Phủ",
            "B. Mậu Thân 1968",
            "C. Chiến dịch mùa khô 1972",
            "D. Điện Biên Phủ trên không"
        ],
        "answer": "B. Mậu Thân 1968"
    },
    # 287
    {
        "question": "Thắng lợi buộc Mỹ phải ký kết hiệp định Paris theo điều khoản chúng ta đưa ra là:",
        "options": [
            "A. Điện Biên Phủ",
            "B. Mậu Thân 1968",
            "C. Chiến dịch mùa khô 1972",
            "D. Điện Biên Phủ trên không 1972"
        ],
        "answer": "D. Điện Biên Phủ trên không 1972"
    },
    # 288
    {
        "question": "Sau phong trào Đồng Khởi 1960 mặt trận được thành lập ở Miền Nam là:",
        "options": [
            "A. Mặt trận dân tộc Miền Nam thống nhất",
            "B. Mặt trận dân tộc Cộng hòa Miền Nam Việt Nam",
            "C. Mặt trận dân tộc Dân chủ Miền Nam",
            "D. Mặt trận dân tộc giải phóng Miền Nam Việt Nam"
        ],
        "answer": "D. Mặt trận dân tộc giải phóng Miền Nam Việt Nam"
    },
    # 289
    {
        "question": "Chiến dịch mở đầu cho cuộc Tổng tiến công giải phóng miền Nam là:",
        "options": [
            "A. Chiến dịch Đà Nẵng",
            "B. Chiến dịch Đông-Nam Bộ",
            "C. Chiến dịch Tây Nguyên",
            "D. Chiến dịch Hồ Chí Minh"
        ],
        "answer": "C. Chiến dịch Tây Nguyên"
    },
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_idx = 258
for i in range(len(clean_questions)):
    data['questions'][start_idx + i] = clean_questions[i]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully cleaned questions {start_idx} to {start_idx + len(clean_questions) - 1}!")
