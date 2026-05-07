import json

data = {
  "section": "file2_page1_to_5",
  "questions": [
    {
      "question": "Hội nghị Trung ương của Đảng mở đầu cho chủ trương chuyển hướng chỉ đạo chiến lược giai đoạn năm 1939 - 1945 là:",
      "options": [
        "A. Hội nghị Trung ương lần thứ 6 - tháng 11/1939",
        "B. Hội nghị Trung ương lần thứ 7 - tháng 11/1940",
        "C. Hội nghị Trung ương lần thứ 8 - tháng 5/1941",
        "D. Hội nghị Trung ương lần thứ 9 - tháng 8/1945"
      ],
      "answer": ""
    },
    {
      "question": "Nội dung chủ trương chuyển hướng chỉ đạo chiến lược giai đoạn năm 1939 - 1945 là:",
      "options": [
        "A. Đưa nhiệm vụ đấu tranh giai cấp lên hàng đầu",
        "B. Quyết định tiến hành Tổng khởi nghĩa",
        "C. Quyết định thành lập chiến khu Việt Bắc",
        "D. Đưa vấn đề giải phóng dân tộc lên hàng đầu"
      ],
      "answer": ""
    },
    {
      "question": "Nguyễn Ái Quốc về nước khi nào và chủ trì Hội nghị Trung ương Đảng lần mấy:",
      "options": [
        "A. Ngày 28 - 01 - 1939 / Chủ trì Hội nghị TW 6 (tháng 11/1939)",
        "B. Ngày 28 - 01 - 1941 / Chủ trì Hội nghị TW lần 8 (tháng 5/1941)",
        "C. Ngày 28 - 01 - 1942 / Chủ trì Hội nghị TW lần 7 (tháng 11/1940)",
        "D. Ngày 28 - 01 - 1943 / Chủ trì Hội nghị TW lần 9 (tháng 11/1944)"
      ],
      "answer": ""
    },
    {
      "question": "Từ năm 1940 nhân dân Việt Nam chịu cảnh “một cổ hai tròng” đó gồm 2 kẻ thù:",
      "options": [
        "A. Pháp và Mỹ",
        "B. Pháp và Tưởng Giới Thạch",
        "C. Nhật và Pháp",
        "D. Nhật và Tưởng Giới Thạch"
      ],
      "answer": ""
    },
    {
      "question": "Ngày Quốc tế lao động (1/5) được tổ chức kỷ niệm lần đầu tiên ở Việt Nam vào thời gian nào?",
      "options": [
        "A. Năm 1930",
        "B. Năm 1935",
        "C. Năm 1936",
        "D. Năm 1945"
      ],
      "answer": ""
    },
    {
      "question": "Văn kiện nào của Đảng đã xác định: “Vấn đề thổ địa là cái cốt của cách mạng tư sản dân quyền”?",
      "options": [
        "A. Đường cách mệnh",
        "B. Cương lĩnh đầu tiên của Đảng (3/2/1930)",
        "C. Luận cương chính trị (10/1930)",
        "D. Chính cương Đảng lao động Việt Nam"
      ],
      "answer": ""
    },
    {
      "question": "Các tổ chức quần chúng: “Công hội đỏ”, “Nông hội đỏ”... được thành lập trong thời kỳ nào?",
      "options": [
        "A. Thời kỳ 1930 - 1931",
        "B. Thời kỳ 1932 - 1935",
        "C. Thời kỳ 1936 - 1939",
        "D. Thời kỳ 1939 - 1945"
      ],
      "answer": ""
    },
    {
      "question": "Khẩu hiệu “Đấu tranh chống chế độ phản động thuộc địa, chống phát xít, chống chiến tranh, đòi tự do dân chủ, cơm áo và hòa bình” được nêu tại Hội nghị nào của Đảng?",
      "options": [
        "A. Hội nghị Ban chấp hành TW tháng 7/1936",
        "B. Hội nghị Ban chấp hành TW tháng 11/1939",
        "C. Hội nghị Ban chấp hành TW tháng 11/1940",
        "D. Hội nghị Ban chấp hành TW tháng 5/1941"
      ],
      "answer": ""
    },
    {
      "question": "Đảng ta chủ trương: “Chuyển hình thức tổ chức bí mật, không hợp pháp sang hình thức tổ chức công khai, hợp pháp, nửa hợp pháp...” tại:",
      "options": [
        "A. Hội nghị Ban chấp hành TW tháng 7/1936",
        "B. Hội nghị Ban chấp hành TW tháng 11/1939",
        "C. Hội nghị Ban chấp hành TW tháng 11/1940",
        "D. Hội nghị Ban chấp hành TW tháng 5/1941"
      ],
      "answer": ""
    },
    {
      "question": "Tổ chức \"Mặt trận dân chủ Đông Dương” được thành lập vào thời kỳ nào?",
      "options": [
        "A. Thời kỳ 1930 - 1931",
        "B. Thời kỳ 1932 - 1935",
        "C. Thời kỳ 1936 - 1939",
        "D. Thời kỳ 1939 - 1945"
      ],
      "answer": ""
    },
    {
      "question": "Chủ trương chuyển hướng chỉ đạo chiến lược của Đảng ta trong thời kỳ 1939 - 1945 nhằm:",
      "options": [
        "A. Ưu tiên giải quyết vấn đề ruộng đất cho nông dân.",
        "B. Giải quyết vấn đề dân sinh, dân chủ, cơm áo và hòa bình.",
        "C. Tập trung giải quyết vấn đề giải phóng dân tộc."
      ],
      "answer": ""
    },
    {
      "question": "Chủ trương tạm gác khẩu hiệu “cách mạng ruộng đất” thay bằng các khẩu hiệu “chống địa tô cao, chống cho vay nặng lãi”, “tịch thu ruộng đất của bọn thực dân đế quốc và bọn địa chủ phản lại quyền lợi dân tộc chia cho dân cày nghèo” được đề ra lần đầu tiên tại:",
      "options": [
        "A. Hội nghị Ban chấp hành TW lần thứ 6 (11/1939)",
        "B. Hội nghị Ban chấp hành TW lần thứ 8 (5/1941)",
        "C. Hội nghị Ban thường vụ TW (3/1945)",
        "D. Hội nghị toàn quốc của Đảng (8/1935)"
      ],
      "answer": ""
    },
    {
      "question": "Hội nghị có ý nghĩa mở đầu cho quá trình chuyển hướng chỉ đạo chiến lược cách mạng của Đảng trong thời kỳ vận động giải phóng dân tộc 1939 - 1945:",
      "options": [
        "A. Hội nghị Ban chấp hành TW tháng 11/1939",
        "B. Hội nghị Ban chấp hành TW tháng 11/1940",
        "C. Hội nghị Ban chấp hành TW tháng 5/1941",
        "D. Hội nghị Ban chấp hành TW tháng 8/1945"
      ],
      "answer": ""
    },
    {
      "question": "Trong các nguyên nhân sau đây, nguyên nhân nào quyết định nhất đối với thắng lợi của Cách mạng Tháng 8 - 1945?",
      "options": [
        "A. Nhật đầu hàng Đồng minh.",
        "B. Có sự lãnh đạo kịp thời, đúng đắn và sáng tạo của Đảng.",
        "C. Lực lượng cách mạng quần chúng được tổ chức và chuẩn bị chu đáo.",
        "D. Có Việt Nam quốc dân đảng (Việt quốc) và Việt Nam cách mạng đảng (Việt cách) tham gia."
      ],
      "answer": ""
    },
    {
      "question": "Các tổ chức quần chúng: Công nhân cứu quốc, nông dân cứu quốc, thanh niên cứu quốc, phụ nữ cứu quốc... được thành lập vào thời kỳ nào?",
      "options": [
        "A. Thời kỳ 1930 - 1931",
        "B. Thời kỳ 1932 - 1935",
        "C. Thời kỳ 1936 - 1939",
        "D. Thời kỳ 1941 - 1945"
      ],
      "answer": ""
    },
    {
      "question": "Đảng ta chớp thời cơ quyết định tổng khởi nghĩa giành chính quyền (8/1945) khi:",
      "options": [
        "A. Quân Đồng minh kéo vào Đông Dương.",
        "B. Cách mạng Nhật bùng nổ giành thắng lợi.",
        "C. Ngay sau khi phát xít Nhật tuyên bố đầu hàng, và trước khi quân Đồng minh vào Đông Dương.",
        "D. Nhật đảo chính Pháp."
      ],
      "answer": ""
    },
    {
      "question": "Chỉ thị “Nhật Pháp bắn nhau và hành động của chúng ta” (12/3/1945) của Ban thường vụ TW Đảng đề ra nhiệm vụ đấu tranh:",
      "options": [
        "A. Đánh đuổi phát xít Pháp - Nhật.",
        "B. Đánh đuổi phát xít Nhật, lập chính quyền của nhân dân.",
        "C. Đánh đuổi thực dân Pháp giành độc lập dân tộc."
      ],
      "answer": ""
    },
    {
      "question": "Tại Hội nghị nào Đảng ta chủ trương phát động cao trào kháng Nhật cứu nước làm tiền đề cho tổng khởi nghĩa?",
      "options": [
        "A. Hội nghị Ban chấp hành TW lần thứ 6 (11/1939)",
        "B. Hội nghị Ban chấp hành TW lần thứ 8 (5/1941)",
        "C. Hội nghị Ban thường vụ TW (3/1945)",
        "D. Hội nghị toàn Đảng (8/1945)"
      ],
      "answer": ""
    },
    {
      "question": "Nguyễn Ái Quốc về nước chủ trì hội nghị nào của Đảng?",
      "options": [
        "A. Hội nghị Ban chấp hành TW lần thứ 6 tháng 11/1939",
        "B. Hội nghị Ban chấp hành TW lần thứ 7 tháng 11/1940",
        "C. Hội nghị Ban chấp hành TW lần thứ 8 tháng 5/1941",
        "D. Hội nghị Ban chấp hành TW tháng 8/1945"
      ],
      "answer": ""
    },
    {
      "question": "Nội dung nào dưới đây không đúng với ý nghĩa lịch sử của Cách mạng Tháng 8/1945?",
      "options": [
        "A. Đập tan xiềng xích nô lệ của thực dân trong gần một thế kỷ.",
        "B. Lập nên nước Việt Nam dân chủ cộng hòa.",
        "C. Nhân dân Việt Nam từ thân phận nô lệ trở thành người chủ đất nước.",
        "D. Làm sụp đổ hoàn toàn chủ nghĩa thực dân kiểu cũ."
      ],
      "answer": ""
    },
    {
      "question": "Trong chỉ thị \"Nhật, Pháp bắn nhau và hành động của chúng ta”, Ban Thường vụ T.Ư Đảng xác định kẻ thù của nhân dân Đông dương lúc này là:",
      "options": [
        "A. Phát xít Nhật và Pháp",
        "B. Phát xít Nhật",
        "C. Phát xít Pháp",
        "D. Thực dân Pháp và tay sai"
      ],
      "answer": ""
    },
    {
      "question": "Câu nói: “Dù phải đốt cháy cả dãy Trường Sơn cũng phải giành cho được độc lập” của Hồ Chí Minh được nói vào thời gian:",
      "options": [
        "A. Tháng 8/1945",
        "B. Tháng 9/1950",
        "C. Tháng 1/1954",
        "D. Tháng 1/1968"
      ],
      "answer": ""
    },
    {
      "question": "Khởi nghĩa giành chính quyền trong Cách mạng tháng 8 ở Sài Gòn diễn ra vào:",
      "options": [
        "A. Ngày 15/8/1945",
        "B. Ngày 19/8/1945",
        "C. Ngày 23/8/1945",
        "D. Ngày 25/8/1945"
      ],
      "answer": ""
    },
    {
      "question": "Lời tuyên bố của Hồ Chí Minh : “Toàn thể dân tộc Việt Nam quyết đem tất cả tinh thần và lực lượng để giữ vững quyền tự do độc lập ấy”, được trích trong:",
      "options": [
        "A. Cương lĩnh đầu tiên của Đảng (năm 1930)",
        "B. Tuyên ngôn Độc lập (năm 1945)",
        "C. Lời kêu gọi toàn quốc kháng chiến 19-12-1946",
        "D. Hiến pháp đầu tiên của nước Việt Nam Dân chủ Cộng hòa"
      ],
      "answer": ""
    },
    {
      "question": "Khó khăn lớn nhất của nước ta sau Cách mạng Tháng 8/1945?",
      "options": [
        "A. Nền kinh tế rơi vào tình trạng kiệt quệ.",
        "B. Các thế lực đế quốc bao vây chống phá hòng tiêu diệt chính quyền cách mạng non trẻ.",
        "C. Chính phủ nước Việt Nam dân chủ cộng hòa chưa được các nước trên thế giới công nhận về pháp lý.",
        "D. Tàn dư của chế độ cũ còn nặng nề, trên 90% dân số mù chữ."
      ],
      "answer": ""
    },
    {
      "question": "Tình cảnh nước ta sau Cách mạng tháng Tám được ví với hình ảnh:",
      "options": [
        "A. Phôi thai",
        "B. “Ngàn cân treo sợi tóc”",
        "C. Trứng nước",
        "D. Nếm mật nằm gai"
      ],
      "answer": ""
    },
    {
      "question": "Ngày 25/11/1945 Ban Chấp hành Trung ương Đảng ra chỉ thị:",
      "options": [
        "A. Nhật - Pháp bắn nhau và hành động của chúng ta.",
        "B. Kháng chiến, kiến quốc",
        "C. Hòa để tiến",
        "D. Toàn quốc kháng chiến."
      ],
      "answer": ""
    },
    {
      "question": "Trong đường lối kháng chiến chống thực dân Pháp (12/1946) của Đảng, phương châm kháng chiến của ta là:",
      "options": [
        "A. Kháng chiến toàn dân: Toàn diện; Lâu dài; Dựa vào sức mình là chính",
        "B. Kháng chiến trường kỳ: Toàn diện; Quyết liệt; Dựa vào sức mình và giúp đỡ quốc tế."
      ],
      "answer": ""
    }
  ]
}

with open(r'c:\vscode\code\TN_MMT\lichsudang\file2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("File successfully updated with perfect clean data.")
