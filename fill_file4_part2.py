import json

answers = [
    "B. Thu mua lương thực từ nước ngoài",                                                                                           # 90
    "A. Phát hành đồng giấy bạc Việt Nam",                                                                                          # 91
    "C. Yếu",                                                                                                                        # 92
    "D. Nha Bình dân học vụ",                                                                                                        # 93
    "A. 1945",                                                                                                                       # 94
    "C. Hạnh phúc, tự do",                                                                                                          # 95
    "C. Hơn 2 triệu người",                                                                                                         # 96
    "A. Chống giặc dốt, xoá nạn mù chữ",                                                                                           # 97
    "D. Đẩy lùi các tệ nạn, hủ tục, thói quen cũ, lạc hậu cản trở tiến bộ",                                                       # 98
    "A. Bầu cử toàn quốc để bầu ra Quốc hội và Chính phủ chính thức",                                                              # 99
    "B. 6/1/1946",                                                                                                                   # 100
    "B. Phổ thông đầu phiếu",                                                                                                       # 101
    "A. Công bộc",                                                                                                                   # 102
    "A. 1946",                                                                                                                       # 103
    "D. Hồ Chí Minh",                                                                                                               # 104
    "A. Hội Liên hiệp Quốc dân Việt Nam",                                                                                          # 105
    "C. Bầu cử Hội đồng nhân dân các cấp",                                                                                         # 106
    "A. Nhà hát lớn Hà Nội",                                                                                                        # 107
    "A. Tích cực mua sắm vũ khí, lương thực",                                                                                      # 108
    "B. Khắc phục và bỏ ngay những thói hư, tật xấu",                                                                              # 109
    "C. Tổ chức cuộc kháng chiến chống thực dân Pháp xâm lược ở Nam Bộ",                                                           # 110
    "A. Vĩnh Thụy",                                                                                                                  # 111
    "D. 1946 - 1954",                                                                                                                # 112
    "B. Cái Bè (Mỹ Tho)",                                                                                                           # 113
    "D. Củng cố lực lượng, kiên quyết đẩy lùi cuộc tấn công của quân Pháp",                                                        # 114
    "C. Nam Bộ",                                                                                                                     # 115
    "D. Triệt để lợi dụng mâu thuẫn kẻ thù, hòa hoãn, nhân nhượng có nguyên tắc với quân Tưởng",                                   # 116
    "A. Giao thiệp thân thiện, ứng xử mềm dẻo, linh hoạt với yêu sách của quân Tưởng và tay sai",                                  # 117
    "C. Tránh mũi nhọn tấn công của Pháp và Tưởng",                                                                                 # 118
    "B. Hội nghiên cứu chủ nghĩa Mác ở Đông Dương",                                                                                # 119
    "A. Thà chết tự do còn hơn sống nô lệ",                                                                                         # 120
    "A. Đồng ý bổ sung thêm 70 ghế trong Quốc hội cho các tổ chức này không qua bầu cử",                                           # 121
    "B. 1946",                                                                                                                       # 122
    "A. Thực dân Pháp",                                                                                                              # 123
    "C. Tiêu diệt tay sai, thúc đẩy nhanh quân Tưởng về nước",                                                                     # 124
    "D. Hiệp định sơ bộ",                                                                                                           # 125
    "A. Cùng lúc đối mặt trực tiếp với hai kẻ thù lớn là Pháp và Tưởng",                                                           # 126
    "C. Quân Pháp phải rút quân dần ra khỏi Việt Nam trong thời hạn 5 năm",                                                         # 127
    "A. Chuẩn bị lực lượng mọi mặt cho cuộc kháng chiến với Pháp",                                                                 # 128
    "B. Hoà để tiến",                                                                                                                # 129
    "D. Quân Pháp ở Việt Nam bộc lộ rõ thái độ bội ước, quyết tâm muốn xâm lược nước ta một lần nữa",                              # 130
    "A. Loạt đại bác bắn vào thành Hà Nội từ pháo đài Láng",                                                                       # 131
    "B. 60 ngày đêm",                                                                                                                # 132
    "C. Dựa trên sức mạnh toàn dân, tiến hành kháng chiến toàn dân, toàn diện, lâu dài và dựa vào sức mình là chính",               # 133
    "D. Trường Chinh",                                                                                                               # 134
    "B. Trung Quốc, Liên Xô, các nước Đông Âu, Triều Tiên",                                                                        # 135
    "A. Mở rộng căn cứ địa Việt Bắc",                                                                                               # 136
    "A. Bộ đội chủ lực, bộ đội địa phương, dân quân du kích",                                                                       # 137
    "A. Kết thúc thời kì chiến đấu trong vòng vây",                                                                                 # 138
    "A. Chiêm Hoá (Tuyên Quang)",                                                                                                   # 139
    "C. Đảng Lao động Việt Nam",                                                                                                    # 140
    "A. Ở nhiều nơi, việc phát triển Đảng quá nhanh dẫn đến việc mắc sai lầm về tiêu chuẩn Đảng viên",                             # 141
    "B. Chiến dịch Hoà Bình",                                                                                                       # 142
    "C. Công nhân, nông dân, tiểu tư sản và tư sản dân tộc",                                                                        # 143
    "B. Độc đoán, quan liêu, gây ra oan sai không đáng có",                                                                         # 144
    "A. Dân chủ nhân dân, một phần thuộc địa và nửa phong kiến",                                                                    # 145
    "A. Pháo đài không thể công phá",                                                                                               # 146
    "D. Võ Nguyên Giáp",                                                                                                            # 147
    "D. Chiến dịch Điện Biên Phủ",                                                                                                  # 148
    "A. Đánh chắc, tiến chắc",                                                                                                      # 149
    "A. Báo hiệu sự thắng lợi của nhân dân các dân tộc bị áp bức, sự sụp đổ của chủ nghĩa thực dân",                               # 150
    "A. Đánh dấu mốc cuộc kháng chiến chống Pháp kết thúc thắng lợi, miền Bắc được hoàn toàn giải phóng",                          # 151
    "B. 21/7/1954",                                                                                                                  # 152
    "B. Được hoàn toàn giải phóng, phát triển theo con đường xã hội chủ nghĩa",                                                     # 153
    "A. Kết hợp chặt chẽ và giải quyết đúng đắn mối quan hệ giữ hai nhiệm vụ cơ bản vừa kháng chiến vừa kiến quốc",                # 154
    "D. Đất nước ta bị chia làm hai miền với hai chế độ khác biệt",                                                                 # 155
    "A. Do chủ quan, giáo điều, không xuất phát từ tình hình thực tiễn ở nông thôn miền Bắc sau ngày giải phóng",                   # 156
    "B. Miền Bắc từng bước đi lên chủ nghĩa xã hội và trở thành hậu phương ổn định của tiền tuyến miền Nam",                       # 157
    "A. Góp phần hình thành đường lối cách mạng ở miền Nam của Đảng",                                                               # 158
    "C. Đế quốc Mỹ",                                                                                                                # 159
    "C. Tập hợp mọi lực lượng đấu tranh nhằm lật đổ chính quyền bù nhìn thân Mỹ, hoàn thành thống nhất Tổ quốc",                   # 160
    "A. Thông qua luật 10/59, đặt những người cộng sản ra khỏi vòng pháp luật",                                                     # 161
    "A. Dùng toà án quân sự đặc biệt để đưa những người bị bắt ra xét xử và bắn giết tại chỗ",                                     # 162
    "A. Tiếp tục cuộc cách mạng dân tộc dân chủ nhân dân",                                                                         # 163
    "D. Bến Tre",                                                                                                                    # 164
    "A. Tăng cường thực hiện chính sách \"tố cộng, diệt cộng\"",                                                                    # 165
    "A. Một tổ chức chính trị để tập hợp rộng rãi quần chúng nhân dân đoàn kết đấu tranh chống lại chính quyền độc tài của Ngô Đình Diệm", # 166
    "A. Đấu tranh đòi hiệp thương tổng tuyển cử",                                                                                   # 167
    "C. Chuyển cách mạng miền Nam từ thế giữ gìn lực lượng sang thế tiến công",                                                     # 168
    "D. Hà Nội",                                                                                                                     # 169
    "A. Xây dựng chủ nghĩa xã hội ở miền Bắc và đấu tranh hoà bình thống nhất nước nhà",                                           # 170
    "A. Thực hiện cách mạng xã hội chủ nghĩa ở miền Bắc, cách mạng dân tộc dân chủ nhân dân ở miền Nam",                           # 171
    "A. Từ một nền kinh tế nông nghiệp lạc hậu tiến thẳng lên chủ nghĩa xã hội, bỏ qua giai đoạn tư bản chủ nghĩa",               # 172
    "A. Hoàn chỉnh đường lối chiến lược chung của cách mạng Việt Nam trong giai đoạn mới",                                          # 173
    "B. 1961 - 1965",                                                                                                                # 174
    "C. Những con tàu bí mật chở vũ khí, hàng hoá từ miền Bắc vào chi viện cho miền Nam chống Mỹ",                                 # 175
    "A. 1961 - 1965",                                                                                                                # 176
    "C. Chiến tranh đặc biệt",                                                                                                      # 177
    "A. Trở thành hậu phương vững chắc, đủ sức cung cấp nhân lực, tài lực, vật lực cho tiền tuyến miền Nam",                       # 178
    "C. Quân giải phóng miền Nam Việt Nam",                                                                                         # 179
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_idx = 90
for i, ans in enumerate(answers):
    data['questions'][start_idx + i]['answer'] = ans

with open(r'c:\vscode\code\TN_MMT\lichsudang\file4.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done: cau {start_idx} den {start_idx + len(answers) - 1}")
