# P40 tie table — WRITTEN BY HAND FROM work/analysis/P40_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Text/gap_after là chuỗi con nguyên văn trong câu (đã kiểm tra số lần xuất hiện).
# Bản tin ngắn 7 câu EN (S002+S003 là MỘT câu bị segmentation chẻ tại "Aug.") / 6 câu VI.
# Không có câu cắt, không có câu VI tự sinh. EN: 0 R liên câu (his/its đều trong câu).

ST = [
    # S002 — nhắc lại nước đầu tiên trong danh sách cứu trợ
    ("S002", "Haiti", "L", "repetition",
     "S001: Haiti, Bangladesh and Vietnam", "high", None,
     "lặp tên nước Haiti (lần nhắc thứ hai trong bản tin)", 1, None, None,
     "LC", None),
    ("S002", "help", "L", "repetition",
     "S001: to help with emergency relief", "high", None,
     "lặp động từ help trong trường cứu trợ; VI đối ứng giúp đỡ (S002)",
     1, None, None, "LC", None),

    # S004 — khoản Bangladesh/Việt Nam
    ("S004", "sent", "L", "repetition",
     "S001: has sent", "high", None,
     "lặp động từ gửi tiền (has sent → was sent)", 1, None, None,
     "LC", None),
    ("S004", "Bangldesh", "L", "repetition",
     "S001: Bangladesh", "high", None,
     "lặp tên nước; nguồn EN sai chính tả Bangldesh (thiếu a) và VI copy "
     "nguyên lỗi — trích nguyên văn, không sửa", 1, None, None, "LC", None),
    ("S004", "assistance", "L", "synonym",
     "S002: to help in the aftermath", "med", None,
     "assistance ≈ help/relief trong trường viện trợ; chuỗi cứu trợ đi qua "
     "S001 emergency relief", 1, None, None, "LC", None),
    ("S004", "people", "L", "repetition",
     "S003: more than 2,000 people", "med", None,
     "lặp danh từ tổng quát people; nhóm người khác nhau (nạn nhân động đất "
     "Haiti ↔ nạn nhân bão Yaas)", 1, None, None, "LC", None),
    ("S004", None, "E", "verbal",
     "S004: About $70,000 was sent (trong câu)", "high", None,
     "[TC] lược động từ bị động trong vế tọa hợp thứ hai sau and; hồi phục "
     "{was sent}", 1, "euros ", "{was sent}", "TC", None),
    ("S004", "Vietnam", "L", "repetition",
     "S001: Vietnam", "high", None,
     "lặp tên nước Việt Nam", 1, None, None, "LC", None),

    # S005 — cách thức chuyển tiền
    ("S005", "Vatican", "L", "repetition",
     "S001: the Vatican said on Tuesday", "high", "R: The",
     "đặt lại tên chủ thể nguồn tin; VI đối ứng Vatican (S004)",
     1, None, None, "LC", None),
    ("S005", "sums", "L", "general word",
     "S002-S004: 200,000 euros / About $70,000 / about 100,000 euros",
     "med", "R: the",
     "danh từ tổng quát tóm chỉ các khoản tiền đã liệt kê; VI đối ứng là chỉ "
     "từ này trong 'số tiền này' (S004, R)", 1, None, None, "LC", None),
    ("S005", None, "E", "nominal",
     "S005: the sums (trong câu)", "high", None,
     "[TC] lược chủ ngữ vế tọa hợp thứ hai sau and; hồi phục {the sums}",
     1, "and ", "{the sums}", "TC", None),
    ("S005", "countries", "L", "general word",
     "S001: Haiti, Bangladesh and Vietnam", "med", "R: the",
     "danh từ tổng quát tóm chỉ ba nước nhận viện trợ; VI đối ứng các nước "
     "(S004)", 1, None, None, "LC", None),

    # S006 — nguồn gốc quỹ Peter's Pence
    ("S006", "charity money", "L", "repetition",
     "S001: charity funds", "high", None,
     "charity lặp; money ≈ funds (đồng nghĩa)", 1, None, None,
     "LC", None),
    ("S006", "pope", "L", "repetition",
     "S001: Pope Francis", "high", "R: the",
     "NP sở hữu cách the pope's đặt lại tên giáo hoàng; mạo từ thâu vào alt; "
     "VI đối ứng Giáo hoàng (S005)", 1, None, None, "LC", None),
    ("S006", "personal disposal", "L", "repetition",
     "S001: at his personal disposal", "high", None,
     "lặp nguyên cụm personal disposal; VI đối ứng danh nghĩa cá nhân (S005)",
     1, None, None, "LC", None),
    ("S006", "contribute", "L", "repetition",
     "S005: initial contributions", "med", None,
     "lặp hình vị contribute/contributions; hướng cho khác nhau (các khoản "
     "của giáo hoàng ↔ tín hữu đóng vào quỹ)", 1, None, None, "LC", None),

    # S007 — quy mô quỹ
    ("S007", "fund", "L", "repetition",
     "S006: Peter's Pence, a fund to which Catholics can contribute", "high",
     "R: The",
     "The fund ← Peter's Pence/a fund; VI đối ứng quỹ này (S006, thêm chỉ từ)",
     1, None, None, "LC", None),
]

