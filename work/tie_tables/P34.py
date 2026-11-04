# P34 tie table — WRITTEN BY HAND FROM work/analysis/P34_semantic.md.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
#
# Text/gap_after là chuỗi con nguyên văn trong câu (đã kiểm bằng pipeline.locate).
# Mỗi literal chỉ xuất hiện 1 lần trong câu của nó nên occ=1 tường minh cho mọi row.
# Cặp 6 câu, không có subhead, không có khối cắt, không có câu VI tự sinh.
# Quy ước: R/C/L chỉ liên câu ([LC]); các đại từ trong câu (it, his, họ, ông, đó
# tại S001/S002/S004) không đánh dấu — liệt kê trong analysis §4.3.
# occ=1 everywhere: mỗi literal được chọn chỉ xuất hiện đúng một lần trong câu.

ST = [
    # S002 — nền: Nga ra lệnh xóa nội dung, phạt nhỏ nhưng liên tục
    ("S002", "Russia", "L", "repetition",
     "S001: Russia's TASS news agency", "high", None,
     "đặt lại tên quốc gia làm chủ ngữ; chuỗi Russian/Russia's gieo ở câu mở đầu "
     "(A Russian court, Russian soldiers, Russia's TASS)", 1, None, None, "LC",
     None),
    ("S002", "content", "L", "repetition",
     "S001: hosting content on YouTube", "high", None,
     "lặp danh từ content (nội dung vì sao bị phạt)", 1, None, None, "LC",
     None),
    ("S002", "fines", "L", "repetition",
     "S001: has fined Alphabet's Google", "high", None,
     "fined → fines: lặp hình vị phạt qua danh hóa (động từ → danh từ)", 1,
     None, None, "LC", None),
    # S003 — Google không bình luận
    ("S003", "Google", "L", "repetition", "S001: Alphabet's Google", "high",
     None, "tên riêng lặp; câu phản hồi bình luận chuẩn của tin tức", 1, None, None,
     "LC", None),
    # S004 — giới chỉ trích cáo buộc chính quyền Nga
    ("S004", "Russian authorities", "L", "repetition",
     "S002: Russia has for several years ordered", "high", "R: the",
     "danh hiệu the Russian authorities = bộ máy nhà nước Nga; lặp hình vị "
     "Russian, đổi mô tả (quốc gia → chính quyền)", 1, None, None, "LC",
     None),
    ("S004", "YouTube", "L", "repetition", "S001: on YouTube", "high", None,
     "tên riêng lặp (YouTube's download speeds)", 1, None, None, "LC", None),
    ("S004", "content", "L", "repetition",
     "S002: remove content it deems illegal", "high", None,
     "lặp content lần 3 trong chuỗi (viewing content on it)", 1, None, None,
     "LC", None),
    # S005 — Nga phủ nhận cáo buộc
    ("S005", "Russia", "L", "repetition", "S004: the Russian authorities",
     "high", None, "tiếp chuỗi Nga (chủ ngữ phủ nhận)", 1, None, None, "LC",
     None),
    ("S005", "that", "R", "demonstrative",
     "S004: Critics accuse the Russian authorities of deliberately disrupting "
     "YouTube's download speeds", "high", None,
     "[LC] quy chiếu mệnh đề: that = trọn cáo buộc của giới chỉ trích ở câu "
     "trước; VI giữ 1-1 với 'điều đó'", 1, None, None, "LC", "A"),
    ("S005", "issues", "L", "general word",
     "S004: deliberately disrupting YouTube's download speeds", "med",
     "R: the",
     "the issues = chuyện tốc độ tải xuống đã nêu (bridging bằng danh từ tổng "
     "quát + mạo từ xác định)", 1, None, None, "LC", None),
    ("S005", "Google", "L", "repetition",
     "S003: Google did not immediately respond", "high", None,
     "tên riêng lặp (Google's own failure)", 1, None, None, "LC", None),
    ("S005", "failure", "L", "repetition", "S002: failures to comply", "med",
     None,
     "lặp hình vị failure, khác referent (hành vi không tuân thủ → việc không "
     "nâng cấp thiết bị); VI phân rã nên không có tie đối ứng", 1, None, None,
     "LC", None),
    ("S005", "charge", "L", "synonym",
     "S004: Critics accuse the Russian authorities", "med", None,
     "charge ≈ accuse (cùng trường tố cáo; đây là tuyên bố của Nga, khác cáo "
     "buộc của giới chỉ trích); VI giữ một từ cáo buộc nên bên VI là lặp", 1,
     None, None, "LC", None),
    # [Phase-2] the company ← Google: mạo từ the + rename bằng danh từ tổng
    # quát (mapping §3.6; H&H §6.1 general noun / §6.2 reiteration by general
    # word — Google → the company như "a bull" → "the animal"); một hình thức
    # một hàng nên the thâu vào alt (mapping §3.13).
    ("S005", "company", "L", "general word",
     "S003: Google did not immediately respond", "med", "R: the",
     "tổng quát hóa chuỗi Google (S001 Alphabet's Google → S003 Google); "
     "quy chiếu trong câu (Google's own failure) thâu vào alt R: the; VI đối "
     "xứng theo vị trí là lặp hình vị công ty (S001 công ty Alphabet)", 1,
     None, None, "LC", None),
    ("S005", "technology", "L", "repetition",
     "S002: foreign technology platforms", "med", None,
     "lặp hình vị technology (technology experts)", 1, None, None, "LC",
     None),
    # S006 — Putin cáo buộc Google
    ("S006", "Putin", "L", "repetition", "S004: President Vladimir Putin",
     "high", None,
     "lặp họ Putin; VI thêm danh xưng 'ông'", 1, None, None, "LC", None),
    ("S006", "accused", "L", "repetition",
     "S004: Critics accuse the Russian authorities", "high", None,
     "accuse → accused lặp hình vị; charge (câu trước) là thành viên đồng nghĩa "
     "cùng chuỗi", 1, None, None, "LC", None),
    ("S006", "Google", "L", "repetition", "S005: Google's own failure", "high",
     None, "tên riêng lặp (accused Google of being a tool)", 1, None, None,
     "LC", None),
    ("S006", "government", "L", "repetition", "S004: his government", "med",
     None,
     "lặp government (chính phủ Nga → the U.S. government): khác referent, "
     "tạo phép đối ngầm Nga–Mỹ", 1, None, None, "LC", None),
]

