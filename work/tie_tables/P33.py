# P33 tie table — WRITTEN BY HAND FROM work/analysis/P33_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Text/gap_after là chuỗi con nguyên văn trong câu (kiểm bằng pipeline.locate).
# KHỐI CẮT VI (tie chỉ phía EN): S012–S013, S021–S022, S029–S031, S042–S045.
# VI gộp: S007+S008→TT S007; S034+S035+S036→TT S028; VI tự sinh TT S015.
# Tiểu đề (S023 EN; S004/S019 TT) không gán nhãn.

ST = [
    # S002
    ("S002", "And", "C", "additive",
     "S001: trend đồ uống trên mạng xã hội", "high", None,
     "VI dồn dẫn nhập nên không có C phía VI", 1, None, None, "LC", None),
    ("S002", "this sweet caffeinated beverage", "R", "demonstrative",
     "S001: how to customize your Starbucks order — Vietnamese iced coffee",
     "high", None,
     "chỉ từ hồi quy về loại đồ uống vừa kể; phần VI tương ứng bị cắt",
     1, None, None, "LC", "A"),
    # S003
    ("S003", "Vietnamese coffee", "L", "repetition",
     "S001: a Vietnamese iced coffee", "high", None,
     "a base of Vietnamese coffee", 1, None, None, "LC", None),
    ("S003", "this now-popular beverage", "R", "demonstrative",
     "S002: salt coffee, or ca phe muoi", "high", None,
     "VI đối ứng 'loại đồ uống' không có chỉ từ → chỉ còn L phía VI", 1,
     None, None, "LC", "A"),
    # S004
    ("S004", "The mixture", "R", "nominal",
     "S003: adding sweetened condensed milk to a base of Vietnamese coffee",
     "high", None, "danh ngữ tóm chỉ hỗn hợp vừa mô tả", 1, None, None,
     "LC", "A"),
    ("S004", "salted cream", "L", "repetition",
     "S002: salt coffee", "high", None, "hình vị 'salt' trong 'salted'",
     1, None, None, "LC", None),
    # S005
    ("S005", "We", "R", "personal",
     "hai chủ quán Ca Phe Muoi (ngoại văn bản — quote)", "med", None,
     "ngoại quy chiếu; 'we' viết thường lần 2 trong quote cùng chuỗi, "
     "không đánh", 1, None, None, "LC", "E"),
    ("S005", "salt coffee", "L", "repetition",
     "S002: salt coffee", "high", None, None, 1, None, None, "LC", None),
    ("S005", "Ca Phe Muoi", "L", "repetition",
     "S002: ca phe muoi", "high", None,
     "tên quán viết hoa; 'coffee shop' từ mới", 1, None, None, "LC",
     None),
    # S006
    ("S006", "This combination", "R", "demonstrative",
     "S005: công thức salt coffee (2010)", "high", None,
     "dấu ngoặc biên tập '(creates a)' của nguồn, ghi §8", 1, None,
     None, "LC", "A"),
    ("S006", "condensed milk", "L", "repetition",
     "S003: sweetened condensed milk", "high", None,
     "occ 1: lần 2 ('the condensed milk') trong câu cùng chuỗi, không đánh",
     1, None, None, "LC", None),
    ("S006", "salt", "L", "repetition", "S002: salt coffee", "high",
     None, None, 1, None, None, "LC", None),
    ("S006", "the coffee", "L", "repetition",
     "S003: a base of Vietnamese coffee", "high", None, None, 1, None,
     None, "LC", None),
    ("S006", "creamy mixture", "L", "repetition", "S004: The mixture",
     "high", None, None, 1, None, None, "LC", None),
    ("S006", "sweetness", "L", "repetition",
     "S003: sweetened condensed milk", "med", None,
     "hình vị sweet lặp (sweet→sweetened→sweetness)", 1, None, None,
     "LC", None),
    # S007
    ("S007", "the cafe", "L", "repetition",
     "S003: A small, no-frills café", "high", None,
     "nguồn đổi chính tả café→cafe, ghi §8", 1, None, None, "LC", None),
    ("S007", "now-famous", "L", "repetition",
     "S003: this now-popular beverage", "med", None,
     "lặp tiền tố 'now-'; 'drink' từ mới khởi tạo chuỗi đồ uống", 1,
     None, None, "LC", None),
    # S008
    ("S008", "Ca phe", "L", "repetition", "S005: Ca Phe Muoi", "high",
     None, "gloss từ Việt không dấu của nguồn", 1, None, None, "LC",
     None),
    ("S008", "coffee", "L", "repetition",
     "S006: the bitterness of the coffee", "high", None, None, 1, None,
     None, "LC", None),
    ("S008", "muoi", "L", "repetition", "S006: salt", "high", None,
     "gloss từ Việt", 1, None, None, "LC", None),
    ("S008", "salt", "L", "repetition", "S006: salt", "high", None,
     None, 1, None, None, "LC", None),
    ("S008", "Vietnamese", "L", "repetition",
     "S003: Vietnamese coffee", "high", None, None, 1, None, None,
     "LC", None),
    # S009
    ("S009", "We", "R", "personal",
     "hai chủ quán (ngoại văn bản — quote)", "med", None,
     "ngoại quy chiếu; 'we' viết thường lần 2,3 trong quote không đánh",
     1, None, None, "LC", "E"),
    ("S009", "this name", "R", "demonstrative",
     "S007: The name of the cafe and now-famous drink", "high", None,
     "phần VI tương ứng bị cắt", 1, None, None, "LC", "A"),
    ("S009", "black coffee", "L", "repetition", "S006: black coffee",
     "high", None, "chỉ giữ phía EN (VI cắt nửa đầu câu)", 1, None,
     None, "LC", None),
    ("S009", "coffee shop", "L", "repetition",
     "S005: Ca Phe Muoi coffee shop", "high", None,
     "'attract' lặp 2 lần trong câu (TC) không đánh", 1, None, None,
     "LC", None),
    ("S009", "salt coffee", "L", "repetition", "S005: salt coffee",
     "high", None, None, 1, None, None, "LC", None),
    ("S009", "the couple", "R", "nominal",
     "S005: co-owners Ho Thi Thanh Huong and Tran Nguyen Huu Phong",
     "high", None, "danh ngữ tóm chỉ hai chủ", 1, None, None, "LC",
     "A"),
    # S010
    ("S010", "The strategy", "R", "nominal",
     "S009: làm khác để thu hút khách rồi giữ chân họ", "high", None,
     "VI đối ứng 'Chiến lược này' là chỉ từ (R demonstrative)", 1, None,
     None, "LC", "A"),
    # S011 — [Phase-2] drinking ← drink (S007): động từ hóa chuỗi drink (H&H
    # §6.2 reiteration; TNT §26 phép lặp từ vựng) — S011 trước đây 0 hàng.
    ("S011", "drinking", "L", "repetition",
     "S007: now-famous drink (chuỗi drink)", "med", None,
     "lặp hình vị drink ở dạng động từ (what they were drinking); 'they' "
     "trong câu chỉ locals and tourists (TC) không đánh", 1, None, None,
     "LC", None),
    # S012 — KHỐI CẮT (VI none)
    ("S012", "Hue", "L", "repetition",
     "S003: Vietnam's historical city of Hue", "high", None,
     "khối cắt, VI none", 1, None, None, "LC", None),
    ("S012", "black coffee", "L", "repetition", "S009: black coffee",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S012", "condensed milk", "L", "repetition", "S006: condensed milk",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S012", "salty coffee", "L", "repetition",
     "S009: the salt coffee taste", "high", None,
     "salt → salty biến thể hình thái; khối cắt, VI none", 1, None,
     None, "LC", None),
    ("S012", "they add", "R", "personal", "S009: the couple", "high",
     None,
     "'they' lần 1 trong câu chỉ people (hư chỉ), không đánh; khối cắt",
     1, None, None, "LC", "A"),
    # [Phase-2] a strange drink ← drink (S007/S011): chuỗi drink (H&H §6.2
    # reiteration); được hàng R "this strange drink" (S013) cite làm tiền
    # trạm — nhóm 12 protocol.
    ("S012", "a strange drink", "L", "repetition",
     "S011: drinking (chuỗi drink S007: now-famous drink)", "high", None,
     "khối cắt, VI none; a strange drink = cà phê muối", 1, None, None,
     "LC", None),
    # [Phase-2] sugar ← sugar (S009): lặp công thức "black coffee + sugar
    # or milk" (H&H §6.2; cấu trúc song song TNT §30 phép đối).
    ("S012", "sugar", "L", "repetition", "S009: with sugar or milk", "high",
     None, "khối cắt, VI none; 'milk' thường (S009) khác 'condensed "
     "milk' nên không đánh", 1, None, None, "LC", None),
    # S013 — KHỐI CẮT
    ("S013", "We", "R", "personal",
     "hai chủ quán (ngoại văn bản — quote)", "med", None,
     "khối cắt, VI none", 1, None, None, "LC", "E"),
    ("S013", "customers", "L", "repetition",
     "S009: attract the customers", "high", None,
     "our first customers; khối cắt, VI none", 1, None, None, "LC",
     None),
    ("S013", "this strange drink", "R", "demonstrative",
     "S012: a strange drink", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", "A"),
    # S014
    ("S014", "salt coffee", "L", "repetition",
     "S012: salty coffee", "high", None,
     "'it' trong câu chỉ salt coffee (trong câu), không đánh", 1, None,
     None, "LC", None),
    ("S014", "historic Hue", "L", "repetition",
     "S003: Vietnam's historical city of Hue", "high", None,
     "lặp 'Hue' + hình vị historic(al)", 1, None, None, "LC", None),
    ("S014", "cafes", "L", "repetition", "S007: the cafe", "high",
     None, None, 1, None, None, "LC", None),
    ("S014", "Vietnam", "L", "repetition",
     "S012: Hue people — như S003: Vietnam's historical city", "high",
     None,
     "around Vietnam; VI 'Việt Nam' lần đầu xuất hiện nên không có hàng",
     1, None, None, "LC", None),
    # [Phase-2] a specialty drink ← this strange drink (S013): chuỗi drink
    # (H&H §6.2); 'specialty' mở chuỗi đặc sản được "a Hue specialty"
    # (S045) cite — nhóm 12 protocol.
    ("S014", "a specialty drink", "L", "repetition",
     "S013: this strange drink", "high", None,
     "lặp danh từ drink; VI S011 đối ứng 'thức uống đặc sản' có hàng "
     "Phase-2 riêng", 1, None, None, "LC", None),
    # S015
    ("S015", "salt coffee", "L", "repetition", "S014: salt coffee",
     "high", None, None, 1, None, None, "LC", None),
    ("S015", "trend", "L", "repetition", "S001: a popular beverage "
     "trend", "high", None, None, 1, None, None, "LC", None),
    ("S015", "Vietnam", "L", "repetition", "S014: around Vietnam",
     "high", None, None, 1, None, None, "LC", None),
    ("S015", "Ca Phe Muoi", "L", "repetition", "S005: Ca Phe Muoi",
     "high", None, "the Ca Phe Muoi founders", 1, None, None, "LC",
     None),
    # [Phase-2] founders ← co-owners (S005): đồng nghĩa chỉ cặp chủ quán (H&H
    # §6.2 synonym; TNT §31 phép thế đẳng nghĩa) — chuỗi khác với chuỗi tên
    # quán nên có hàng riêng.
    ("S015", "founders", "L", "synonym",
     "S005: co-owners Ho Thi Thanh Huong and Tran Nguyen Huu Phong",
     "high", None,
     "đổi danh hiệu cặp chủ (the Ca Phe Muoi founders); VI S012 đối ứng "
     "'người sáng lập' ← 'đồng sở hữu'", 1, None, None, "LC", None),
    # S016
    ("S016", "Hue", "L", "repetition", "S014: historic Hue", "high",
     None, None, 1, None, None, "LC", None),
    ("S016", "salt coffee", "L", "repetition", "S015: salt coffee",
     "high", None, None, 1, None, None, "LC", None),
    ("S016", "black coffee", "L", "repetition", "S012: black coffee",
     "high", None,
     "'white coffee' từ mới, không đánh; 'so' trong câu không đánh C",
     1, None, None, "LC", None),
    ("S016", "this trend", "R", "demonstrative",
     "S015: a trend across Vietnam", "high", None, None, 1, None,
     None, "LC", "A"),
    ("S016", "our", "R", "personal",
     "chủ quán (ngoại văn bản — quote)", "med", None,
     "our business — ngoại quy chiếu", 1, None, None, "LC", "E"),
    # [Phase-2] a daily drink ← a specialty drink (S014): chuỗi drink (H&H
    # §6.2); được "a drink" (S045) cite làm tiền trạm — nhóm 12 protocol.
    ("S016", "a daily drink", "L", "repetition",
     "S014: a specialty drink", "high", None,
     "lặp danh từ drink; 'like black coffee or white coffee' so sánh "
     "trong câu (TC) không đánh", 1, None, None, "LC", None),
    # S017
    ("S017", "the café", "L", "repetition", "S007: the cafe", "high",
     None, "'its' trong câu không đánh", 1, None, None, "LC", None),
    ("S017", "salt coffee", "L", "repetition", "S016: salt coffee",
     "high", None, "VI bỏ 'salt coffee' — chỉ EN có hàng", 1, None,
     None, "LC", None),
    ("S017", "Vietnamese", "L", "repetition", "S008: Vietnamese",
     "high", None, "other Vietnamese cities", 1, None, None, "LC",
     None),
    # [Phase-2] Today ← (mạch hồi tưởng 2010–Covid): continuative (H&H §5.8 —
    # P21 precedent "Now," → continuative): mở khung discours về hiện tại,
    # không nối sự kiện trong thế giới.
    ("S017", "Today", "C", "continuative",
     "S016: quote xu hướng sau Covid (chuyển khung về hiện tại)", "med",
     None,
     "H&H §5.8 continuative; VI S014 đối ứng 'Ngày nay' có hàng riêng", 1,
     None, None, "LC", None),
    # [Phase-2] other ← In Hue (S016): quy chiếu so sánh (H&H §2.5 "other")
    # — "other Vietnamese cities" = các thành phố khác, không kể Huế.
    ("S017", "other", "R", "comparative",
     "S016: In Hue", "high", None,
     "[LC] quy chiếu so sánh: other = khác với Huế (thành phố của quán); "
     "'as well' cuối câu cùng phép bổ sung, không đánh thêm; VI bỏ "
     "comparative ('bán khắp nơi Việt Nam') — dịch chuyển R→zero (NTT "
     "2020 §5)", 1, None, None, "LC", "A"),
    # S018
    ("S018", "the name", "R", "nominal",
     "S007: The name of the cafe and now-famous drink", "high", None,
     "VI đối ứng 'cái tên' chỉ là lặp từ (L)", 1, None, None, "LC",
     "A"),
    ("S018", "the flavors", "L", "repetition",
     "S013: perfected the flavors", "high", None,
     "chuỗi từ câu bị cắt S013 — VI không có đối ứng", 1, None, None,
     "LC", None),
    # S019
    ("S019", "The sweetened milk", "L", "repetition",
     "S006: condensed milk", "high", None,
     "dạng rút gọn của 'sweetened condensed milk' (S003)", 1, None,
     None, "LC", None),
    ("S019", "cream", "L", "repetition", "S004: salted cream", "high",
     None, None, 1, None, None, "LC", None),
    ("S019", "balances", "L", "repetition",
     "S006: balances the sweetness", "high", None, None, 1, None,
     None, "LC", None),
    ("S019", "the bitterness of the coffee", "L", "repetition",
     "S006: softens the bitterness of the coffee", "high", None,
     "kết 2 chuỗi bitterness + coffee", 1, None, None, "LC", None),
    ("S019", "salt", "L", "repetition", "S016: this trend — chuỗi muối "
     "S008", "high", None,
     "occ 1: lần 2 nằm trong 'salted caramel' (hàng riêng)", 1, None,
     None, "LC", None),
    ("S019", "the sweetness", "L", "repetition",
     "S006: the sweetness of the condensed milk", "high", None, None, 1,
     None, None, "LC", None),
    ("S019", "salted caramel", "L", "repetition",
     "S004: salted cream", "high", None, "lặp 'salted'", 1, None, None,
     "LC", None),
    ("S019", "caramel flavors", "L", "repetition",
     "S018: the flavors", "high", None, None, 1, None, None, "LC",
     None),
    # S020
    ("S020", "Starbucks", "L", "repetition",
     "S001: your Starbucks order", "high", None,
     "'their' trong câu không đánh", 1, None, None, "LC", None),
    ("S020", "Vietnam", "L", "repetition", "S015: across Vietnam",
     "high", None, None, 1, None, None, "LC", None),
    ("S020", "salt coffee", "L", "repetition", "S017: salt coffee",
     "high", None, "the salt coffee wave", 1, None, None, "LC", None),
    ("S020", "ca phe muoi", "L", "repetition",
     "S002: ca phe muoi", "high", None,
     "VI gộp vào 'cà phê muối' occ-note nên chỉ EN có hàng riêng", 1,
     None, None, "LC", None),
    # [Phase-2] Even ← cafes around Vietnam began serving it (S014): additive
    # (H&H §5.4) — bổ sung trường hợp cực đoan (Starbucks) vào tập quán đã
    # phục vụ cà phê muối.
    ("S020", "Even", "C", "additive",
     "S014: cafes around Vietnam began serving it as well", "med", None,
     "ngay cả Starbucks cũng theo làn sóng; VI S018 đối ứng 'Ngay cả... "
     "cũng'", 1, None, None, "LC", None),
    # [Phase-2] wave ← this trend (S016): đồng nghĩa ẩn dụ (H&H §6.2
    # synonym) — "the salt coffee wave" tiếp chuỗi trend; "their own
    # version" là danh từ quan hệ, không đánh.
    ("S020", "wave", "L", "synonym", "S016: this trend", "high",
     None,
     "wave ≈ trend (ẩn dụ 'sóng'); VI S018 đối ứng 'làn sóng' có hàng "
     "riêng", 1, None, None, "LC", None),
    # S021 — KHỐI CẮT
    ("S021", "Vietnam", "L", "repetition", "S020: in Vietnam", "high",
     None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S021", "salt", "L", "repetition", "S019: salt", "high", None,
     "khối cắt, VI none", 1, None, None, "LC", None),
    ("S021", "coffee", "L", "repetition",
     "S019: the bitterness of the coffee", "high", None,
     "'its' trong câu không đánh; khối cắt", 1, None, None, "LC",
     None),
    # S022 — KHỐI CẮT
    ("S022", "it", "R", "personal", "S021: adds salt to its coffee",
     "high", None,
     "khối cắt, VI none; 'we/our' hư chỉ phổ quát, không đánh", 1, None,
     None, "LC", "A"),
    ("S022", "the bitterness", "L", "repetition",
     "S019: the bitterness of the coffee", "high", None,
     "khối cắt, VI none", 1, None, None, "LC", None),
    ("S022", "heighten", "L", "repetition",
     "S019: salt heightens the sweetness", "high", None,
     "heightens → heighten; khối cắt", 1, None, None, "LC", None),
    ("S022", "the flavors", "L", "repetition", "S019: caramel flavors",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    # [Phase-2] the tradition ← adds salt to its coffee (S021): danh từ tổng
    # quát bridging (H&H §6.1 general noun) — tóm thói quen thêm muối vừa
    # nêu; mạo từ the mang định danh (mapping §3.6).
    ("S022", "the tradition", "L", "general word",
     "S021: adds salt to its coffee", "med", "R: the",
     "khối cắt, VI none; danh từ tổng quát chỉ thực hành thêm muối", 1,
     None, None, "LC", None),
    # [Phase-2] countries ← the only country (S021): lặp hình vị country với
    # số nhiều phổ quát (H&H §6.2; precedent P21 "companies") — referent
    # đổi (Turkey, Hungary, Siberia) nhưng giữ chuỗi.
    ("S022", "countries", "L", "repetition",
     "S021: the only country", "med", None,
     "khối cắt, VI none; số nhiều phổ quát sau số ít định danh", 1, None,
     None, "LC", None),
    # S024
    ("S024", "Vietnam", "L", "repetition", "S021: Vietnam", "high",
     None, None, 1, None, None, "LC", None),
    ("S024", "coffee", "L", "repetition", "S021: its coffee", "high",
     None, "exporter of coffee", 1, None, None, "LC", None),
    # S025
    ("S025", "The country’s", "R", "general noun",
     "S024: Vietnam", "high", None,
     "danh từ tổng chỉ + đồng thời lặp 'country' (S021), ghi note", 1,
     None, None, "LC", "A"),
    ("S025", "coffee", "L", "repetition", "S024: exporter of coffee",
     "high", None, "coffee exports", 1, None, None, "LC", None),
    # [Phase-2] exports ← exporter (S024): lặp hình vị export (H&H §6.2; TNT
    # §26) — "coffee exports" đối xứng VI "xuất khẩu cà phê" (S021).
    ("S025", "exports", "L", "repetition",
     "S024: second-largest exporter of coffee", "high", None,
     "exporter → exports (danh hóa cùng hình vị)", 1, None, None, "LC",
     None),
    # S026
    ("S026", "salt coffee", "L", "repetition", "S020: salt coffee",
     "high", None,
     "'That' chủ ngữ mệnh đề đặt trước, không hồi quy — không đánh",
     1, None, None, "LC", None),
    ("S026", "cafes", "L", "repetition", "S014: cafes", "high", None,
     None, 1, None, None, "LC", None),
    ("S026", "Hue", "L", "repetition", "S016: In Hue", "high", None,
     None, 1, None, None, "LC", None),
    ("S026", "Vietnam", "L", "repetition", "S025: The country's",
     "high", None, None, 1, None, None, "LC", None),
    # S027
    ("S027", "coffee", "L", "repetition", "S026: salt coffee", "high",
     None, None, 1, None, None, "LC", None),
    ("S027", "the country", "R", "general noun",
     "S026: across Vietnam", "high", None,
     "lặp 'country' (S025) + quy chiếu Việt Nam", 1, None, None, "LC",
     "A"),
    # [Phase-2] popular ← now-famous (S007): tiếp chuỗi popular (S003
    # now-popular → S007 now-famous → S027 extremely popular) — H&H §6.2
    # synonym; "ubiquitous/common" (S026) mỗi từ chỉ xuất hiện một lần nên
    # không đánh.
    ("S027", "popular", "L", "synonym", "S007: now-famous drink", "med",
     None,
     "famous ≈ popular; VI đối ứng chuỗi 'phổ biến' (S002, S022, S023)", 1,
     None, None, "LC", None),
    # S028
    ("S028", "Coffee outlets", "L", "repetition",
     "S024: exporter of coffee", "high", None, None, 1, None, None,
     "LC", None),
    ("S028", "cafes", "L", "repetition", "S026: cafes", "high", None,
     None, 1, None, None, "LC", None),
    # S029 — KHỐI CẮT (ghi chú biên tập "(Read more…)")
    ("S029", "Vietnam’s", "L", "repetition", "S027: the country",
     "high", None, "câu chú thích biên tập; khối cắt, VI none", 1,
     None, None, "LC", None),
    ("S029", "coffee", "L", "repetition", "S028: Coffee outlets",
     "high", None, "coffee culture; khối cắt, VI none", 1, None, None,
     "LC", None),
    # S030 — KHỐI CẮT
    ("S030", "Vietnamese coffee", "L", "repetition",
     "S029: coffee culture — chuỗi Vietnamese (S020)", "high", None,
     "khối cắt, VI none", 1, None, None, "LC", None),
    ("S030", "brewed", "L", "repetition", "S022: our brews", "med",
     None,
     "brews → brewed; 'brewing device' lần 2 trong câu (TC) không đánh; "
     "khối cắt", 1, None, None, "LC", None),
    # S031 — KHỐI CẮT
    ("S031", "sweetened condensed milk", "L", "repetition",
     "S019: The sweetened milk", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", None),
    ("S031", "brew", "L", "repetition", "S030: brewed in a phin",
     "high", None, "the strong brew; khối cắt", 1, None, None, "LC",
     None),
    # S032
    ("S032", "And", "C", "additive",
     "S031: stir sweetened condensed milk into the brew", "high", None,
     "VI mở câu mới không có And (khối S029–S031 bị cắt)", 1, None,
     None, "LC", None),
    ("S032", "salt coffee", "L", "repetition", "S026: salt coffee",
     "high", None, "'them' trong câu không đánh", 1, None, None, "LC",
     None),
    ("S032", "Vietnamese coffee", "L", "repetition",
     "S030: Traditional Vietnamese coffee", "high", None,
     "kết chuỗi Vietnamese + coffee", 1, None, None, "LC", None),
    # [Phase-2] drinks ← a daily drink (S016): chuỗi drink (H&H §6.2); được
    # "them all" (S033) cite làm tiền trạm — nhóm 12 protocol.
    ("S032", "drinks", "L", "repetition", "S016: a daily drink", "high",
     None,
     "đầu từ drinks của 'Vietnamese coffee drinks'; 'them' trong câu "
     "(TC) không đánh", 1, None, None, "LC", None),
    # S033
    ("S033", "them all", "R", "personal",
     "S032: several distinctive Vietnamese coffee drinks", "high",
     None,
     "'this dessert-like recipe' trong câu chỉ egg coffee, không đánh",
     1, None, None, "LC", "A"),
    ("S033", "condensed milk", "L", "repetition",
     "S031: sweetened condensed milk", "high", None, None, 1, None,
     None, "LC", None),
    ("S033", "coffee base", "L", "repetition", "S032: Vietnamese "
     "coffee drinks", "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] Invented ← inventing (S003): lặp động từ (H&H §6.2; TNT §26)
    # — phép đối ngầm: cà phê muối phát minh ở Huế ↔ cà phê trứng phát
    # minh ở Hà Nội (TNT §30).
    ("S033", "Invented", "L", "repetition",
     "S003: widely credited with inventing this now-popular beverage",
     "high", None,
     "động từ invent lặp (inventing → Invented); VI S027 đối ứng 'phát "
     "minh' ← S002 'phát minh ra'", 1, None, None, "LC", None),
    # [Phase-2] famous ← now-famous (S007): chuỗi famous (H&H §6.2) — "the
    # most famous of them all"; VI S026 đối ứng "nổi tiếng nhất".
    ("S033", "famous", "L", "repetition", "S007: now-famous drink",
     "high", None, "lặp tính từ famous (most famous)", 1, None, None,
     "LC", None),
    # S034
    ("S034", "And then", "C", "additive",
     "S033: egg coffee", "high", None,
     "VI gộp 3 câu đồ uống thành 1 (S028) vẫn giữ 'Và sau đó'", 1,
     None, None, "LC", None),
    ("S034", "coffee blended", "L", "repetition",
     "S033: a coffee base", "high", None,
     "'coconut milk' vật liệu mới, không đánh", 1, None, None, "LC",
     None),
    # S035
    ("S035", "ca phe", "L", "repetition", "S020: ca phe muoi", "high",
     None, "sinh to ca phe — gloss từ Việt", 1, None, None, "LC",
     None),
    ("S035", "coffee is combined", "L", "repetition",
     "S034: coffee blended", "high", None, None, 1, None, None, "LC",
     None),
    # S036
    ("S036", "And finally", "C", "additive",
     "S035: fruit shake coffee", "high", None,
     "VI gộp nên mất C riêng — chỉ EN có hàng", 1, None, None, "LC",
     None),
    ("S036", "ca phe", "L", "repetition", "S035: sinh to ca phe",
     "high", None,
     "sua chua ca phe — gloss (nguồn có ký tự vô hình sau 'phe', ghi §8)",
     1, None, None, "LC", None),
    ("S036", "black coffee", "L", "repetition", "S016: black coffee",
     "high", None, None, 1, None, None, "LC", None),
    ("S036", "creamy", "L", "repetition", "S006: creamy mixture",
     "med", None, "hình vị creamy lặp", 1, None, None, "LC", None),
    ("S036", "Vietnamese", "L", "repetition",
     "S032: Vietnamese coffee", "high", None,
     "creamy Vietnamese yogurt", 1, None, None, "LC", None),
    ("S036", "French legacy", "L", "repetition",
     "S027: French colonists", "high", None,
     "'another' nhắc lại di sản thuộc địa", 1, None, None, "LC",
     None),
    # S037
    ("S037", "these novel coffee experiences and flavors", "R",
     "demonstrative",
     "S032–S036: các thức uống cà phê đặc sản vừa kể", "high", None,
     "hậu chỉ từ; bên trong lặp chuỗi coffee (S036) + flavors (S022), "
     "ghi note", 1, None, None, "LC", "A"),
    # S038
    ("S038", "Mintel", "L", "repetition",
     "S037: global market research agency Mintel", "high", None,
     "'they' trong câu không đánh", 1, None, None, "LC", None),
    ("S038", "consumers", "L", "repetition",
     "S037: consumers outside Asia", "high", None, None, 1, None,
     None, "LC", None),
    ("S038", "coffee drinks", "L", "repetition",
     "S037: these novel coffee experiences", "high", None,
     "lặp 'coffee'", 1, None, None, "LC", None),
    ("S038", "Vietnamese coffee", "L", "repetition",
     "S032: Vietnamese coffee drinks", "high", None, None, 1, None,
     None, "LC", None),
    # [Phase-2] interested ← interested (S037): lặp tính từ (H&H §6.2) —
    # phát hiện khảo sát được nhắc lại ở câu số liệu; VI S030 đối ứng
    # "quan tâm" ← S029.
    ("S038", "interested", "L", "repetition",
     "S037: increasingly interested in these novel coffee experiences",
     "high", None, "lặp interested (were interested in trying)", 1, None,
     None, "LC", None),
    # S039
    ("S039", "In the US", "L", "repetition", "S038: Mintel in the US",
     "high", None,
     "'across the country' trong câu chỉ Mỹ, không đánh", 1, None,
     None, "LC", None),
    ("S039", "a café chain", "L", "repetition", "S028: cafes", "high",
     None,
     "'first café' lần 2 trong câu cùng chuỗi, không đánh", 1, None,
     None, "LC", None),
    ("S039", "Vietnamese drinks", "L", "repetition",
     "S038: Vietnamese coffee", "high", None, "lặp 'Vietnamese'", 1,
     None, None, "LC", None),
    # [Phase-2] branches ← branches (S020): lặp danh từ branch (H&H §6.2) —
    # referent đổi (7 Leaves, không phải Starbucks) nhưng giữ chuỗi hình
    # vị; tiền trạm cho "branch" (S044) — nhóm 12 protocol.
    ("S039", "branches", "L", "repetition",
     "S020: Starbucks' branches", "high", None,
     "more than 40 branches; VI S031 đối ứng 'chi nhánh' có hàng riêng", 1,
     None, None, "LC", None),
    # S040
    ("S040", "Meanwhile", "C", "temporal",
     "S039: 7 Leaves Café opened in 2011", "high", None, None, 1,
     None, None, "LC", None),
    ("S040", "Vietnamese cafes", "L", "repetition",
     "S039: Vietnamese drinks + a café chain", "high", None,
     "kết 2 chuỗi Vietnamese + cafes", 1, None, None, "LC", None),
    ("S040", "the country", "R", "general noun", "S039: In the US",
     "high", None, "lặp 'the country' (S039)", 1, None, None, "LC",
     "A"),
    ("S040", "Phin Ca Phe", "L", "repetition",
     "S020: ca phe muoi", "med", None,
     "tên quán chứa chuỗi 'ca phe' (không dấu)", 1, None, None, "LC",
     None),
    ("S040", "salt coffee", "L", "repetition", "S032: salt coffee",
     "high", None, "versions of salt coffee", 1, None, None, "LC",
     None),
    # [Phase-2] independent ← a café chain (S039): phép đối liên câu (TNT
    # §30; H&H §6.4 opposites) — chain ↔ independent; VI S032 đối ứng
    # "riêng lẻ" ← "chuỗi" (nhóm 2 protocol).
    ("S040", "independent", "L", "antonym",
     "S039: a café chain selling Vietnamese drinks", "med", None,
     "independent Vietnamese cafes đối lập chuỗi 7 Leaves (S039); VI S032 "
     "'riêng lẻ' có hàng Phase-2 riêng", 1, None, None, "LC",
     None),
    # S041
    ("S041", "Vietnamese coffee drinks", "L", "repetition",
     "S038: Vietnamese coffee", "high", None, None, 1, None, None,
     "LC", None),
    ("S041", "ca phe trung", "L", "repetition", "S033: egg coffee, or "
     "ca phe trung", "high", None, None, 1, None, None, "LC", None),
    ("S041", "Caphe House", "L", "repetition",
     "S040: Phin Ca Phe", "med", None,
     "tên quán chứa chuỗi 'caphe'", 1, None, None, "LC", None),
    # [Phase-2] venues ← Vietnamese cafes (S040): danh từ tổng quát (H&H
    # §6.1 general noun) — "venues" tổng quát hóa chuỗi quán; VI S033 đối
    # ứng "địa điểm".
    ("S041", "venues", "L", "general word",
     "S040: independent Vietnamese cafes", "med", None,
     "danh từ tổng quát chỉ các quán (venues like Caphe House)", 1, None,
     None, "LC", None),
    # S042 — KHỐI CẮT
    ("S042", "Hue", "L", "repetition", "S026: cafes in Hue", "high",
     None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S042", "Huong and Phong", "L", "repetition",
     "S005: co-owners Ho Thi Thanh Huong and Tran Nguyen Huu Phong",
     "high", None,
     "tên riêng lặp dạng rút gọn; khối cắt", 1, None, None, "LC",
     None),
    ("S042", "salt coffee", "L", "repetition", "S040: salt coffee",
     "high", None,
     "'their' trong câu không đánh; khối cắt", 1, None, None, "LC",
     None),
    ("S042", "salted lemon jam", "L", "repetition",
     "S019: salted caramel", "high", None, "lặp 'salted'; khối cắt", 1,
     None, None, "LC", None),
    ("S042", "chanh xi muoi", "L", "repetition", "S008: muoi means "
     "salt", "high", None,
     "tên món chứa 'muoi'; khối cắt", 1, None, None, "LC", None),
    # [Phase-2] patrons ← customers (S013): đồng nghĩa (H&H §6.2 synonym;
    # TNT §31) — chuỗi khách: customers → patrons.
    ("S042", "patrons", "L", "synonym", "S013: our first customers",
     "high", None,
     "khối cắt, VI none; 'their' trong câu (TC) không đánh; 'other items' "
     "so sánh trong câu (TC) không đánh", 1, None, None, "LC", None),
    # S043 — KHỐI CẮT
    ("S043", "they", "R", "personal", "S042: Huong and Phong",
     "high", None,
     "occ 1: lần 2 ('they think') trong câu cùng chuỗi, không đánh; "
     "'the former' trong câu không đánh; khối cắt", 1, None, None,
     "LC", "A"),
    ("S043", "salt coffee", "L", "repetition", "S042: salt coffee",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S043", "iced", "L", "repetition", "S004: served hot or iced",
     "high", None,
     "'hot' lần 2 trong câu (TC) không đánh; khối cắt", 1, None, None,
     "LC", None),
    # [Phase-2] And ← (S042): additive liên câu (H&H §5.4) — bổ sung thông
    # tin thứ hai về quán (bán cả iced lẫn hot); "though" nhượng bộ trong
    # câu không đánh.
    ("S043", "And", "C", "additive",
     "S042: the majority of their patrons order salt coffee", "med",
     None, "khối cắt, VI none; And though = bổ sung + nhượng bộ trong câu",
     1, None, None, "LC", None),
    # S044 — KHỐI CẮT
    ("S044", "The couple", "L", "repetition", "S042: Huong and Phong "
     "— the couple (S009)", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", None),
    ("S044", "Ca Phe Muoi", "L", "repetition", "S015: Ca Phe Muoi",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S044", "Hue", "L", "repetition", "S042: Back in Hue", "high",
     None, "the ancient Hue Imperial City; khối cắt", 1, None, None,
     "LC", None),
    # [Phase-2] bigger ← our first Ca Phe Muoi coffee shop (S005): quy
    # chiếu so sánh (H&H §2.5 particular comparison) — "bigger" lấy quán
    # đầu làm chuẩn.
    ("S044", "bigger", "R", "comparative",
     "S005: our first Ca Phe Muoi coffee shop", "med", None,
     "[LC] quy chiếu so sánh: bigger = to hơn quán đầu (S005); nằm cùng "
     "NP với phép đối first (S005) ↔ second (S044) — TNT §30", 1, None,
     None, "LC", "A"),
    # [Phase-2] branch ← branches (S039): lặp danh từ branch (H&H §6.2);
    # branch ≈ coffee shop (S005); phép đối first ↔ second (TNT §30).
    ("S044", "branch", "L", "repetition",
     "S039: more than 40 branches", "high", None,
     "khối cắt, VI none; a second, bigger branch of Ca Phe Muoi — "
     "referent về quán của Huong & Phong nhưng chuỗi hình vị chạy qua "
     "Starbucks (S020), 7 Leaves (S039)", 1, None, None, "LC", None),
    # S045 — KHỐI CẮT
    ("S045", "We", "R", "personal",
     "hai chủ quán (ngoại văn bản — quote)", "med", None,
     "khối cắt, VI none; 'we' viết thường lần 2 không đánh", 1, None,
     None, "LC", "E"),
    ("S045", "a drink", "L", "repetition", "S016: a daily drink",
     "high", None,
     "'it' trong câu không đánh; khối cắt", 1, None, None, "LC",
     None),
    ("S045", "a Hue specialty", "L", "repetition",
     "S014: a specialty drink representing historic Hue", "high",
     None,
     "kết specialty + Hue — hồi quy xa 31 câu; khối cắt", 1, None,
     None, "LC", None),
    ("S045", "they say", "R", "personal", "S044: The couple", "high",
     None, "khối cắt, VI none", 1, None, None, "LC", "A"),
]

TT = [
    # S002 (= EN S003)
    ("S002", "loại đồ uống", "L", "repetition",
     "S001: xu hướng đồ uống", "high", None,
     "không có chỉ từ như EN 'this now-popular beverage' (R)", 1, None,
     None, "LC", None),
    # [Phase-2] cà phê Việt Nam ← Cà phê muối (S001): lặp hình vị "cà phê"
    # (H&H §6.2 reiteration; TNT §26 phép lặp) — đối xứng EN S003
    # "Vietnamese coffee" ← S001 "a Vietnamese iced coffee" (nhóm 4).
    ("S002", "cà phê Việt Nam", "L", "repetition",
     "S001: Cà phê muối (tên đồ uống mở bài)", "high", None,
     "lặp hình vị 'cà phê'; 'Việt Nam' từ mới trong hợp chất — mắt xích "
     "đầu của cả chuỗi cà phê lẫn chuỗi Việt Nam (S011 cite)", 1, None,
     None, "LC", None),
    # [Phase-2] phổ biến ← phổ biến (S001): chuỗi tính từ sót (H&H §6.2; TNT
    # §26) — mắt xích được hàng S022 cite làm tiền trạm (nhóm 12 protocol).
    ("S002", "phổ biến", "L", "repetition",
     "S001: xu hướng đồ uống phổ biến", "high", None,
     "EN gộp 'popular' vào span R 'this now-popular beverage' nên chỉ 1 "
     "hàng; VI tách thành 2 hàng L (loại đồ uống + phổ biến)", 1, None,
     None, "LC", None),
    # S003 (= EN S004)
    ("S003", "Hỗn hợp này", "R", "demonstrative",
     "S002: thêm sữa đặc có đường vào cà phê Việt Nam", "high", None,
     "hậu chỉ từ 'này'; đối ứng EN 'The mixture' (R nominal)", 1, None,
     None, "LC", "A"),
    ("S003", "kem muối", "L", "repetition",
     "S001: Cà phê muối", "high", None, "hình vị 'muối' lặp", 1, None,
     None, "LC", None),
    # S005 (= EN S005)
    ("S005", "Chúng tôi", "R", "personal",
     "hai chủ quán (ngoại văn bản — quote)", "med", None,
     "ngoại quy chiếu", 1, None, None, "LC", "E"),
    ("S005", "cà phê muối", "L", "repetition",
     "S001: Cà phê muối", "high", None, None, 1, None, None, "LC",
     None),
    ("S005", "Cà phê Muối", "L", "repetition",
     "S001: Cà phê muối", "high", None,
     "tên quán viết hoa từng chữ", 1, None, None, "LC", None),
    # S006 (= EN S006)
    ("S006", "này", "R", "demonstrative",
     "S002: thêm sữa đặc có đường vào cà phê Việt Nam", "high", None,
     "hậu chỉ từ gắn cả danh ngữ 'Sự kết hợp giữa sữa đặc, muối và cà "
     "phê đen'; VI bỏ dấu quote như EN biên tập, ghi §8", 1, None,
     None, "LC", "A"),
    ("S006", "sữa đặc", "L", "repetition",
     "S002: sữa đặc có đường", "high", None,
     "occ 1: lần 2 ('của sữa đặc') trong câu cùng chuỗi, không đánh",
     1, None, None, "LC", None),
    ("S006", "muối", "L", "repetition", "S003: kem muối", "high",
     None, None, 1, None, None, "LC", None),
    ("S006", "cà phê đen", "L", "repetition", "S005: cà phê muối",
     "high", None, "lặp 'cà phê'; 'đen' từ mới", 1, None, None, "LC",
     None),
    ("S006", "hỗn hợp", "L", "repetition", "S003: Hỗn hợp này",
     "high", None, None, 1, None, None, "LC", None),
    # S007 (= EN S007+S008 gộp)
    ("S007", "quán cà phê", "L", "repetition",
     "S005: quán Cà phê Muối", "high", None,
     "'điều đó' chiếu tới phần sau trong câu (VI tự sinh), không đánh",
     1, None, None, "LC", None),
    ("S007", "đồ uống", "L", "repetition",
     "S001: xu hướng đồ uống", "high", None, None, 1, None, None,
     "LC", None),
    ("S007", "cà phê và muối", "L", "repetition",
     "S005: cà phê muối", "high", None,
     "kết 2 chuỗi cà phê + muối; đối ứng gloss EN S008 (5 hàng EN-only)",
     1, None, None, "LC", None),
    # S008 (= EN S009, cắt nửa đầu)
    ("S008", "quán cà phê", "L", "repetition",
     "S007: quán cà phê", "high", None, None, 1, None, None, "LC",
     None),
    ("S008", "chúng tôi", "R", "personal",
     "hai chủ quán (ngoại văn bản — quote)", "med", None,
     "ngoại quy chiếu; 'họ' trong câu chỉ khách hàng, không đánh", 1,
     None, None, "LC", "E"),
    ("S008", "cà phê muối", "L", "repetition", "S007: cà phê và muối",
     "high", None, None, 1, None, None, "LC", None),
    ("S008", "cặp đôi", "R", "nominal",
     "S005: đồng sở hữu Hồ Thị Thanh Hương và Trần Nguyễn Hữu Phong",
     "high", None, "danh ngữ tóm chỉ hai chủ", 1, None, None, "LC",
     "A"),
    # S009 (= EN S010)
    ("S009", "Chiến lược này", "R", "demonstrative",
     "S008: làm khác một chút để thu hút khách hàng", "high", None,
     "hậu chỉ từ 'này'; EN 'The strategy' là R nominal", 1, None,
     None, "LC", "A"),
    # S010 (= EN S011)
    # [Phase-2] uống ← đồ uống (S007): lặp hình vị drink ở dạng động từ (H&H
    # §6.2 reiteration; TNT §26 phép lặp) — đối xứng EN S011 "drinking" ←
    # S007 "drink" (nhóm 4).
    ("S010", "uống", "L", "repetition",
     "S007: đồ uống nổi tiếng hiện nay (chuỗi đồ uống)", "med", None,
     "lặp hình vị 'uống' ở dạng động từ (những gì đang uống); 'khách du "
     "lịch' lần đầu không đánh", 1, None, None, "LC", None),
    # S011 (= EN S014)
    ("S011", "cà phê muối", "L", "repetition",
     "S008: cà phê muối", "high", None,
     "'món này' trong câu chỉ cà phê muối (trong câu), không đánh", 1,
     None, None, "LC", None),
    ("S011", "Huế", "L", "repetition", "S002: thành phố Huế", "high",
     None, None, 1, None, None, "LC", None),
    ("S011", "các quán cà phê", "L", "repetition",
     "S008: quán cà phê", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] thức uống ← đồ uống (S007): chuỗi đồ uống (H&H §6.2; TNT
    # §26) — đối xứng EN S014 "a specialty drink" (nhóm 4).
    ("S011", "thức uống", "L", "repetition",
     "S007: đồ uống (chuỗi đồ uống S001)", "high", None,
     "biến thể 'đồ' → 'thức' cùng trường đồ uống; 'đặc sản' lần đầu không "
     "đánh (mắt xích cho S025)", 1, None, None, "LC", None),
    # [Phase-2] Việt Nam ← cà phê Việt Nam (S002): mắt xích được hàng S012
    # "Việt Nam" cite làm tiền trạm nhưng chưa có hàng — nhóm 12 protocol
    # (H&H §6.2; TNT §26).
    ("S011", "Việt Nam", "L", "repetition",
     "S002: cà phê Việt Nam", "high", None,
     "trên khắp Việt Nam — sót ở Phase-1 vì coi S002 là lần đầu", 1, None,
     None, "LC", None),
    # S012 (= EN S015)
    ("S012", "Cà phê Muối", "L", "repetition",
     "S005: quán Cà phê Muối", "high", None,
     "Những người sáng lập Cà phê Muối", 1, None, None, "LC", None),
    ("S012", "cà phê muối", "L", "repetition", "S011: cà phê muối",
     "high", None, None, 1, None, None, "LC", None),
    ("S012", "xu hướng", "L", "repetition", "S001: xu hướng đồ uống",
     "high", None, None, 1, None, None, "LC", None),
    ("S012", "Việt Nam", "L", "repetition", "S011: trên khắp Việt "
     "Nam", "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] người sáng lập ← đồng sở hữu (S005): đồng nghĩa cặp chủ quán
    # (H&H §6.2 synonym; TNT §31 phép thế đẳng nghĩa) — đối xứng EN S015
    # "founders" ← "co-owners" (nhóm 4).
    ("S012", "người sáng lập", "L", "synonym",
     "S005: đồng sở hữu Hồ Thị Thanh Hương và Trần Nguyễn Hữu Phong",
     "high", None,
     "đổi danh hiệu cặp chủ (Những người sáng lập Cà phê Muối)", 1, None,
     None, "LC", None),
    # S013 (= EN S016)
    ("S013", "Huế", "L", "repetition", "S011: Huế", "high", None,
     None, 1, None, None, "LC", None),
    ("S013", "cà phê muối", "L", "repetition", "S012: cà phê muối",
     "high", None, None, 1, None, None, "LC", None),
    ("S013", "cà phê đen", "L", "repetition", "S006: cà phê đen",
     "high", None, None, 1, None, None, "LC", None),
    ("S013", "cà phê sữa", "L", "repetition",
     "S006: cà phê đen + sữa đặc", "high", None,
     "kết 2 chuỗi cà phê + sữa; EN 'white coffee' từ mới không có hàng",
     1, None, None, "LC", None),
    ("S013", "xu hướng này", "R", "demonstrative",
     "S012: trở thành xu hướng", "high", None, None, 1, None, None,
     "LC", "A"),
    ("S013", "chúng tôi", "R", "personal",
     "chủ quán (ngoại văn bản — quote)", "med", None,
     "hoạt động kinh doanh của chúng tôi — ngoại quy chiếu", 1, None,
     None, "LC", "E"),
    # [Phase-2] thức uống ← thức uống đặc sản (S011): chuỗi đồ uống (H&H
    # §6.2; TNT §26) — đối xứng EN S016 "a daily drink" ← S014 (nhóm 4).
    ("S013", "thức uống", "L", "repetition",
     "S011: thức uống đặc sản", "high", None,
     "thức uống hàng ngày; 'như cà phê đen hay cà phê sữa' so sánh trong "
     "câu (TC) không đánh", 1, None, None, "LC", None),
    # S014 (= EN S017)
    ("S014", "quán cà phê", "L", "repetition",
     "S013: Ở Huế — quán cà phê (S011)", "high", None,
     "VI bỏ 'salt coffee' so với EN", 1, None, None, "LC", None),
    ("S014", "anh chị", "R", "personal",
     "S005: đồng sở hữu Hồ Thị Thanh Hương và Trần Nguyễn Hữu Phong",
     "high", None,
     "danh xưng cặp chủ — VI tự sinh; EN 'its' trong câu không đánh",
     1, None, None, "LC", "A"),
    ("S014", "Việt Nam", "L", "repetition", "S013: kinh doanh — Việt "
     "Nam (S012)", "high", None, "bán khắp nơi Việt Nam", 1, None,
     None, "LC", None),
    # [Phase-2] Ngày nay ← (S013): continuative (H&H §5.8 — precedent P21
    # "Now,"): mở khung discours về hiện tại sau mạch hồi tưởng 2010–Covid
    # — đối xứng EN S017 "Today" (nhóm 5).
    ("S014", "Ngày nay", "C", "continuative",
     "S013: quote xu hướng sau Covid (chuyển khung về hiện tại)", "med",
     None,
     "H&H §5.8 continuative — bộ tổ chức discours, không nối sự kiện "
     "trong thế giới", 1, None, None, "LC", None),
    # S015 (VI TỰ SINH — không có câu EN đối ứng)
    # [Phase-2] đồng thời ← (S014): additive liên câu (H&H §5.4) — câu VI tự
    # sinh bị segmenter tách khỏi S014 tại dấu phẩy nên "đồng thời" đứng
    # đầu câu (nhóm 11; bẫy nguồn ghi §8).
    ("S015", "đồng thời", "C", "additive",
     "S014: quán cà phê còn đóng chai để bán khắp nơi Việt Nam", "med",
     None,
     "bổ sung đồng thời hai phát triển (đóng chai bán + du khách tìm uống "
     "thử); 'như cách' so sánh trong câu (TC) không đánh", 1, None, None,
     "LC", None),
    ("S015", "Việt Nam", "L", "repetition", "S014: Việt Nam", "high",
     None,
     "câu VI tự sinh; 'cà phê trứng' nhắc trước phần chính thức "
     "(cataphora) không đánh", 1, None, None, "LC", None),
    ("S015", "loại cà phê này", "R", "demonstrative",
     "S013: cà phê muối", "high", None,
     "câu VI tự sinh; 'họ' trong câu chỉ du khách, không đánh", 1,
     None, None, "LC", "A"),
    # S016 (= EN S018)
    ("S016", "cái tên", "L", "repetition",
     "S007: Tên của quán cà phê", "high", None,
     "'cái' là mạo từ xác định; EN 'the name' là R", 1, None, None,
     "LC", None),
    # [Phase-2] kem ← kem muối (S003): chuỗi cream (H&H §6.2; TNT §26) —
    # đối xứng EN S019 "cream" ← "salted cream" (nhóm 4).
    ("S017", "kem", "L", "repetition",
     "S003: kem muối", "high", None,
     "lặp 'kem' trong 'kem ngọt'; mắt xích giữa 'hỗn hợp kem' (S006) nằm "
     "trong hàng 'hỗn hợp' nên bỏ qua như EN bỏ 'creamy' (S006)", 1, None,
     None, "LC", None),
    # S017 (= EN S019)
    ("S017", "Sữa", "L", "repetition",
     "S006: sữa đặc", "high", None, "Sữa và kem ngọt", 1, None, None,
     "LC", None),
    ("S017", "cân bằng", "L", "repetition",
     "S006: cân bằng vị ngọt", "high", None, None, 1, None, None,
     "LC", None),
    ("S017", "vị đắng", "L", "repetition",
     "S006: vị đắng của cà phê", "high", None, None, 1, None, None,
     "LC", None),
    ("S017", "cà phê", "L", "repetition", "S013: cà phê muối",
     "high", None, "vị đắng của cà phê", 1, None, None, "LC", None),
    ("S017", "muối", "L", "repetition", "S013: cà phê sữa — chuỗi muối "
     "(S006)", "high", None,
     "occ 1: lần 2 ('một chút muối') trong câu cùng chuỗi, không đánh",
     1, None, None, "LC", None),
    ("S017", "vị ngọt", "L", "repetition", "S006: vị ngọt của sữa "
     "đặc", "high", None, None, 1, None, None, "LC", None),
    ("S017", "mặn", "L", "repetition",
     "S006: muối", "med", None,
     "muối → mặn (cùng trường vị mặn); 'ca ra men' từ mượn lần đầu "
     "không đánh", 1, None, None, "LC", None),
    ("S017", "hương vị", "L", "repetition", "S016: hương vị thực sự",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] Ngay cả ← (S011): additive (H&H §5.4) — bổ sung trường hợp
    # cực đoan (Starbucks) vào tập quán đã phục vụ cà phê muối — đối xứng
    # EN S020 "Even" (nhóm 11; "cũng" khép cặp liên từ).
    ("S018", "Ngay cả", "C", "additive",
     "S011: các quán cà phê trên khắp Việt Nam cũng bắt đầu phục vụ",
     "med", None,
     "cặp 'Ngay cả…cũng' nhấn mức cực đoan; EN đối ứng 'Even…as well'", 1,
     None, None, "LC", None),
    # [Phase-2] làn sóng ← xu hướng này (S013): đồng nghĩa ẩn dụ (H&H §6.2
    # synonym) — đối xứng EN S020 "wave" ← "this trend" (nhóm 4).
    ("S018", "làn sóng", "L", "synonym",
     "S013: xu hướng này", "high", None,
     "làn sóng ≈ xu hướng (ẩn dụ 'sóng'); chuỗi xu hướng S001→S012→S013", 1,
     None, None, "LC", None),
    # S018 (= EN S020)
    ("S018", "Starbucks", "L", "repetition",
     "S001: 'ông lớn' Starbucks", "high", None,
     "'của riêng mình' trong câu không đánh", 1, None, None, "LC",
     None),
    ("S018", "Việt Nam", "L", "repetition", "S015: Việt Nam", "high",
     None, None, 1, None, None, "LC", None),
    ("S018", "cà phê muối", "L", "repetition",
     "S015: loại cà phê này", "high", None,
     "occ 1: lần 2 ('phiên bản cà phê muối') trong câu cùng chuỗi, "
     "không đánh — EN có hàng 'ca phe muoi' riêng", 1, None, None,
     "LC", None),
    # S020 (= EN S024)
    ("S020", "Việt Nam", "L", "repetition", "S018: Việt Nam", "high",
     None, None, 1, None, None, "LC", None),
    ("S020", "cà phê", "L", "repetition",
     "S018: cà phê muối", "high", None,
     "occ 1: lặp 2 lần trong câu (trồng cà phê Robusta, xuất khẩu cà "
     "phê), chọn lần 1", 1, None, None, "LC", None),
    # S021 (= EN S025)
    ("S021", "Việt Nam", "L", "repetition", "S020: Việt Nam", "high",
     None,
     "xuất khẩu cà phê của Việt Nam; EN 'The country's' là R", 1, None,
     None, "LC", None),
    ("S021", "cà phê", "L", "repetition", "S020: cà phê", "high",
     None, "xuất khẩu cà phê", 1, None, None, "LC", None),
    # [Phase-2] xuất khẩu ← nước xuất khẩu (S020): lặp hình vị xuất khẩu
    # (H&H §6.2; TNT §26 danh hóa) — đối xứng EN S025 "exports" ←
    # "exporter" (nhóm 4).
    ("S021", "xuất khẩu", "L", "repetition",
     "S020: nước xuất khẩu cà phê lớn thứ hai", "high", None,
     "xuất khẩu cà phê của Việt Nam — lặp hình vị 'xuất khẩu'", 1, None,
     None, "LC", None),
    # S022 (= EN S026)
    ("S022", "cà phê muối", "L", "repetition", "S018: cà phê muối",
     "high", None,
     "'Việc' đối ứng EN 'That' — nominalizer không hồi quy, không đánh",
     1, None, None, "LC", None),
    ("S022", "các quán cà phê", "L", "repetition",
     "S011: các quán cà phê", "high", None, None, 1, None, None, "LC",
     None),
    ("S022", "Huế", "L", "repetition", "S013: Huế", "high", None,
     None, 1, None, None, "LC", None),
    ("S022", "Việt Nam", "L", "repetition", "S021: Việt Nam", "high",
     None, None, 1, None, None, "LC", None),
    # [Phase-2] phổ biến ← phổ biến (S002): chuỗi tính từ sót (H&H §6.2) —
    # tiền trạm cho S023 (nhóm 12; một dấu cho mỗi chuỗi trong mỗi câu).
    ("S022", "phổ biến", "L", "repetition",
     "S002: loại đồ uống phổ biến", "high", None,
     "occ 1: lần 2 ('lựa chọn phổ biến') trong câu cùng chuỗi, không đánh",
     1, None, None, "LC", None),
    # S023 (= EN S027)
    ("S023", "cà phê", "L", "repetition", "S022: các quán cà phê",
     "high", None, "cà phê ngày nay", 1, None, None, "LC", None),
    ("S023", "cả nước", "R", "general noun",
     "S022: trên khắp Việt Nam", "med", None,
     "quy chiếu hiểu ngầm qua 'cả' — VI không có mạo từ; EN 'the "
     "country' lặp từ (S025)", 1, None, None, "LC", "A"),
    # [Phase-2] phổ biến ← phổ biến (S022): chuỗi tính từ (H&H §6.2; TNT
    # §26) — đối xứng EN S027 "popular" ← "now-famous" (nhóm 4).
    ("S023", "phổ biến", "L", "repetition",
     "S022: trở nên phổ biến", "high", None,
     "cực kỳ phổ biến khắp cả nước; EN S027 'extremely popular'", 1, None,
     None, "LC", None),
    # S024 (= EN S028)
    ("S024", "quán cà phê", "L", "repetition",
     "S022: các quán cà phê", "high", None,
     "occ 1: lần 2 ('quán cà phê hiện đại') trong câu cùng chuỗi, "
     "không đánh", 1, None, None, "LC", None),
    ("S024", "máy rang cà phê", "L", "repetition",
     "S023: cà phê", "high", None, "trường cà phê — máy rang tại chỗ",
     1, None, None, "LC", None),
    # S025 (= EN S032)
    ("S025", "Cà phê muối", "L", "repetition",
     "S022: cà phê muối", "high", None,
     "'chúng' trong câu chỉ các ly cà phê, không đánh", 1, None, None,
     "LC", None),
    ("S025", "ly cà phê", "L", "repetition", "S024: máy rang cà phê",
     "high", None, None, 1, None, None, "LC", None),
    ("S025", "Việt Nam", "L", "repetition", "S022: Việt Nam", "high",
     None, "của Việt Nam", 1, None, None, "LC", None),
    # [Phase-2] đặc sản ← thức uống đặc sản (S011): chuỗi đặc sản (H&H
    # §6.2; TNT §26) — mở chuỗi cho "a Hue specialty" (S045 EN, khối cắt);
    # nhóm 4.
    ("S025", "đặc sản", "L", "repetition",
     "S011: thức uống đặc sản", "high", None,
     "những ly cà phê đặc sản; 'ly cà phê' có hàng riêng trong cùng NP", 1,
     None, None, "LC", None),
    # S026 (= EN S033 phần 1)
    ("S026", "trong số đó", "R", "demonstrative",
     "S025: những ly cà phê đặc sản của Việt Nam", "high", None,
     "đối ứng EN 'them all' (S033)", 1, None, None, "LC", "A"),
    # [Phase-2] nổi tiếng ← đồ uống nổi tiếng (S007): chuỗi famous (H&H
    # §6.2) — đối xứng EN S033 "famous" ← "now-famous" (nhóm 4).
    ("S026", "nổi tiếng", "L", "repetition",
     "S007: đồ uống nổi tiếng hiện nay", "high", None,
     "nổi tiếng nhất trong số đó — lặp tính từ 'nổi tiếng'", 1, None, None,
     "LC", None),
    # [Phase-2] cà phê trứng ← cà phê trứng ở Hà Nội (S015): mắt xích được
    # hàng S033 cite làm tiền trạm nhưng chưa có hàng — nhóm 12 protocol
    # (H&H §6.2; TNT §26; lần 1 là nhắc trước trong câu VI tự sinh).
    ("S026", "cà phê trứng", "L", "repetition",
     "S015: cà phê trứng ở Hà Nội (câu VI tự sinh nhắc trước)", "med",
     None,
     "S015 lần đầu không đánh; S026 là lần 2 — lặp tên món", 1, None,
     None, "LC", None),
    # S027 (= EN S033 phần 2)
    ("S027", "sữa đặc", "L", "repetition",
     "S006: sữa đặc", "high", None,
     "đánh bọt sữa đặc; 'món tráng miệng này' trong câu không đánh", 1,
     None, None, "LC", None),
    ("S027", "nền cà phê", "L", "repetition",
     "S026: cà phê trứng", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] phát minh ← phát minh ra (S002): lặp động từ (H&H §6.2; TNT
    # §26) — đối xứng EN S033 "Invented" ← S003 "inventing"; phép đối ngầm
    # Huế ↔ Hà Nội (TNT §30).
    ("S027", "phát minh", "L", "repetition",
     "S002: phát minh ra loại đồ uống", "high", None,
     "Được phát minh ở Hà Nội — đối ứng EN 'Invented in Hanoi'", 1, None,
     None, "LC", None),
    # [Phase-2] trứng ← cà phê trứng (S026): VI tách EN S033 thành 2 câu nên
    # cặp "egg coffee → egg yolks" trong câu EN thành lặp LIÊN CÂU phía VI
    # — nhóm 6 protocol ([TC]→[LC] do VI tách câu).
    ("S027", "trứng", "L", "repetition",
     "S026: cà phê trứng", "high", None,
     "lòng đỏ trứng; EN 'egg yolks' cùng câu S033 chỉ là [TC]", 1, None,
     None, "LC", None),
    # [Phase-2] Hà Nội ← Hà Nội (S015): chuỗi Hà Nội (H&H §6.2; TNT §26) —
    # tiền trạm là nhắc trước trong câu VI tự sinh (nhóm 4).
    ("S027", "Hà Nội", "L", "repetition",
     "S015: cà phê trứng ở Hà Nội", "med", None,
     "Được phát minh ở Hà Nội; EN 'In Hanoi' (S033) lần đầu không có hàng",
     1, None, None, "LC", None),
    # S028 (= EN S034+S035+S036 GỘP)
    ("S028", "Và sau đó", "C", "additive",
     "S027: cà phê trứng", "high", None,
     "gộp 3 câu EN thành 1 — chỉ còn 1 C (EN có 'And then'+'And finally')",
     1, None, None, "LC", None),
    ("S028", "cà phê", "L", "repetition",
     "S027: nền cà phê", "high", None,
     "occ 1: lặp 3 lần trong câu (cốt dừa, sinh tố, sữa chua) cùng "
     "chuỗi, không đánh", 1, None, None, "LC", None),
    # S029 (= EN S037)
    ("S029", "những trải nghiệm và hương vị cà phê mới lạ này", "R",
     "demonstrative",
     "S025–S028: các loại cà phê đặc sản vừa kể", "high", None,
     "hậu chỉ từ 'này'; bên trong lặp chuỗi cà phê + hương vị (S016), "
     "ghi note", 1, None, None, "LC", "A"),
    # S030 (= EN S038)
    ("S030", "người tiêu dùng", "L", "repetition",
     "S029: người tiêu dùng", "high", None,
     "'họ' trong câu không đánh", 1, None, None, "LC", None),
    ("S030", "Mintel", "L", "repetition",
     "S029: Mintel", "high", None, None, 1, None, None, "LC", None),
    ("S030", "đồ uống cà phê", "L", "repetition",
     "S029: hương vị cà phê", "high", None, None, 1, None, None, "LC",
     None),
    ("S030", "cà phê Việt Nam", "L", "repetition",
     "S002: cà phê Việt Nam", "high", None,
     "hồi quy xa về S002 — kết chuỗi cà phê + Việt Nam", 1, None,
     None, "LC", None),
    # [Phase-2] quan tâm ← quan tâm (S029): lặp động từ (H&H §6.2; TNT §26)
    # — đối xứng EN S038 "interested" ← S037 (nhóm 4).
    ("S030", "quan tâm", "L", "repetition",
     "S029: ngày càng quan tâm đến những trải nghiệm", "high", None,
     "họ quan tâm đến việc thử — phát hiện khảo sát nhắc lại ở câu số "
     "liệu", 1, None, None, "LC", None),
    # S031 (= EN S039)
    ("S031", "Tại Mỹ", "L", "repetition", "S030: tại Mỹ", "high",
     None,
     "'đất nước' trong câu chỉ Mỹ, không đánh", 1, None, None, "LC",
     None),
    ("S031", "quán cà phê", "L", "repetition",
     "S024: quán cà phê", "high", None,
     "occ 1: lần 2 ('mở quán cà phê đầu tiên') trong câu cùng chuỗi, "
     "không đánh", 1, None, None, "LC", None),
    ("S031", "đồ uống Việt Nam", "L", "repetition",
     "S030: cà phê Việt Nam", "high", None, "lặp 'Việt Nam'", 1, None,
     None, "LC", None),
    # [Phase-2] chi nhánh ← chi nhánh Starbucks (S018): lặp danh từ (H&H
    # §6.2; precedent P21 "companies") — đối xứng EN S039 "branches" ← S020
    # (nhóm 4).
    ("S031", "chi nhánh", "L", "repetition",
     "S018: chi nhánh Starbucks tại Việt Nam", "high", None,
     "hơn 40 chi nhánh; referent đổi (7 Leaves) nhưng giữ chuỗi hình vị", 1,
     None, None, "LC", None),
    # S032 (= EN S040)
    ("S032", "Trong khi đó", "C", "temporal",
     "S031: 7 Leaves Café mở rộng 40 chi nhánh", "high", None,
     "đối ứng EN 'Meanwhile'", 1, None, None, "LC", None),
    ("S032", "quán cà phê", "L", "repetition",
     "S031: quán cà phê", "high", None, "các quán cà phê riêng lẻ", 1,
     None, None, "LC", None),
    ("S032", "Việt Nam", "L", "repetition",
     "S031: đồ uống Việt Nam", "high", None, None, 1, None, None,
     "LC", None),
    ("S032", "nước Mỹ", "L", "repetition", "S031: Tại Mỹ", "high",
     None, "khắp nước Mỹ", 1, None, None, "LC", None),
    ("S032", "Phin Ca Phe", "L", "repetition",
     "S028: cà phê", "med", None,
     "tên quán chứa chuỗi 'ca phe' (không dấu)", 1, None, None, "LC",
     None),
    ("S032", "cà phê muối", "L", "repetition",
     "S025: Cà phê muối", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] riêng lẻ ← chuỗi quán cà phê (S031): phép đối liên câu (TNT
    # §30; H&H §6.4 opposites) — đối xứng EN S040 "independent" ← "a café
    # chain" (nhóm 2).
    ("S032", "riêng lẻ", "L", "antonym",
     "S031: chuỗi quán cà phê", "med", None,
     "riêng lẻ (độc lập) đối lập 'chuỗi'; 'quán cà phê' có hàng riêng", 1,
     None, None, "LC", None),
    # S033 (= EN S041)
    ("S033", "Caphe House", "L", "repetition",
     "S032: Phin Ca Phe", "med", None,
     "tên quán chứa chuỗi 'caphe' (viết dính)", 1, None, None, "LC",
     None),
    ("S033", "đồ uống cà phê Việt Nam", "L", "repetition",
     "S030: cà phê Việt Nam", "high", None,
     "lặp cụm 'cà phê Việt Nam' (S002, S030)", 1, None, None, "LC",
     None),
    ("S033", "cà phê trứng", "L", "repetition",
     "S026: cà phê trứng", "high", None,
     "hồi quy xa về S026 (S015 mới là nhắc trước không đánh)", 1,
     None, None, "LC", None),
    # [Phase-2] địa điểm ← các quán cà phê riêng lẻ (S032): danh từ tổng
    # quát (H&H §6.1 general word) — đối xứng EN S041 "venues" (nhóm 3).
    ("S033", "địa điểm", "L", "general word",
     "S032: các quán cà phê riêng lẻ của Việt Nam", "med", None,
     "những địa điểm như Caphe House tổng quát hóa chuỗi quán", 1, None,
     None, "LC", None),
]
