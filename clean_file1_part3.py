import json

clean_questions = [
    # 77
    {
        "question": "Khó khăn lớn nhất của nước ta sau Cách mạng tháng 8 (1945) là:",
        "options": [
            "A. Nền kinh tế rơi vào tình trạng kiệt quệ.",
            "B. Các thế lực ngoại xâm bao vây chống phá hòng tiêu diệt chính quyền cách mạng non trẻ.",
            "C. Chính phủ nước Việt Nam dân chủ cộng hòa chưa được các nước trên thế giới công nhận về pháp lý.",
            "D. Tàn dư của chế độ cũ còn nặng nề, trên 90% dân số mù chữ."
        ],
        "answer": "B. Các thế lực ngoại xâm bao vây chống phá hòng tiêu diệt chính quyền cách mạng non trẻ."
    },
    # 78
    {
        "question": "Trong ba loại giặc (giặc đói, giặc dốt và giặc ngoại xâm), loại giặc nguy hiểm nhất hiện diện trên lãnh thổ nước ta ngay sau Cách mạng tháng Tám (1945) là:",
        "options": [
            "A. Giặc đói.",
            "B. Giặc dốt.",
            "C. Giặc ngoại xâm.",
            "D. Tất cả đều đúng."
        ],
        "answer": "C. Giặc ngoại xâm."
    },
    # 79
    {
        "question": "Phương châm kháng chiến trong đường lối kháng chiến chống thực dân Pháp (1946) của Đảng là:",
        "options": [
            "A. Kháng chiến toàn dân; Toàn diện; Trường kỳ; Dựa vào sức mình là chính.",
            "B. Kháng chiến trường kỳ; Toàn diện; Quyết liệt; Dựa vào sức mình đồng thời nhận tất cả sự giúp đỡ của quốc tế.",
            "C. Kháng chiến toàn quốc; Toàn diện; Bền bỉ; Toàn nhân dân và giúp đỡ quốc tế.",
            "D. Kháng chiến toàn dân; Toàn diện; Sáng tạo; Bám vào thắt lưng địch mà đánh."
        ],
        "answer": "A. Kháng chiến toàn dân; Toàn diện; Trường kỳ; Dựa vào sức mình là chính."
    },
    # 80
    {
        "question": "Chỉ ra nội dung sai khi nói về ý nghĩa lịch sử của cuộc kháng chiến chống thực dân Pháp và can thiệp Mỹ (1945 - 1954):",
        "options": [
            "A. Chấm dứt ách thống trị của chủ nghĩa thực dân cũ gần một thế kỷ.",
            "B. Bảo vệ được thành quả Cách mạng Tháng 8, giải phóng hoàn toàn miền Bắc.",
            "C. Góp phần cổ vũ mạnh mẽ các dân tộc thuộc địa vùng lên giành độc lập.",
            "D. Hoàn thành cách mạng dân tộc dân chủ nhân dân trên phạm vi cả nước."
        ],
        "answer": "D. Hoàn thành cách mạng dân tộc dân chủ nhân dân trên phạm vi cả nước."
    },
    # 81
    {
        "question": "Ngày 11-11-1945, Đảng Cộng sản Đông Dương ra Thông cáo tự ý giải tán nhưng thực tế vẫn hoạt động với danh nghĩa là:",
        "options": [
            "A. \"Hội nghiên cứu chủ nghĩa Mác ở Đông Dương\"",
            "B. \"Hội nghiên cứu chủ nghĩa Mác - Lênin ở Đông Nam Á\"",
            "C. \"Hội nghiên cứu chủ nghĩa Mác ở Việt Nam\"",
            "D. \"Hội nghiên cứu chủ nghĩa Mác, Tư tưởng Hồ Chí Minh ở Đông Dương\""
        ],
        "answer": "A. \"Hội nghiên cứu chủ nghĩa Mác ở Đông Dương\""
    },
    # 82
    {
        "question": "Chỉ ra nội dung sai trong Hiệp định Giơnevơ về chấm dứt chiến tranh, lập lại hoà bình ở Đông Dương:",
        "options": [
            "A. Các nước tham dự Hội nghị cam kết tôn trọng các quyền dân tộc cơ bản là độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ của nhân dân Việt Nam, Lào và Campuchia.",
            "B. Pháp rút quân ra khỏi 3 nước Đông Dương, vĩ tuyến 17 là giới tuyến quân sự tạm thời ở Việt Nam. Việt Nam sẽ tổng tuyển cử thống nhất đất nước vào tháng 7-1956.",
            "C. Pháp tuyên bố công nhận Việt Nam là một nước tự do nằm trong Liên hiệp Pháp.",
            "D. Tất cả đều sai."
        ],
        "answer": "C. Pháp tuyên bố công nhận Việt Nam là một nước tự do nằm trong Liên hiệp Pháp."
    },
    # 83
    {
        "question": "Tháng 2 năm 1951, Đại hội đại biểu lần thứ II của Đảng Cộng sản Đông Dương, tại tỉnh Tuyên Quang, đã ra Nghị quyết quan trọng tuyên bố:",
        "options": [
            "A. Xây dựng chiến khu cách mạng.",
            "B. Xây dựng lực lượng, chuẩn bị khởi nghĩa vũ trang.",
            "C. Chia tách Đảng Cộng sản Đông Dương thành 3 Đảng để lãnh đạo cách mạng 3 nước Đông Dương.",
            "D. Đề ra đường lối Chiến tranh du kích, trường kỳ kháng chiến."
        ],
        "answer": "C. Chia tách Đảng Cộng sản Đông Dương thành 3 Đảng để lãnh đạo cách mạng 3 nước Đông Dương."
    },
    # 84
    {
        "question": "Hội nghị Trung ương lần thứ 15 (tháng 1/1959), Đảng đề ra hai nhiệm vụ chiến lược gồm:",
        "options": [
            "A. Cách mạng xã hội chủ nghĩa ở miền Bắc và cách mạng dân tộc dân chủ nhân dân ở miền Nam.",
            "B. Cách mạng bảo vệ Tổ quốc ở miền Bắc và cách mạng giải phóng dân tộc ở miền Nam.",
            "C. Cách mạng dân chủ nhân dân ở miền Bắc và cách mạng giành chính quyền ở miền Nam.",
            "D. Cách mạng dân chủ xã hội ở miền Bắc và cách mạng dân chủ nhân dân ở miền Nam."
        ],
        "answer": "A. Cách mạng xã hội chủ nghĩa ở miền Bắc và cách mạng dân tộc dân chủ nhân dân ở miền Nam."
    },
    # 85
    {
        "question": "Nghị quyết nào của Đảng mở đường cho cao trào \"Đồng khởi\" ở miền Nam:",
        "options": [
            "A. Nghị quyết Ban chấp hành TW lần thứ 15 (1/1959).",
            "B. Nghị quyết Ban chấp hành TW lần thứ 11 (3/1965).",
            "C. Nghị quyết Ban chấp hành TW lần thứ 12 (12/1963).",
            "D. Nghị quyết Ban chấp hành TW lần thứ 14 (1/1968)."
        ],
        "answer": "A. Nghị quyết Ban chấp hành TW lần thứ 15 (1/1959)."
    },
    # 86
    {
        "question": "Sau khi chiến lược \"Chiến tranh đơn phương\" thất bại, đế quốc Mỹ đã chuyển sang chiến lược:",
        "options": [
            "A. Chiến lược Chiến tranh cục bộ.",
            "B. Chiến lược Chiến tranh Việt Nam hóa.",
            "C. Chiến lược Chiến tranh đặc biệt.",
            "D. Chiến lược Chiến tranh leo thang phá hoại miền Bắc."
        ],
        "answer": "C. Chiến lược Chiến tranh đặc biệt."
    },
    # 87
    {
        "question": "Chiến thắng của trận đánh nào đã củng cố cho Đảng đề ra quyết tâm giải phóng Miền Nam trong năm 1975:",
        "options": [
            "A. Chiến thắng Buôn Mê Thuột.",
            "B. Chiến thắng Đông Nam bộ.",
            "C. Chiến thắng Phước Long.",
            "D. Chiến thắng Tây Nguyên."
        ],
        "answer": "C. Chiến thắng Phước Long."
    },
    # 88
    {
        "question": "Thắng lợi nào: \"Mãi mãi được ghi vào lịch sử dân tộc như một trang chói lọi nhất, một biểu tượng sáng ngời về sự toàn thắng... đi vào lịch sử thế giới như một chiến công vĩ đại của thế kỷ XX, một sự kiện có tầm quan trọng quốc tế to lớn và tính thời đại sâu sắc\":",
        "options": [
            "A. Thắng lợi của Cách mạng Tháng 8.",
            "B. Thắng lợi của cuộc kháng chiến chống thực dân Pháp xâm lược.",
            "C. Thắng lợi của cuộc kháng chiến chống Mỹ, cứu nước.",
            "D. Thắng lợi của cuộc chiến tranh bảo vệ biên giới phía Bắc."
        ],
        "answer": "C. Thắng lợi của cuộc kháng chiến chống Mỹ, cứu nước."
    },
    # 89
    {
        "question": "Cuộc Tổng tiến công chiến lược giải phóng hoàn toàn miền Nam vào mùa xuân năm 1975 được thực hiện liên tiếp bởi các chiến dịch nào:",
        "options": [
            "A. Chiến dịch Tây Nguyên, Chiến dịch Bình Trị Thiên, Chiến dịch Hồ Chí Minh.",
            "B. Chiến dịch Quảng Trị, Chiến dịch Huế - Đà Nẵng, Chiến dịch Hồ Chí Minh.",
            "C. Chiến dịch Tây Nguyên, Chiến dịch Huế - Đà Nẵng, Chiến dịch Hồ Chí Minh.",
            "D. Chiến dịch Tây Nguyên, Chiến dịch đường 9 Nam - Lào, Chiến dịch Hồ Chí Minh."
        ],
        "answer": "C. Chiến dịch Tây Nguyên, Chiến dịch Huế - Đà Nẵng, Chiến dịch Hồ Chí Minh."
    },
    # 90
    {
        "question": "Nội dung nào dưới đây không đúng với bài học kinh nghiệm của cuộc kháng chiến chống Mỹ, cứu nước:",
        "options": [
            "A. Giương cao ngọn cờ độc lập dân tộc và chủ nghĩa xã hội.",
            "B. Giải quyết đúng đắn nhiệm vụ chống đế quốc và chống phong kiến tay sai.",
            "C. Nghệ thuật tiến hành chiến tranh nhân dân sáng tạo.",
            "D. Coi trọng công tác xây dựng Đảng và tổ chức xây dựng lực lượng chiến đấu trong cả nước."
        ],
        "answer": "B. Giải quyết đúng đắn nhiệm vụ chống đế quốc và chống phong kiến tay sai."
    },
    # 91
    {
        "question": "Cuộc bầu cử Quốc hội chung cả nước sau khi Tổ quốc thống nhất được tiến hành vào thời gian:",
        "options": [
            "A. 4/1975.",
            "B. 4/1976.",
            "C. 5/1975.",
            "D. 6/1976."
        ],
        "answer": "B. 4/1976."
    },
    # 92
    {
        "question": "Quốc hiệu Cộng hoà xã hội chủ nghĩa Việt Nam chính thức được đặt vào thời gian nào, tại đâu:",
        "options": [
            "A. Tại Hội nghị hiệp thương (9/1975).",
            "B. Tại Kỳ họp thứ nhất của Quốc hội khoá VI (tháng 7/1976).",
            "C. Tại Đại hội IV của Đảng (12/1976).",
            "D. Tại Đại hội V của Đảng (12/1982)."
        ],
        "answer": "B. Tại Kỳ họp thứ nhất của Quốc hội khoá VI (tháng 7/1976)."
    },
    # 93
    {
        "question": "Đại hội nào là \"Đại hội toàn thắng của sự nghiệp giải phóng dân tộc, thống nhất Tổ quốc, khẳng định và xác định đường lối đưa cả nước tiến lên chủ nghĩa xã hội\":",
        "options": [
            "A. Đại hội lần thứ IV.",
            "B. Đại hội lần thứ V.",
            "C. Đại hội lần thứ VI.",
            "D. Đại hội lần thứ VII."
        ],
        "answer": "A. Đại hội lần thứ IV."
    },
    # 94
    {
        "question": "Quân đội nhân dân Việt Nam đã giúp đỡ nhân dân Campuchia giải phóng khỏi chế độ diệt chủng của Polpot vào thời gian:",
        "options": [
            "A. 1977.",
            "B. 1978.",
            "C. 1979.",
            "D. 1980."
        ],
        "answer": "C. 1979."
    },
    # 95
    {
        "question": "Trung Quốc đã đem quân đội xâm lược biên giới 6 tỉnh nước ta từ Lai Châu đến Quảng Ninh vào thời điểm:",
        "options": [
            "A. 17-2-1978.",
            "B. 17-2-1979.",
            "C. 17-2-1980.",
            "D. 17-2-1981."
        ],
        "answer": "B. 17-2-1979."
    },
    # 96
    {
        "question": "Đường lối công nghiệp hóa XHCN ở miền Bắc đề ra tại Đại hội lần thứ III của Đảng (9/1960) đã chủ trương ưu tiên phát triển ngành nào:",
        "options": [
            "A. Nông nghiệp.",
            "B. Công nghiệp nhẹ.",
            "C. Công nghiệp nặng.",
            "D. Dịch vụ."
        ],
        "answer": "C. Công nghiệp nặng."
    },
    # 97
    {
        "question": "Khó khăn và cũng là đặc điểm lớn nhất của kinh tế miền Bắc khi bước vào thời kỳ quá độ lên chủ nghĩa xã hội sau năm 1954 là:",
        "options": [
            "A. Tàn dư của chế độ cũ còn nặng nề, trên 90% dân số mù chữ.",
            "B. Từ một nền kinh tế nông nghiệp lạc hậu tiến thẳng lên CNXH không trải qua giai đoạn phát triển tư bản chủ nghĩa.",
            "C. Mô hình các nước xã hội chủ nghĩa trên thế giới vốn có những khiếm khuyết, nhược điểm rất khó để học tập rút kinh nghiệm.",
            "D. Xây dựng chủ nghĩa xã hội trong điều kiện một nửa nước có chiến tranh."
        ],
        "answer": "B. Từ một nền kinh tế nông nghiệp lạc hậu tiến thẳng lên CNXH không trải qua giai đoạn phát triển tư bản chủ nghĩa."
    },
    # 98
    {
        "question": "(NC) Chọn câu nội dung sai khi nói về đặc trưng chủ yếu của CNH ở nước ta thời kỳ trước đổi mới:",
        "options": [
            "A. Công nghiệp hóa theo mô hình nền kinh tế khép kín, hướng nội và thiên về công nghiệp nặng.",
            "B. Công nghiệp hóa là sự nghiệp của toàn dân, của tất cả các thành phần kinh tế.",
            "C. Công nghiệp hóa chủ yếu dựa vào lợi thế của lao động, tài nguyên, đất đai và nguồn viện trợ của các nước XHCN.",
            "D. Việc phân bố nguồn lực cho CNH được thực hiện thông qua cơ chế kế hoạch hóa tập trung quan liêu bao cấp, không tôn trọng các quy luật của thị trường."
        ],
        "answer": "B. Công nghiệp hóa là sự nghiệp của toàn dân, của tất cả các thành phần kinh tế."
    },
    # 99
    {
        "question": "(NC) Đại hội nào của Đảng đã nhận định rằng, \"Nước ta đã ra khỏi khủng hoảng kinh tế-xã hội, nhiệm vụ chuẩn bị tiền đề cho công nghiệp hóa cơ bản đã hoàn thành, cho phép nước ta chuyển sang thời kỳ mới đẩy mạnh công nghiệp hóa, hiện đại hóa đất nước\":",
        "options": [
            "A. Đại hội VII (tháng 6/1991).",
            "B. Đại hội VIII (tháng 6/1996).",
            "C. Đại hội IX (tháng 4/2001).",
            "D. Đại hội X (tháng 4/2006)."
        ],
        "answer": "B. Đại hội VIII (tháng 6/1996)."
    },
    # 100
    {
        "question": "(NC) Theo tư duy mới của Đảng từ Đại hội VI (1986), kinh tế thị trường chỉ đối lập với:",
        "options": [
            "A. Kinh tế tự nhiên tự cấp, tự túc.",
            "B. Kinh tế tư bản chủ nghĩa.",
            "C. Kinh tế trong thời kỳ quá độ lên chủ nghĩa xã hội.",
            "D. Kinh tế xã hội chủ nghĩa."
        ],
        "answer": "A. Kinh tế tự nhiên tự cấp, tự túc."
    },
    # 101
    {
        "question": "(NC) Quan điểm \"mở rộng, đa dạng hoá, đa phương hoá các quan hệ đối ngoại\" được Đảng đề ra tại:",
        "options": [
            "A. Đại hội VI (tháng 12/1986).",
            "B. Đại hội VII (tháng 6/1991).",
            "C. Đại hội VIII (tháng 6/1996).",
            "D. Đại hội IX (tháng 4/2001)."
        ],
        "answer": "B. Đại hội VII (tháng 6/1991)."
    },
    # 102
    {
        "question": "(NC) Quan điểm: \"Kinh tế thị trường định hướng XHCN là một kiểu tổ chức kinh tế, vừa tuân theo quy luật của kinh tế thị trường, vừa dựa trên cơ sở và chịu sự dẫn dắt, chi phối bởi các nguyên tắc và bản chất của CNXH\" được xác định tại:",
        "options": [
            "A. Đại hội VII (tháng 6/1991).",
            "B. Đại hội VIII (tháng 6/1996).",
            "C. Đại hội IX (tháng 4/2001).",
            "D. Đại hội X (tháng 4/2006)."
        ],
        "answer": "C. Đại hội IX (tháng 4/2001)."
    },
    # 103
    {
        "question": "(NC) Mục tiêu cụ thể về đẩy mạnh CNH, HĐH gắn liền với phát triển kinh tế tri thức để sớm đưa nước ta ra khỏi tình trạng kém phát triển được Đảng ta chính thức nêu tại:",
        "options": [
            "A. Đại hội lần thứ IV (12/1976).",
            "B. Đại hội lần thứ VI (12/1986).",
            "C. Đại hội lần thứ XII (01/2016).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "D. Đại hội lần thứ X (4/2006)."
    },
    # 104
    {
        "question": "Ai đã đưa ra nhận định sau: \"Chế độ cai trị, bóc lột hà khắc của thực dân Pháp đối với nhân dân Việt Nam là chế độ độc tài chuyên chế nhất, nó vô cùng khả ố và khủng khiếp hơn cả chế độ chuyên chế của nhà nước quân chủ châu Á đời xưa\":",
        "options": [
            "A. Nguyễn Ái Quốc.",
            "B. Phan Bội Châu.",
            "C. Phan Chu Trinh.",
            "D. Phan Văn Trường."
        ],
        "answer": "D. Phan Văn Trường."
    },
    # 105
    {
        "question": "Mục đích của Việt Nam Quốc dân đảng là:",
        "options": [
            "A. Đánh đuổi thực dân Pháp xâm lược, giành độc lập dân tộc với phương pháp đấu tranh vũ trang nhưng theo lối manh động, ám sát cá nhân và lực lượng chủ yếu là binh lính, sinh viên...",
            "B. Xây dựng chế độ cộng hòa tư sản với phương pháp đấu tranh vũ trang nhưng theo lối manh động, ám sát cá nhân và lực lượng chủ yếu là binh lính, sinh viên...",
            "C. Đấu tranh với khẩu hiệu \"không thành công thì thành nhân\".",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 106
    {
        "question": "Cuối thế kỷ XIX, đầu thế kỷ XX, \"các phong trào cứu nước từ lập trường Cần Vương đến lập trường tư sản, tiểu tư sản qua khảo nghiệm lịch sử đều lần lượt thất bại\". Nhận định này là của:",
        "options": [
            "A. Nguyễn Ái Quốc.",
            "B. Trần Phú.",
            "C. Đảng Cộng sản Việt Nam.",
            "D. Quốc tế Cộng sản."
        ],
        "answer": "D. Quốc tế Cộng sản."
    },
    # 107
    {
        "question": "Văn kiện nào đã khẳng định rằng Đảng Cộng sản Việt Nam tổ chức ra để lãnh đạo quần chúng lao khổ làm giai cấp tranh đấu để tiêu trừ tư bản đế quốc chủ nghĩa, làm cho thực hiện xã hội cộng sản:",
        "options": [
            "A. Cương lĩnh chính trị đầu tiên của Đảng (2/1930).",
            "B. Đường kách mệnh (1927).",
            "C. Luận cương chính trị (10/1930).",
            "D. Hiến pháp năm 1946."
        ],
        "answer": "A. Cương lĩnh chính trị đầu tiên của Đảng (2/1930)."
    },
    # 108
    {
        "question": "Nội dung nào đúng khi nói về vai trò lãnh đạo của Đảng đã được nêu lên trong Cương lĩnh chính trị đầu tiên (2/1930):",
        "options": [
            "A. Đảng là đội tiền phong của vô sản giai cấp phải thu phục cho được đại bộ phận giai cấp mình.",
            "B. Đảng là đội tiên phong của vô sản giai cấp, phải làm cho giai cấp mình lãnh đạo được dân chúng.",
            "C. Đảng là đội tiên phong của đạo quân vô sản gồm một số lớn của giai cấp công nhân và làm cho họ có đủ năng lực lãnh đạo quần chúng.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 109
    {
        "question": "Theo Hồ Chí Minh, \"Việc thành lập Đảng là một bước ngoặt vô cùng quan trọng trong lịch sử cách mạng Việt Nam ta. Nó chứng tỏ rằng\":",
        "options": [
            "A. Giai cấp vô sản ta đã trưởng thành và đủ sức lãnh đạo cách mạng.",
            "B. Giai cấp công nhân và nông dân ta đã trưởng thành và đủ sức lãnh đạo cách mạng.",
            "C. Giai cấp vô sản và tầng lớp trí thức ta đã trưởng thành và đủ sức lãnh đạo cách mạng.",
            "D. Tầng lớp trí thức ta đã trưởng thành và đủ sức lãnh đạo cách mạng."
        ],
        "answer": "A. Giai cấp vô sản ta đã trưởng thành và đủ sức lãnh đạo cách mạng."
    },
    # 110
    {
        "question": "Tháng 9-1930, Ban Thường vụ Trung ương Đảng gửi thông tri nêu rõ trách nhiệm của Xứ ủy Trung kỳ thời điểm này là:",
        "options": [
            "A. Tổ chức quần chúng chống khủng bố.",
            "B. Duy trì kiên cố ảnh hưởng của Đảng, của Xô viết trong quần chúng, để đến khi thất bại thì ý nghĩa Xô viết ăn sâu vào trong óc quần chúng và lực lượng của Đảng và Nông hội vẫn duy trì.",
            "C. Giữ vững lực lượng cách mạng.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 111
    {
        "question": "Chọn đáp án đúng khi nói về tổn thất của Đảng trong cao trào đấu tranh 1930 - 1931:",
        "options": [
            "A. Hàng nghìn chiến sĩ cộng sản, hàng vạn người yêu nước bị bắt, bị giết hoặc bị tù đày.",
            "B. Toàn bộ Ban Chấp hành Trung ương Đảng bị bắt, không còn lại một ủy viên nào.",
            "C. Các tổ chức của Đảng và của quần chúng tan rã hầu hết.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 112
    {
        "question": "Phong trào cách mạng năm 1930-1931 là bước thắng lợi đầu tiên có ý nghĩa quyết định đến tiến trình phát triển về sau của cách mạng Việt Nam. Nó đã:",
        "options": [
            "A. Khẳng định trong thực tế quyền lãnh đạo và năng lực lãnh đạo cách mạng của giai cấp công nhân Việt Nam.",
            "B. Đem lại cho nông dân niềm tin vững chắc vào giai cấp vô sản.",
            "C. Đem lại cho đông đảo quần chúng công nông lòng tự tin ở sức lực cách mạng.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 113
    {
        "question": "Văn kiện nào đã khẳng định rằng, \"có đánh đổ đế quốc chủ nghĩa mới phá được cái giai cấp địa chủ và làm cách mạng thổ địa được thắng lợi; mà có phá tan chế độ phong kiến thì mới đánh đổ được đế quốc chủ nghĩa\":",
        "options": [
            "A. Bản án chế độ thực dân Pháp (1925).",
            "B. Cương lĩnh chính trị đầu tiên của Đảng (2/1930).",
            "C. Luận cương chính trị (10/1930).",
            "D. Văn kiện Hội nghị TW 8 (5/1941)."
        ],
        "answer": "C. Luận cương chính trị (10/1930)."
    },
    # 114
    {
        "question": "Nội dung nào không đúng với nhiệm vụ cách mạng đã được Hội nghị Ban Chấp hành Trung ương lần thứ 2 của Đảng (26-7-1936) nêu ra:",
        "options": [
            "A. Trước mắt là chống phát xít, chống chiến tranh đế quốc, chống phản động thuộc địa và tay sai, đòi tự do, dân chủ, cơm áo và hòa bình.",
            "B. Lập Mặt trận nhân dân phản đế rộng rãi chính để bao gồm các giai cấp, các đảng phái, các đoàn thể chính trị và tín ngưỡng tôn giáo khác nhau, các dân tộc ở xứ Đông Dương để cùng nhau tranh đấu để đòi những điều dân chủ đơn sơ.",
            "C. Chuyển hình thức tổ chức bí mật, không hợp pháp sang các hình thức tổ chức và đấu tranh công khai, nửa công khai, hợp pháp, nửa hợp pháp, kết hợp với bí mật, bất hợp pháp.",
            "D. Tất cả đều sai."
        ],
        "answer": "C. Chuyển hình thức tổ chức bí mật, không hợp pháp sang các hình thức tổ chức và đấu tranh công khai, nửa công khai, hợp pháp, nửa hợp pháp, kết hợp với bí mật, bất hợp pháp."
    },
    # 115
    {
        "question": "\"Cuộc dân tộc giải phóng không nhất thiết phải kết chặt với cuộc cách mạng điền địa. Nghĩa là không thể nói rằng: muốn đánh đổ đế quốc cần phải phát triển cách mạng điền địa, muốn giải quyết vấn đề điền địa thì cần phải đánh đổ đế quốc\". Đây là nhận định của Đảng được nêu ra ở văn kiện:",
        "options": [
            "A. Cương lĩnh chính trị đầu tiên (2/1930).",
            "B. Luận cương chính trị (10/1930).",
            "C. Chung quanh vấn đề chiến sách mới (10/1936).",
            "D. Báo cáo trình Hội nghị TW 8 (5/1941)."
        ],
        "answer": "C. Chung quanh vấn đề chiến sách mới (10/1936)."
    },
    # 116
    {
        "question": "\"Bước đường sinh tồn của các dân tộc Đông Dương không có con đường nào khác hơn là con đường đánh đổ đế quốc Pháp, chống tất cả ách ngoại xâm vô luận da trắng hay da vàng để giành lấy giải phóng độc lập\". Đây là nhận định của Đảng tại:",
        "options": [
            "A. Hội nghị Ban Chấp hành Trung ương Đảng (11/1939).",
            "B. Hội nghị Ban Chấp hành Trung ương Đảng (11/1940).",
            "C. Hội nghị Ban Chấp hành Trung ương Đảng (5/1941).",
            "D. Hội nghị Ban Thường vụ Trung ương Đảng (3/1945)."
        ],
        "answer": "A. Hội nghị Ban Chấp hành Trung ương Đảng (11/1939)."
    },
    # 117
    {
        "question": "Hội nghị Ban Chấp hành Trung ương Đảng nào sau đây đã \"Đứng trên lập trường giải phóng dân tộc, lấy quyền lợi dân tộc làm tối cao, tất cả mọi vấn đề của cuộc cách mệnh, cả vấn đề điền địa cũng phải nhằm vào cái mục đích ấy mà giải quyết\":",
        "options": [
            "A. Hội nghị Ban Chấp hành Trung ương Đảng (11/1939).",
            "B. Hội nghị Ban Chấp hành Trung ương Đảng (11/1940).",
            "C. Hội nghị Ban Chấp hành Trung ương Đảng (5/1941).",
            "D. Hội nghị Ban Thường vụ Trung ương Đảng (3/1945)."
        ],
        "answer": "A. Hội nghị Ban Chấp hành Trung ương Đảng (11/1939)."
    },
    # 118
    {
        "question": "\"Trong lúc quyền lợi dân tộc giải phóng cao hơn hết thảy, chúng ta phải đoàn kết lại đánh đổ bọn đế quốc và bọn Việt gian đặng cứu giống nòi ra khỏi nước sôi lửa nóng\". Đây là:",
        "options": [
            "A. Thư kêu gọi đồng bào cả nước của lãnh tụ Nguyễn Ái Quốc ngay sau Hội nghị lần thứ tám Ban Chấp hành Trung ương Đảng (6/6/1941).",
            "B. Thư kêu gọi đồng bào cả nước của Tổng bí thư Trường Chinh ngay sau Hội nghị lần thứ tám Ban Chấp hành Trung ương Đảng (6/6/1941).",
            "C. Thư kêu gọi đồng bào cả nước của Thường vụ TW Đảng ngay sau Hội nghị lần thứ tám Ban Chấp hành Trung ương Đảng (6/6/1941).",
            "D. Thư kêu gọi đồng bào cả nước của Ban chấp hành TW Đảng ngay sau Hội nghị lần thứ tám Ban Chấp hành Trung ương Đảng (6/6/1941)."
        ],
        "answer": "A. Thư kêu gọi đồng bào cả nước của lãnh tụ Nguyễn Ái Quốc ngay sau Hội nghị lần thứ tám Ban Chấp hành Trung ương Đảng (6/6/1941)."
    },
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_idx = 77
for i in range(len(clean_questions)):
    data['questions'][start_idx + i] = clean_questions[i]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully cleaned questions {start_idx} to {start_idx + len(clean_questions) - 1}!")
print(f"Total questions cleaned: {len(clean_questions)}")
