import json

clean_questions = [
    {
      "question": "Thời gian thực dân Pháp tiến hành khai thác thuộc địa lần thứ nhất ở Việt Nam:",
      "options": [
        "A. 1858-1884",
        "B. 1884-1896",
        "C. 1896-1913",
        "D. 1914-1918"
      ],
      "answer": "C. 1896-1913"
    },
    {
      "question": "Trong đợt khai thác thuộc địa lần thứ nhất của thực dân Pháp ở nước ta đã hình thành giai cấp mới nào?",
      "options": [
        "A. Giai cấp tư sản",
        "B. Giai cấp tư sản và công nhân",
        "C. Giai cấp công nhân",
        "D. Giai cấp tiểu tư sản"
      ],
      "answer": "C. Giai cấp công nhân"
    },
    {
      "question": "Mâu thuẫn chủ yếu nhất của xã hội Việt Nam dưới ách thống trị của thực dân Pháp là:",
      "options": [
        "A. Mâu thuẫn giữa toàn thể nhân dân Việt Nam với đế quốc Pháp.",
        "B. Mâu thuẫn giữa nông dân với giai cấp địa chủ phong kiến.",
        "C. Mâu thuẫn giữa vô sản và tư sản."
      ],
      "answer": "A. Mâu thuẫn giữa toàn thể nhân dân Việt Nam với đế quốc Pháp."
    },
    {
      "question": "Sự kiện nào dưới đây cho thấy phong trào công nhân Việt Nam đã trở thành một phong trào tự giác:",
      "options": [
        "A. Năm 1920 (tổ chức công hội ở Sài Gòn được thành lập)",
        "B. Năm 1925 (cuộc bãi công Ba Son)",
        "C. Năm 1929 (sự ra đời ba tổ chức cộng sản)",
        "D. Năm 1930 (Đảng Cộng sản Việt Nam ra đời)"
      ],
      "answer": "B. Năm 1925 (cuộc bãi công Ba Son)"
    },
    {
      "question": "Kết luận sau đây của Nguyễn Ái Quốc: “Những lời tuyên bố dân tộc tự quyết của bọn đế quốc chỉ là trò bịp bợm...” được rút ra từ sau sự kiện nào:",
      "options": [
        "A. Cách mạng Tháng 10 - Nga thành công (1917).",
        "B. Gửi đến Hội nghị Vecxay Bản yêu sách đòi quyền dân tộc tự quyết cho nhân dân Việt Nam không được chấp nhận (1919).",
        "C. Đọc “Luận cương về vấn đề dân tộc và thuộc địa” của Lênin (7/1920).",
        "D. Gia nhập Quốc tế III (12/1920)."
      ],
      "answer": "B. Gửi đến Hội nghị Vecxay Bản yêu sách đòi quyền dân tộc tự quyết cho nhân dân Việt Nam không được chấp nhận (1919)."
    },
    {
      "question": "Trong các tổ chức sau, tổ chức nào Nguyễn Ái Quốc không tham gia sáng lập?",
      "options": [
        "A. Hội liên hiệp các dân tộc thuộc địa.",
        "B. Quốc tế cộng sản.",
        "C. Hội liên hiệp các dân tộc bị áp bức ở Á Đông.",
        "D. Đảng cộng sản Pháp."
      ],
      "answer": "B. Quốc tế cộng sản."
    },
    {
      "question": "Tính chất của xã hội Việt Nam dưới chính sách thống trị của thực dân Pháp:",
      "options": [
        "A. Là xã hội thuộc địa.",
        "B. Là xã hội thuộc địa nửa phong kiến.",
        "C. Là xã hội tư bản.",
        "D. Là xã hội nửa phong kiến, nửa thuộc địa."
      ],
      "answer": "B. Là xã hội thuộc địa nửa phong kiến."
    },
    {
      "question": "Năm 1929 ở Việt Nam đã ra đời 3 tổ chức cộng sản gồm:",
      "options": [
        "A. Đông Dương Cộng sản đảng, An Nam Cộng sản đảng, Quốc dân đảng.",
        "B. Đông Dương Cộng sản đảng, An Nam Cộng sản đảng, Hội liên hiệp các dân tộc bị áp bức Á Đông.",
        "C. Đông Dương Cộng sản đảng, An Nam Cộng sản đảng, Đông Dương Cộng sản Liên đoàn.",
        "D. Đông Dương Cộng sản đảng, An Nam Cộng sản đảng, Việt Nam quang phục hội."
      ],
      "answer": "C. Đông Dương Cộng sản đảng, An Nam Cộng sản đảng, Đông Dương Cộng sản Liên đoàn."
    },
    {
      "question": "Tác phẩm Đường cách mệnh là tập hợp những bài giảng của ai?",
      "options": [
        "A. Trần Phú.",
        "B. Nguyễn Ái Quốc.",
        "C. Nguyễn Văn Cừ.",
        "D. Trường Chinh."
      ],
      "answer": "B. Nguyễn Ái Quốc."
    },
    {
      "question": "Trong các sách báo sau đây, tác phẩm nào không phải là của Nguyễn Ái Quốc:",
      "options": [
        "A. Báo Le Paria (Người cùng khổ).",
        "B. Bản án chế độ thực dân Pháp.",
        "C. Tự chỉ trích.",
        "D. Đường cách mệnh."
      ],
      "answer": "C. Tự chỉ trích."
    },
    {
      "question": "Chi bộ cộng sản đầu tiên ở Việt Nam (3/1929) ra đời ở đâu?",
      "options": [
        "A. Quảng Châu",
        "B. Hương Cảng",
        "C. Paris",
        "D. Hà Nội"
      ],
      "answer": "D. Hà Nội"
    },
    {
      "question": "Nguyễn Ái Quốc nói “Dựa vào Nhật để đánh Pháp chẳng khác nào đuổi hổ cửa trước rước beo cửa sau” là câu nói về ai trong các nhân sĩ sau:",
      "options": [
        "A. Phan Bội Châu.",
        "B. Phan Chu Trinh.",
        "C. Nguyễn Thái Học.",
        "D. Bùi Quang Chiêu."
      ],
      "answer": "A. Phan Bội Châu."
    },
    {
      "question": "Nguyễn Ái Quốc nói “Dựa vào Pháp để cải cách đất nước chẳng khác nào ngửa tay xin giặc rủ lòng thương” là câu nói về ai trong các nhân sĩ sau:",
      "options": [
        "A. Phan Bội Châu.",
        "B. Phan Chu Trinh.",
        "C. Trần Trọng Kim.",
        "D. Nguyễn Thái Học."
      ],
      "answer": "B. Phan Chu Trinh."
    },
    {
      "question": "Hội Việt Nam Cách mạng Thanh niên thực hiện chủ trương \"vô sản hoá\" vào thời gian nào:",
      "options": [
        "A. Cuối năm 1926 đầu năm 1927",
        "B. Cuối năm 1927 đầu năm 1928",
        "C. Cuối năm 1928 đầu năm 1929",
        "D. Cuối năm 1929 đầu năm 1930"
      ],
      "answer": "C. Cuối năm 1928 đầu năm 1929"
    },
    {
      "question": "Sự ra đời Đảng Cộng sản Việt Nam là sự kết hợp của các yếu tố:",
      "options": [
        "A. Chủ nghĩa Mác với phong trào công nhân Việt Nam.",
        "B. Chủ nghĩa Mác với phong trào nông dân Việt Nam.",
        "C. Phong trào công nhân VN và phong trào yêu nước Việt Nam.",
        "D. Chủ nghĩa Mác với phong trào công nhân và phong trào yêu nước Việt Nam."
      ],
      "answer": "D. Chủ nghĩa Mác với phong trào công nhân và phong trào yêu nước Việt Nam."
    },
    {
      "question": "Tham dự Hội nghị thành lập Đảng Cộng sản Việt Nam 3/2/1930 bao gồm các đại biểu của các tổ chức:",
      "options": [
        "A. Đại biểu Quốc tế cộng sản + An Nam cộng sản đảng + Đông Dương cộng sản liên đoàn.",
        "B. Đại biểu Quốc tế cộng sản + Đông Dương cộng sản đảng + An Nam cộng sản đảng.",
        "C. Đại biểu Quốc tế cộng sản + Đông Dương cộng sản đảng + Đông Dương cộng sản liên đoàn.",
        "D. Đại biểu Quốc tế cộng sản + An Nam cộng sản đảng + Tân Việt cách mạng đảng."
      ],
      "answer": "B. Đại biểu Quốc tế cộng sản + Đông Dương cộng sản đảng + An Nam cộng sản đảng."
    },
    {
      "question": "Phương hướng chiến lược của cách mạng Việt Nam được thể hiện trong Cương lĩnh đầu tiên do Nguyễn Ái Quốc soạn thảo (2/1930):",
      "options": [
        "A. Tư sản dân quyền cách mạng bỏ qua tư bản tiến thẳng lên chủ nghĩa xã hội.",
        "B. Tư sản dân quyền cách mạng và thổ địa cách mạng để đi tới xã hội cộng sản.",
        "C. Cách mạng dân tộc dân chủ nhân dân tiến lên cách mạng xã hội chủ nghĩa.",
        "D. Cách mạng xã hội chủ nghĩa."
      ],
      "answer": "B. Tư sản dân quyền cách mạng và thổ địa cách mạng để đi tới xã hội cộng sản."
    },
    {
      "question": "Cương lĩnh chính trị đầu tiên của Đảng do Nguyễn Ái Quốc soạn thảo bao gồm các văn kiện nào:",
      "options": [
        "A. Chánh cương vắn tắt, Sách lược vắn tắt, Điều lệ vắn tắt, Chương trình tóm tắt và Lời kêu gọi nhân dịp thành lập Đảng.",
        "B. Chánh cương vắn tắt, Sách lược vắn tắt, Điều lệ vắn tắt, Đường cách mệnh.",
        "C. Chánh cương vắn tắt, Sách lược vắn tắt, Điều lệ vắn tắt, Người cùng khổ.",
        "D. Chánh cương vắn tắt, Sách lược vắn tắt, Điều lệ vắn tắt, Le Paria, Lời kêu gọi nhân dịp thành lập Đảng."
      ],
      "answer": "A. Chánh cương vắn tắt, Sách lược vắn tắt, Điều lệ vắn tắt, Chương trình tóm tắt và Lời kêu gọi nhân dịp thành lập Đảng."
    },
    {
      "question": "Cương lĩnh chính trị đầu tiên đã xác định Đảng Cộng sản Việt Nam là:",
      "options": [
        "A. Đội tiên phong của giai cấp vô sản Việt Nam.",
        "B. Đội tiên phong của Học trò, nhà buôn nhỏ và điền chủ nhỏ.",
        "C. Đội tiên phong của nông dân, trí thức và nhà buôn.",
        "D. Đội tiên phong của dân tộc Việt Nam."
      ],
      "answer": "A. Đội tiên phong của giai cấp vô sản Việt Nam."
    },
    {
      "question": "Tìm ý đúng điền vào chỗ trống: Cương lĩnh đầu tiên của Đảng chủ trương: “... đã ra mặt phản cách mạng thì phải kiên quyết đánh đổ”",
      "options": [
        "A. Giai cấp nào.",
        "B. Dân tộc nào.",
        "C. Bộ phận nào.",
        "D. Lực lượng nào."
      ],
      "answer": "C. Bộ phận nào."
    },
    {
      "question": "Hội nghị thành lập Đảng (tháng 1/1930) đã lấy tên Đảng là:",
      "options": [
        "A. Đảng lao động Việt Nam",
        "B. Đảng Cộng sản Đông Dương",
        "C. Đảng Cộng sản Việt Nam",
        "D. Đảng Xã hội Việt Nam"
      ],
      "answer": "C. Đảng Cộng sản Việt Nam"
    },
    {
      "question": "Văn kiện nào đã nhấn mạnh: “Vấn đề thổ địa là cốt lõi của cách mạng tư sản dân quyền”?",
      "options": [
        "A. Luận cương chính trị",
        "B. Cương lĩnh tháng 2",
        "C. Chính cương vắn tắt",
        "D. Sách lược vắn tắt"
      ],
      "answer": "A. Luận cương chính trị"
    },
    {
      "question": "Hội nghị Ban chấp hành Trung ương Đảng lần thứ nhất (10/1930), lấy tên Đảng và bầu Tổng Bí thư là:",
      "options": [
        "A. Đảng Lao động Đông Dương/Nguyễn Ái Quốc là Tổng Bí thư",
        "B. Đảng Lao động Việt Nam/Lê Hồng Phong là Tổng Bí thư",
        "C. Đảng Cộng sản Việt Nam/Hà Huy Tập là Tổng Bí thư",
        "D. Đảng Cộng sản Đông Dương/Trần Phú là Tổng Bí thư"
      ],
      "answer": "D. Đảng Cộng sản Đông Dương/ Trần Phú là Tổng Bí thư"
    },
    {
      "question": "Luận cương chính trị, tháng 10-1930 xác định mâu thuẫn chủ yếu ở Đông Dương là:",
      "options": [
        "A. Các dân tộc Đông Dương với đế quốc Pháp và Phong kiến, địa chủ, tay sai đế quốc",
        "B. Nhân dân Đông Dương chủ yếu là dân cày với địa chủ phong kiến và chủ nghĩa đế quốc",
        "C. Thợ thuyền, dân cày và các phần tử lao khổ với địa chủ, phong kiến, và tư bản đế quốc",
        "D. Công nhân, nông dân, trí thức Đông Dương với đế quốc Pháp và tay sai, phản động"
      ],
      "answer": "C. Thợ thuyền, dân cày và các phần tử lao khổ với địa chủ, phong kiến, và tư bản đế quốc"
    },
    {
      "question": "Luận cương chính trị tháng 10-1930 xác định \"cái cốt của cách mạng tư sản dân quyền” là:",
      "options": [
        "A. Vấn đề dân tộc.",
        "B. Vấn đề thổ địa.",
        "C. Vấn đề giành chính quyền.",
        "D. Vấn đề dân chủ."
      ],
      "answer": "B. Vấn đề thổ địa."
    },
    {
      "question": "Về lực lượng cách mạng, Luận cương Chính trị tháng 10 -1930 xác định:",
      "options": [
        "A. Công nhân, tiểu tư sản, tư sản dân tộc",
        "B. Nông dân, tiểu tư sản",
        "C. Công nhân, nông dân, tiểu tư sản",
        "D. Công nhân, nông dân"
      ],
      "answer": "D. Công nhân, nông dân"
    },
    {
      "question": "Bộ câu hỏi trắc nghiệm môn Lịch sử Đảng Cộng sản Việt Nam. Môn học Lịch sử Đảng Cộng sản Việt Nam nghiên cứu có hệ thống các sự kiện lịch sử Đảng để giúp sinh viên:",
      "options": [
        "A. Hiểu rõ nội dung của các sự kiện đó gắn liền với sự lãnh đạo của Đảng.",
        "B. Hiểu rõ tính chất của các sự kiện đó gắn liền với sự lãnh đạo của Đảng.",
        "C. Hiểu rõ bản chất của các sự kiện đó gắn liền với sự lãnh đạo của Đảng.",
        "D. Tất cả đều đúng."
      ],
      "answer": "D. Tất cả đều đúng."
    },
    {
      "question": "Trong đợt khai thác thuộc địa lần thứ nhất của thực dân Pháp (1897 — 1914) ở nước ta đã hình thành giai cấp mới nào:",
      "options": [
        "A. Giai cấp tư sản.",
        "B. Giai cấp tư sản và công nhân.",
        "C. Giai cấp công nhân.",
        "D. Giai cấp tiểu tư sản."
      ],
      "answer": "C. Giai cấp công nhân."
    },
    {
      "question": "Mâu thuẫn chủ yếu nhất trong xã hội Việt Nam dưới ách thống trị của thực dân Pháp là:",
      "options": [
        "A. Mâu thuẫn giữa toàn thể nhân dân Việt Nam với đế quốc Pháp.",
        "B. Mâu thuẫn giữa nông dân với giai cấp địa chủ phong kiến.",
        "C. Mâu thuẫn giữa vô sản và tư sản."
      ],
      "answer": "A. Mâu thuẫn giữa toàn thể nhân dân Việt Nam với đế quốc Pháp."
    },
    {
      "question": "Nhiệm vụ học tập môn Lịch sử Đảng Cộng sản Việt Nam là:",
      "options": [
        "A. Để nhận thức đầy đủ, có hệ thống những tri thức lịch sử lãnh đạo, đấu tranh và cầm quyền của Đảng.",
        "B. Để giáo dục sâu sắc tinh thần yêu nước, ý thức, niềm tự hào, tự tôn, ý chí tự lực, tự cường dân tộc.",
        "C. Để hiểu rõ hiện tại và dự báo tương lai sự phát triển của Đảng và Dân tộc Việt Nam.",
        "D. Tất cả đều đúng."
      ],
      "answer": "D. Tất cả đều đúng."
    },
    {
      "question": "Sự kiện nào dưới đây cho thấy phong trào công nhân Việt Nam đã trở thành một phong trào tự giác:",
      "options": [
        "A. Năm 1920 (tổ chức công hội ở Sài Gòn được thành lập).",
        "B. Năm 1925 (cuộc bãi công Ba Son).",
        "C. Năm 1929 (sự ra đời ba tổ chức cộng sản).",
        "D. Năm 1930 (Đảng Cộng sản Việt Nam ra đời)."
      ],
      "answer": "B. Năm 1925 (cuộc bãi công Ba Son)."
    },
    {
      "question": "Trong các tổ chức sau, tổ chức nào Nguyễn Ái Quốc không tham gia sáng lập:",
      "options": [
        "A. Hội liên hiệp các dân tộc thuộc địa.",
        "B. Quốc tế cộng sản.",
        "C. Hội liên hiệp các dân tộc bị áp bức ở Á Đông.",
        "D. Đảng Cộng sản Pháp."
      ],
      "answer": "B. Quốc tế cộng sản."
    },
    {
      "question": "Tính chất của xã hội Việt Nam dưới chính sách thống trị của thực dân Pháp:",
      "options": [
        "A. Là xã hội thuộc địa.",
        "B. Là xã hội thuộc địa nửa phong kiến.",
        "C. Là xã hội tư bản.",
        "D. Là xã hội nửa phong kiến, nửa thuộc địa."
      ],
      "answer": "B. Là xã hội thuộc địa nửa phong kiến."
    },
    {
      "question": "Hội Việt Nam Cách mạng Thanh niên thực hiện chủ trương \"vô sản hoá\" vào thời gian nào:",
      "options": [
        "A. Cuối năm 1926 đầu năm 1927.",
        "B. Cuối năm 1927 đầu năm 1928.",
        "C. Cuối năm 1928 đầu năm 1929.",
        "D. Cuối năm 1929 đầu năm 1930."
      ],
      "answer": "C. Cuối năm 1928 đầu năm 1929."
    },
    {
      "question": "Phương hướng chiến lược của cách mạng Việt Nam được thể hiện trong Cương lĩnh đầu tiên do Nguyễn Ái Quốc soạn thảo (2/1930) là thực hiện:",
      "options": [
        "A. Tư sản dân quyền cách mạng bỏ qua tư bản tiến thẳng lên chủ nghĩa xã hội.",
        "B. Tư sản dân quyền cách mạng và thổ địa cách mạng để đi tới xã hội cộng sản.",
        "C. Cách mạng dân tộc dân chủ nhân dân tiến lên cách mạng xã hội chủ nghĩa.",
        "D. Cách mạng xã hội chủ nghĩa."
      ],
      "answer": "B. Tư sản dân quyền cách mạng và thổ địa cách mạng để đi tới xã hội cộng sản."
    },
    {
      "question": "Hội nghị Trung ương của Đảng mở đầu cho chủ trương chuyển hướng chỉ đạo chiến lược giai đoạn năm 1939 - 1945 là:",
      "options": [
        "A. Hội nghị Trung ương lần thứ 6 - tháng 11/1939",
        "B. Hội nghị Trung ương lần thứ 7 - tháng 11/1940",
        "C. Hội nghị Trung ương lần thứ 8 - tháng 5/1941",
        "D. Hội nghị Trung ương lần thứ 9 - tháng 8/1945"
      ],
      "answer": "A. Hội nghị Trung ương lần thứ 6 - tháng 11/1939"
    },
    {
      "question": "Tìm ý đúng điền vào chỗ trống: Cương lĩnh đầu tiên của Đảng chủ trương: \"... đã ra mặt phản cách mạng thì phải kiên quyết đánh đổ”",
      "options": [
        "A. Giai cấp nào.",
        "B. Dân tộc nào.",
        "C. Bộ phận nào.",
        "D. Lực lượng nào."
      ],
      "answer": "C. Bộ phận nào."
    },
    {
      "question": "Cương lĩnh chính trị đầu tiên đã xác định Đảng Cộng sản Việt Nam là:",
      "options": [
        "A. Đội tiên phong của giai cấp công nhân (vô sản) Việt Nam",
        "B. Đội tiên phong của Học trò, nhà buôn nhỏ và điền chủ nhỏ",
        "C. Đội tiên phong của nông dân, trí thức và nhà buôn",
        "D. Đội tiên phong của giai cấp công nhân (vô sản) Việt Nam đồng thời là đội tiên phong của nhân dân lao động và của dân tộc Việt Nam."
      ],
      "answer": "A. Đội tiên phong của giai cấp công nhân (vô sản) Việt Nam"
    },
    {
      "question": "Hội nghị đánh dấu hoàn thiện chuyển hướng chỉ đạo chiến lược giai đoạn 1939-1945 là:",
      "options": [
        "A. Hội nghị trung ương 6, khóa I",
        "B. Hội nghị trung ương 7, khóa I",
        "C. Hội nghị trung ương 8, khóa I",
        "D. Hội nghị trung ương 9, khóa I"
      ],
      "answer": "C. Hội nghị trung ương 8, khóa I"
    },
    {
      "question": "Ngày Quốc tế lao động (1/5) được tổ chức kỷ niệm lần đầu tiên ở Việt Nam vào thời gian nào:",
      "options": [
        "A. Năm 1930",
        "B. Năm 1935",
        "C. Năm 1936",
        "D. Năm 1945"
      ],
      "answer": "A. Năm 1930"
    },
    {
      "question": "Khẩu hiệu “Đấu tranh chống chế độ phản động thuộc địa, chống phát xít, chống chiến tranh, đòi tự do dân chủ, cơm áo và hòa bình” được nêu ra tại Hội nghị nào của Đảng:",
      "options": [
        "A. Hội nghị Ban chấp hành TW5 tháng 7/1936",
        "B. Hội nghị Ban chấp hành TW6 tháng 11/1939",
        "C. Hội nghị Ban chấp hành TW7 tháng 11/1940",
        "D. Hội nghị Ban chấp hành TW8 tháng 5/1941"
      ],
      "answer": "A. Hội nghị Ban chấp hành TW5 tháng 7/1936"
    },
    {
      "question": "Câu nói “Dù phải đốt cháy cả dãy Trường Sơn cũng phải giành cho được độc lập” của Hồ Chí Minh được nói vào thời gian:",
      "options": [
        "A. Tháng 8/1945.",
        "B. Tháng 8/1944.",
        "C. Tháng 8/1941.",
        "D. Tháng 9/1945."
      ],
      "answer": "A. Tháng 8/1945."
    },
    {
      "question": "Đảng ta chớp thời cơ quyết định Tổng khởi nghĩa giành chính quyền (8/1945) khi:",
      "options": [
        "A. Quân Đồng minh kéo vào Đông Dương.",
        "B. Cách mạng Nhật bùng nổ giành thắng lợi.",
        "C. Ngay sau khi phát xít Nhật tuyên bố đầu hàng và trước khi quân Đồng minh nhảy vào Đông Dương.",
        "D. Nhật đảo chính Pháp."
      ],
      "answer": "C. Ngay sau khi phát xít Nhật tuyên bố đầu hàng và trước khi quân Đồng minh nhảy vào Đông Dương."
    },
    {
      "question": "Nội dung nào dưới đây không đúng với ý nghĩa lịch sử của Cách mạng Tháng 8/1945:",
      "options": [
        "A. Đập tan xiềng xích nô lệ của thực dân trong gần một thế kỷ.",
        "B. Lập nên nước Việt Nam dân chủ cộng hòa.",
        "C. Nhân dân Việt Nam từ thân phận nô lệ trở thành người chủ đất nước.",
        "D. Làm sụp đổ hoàn toàn chủ nghĩa thực dân kiểu cũ."
      ],
      "answer": "D. Làm sụp đổ hoàn toàn chủ nghĩa thực dân kiểu cũ."
    }
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_idx = 33
for i in range(len(clean_questions)):
    data['questions'][start_idx + i] = clean_questions[i]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully cleaned questions {start_idx} to {start_idx + len(clean_questions) - 1}!")
