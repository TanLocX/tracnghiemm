import json

new_questions = [
    {
      "question": "Chọn câu SAI. Trong giai đoạn 1945-1954, chính sách xã hội của Đảng ta là:",
      "options": [
        "A. Làm cho dân có ăn, làm cho dân có mặc, làm cho dân có chỗ ở, làm cho dân được học hành.",
        "B. Làm cho người nghèo thì đủ ăn, người đủ ăn thì khá giả, người khá giả thì giàu thêm.",
        "C. Thực hiện đưa nông dân vào con đường làm ăn tập thể, phân phối bình quân.",
        "D. Thực hiện chính sách điều hòa lợi ích giữa chủ và thợ."
      ],
      "answer": ""
    },
    {
      "question": "Nghị quyết Đại hội nào của Đảng chỉ rõ: “Thực hiện chế độ phân phối chủ yếu theo kết quả lao động, hiệu quả kinh tế, đồng thời theo mức đóng góp vốn cùng các nguồn lực khác và thông qua phúc lợi xã hội”?",
      "options": [
        "A. Đại hội lần thứ VII (6/1991).",
        "B. Đại hội lần thứ VIII (6/1996).",
        "C. Đại hội lần thứ IX (4/2001).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Điền vào chỗ trống, Xây dựng và phát triển văn hóa là sự nghiệp của toàn dân do Đảng lãnh đạo, trong đó ..... giữ vai trò quan trọng.",
      "options": [
        "A. Giai cấp công nông.",
        "B. Giai cấp nông dân.",
        "C. Tầng lớp doanh nhân.",
        "D. Đội ngũ trí thức."
      ],
      "answer": ""
    },
    {
      "question": "Cốt lõi nền văn hóa của dân tộc là:",
      "options": [
        "A. Hệ tư tưởng của giai cấp vô sản.",
        "B. Hệ giá trị của dân tộc.",
        "C. Hệ tư tưởng của giai cấp phong kiến.",
        "D. Hệ tư tưởng của giai cấp tư sản."
      ],
      "answer": ""
    },
    {
      "question": "Tại đại hội nào Đảng ta nâng các vấn đề xã hội lên tầm chính sách xã hội, đặt rõ tầm quan trọng của chính sách xã hội đối với chính sách kinh tế và chính sách ở các lĩnh vực khác.",
      "options": [
        "A. Đại hội VI",
        "B. Đại hội VII",
        "C. Đại hội VIII",
        "D. Đại hội IX"
      ],
      "answer": ""
    },
    {
      "question": "Tìm câu SAI. Quan điểm mới trong giải quyết vấn đề xã hội:",
      "options": [
        "A. Kế hoạch phát triển kinh tế phải tính đến mục tiêu phát triển các lĩnh vực xã hội có liên quan trực tiếp.",
        "B. Mục tiêu phát triển kinh tế phải tính đến tác động và hậu quả xã hội có thể xảy ra để chủ động xử lý.",
        "C. Mục tiêu phát triển kinh tế phải được ưu tiên trước vấn đề xã hội để tạo cơ sở vật chất nhằm giải quyết vấn đề xã hội và môi trường.",
        "D. Chính sách xã hội phải được thực hiện trên cơ sở phát triển kinh tế, gắn bó hữu cơ giữa quyền lợi và nghĩa vụ, giữa cống hiến và hưởng thụ."
      ],
      "answer": ""
    },
    {
      "question": "Đại Hội nào Đảng ta xác định xã hội xã hội chủ nghĩa mà nhân dân ta xây dựng là một xã hội: “...Con người được giải phóng khỏi áp bức, bóc lột, bất công, làm theo năng lực, hưởng theo lao động, có cuộc sống ấm no, tự do, hạnh phúc, có điều kiện phát triển toàn diện cá nhân..”?",
      "options": [
        "A. Đại hội lần thứ VII (6/1991).",
        "B. Đại hội lần thứ VIII (6/1996).",
        "C. Đại hội lần thứ IX (4/2001).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Sau khi Cách mạng Tháng Tám năm 1945 thành công, ngày 3-10-1945, Chính phủ lâm thời nước Việt Nam Dân chủ Cộng hòa ra \"Thông cáo về chính sách ngoại giao của nước Cộng hòa Dân chủ Việt Nam\". Mục tiêu của đối ngoại được xác định là:",
      "options": [
        "A. Tìm sự ủng hộ về quân sự.",
        "B. Chống lại chính phủ Pháp Đờ Gôn.",
        "C. Kêu gọi sự đầu tư của nước ngoài.",
        "D. Góp phần đưa nước nhà đến sự độc lập hoàn toàn và vĩnh viễn."
      ],
      "answer": ""
    },
    {
      "question": "Trung Quốc và Liên Xô đặt quan hệ ngoại giao với VN vào thời gian nào?",
      "options": [
        "A. Năm 1945.",
        "B. Năm 1950.",
        "C. Năm 1955.",
        "D. Năm 1960."
      ],
      "answer": ""
    },
    {
      "question": "“Thực lực là cái chiêng, ngoại giao là cái tiếng. Cái chiêng có to thì cái tiếng mới lớn” là câu nói của ai?",
      "options": [
        "A. Lê Duẩn.",
        "B. Hồ Chí Minh.",
        "C. Phạm Văn Đồng.",
        "D. Nguyễn Hữu Thọ."
      ],
      "answer": ""
    },
    {
      "question": "“Dĩ bất biến, ứng vạn biến” là câu nói của Hồ Chí Minh với ai trước khi Người lên đường sang Pháp năm 1946?",
      "options": [
        "A. Võ Nguyên Giáp.",
        "B. Phạm Văn Đồng.",
        "C. Huỳnh Thúc Kháng.",
        "D. Trường Chinh."
      ],
      "answer": ""
    },
    {
      "question": "\"Ra sức tranh thủ những điều kiện quốc tế thuận lợi để nhanh chóng hàn gắn vết thương chiến tranh, xây dựng cơ sở vật chất kỹ thuật của chủ nghĩa xã hội” là nhiệm vụ đối ngoại được xác định ở Đại Hội Đảng lần thứ mấy?",
      "options": [
        "A. Đại hội II",
        "B. Đại hội IV",
        "C. Đại hội V",
        "D. Đại hội VI"
      ],
      "answer": ""
    },
    {
      "question": "Bảo đảm thắng lợi cho sự nghiệp xây dựng chủ nghĩa xã hội ở miền Bắc và sự nghiệp thống nhất nước nhà là mục tiêu ngoại giao trong giai đoạn nào?",
      "options": [
        "A. 1945 — 1954",
        "B. 1954 — 1975",
        "C. 1975 — 1980",
        "D. 1980 — 1985"
      ],
      "answer": ""
    },
    {
      "question": "Trong văn kiện nào Thực dân Pháp và các nước cam kết tôn trọng độc lập chủ quyền và thống nhất toàn vẹn lãnh thổ của ba nước Đông Dương?",
      "options": [
        "A. Hiệp ước Patơnốt.",
        "B. Hiệp ước Sơ bộ",
        "C. Hiệp định Paris",
        "D. Hiệp định Giơnevơ."
      ],
      "answer": ""
    },
    {
      "question": "Việt Nam gia nhập tổ chức Liên Hiệp Quốc vào thời gian nào?",
      "options": [
        "A. Ngày 20/9/1977.",
        "B. Ngày 18/1/1979.",
        "C. Ngày 10/10/1981.",
        "D. Ngày 7/5/1986."
      ],
      "answer": ""
    },
    {
      "question": "Trung Quốc và Việt Nam bình thường hóa quan hệ ngoại giao vào thời gian nào?",
      "options": [
        "A. 1986.",
        "B. 1991.",
        "C. 1955.",
        "D. 2006."
      ],
      "answer": ""
    },
    {
      "question": "Việt Nam được bầu làm Ủy viên không thường trực Hội đồng bảo an Liên Hợp quốc vào nhiệm kỳ nào?",
      "options": [
        "A. Nhiệm kỳ 2000 -2001.",
        "B. Nhiệm kỳ 2003 -2006.",
        "C. Nhiệm kỳ 2008 -2009.",
        "D. Nhiệm kỳ 2009 -2010."
      ],
      "answer": ""
    },
    {
      "question": "Việt Nam là thành viên thứ bao nhiêu của WTO?",
      "options": [
        "A. Thứ 100.",
        "B. Thứ 115.",
        "C. Thứ 150.",
        "D. Thứ 155."
      ],
      "answer": ""
    },
    {
      "question": "Tính đến năm 2009, Việt Nam đã thiết lập quan hệ ngoại giao với bao nhiêu quốc gia trên thế giới?",
      "options": [
        "A. 100 nước.",
        "B. 150 nước.",
        "C. 169 nước.",
        "D. 200 nước."
      ],
      "answer": ""
    },
    {
      "question": "Chủ trương: \"Việt Nam muốn làm bạn với tất cả các nước trong cộng đồng thế giới, phấn đấu vì hòa bình, độc lập và phát triển\" được Đảng ta xác định tại Đại hội nào?",
      "options": [
        "A. Đại hội lần thứ VII (6/1991).",
        "B. Đại hội lần thứ VIII (6/1996).",
        "C. Đại hội lần thứ IX (4/2001).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Chủ trương: “Việt Nam sẵn sàng là bạn, là đối tác tin cậy của các nước trong cộng đồng thế giới, phấn đấu vì hòa bình, độc lập và phát triển” được Đảng ta xác định tại Đại hội nào?",
      "options": [
        "A. Đại hội lần thứ VII (6/1991).",
        "B. Đại hội lần thứ VIII (6/1996).",
        "C. Đại hội lần thứ IX (4/2001).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Nội dung nào không đúng với chủ trương đối ngoại của Đảng đưa ra tại Đại hội VIII (1996)?",
      "options": [
        "A. Củng cố quan hệ với các nước láng giềng.",
        "B. Mở rộng quan hệ với các đảng cầm quyền và các đảng khác.",
        "C. Mở rộng quan hệ đối ngoại nhân dân, tổ chức phi chính phủ.",
        "D. Thử nghiệm để tiến tới thực hiện đầu tư ra nước ngoài."
      ],
      "answer": ""
    },
    {
      "question": "Việt Nam gia nhập tổ chức Diễn đàn hợp tác kinh tế châu Á - Thái Bình Dương (APEC) vào thời gian nào?",
      "options": [
        "A. Tháng 9/2001.",
        "B. Tháng 1/2005.",
        "C. Tháng 1/2007.",
        "D. Tháng 7/2007."
      ],
      "answer": ""
    },
    {
      "question": "Việt Nam tham gia Diễn đàn hợp tác Á - Âu (ASEM) với tư cách là thành viên sáng lập vào thời gian nào?",
      "options": [
        "A. Tháng 3/2001.",
        "B. Tháng 3/1996.",
        "C. Tháng 11/2006.",
        "D. Tháng 1/2007."
      ],
      "answer": ""
    },
    {
      "question": "Nghị quyết nào đã đặt nền móng để hình thành đường lối đối ngoại độc lập tự chủ, rộng mở, đa phương hóa đa dạng hóa quan hệ quốc tế?",
      "options": [
        "A. Nghị quyết Đại hội lần thứ V (3/1982).",
        "B. Nghị quyết Đại hội lần thứ VI (12/1986).",
        "C. Nghị quyết số 13 của Bộ chính trị (5/1988).",
        "D. Nghị quyết Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Tại Đại hội nào Đảng ta nhận định: \"Toàn cầu hóa kinh tế là một một xu thế khách quan, lôi cuốn ngày càng nhiều nước tham gia....chứa đựng nhiều mâu thuẫn, vừa có mặt tích cực, vừa có mặt tiêu cực, vừa có hợp tác vừa có đấu tranh\"?",
      "options": [
        "A. Đại hội lần thứ VII (6/1991).",
        "B. Đại hội lần thứ VIII (6/1996).",
        "C. Đại hội lần thứ IX (4/2001).",
        "D. Đại hội lần thứ X (4/2006)."
      ],
      "answer": ""
    },
    {
      "question": "Quan điểm: \"Mở rộng, đa dạng hoá, đa phương hoá các quan hệ đối ngoại\" được đề ra tại:",
      "options": [
        "A. Đại hội VI (tháng 12/1986)",
        "B. Đại hội VII (tháng 6/1991)",
        "C. Đại hội VIII (tháng 6/1996)",
        "D. Đại hội IX (tháng 4/2001)"
      ],
      "answer": ""
    },
    {
      "question": "Việt Nam trở thành thành viên chính thức của ASEAN vào thời gian và là thành viên thứ:",
      "options": [
        "A. 7/1994, thành viên thứ 6",
        "B. 7/1995, thành viên thứ 7",
        "C. 7/1996, thành viên thứ 8",
        "D. 7/1997, thành viên thứ 9"
      ],
      "answer": ""
    },
    {
      "question": "Việt Nam bình thường hóa quan hệ với Mỹ vào thời gian:",
      "options": [
        "A. 1994",
        "B. 1995",
        "C. 1996",
        "D. 1997"
      ],
      "answer": ""
    },
    {
      "question": "Việt Nam trở thành thành viên chính thức của tổ chức Thương mại thế giới (WTO) vào thời gian nào, là thành viên thứ mấy:",
      "options": [
        "A. 2006, thành viên thứ 149",
        "B. 2007, thành viên thứ 150",
        "C. 2006, thành viên thứ 151",
        "D. 2007, thành viên thứ 149"
      ],
      "answer": ""
    },
    {
      "question": "“Chiến lược biển Việt Nam đến năm 2020” được thông qua tại:",
      "options": [
        "A. Đại hội VIII (tháng 6/1996)",
        "B. Hội nghị trung ương 2 khóa X (2005)",
        "C. Đại hội X (tháng 4/2006)",
        "D. Hội nghị Trung ương 4 khóa X (1 - 2007)"
      ],
      "answer": ""
    },
    {
      "question": "Quan điểm của Đảng: \"Xây dựng nền văn hóa Việt Nam tiên tiến, đậm đà bản sắc dân tộc\", được Đảng nêu lần đầu tiên tại:",
      "options": [
        "A. Đại hội VI (tháng 12/1986)",
        "B. Đại hội VII (tháng 6/1991)",
        "C. Đại hội VIII (tháng 6/1996)",
        "D. Đại hội IX (tháng 4/2001)"
      ],
      "answer": ""
    },
    {
      "question": "Đại hội nào của Đảng đưa ra quan điểm chỉ đạo: “Đổi mới căn bản và toàn diện giáo dục và đào tạo...”:",
      "options": [
        "A. Đại hội VIII",
        "B. Đại hội IX",
        "C. Đại hội X",
        "D. Đại hội XI"
      ],
      "answer": ""
    },
    {
      "question": "Đại hội nào của Đảng đã đề ra chủ trương về đối ngoại: \"Hợp tác bình đẳng và cùng có lợi với tất cả các nước, không phân biệt chế độ chính trị - xã hội, trên cơ sở các nguyên tắc cùng tôn trọng hòa bình\":",
      "options": [
        "A. Đại hội VI",
        "B. Đại hội VII",
        "C. Đại hội VIII",
        "D. Đại hội IX"
      ],
      "answer": ""
    },
    {
      "question": "Quan điểm “Đoàn kết, hợp tác toàn diện với Liên Xô, coi quan hệ với Liên Xô là hòn đá tảng trong chính sách đối ngoại của Việt Nam” được xác định vào giai đoạn:",
      "options": [
        "A. 1945-1954.",
        "B. 1954-1975.",
        "C. 1975-1985.",
        "D. 1986-1996."
      ],
      "answer": ""
    },
    {
      "question": "Ngay sau khi chiến dịch Điện Biên Phủ kết thúc, Hội nghị quốc tế về chấm dứt chiến tranh Đông Dương đã diễn ra tại:",
      "options": [
        "A. Pari",
        "B. Giơnevơ.",
        "C. Postđam",
        "D. New York"
      ],
      "answer": ""
    },
    {
      "question": "Hiệp định Giơnevơ về chấm dứt chiến tranh, lập lại hoà bình ở Đông Dương đã quy định:",
      "options": [
        "A. Các nước tham dự Hội nghị cam kết tôn trọng các quyền dân tộc cơ bản là độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ của nhân dân Việt Nam và nhân dân Lào, Campuchia",
        "B. Pháp rút quân ra khỏi 3 nước Đông Dương. Vĩ tuyến 17 là giới tuyến quân sự tạm thời ở Việt Nam và sẽ tổng tuyển cử thống nhất đất nước vào tháng 7-1956",
        "C. Pháp tuyên bố công nhận Việt Nam là một nước tự do",
        "D. Cả hai phương án A và B."
      ],
      "answer": ""
    },
    {
      "question": "Cương lĩnh xây dựng đất nước trong thời kỳ quá độ lên chủ nghĩa xã hội được thông qua trong Đại hội nào của Đảng:",
      "options": [
        "A. Đại hội VI",
        "B. Đại hội VII",
        "C. Đại hội VIII",
        "D. Đại hội IX"
      ],
      "answer": ""
    }
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['questions'].extend(new_questions)
data['section'] = 'file2_full_to_page27'

with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully appended {len(new_questions)} questions from pages 21-27!")
