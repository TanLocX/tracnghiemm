import json

clean_questions = [
    # 157
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
    # 158
    {
        "question": "Quan điểm của Đảng: \"Nền kinh tế thị trường định hướng XHCN là mô hình kinh tế tổng quát của nước ta trong thời kỳ quá độ lên CNXH\" được xác định từ:",
        "options": [
            "A. Đại hội VI",
            "B. Đại hội VII",
            "C. Đại hội VIII",
            "D. Đại hội IX"
        ],
        "answer": "D. Đại hội IX"
    },
    # 159
    {
        "question": "Quan điểm: \"Kinh tế thị trường định hướng XHCN là một kiểu tổ chức kinh tế, vừa tuân theo quy luật của kinh tế thị trường, vừa dựa trên cơ sở và chịu sự dẫn dắt, chi phối bởi các nguyên tắc và bản chất của CNXH\" được xác định tại:",
        "options": [
            "A. Đại hội VII",
            "B. Đại hội VIII",
            "C. Đại hội IX",
            "D. Đại hội X"
        ],
        "answer": "D. Đại hội X"
    },
    # 160
    {
        "question": "Nội dung nào dưới đây được đề ra trong Chỉ thị số 100-CT/TW của Đảng (13/1/1981)?",
        "options": [
            "A. Mở rộng khoán sản phẩm đến nhóm lao động và người lao động trong hợp tác xã nông nghiệp",
            "B. Đổi mới cơ chế kinh tế nông nghiệp: thực hiện cơ chế khoán sản phẩm cuối cùng đến nhóm hộ và hộ xã viên.",
            "C. Mở rộng hình thức trả lương sản phẩm và vận dụng hình thức tiền thưởng trong các đơn vị sản xuất kinh doanh của nhà nước."
        ],
        "answer": "A. Mở rộng khoán sản phẩm đến nhóm lao động và người lao động trong hợp tác xã nông nghiệp"
    },
    # 161
    {
        "question": "Chọn câu SAI khi nói về nền kinh tế kế hoạch hóa tập trung bao cấp?",
        "options": [
            "A. Nhà nước bao cấp qua giá.",
            "B. Nhà nước bao cấp qua chế độ tem phiếu.",
            "C. Nhà nước bao cấp theo chế độ cấp phát vốn.",
            "D. Các hình thức bao cấp trên đã ngừng thực hiện ở năm 1975."
        ],
        "answer": "D. Các hình thức bao cấp trên đã ngừng thực hiện ở năm 1975."
    },
    # 162
    {
        "question": "Việc duy trì cơ chế tập trung bao cấp của Đảng ta có nguyên nhân chủ yếu từ?",
        "options": [
            "A. Hoàn cảnh chiến tranh.",
            "B. Nhận thức không đầy đủ về những đặc trưng của thời kỳ quá độ lên chủ nghĩa xã hội.",
            "C. Tư duy độc lập dân tộc gắn với chủ nghĩa xã hội.",
            "D. Quan hệ với các nước trong hệ thống xã hội chủ nghĩa."
        ],
        "answer": "B. Nhận thức không đầy đủ về những đặc trưng của thời kỳ quá độ lên chủ nghĩa xã hội."
    },
    # 163
    {
        "question": "Tại đại hội nào Đảng ta đã xác định cơ chế vận hành của nền kinh tế ở nước ta là \"cơ chế thị trường có sự quản lý của Nhà nước bằng pháp luật, chính sách và các công cụ khác\"?",
        "options": [
            "A. Đại hội lần thứ VI (12/1986).",
            "B. Đại hội lần thứ VII (6/1991).",
            "C. Đại hội lần thứ IX (4/2001).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "B. Đại hội lần thứ VII (6/1991)."
    },
    # 164
    {
        "question": "Đại hội nào đã xác định: Kinh tế thị trường định hướng xã hội chủ nghĩa là một kiểu tổ chức kinh tế vừa tuân theo quy luật của kinh tế thị trường vừa dựa trên cơ sở và chịu sự dẫn dắt chi phối bởi các nguyên tắc và bản chất của chủ nghĩa xã hội?",
        "options": [
            "A. Đại hội lần thứ VII (6/1991).",
            "B. Đại hội lần thứ VIII (6/1996).",
            "C. Đại hội lần thứ IX (4/2001).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "D. Đại hội lần thứ X (4/2006)."
    },
    # 165
    {
        "question": "Kinh tế thị trường có mầm mống từ trong xã hội nào?",
        "options": [
            "A. Phong kiến",
            "B. Tư bản chủ nghĩa",
            "C. Chiếm hữu nô lệ",
            "D. Xã hội chủ nghĩa."
        ],
        "answer": "A. Phong kiến"
    },
    # 166
    {
        "question": "Theo tư duy mới, kinh tế thị trường chỉ đối lập với?",
        "options": [
            "A. Kinh tế tự nhiên tự cấp, tự túc.",
            "B. Kinh tế tư bản chủ nghĩa.",
            "C. Kinh tế trong thời kỳ quá độ lên chủ nghĩa xã hội",
            "D. Kinh tế XHCN"
        ],
        "answer": "A. Kinh tế tự nhiên tự cấp, tự túc."
    },
    # 167
    {
        "question": "Một trong những đặc trưng của nền kinh tế thị trường định hướng XHCN là?",
        "options": [
            "A. Gồm nhiều thành phần kinh tế.",
            "B. Gồm nhiều thành phần kinh tế, trong đó kinh tế nhà nước giữ vai trò chủ đạo",
            "C. Gồm nhiều thành phần kinh tế, trong đó kinh tế tư nhân giữ vai trò chủ đạo",
            "D. Gồm nhiều thành phần kinh tế, trong đó kinh tế tư bản nhà nước giữ vai trò chủ đạo."
        ],
        "answer": "B. Gồm nhiều thành phần kinh tế, trong đó kinh tế nhà nước giữ vai trò chủ đạo"
    },
    # 168
    {
        "question": "Nền kinh tế thị trường định hướng XHCN thực hiện nhiều hình thức phân phối thu nhập, trong đó?",
        "options": [
            "A. Phân phối bình quân là hình thức chủ yếu.",
            "B. Phân phối theo kết quả lao động là hình thức chủ yếu.",
            "C. Phân phối qua các quỹ phúc lợi xã hội, tập thể là chủ yếu.",
            "D. Phân phối theo vốn, tài sản, cổ phần là chủ yếu."
        ],
        "answer": "B. Phân phối theo kết quả lao động là hình thức chủ yếu."
    },
    # 169
    {
        "question": "Sự khác biệt về mục đích phát triển của kinh tế thị trường định hướng XHCN ở nước ta và kinh tế thị trường tư bản chủ nghĩa nói chung?",
        "options": [
            "A. để nâng cao tiềm lực của các doanh nghiệp.",
            "B. để nâng cao đời sống cho mọi người, mọi người đều được hưởng những thành quả phát triển.",
            "C. để bảo vệ và phát triển các tập đoàn kinh tế.",
            "D. để có lợi nhuận tối đa."
        ],
        "answer": "B. để nâng cao đời sống cho mọi người, mọi người đều được hưởng những thành quả phát triển."
    },
    # 170
    {
        "question": "Đại hội nào Đảng ta xác định 5 thành phần kinh tế gồm: Kinh tế nhà nước; Kinh tế tập thể; Kinh tế tư nhân (cá thể, tiểu chủ, tư bản tư nhân); Kinh tế tư bản nhà nước và Kinh tế có vốn đầu tư nước ngoài?",
        "options": [
            "A. Đại hội lần thứ VII (6/1991).",
            "B. Đại hội lần thứ VIII (6/1996).",
            "C. Đại hội lần thứ IX (4/2001).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "C. Đại hội lần thứ IX (4/2001)."
    },
    # 171
    {
        "question": "Một trong những quan điểm để hoàn thiện thể chế kinh tế thị trường định hướng XHCN ở VN là?",
        "options": [
            "A. Đẩy mạnh CNH, HĐH, ứng dụng nhanh tiến bộ khoa học - công nghệ, đẩy mạnh phân công lao động quốc tế.",
            "B. Chủ động tích cực giải quyết các vấn đề lý luận và thực tiễn quan trọng, bức xúc, đồng thời phải có bước đi vững chắc, vừa làm vừa rút kinh nghiệm.",
            "C. Đẩy mạnh CNH, HĐH, ứng dụng nhanh tiến bộ khoa học - công nghệ, đẩy mạnh phân công chuyên môn hóa.",
            "D. Đẩy mạnh CNH, HĐH, ứng dụng nhanh tiến bộ khoa học - công nghệ, đẩy mạnh phân công xã hội."
        ],
        "answer": "B. Chủ động tích cực giải quyết các vấn đề lý luận và thực tiễn quan trọng, bức xúc, đồng thời phải có bước đi vững chắc, vừa làm vừa rút kinh nghiệm."
    },
    # 172
    {
        "question": "Một trong những chủ trương của Đảng để tiếp tục hoàn thiện thể chế kinh tế thị trường định hướng XHCN ở VN là:",
        "options": [
            "A. Hình thành và phát triển không đồng bộ các loại thị trường.",
            "B. Hình thành và phát triển đồng bộ các loại thị trường trong và ngoài nước.",
            "C. Hoàn thiện thể chế đảm bảo đồng bộ các yếu tố thị trường và phát triển đồng bộ các loại thị trường.",
            "D. Hình thành và phát triển đồng bộ các loại thị trường dịch vụ."
        ],
        "answer": "C. Hoàn thiện thể chế đảm bảo đồng bộ các yếu tố thị trường và phát triển đồng bộ các loại thị trường."
    },
    # 173
    {
        "question": "Thuật ngữ \"hệ thống chính trị\" được Đảng ta sử dụng lần đầu tiên tại:",
        "options": [
            "A. Đại hội lần thứ IV (12/1976).",
            "B. Đại hội lần thứ VI (12/1986).",
            "C. Hội nghị TW 6 - khóa VI (3/1989).",
            "D. Đại hội lần thứ VII (6/1991)."
        ],
        "answer": "C. Hội nghị TW 6 - khóa VI (3/1989)."
    },
    # 174
    {
        "question": "Đảng ta khẳng định \"Nhà nước xã hội chủ nghĩa Việt Nam là nhà nước chuyên chính vô sản\" tại:",
        "options": [
            "A. Đại hội toàn quốc lần thứ IV (12/1976).",
            "B. Hiến pháp nước Việt Nam dân chủ cộng hòa (1946).",
            "C. Hiến pháp nước cộng hòa xã hội chủ nghĩa Việt Nam (1980).",
            "D. Đại hội Đảng lần thứ VI (12/1986)."
        ],
        "answer": "C. Hiến pháp nước cộng hòa xã hội chủ nghĩa Việt Nam (1980)."
    },
    # 175
    {
        "question": "Thuật ngữ \"hệ thống chuyên chính vô sản\" được Đảng bắt đầu sử dụng chính thức từ:",
        "options": [
            "A. Đại hội lần thứ I (3/1935).",
            "B. Đại hội lần thứ III (9/1960).",
            "C. Đại hội lần thứ IV (12/1976).",
            "D. Đại hội lần thứ VI (12/1986)."
        ],
        "answer": "C. Đại hội lần thứ IV (12/1976)."
    },
    # 176
    {
        "question": "Đảng ta xác định cơ sở xã hội của hệ thống chuyên chính vô sản gồm:",
        "options": [
            "A. Liên minh giai cấp giữa giai cấp công nhân và nông dân.",
            "B. Liên minh giai cấp giữa giai cấp công nhân - nông dân và tầng lớp trí thức.",
            "C. Liên minh giai cấp giữa giai cấp nông dân và tầng lớp trí thức.",
            "D. Liên minh giai cấp giữa giai cấp công nhân - nông dân và tầng lớp tiểu tư sản."
        ],
        "answer": "B. Liên minh giai cấp giữa giai cấp công nhân - nông dân và tầng lớp trí thức."
    },
    # 177
    {
        "question": "Hệ thống chính trị ở Việt Nam gồm:",
        "options": [
            "A. Đảng, Mặt trận Tổ quốc Việt Nam, Mặt trận dân chủ và Nhà nước.",
            "B. Đảng, Nhà nước, Mặt trận Tổ quốc và các đoàn thể chính trị - xã hội (Tổng liên đoàn lao động Việt Nam, Đoàn thanh niên cộng sản Hồ Chí Minh, Hội liên hiệp phụ nữ Việt Nam, Hội cựu chiến binh Việt Nam, Hội nông dân Việt Nam...).",
            "C. Đảng, Nhà nước, Mặt trận Tổ quốc Việt Nam, Mặt trận Liên Việt.",
            "D. Đảng Cộng sản Việt Nam, Nhà nước, Mặt trận Tổ quốc, Đảng dân chủ và Đảng xã hội."
        ],
        "answer": "B. Đảng, Nhà nước, Mặt trận Tổ quốc và các đoàn thể chính trị - xã hội (Tổng liên đoàn lao động Việt Nam, Đoàn thanh niên cộng sản Hồ Chí Minh, Hội liên hiệp phụ nữ Việt Nam, Hội cựu chiến binh Việt Nam, Hội nông dân Việt Nam...)."
    },
    # 178
    {
        "question": "Điền vào chỗ trống: Trong đường lối xây dựng hệ thống chính trị Đảng ta xác định vai trò rất quan trọng của ......... là tập hợp, vận động, đoàn kết rộng rãi các tầng lớp nhân dân, đại diện cho quyền và lợi ích hợp pháp của nhân dân, thực hiện tốt vai trò giám sát và phản biện xã hội.",
        "options": [
            "A. Đảng.",
            "B. Nhà nước.",
            "C. Mặt trận tổ quốc Việt Nam và các đoàn thể.",
            "D. Chính phủ."
        ],
        "answer": "C. Mặt trận tổ quốc Việt Nam và các đoàn thể."
    },
    # 179
    {
        "question": "Theo Đại hội IX mối quan hệ giữa các giai cấp, các tầng lớp trong xã hội là \"quan hệ ..... trong nội bộ nhân dân đoàn kết và hợp tác lâu dài sự nghiệp xây dựng và bảo vệ tổ quốc dưới sự lãnh đạo của Đảng\".",
        "options": [
            "A. Hợp tác và đoàn kết.",
            "B. Hợp tác và đấu tranh.",
            "C. Đồng thuận.",
            "D. Tùy thuộc lẫn nhau."
        ],
        "answer": "C. Đồng thuận."
    },
    # 180
    {
        "question": "Chọn câu SAI. Về vị trí và vai trò của Đảng, Cương lĩnh 1991 xác định:",
        "options": [
            "A. Đảng lãnh đạo hệ thống chính trị đồng thời là một bộ phận của hệ thống chính trị",
            "B. Đảng liên hệ mật thiết với nhân dân, chịu sự giám sát của nhân dân",
            "C. Đảng đề ra Hiến pháp và Pháp luật",
            "D. Đảng hoạt động trong khuôn khổ hiến pháp và pháp luật"
        ],
        "answer": "C. Đảng đề ra Hiến pháp và Pháp luật"
    },
    # 181
    {
        "question": "Nhà nước pháp quyền là:",
        "options": [
            "A. Sản phẩm của xã hội tư bản chủ nghĩa",
            "B. Sản phẩm của xã hội chủ nghĩa",
            "C. Sản phẩm của trí tuệ nhân loại trong quản lý xã hội.",
            "D. Sản phẩm của xã hội phong kiến."
        ],
        "answer": "C. Sản phẩm của trí tuệ nhân loại trong quản lý xã hội."
    },
    # 182
    {
        "question": "Bản \"Đề cương văn hóa Việt Nam\" được Ban thường vụ TW Đảng thông qua năm 1943, do ai trực tiếp soạn thảo?",
        "options": [
            "A. Hồ Chí Minh",
            "B. Phạm Văn Đồng",
            "C. Trường Chinh",
            "D. Lê Duẩn."
        ],
        "answer": "C. Trường Chinh"
    },
    # 183
    {
        "question": "Đề cương văn hóa Việt Nam được Đảng xây dựng:",
        "options": [
            "A. Trước Cách mạng tháng Tám",
            "B. Trong kháng chiến chống Pháp",
            "C. Trong kháng chiến chống Mỹ",
            "D. Trong thời kỳ cả nước quá độ lên CNXH"
        ],
        "answer": "A. Trước Cách mạng tháng Tám"
    },
    # 184
    {
        "question": "Giữa thế kỷ 20 (năm 1945), Việt Nam có bao nhiêu dân số mù chữ?",
        "options": [
            "A. Hơn 70%",
            "B. Hơn 90%.",
            "C. Hơn 80%",
            "D. Hơn 60%."
        ],
        "answer": "B. Hơn 90%."
    },
    # 185
    {
        "question": "Đại hội lần thứ mấy Đảng ta đã đưa ra quan điểm phải xây dựng nền văn hóa VN thành một nền \"văn hóa tiên tiến và đậm đà bản sắc dân tộc\"?",
        "options": [
            "A. Đại hội lần thứ VI.",
            "B. Đại hội lần thứ VII.",
            "C. Đại hội lần thứ VIII.",
            "D. Đại hội lần thứ X."
        ],
        "answer": "C. Đại hội lần thứ VIII."
    },
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_idx = 157
for i in range(len(clean_questions)):
    data['questions'][start_idx + i] = clean_questions[i]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully cleaned questions {start_idx} to {start_idx + len(clean_questions) - 1}!")
print(f"Total questions cleaned: {len(clean_questions)}")
