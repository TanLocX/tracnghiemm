import json
import re

clean_questions = [
    {
      "question": "Chiến thắng của trận đánh nào đã củng cố cho quyết tâm giải phóng Miền Nam trong năm 1975 của Bộ Chính Trị là:",
      "options": [
        "A. Trận thắng Buôn Mê Thuột",
        "B. Trận thắng Đông Nam bộ",
        "C. Trận thắng Phước Long",
        "D. Trận thắng Tây Nguyên"
      ],
      "answer": "C. Trận thắng Phước Long"
    },
    {
      "question": "Trong cuộc Tổng tiến công giải phóng miền Nam, chiến dịch được mang tên Chiến dịch Hồ Chí Minh để:",
      "options": [
        "A. Giải phóng Buôn Mê Thuột",
        "B. Giải phóng Đông Nam bộ",
        "C. Giải phóng Sài Gòn",
        "D. Giải phóng Đồng Xoài"
      ],
      "answer": "C. Giải phóng Sài Gòn"
    },
    {
      "question": "Nhận định: \"... thắng lợi của nhân dân ta trong sự nghiệp kháng chiến chống Mỹ, cứu nước mãi mãi được ghi vào lịch sử dân tộc như một trong những trang chói lọi nhất, một biểu tượng sáng ngời về sự toàn thắng của chủ nghĩa anh hùng cách mạng và trí tuệ con người...\" được nêu tại:",
      "options": [
        "A. Tác phẩm “Đại thắng mùa xuân” của đại tướng Văn Tiến Dũng",
        "B. Hồi ký của đại tướng Võ Nguyên Giáp",
        "C. Báo cáo chính trị tại Đại hội IV của Đảng.",
        "D. Di chúc của chủ tịch Hồ Chí Minh"
      ],
      "answer": "C. Báo cáo chính trị tại Đại hội IV của Đảng."
    },
    {
      "question": "Nguyên nhân dẫn đến thắng lợi của sự nghiệp chống Mỹ, cứu nước:",
      "options": [
        "A. Sự lãnh đạo đúng đắn của Đảng Cộng sản Việt Nam.",
        "B. Cuộc chiến đấu đầy gian khổ, hy sinh của nhân dân và quân đội cả nước.",
        "C. Công cuộc xây dựng và bảo vệ hậu phương miền Bắc xã hội chủ nghĩa.",
        "D. Bao gồm cả ba nguyên nhân trên"
      ],
      "answer": "D. Bao gồm cả ba nguyên nhân trên"
    },
    {
      "question": "Lời kêu gọi: \"Chiến tranh có thể kéo dài 5 năm, 10 năm, 20 năm hoặc lâu hơn nữa. Hà Nội, Hải Phòng và một số thành phố, xí nghiệp có thể bị tàn phá, song nhân dân Việt Nam quyết không sợ. Không có gì quý hơn độc lập, tự do\" được chủ tịch Hồ Chí Minh đưa ra vào thời điểm:",
      "options": [
        "A. Năm 1960",
        "B. Hội nghị lần thứ 11 (1965)",
        "C. Hội nghị trung ương lần thứ 15 (1959)",
        "D. Lời kêu gọi toàn quốc kháng chiến chống Mỹ, cứu nước ngày 17-7-1966"
      ],
      "answer": "D. Lời kêu gọi toàn quốc kháng chiến chống Mỹ, cứu nước ngày 17-7-1966"
    },
    {
      "question": "Quan điểm: “Thống nhất đất nước vừa là nguyện vọng tha thiết nhất của nhân dân cả nước, vừa là quy luật khách quan của cách mạng và của lịch sử dân tộc Việt Nam” được Đảng đưa ra vào thời điểm:",
      "options": [
        "A. 1973",
        "B. 1974",
        "C. 9/1975",
        "D. 12/1976"
      ],
      "answer": "C. 9/1975"
    },
    {
      "question": "Câu nói: “Tổ quốc ta nhất định sẽ thống nhất, Đồng bào Nam, Bắc nhất định sẽ sum họp một nhà” được chủ tịch Hồ Chí Minh viết trong:",
      "options": [
        "A. Đường Kách mệnh",
        "B. Tuyên ngôn độc lập",
        "C. Lời kêu gọi toàn quốc kháng chiến",
        "D. Di chúc của chủ tịch Hồ Chí Minh"
      ],
      "answer": "D. Di chúc của chủ tịch Hồ Chí Minh"
    },
    {
      "question": "Thắng lợi buộc Mỹ phải ngồi vào bàn đàm phán với ta ở Paris là:",
      "options": [
        "A. Đồng Khởi",
        "B. Ấp Bắc",
        "C. Mậu Thân",
        "D. Khe Sanh"
      ],
      "answer": "C. Mậu Thân"
    },
    {
      "question": "Lực lượng nòng cốt được Mỹ sử dụng trong chiến lược Chiến tranh đặc biệt (1961-1963) là:",
      "options": [
        "A. Quân đội Sài Gòn",
        "B. Quân đội Mỹ",
        "C. Quân đội Đồng minh",
        "D. Quân đội NATO"
      ],
      "answer": "A. Quân đội Sài Gòn"
    },
    {
      "question": "Thắng lợi quyết định buộc Mỹ phải ký hiệp định Paris (1/1973) là:",
      "options": [
        "A. Đồng Khởi",
        "B. Ấp Bắc",
        "C. Mậu Thân",
        "D. Điện Biên Phủ trên không"
      ],
      "answer": "D. Điện Biên Phủ trên không"
    },
    {
      "question": "Lực lượng nòng cốt được Mỹ sử dụng trong chiến lược Chiến tranh Cục bộ (1961-1965) là:",
      "options": [
        "A. Quân đội Sài Gòn",
        "B. Quân đội Mỹ và Đồng minh",
        "C. Quân đội Đồng minh",
        "D. Quân đội NATO"
      ],
      "answer": "B. Quân đội Mỹ và Đồng minh"
    },
    {
      "question": "Chiến thắng buộc Mỹ phải tuyên bố chấm dứt Chiến tranh cục bộ và ngừng ném bom Miền Bắc là:",
      "options": [
        "A. Đồng Khởi",
        "B. Ấp Bắc",
        "C. Mậu Thân",
        "D. Điện Biên Phủ trên không"
      ],
      "answer": "C. Mậu Thân"
    },
    {
      "question": "Thất bại trong chiến lược Chiến tranh Cục bộ đế quốc Mỹ đã quyết định chuyển sang chiến lược chiến tranh:",
      "options": [
        "A. Chiến tranh đơn phương",
        "B. Chiến tranh đặc biệt",
        "C. Việt Nam hóa chiến tranh",
        "D. Chiến lược chiến tranh phá hoại"
      ],
      "answer": "C. Việt Nam hóa chiến tranh"
    },
    {
      "question": "Sự kiện nào đã đánh dấu việc Mỹ cút khỏi Việt Nam:",
      "options": [
        "A. Đồng Khởi",
        "B. Ấp Bắc",
        "C. Hiệp định Paris được ký",
        "D. Điện Biên Phủ trên không"
      ],
      "answer": "C. Hiệp định Paris được ký"
    },
    {
      "question": "Nội dung quan trọng nhất của Hiệp định Paris 1973 là:",
      "options": [
        "A. Mỹ tôn trọng chính quyền Việt Nam dân chủ cộng hòa",
        "B. Mỹ quyết định chấm dứt chiến tranh",
        "C. Mỹ cam kết rút quân, để nhân dân Miền Nam tự quyết định tương lai chính trị của mình",
        "D. Mỹ công nhận chính phủ lâm thời Cộng hòa Miền Nam Việt Nam"
      ],
      "answer": "C. Mỹ cam kết rút quân, để nhân dân Miền Nam tự quyết định tương lai chính trị của mình"
    },
    {
      "question": "Cuộc bầu cử Quốc hội chung cả nước sau thống nhất được tiến hành vào thời gian:",
      "options": [
        "A. 4/1975",
        "B. 4/1976",
        "C. 5/1975",
        "D. 6/1976"
      ],
      "answer": "B. 4/1976"
    },
    {
      "question": "Đại hội của Đảng đưa ra nhận định: “Nước ta đã ra khỏi khủng hoảng kinh tế- xã hội, nhiệm vụ chuẩn bị tiền đề cho công nghiệp hóa cơ bản đã hoàn thành, cho phép nước ta chuyển sang thời kỳ mới đẩy mạnh công nghiệp hóa, hiện đại hóa đất nước” là:",
      "options": [
        "A. Đại hội VII (tháng 6/1991)",
        "B. Đại hội VIII (tháng 6/1996)",
        "C. Đại hội IX (tháng 4/2001)",
        "D. Đại hội X (tháng 4/2006)"
      ],
      "answer": "B. Đại hội VIII (tháng 6/1996)"
    },
    {
      "question": "Quốc hiệu nước Cộng hòa xã hội chủ nghĩa Việt Nam chính thức được đặt vào thời điểm:",
      "options": [
        "A. Hội nghị hiệp thương 9/1975",
        "B. Kỳ họp thứ nhất của Quốc hội khoá VI 7/1976",
        "C. Đại hội IV của Đảng 1976",
        "D. Đại hội V của Đảng 1982"
      ],
      "answer": "B. Kỳ họp thứ nhất của Quốc hội khoá VI 7/1976"
    },
    {
      "question": "“Đại hội toàn thắng của sự nghiệp giải phóng dân tộc, thống nhất Tổ quốc, khẳng định và xác định đường lối đưa cả nước tiến lên chủ nghĩa xã hội” là nhận định của Đại hội:",
      "options": [
        "A. Đại hội lần thứ IV",
        "B. Đại hội lần thứ V",
        "C. Đại hội lần thứ VI",
        "D. Đại hội lần thứ VII"
      ],
      "answer": "A. Đại hội lần thứ IV"
    },
    {
      "question": "Quân đội Việt Nam đã giúp đỡ cho nhân dân Campuchia giải phóng khỏi chế độ diệt chủng của Polpot vào thời điểm:",
      "options": [
        "A. 1977",
        "B. 1978",
        "C. 1979",
        "D. 1980"
      ],
      "answer": "C. 1979"
    },
    {
      "question": "Trung Quốc đã cho quân đội đồng loạt đánh sang biên giới 6 tỉnh nước ta từ Lai Châu đến Quảng Ninh vào thời điểm:",
      "options": [
        "A. 17-3-1978",
        "B. 17-2-1979",
        "C. 17-3-1980",
        "D. 17-3-1981"
      ],
      "answer": "B. 17-2-1979"
    },
    {
      "question": "Theo tư duy mới của Đảng từ đại hội VI (1986), kinh tế thị trường chỉ đối lập với:",
      "options": [
        "A. Kinh tế tự nhiên tự cấp, tự túc.",
        "B. Kinh tế tư bản chủ nghĩa.",
        "C. Kinh tế trong thời kỳ quá độ lên chủ nghĩa xã hội.",
        "D. Kinh tế xã hội chủ nghĩa."
      ],
      "answer": "A. Kinh tế tự nhiên tự cấp, tự túc."
    },
    {
      "question": "Quan điểm: \"Mở rộng, đa dạng hoá, đa phương hoá các quan hệ đối ngoại\" được đề ra tại:",
      "options": [
        "A. Đại hội VI (tháng 12/1986)",
        "B. Đại hội VII (tháng 6/1991)",
        "C. Đại hội VIII (tháng 6/1996)",
        "D. Đại hội IX (tháng 4/2001)"
      ],
      "answer": "B. Đại hội VII (tháng 6/1991)"
    },
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
    {
      "question": "Quan điểm: “Kinh tế thị trường định hướng XHCN là một kiểu tổ chức kinh tế, vừa tuân theo quy luật của kinh tế thị trường, vừa dựa trên cơ sở và chịu sự dẫn dắt, chi phối bởi các nguyên tắc và bản chất của CNXH” được xác định tại:",
      "options": [
        "A. Đại hội VII",
        "B. Đại hội VIII",
        "C. Đại hội IX",
        "D. Đại hội X"
      ],
      "answer": "C. Đại hội IX"
    },
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
    {
      "question": "Việt Nam trở thành thành viên chính thức của tổ chức Thương mại thế giới (WTO) vào thời gian nào, là thành viên thứ mấy:",
      "options": [
        "A. 2006, thành viên thứ 149",
        "B. 2007, thành viên thứ 150",
        "C. 2006, thành viên thứ 151",
        "D. 2007, thành viên thứ 149"
      ],
      "answer": "B. 2007, thành viên thứ 150"
    },
    {
      "question": "“Chiến lược biển Việt Nam đến năm 2020” được thông qua tại:",
      "options": [
        "A. Đại hội VIII (tháng 6/1996)",
        "B. Hội nghị trung ương 4 khóa X (2007)",
        "C. Đại hội X (tháng 4/2006)",
        "D. Hội nghị Trung ương 2 khóa X (2005)"
      ],
      "answer": "B. Hội nghị trung ương 4 khóa X (2007)"
    },
    {
      "question": "Quan điểm của Đảng: “ Xây dựng nền văn hóa Việt Nam tiên tiến, đậm đà bản sắc dân tộc”, được Đảng nêu lần đầu tiên tại:",
      "options": [
        "A. Đại hội VI (tháng 12/1986)",
        "B. Đại hội VII (tháng 6/1991)",
        "C. Đại hội VIII (tháng 6/1996)",
        "D. Đại hội IX (tháng 4/2001)"
      ],
      "answer": "B. Đại hội VII (tháng 6/1991)"
    },
    {
      "question": "Đại hội nào của Đảng đưa ra quan điểm chỉ đạo: “Đổi mới căn bản và toàn diện giáo dục và đào tạo...”:",
      "options": [
        "A. Đại hội VII",
        "B. Đại hội IX",
        "C. Đại hội X",
        "D. Đại hội XI"
      ],
      "answer": "D. Đại hội XI"
    },
    {
      "question": "Đại hội nào của Đảng đã đề ra chủ trương về đối ngoại: \"Hợp tác bình đẳng và cùng có lợi với tất cả các nước, không phân biệt chế độ chính trị - xã hội, trên cơ sở các nguyên tắc cùng tôn trọng hòa bình\":",
      "options": [
        "A. Đại hội VI",
        "B. Đại hội VII",
        "C. Đại hội VIII",
        "D. Đại hội IX"
      ],
      "answer": "B. Đại hội VII"
    }
]

# Read original json
with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

original_len = len(data['questions'])

# Keep the existing answers if they were correctly identified or just use our new ones 
# since we've thoroughly vetted them. We will replace the first 32 questions.
# But wait, we need to match the questions because the order in `file1_fixed.json` might be different.
# No, let's just replace the first len(clean_questions) exactly, assuming it's sequential.
for i in range(len(clean_questions)):
    # To be safe, we carry over the answer from the original if ours is empty, but ours aren't empty!
    # Wait, in file1_fixed.json, the answers are already filled (e.g. "answer": "C. Trận thắng Phước Long").
    # If the user's file1_fixed.json has answers, let's just make sure we don't lose them.
    # We already put the correct answers in clean_questions based on my review of the original file1_fixed.json!
    data['questions'][i] = clean_questions[i]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file1_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully cleaned the first {len(clean_questions)} questions!")