TT = [
    # S002 — khoản Haiti
    ("S002", "Haiti", "L", "repetition",
     "S001: Haiti, Bangladesh và Việt Nam", "high", None,
     "lặp tên nước Haiti", 1, None, None, "LC", None),
    ("S002", "giúp đỡ", "L", "repetition",
     "S001: để giúp cứu trợ khẩn cấp", "high", None,
     "lặp hình vị giúp (giúp cứu trợ → giúp đỡ); đối ứng EN help (S002)",
     1, None, None, "LC", None),

    # S003 — khoản Bangladesh/Việt Nam
    ("S003", "gửi", "L", "repetition",
     "S001: vừa gửi", "high", None,
     "lặp động từ gửi (vừa gửi → đã được gửi)", 1, None, None,
     "LC", None),
    ("S003", "Bangldesh", "L", "repetition",
     "S001: Bangladesh", "high", None,
     "copy nguyên lỗi chính tả Bangldesh của bản EN", 1, None, None,
     "LC", None),
    ("S003", "hỗ trợ", "L", "synonym",
     "S002: để giúp đỡ", "med", None,
     "hỗ trợ ≈ giúp đỡ; hình vị trợ lặp với cứu trợ (S001)", 1, None, None,
     "LC", None),
    ("S003", "người", "L", "repetition",
     "S002: hơn 2.000 người thiệt mạng", "med", None,
     "lặp danh từ tổng quát người; nhóm người khác nhau (nạn nhân động đất ↔ "
     "nạn nhân bão)", 1, None, None, "LC", None),
    ("S003", None, "E", "verbal",
     "S003: đã được gửi đến Bangldesh (trong câu)", "high", None,
     "[TC] lược động từ trong vế tọa hợp thứ hai sau và; hồi phục "
     "{đã được gửi}; đối ứng E-EN1 (S004 EN)", 1, "euro ", "{đã được gửi}",
     "TC", None),
    ("S003", "Việt Nam", "L", "repetition",
     "S001: Việt Nam", "high", None,
     "lặp tên nước Việt Nam", 1, None, None, "LC", None),

    # S004 — cách thức chuyển tiền
    ("S004", "Vatican", "L", "repetition",
     "S001: Reuters dẫn nguồn tin từ Vatican", "high", None,
     "đặt lại tên chủ thể; Vatican xuất hiện 2 lần trong câu (các đại sứ quán "
     "của Vatican) — 1 chuỗi 1 dấu, lần thứ hai không đánh", 1, None, None,
     "LC", None),
    ("S004", "này", "R", "demonstrative",
     "S002-S003: 200.000 euro ... Khoảng 70.000 đôla ... khoảng 100.000 euro",
     "high", None,
     "số tiền này — chỉ từ tóm chỉ các khoản tiền đã nêu; EN đối ứng the sums "
     "(S005 EN, L general word)", 1, None, None, "LC", "A"),
    ("S004", None, "E", "nominal",
     "S004: số tiền này (trong câu)", "high", None,
     "[TC] lược chủ ngữ vế tọa hợp thứ hai sau và; hồi phục {số tiền này}; "
     "đối ứng E-EN2 (S005 EN)", 1, "và ", "{số tiền này}", "TC", None),
    ("S004", "chuyển giao", "L", "repetition",
     "S002: sẽ được chuyển đến Haiti", "med", None,
     "lặp hình vị chuyển (chuyển → chuyển giao); EN đổi động từ (administered) "
     "nên không có đối ứng EN — VI tự sinh mắt xích chuỗi động từ",
     1, None, None, "LC", None),
    ("S004", "các nước", "L", "general word",
     "S001: Haiti, Bangladesh và Việt Nam", "med", None,
     "danh từ tổng quát tóm chỉ ba nước nhận viện trợ; đối ứng EN the "
     "countries (S005)", 1, None, None, "LC", None),

    # S005 — nguồn gốc quỹ Peter's Pence (VI đảo trật tự, tái dùng công thức S001)
    ("S005", "số tiền từ thiện", "L", "repetition",
     "S001: quỹ từ thiện", "high", None,
     "từ thiện lặp; quỹ ≈ số tiền; chuỗi đi qua S004 (số tiền này); đối ứng "
     "EN charity money (S006)", 1, None, None, "LC", None),
    ("S005", "này", "R", "demonstrative",
     "S004: số tiền này", "high", None,
     "số tiền từ thiện này — chỉ từ; EN chỉ dùng mạo từ (the charity money, "
     "S006 EN)", 1, None, None, "LC", "A"),
    ("S005", "Giáo hoàng", "L", "repetition",
     "S001: Ðức giáo hoàng Francis", "high", None,
     "danh xưng viết hoa giữa câu, bỏ Ðức so với S001; đối ứng EN the pope's "
     "(S006)", 1, None, None, "LC", None),
    ("S005", "danh nghĩa cá nhân", "L", "repetition",
     "S001: với danh nghĩa cá nhân", "high", None,
     "lặp nguyên cụm (dấu vết tái dùng công thức câu mở đầu); đối ứng EN "
     "personal disposal (S006)", 1, None, None, "LC", None),
    ("S005", "đóng góp", "L", "repetition",
     "S004: khoản đóng góp ban đầu", "med", None,
     "lặp hình vị đóng góp; hướng cho khác nhau (khoản của giáo hoàng ↔ tín "
     "hữu đóng vào quỹ); đối ứng EN contribute (S006)", 1, None, None,
     "LC", None),

    # S006 — quy mô quỹ
    ("S006", "quỹ", "L", "repetition",
     "S005: quỹ Peter's Pence", "high", None,
     "quỹ này ← quỹ Peter's Pence/một quỹ; đối ứng EN The fund (S007)",
     1, None, None, "LC", None),
    ("S006", "này", "R", "demonstrative",
     "S005: quỹ Peter's Pence", "high", None,
     "quỹ này — chỉ từ; EN chỉ có mạo từ The (S007 EN)", 1, None, None,
     "LC", "A"),
]
