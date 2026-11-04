# P35 tie table — WRITTEN BY HAND FROM work/analysis/P35_semantic.md.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
#
# Text/gap_after là chuỗi con nguyên văn trong câu (kiểm bằng pipeline.locate).
# P35 = 8 câu EN / 8 câu VI, ánh xạ 1-1, không có khối cắt.
# Quy ước: mỗi chuỗi L 1 dấu/câu; đại từ trong câu không đánh (xem §4.3 analysis).

ST = [
    # S001 — không có tie: toàn bộ lần đầu; "it" ← Maxar Technologies (trong câu).

    # S002
    ("S002", "Maxar", "L", "repetition",
     "S001: U.S. aerospace firm Maxar Technologies", "high", None,
     "[LC] lặp tên riêng; 'it has contracts' trong câu không đánh", 1, None,
     None, "LC", None),
    ("S002", "U.S. government", "L", "repetition",
     "S001: one U.S. government platform", "high", "R: the",
     "[LC] lặp nguyên văn U.S. government (ở S001 là định ngữ của platform); "
     "cùng thực thể với chính quyền Trump", 1, None, None, "LC", None),
    # [Phase-2] use ← users (S001): lặp hình vị use qua đổi loại từ danh từ
    # → động từ (H&H §6.2 reiteration; TNT §26 phép lặp; tiền lệ P21 invest
    # ← investments); referent khác (người dùng Ukraine ≠ mỗi khách hàng)
    # nên conf med.
    ("S002", "use", "L", "repetition",
     "S001: Ukrainian users' access", "med", None,
     "[LC] lặp hình vị use (users → use); 'họ' trong quote ← Each customer "
     "cùng câu, không đánh", 1, None, None, "LC", None),
    # [Phase-2] share ← sharing (S001): mắt xích sót của chuỗi chia sẻ
    # (H&H §6.2; TNT §26) — dữ liệu khách hàng chia sẻ chính là hình ảnh vệ
    # tinh = nguồn tình báo bị đình chỉ; S008 intelligence-sharing giữ tiền
    # trạm S001 vì trùng cặp predication (tiền lệ P21 scams ← scams bỏ qua
    # scammed ở giữa).
    ("S002", "share", "L", "repetition",
     "S001: suspends intelligence sharing", "med", None,
     "[LC] lặp hình vị share (sharing → share); khách hàng chia sẻ chính là "
     "dữ liệu hình ảnh = tình báo bị đình chỉ", 1, None, None, "LC", None),
    ("S002", "that data", "R", "demonstrative",
     "S001: satellite imagery", "med", None,
     "[LC] demonstrative NP truy hồi hình ảnh vệ tinh (dữ liệu khách hàng "
     "dùng/chia sẻ); 'their/they' trong quote ← 'Each customer' cùng câu, "
     "không đánh", 1, None, None, "LC", "A"),

    # S003
    ("S003", "company", "L", "general word", "S002: Maxar", "high", "R: The",
     "[LC] danh từ tổng quát chỉ Maxar", 1, None, None, "LC", None),
    ("S003", "contract", "L", "repetition",
     "S002: contracts with the U.S. government", "high", "R: the",
     "[LC] lặp contract; 'in question' tóm chỉ hợp đồng đang bàn (VI: 'được "
     "nói tới')", 1, None, None, "LC", None),
    # [Phase-2] GEGD (S003) ← platform (S001): mắt xích được cite làm tiền
    # trạm ở S004 nhưng trước đây không có hàng (bài học P28, nhóm 12) —
    # GEGD là tên riêng của "one U.S. government platform" đã nêu ở S001,
    # nhận diện hồi tố qua S004 "suspend Ukrainian accounts in GEGD" (=
    # sự kiện S001); H&H §6.1 bridging; "a U.S. government program" là đồng
    # vị trong câu, không đánh thêm.
    ("S003", "GEGD", "L", "general word",
     "S001: one U.S. government platform", "med", None,
     "[LC] đặt tên riêng cho nền tảng đã nêu ở S001 (nhận diện hồi tố; "
     "H&H §6.1 bridging)", 1, None, None, "LC", None),
    ("S003", "U.S. government", "L", "repetition",
     "S002: the U.S. government", "high", None,
     "[LC] định ngữ trong 'a U.S. government program'; 'program' lặp trong "
     "câu với 'GEOINT Delivery program'; 'the United States' cuối câu là "
     "biến thể U.S. → United States — đều không đánh thêm", 1, None, None,
     "LC", None),
    ("S003", "access", "L", "repetition",
     "S001: Ukrainian users' access to satellite imagery", "high", None,
     "[LC] lặp danh từ access", 1, None, None, "LC", None),
    ("S003", "satellite imagery", "L", "repetition",
     "S001: satellite imagery", "high", None,
     "[LC] lặp satellite imagery; thêm định ngữ mới 'commercial'", 1, None,
     None, "LC", None),

    # S004
    ("S004", "U.S. government", "L", "repetition",
     "S003: a U.S. government program", "high", "R: The",
     "[LC] chủ ngữ câu trích dẫn; 'the U.S. National Geospatial-Intelligence "
     "Agency' lần đầu không đánh; 'the action' trong câu không đánh", 1,
     None, None, "LC", None),
    # [Phase-2] decided ← decisions (S002): lặp hình vị decide qua danh từ
    # → động từ (H&H §6.2 reiteration; TNT §26 phép lặp); hai "quyết định"
    # khác referent (khách hàng ≠ chính phủ) nên conf med; hàng này neo mắt
    # xích S004 được "directive" (S005) và C-EN1 cite làm tiền trạm.
    ("S004", "decided", "L", "repetition",
     "S002: makes their own decisions", "med", None,
     "[LC] lặp hình vị decide (decisions → decided); quyết định của chính "
     "phủ ≠ của khách hàng — lặp từ vựng, khác referent", 1, None, None,
     "LC", None),
    ("S004", "suspend", "L", "repetition",
     "S001: suspends intelligence sharing", "high", None,
     "[LC] lặp động từ suspend (đối tượng khác: accounts)", 1, None, None,
     "LC", None),
    ("S004", "Ukrainian accounts", "L", "repetition",
     "S001: Ukrainian users' access", "med", None,
     "[LC] lặp Ukrainian; đổi đầu từ users → accounts", 1, None, None, "LC",
     None),
    ("S004", "GEGD", "L", "repetition",
     "S003: GEGD (the Global Enhanced GEOINT Delivery program)", "high",
     None, "[LC] viết tắt lặp", 1, None, None, "LC", None),
    ("S004", "Maxar", "L", "repetition", "S003: The company", "high", None,
     "[LC] đặt lại tên sau 'The company'", 1, None, None, "LC", None),

    # S005
    ("S005", "In accordance with", "C", "causal",
     "S004: The U.S. government has decided to temporarily suspend Ukrainian "
     "accounts in GEGD", "med", None,
     "[LC] nối nhân-quả: hành động của NGA tuân theo quyết định đã nêu ở "
     "S004; 'directive' truy hồi 'has decided'", 1, None, None, "LC", None),
    ("S005", "administration", "L", "synonym",
     "S004: The U.S. government", "med", "R: the",
     "[LC] administration ≈ U.S. government — cùng thực thể chính quyền Mỹ "
     "(lần đầu: S001 'Donald Trump's administration'); 'U.S. "
     "government-purchased' cuối câu cùng chuỗi, không đánh thêm", 1, None,
     None, "LC", None),
    # [Phase-2] directive ← decided (S004): danh từ tổng quát đổi tên quyết
    # định đã nêu (H&H §6.1 general word; mapping §3.6 the+rename → alt
    # "R: the"); trước đây §6 analysis liệt vào danh sách "không đánh" —
    # Phase-2 nhóm 3 điều chỉnh; tách khỏi hàng C "In accordance with"
    # (khác hình thức, khác quan hệ).
    ("S005", "directive", "L", "general word",
     "S004: has decided to temporarily suspend Ukrainian accounts in "
     "GEGD", "med", "R: the",
     "[LC] danh từ tổng quát tóm chỉ quyết định của chính quyền ở S004 "
     "(H&H §6.1); khác hình thức với hàng C cùng câu", 1, None, None,
     "LC", None),
    ("S005", "Ukraine", "L", "repetition", "S004: Ukrainian accounts",
     "high", None, "[LC] danh từ Ukraine lặp tính từ Ukrainian", 1, None,
     None, "LC", None),
    ("S005", "NGA", "L", "synonym",
     "S004: the U.S. National Geospatial-Intelligence Agency", "high", None,
     "[LC] nén thành viết tắt (VI lặp tên đầy đủ); 'the agency' trong câu "
     "(a spokesperson for the agency) quy chiếu trong câu, không đánh", 1,
     None, None, "LC", None),
    ("S005", "suspended", "L", "repetition", "S004: temporarily suspend",
     "high", None,
     "[LC] lặp suspend; 'temporarily' lặp cặp S004-S005 (không đánh riêng)",
     1, None, None, "LC", None),
    ("S005", "access", "L", "repetition",
     "S003: access to commercial satellite imagery", "high", None,
     "[LC] lần 1 trong câu (suspended access to); lần 2 (portal for access) "
     "không đánh thêm", 1, None, None, "LC", None),
    ("S005", "Global Enhanced GEOINT Delivery system", "L", "synonym",
     "S004: GEGD", "high", "R: the",
     "[LC] viết tắt S004 được mở rộng tên đầy đủ (lần đầu S003 'the Global "
     "Enhanced GEOINT Delivery program'; đổi program → system); 'or GEGD' "
     "trong câu là đồng vị, không đánh thêm", 1, None, None, "LC", None),
    ("S005", "commercial imagery", "L", "repetition",
     "S003: commercial satellite imagery", "high", None,
     "[LC] rút gọn commercial (satellite) imagery; 'the primary portal' là "
     "đồng vị với GEGD trong câu", 1, None, None, "LC", None),

    # S006
    ("S006", "Maxar", "L", "repetition", "S004: Maxar", "high", None,
     "[LC] trong 'Maxar's action' (chiếm hữu cách)", 1, None, None, "LC",
     None),
    ("S006", "action", "L", "general word",
     "S001: it had disabled Ukrainian users' access", "med", None,
     "[LC] danh từ tổng quát tóm chỉ hành động vô hiệu hóa ở S001 ('the "
     "action' S004 là quy chiếu trong câu, không đánh)", 1, None, None,
     "LC", None),

    # S007
    ("S007", "contractual", "L", "repetition",
     "S003: the contract in question", "med", None,
     "[LC] hình vị contract- lặp dưới dạng tính từ", 1, None, None, "LC",
     None),
    # [Phase-2] change ← action (S006): danh từ tổng quát tóm chỉ hành động
    # của Maxar (H&H §6.1); phủ định "no change" tạo phép đối với hành động
    # đã xảy ra (TNT §30 phép đối).
    ("S007", "change", "L", "general word",
     "S006: Maxar's action", "med", None,
     "[LC] danh từ tổng quát: 'no change' đối lập phép đối với hành động "
     "đã nêu ở S006 (TNT §30; H&H §6.1)", 1, None, None, "LC", None),
    # [Phase-2] other — R so sánh (H&H §2.5): "other Maxar customer
    # programs" = khác với GEGD — hợp đồng/chương trình đang nói tới
    # (S003-S005, câu trước) → [LC] quy chiếu so sánh, ref A; VI đối ứng
    # "khác" cũng liên câu (khác P21: EN further nằm cùng câu → [TC]).
    ("S007", "other", "R", "comparative",
     "S003-S005: GEGD (the contract in question)", "high", None,
     "[LC] quy chiếu so sánh: other = khác với GEGD đã nêu ở câu trước "
     "(H&H §2.5)", 1, None, None, "LC", "A"),
    ("S007", "Maxar", "L", "repetition", "S006: Maxar's action", "high",
     None,
     "[LC] trong 'other Maxar customer programs'; 'the company' trong câu "
     "cùng chuỗi, không đánh thêm; 'We/our' trong quote attribution cùng "
     "câu, không đánh", 1, None, None, "LC", None),
    ("S007", "customer", "L", "repetition", "S002: Each customer", "med",
     None, "[LC] lặp customer (định ngữ)", 1, None, None, "LC", None),
    ("S007", "programs", "L", "repetition",
     "S003: a U.S. government program", "med", None,
     "[LC] lặp program — GEGD là một trong các chương trình khách hàng", 1,
     None, None, "LC", None),
    ("S007", "statement", "L", "repetition", "S002: In a statement", "high",
     None, "[LC] công thức attribution lặp", 1, None, None, "LC", None),

    # S008
    ("S008", "Washington", "L", "synonym", "S005: the administration",
     "med", None,
     "[LC] hoán dụ địa danh chỉ chính quyền Mỹ (đối xứng predication S001: "
     "administration suspends intelligence sharing); 'the Trump "
     "administration' trong câu cùng chuỗi, không đánh thêm", 1, None, None,
     "LC", None),
    ("S008", "suspended", "L", "repetition",
     "S005: temporarily suspended", "high", None,
     "[LC] động từ suspend lặp lần 3", 1, None, None, "LC", None),
    ("S008", "intelligence-sharing", "L", "repetition",
     "S001: intelligence sharing", "high", None,
     "[LC] lặp gần nguyên văn, trùng cặp predication với S001", 1, None,
     None, "LC", None),
    ("S008", "Ukraine", "L", "repetition", "S005: support to Ukraine",
     "high", None,
     "[LC] 'Zelenskiy's government' là chính phủ Ukraine (lần đầu), không "
     "thuộc chuỗi chính quyền Mỹ", 1, None, None, "LC", None),
]

