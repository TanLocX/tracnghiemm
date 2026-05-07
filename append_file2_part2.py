import json

new_questions = [
    {
      "question": "Ngày 19/12/1946 Ban Thường vụ T.Ư Đảng họp hội nghị mở rộng tại làng Vạn Phúc, Hà Đông đã quyết định:",
      "options": [
        "A. Chấp nhận những yêu sách trong Tối hậu thư của Pháp",
        "B. Tiếp tục hòa hoãn để chuẩn bị lực lượng",
        "C. Phát động cuộc kháng chiến chống Thực dân Pháp trong cả nước",
        "D. Tiến hành Tổng khởi nghĩa"
      ],
      "answer": ""
    },
    {
      "question": "Những văn kiện nào sau đây thể hiện nội dung đường lối kháng chiến chống thực dân Pháp của Đảng (tháng 12/1946):",
      "options": [
        "A. Chỉ thị Toàn dân chiến đấu của Trung ương Đảng",
        "B. Tuyên ngôn độc lập của Hồ Chủ tịch",
        "C. Tác phẩm: \"Chiến đấu trong vòng vây” của Đại tướng Võ Nguyên Giáp",
        "D. Tác phẩm: “Kháng chiến nhất định thắng lợi” của Tổng Bí thư Trường Chinh"
      ],
      "answer": ""
    },
    {
      "question": "Chỉ ra chỗ sai khi nói về ý nghĩa lịch sử của cuộc kháng chiến chống thực dân Pháp và can thiệp Mỹ (1945 - 1954):",
      "options": [
        "A. Chấm dứt ách thống trị của chủ nghĩa thực dân cũ gần một thế kỷ.",
        "B. Bảo vệ được thành quả cách mạng Tháng 8, giải phóng hoàn toàn miền Bắc.",
        "C. Góp phần cổ vũ mạnh mẽ các dân tộc thuộc địa vùng lên giành độc lập.",
        "D. Hoàn thành cách mạng dân tộc dân chủ nhân dân trên phạm vi cả nước."
      ],
      "answer": ""
    },
    {
      "question": "Hiệp định Giơnevơ quy định:",
      "options": [
        "A. Các nước tôn trọng quyền dân tộc cơ bản của nhân dân Việt Nam.",
        "B. Các nước tôn trọng quyền dân tộc cơ bản của nhân dân Lào.",
        "C. Các nước tôn trọng quyền dân tộc cơ bản của nhân dân Campuchia.",
        "D. Các nước tôn trọng quyền dân tộc cơ bản của nhân dân Việt Nam, Lào, Campuchia."
      ],
      "answer": ""
    },
    {
      "question": "Tại Đại hội nào Đảng nhấn mạnh: “Đảng lao động Việt Nam là đảng của giai cấp công nhân và nhân dân Việt Nam”?",
      "options": [
        "A. Đại hội lần thứ I.",
        "B. Đại hội lần thứ II.",
        "C. Đại hội lần thứ III.",
        "D. Đại hội lần thứ IV."
      ],
      "answer": ""
    },
    {
      "question": "Lời kêu gọi của Hồ Chủ tịch: \"...Chúng ta thà hy sinh tất cả chứ nhất định không chịu mất nước, không chịu làm nô lệ...” trong văn kiện nào?",
      "options": [
        "A. Lời kêu gọi nhân dịp thành lập Đảng Cộng sản Việt Nam (2/1930)",
        "B. Lời kêu gọi toàn quốc khởi nghĩa (8/1945)",
        "C. Lời kêu gọi toàn quốc kháng chiến (12/1946)",
        "D. Lời kêu gọi kháng chiến chống Mỹ (7/1966)"
      ],
      "answer": ""
    },
    {
      "question": "Chiến công nào được ghi vào lịch sử dân tộc: “như một Bạch Đằng, một Chi Lăng hay một Đống Đa trong thế kỷ XX và đi vào lịch sử thế giới như một chiến công hiển hách, báo hiệu sự thắng lợi của nhân dân các dân tộc bị áp bức, sự sụp đổ của chủ nghĩa thực dân”?",
      "options": [
        "A. Chiến thắng của chiến dịch Biên giới thu - đông (1950)",
        "B. Chiến thắng Điện Biên Phủ (1954)",
        "C. Chiến thắng Điện Biên Phủ trên không (1972)",
        "D. Chiến thắng của chiến dịch Hồ Chí Minh (1975)"
      ],
      "answer": ""
    },
    {
      "question": "Tháng 2 năm 1951, Đại hội đại biểu lần thứ II của Đảng Cộng sản Đông Dương tại tỉnh Tuyên Quang, đã ra Nghị quyết quan trọng:",
      "options": [
        "A. Xây dựng chiến khu cách mạng",
        "B. Xây dựng lực lượng, chuẩn bị khởi nghĩa vũ trang",
        "C. Chia tách Đảng Cộng sản Đông Dương thành 3 Đảng để lãnh đạo cách mạng 3 nước",
        "D. Đề ra đường lối Chiến tranh du kích, trường kỳ kháng chiến"
      ],
      "answer": ""
    },
    {
      "question": "Đại hội II của Đảng diễn ra vào thời gian nào và đổi tên là:",
      "options": [
        "A. Tháng 2/1930, lấy tên là Đảng Cộng sản Việt Nam",
        "B. Tháng 8/1945, lấy tên là Đảng Cách mạng Việt Nam",
        "C. Tháng 2/1951, lấy tên là Đảng Lao động Việt Nam",
        "D. Tháng 7/1954, lấy tên là Đảng Cộng sản Việt Nam"
      ],
      "answer": ""
    },
    {
      "question": "Nghị quyết nào của Đảng mở đường cho cao trào “Đồng khởi” ở miền Nam?",
      "options": [
        "A. Nghị quyết Ban chấp hành TW lần thứ 15 (1/1959)",
        "B. Nghị quyết Ban chấp hành TW lần thứ 11 (3/1965)",
        "C. Nghị quyết Ban chấp hành TW lần thứ 12 (12/1965)",
        "D. Nghị quyết Ban chấp hành TW lần thứ 14 (1/1968)"
      ],
      "answer": ""
    },
    {
      "question": "Mặt trận giải phóng dân tộc miền Nam Việt Nam được thành lập nhằm:",
      "options": [
        "A. Tập hợp quần chúng nhân dân miền Nam đứng lên chống Mỹ, cứu nước.",
        "B. Tập hợp quần chúng nhân dân miền Nam đứng lên chống Pháp.",
        "C. Tập hợp quần chúng nhân dân miền Nam đứng lên làm Cách mạng tháng Tám.",
        "D. Tập hợp quần chúng nhân dân miền Nam đứng lên chống phát xít Nhật xâm lược."
      ],
      "answer": ""
    },
    {
      "question": "Hồ Chí Minh khẳng định \"Không có gì quý hơn độc lập tự do” trong:",
      "options": [
        "A. Lời kêu gọi toàn quốc khởi nghĩa (8/1945)",
        "B. Lời kêu gọi toàn quốc kháng chiến (19/12/1946)",
        "C. Lời kêu gọi kháng chiến chống Mỹ cứu nước (17/7/1966)",
        "D. Di chúc của Hồ Chí Minh (1969)"
      ],
      "answer": ""
    },
    {
      "question": "Thắng lợi nào: “Mãi mãi được ghi vào lịch sử dân tộc như một trang chói lọi nhất, một biểu tượng sáng ngời về sự toàn thắng... đi vào lịch sử thế giới như một chiến công vĩ đại của thế kỷ XX, một sự kiện có tầm quan trọng quốc tế to lớn và tính thời đại sâu sắc”?",
      "options": [
        "A. Thắng lợi của Cách mạng Tháng 8.",
        "B. Thắng lợi của cuộc kháng chiến chống thực dân Pháp xâm lược.",
        "C. Thắng lợi của cuộc kháng chiến chống Mỹ xâm lược.",
        "D. Thắng lợi của cuộc chiến tranh bảo vệ biên giới phía Bắc (1979)."
      ],
      "answer": ""
    },
    {
      "question": "Cuộc Tổng tiến công chiến lược giải phóng hoàn toàn miền Nam vào mùa xuân năm 1975 được thực hiện liên tiếp bởi các chiến dịch:",
      "options": [
        "A. Chiến dịch Tây Nguyên, chiến dịch Bình Trị Thiên, chiến dịch Hồ Chí Minh.",
        "B. Chiến dịch Quảng Trị, chiến dịch Huế - Đà Nẵng, chiến dịch Hồ Chí Minh.",
        "C. Chiến dịch Tây Nguyên, chiến dịch Huế - Đà Nẵng, chiến dịch Hồ Chí Minh.",
        "D. Chiến dịch Tây Nguyên, chiến dịch đường 9 Nam - Lào, chiến dịch Hồ Chí Minh."
      ],
      "answer": ""
    },
    {
      "question": "Nội dung nào không đúng với bài học kinh nghiệm của cuộc kháng chiến chống Mỹ cứu nước?",
      "options": [
        "A. Giương cao ngọn cờ độc lập dân tộc và chủ nghĩa xã hội.",
        "B. Giải quyết đúng đắn nhiệm vụ chống đế quốc và chống phong kiến.",
        "C. Nghệ thuật tiến hành chiến tranh nhân dân sáng tạo.",
        "D. Coi trọng công tác xây dựng Đảng và tổ chức xây dựng lực lượng chiến đấu trong cả nước."
      ],
      "answer": ""
    },
    {
      "question": "Hội nghị TW Đảng lần thứ 11 và lần thứ 12 đã dựa trên bối cảnh lịch sử nào để đề ra đường lối kháng chiến chống Mỹ, cứu nước trên cả nước:",
      "options": [
        "A. Mỹ gây chiến tranh cục bộ ở miền Nam và đưa chiến tranh phá hoại ra miền Bắc",
        "B. Mỹ gây chiến tranh đặc biệt ở miền Nam và gây hấn ở vịnh Bắc Bộ",
        "C. Mỹ gây chiến tranh đơn phương ở miền Nam và leo thang bắn phá miền Bắc",
        "D. Mỹ thực hiện “Việt Nam hóa chiến tranh” ở miền Nam và âm mưu đánh ra miền Bắc"
      ],
      "answer": ""
    },
    {
      "question": "Sau khi Chiến tranh “đơn phương” thất bại, đế quốc Mỹ đã chuyển sang chiến lược:",
      "options": [
        "A. Chiến tranh cục bộ",
        "B. Chiến tranh Việt Nam hóa",
        "C. Chiến tranh đặc biệt",
        "D. Chiến tranh phá hoại"
      ],
      "answer": ""
    },
    {
      "question": "Sau phong trào Đồng Khởi 1960 mặt trận được thành lập ở Miền Nam là:",
      "options": [
        "A. Mặt trận dân tộc Miền Nam thống nhất",
        "B. Mặt trận dân tộc Cộng hòa Miền Nam Việt Nam",
        "C. Mặt trận dân tộc Dân chủ Miền Nam",
        "D. Mặt trận dân tộc giải phóng Miền Nam Việt Nam"
      ],
      "answer": ""
    },
    {
      "question": "Lời kêu gọi: \"Chiến tranh có thể kéo dài 5 năm, 10 năm, 20 năm hoặc lâu hơn nữa. Hà Nội, Hải Phòng và một số thành phố, xí nghiệp có thể bị tàn phá, song nhân dân Việt Nam quyết không sợ. Không có gì quý hơn độc lập, tự do\" được chủ tịch Hồ Chí Minh đưa ra vào thời điểm:",
      "options": [
        "A. Đại hội III (1960)",
        "B. Hội nghị lần thứ 11 (1965)",
        "C. Hội nghị trung ương lần thứ 15 (1959)",
        "D. Lời kêu gọi toàn quốc kháng chiến chống Mỹ, cứu nước ngày 17-7-1966"
      ],
      "answer": ""
    },
    {
      "question": "Câu nói: “Tổ quốc ta nhất định sẽ thống nhất, Đồng bào Nam, Bắc nhất định sẽ sum họp một nhà” được chủ tịch Hồ Chí Minh viết trong:",
      "options": [
        "A. Đường kách mệnh",
        "B. Tuyên ngôn độc lập",
        "C. Lời kêu gọi toàn quốc kháng chiến",
        "D. Di chúc của chủ tịch Hồ Chí Minh"
      ],
      "answer": ""
    },
    {
      "question": "Đường lối công nghiệp hóa XHCN ở miền Bắc đề ra tại Đại hội lần thứ III của Đảng (9/1960) chủ trương ưu tiên phát triển ngành nào?",
      "options": [
        "A. Nông nghiệp.",
        "B. Công nghiệp nhẹ.",
        "C. Công nghiệp nặng.",
        "D. Dịch vụ."
      ],
      "answer": ""
    },
    {
      "question": "Khó khăn và cũng là đặc điểm lớn nhất của kinh tế miền Bắc khi bước vào thời kỳ quá độ lên chủ nghĩa xã hội sau năm 1954 là:",
      "options": [
        "A. Tàn dư của chế độ cũ còn nặng nề, trên 90% dân số mù chữ.",
        "B. Từ một nền kinh tế nông nghiệp lạc hậu tiến thẳng lên CNXH không trải qua giai đoạn phát triển tư bản chủ nghĩa.",
        "C. Mô hình các nước xã hội chủ nghĩa trên thế giới vốn có những khiếm khuyết, nhược điểm rất khó để học tập rút kinh nghiệm.",
        "D. Xây dựng chủ nghĩa xã hội trong điều kiện một nửa nước có chiến tranh."
      ],
      "answer": ""
    },
    {
      "question": "Chọn câu SAI. Đặc trưng chủ yếu CNH thời kỳ trước đổi mới là:",
      "options": [
        "A. Công nghiệp hóa theo mô hình nền kinh tế khép kín, hướng nội và thiên về công nghiệp nặng.",
        "B. Công nghiệp hóa là sự nghiệp của toàn dân, của tất cả các thành phần kinh tế.",
        "C. Công nghiệp hóa chủ yếu dựa vào lợi thế của lao động, tài nguyên, đất đai và nguồn viện trợ của các nước XHCN.",
        "D. Việc phân bổ nguồn lực cho CNH được thực hiện thông qua cơ chế kế hoạch hóa tập trung quan liêu bao cấp, không tôn trọng các quy luật của thị trường."
      ],
      "answer": ""
    },
    {
      "question": "Đại hội nào của Đảng đưa ra nhận định: “Nước ta đã ra khỏi khủng hoảng kinh tế- xã hội, nhiệm vụ chuẩn bị tiền đề cho công nghiệp hóa cơ bản đã hoàn thành, cho phép nước ta chuyển sang thời kỳ mới đẩy mạnh công nghiệp hóa, hiện đại hóa đất nước”:",
      "options": [
        "A. Đại hội VII (tháng 6/1991)",
        "B. Đại hội VIII (tháng 6/1996)",
        "C. Đại hội IX (tháng 4/2001)",
        "D. Đại hội X (tháng 4/2006)"
      ],
      "answer": ""
    },
    {
      "question": "\"CNH là nhiệm vụ trung tâm của thời kỳ quá độ lên chủ nghĩa xã hội ở nước ta” được Đảng xác định lần đầu tiên tại:",
      "options": [
        "A. Hội nghị Ban chấp hành TW lần thứ 14 - khóa II (11/1958)",
        "B. Hội nghị Ban chấp hành TW lần thứ 16 - khóa II (4/1959)",
        "C. Đại hội lần thứ III của Đảng (9/1960)",
        "D. Hội nghị Ban chấp hành TW lần thứ 19 - khóa III (3/1971)"
      ],
      "answer": ""
    }
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# The last question of page 5 was index 27
data['questions'].extend(new_questions)
data['section'] = 'file2_page1_to_10'

with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully appended {len(new_questions)} questions!")
