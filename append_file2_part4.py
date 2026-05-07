import json

new_questions = [
    {
      "question": "Sự khác biệt về mục đích phát triển của kinh tế thị trường định hướng XHCN ở nước ta và kinh tế thị trường tư bản chủ nghĩa nói chung?",
      "options": [
        "A. Để nâng cao tiềm lực của các doanh nghiệp.",
        "B. Để nâng cao đời sống cho mọi người, mọi người đều được hưởng những thành quả phát triển.",
        "C. Để bảo vệ và phát triển các tập đoàn kinh tế.",
        "D. Để có lợi nhuận tối đa."
      ],
      "answer": ""
    },
    {
      "question": "Đại hội nào Đảng ta xác định 5 thành phần kinh tế gồm: Kinh tế nhà nước; Kinh tế tập thể; Kinh tế tư nhân (cá thể, tiểu chủ, tư bản tư nhân); Kinh tế tư bản nhà nước và Kinh tế có vốn đầu tư nước ngoài?",
      "options": [
        "A. Đại hội lần thứ VII (6/1991).",
        "B. Đại hội lần thứ VIII (6/1996).",
        "C. Đại hội lần thứ IX (4/2001).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Một trong những quan điểm để hoàn thiện thể chế kinh tế thị trường định hướng XHCN ở VN là?",
      "options": [
        "A. Đẩy mạnh CNH, HĐH, ứng dụng nhanh tiến bộ khoa học-công nghệ, đẩy mạnh phân công lao động quốc tế.",
        "B. Chủ động tích cực giải quyết các vấn đề lý luận và thực tiễn quan trọng, bức xúc, đồng thời phải có bước đi vững chắc, vừa làm vừa rút kinh nghiệm.",
        "C. Đẩy mạnh CNH, HĐH, ứng dụng nhanh tiến bộ khoa học - công nghệ, đẩy mạnh phân công chuyên môn hóa.",
        "D. Đẩy mạnh CNH, HĐH, ứng dụng nhanh tiến bộ khoa học - công nghệ, đẩy mạnh phân công xã hội."
      ],
      "answer": ""
    },
    {
      "question": "Một trong những chủ trương của Đảng để tiếp tục hoàn thiện thể chế kinh tế thị trường định hướng XHCN ở VN là:",
      "options": [
        "A. Hình thành và phát triển không đồng bộ các loại thị trường.",
        "B. Hình thành và phát triển đồng bộ các loại thị trường trong và ngoài nước.",
        "C. Hoàn thiện thể chế đảm bảo đồng bộ các yếu tố thị trường và phát triển đồng bộ các loại thị trường.",
        "D. Hình thành và phát triển đồng bộ các loại thị trường dịch vụ."
      ],
      "answer": ""
    },
    {
      "question": "Thuật ngữ “hệ thống chính trị” được Đảng ta sử dụng lần đầu tiên tại:",
      "options": [
        "A. Đại hội lần thứ IV (12/1976).",
        "B. Đại hội lần thứ VI (12/1986).",
        "C. Hội nghị TW 6 - khóa VI (3/1989).",
        "D. Đại hội lần thứ VII (6/1991)."
      ],
      "answer": ""
    },
    {
      "question": "Đảng ta khẳng định “Nhà nước xã hội chủ nghĩa Việt Nam là nhà nước chuyên chính vô sản” tại:",
      "options": [
        "A. Đại hội toàn quốc lần thứ IV (12/1976).",
        "B. Hiến pháp nước Việt Nam dân chủ cộng hòa (1946).",
        "C. Hiến pháp nước cộng hòa xã hội chủ nghĩa Việt Nam (1980).",
        "D. Đại hội Đảng lần thứ VI (12/1986)."
      ],
      "answer": ""
    },
    {
      "question": "Thuật ngữ “hệ thống chuyên chính vô sản” được Đảng bắt đầu sử dụng chính thức từ:",
      "options": [
        "A. Đại hội lần thứ I (3/1935).",
        "B. Đại hội lần thứ III (9/1960).",
        "C. Đại hội lần thứ IV (12/1976).",
        "D. Đại hội lần thứ VI (12/1986)."
      ],
      "answer": ""
    },
    {
      "question": "Đảng ta xác định cơ sở xã hội của hệ thống chuyên chính vô sản gồm:",
      "options": [
        "A. Liên minh giai cấp giữa giai cấp công nhân và nông dân.",
        "B. Liên minh giai cấp giữa giai cấp công nhân - nông dân và tầng lớp trí thức.",
        "C. Liên minh giai cấp giữa giai cấp nông dân và tầng lớp trí thức.",
        "D. Liên minh giai cấp giữa giai cấp công nhân - nông dân và tầng lớp tiểu tư sản."
      ],
      "answer": ""
    },
    {
      "question": "Hệ thống chính trị ở Việt Nam gồm:",
      "options": [
        "A. Đảng, Mặt trận Tổ quốc Việt Nam, Mặt trận dân chủ và Nhà nước.",
        "B. Đảng, Nhà nước, Mặt trận Tổ quốc và các đoàn thể chính trị - xã hội (Tổng liên đoàn lao động Việt Nam, Đoàn thanh niên cộng sản Hồ Chí Minh, Hội liên hiệp phụ nữ Việt Nam, Hội cựu chiến binh Việt Nam, Hội nông dân Việt Nam...).",
        "C. Đảng, Nhà nước, Mặt trận Tổ quốc Việt Nam, Mặt trận Liên Việt.",
        "D. Đảng Cộng sản Việt Nam, Nhà nước, Mặt trận Tổ quốc, Đảng dân chủ và Đảng xã hội."
      ],
      "answer": ""
    },
    {
      "question": "Điền vào chỗ trống: Trong đường lối xây dựng hệ thống chính trị Đảng ta xác định vai trò rất quan trọng của .......... là tập hợp, vận động, đoàn kết rộng rãi các tầng lớp nhân dân, đại diện cho quyền và lợi ích hợp pháp của nhân dân, thực hiện tốt vai trò giám sát và phản biện xã hội.",
      "options": [
        "A. Đảng.",
        "B. Nhà nước.",
        "C. Mặt trận Tổ quốc Việt Nam và các đoàn thể.",
        "D. Chính phủ."
      ],
      "answer": ""
    },
    {
      "question": "Theo Đại hội IX mối quan hệ giữa các giai cấp, các tầng lớp trong xã hội là “quan hệ......trong nội bộ nhân dân, đoàn kết và hợp tác lâu dài sự nghiệp xây dựng và bảo vệ tổ quốc dưới sự lãnh đạo của Đảng”.",
      "options": [
        "A. Hợp tác và đoàn kết.",
        "B. Hợp tác và đấu tranh.",
        "C. Đồng thuận.",
        "D. Tùy thuộc lẫn nhau."
      ],
      "answer": ""
    },
    {
      "question": "Chọn câu SAI. Về vị trí và vai trò của Đảng, Cương lĩnh 1991 xác định:",
      "options": [
        "A. Đảng lãnh đạo hệ thống chính trị đồng thời là một bộ phận của hệ thống chính trị",
        "B. Đảng liên hệ mật thiết với nhân dân, chịu sự giám sát của nhân dân",
        "C. Đảng đề ra Hiến pháp và Pháp luật",
        "D. Đảng hoạt động trong khuôn khổ hiến pháp và pháp luật"
      ],
      "answer": ""
    },
    {
      "question": "Nhà nước pháp quyền là:",
      "options": [
        "A. Sản phẩm của xã hội tư bản chủ nghĩa",
        "B. Sản phẩm của xã hội chủ nghĩa",
        "C. Sản phẩm của trí tuệ nhân loại trong quản lý xã hội",
        "D. Sản phẩm của xã hội phong kiến."
      ],
      "answer": ""
    },
    {
      "question": "Bản “Đề cương văn hóa Việt Nam” được Ban thường vụ TW Đảng thông qua năm 1943, do ai trực tiếp soạn thảo?",
      "options": [
        "A. Hồ Chí Minh",
        "B. Phạm Văn Đồng",
        "C. Trường Chinh",
        "D. Lê Duẩn."
      ],
      "answer": ""
    },
    {
      "question": "Đề cương văn hóa Việt Nam được Đảng xây dựng:",
      "options": [
        "A. Trước Cách mạng tháng Tám",
        "B. Trong kháng chiến chống Pháp",
        "C. Trong kháng chiến chống Mỹ",
        "D. Trong thời kì cả nước quá độ lên CNXH"
      ],
      "answer": ""
    },
    {
      "question": "Giữa thế kỉ 20 (năm 1945), Việt Nam có bao nhiêu dân số mù chữ:",
      "options": [
        "A. Hơn 70%",
        "B. Hơn 90%",
        "C. Hơn 80%",
        "D. Hơn 60%"
      ],
      "answer": ""
    },
    {
      "question": "Ngày 3/9/1945, trong phiên họp đầu tiên của Chính phủ, Chủ tịch Hồ Chí Minh đã trình bày 6 nhiệm vụ cấp bách. Trong đó, có 3 nhiệm vụ về văn hóa là:",
      "options": [
        "A. Xóa bỏ tàn dư văn hóa nô dịch, đẩy mạnh hoạt động của báo chí.",
        "B. Bài trừ tệ nạn xã hội, xây dựng thuần phong mỹ tục.",
        "C. Chống nạn mù chữ và giáo dục lại tinh thần của nhân dân.",
        "D. Diệt giặc dốt và đẩy mạnh xây dựng nền giáo dục mới."
      ],
      "answer": ""
    },
    {
      "question": "Tìm câu SAI. Đường lối văn hóa kháng chiến có một trong những nội dung cơ bản là:",
      "options": [
        "A. Tập trung cho kháng chiến thành công trước, sau đó tập trung cho văn hóa",
        "B. Xây dựng mối quan hệ giữa văn hóa và CMGPDT, cử động văn hóa cứu quốc",
        "C. Xây dựng nền văn hóa dân chủ mới VN có tính chất dân tộc, khoa học và đại chúng",
        "D. Tích cực bài trừ nạn mù chữ, mở Đại học và Trung học, cải cách việc học theo tinh thần mới."
      ],
      "answer": ""
    },
    {
      "question": "Câu nói: “Ngày nay chúng ta đã xây nền nước Việt Nam dân chủ cộng hòa nhưng khi nước nhà độc lập mà dân không được hưởng tự do, hạnh phúc thì nền độc lập đó không có nghĩa lý gì...” là câu nói của ai?",
      "options": [
        "A. Trường Chinh.",
        "B. Phạm Văn Đồng.",
        "C. Hồ Chí Minh.",
        "D. Võ Nguyên Giáp."
      ],
      "answer": ""
    },
    {
      "question": "Câu nói: “Một dân tộc dốt là một dân tộc yếu...” được Chủ tịch Hồ Chí Minh nói vào thời gian nào?",
      "options": [
        "A. Ngày 3/9/1945.",
        "B. Ngày 27/7/1947.",
        "C. Ngày 17/7/1965.",
        "D. Ngày 15/5/1965."
      ],
      "answer": ""
    },
    {
      "question": "Câu nói: \"Non sông Việt Nam có trở nên tươi đẹp hay không, dân tộc Việt Nam có bước tới đài vinh quang để sánh vai với các cường quốc năm châu được hay không, chính là nhờ một phần lớn ở công học tập của các em\" được Hồ Chí Minh nói vào thời gian nào?",
      "options": [
        "A. Tháng 9/1945.",
        "B. Tháng 11/1945.",
        "C. Tháng 12/1946.",
        "D. Tháng 7/1947."
      ],
      "answer": ""
    },
    {
      "question": "Đại hội lần thứ mấy Đảng ta đã đưa ra quan điểm phải xây dựng về nền văn hóa VN thành một nền “văn hóa tiên tiến và đậm đà bản sắc dân tộc!”?",
      "options": [
        "A. Đại hội lần thứ VI.",
        "B. Đại hội lần thứ VII.",
        "C. Đại hội lần thứ VIII.",
        "D. Đại hội lần thứ X."
      ],
      "answer": ""
    },
    {
      "question": "Chọn phương án để điền vào chỗ trống. Cương lĩnh năm 1991 đã đề ra 1 trong 7 phương hướng là \"Tiến hành cách mạng XHCN trong lĩnh vực tư tưởng và văn hóa làm cho ....... giữ vị trí chủ đạo trong đời sống tinh thần xã hội”",
      "options": [
        "A. Những giá trị của Chủ nghĩa cộng sản",
        "B. Thế giới quan Mác Lênin và tư tưởng Hồ Chí Minh",
        "C. Bản sắc dân tộc và yếu tố tiên tiến",
        "D. Tư duy thực tế"
      ],
      "answer": ""
    },
    {
      "question": "Đại hội VII (1991) và Đại hội VIII (1996) khẳng định lĩnh vực nào đóng vai trò then chốt trong sự nghiệp xây dựng chủ nghĩa xã hội và bảo vệ Tổ quốc",
      "options": [
        "A. Khoa học công nghệ và an ninh quốc phòng",
        "B. Giáo dục - đào tạo và an ninh quốc phòng",
        "C. Ổn định chính trị và an ninh",
        "D. Giáo dục - đào tạo, khoa học — công nghệ."
      ],
      "answer": ""
    },
    {
      "question": "Chọn câu SAI. Quan điểm của hội nghị TW 5 khóa VIII là:",
      "options": [
        "A. Xây dựng và phát triển nền văn hóa phải nhằm mục tiêu kinh tế, vì hiệu quả kinh tế.",
        "B. Nền văn hóa Việt Nam là nền văn hóa tiên tiến, đậm đà bản sắc dân tộc.",
        "C. Xây dựng và phát triển nền văn hóa là sự nghiệp của toàn dân do Đảng lãnh đạo, trong đó đội ngũ trí thức giữ vai trò quan trọng.",
        "D. Văn hóa là nền tảng tinh thần của xã hội, vừa là mục tiêu, vừa là động lực thúc đẩy phát triển kinh tế - xã hội."
      ],
      "answer": ""
    }
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['questions'].extend(new_questions)
data['section'] = 'file2_page1_to_20'

with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully appended {len(new_questions)} questions from pages 16-20!")
