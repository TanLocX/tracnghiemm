import json

clean_questions = [
    # 186
    {
        "question": "Chọn phương án để điền vào chỗ trống. Cương lĩnh năm 1991 đã đề ra 1 trong 7 phương hướng là \"Tiến hành cách mạng XHCN trong lĩnh vực tư tưởng và văn hóa làm cho ...... giữ vị trí chủ đạo trong đời sống tinh thần xã hội\"",
        "options": [
            "A. Những giá trị của Chủ nghĩa cộng sản",
            "B. Thế giới quan Mác Lênin và tư tưởng Hồ Chí Minh.",
            "C. Bản sắc dân tộc và yếu tố tiên tiến",
            "D. Tư duy thực tế"
        ],
        "answer": "B. Thế giới quan Mác Lênin và tư tưởng Hồ Chí Minh."
    },
    # 187
    {
        "question": "Đại hội VII (1991) và Đại hội VIII (1996) khẳng định lĩnh vực nào đóng vai trò then chốt trong sự nghiệp xây dựng chủ nghĩa xã hội và bảo vệ Tổ quốc?",
        "options": [
            "A. Khoa học công nghệ và an ninh quốc phòng",
            "B. Giáo dục - đào tạo và an ninh quốc phòng",
            "C. Ổn định chính trị và an ninh",
            "D. Giáo dục - đào tạo, khoa học - công nghệ."
        ],
        "answer": "D. Giáo dục - đào tạo, khoa học - công nghệ."
    },
    # 188
    {
        "question": "Chọn câu SAI. Quan điểm của Hội nghị TW 5 khóa VIII là:",
        "options": [
            "A. Xây dựng và phát triển nền văn hóa phải nhằm mục tiêu kinh tế, vì hiệu quả kinh tế.",
            "B. Nền văn hóa Việt Nam là nền văn hóa tiên tiến, đậm đà bản sắc dân tộc.",
            "C. Xây dựng và phát triển nền văn hóa là sự nghiệp của toàn dân, do Đảng lãnh đạo, trong đó đội ngũ trí thức giữ vai trò quan trọng.",
            "D. Văn hóa là nền tảng tinh thần của xã hội, vừa là mục tiêu, vừa là động lực thúc đẩy phát triển kinh tế - xã hội."
        ],
        "answer": "A. Xây dựng và phát triển nền văn hóa phải nhằm mục tiêu kinh tế, vì hiệu quả kinh tế."
    },
    # 189
    {
        "question": "Chọn câu SAI. Trong giai đoạn 1945-1954, chính sách xã hội của Đảng ta là:",
        "options": [
            "A. Làm cho dân có ăn, làm cho dân có mặc, làm cho dân có chỗ ở, làm cho dân được học hành.",
            "B. Làm cho người nghèo thì đủ ăn, người đủ ăn thì khá giàu, người khá giàu thì giàu thêm.",
            "C. Thực hiện đưa nông dân vào con đường làm ăn tập thể, phân phối bình quân.",
            "D. Thực hiện chính sách điều hòa lợi ích giữa chủ và thợ"
        ],
        "answer": "C. Thực hiện đưa nông dân vào con đường làm ăn tập thể, phân phối bình quân."
    },
    # 190
    {
        "question": "Nghị quyết Đại hội nào của Đảng chỉ rõ: \"Thực hiện chế độ phân phối chủ yếu theo kết quả lao động, hiệu quả kinh tế, đồng thời theo mức đóng góp vốn cùng các nguồn lực khác và thông qua phúc lợi xã hội\"?",
        "options": [
            "A. Đại hội lần thứ VII (6/1991).",
            "B. Đại hội lần thứ VIII (6/1996).",
            "C. Đại hội lần thứ IX (4/2001).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "C. Đại hội lần thứ IX (4/2001)."
    },
    # 191
    {
        "question": "Điền vào chỗ trống. Xây dựng và phát triển văn hóa là sự nghiệp của toàn dân do Đảng lãnh đạo, trong đó ..... giữ vai trò quan trọng.",
        "options": [
            "A. Giai cấp công nông.",
            "B. Giai cấp nông dân.",
            "C. Tầng lớp doanh nhân.",
            "D. Đội ngũ trí thức"
        ],
        "answer": "D. Đội ngũ trí thức"
    },
    # 192
    {
        "question": "Cốt lõi nền văn hóa của dân tộc là",
        "options": [
            "A. Hệ tư tưởng của giai cấp vô sản",
            "B. Hệ giá trị của dân tộc",
            "C. Hệ tư tưởng của giai cấp phong kiến",
            "D. Hệ tư tưởng của giai cấp tư sản"
        ],
        "answer": "B. Hệ giá trị của dân tộc"
    },
    # 193
    {
        "question": "Tại đại hội nào Đảng ta nâng các vấn đề xã hội lên tầm chính sách xã hội, đặt rõ tầm quan trọng của chính sách xã hội đối với chính sách kinh tế và chính sách ở các lĩnh vực khác?",
        "options": [
            "A. Đại hội VI",
            "B. Đại hội VII",
            "C. Đại hội VIII",
            "D. Đại hội IX"
        ],
        "answer": "C. Đại hội VIII"
    },
    # 194
    {
        "question": "Tìm câu SAI. Quan điểm mới trong giải quyết vấn đề xã hội:",
        "options": [
            "A. Kế hoạch phát triển kinh tế phải tính đến mục tiêu phát triển các lĩnh vực xã hội có liên quan trực tiếp.",
            "B. Mục tiêu phát triển kinh tế phải tính đến tác động và hậu quả xã hội có thể xảy ra để chủ động xử lý.",
            "C. Mục tiêu phát triển kinh tế phải được ưu tiên trước vấn đề xã hội để tạo cơ sở vật chất nhằm giải quyết vấn đề xã hội và môi trường.",
            "D. Chính sách xã hội phải được thực hiện trên cơ sở phát triển kinh tế, gắn bó hữu cơ giữa quyền lợi và nghĩa vụ, giữa công hiến và hưởng thụ."
        ],
        "answer": "C. Mục tiêu phát triển kinh tế phải được ưu tiên trước vấn đề xã hội để tạo cơ sở vật chất nhằm giải quyết vấn đề xã hội và môi trường."
    },
    # 195
    {
        "question": "Đại hội nào Đảng ta xác định xã hội xã hội chủ nghĩa mà nhân dân ta xây dựng là một xã hội: \"...Con người được giải phóng khỏi áp bức, bóc lột, bất công, làm theo năng lực, hưởng theo lao động, có cuộc sống ấm no, tự do, hạnh phúc, có điều kiện phát triển toàn diện cá nhân...\"?",
        "options": [
            "A. Đại hội lần thứ VII (6/1991).",
            "B. Đại hội lần thứ VIII (6/1996).",
            "C. Đại hội lần thứ IX (4/2001).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "A. Đại hội lần thứ VII (6/1991)."
    },
    # 196
    {
        "question": "Sau khi Cách mạng Tháng Tám năm 1945 thành công, ngày 3-10-1945, Chính phủ lâm thời nước Việt Nam Dân chủ Cộng hòa ra \"Thông cáo về chính sách ngoại giao của nước Cộng hòa Dân chủ Việt Nam\". Mục tiêu của đối ngoại được xác định là:",
        "options": [
            "A. Tìm sự ủng hộ về quân sự.",
            "B. Chống lại chính phủ Pháp Đờ Gôn.",
            "C. Kêu gọi sự đầu tư của nước ngoài.",
            "D. Góp phần đưa nước nhà đến sự độc lập hoàn toàn và vĩnh viễn"
        ],
        "answer": "D. Góp phần đưa nước nhà đến sự độc lập hoàn toàn và vĩnh viễn"
    },
    # 197
    {
        "question": "Trung Quốc và Liên Xô đặt quan hệ ngoại giao với VN vào thời gian nào?",
        "options": [
            "A. Năm 1945.",
            "B. Năm 1950.",
            "C. Năm 1955.",
            "D. Năm 1960."
        ],
        "answer": "B. Năm 1950."
    },
    # 198
    {
        "question": "\"Thực lực là cái chiêng, ngoại giao là cái tiếng. Cái chiêng có to thì cái tiếng mới lớn\" là câu nói của ai?",
        "options": [
            "A. Lê Duẩn.",
            "B. Hồ Chí Minh.",
            "C. Phạm Văn Đồng.",
            "D. Nguyễn Hữu Thọ."
        ],
        "answer": "B. Hồ Chí Minh."
    },
    # 199
    {
        "question": "\"Dĩ bất biến, ứng vạn biến\" là câu nói của Hồ Chí Minh với ai trước khi Người lên đường sang Pháp năm 1946?",
        "options": [
            "A. Võ Nguyên Giáp.",
            "B. Phạm Văn Đồng.",
            "C. Huỳnh Thúc Kháng.",
            "D. Trường Chinh."
        ],
        "answer": "C. Huỳnh Thúc Kháng."
    },
    # 200
    {
        "question": "\"Ra sức tranh thủ những điều kiện quốc tế thuận lợi để nhanh chóng hàn gắn vết thương chiến tranh, xây dựng cơ sở vật chất kỹ thuật của chủ nghĩa xã hội\" là nhiệm vụ đối ngoại được xác định ở Đại hội Đảng lần thứ mấy?",
        "options": [
            "A. Đại hội III",
            "B. Đại hội IV",
            "C. Đại hội V",
            "D. Đại hội VI"
        ],
        "answer": "B. Đại hội IV"
    },
    # 201
    {
        "question": "Bảo đảm thắng lợi cho sự nghiệp xây dựng chủ nghĩa xã hội ở miền Bắc và sự nghiệp thống nhất nước nhà là mục tiêu ngoại giao trong giai đoạn nào?",
        "options": [
            "A. 1945 - 1954",
            "B. 1954 - 1975",
            "C. 1975 - 1980",
            "D. 1980 - 1985"
        ],
        "answer": "B. 1954 - 1975"
    },
    # 202
    {
        "question": "Trong văn kiện nào Thực dân Pháp và các nước cam kết tôn trọng độc lập chủ quyền và thống nhất toàn vẹn lãnh thổ của ba nước Đông Dương?",
        "options": [
            "A. Hiệp ước Patơnốt.",
            "B. Hiệp ước Sơ bộ",
            "C. Hiệp định Paris",
            "D. Hiệp định Giơnevơ."
        ],
        "answer": "D. Hiệp định Giơnevơ."
    },
    # 203
    {
        "question": "Việt Nam gia nhập tổ chức Liên Hiệp quốc vào thời gian nào?",
        "options": [
            "A. Ngày 20/9/1977.",
            "B. Ngày 18/1/1979.",
            "C. Ngày 10/10/1981.",
            "D. Ngày 7/5/1986."
        ],
        "answer": "A. Ngày 20/9/1977."
    },
    # 204
    {
        "question": "Trung Quốc và Việt Nam bình thường hóa quan hệ ngoại giao vào thời gian nào?",
        "options": [
            "A. 1986.",
            "B. 1991.",
            "C. 1995.",
            "D. 2006."
        ],
        "answer": "B. 1991."
    },
    # 205
    {
        "question": "Việt Nam được bầu làm Ủy viên không thường trực Hội đồng bảo an Liên Hợp quốc vào nhiệm kỳ nào?",
        "options": [
            "A. Nhiệm kỳ 2000-2001.",
            "B. Nhiệm kỳ 2005-2006.",
            "C. Nhiệm kỳ 2008-2009.",
            "D. Nhiệm kỳ 2009-2010."
        ],
        "answer": "C. Nhiệm kỳ 2008-2009."
    },
    # 206
    {
        "question": "Việt Nam là thành viên thứ bao nhiêu của WTO?",
        "options": [
            "A. Thứ 100.",
            "B. Thứ 115.",
            "C. Thứ 150.",
            "D. Thứ 155."
        ],
        "answer": "C. Thứ 150."
    },
    # 207
    {
        "question": "Tính đến năm 2009, Việt Nam đã thiết lập quan hệ ngoại giao với bao nhiêu quốc gia trên thế giới?",
        "options": [
            "A. 100 nước.",
            "B. 150 nước.",
            "C. 169 nước.",
            "D. 200 nước."
        ],
        "answer": "C. 169 nước."
    },
    # 208
    {
        "question": "Chủ trương: \"Việt Nam muốn làm bạn với tất cả các nước trong cộng đồng thế giới, phấn đấu vì hòa bình, độc lập và phát triển\" được Đảng ta xác định tại Đại hội nào?",
        "options": [
            "A. Đại hội lần thứ VII (6/1991).",
            "B. Đại hội lần thứ VIII (6/1996).",
            "C. Đại hội lần thứ IX (4/2001).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "A. Đại hội lần thứ VII (6/1991)."
    },
    # 209
    {
        "question": "Chủ trương: \"Việt Nam sẵn sàng là bạn, là đối tác tin cậy của các nước trong cộng đồng thế giới, phấn đấu vì hòa bình, độc lập và phát triển\" được Đảng ta xác định tại Đại hội nào?",
        "options": [
            "A. Đại hội lần thứ VII (6/1991).",
            "B. Đại hội lần thứ VIII (6/1996).",
            "C. Đại hội lần thứ IX (4/2001).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "C. Đại hội lần thứ IX (4/2001)."
    },
    # 210
    {
        "question": "Nội dung nào không đúng với chủ trương đối ngoại của Đảng đưa ra tại Đại hội VIII (1996)?",
        "options": [
            "A. Củng cố quan hệ với các nước láng giềng.",
            "B. Mở rộng quan hệ với các đảng cầm quyền và các đảng khác",
            "C. Mở rộng quan hệ đối ngoại nhân dân, tổ chức phi chính phủ",
            "D. Thử nghiệm để tiến tới thực hiện đầu tư ra nước ngoài"
        ],
        "answer": "D. Thử nghiệm để tiến tới thực hiện đầu tư ra nước ngoài"
    },
    # 211
    {
        "question": "Việt Nam gia nhập tổ chức Diễn đàn hợp tác kinh tế châu Á - Thái Bình Dương (APEC) vào thời gian nào?",
        "options": [
            "A. Tháng 9/2001.",
            "B. Tháng 1/2005.",
            "C. Tháng 1/2007.",
            "D. Tháng 7/2007."
        ],
        "answer": "C. Tháng 1/2007."
    },
    # 212
    {
        "question": "Việt Nam tham gia Diễn đàn hợp tác Á - Âu (ASEM) với tư cách là thành viên sáng lập vào thời gian nào?",
        "options": [
            "A. Tháng 3/2001.",
            "B. Tháng 3/1996.",
            "C. Tháng 11/2006.",
            "D. Tháng 1/2007."
        ],
        "answer": "B. Tháng 3/1996."
    },
    # 213
    {
        "question": "Nghị quyết nào đã đặt nền móng để hình thành đường lối đối ngoại độc lập tự chủ, rộng mở, đa phương hóa, đa dạng hóa quan hệ quốc tế?",
        "options": [
            "A. Nghị quyết Đại hội lần thứ V (3/1982).",
            "B. Nghị quyết Đại hội lần thứ VI (12/1986).",
            "C. Nghị quyết số 13 của Bộ chính trị (5/1988).",
            "D. Nghị quyết Đại hội lần thứ X (4/2006)."
        ],
        "answer": "C. Nghị quyết số 13 của Bộ chính trị (5/1988)."
    },
    # 214
    {
        "question": "Tại Đại hội nào Đảng ta nhận định: \"Toàn cầu hóa kinh tế là một xu thế khách quan, lôi cuốn ngày càng nhiều nước tham gia....chứa đựng nhiều mâu thuẫn, vừa có mặt tích cực, vừa có mặt tiêu cực, vừa có hợp tác vừa có đấu tranh\"?",
        "options": [
            "A. Đại hội lần thứ VII (6/1991).",
            "B. Đại hội lần thứ VIII (6/1996).",
            "C. Đại hội lần thứ IX (4/2001).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "C. Đại hội lần thứ IX (4/2001)."
    },
    # 215
    {
        "question": "Quan điểm: \"Mở rộng, đa dạng hóa, đa phương hóa các quan hệ đối ngoại\" được đề ra tại:",
        "options": [
            "A. Đại hội VI (tháng 12/1986)",
            "B. Đại hội VII (tháng 6/1991)",
            "C. Đại hội VIII (tháng 6/1996)",
            "D. Đại hội IX (tháng 4/2001)"
        ],
        "answer": "B. Đại hội VII (tháng 6/1991)"
    },
    # 216
    {
        "question": "Việt Nam trở thành thành viên chính thức của ASEAN vào thời gian và là thành viên thứ:",
        "options": [
            "A. 7/1994, thành viên thứ 6",
            "B. 7/1995, thành viên thứ 7",
            "C. 7/1996, thành viên thứ 8",
            "D. 7/1997, thành viên thứ 9"
        ],
        "answer": "B. 7/1995, thành viên thứ 7"
    },
    # 217
    {
        "question": "Việt Nam bình thường hóa quan hệ với Mỹ vào thời gian:",
        "options": [
            "A. 1994",
            "B. 1995",
            "C. 1996",
            "D. 1997"
        ],
        "answer": "B. 1995"
    },
    # 218
    {
        "question": "Việt Nam trở thành thành viên chính thức của tổ chức Thương mại thế giới (WTO) vào thời gian nào, là thành viên thứ mấy?",
        "options": [
            "A. 2006, thành viên thứ 149",
            "B. 2007, thành viên thứ 150",
            "C. 2006, thành viên thứ 151",
            "D. 2007, thành viên thứ 149"
        ],
        "answer": "B. 2007, thành viên thứ 150"
    },
    # 219
    {
        "question": "\"Chiến lược biển Việt Nam đến năm 2020\" được thông qua tại:",
        "options": [
            "A. Đại hội VIII (tháng 6/1996)",
            "B. Hội nghị Trung ương 2 khóa IX (2005)",
            "C. Đại hội X (tháng 4/2006)",
            "D. Hội nghị Trung ương 4 khóa X (1/2007)"
        ],
        "answer": "D. Hội nghị Trung ương 4 khóa X (1/2007)"
    },
    # 220
    {
        "question": "Quan điểm của Đảng: \"Xây dựng nền văn hóa Việt Nam tiên tiến, đậm đà bản sắc dân tộc\", được Đảng nêu lần đầu tiên tại:",
        "options": [
            "A. Đại hội VI (tháng 12/1986)",
            "B. Đại hội VII (tháng 6/1991)",
            "C. Đại hội VIII (tháng 6/1996)",
            "D. Đại hội IX (tháng 4/2001)."
        ],
        "answer": "C. Đại hội VIII (tháng 6/1996)"
    },
    # 221
    {
        "question": "Đại hội nào của Đảng đưa ra quan điểm chỉ đạo: \"Đổi mới căn bản và toàn diện giáo dục và đào tạo ...\"?",
        "options": [
            "A. Đại hội VII",
            "B. Đại hội IX",
            "C. Đại hội X",
            "D. Đại hội XI"
        ],
        "answer": "D. Đại hội XI"
    },
    # 222
    {
        "question": "Đại hội nào của Đảng đã đề ra chủ trương về đối ngoại: \"Hợp tác bình đẳng và cùng có lợi với tất cả các nước, không phân biệt chế độ chính trị - xã hội, trên cơ sở các nguyên tắc cùng tôn trọng hòa bình\"?",
        "options": [
            "A. Đại hội VI",
            "B. Đại hội VII",
            "C. Đại hội VIII",
            "D. Đại hội IX"
        ],
        "answer": "B. Đại hội VII"
    },
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_idx = 186
for i in range(len(clean_questions)):
    data['questions'][start_idx + i] = clean_questions[i]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully cleaned questions {start_idx} to {start_idx + len(clean_questions) - 1}!")
print(f"Total questions cleaned: {len(clean_questions)}")
