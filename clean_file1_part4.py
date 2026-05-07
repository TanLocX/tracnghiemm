import json

clean_questions = [
    # 119
    {
        "question": "Các tờ báo Giải phóng, Cờ giải phóng, Chặt xiềng, Cứu quốc, Việt Nam độc lập, Bãi Sậy, Đuổi giặc nước, Tiền phong, Kèn gọi lính, Quân giải phóng, Kháng địch, Độc lập là cơ quan ngôn luận của:",
        "options": [
            "A. Là cơ quan ngôn luận của Đảng Cộng sản Đông Dương.",
            "B. Là cơ quan ngôn luận của Mặt trận Việt Minh.",
            "C. Là cơ quan ngôn luận của Đảng Cộng sản Đông Dương và Mặt trận Việt Minh.",
            "D. Là cơ quan ngôn luận của Mặt trận Việt Minh và Mặt trận dân tộc thống nhất phản đế Đông Dương."
        ],
        "answer": "C. Là cơ quan ngôn luận của Đảng Cộng sản Đông Dương và Mặt trận Việt Minh."
    },
    # 120
    {
        "question": "Chọn đáp án đúng:",
        "options": [
            "A. Việt Minh là mặt trận đại đoàn kết dân tộc Việt Nam, là nơi tập hợp, giác ngộ và rèn luyện lực lượng chính trị rộng lớn, một lực lượng cơ bản và có ý nghĩa quyết định trong tổng khởi nghĩa giành chính quyền.",
            "B. Việt Minh là mặt trận đại đoàn kết dân tộc Việt Nam, là nơi tập hợp, giác ngộ và rèn luyện lực lượng chính trị rộng lớn, một lực lượng cơ bản và có ý nghĩa quan trọng cho thắng lợi của tổng khởi nghĩa giành chính quyền.",
            "C. Việt Minh là mặt trận đại đoàn kết 3 dân tộc Việt Nam, Lào, Campuchia, là nơi tập hợp, giác ngộ và rèn luyện lực lượng chính trị rộng lớn, một lực lượng cơ bản và có ý nghĩa quyết định cho việc giành độc lập của 3 nước Đông Dương.",
            "D. Tất cả đều đúng."
        ],
        "answer": "A. Việt Minh là mặt trận đại đoàn kết dân tộc Việt Nam, là nơi tập hợp, giác ngộ và rèn luyện lực lượng chính trị rộng lớn, một lực lượng cơ bản và có ý nghĩa quyết định trong tổng khởi nghĩa giành chính quyền."
    },
    # 121
    {
        "question": "Trong Cách mạng tháng Tám (1945), Đảng đã nêu rõ lúc này toàn Đảng, toàn dân cần phải \"tập trung, thống nhất và kịp thời\". Đó là:",
        "options": [
            "A. Là phương hướng hành động của Đảng trong tổng khởi nghĩa tháng Tám (1945).",
            "B. Là khẩu hiệu đấu tranh của Đảng trong Tổng khởi nghĩa tháng Tám (1945).",
            "C. Là nguyên tắc chỉ đạo của Đảng trong Tổng khởi nghĩa tháng Tám (1945).",
            "D. Là chủ trương của Đảng trong Tổng khởi nghĩa tháng Tám (1945)."
        ],
        "answer": "C. Là nguyên tắc chỉ đạo của Đảng trong Tổng khởi nghĩa tháng Tám (1945)."
    },
    # 122
    {
        "question": "Phương hướng hành động của Đảng trong Tổng khởi nghĩa tháng Tám (1945) là:",
        "options": [
            "A. Phải đánh chiếm ngay những nơi chắc thắng, không kể thành phố hay nông thôn; quân sự và chính trị phải phối hợp.",
            "B. Phải làm tan rã tinh thần quân địch và dụ chúng hàng trước khi đánh.",
            "C. Phải chộp lấy những căn cứ chính (kể cả ở các đô thị) trước khi quân Đồng minh vào; thành lập ủy ban nhân dân ở những nơi đã giành được quyền làm chủ.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 123
    {
        "question": "Chọn đáp án đúng khi nói về vai trò của cuộc khởi nghĩa thắng lợi ở Hà Nội:",
        "options": [
            "A. Thắng lợi của cuộc khởi nghĩa ở Hà Nội ảnh hưởng nhanh chóng đến nhiều tỉnh và thành phố khác, cổ vũ mạnh mẽ phong trào cả nước, tạo điều kiện thuận lợi lớn cho quá trình tổng khởi nghĩa thắng lợi.",
            "B. Thắng lợi của cuộc khởi nghĩa ở Hà Nội có vai trò quan trọng, cổ vũ mạnh mẽ phong trào cả nước, tạo điều kiện thuận lợi lớn cho quá trình tổng khởi nghĩa thắng lợi.",
            "C. Thắng lợi của cuộc khởi nghĩa ở Hà Nội có vai trò quyết định, cổ vũ mạnh mẽ phong trào cả nước, tạo điều kiện thuận lợi lớn cho quá trình tổng khởi nghĩa thắng lợi.",
            "D. Thắng lợi của cuộc khởi nghĩa ở Hà Nội ảnh hưởng nhanh chóng đến Huế, Sài Gòn, tạo điều kiện thuận lợi lớn cho quá trình tổng khởi nghĩa thắng lợi."
        ],
        "answer": "A. Thắng lợi của cuộc khởi nghĩa ở Hà Nội ảnh hưởng nhanh chóng đến nhiều tỉnh và thành phố khác, cổ vũ mạnh mẽ phong trào cả nước, tạo điều kiện thuận lợi lớn cho quá trình tổng khởi nghĩa thắng lợi."
    },
    # 124
    {
        "question": "Chọn đáp án đúng:",
        "options": [
            "A. Những cuộc khởi nghĩa ở Hà Nội, Huế, Sài Gòn và các đô thị đập tan các cơ quan đầu não của kẻ thù có ý nghĩa lớn, cổ vũ mạnh mẽ phong trào cả nước, tạo điều kiện thuận lợi lớn cho quá trình tổng khởi nghĩa thắng lợi.",
            "B. Những cuộc khởi nghĩa ở Hà Nội, Huế, Sài Gòn và các cơ quan đầu não của kẻ thù ở đây có ý nghĩa quyết định thắng lợi trong cả nước.",
            "C. Những cuộc khởi nghĩa ở Hà Nội, Huế, Sài Gòn và các đô thị đập tan các cơ quan đầu não của kẻ thù có ý nghĩa quyết định thắng lợi trong cả nước.",
            "D. Những cuộc khởi nghĩa ở Hà Nội, Huế, Sài Gòn và các đô thị đập tan các cơ quan đầu não của kẻ thù có ý nghĩa quan trọng, thúc đẩy nhanh chóng cho thắng lợi trong cả nước."
        ],
        "answer": "C. Những cuộc khởi nghĩa ở Hà Nội, Huế, Sài Gòn và các đô thị đập tan các cơ quan đầu não của kẻ thù có ý nghĩa quyết định thắng lợi trong cả nước."
    },
    # 125
    {
        "question": "Cách mạng tháng Tám năm 1945 có tính chất là một cuộc cách mạng giải phóng dân tộc điển hình vì:",
        "options": [
            "A. Cách mạng tháng Tám đã tập trung hoàn thành nhiệm vụ hàng đầu của cách mạng là giải phóng dân tộc. Mục đích của nó là làm cho dân tộc Việt Nam thoát khỏi ách đế quốc, làm cho nước Việt Nam thành một nước độc lập tự do.",
            "B. Cách mạng tháng Tám đã thành lập chính quyền nhà nước \"của chung toàn dân tộc\".",
            "C. Cách mạng tháng Tám là sự vùng dậy của lực lượng toàn dân tộc, đoàn kết chặt chẽ trong mặt trận Việt Minh với những tổ chức quần chúng mang tên \"cứu quốc\".",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 126
    {
        "question": "Cách mạng tháng Tám năm 1945 là \"một cuộc cách mạng giải phóng dân tộc mang tính chất dân chủ mới\" vì:",
        "options": [
            "A. Thắng lợi của Cách mạng tháng Tám đã giải phóng dân tộc Việt Nam. Cuộc cách mạng này là một bộ phận của phe dân chủ chống phát xít.",
            "B. Cuộc cách mạng tháng Tám đã giải quyết một số quyền lợi cho nông dân, lực lượng đông đảo nhất trong dân tộc.",
            "C. Cuộc cách mạng tháng Tám thành công đã đưa đến việc xây dựng chính quyền nhà nước dân chủ nhân dân đầu tiên ở Việt Nam, xóa bỏ chế độ quân chủ phong kiến. Các tầng lớp nhân dân được hưởng quyền tự do, dân chủ.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 127
    {
        "question": "\"Cách mạng tháng Tám Việt Nam là một cuộc cách mạng giải phóng dân tộc. Mục đích của nó là làm cho dân tộc Việt Nam thoát khỏi ách đế quốc, làm cho nước Việt Nam thành một nước độc lập tự do\". Đây là nhận định của Tổng Bí thư Trường Chinh đề nhấn mạnh:",
        "options": [
            "A. Tính chất của cuộc Cách mạng tháng Tám năm 1945.",
            "B. Ý nghĩa to lớn đối với phong trào cách mạng thế giới của cuộc Cách mạng tháng Tám năm 1945.",
            "C. Ý nghĩa to lớn đối với dân tộc Việt Nam của cuộc Cách mạng tháng Tám năm 1945.",
            "D. Bài học kinh nghiệm của cuộc Cách mạng tháng Tám năm 1945."
        ],
        "answer": "A. Tính chất của cuộc Cách mạng tháng Tám năm 1945."
    },
    # 128
    {
        "question": "Chỉ ra đáp án sai khi nói về nhiệm vụ chủ yếu trước mắt được Đảng đề ra ngay sau khi Cách mạng tháng Tám thành công:",
        "options": [
            "A. Diệt giặc đói, diệt giặc dốt và diệt giặc ngoại xâm.",
            "B. Củng cố chính quyền, chống thực dân Pháp xâm lược, bài trừ nội phản, cải thiện đời sống cho nhân dân.",
            "C. Cuộc cách mạng Đông Dương lúc này vẫn là \"dân tộc giải phóng\"; \"Dân tộc trên hết, Tổ quốc trên hết\".",
            "D. Tất cả đều đúng."
        ],
        "answer": "C. Cuộc cách mạng Đông Dương lúc này vẫn là \"dân tộc giải phóng\"; \"Dân tộc trên hết, Tổ quốc trên hết\"."
    },
    # 129
    {
        "question": "Đâu là nội dung về biện pháp trong Chỉ thị \"Kháng chiến - kiến quốc\" của Ban Chấp hành Trung ương Đảng ra ngày 25/11/1945:",
        "options": [
            "A. Cuộc cách mạng Đông Dương lúc này vẫn là \"dân tộc giải phóng\".",
            "B. Củng cố chính quyền, chống thực dân Pháp xâm lược, bài trừ nội phản, cải thiện đời sống cho nhân dân.",
            "C. Nhanh chóng xúc tiến bầu cử Quốc hội để đi đến thành lập Chính phủ chính thức, lập ra Hiến pháp, động viên lực lượng toàn dân, kiên trì kháng chiến và chuẩn bị kháng chiến lâu dài.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 130
    {
        "question": "Chọn nội dung đúng khi nói về ý nghĩa của những chủ trương, biện pháp, sách lược và đối sách đúng đắn của Đảng, Chính phủ và Chủ tịch Hồ Chí Minh trong tình cảnh \"ngàn cân treo sợi tóc\" của dân tộc (1945 - 1946):",
        "options": [
            "A. Đã ngăn chặn bước tiến của đội quân xâm lược Pháp ở Nam bộ, vạch trần và làm thất bại mọi âm mưu, hoạt động chống phá của các kẻ thù.",
            "B. Đã củng cố, giữ vững và bảo vệ bộ máy chính quyền cách mạng từ Trung ương đến cơ sở và những thành quả của cuộc Cách mạng tháng Tám.",
            "C. Đã tạo thêm thời gian hòa bình, hòa hoãn, tranh thủ xây dựng thực lực, chuẩn bị sẵn sàng cho cuộc kháng chiến lâu dài.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 131
    {
        "question": "Chính cương của Đảng Lao động Việt Nam đã xác định tính chất của xã hội Việt Nam lúc này là:",
        "options": [
            "A. Xã hội Việt Nam lúc này có tính chất dân chủ nhân dân và một phần phong kiến.",
            "B. Xã hội Việt Nam lúc này có tính chất dân chủ nhân dân và một phần thuộc địa nửa phong kiến.",
            "C. Xã hội Việt Nam lúc này có tính chất dân chủ nhân dân, một phần thuộc địa và nửa phong kiến.",
            "D. Xã hội Việt Nam lúc này có tính chất dân chủ nhân dân, một phần xã hội chủ nghĩa và nửa phong kiến."
        ],
        "answer": "C. Xã hội Việt Nam lúc này có tính chất dân chủ nhân dân, một phần thuộc địa và nửa phong kiến."
    },
    # 132
    {
        "question": "Chính cương của Đảng Lao động Việt Nam (1951) đã xác định nhiệm vụ của cách mạng Việt Nam lúc này là:",
        "options": [
            "A. Đánh đuổi bọn đế quốc xâm lược, giành độc lập và thống nhất thật sự cho dân tộc.",
            "B. Xóa bỏ những tàn tích phong kiến và nửa phong kiến, làm cho người cày có ruộng.",
            "C. Phát triển chế độ dân chủ nhân dân, gây cơ sở cho chủ nghĩa xã hội.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 133
    {
        "question": "Đâu không phải là nhiệm vụ của cách mạng Việt Nam được nêu trong Chính cương của Đảng Lao động Việt Nam (1951):",
        "options": [
            "A. Cách mạng Việt Nam đánh đuổi bọn đế quốc xâm lược, giành độc lập và thống nhất thật sự cho dân tộc.",
            "B. Cách mạng Việt Nam xóa bỏ những tàn tích phong kiến và nửa phong kiến, làm cho người cày có ruộng.",
            "C. Cách mạng Việt Nam phát triển chế độ dân chủ nhân dân, gây cơ sở cho chủ nghĩa xã hội.",
            "D. Cách mạng Việt Nam là cuộc cách mạng dân tộc, dân chủ nhân dân do Đảng của giai cấp công nhân lãnh đạo nên nhất định sẽ tiến lên chủ nghĩa xã hội. Đây là quá trình lâu dài, có các giai đoạn phát triển tương ứng."
        ],
        "answer": "D. Cách mạng Việt Nam là cuộc cách mạng dân tộc, dân chủ nhân dân do Đảng của giai cấp công nhân lãnh đạo nên nhất định sẽ tiến lên chủ nghĩa xã hội. Đây là quá trình lâu dài, có các giai đoạn phát triển tương ứng."
    },
    # 134
    {
        "question": "Chiến thắng nào được Đảng đánh giá là \"thiên sử vàng của dân tộc Việt Nam\", được ghi nhận là một chiến công vĩ đại của dân tộc Việt Nam trong thế kỷ XX và \"đi vào lịch sử thế giới như một chiến công hiển hách, báo hiệu sự thắng lợi của nhân dân các dân tộc bị áp bức, sự sụp đổ của chủ nghĩa thực dân\":",
        "options": [
            "A. Chiến thắng của Chiến dịch Điện Biên Phủ.",
            "B. Chiến thắng của cuộc kháng chiến chống Pháp.",
            "C. Chiến thắng của Chiến dịch Hồ Chí Minh.",
            "D. Chiến thắng của cuộc kháng chiến chống Mỹ."
        ],
        "answer": "A. Chiến thắng của Chiến dịch Điện Biên Phủ."
    },
    # 135
    {
        "question": "Đối với vùng rừng núi: Lấy đấu tranh vũ trang là chủ yếu; đối với vùng nông thôn đồng bằng: Kết hợp hai hình thức đấu tranh vũ trang và chính trị; đối với vùng đô thị: Lấy đấu tranh chính trị là chủ yếu. Đây là phương châm đấu tranh của Bộ Chính trị khóa II để lãnh đạo, chỉ đạo toàn dân nhằm:",
        "options": [
            "A. Chống lại Chiến lược Chiến tranh Đơn phương của Mỹ.",
            "B. Chống lại Chiến lược Chiến tranh đặc biệt của Mỹ.",
            "C. Chống lại Chiến lược Chiến tranh cục bộ của Mỹ.",
            "D. Chống lại Chiến lược Việt Nam hóa chiến tranh của Mỹ."
        ],
        "answer": "B. Chống lại Chiến lược Chiến tranh đặc biệt của Mỹ."
    },
    # 136
    {
        "question": "Đâu là nội dung về phương châm chiến lược được đề ra tại Hội nghị lần thứ 11 (3-1965) và Hội nghị lần thứ 12 (12-1965) của Ban Chấp hành Trung ương Đảng để chiến đấu và chiến thắng đế quốc Mỹ xâm lược:",
        "options": [
            "A. Kiên quyết đánh bại cuộc chiến tranh xâm lược của đế quốc Mỹ trong bất kỳ tình huống nào, nhằm bảo vệ miền Bắc, giải phóng miền Nam, hoàn thành cách mạng dân tộc dân chủ nhân dân trong cả nước, tiến tới thực hiện hòa bình thống nhất nước nhà.",
            "B. Giữ vững và phát triển thế tiến công, kiên quyết tiến công và liên tục tiến công. Chuyển hướng xây dựng kinh tế, bảo đảm tiếp tục xây dựng miền Bắc vững mạnh về kinh tế và quốc phòng trong điều kiện có chiến tranh, tiến hành cuộc chiến tranh nhân dân chống chiến tranh phá hoại của đế quốc Mỹ.",
            "C. Phát động cuộc kháng chiến chống Mỹ, cứu nước trong toàn quốc, coi chống Mỹ, cứu nước là nhiệm vụ thiêng liêng của cả dân tộc từ Nam chí Bắc.",
            "D. Đánh lâu dài, dựa vào sức mình là chính, càng đánh càng mạnh; cần phải cố gắng đến mức độ cao, tập trung lực lượng của cả hai miền để mở những cuộc tiến công lớn, tranh thủ thời cơ giành thắng lợi quyết định trong thời gian tương đối ngắn trên chiến trường miền Nam."
        ],
        "answer": "D. Đánh lâu dài, dựa vào sức mình là chính, càng đánh càng mạnh; cần phải cố gắng đến mức độ cao, tập trung lực lượng của cả hai miền để mở những cuộc tiến công lớn, tranh thủ thời cơ giành thắng lợi quyết định trong thời gian tương đối ngắn trên chiến trường miền Nam."
    },
    # 137
    {
        "question": "Chiến thắng nào của quân dân Việt Nam sau đây đã \"đánh bại được ý chí xâm lược của Mỹ, tạo nên bước ngoặt quyết định của chiến tranh\":",
        "options": [
            "A. Chiến thắng của Chiến dịch Đường 9 - Nam Lào.",
            "B. Chiến thắng của Tổng tiến công và nổi dậy Tết Mậu Thân 1968.",
            "C. Chiến thắng của trận \"Điện Biên phủ trên không\".",
            "D. Chiến thắng của Tổng tiến công và nổi dậy mùa xuân năm 1975."
        ],
        "answer": "B. Chiến thắng của Tổng tiến công và nổi dậy Tết Mậu Thân 1968."
    },
    # 138
    {
        "question": "Ai là người giữ chức Tổng Bí thư Ban chấp hành Trung ương Đảng Cộng sản Việt Nam giai đoạn (2011 - 2021):",
        "options": [
            "A. Đỗ Mười.",
            "B. Lê Khả Phiêu.",
            "C. Nông Đức Mạnh.",
            "D. Nguyễn Phú Trọng."
        ],
        "answer": "D. Nguyễn Phú Trọng."
    },
    # 139
    {
        "question": "Việt Nam và Hoa Kỳ đã tuyên bố bình thường hóa quan hệ đối ngoại vào thời gian nào:",
        "options": [
            "A. Ngày 11/7/1994.",
            "B. Ngày 11/7/1995.",
            "C. Ngày 11/9/2001.",
            "D. Ngày 11/7/2000."
        ],
        "answer": "B. Ngày 11/7/1995."
    },
    # 140
    {
        "question": "Việt Nam và Trung Quốc hiện nay duy trì quan hệ trên tinh thần \"4 tốt\" gồm:",
        "options": [
            "A. Hợp tác tốt, bạn bè tốt, đồng chí tốt, đối tác tốt và bền vững.",
            "B. Láng giềng tốt, bạn bè tốt, đồng chí tốt, đối tác tốt.",
            "C. Khách hàng tốt, bạn bè tốt, đồng đội tốt, đối tác tốt.",
            "D. Cùng là thành viên tốt, bạn bè tốt, đồng chí tốt, đối phương tốt."
        ],
        "answer": "B. Láng giềng tốt, bạn bè tốt, đồng chí tốt, đối tác tốt."
    },
    # 141
    {
        "question": "Đâu là nội dung trong đường lối phát triển nền văn hóa mới của Việt Nam hiện nay:",
        "options": [
            "A. Xây dựng nền văn hóa tiên tiến, đậm đà bản sắc dân tộc, phát triển toàn diện, thống nhất trong đa dạng, thấm nhuần sâu sắc tinh thần nhân văn, dân chủ, tiến bộ, trở thành nền tảng tinh thần vững chắc.",
            "B. Kế thừa và phát huy những truyền thống văn hóa tốt đẹp của cộng đồng các dân tộc Việt Nam.",
            "C. Tiếp thu những tinh hoa văn hóa nhân loại, xây dựng một xã hội dân chủ, công bằng, văn minh, vì lợi ích chân chính và phẩm giá con người, với trình độ tri thức, đạo đức, thể lực và thẩm mỹ ngày càng cao.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 142
    {
        "question": "Trong nền kinh tế thị trường định hướng xã hội chủ nghĩa của Việt Nam hiện nay đang tồn tại các thành phần kinh tế nào:",
        "options": [
            "A. Kinh tế nhà nước.",
            "B. Kinh tế tập thể và kinh tế tư nhân.",
            "C. Kinh tế có vốn đầu tư nước ngoài.",
            "D. Tất cả đều đúng."
        ],
        "answer": "D. Tất cả đều đúng."
    },
    # 143
    {
        "question": "Nền kinh tế Việt Nam hiện nay là nền kinh tế:",
        "options": [
            "A. Nền kinh tế thị trường cạnh tranh tự do.",
            "B. Nền kinh tế thị trường tư bản chủ nghĩa.",
            "C. Nền kinh tế thị trường định hướng xã hội chủ nghĩa.",
            "D. Nền kinh tế thị trường xã hội chủ nghĩa."
        ],
        "answer": "C. Nền kinh tế thị trường định hướng xã hội chủ nghĩa."
    },
    # 144
    {
        "question": "Đại hội đại biểu toàn quốc lần thứ mấy của Đảng Cộng sản Việt Nam đã xác định: \"Ưu tiên phát triển công nghiệp nặng một cách hợp lý trên cơ sở phát triển nông nghiệp và công nghiệp nhẹ, kết hợp xây dựng công nghiệp và nông nghiệp thành một cơ cấu kinh tế công - nông nghiệp\":",
        "options": [
            "A. Đại hội lần thứ III (9/1960).",
            "B. Đại hội lần thứ IV (12/1976).",
            "C. Đại hội lần thứ II (02/1951).",
            "D. Đại hội lần thứ I (03/1935)."
        ],
        "answer": "A. Đại hội lần thứ III (9/1960)."
    },
    # 145
    {
        "question": "Tại Đại hội đại biểu toàn quốc nào Đảng Cộng sản Việt Nam đã chủ trương \"tập trung sức phát triển nông nghiệp coi nông nghiệp là mặt trận hàng đầu\":",
        "options": [
            "A. Đại hội lần thứ III (9/1960).",
            "B. Đại hội lần thứ II (02/1951).",
            "C. Đại hội lần thứ V (3/1982).",
            "D. Đại hội lần thứ I (03/1935)."
        ],
        "answer": "C. Đại hội lần thứ V (3/1982)."
    },
    # 146
    {
        "question": "Quan điểm \"Mở rộng, đa dạng hoá, đa phương hoá các quan hệ đối ngoại\" được Đảng Cộng sản Việt Nam đề ra tại Đại hội đại biểu toàn quốc lần thứ mấy:",
        "options": [
            "A. Đại hội VI (tháng 12/1986).",
            "B. Đại hội VII (tháng 6/1991).",
            "C. Đại hội VIII (tháng 6/1996).",
            "D. Đại hội IX (tháng 4/2001)."
        ],
        "answer": "B. Đại hội VII (tháng 6/1991)."
    },
    # 147
    {
        "question": "Về chế độ chính trị. Hiến pháp Nước Cộng hòa xã hội chủ nghĩa Việt Nam năm 2013 quy định:",
        "options": [
            "A. Nước Việt Nam là một nước dân chủ cộng hoà. Tất cả quyền bính trong nước là của toàn thể nhân dân Việt Nam, không phân biệt nòi giống, gái trai, giàu nghèo, giai cấp, tôn giáo.",
            "B. Nước Việt Nam dân chủ cộng hòa là một nước độc lập, có chủ quyền, thống nhất và toàn vẹn lãnh thổ, bao gồm đất liền, vùng trời, vùng quyền tài phán.",
            "C. Nước Cộng hoà xã hội chủ nghĩa Việt Nam là một nước độc lập, có chủ quyền, thống nhất và toàn vẹn lãnh thổ và là thành viên không thường trực của Hội đồng bảo an Liên hợp quốc.",
            "D. Nước Cộng hoà xã hội chủ nghĩa Việt Nam là một nước độc lập, có chủ quyền, thống nhất và toàn vẹn lãnh thổ, bao gồm đất liền, hải đảo, vùng biển và vùng trời."
        ],
        "answer": "D. Nước Cộng hoà xã hội chủ nghĩa Việt Nam là một nước độc lập, có chủ quyền, thống nhất và toàn vẹn lãnh thổ, bao gồm đất liền, hải đảo, vùng biển và vùng trời."
    },
    # 148
    {
        "question": "Nội dung nào sau đây được quy định trong Hiến pháp Nước Cộng hòa xã hội chủ nghĩa Việt Nam năm 2013 về chế độ chính trị:",
        "options": [
            "A. Nhà nước Cộng hòa xã hội chủ nghĩa Việt Nam là nhà nước pháp quyền xã hội chủ nghĩa của Nhân dân, do Nhân dân, vì Nhân dân.",
            "B. Nước Cộng hòa xã hội chủ nghĩa Việt Nam do Nhân dân làm chủ; tất cả quyền lực nhà nước thuộc về Nhân dân mà nền tảng là liên minh giữa giai cấp công nhân với giai cấp nông dân và đội ngũ trí thức.",
            "C. Quyền lực nhà nước là thống nhất, có sự phân công, phối hợp, kiểm soát giữa các cơ quan nhà nước trong việc thực hiện các quyền lập pháp, hành pháp, tư pháp.",
            "D. Tất cả các đáp án."
        ],
        "answer": "D. Tất cả các đáp án."
    },
    # 149
    {
        "question": "Đại hội đại biểu toàn quốc lần thứ mấy của Đảng Cộng sản Việt Nam đã xác định \"Nền kinh tế thị trường định hướng xã hội chủ nghĩa ở Việt Nam là nền kinh tế vận hành đầy đủ, đồng bộ theo các quy luật của kinh tế thị trường, đồng thời đảm bảo định hướng xã hội chủ nghĩa, phù hợp với từng giai đoạn phát triển của đất nước\":",
        "options": [
            "A. Đại hội VI (1986).",
            "B. Đại hội X (2006).",
            "C. Đại hội XI (2011).",
            "D. Đại hội XII (2016)."
        ],
        "answer": "D. Đại hội XII (2016)."
    },
    # 150
    {
        "question": "Nội dung nào sau đây được quy định trong Hiến pháp Nước Cộng hòa xã hội chủ nghĩa Việt Nam năm 2013:",
        "options": [
            "A. Tổ quốc Việt Nam là thiêng liêng, bất khả xâm phạm.",
            "B. Quốc kỳ nước Cộng hòa xã hội chủ nghĩa Việt Nam hình chữ nhật, chiều rộng bằng hai phần ba chiều dài, nền đỏ, ở giữa có ngôi sao vàng năm cánh.",
            "C. Đảng Cộng sản Việt Nam - Đội tiên phong của giai cấp công nhân, đồng thời là đội tiên phong của nhân dân lao động và của dân tộc Việt Nam, đại biểu trung thành lợi ích của giai cấp công nhân, nhân dân lao động và của cả dân tộc, lấy chủ nghĩa Mác - Lênin và tư tưởng Hồ Chí Minh làm nền tảng tư tưởng, là lực lượng lãnh đạo Nhà nước và xã hội.",
            "D. Tất cả các đáp án."
        ],
        "answer": "D. Tất cả các đáp án."
    },
    # 151
    {
        "question": "Đại hội nào Đảng ta xác định: \"Phải coi kinh tế tri thức là yếu tố quan trọng của nền kinh tế và CNH, HĐH\":",
        "options": [
            "A. Đại hội lần thứ VII (6/1991).",
            "B. Đại hội lần thứ VIII (6/1996).",
            "C. Đại hội lần thứ IX (4/2001).",
            "D. Đại hội lần thứ X (4/2006)."
        ],
        "answer": "D. Đại hội lần thứ X (4/2006)."
    },
    # 152
    {
        "question": "Sự khác biệt cơ bản giữa kinh tế thị trường định hướng xã hội chủ nghĩa với kinh tế thị trường tư bản chủ nghĩa ở chỗ:",
        "options": [
            "A. Bảo đảm vai trò quản lý, điều tiết nền kinh tế của Nhà nước pháp quyền xã hội chủ nghĩa dưới sự lãnh đạo của Đảng.",
            "B. Bảo đảm vai trò quản lý, điều tiết nền kinh tế của Nhà nước pháp quyền.",
            "C. Bảo đảm sự tồn tại của nhiều thành phần kinh tế.",
            "D. Là nền kinh tế hội nhập với kinh tế thế giới."
        ],
        "answer": "A. Bảo đảm vai trò quản lý, điều tiết nền kinh tế của Nhà nước pháp quyền xã hội chủ nghĩa dưới sự lãnh đạo của Đảng."
    },
    # 153
    {
        "question": "Theo tư duy mới của Đảng từ Đại hội VI (1986), kinh tế thị trường chỉ đối lập với:",
        "options": [
            "A. Kinh tế tự nhiên tự cấp, tự túc.",
            "B. Kinh tế tư bản chủ nghĩa.",
            "C. Kinh tế trong thời kỳ quá độ lên chủ nghĩa xã hội.",
            "D. Kinh tế xã hội chủ nghĩa."
        ],
        "answer": "A. Kinh tế tự nhiên tự cấp, tự túc."
    },
    # 154
    {
        "question": "\"Chiến lược biển Việt Nam đến năm 2020\" được thông qua tại:",
        "options": [
            "A. Đại hội VIII (tháng 6/1996).",
            "B. Hội nghị Trung ương 2 khóa IX (2005).",
            "C. Đại hội X (tháng 4/2006).",
            "D. Hội nghị Trung ương 4 khóa X (1-2007)."
        ],
        "answer": "D. Hội nghị Trung ương 4 khóa X (1-2007)."
    },
    # 155
    {
        "question": "Quan điểm của Đảng: \"Xây dựng nền văn hóa Việt Nam tiên tiến, đậm đà bản sắc dân tộc\" được Đảng nêu lần đầu tiên tại:",
        "options": [
            "A. Đại hội VI (tháng 12/1986).",
            "B. Đại hội VII (tháng 6/1991).",
            "C. Đại hội VIII (tháng 6/1996).",
            "D. Đại hội IX (tháng 4/2001)."
        ],
        "answer": "C. Đại hội VIII (tháng 6/1996)."
    },
    # 156
    {
        "question": "Đại hội nào của Đảng đưa ra quan điểm chỉ đạo: \"Đổi mới căn bản và toàn diện giáo dục và đào tạo ...\":",
        "options": [
            "A. Đại hội VII.",
            "B. Đại hội IX.",
            "C. Đại hội XI.",
            "D. Đại hội XII."
        ],
        "answer": "C. Đại hội XI."
    },
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_idx = 119
for i in range(len(clean_questions)):
    data['questions'][start_idx + i] = clean_questions[i]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully cleaned questions {start_idx} to {start_idx + len(clean_questions) - 1}!")
print(f"Total questions cleaned: {len(clean_questions)}")