TT = [
    # S002 — nền: Nga ra lệnh xóa nội dung, tiền phạt nhỏ
    ("S002", "Nga", "L", "repetition",
     "S001: hãng thông tấn TASS của Nga", "high", None,
     "đặt lại tên quốc gia làm chủ ngữ; chuỗi Nga ×3 gieo ở câu mở đầu (Một "
     "tòa án Nga, binh lính Nga, TASS của Nga)", 1, None, None, "LC", None),
    ("S002", "nội dung", "L", "repetition",
     "S001: lưu trữ nội dung trên YouTube", "high", None,
     "lặp danh từ nội dung", 1, None, None, "LC", None),
    ("S002", "tiền phạt", "L", "repetition", "S001: phạt Google", "high",
     None,
     "phạt → tiền phạt: lặp hình vị phạt qua danh hóa (động từ → danh từ)", 1,
     None, None, "LC", None),
    # S003 — Google không trả lời
    ("S003", "Google", "L", "repetition",
     "S001: Google thuộc công ty Alphabet", "high", None,
     "tên riêng lặp; câu phản hồi chuẩn bình luận", 1, None, None, "LC",
     None),
    # S004 — những người chỉ trích cáo buộc chính quyền Nga
    ("S004", "chính quyền Nga", "L", "repetition",
     "S002: Nga đã ra lệnh", "high", None,
     "danh hiệu chính quyền Nga = bộ máy nhà nước; lặp hình vị Nga, đổi mô tả "
     "(quốc gia → chính quyền)", 1, None, None, "LC", None),
    ("S004", "YouTube", "L", "repetition", "S001: trên YouTube", "high", None,
     "tên riêng lặp (tốc độ tải xuống của YouTube)", 1, None, None, "LC",
     None),
    ("S004", "nội dung", "L", "repetition",
     "S002: xóa nội dung mà họ xem là bất hợp pháp", "high", None,
     "lặp nội dung lần 3 trong chuỗi (những nội dung trên đó)", 1, None, None,
     "LC", None),
    # S005 — Nga phủ nhận điều đó
    ("S005", "Nga", "L", "repetition", "S004: chính quyền Nga", "high", None,
     "tiếp chuỗi Nga (chủ ngữ phủ nhận)", 1, None, None, "LC", None),
    ("S005", "điều đó", "R", "demonstrative",
     "S004: Những người chỉ trích cáo buộc chính quyền Nga cố tình làm gián "
     "đoạn tốc độ tải xuống của YouTube", "high", None,
     "[LC] quy chiếu mệnh đề: điều đó = trọn cáo buộc của giới chỉ trích ở câu "
     "trước; giữ 1-1 với EN 'that'", 1, None, None, "LC", "A"),
    ("S005", "vấn đề", "L", "general word",
     "S004: làm gián đoạn tốc độ tải xuống của YouTube", "med", "R: các",
     "các vấn đề = chuyện tốc độ tải xuống đã nêu (bridging bằng danh từ tổng "
     "quát + 'các'); đối ứng EN 'the issues'", 1, None, None, "LC", None),
    ("S005", "Google", "L", "repetition", "S003: Google không trả lời", "high",
     None, "tên riêng lặp (do chính Google không nâng cấp)", 1, None, None,
     "LC", None),
    ("S005", "công ty", "L", "repetition", "S001: công ty Alphabet", "med",
     None,
     "lặp hình vị công ty; referent dịch chuyển (câu mở đầu chỉ Alphabet, ở "
     "đây chỉ Google theo quy chiếu trong câu); EN không có chuỗi 'company' "
     "tương ứng vì 'thuộc công ty' là VI tự sinh", 1, None, None, "LC",
     None),
    ("S005", "cáo buộc", "L", "repetition",
     "S004: Những người chỉ trích cáo buộc chính quyền Nga", "high", None,
     "động từ → danh từ: lặp nguyên văn cáo buộc; EN đổi từ (accuse → charge)",
     1, None, None, "LC", None),
    ("S005", "công nghệ", "L", "repetition",
     "S002: các nền tảng công nghệ", "med", None,
     "lặp công nghệ (chuyên gia công nghệ)", 1, None, None, "LC", None),
    # S006 — ông Putin cáo buộc Google
    ("S006", "Putin", "L", "repetition", "S004: Tổng thống Vladimir Putin",
     "high", None,
     "lặp họ Putin; VI thêm danh xưng 'ông' (EN chỉ 'Putin')", 1, None, None,
     "LC", None),
    ("S006", "cáo buộc", "L", "repetition", "S005: một cáo buộc", "high",
     None,
     "lặp nguyên văn cáo buộc (danh từ ở câu trước → động từ ở đây); EN dùng "
     "accused", 1, None, None, "LC", None),
    ("S006", "Google", "L", "repetition", "S005: do chính Google", "high",
     None, "tên riêng lặp (cáo buộc Google là công cụ)", 1, None, None, "LC",
     None),
    ("S006", "chính phủ", "L", "repetition", "S004: chính phủ của ông", "med",
     None,
     "lặp chính phủ (chính phủ của Putin → chính phủ Mỹ): khác referent, tạo "
     "phép đối ngầm Nga–Mỹ", 1, None, None, "LC", None),
]
