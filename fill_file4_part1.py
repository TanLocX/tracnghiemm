import json

# Danh sách đáp án câu 0-89
answers = [
    "B. Tập trung dân chủ",                                                                              # 0
    "C. Sự ra đời, phát triển và hoạt động lãnh đạo của Đảng qua các thời kỳ lịch sử",                  # 1
    "B. Chức năng nhận thức, giáo dục, dự báo và phê phán",                                              # 2
    "A. Khẳng định, chứng minh giá trị khoa học của những mục tiêu chiến lược và sách lược cách mạng mà Đảng đề ra trong cương lĩnh",  # 3
    "A. Chủ nghĩa duy vật biện chứng và chủ nghĩa duy vật lịch sử",                                     # 4
    "B. Để nhận thức tiến trình cách mạng do Đảng Cộng sản Việt Nam lãnh đạo",                          # 5
    "D. Phương pháp logic",                                                                               # 6
    "A. Làm rõ kinh nghiệm, bài học, quy luật phát triển của cách mạng Việt Nam",                       # 7
    "B. Phương pháp làm việc nhóm",                                                                       # 8
    "B. Giáo dục lý tưởng, truyền thống đấu tranh của Đảng, bồi đắp niềm tin vào sự lãnh đạo của Đảng", # 9
    "A. Mâu thuẫn giữa dân tộc ta với thực dân Pháp, mâu thuẫn giữa nông dân với địa chủ phong kiến",  # 10
    "C. Công nhân",                                                                                       # 11
    "A. Địa chủ phong kiến và nông dân",                                                                  # 12
    "C. Không có đường lối rõ ràng dẫn đến thất bại và bị thực dân Pháp đàn áp một cách nặng nề",      # 13
    "A. Ngu dân",                                                                                         # 14
    "A. Có sự tham gia vào đời sống chính trị, kinh tế của chính quyền thực dân Pháp",                  # 15
    "C. Vì địa vị kinh tế của họ bấp bênh, thái độ hay dao động",                                       # 16
    "A. Giải phóng dân tộc",                                                                              # 17
    "D. Năm 1930, khi Đảng Cộng sản Việt Nam ra đời",                                                    # 18
    "C. Vụ mưu sát viên toàn quyền Méc-Lanh của Phạm Hồng Thái (1924)",                                 # 19
    "C. Khuynh hướng vô sản",                                                                             # 20
    "C. Phan Bội Châu",                                                                                   # 21
    "B. Đọc bản Sơ thảo lần thứ nhất những luận cương về vấn đề dân tộc và vấn đề thuộc địa của Lênin", # 22
    "D. Người cùng khổ",                                                                                  # 23
    "B. 1920",                                                                                            # 24
    "B. Cách mạng dân tộc, dân chủ",                                                                     # 25
    "C. Yên Bái",                                                                                         # 26
    "A. Bản án chế độ thực dân Pháp",                                                                    # 27
    "D. Thành lập Hội Việt Nam Cách mạng Thanh niên (6/1925)",                                           # 28
    "D. Thanh niên",                                                                                      # 29
    "C. Bãi công của thợ máy xưởng Ba Son cảng Sài Gòn (1925)",                                          # 30
    "B. Đường Kách mệnh (1927)",                                                                          # 31
    "B. Tư sản dân quyền và thổ địa cách mạng để đi tới xã hội cộng sản",                               # 32
    "D. Chuẩn bị thành lập một đảng cộng sản thay thế Hội Việt Nam Cách mạng Thanh niên",               # 33
    "D. Hội Việt Nam Cách mạng Thanh niên",                                                              # 34
    "B. Đông Dương Cộng sản Đảng",                                                                       # 35
    "B. Hội Việt Nam Cách mạng Thanh niên",                                                              # 36
    "A. Truyền bá tư tưởng vô sản, xây dựng, phát triển tổ chức của công nhân",                         # 37
    "A. Cách mạng Việt Nam đã có bước phát triển về chất, phù hợp với yêu cầu của lịch sử",             # 38
    "C. Thống nhất các tổ chức cộng sản",                                                                # 39
    "B. Dân quyền cách mạng",                                                                            # 40
    "B. Giai cấp công nhân",                                                                              # 41
    "D. Sự ra đời của ba tổ chức Cộng sản (1929)",                                                       # 42
    "C. Chánh cương vắn tắt và Sách lược vắn tắt của Đảng",                                             # 43
    "A. Đánh đổ đế quốc Pháp và phong kiến, làm cho nước Nam hoàn toàn độc lập",                        # 44
    "B. Đấu tranh chống chủ nghĩa phát-xít, chống chiến tranh, bảo vệ dân chủ và hòa bình",             # 45
    "A. Cách mạng điền địa",                                                                             # 46
    "C. Mặt trận nhân dân Pháp lên cầm quyền ở Đông Dương",                                             # 47
    "C. Chống phát-xít, chống chiến tranh đế quốc, chống bọn phản động thuộc địa, đòi tự do, dân chủ, cơm áo hòa bình", # 48
    "B. Đấu tranh nghị trường",                                                                           # 49
    "D. Phản động thuộc địa và bè lũ tay sai",                                                           # 50
    "B. Giúp cán bộ, đảng viên của Đảng được rèn luyện và trưởng thành",                                # 51
    "D. Mặt trận Dân chủ Đông Dương",                                                                    # 52
    "B. Cuộc vận động dân chủ 1936 - 1939",                                                              # 53
    "A. Chuẩn bị khởi nghĩa vũ trang",                                                                   # 54
    "B. Giải phóng dân tộc",                                                                              # 55
    "C. Rút vào hoạt động bí mật, chuyển trọng tâm công tác về nông thôn",                               # 56
    "C. Kinh tế chỉ huy",                                                                                 # 57
    "B. Bắt người dân nhổ lúa, trồng đay lấy nguyên liệu phục vụ chiến tranh",                          # 58
    "D. Dân tộc giải phóng",                                                                              # 59
    "C. 1941",                                                                                            # 60
    "C. Mặt trận Việt Minh",                                                                              # 61
    "C. Phát động cao trào kháng Nhật cứu nước",                                                          # 62
    "C. Đặt ra vấn đề giải phóng dân tộc trong từng nước Đông Dương",                                   # 63
    "C. 22/12/1944",                                                                                      # 64
    "B. Thời cơ trong khởi nghĩa giành chính quyền",                                                     # 65
    "B. Khởi nghĩa Nam Kì (1940)",                                                                        # 66
    "A. Nhiệm vụ quân sự",                                                                                # 67
    "A. Quân Nhật",                                                                                       # 68
    "B. Chỉ thị Nhật - Pháp bắn nhau và hành động của chúng ta (3/1945)",                                # 69
    "D. Sự đầu hàng vô điều kiện của phát-xít Nhật",                                                     # 70
    "C. 1945",                                                                                            # 71
    "B. Hội nghị toàn quốc của Đảng (8/1945)",                                                           # 72
    "D. Tập trung, thống nhất và kịp thời",                                                               # 73
    "A. Tán thành chủ trương Tổng khởi nghĩa của Đảng, quyết định đặt tên nước Việt Nam Dân chủ Cộng hòa", # 74
    "C. Từ sau khi Nhật đầu hàng Đồng minh đến trước khi quân Đồng minh vào Đông Dương",                # 75
    "A. Ủy ban giải phóng dân tộc Việt Nam",                                                             # 76
    "C. Ủy ban dân tộc Giải phóng Việt Nam",                                                             # 77
    "B. 19/8/1945",                                                                                       # 78
    "C. Đấu tranh chính trị kết hợp với đấu tranh vũ trang",                                             # 79
    "C. Sự lãnh đạo của Đảng",                                                                           # 80
    "D. Giương cao ngọn cờ độc lập dân tộc, kết hợp đúng đắn hai nhiệm vụ chống đế quốc và chống phong kiến", # 81
    "B. Cuộc cách mạng giải phóng dân tộc",                                                              # 82
    "B. Độc lập và tự do",                                                                                # 83
    "A. Chưa có quốc gia nào ủng hộ lập trường độc lập và công nhận địa vị pháp lý về mặt nhà nước của Việt Nam", # 84
    "C. Thực dân Pháp",                                                                                   # 85
    "A. Diệt Cộng, cầm Hồ",                                                                              # 86
    "B. Ngân khố nhà nước trống rỗng",                                                                    # 87
    "C. Công nghiệp đình đốn, nông nghiệp bị hoang hóa",                                                 # 88
    "A. Công nông",                                                                                       # 89
]

with open(r'c:\vscode\code\TN_MMT\lichsudang\file4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

start_idx = 0
for i, ans in enumerate(answers):
    data['questions'][start_idx + i]['answer'] = ans

with open(r'c:\vscode\code\TN_MMT\lichsudang\file4.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done: cau {start_idx} den {start_idx + len(answers) - 1}")