TT = [
    # S001 — không có tie: toàn bộ lần đầu; "họ" ← Công ty...Maxar (trong câu).

    # S002
    ("S002", "Maxar", "L", "repetition",
     "S001: Công ty hàng không vũ trụ Mỹ Maxar Technologies", "high", None,
     "[LC] lặp tên riêng; 'họ có những hợp đồng' trong câu không đánh", 1,
     None, None, "LC", None),
    ("S002", "chính phủ Mỹ", "L", "repetition",
     "S001: một nền tảng của chính phủ Mỹ", "high", None,
     "[LC] lặp chính phủ Mỹ (S001 là định ngữ sở hữu)", 1, None, None, "LC",
     None),
    # [Phase-2] sử dụng ← người dùng (S001): lặp gốc dùng/dụng qua đổi
    # loại từ (H&H §6.2 reiteration; TNT §26 phép lặp) — đối xứng EN use ←
    # users; referent khác (người dùng Ukraine ≠ mỗi khách hàng) nên
    # conf med.
    ("S002", "sử dụng", "L", "repetition",
     "S001: người dùng Ukraine", "med", None,
     "[LC] lặp gốc dùng/dụng (người dùng → sử dụng); 'họ' trong quote ← "
     "Mỗi khách hàng cùng câu, không đánh", 1, None, None, "LC", None),
    # [Phase-2] chia sẻ ← chia sẻ thông tin tình báo (S001): mắt xích sót
    # của chuỗi chia sẻ (H&H §6.2; TNT §26); S008 giữ tiền trạm S001 vì
    # trùng cặp predication.
    ("S002", "chia sẻ", "L", "repetition",
     "S001: đình chỉ việc chia sẻ thông tin tình báo", "med", None,
     "[LC] lặp chia sẻ; khách hàng chia sẻ chính là dữ liệu hình ảnh = "
     "nguồn tình báo bị đình chỉ", 1, None, None, "LC", None),
    ("S002", "dữ liệu đó", "R", "demonstrative",
     "S001: hình ảnh vệ tinh", "med", None,
     "[LC] chỉ từ 'đó' truy hồi hình ảnh vệ tinh; 'họ' trong quote ← 'Mỗi "
     "khách hàng' cùng câu, không đánh", 1, None, None, "LC", "A"),

    # S003
    ("S003", "Công ty", "L", "general word", "S002: Maxar", "high", None,
     "[LC] danh từ tổng quát chỉ Maxar", 1, None, None, "LC", None),
    ("S003", "hợp đồng", "L", "repetition",
     "S002: những hợp đồng với chính phủ Mỹ", "high", None,
     "[LC] 'được nói tới' đối ứng EN 'in question'", 1, None, None, "LC",
     None),
    # [Phase-2] GEGD (S003) ← nền tảng (S001): mắt xích được cite ở S004
    # nhưng trước đây không có hàng (bài học P28, nhóm 12); H&H §6.1
    # bridging — GEGD là tên riêng của "một nền tảng của chính phủ Mỹ",
    # nhận diện hồi tố qua S004 "đình chỉ các tài khoản trong GEGD" (=
    # sự kiện S001); "một chương trình của chính phủ Mỹ" là đồng vị trong
    # câu, không đánh thêm.
    ("S003", "GEGD", "L", "general word",
     "S001: một nền tảng của chính phủ Mỹ", "med", None,
     "[LC] đặt tên riêng cho nền tảng đã nêu ở S001 (nhận diện hồi tố; "
     "H&H §6.1 bridging)", 1, None, None, "LC", None),
    ("S003", "chính phủ Mỹ", "L", "repetition", "S002: chính phủ Mỹ", "high",
     None,
     "[LC] định ngữ trong 'một chương trình của chính phủ Mỹ'; 'chương "
     "trình' lặp trong câu với tên GEGD; 'do Mỹ thu thập' cuối câu cùng "
     "chuỗi (đối ứng EN 'the United States') — đều không đánh thêm", 1,
     None, None, "LC", None),
    ("S003", "tiếp cận", "L", "repetition",
     "S001: quyền tiếp cận của người dùng Ukraine", "high", None,
     "[LC] lặp tiếp cận", 1, None, None, "LC", None),
    ("S003", "hình ảnh vệ tinh", "L", "repetition",
     "S001: hình ảnh vệ tinh", "high", None,
     "[LC] thêm định ngữ 'thương mại' (commercial)", 1, None, None, "LC",
     None),
    ("S003", "người dùng", "L", "repetition", "S001: người dùng Ukraine",
     "high", None,
     "[LC] VI tự sinh bổ sung 'cho người dùng' (EN chỉ có 'providing "
     "access', không có users)", 1, None, None, "LC", None),

    # S004
    ("S004", "Chính phủ Hoa Kỳ", "L", "repetition",
     "S003: chính phủ Mỹ", "high", None,
     "[LC] lặp Chính phủ; biến thể Mỹ → Hoa Kỳ; 'Cơ quan Tình báo Địa "
     "không gian Quốc gia Hoa Kỳ' lần đầu không đánh; 'việc này' trong câu "
     "không đánh", 1, None, None, "LC", None),
    # [Phase-2] quyết định ← quyết định (S002): lặp từ vựng (TNT §26 phép
    # lặp; H&H §6.2 reiteration); hai "quyết định" khác referent (khách
    # hàng ≠ chính phủ) nên conf med; neo mắt xích S004 được "chỉ thị"
    # (S005) và C-VI1 cite làm tiền trạm.
    ("S004", "quyết định", "L", "repetition",
     "S002: Mỗi khách hàng tự quyết định", "med", None,
     "[LC] lặp quyết định (tự quyết định → đã quyết định); khác referent: "
     "khách hàng ≠ chính phủ", 1, None, None, "LC", None),
    ("S004", "đình chỉ", "L", "repetition",
     "S001: đình chỉ việc chia sẻ thông tin tình báo", "high", None,
     "[LC] lặp động từ đình chỉ; 'tạm thời' lặp cặp S004-S005 (không đánh "
     "riêng)", 1, None, None, "LC", None),
    ("S004", "tài khoản của Ukraine", "L", "repetition",
     "S001: người dùng Ukraine", "med", None,
     "[LC] lặp Ukraine; đổi đầu từ người dùng → tài khoản", 1, None, None,
     "LC", None),
    ("S004", "GEGD", "L", "repetition",
     "S003: GEGD (chương trình Cung cấp Tình báo Địa lý Cải tiến Toàn "
     "cầu)", "high", None, "[LC] viết tắt lặp", 1, None, None, "LC", None),
    ("S004", "Maxar", "L", "repetition", "S003: Công ty", "high", None,
     "[LC] đặt lại tên sau 'Công ty'", 1, None, None, "LC", None),
    ("S004", None, "E", "nominal", "S004: Maxar (trong câu)", "high", None,
     "[TC] lược chủ ngữ vế tọa hợp sau 'và'; hồi phục {Maxar} (EN dùng "
     "participle 'referring')", 1, "và ", "{Maxar}", "TC", None),

    # S005
    ("S005", "Tuân theo", "C", "causal",
     "S004: Chính phủ Hoa Kỳ đã quyết định tạm thời đình chỉ các tài khoản "
     "của Ukraine", "med", None,
     "[LC] nối nhân-quả: hành động của cơ quan tuân theo quyết định S004; "
     "'chỉ thị' truy hồi 'đã quyết định'", 1, None, None, "LC", None),
    # [Phase-2] chỉ thị ← quyết định (S004): danh từ tổng quát đổi tên quyết
    # định đã nêu (H&H §6.1 general word; mapping §3.6) — VI không có mạo
    # từ, định danh bằng ngữ cảnh (mapping §4); trước đây §6 liệt vào
    # "không đánh" — Phase-2 nhóm 3 điều chỉnh; tách khỏi hàng C "Tuân
    # theo" (khác hình thức, khác quan hệ).
    ("S005", "chỉ thị", "L", "general word",
     "S004: đã quyết định tạm thời đình chỉ các tài khoản của Ukraine",
     "med", None,
     "[LC] danh từ tổng quát tóm chỉ quyết định của chính quyền ở S004 "
     "(H&H §6.1); khác hình thức với hàng C cùng câu", 1, None, None, "LC",
     None),
    ("S005", "chính quyền", "L", "synonym",
     "S004: Chính phủ Hoa Kỳ", "med", None,
     "[LC] chính quyền ≈ chính phủ — cùng thực thể (lần đầu: S001 'chính "
     "quyền của Tổng thống Mỹ Donald Trump'); 'chính phủ Hoa Kỳ' cuối câu "
     "cùng chuỗi, không đánh thêm", 1, None, None, "LC", None),
    ("S005", "Ukraine", "L", "repetition", "S004: tài khoản của Ukraine",
     "high", None, "[LC] lặp Ukraine", 1, None, None, "LC", None),
    ("S005", "Cơ quan Tình báo Địa không gian Quốc gia Hoa Kỳ", "L",
     "repetition",
     "S004: Cơ quan Tình báo Địa không gian Quốc gia Hoa Kỳ", "high", None,
     "[LC] lặp nguyên văn tên đầy đủ (EN nén thành viết tắt NGA); 'cơ quan "
     "này' trong câu (phát ngôn viên của cơ quan này) quy chiếu trong câu, "
     "không đánh", 1, None, None, "LC", None),
    ("S005", "đình chỉ", "L", "repetition", "S004: đình chỉ", "high", None,
     "[LC] lặp động từ đình chỉ", 1, None, None, "LC", None),
    ("S005", "tiếp cận", "L", "repetition",
     "S003: tiếp cận hình ảnh vệ tinh thương mại", "high", None,
     "[LC] lần 1 trong câu (khả năng tiếp cận); lần 2 (để tiếp cận hình "
     "ảnh) không đánh thêm", 1, None, None, "LC", None),
    ("S005", "hệ thống Cung cấp Tình báo Địa lý Cải tiến Toàn cầu", "L",
     "synonym", "S004: GEGD", "high", None,
     "[LC] viết tắt S004 được mở rộng tên dịch đầy đủ (lần đầu S003 "
     "'chương trình Cung cấp Tình báo Địa lý Cải tiến Toàn cầu'; đổi "
     "chương trình → hệ thống); 'hay GEGD' trong câu là đồng vị, không "
     "đánh thêm", 1, None, None, "LC", None),
    ("S005", "hình ảnh thương mại", "L", "repetition",
     "S003: hình ảnh vệ tinh thương mại", "high", None,
     "[LC] rút gọn bỏ 'vệ tinh' — đối xứng EN commercial imagery; 'cổng "
     "chính' là đồng vị với GEGD trong câu", 1, None, None, "LC", None),

    # S006
    ("S006", "Maxar", "L", "repetition", "S004: Maxar", "high", None,
     "[LC] trong 'Hành động của Maxar'", 1, None, None, "LC", None),
    ("S006", "Hành động", "L", "general word",
     "S001: vô hiệu hóa quyền tiếp cận của người dùng Ukraine", "med", None,
     "[LC] danh từ tổng quát tóm chỉ hành động ở S001 ('việc này' S004 là "
     "quy chiếu trong câu, không đánh)", 1, None, None, "LC", None),

    # S007
    ("S007", "hợp đồng", "L", "repetition",
     "S003: hợp đồng được nói tới", "high", None,
     "[LC] trong 'cam kết theo hợp đồng của mình' (EN dùng tính từ "
     "contractual); 'Chúng tôi/mình' trong quote attribution cùng câu, "
     "không đánh", 1, None, None, "LC", None),
    # [Phase-2] thay đổi ← Hành động (S006): danh từ tổng quát tóm chỉ tình
    # huống câu trước (H&H §6.1); phủ định "không có thay đổi nào" tạo
    # phép đối với hành động đã xảy ra (TNT §30 phép đối) — đối xứng EN
    # change.
    ("S007", "thay đổi", "L", "general word",
     "S006: Hành động của Maxar", "med", None,
     "[LC] danh từ tổng quát: 'không có thay đổi nào' đối lập phép đối "
     "với hành động ở S006 (TNT §30; H&H §6.1)", 1, None, None, "LC",
     None),
    ("S007", "chương trình", "L", "repetition",
     "S003: một chương trình của chính phủ Mỹ", "med", None,
     "[LC] trong 'các chương trình khách hàng khác'", 1, None, None, "LC",
     None),
    ("S007", "khách hàng", "L", "repetition", "S002: Mỗi khách hàng", "med",
     None, "[LC] lặp khách hàng (định ngữ)", 1, None, None, "LC", None),
    # [Phase-2] khác — R so sánh (H&H §2.5): "các chương trình khách hàng
    # khác" = khác với GEGD đang nói tới (S003-S005, câu trước) → [LC],
    # ref A; đối xứng EN other. BẪY chuỗi con: "khác" lần 1 nằm TRONG
    # "khách" (khách hàng), lần 2 mới là từ độc lập → occ=2 (tiền lệ P26,
    # ghi chú vị trí).
    ("S007", "khác", "R", "comparative",
     "S003-S005: GEGD (hợp đồng được nói tới)", "high", None,
     "[LC] quy chiếu so sánh: khác = khác với GEGD ở câu trước (H&H §2.5); "
     "occ=2 vì lần 1 là chuỗi con trong 'khách'", 2, None, None, "LC",
     "A"),
    ("S007", "Maxar", "L", "repetition", "S006: Maxar", "high", None,
     "[LC] trong 'các chương trình khách hàng khác của Maxar'; 'công ty' "
     "trong câu cùng chuỗi, không đánh thêm", 1, None, None, "LC", None),
    ("S007", "phát biểu", "L", "repetition",
     "S002: Trong một phát biểu", "high", None,
     "[LC] công thức attribution lặp", 1, None, None, "LC", None),

    # S008
    ("S008", "Washington", "L", "synonym", "S005: chính quyền", "med", None,
     "[LC] hoán dụ địa danh chỉ chính quyền Mỹ; 'chính quyền Trump' trong "
     "câu cùng chuỗi, không đánh thêm", 1, None, None, "LC", None),
    ("S008", "đình chỉ", "L", "repetition", "S005: đình chỉ", "high", None,
     "[LC] động từ đình chỉ lặp lần 3", 1, None, None, "LC", None),
    ("S008", "chia sẻ thông tin tình báo", "L", "repetition",
     "S001: đình chỉ việc chia sẻ thông tin tình báo với Kyiv", "high",
     None, "[LC] lặp gần nguyên văn, trùng cặp predication S001", 1, None,
     None, "LC", None),
    ("S008", "Ukraine", "L", "repetition", "S005: hỗ trợ Ukraine", "high",
     None,
     "[LC] 'chính phủ của Tổng thống Volodymyr Zelenskyy' là chính phủ "
     "Ukraine (lần đầu), không thuộc chuỗi chính quyền Mỹ; 'họ' trong câu "
     "quy chiếu chính phủ này, không đánh", 1, None, None, "LC", None),
]
