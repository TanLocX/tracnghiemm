import json

answers = {
    180: "A. Sự chi viện nhiệt tình của hậu phương miền Bắc cho tiền tuyến miền Nam trong cuộc kháng chiến chống Mỹ",
    181: "B. Tổng công kích, tổng khởi nghĩa",
    182: "B. 12 ngày đêm",
    183: "D. Việt Nam hoá chiến tranh",
    184: "C. Dùng người Việt Nam đánh người Việt Nam",
    185: "A. Mỹ - Ngụy",
    186: "B. Lam Sơn 719",
    187: "A. 27/1/1973",
    188: "D. Chiến dịch Tây Nguyên",
    189: "C. Giải phóng miền Nam trong năm 1975",
    190: "C. Hồ Chí Minh",
    191: "D. Võ Nguyên Giáp",
    192: "A. Rút quân khỏi Việt Nam, tạo thế xoay chuyển có lợi cho cách mạng",
    193: "A. Đồng bằng sông Cửu Long và các đảo, quần đảo ở Biển Đông",
    194: "A. Giải quyết hài hoà nhiệm vụ của hai miền Nam Bắc trong bối cảnh nước ta bị chia cắt làm hai miền",
    195: "A. Giành lại nền độc lập, thống nhất, toàn vẹn lãnh thổ cho đất nước",
    196: "A. Sự trợ giúp, hy sinh quên mình của hậu phương lớn miền Bắc xã hội chủ nghĩa",
    197: "C. Chủ nghĩa anh hùng cách mạng",
    198: "A. Đã có hoà bình, độc lập, thống nhất, cả nước quá độ lên chủ nghĩa xã hội",
    199: "C. Hoàn thành việc thống nhất đất nước về mặt nhà nước",
    200: "A. Đồng thời tiến hành cải tạo xã hội chủ nghĩa và xây dựng chủ nghĩa xã hội",
    201: "C. Năm 1976",
    202: "A. Để mau chóng phát huy toàn bộ sức mạnh mới của đất nước",
    203: "A. 1976",
    204: "B. Văn Cao",
    205: "B. Nước ta đang trong quá trình từ sản xuất nhỏ tiến thẳng lên chủ nghĩa xã hội, bỏ qua giai đoạn phát triển tư bản chủ nghĩa",
    206: "B. Chuyên chính vô sản",
    207: "A. Quân Khmer Đỏ",
    208: "D. 1982",
    209: "C. Nông nghiệp",
    210: "B. Xoá bỏ cơ chế tập trung quan liêu, bao cấp chuyển sang cơ chế hạch toán kinh doanh",
    211: "B. Xây dựng thành công chủ nghĩa xã hội và bảo vệ vững chắc Tổ quốc Việt Nam xã hội chủ nghĩa",
    212: "A. Nền kinh tế có cơ cấu nhiều thành phần",
    213: "C. Đạt được những thắng lợi to lớn trong sự nghiệp bảo vệ Tổ quốc và làm nghĩa vụ quốc tế",
    214: "C. Việt Nam đang ở trong tình trạng khủng hoảng kinh tế - xã hội",
    215: "D. Sự thật",
    216: "A. Có những khuyết điểm trong hoạt động tư tưởng, tổ chức và công tác cán bộ của Đảng",
    217: "C. Hàng lương thực - thực phẩm, hàng tiêu dùng và hàng xuất khẩu",
    218: "C. Liên Xô",
    219: "A. Lấy dân làm gốc",
    220: "C. Người dân được nhận khoán và canh tác trên diện tích ổn định trong vòng 15 năm, đảm bảo có thu nhập từ 40% sản lượng khoán trở lên",
    221: "C. 1995",
    222: "C. Đảng Cộng sản - tập trung dân chủ",
    223: "B. Còn tồn tại nền kinh tế nhiều thành phần, trong đó có thành phần đối lập",
    224: "B. Chủ nghĩa Mác - Lênin",
    225: "B. Con người",
    226: "B. Tụt hậu về kinh tế, chệch hướng xã hội chủ nghĩa, nạn tham nhũng và nguy cơ “diễn biến hoà bình”",
    227: "A. Dân giàu, nước mạnh, xã hội công bằng, văn minh",
    228: "A. Kinh tế nhà nước",
    229: "C. Giáo dục - đào tạo và khoa học công nghệ",
    230: "A. Tạo ra nền tảng cơ bản để đến năm 2020 nước ta cơ bản trở thành một nước công nghiệp theo hướng hiện đại",
    231: "D. Kinh tế tư nhân",
    232: "C. Ra khỏi tình trạng kém phát triển",
    233: "B. Xây dựng, chỉnh đốn Đảng",
    234: "B. Đất đai",
    235: "C. Tôn trọng và bảo đảm quyền tự do tín ngưỡng",
    236: "B. Cho phép Đảng viên làm kinh tế tư nhân",
    237: "C. 2010",
    238: "C. Pháp luật",
    239: "A. 22",
    240: "A. Thanh niên",
    241: "D. 2006",
    242: "B. 230",
    243: "D. Trung Quốc",
    244: "B. 1999",
    245: "C. Báo chí",
    246: "B. 2013",
    247: "C. Quan liêu, tham nhũng, xa rời nhân dân",
    248: "B. Nước công nghiệp theo hướng hiện đại",
    249: "C. Mặt trận Tổ quốc Việt Nam",
    250: "B. Ứng xử của các bên ở biển Đông",
    251: "A. Trong bất kỳ điều kiện, tình huống nào cũng phải luôn kiên trì thực hiện đường lối và mục tiêu đổi mới",
    252: "A. 1.100USD",
    253: "A. Kinh tế, chính trị, xã hội",
    254: "C. Chăm lo xây dựng con người có nhân cách và lối sống tốt đẹp",
    255: "A. Xoá bỏ tình trạng nghèo đói cùng cực",
    256: "B. Biển",
    257: "D. Phòng chống tham nhũng",
    258: "B. Ban Nội chính Trung ương",
    259: "A. Đã xây dựng và hoàn thiện từng bước nền kinh tế thị trường định hướng xã hội chủ nghĩa",
    260: "C. Giảm nghèo",
    261: "A. Quán triệt tinh thần lấy dân làm gốc, vì lợi ích của nhân dân",
    262: "D. Công tác cán bộ",
    263: "C. Đảng lãnh đạo, Nhà nước quản lý, nhân dân làm chủ",
    264: "B. Cán bộ, đảng viên",
    265: "A. Một",
    266: "C. 1971",
    267: "C. 895 cuộc hành quân",
    268: "C. Quảng Trị",
    269: "C. Từ 4/1972 đến 1/1973",
}

with open(r'c:\vscode\code\TN_MMT\lichsudang\file4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

mismatches = []
for idx, answer_str in answers.items():
    q = data['questions'][idx]
    if answer_str not in q['options']:
        mismatches.append((idx, answer_str, q['options']))
    else:
        q['answer'] = answer_str

if mismatches:
    print("CẢNH BÁO - answer không khớp options:")
    for idx, ans, opts in mismatches:
        print(f"  Câu {idx}: '{ans}'")
        print(f"  Options: {opts}")
else:
    with open(r'c:\vscode\code\TN_MMT\lichsudang\file4.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    empty = [i for i, q in enumerate(data['questions']) if not q.get('answer', '').strip()]
    print(f"Done: câu 180 đến 269")
    print(f"Tổng câu còn thiếu answer: {len(empty)}")
    if empty:
        print(f"Câu thiếu: {empty}")
    else:
        print("Tất cả câu đã có answer!")
