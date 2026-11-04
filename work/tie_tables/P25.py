# P25 tie table — WRITTEN BY HAND FROM work/analysis/P25_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Text là chuỗi con nguyên văn trong câu (kiểm bằng pipeline.locate).
# KHỐI CẮT VI (tie chỉ EN): S006, S008, S015-S016, S023, S034-S045.
# KHỐI VI TỰ SINH (không có EN): S023-S031, S034, S039-S051.
# Tiểu đề (S017/S028/S046 EN; S013/S032/S052 VI) không gán nhãn.

ST = [
    # S002
    ("S002", "Underlying inflation", "L", "repetition",
     "S001: Underlying inflation dropped", "high", None, None, 1, None,
     None, "LC", None),
    ("S002", "the December quarter", "L", "repetition",
     "S001: in the December quarter", "high", None, None, 1, None, None,
     "LC", None),
    ("S002", "the lowest rate", "L", "repetition",
     "S001: its lowest rate in three years", "high", None, None, 1, None,
     None, "LC", None),
    # [Phase-2] eased ← dropped (S001): động từ chuỗi giảm bị sót (H&H §6.2
    # reiteration; TNT §26 phép lặp) — VI đối ứng "giảm xuống" (S002) lặp
    # nguyên hình → dịch chuyển EN synonym ↔ VI repetition, ghi §7.
    ("S002", "eased", "L", "synonym",
     "S001: Underlying inflation dropped", "high", None,
     "eased ≈ dropped — đồng nghĩa chuỗi động từ giảm (has eased to 3.2 "
     "per cent)", 1, None, None, "LC", None),
    # S003
    ("S003", "It", "R", "personal",
     "S002: Underlying inflation", "high", None,
     "VI hiện thực hóa thành 'lạm phát' nên không có R VI", 1, None, None,
     "LC", "A"),
    ("S003", "the previous quarter", "L", "repetition",
     "S002: the December quarter", "high", None,
     "VI 'quý trước' là lần đầu xuất hiện 'quý'", 1, None, None, "LC",
     None),
    # S004
    ("S004", "Meanwhile", "C", "temporal",
     "S003: It was at 3.6 per cent in the previous quarter", "high",
     None, None, 1, None, None, "LC", None),
    ("S004", "the December quarter", "L", "repetition",
     "S002: the December quarter", "high", None, None, 1, None, None,
     "LC", None),
    # S005
    ("S005", "ABS", "L", "repetition",
     "S002: Australian Bureau of Statistics (ABS)", "high", None, None,
     1, None, None, "LC", None),
    ("S005", "it", "R", "personal",
     "S004: the Consumer Price Index (CPI) rose by 0.2 per cent",
     "high", None, "it = mức tăng quý 4", 1, None, None, "LC", "A"),
    ("S005", "the lowest quarterly rises", "L", "repetition",
     "S002: the lowest rate", "high", None,
     "lặp 'the lowest'; 'quarterly/rises' khởi tạo chuỗi", 1, None,
     None, "LC", None),
    # S006 — KHỐI CẮT (VI none)
    ("S006", "December quarter", "L", "repetition",
     "S004: the December quarter", "high", None,
     "trong 'December quarter's rise'; khối cắt, VI none", 1, None,
     None, "LC", None),
    ("S006", "the September 2024 quarter", "L", "repetition",
     "S003: the previous quarter", "high", None,
     "khởi tạo chuỗi 'September quarter'; khối cắt", 1, None, None,
     "LC", None),
    # [Phase-2] rise ← rises (S005): mắt xích chuỗi 'rise' bị sót, được
    # S007 'These rises' cite làm tiền trạm (nhóm 12 bài học P28) —
    # H&H §6.2 reiteration; TNT §26; khối cắt, VI none.
    ("S006", "rise", "L", "repetition",
     "S005: the lowest quarterly rises", "high", None,
     "December quarter's rise — lặp rise (rises → rise); khối cắt", 1,
     None, None, "LC", None),
    ("S006", "she", "R", "personal",
     "S005: Michelle Marquardt", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", "A"),
    # S007
    ("S007", "These rises", "R", "demonstrative",
     "S005–S006: the lowest quarterly rises", "high", None, None, 1,
     None, None, "LC", "A"),
    ("S007", "the lowest", "L", "repetition",
     "S005: the lowest quarterly rises", "high", None, None, 1, None,
     None, "LC", None),
    ("S007", "the June 2020 quarter", "L", "repetition",
     "S006: the September 2024 quarter", "high", None,
     "lặp 'quarter'", 1, None, None, "LC", None),
    # [Phase-2] fell ↔ rises (S005): phép đối tăng–giảm liên câu (TNT §30;
    # H&H §6.4 opposites) — CPI giảm quý 6/2020 đối lập các mức tăng đang
    # nói; khởi tạo chuỗi fall (S015 falls, S022 the fall…); VI đối ứng
    # 'CPI giảm' (S006) đọc là lặp chuỗi 'giảm' — dịch chuyển antonym ↔
    # repetition, ghi §7.
    ("S007", "fell", "L", "antonym",
     "S005: the lowest quarterly rises", "high", None,
     "phép đối tăng↔giảm: when the CPI fell đối lập rises câu trước; "
     "khởi tạo chuỗi fall", 1, None, None, "LC", None),
    ("S007", "the CPI", "L", "repetition",
     "S004: the Consumer Price Index (CPI)", "high", None, None, 1,
     None, None, "LC", None),
    # S008 — KHỐI CẮT
    ("S008", "the December quarter", "L", "repetition",
     "S006: December quarter's rise", "high", None,
     "khối cắt, VI none", 1, None, None, "LC", None),
    # [Phase-2] rise ← rise (S006): chuỗi 'rise' bị sót (H&H §6.2) —
    # "the December quarter's rise of 2.4 per cent"; khối cắt.
    ("S008", "rise", "L", "repetition",
     "S006: December quarter's rise", "high", None,
     "lặp rise; khối cắt, VI none", 1, None, None, "LC", None),
    ("S008", "the September quarter", "L", "repetition",
     "S006: the September 2024 quarter", "high", None, "khối cắt", 1,
     None, None, "LC", None),
    # S009
    ("S009", "price rises", "L", "repetition",
     "S005: price statistics + S007: These rises", "high", None,
     "kết chuỗi price + rise", 1, None, None, "LC", None),
    ("S009", "the increase", "L", "repetition",
     "S006: the 0.2 per cent increase", "high", None,
     "mạo từ tóm chỉ mức tăng vừa kể + lặp từ", 1, None, None, "LC",
     None),
    # S010
    ("S010", "The CPI", "L", "repetition", "S007: the CPI", "high",
     None, None, 1, None, None, "LC", None),
    ("S010", "inflation", "L", "repetition",
     "S002: Underlying inflation", "high", None,
     "hình vị 'inflation' trong 'underlying inflation'", 1, None, None,
     "LC", None),
    # S011
    ("S011", "The ABS", "L", "repetition", "S005: ABS", "high", None,
     None, 1, None, None, "LC", None),
    ("S011", "price fluctuations", "L", "repetition",
     "S009: price rises", "high", None, "lặp 'price'", 1, None, None,
     "LC", None),
    ("S011", "household", "L", "repetition", "S010: households",
     "high", None, "household spending", 1, None, None, "LC", None),
    ("S011", "housing", "L", "repetition", "S009: housing and "
     "transport", "high", None, None, 1, None, None, "LC", None),
    ("S011", "public transport", "L", "repetition",
     "S009: transport", "high", None, None, 1, None, None, "LC", None),
    # S012
    ("S012", "However", "C", "adversative",
     "S011: The ABS gathers data from businesses", "high", None, None,
     1, None, None, "LC", None),
    ("S012", "the CPI", "L", "repetition", "S010: The CPI", "high",
     None, None, 1, None, None, "LC", None),
    ("S012", "data", "L", "repetition", "S011: gathers data", "high",
     None, None, 1, None, None, "LC", None),
    ("S012", "price changes", "L", "repetition",
     "S011: price fluctuations", "high", None, "lặp 'price'", 1, None,
     None, "LC", None),
    # S013
    ("S013", "underlying inflation", "L", "repetition",
     "S010: inflation", "high", None, None, 1, None, None, "LC", None),
    ("S013", "price swings", "L", "repetition",
     "S011: price fluctuations", "high", None,
     "lặp 'price'; swings ≈ fluctuations đồng nghĩa, ghi nhận", 1,
     None, None, "LC", None),
    # S014
    ("S014", "It", "R", "personal", "S013: the trimmed mean", "high",
     None, None, 1, None, None, "LC", "A"),
    ("S014", "the December quarter", "L", "repetition",
     "S004: the December quarter", "high", None, None, 1, None, None,
     "LC", None),
    ("S014", "the ABS", "L", "repetition", "S012: The ABS — S011",
     "high", None, None, 1, None, None, "LC", None),
    # S015 — KHỐI CẮT
    ("S015", "The trimmed mean", "L", "repetition",
     "S013: the trimmed mean", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", None),
    ("S015", "price falls", "L", "repetition",
     "S007: the CPI fell", "high", None,
     "fell → falls; khởi tạo chuỗi fall; khối cắt", 1, None, None,
     "LC", None),
    ("S015", "price rises", "L", "repetition", "S009: price rises",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    # S016 — KHỐI CẮT
    ("S016", "As a result", "C", "causal",
     "S015: The trimmed mean excluded price falls", "high", None,
     "khối cắt, VI none", 1, None, None, "LC", None),
    ("S016", "trimmed mean", "L", "repetition",
     "S015: The trimmed mean", "high", None, "khối cắt", 1, None, None,
     "LC", None),
    ("S016", "inflation", "L", "repetition",
     "S013: underlying inflation", "high", None,
     "occ 1: lần 2 ('CPI inflation' — hàng riêng) không đánh; khối cắt",
     1, None, None, "LC", None),
    ("S016", "CPI inflation", "L", "repetition",
     "S012: the CPI + S010: inflation", "high", None,
     "kết chuỗi CPI + inflation; khối cắt", 1, None, None, "LC", None),
    ("S016", "Marquardt", "L", "repetition",
     "S005: Michelle Marquardt", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", None),
    # S018
    # [Phase-2] the latest figures ← data (S012): mắt xích chuỗi dữ liệu
    # bị sót, được S029 'the latest figures' cite (nhóm 12 bài học P28) —
    # figures ≈ data đồng nghĩa (H&H §6.2); cũng đọc được là bridging tới
    # số liệu lạm phát vừa công bố (H&H §6.1) — một hình thức một hàng
    # (mapping §3.13) chọn đồng nghĩa theo chuỗi §6; VI 'những con số mới
    # nhất' (S014 TT) cũng thêm hàng.
    ("S018", "the latest figures", "L", "synonym",
     "S012: data from Australia's capital cities", "med", None,
     "figures ≈ data — đồng nghĩa chuỗi dữ liệu; ý chỉ số liệu lạm phát "
     "vừa công bố", 1, None, None, "LC", None),
    ("S018", "a rate cut", "L", "repetition",
     "S001: a pre-election rate cut", "high", None,
     "'the latest figures' có hàng riêng Phase-2", 1, None, None,
     "LC", None),
    # S019
    ("S019", "an interest rate cut", "L", "repetition",
     "S018: a rate cut", "high", None, None, 1, None, None, "LC",
     None),
    ("S019", "he", "R", "personal",
     "S018: Betashares chief economist David Bassenese", "high", None,
     None, 1, None, None, "LC", "A"),
    # S020
    ("S020", "the Reserve Bank", "L", "repetition",
     "S013: The Reserve Bank of Australia (RBA)", "high", None, None,
     1, None, None, "LC", None),
    ("S020", "these inflation results", "R", "demonstrative",
     "S001–S016: kết quả lạm phát vừa công bố", "high", None,
     "hậu chỉ từ + lặp 'inflation'", 1, None, None, "LC", "A"),
    ("S020", "households", "L", "repetition", "S011: household",
     "high", None, None, 1, None, None, "LC", None),
    ("S020", "an interest rate cut", "L", "repetition",
     "S019: an interest rate cut", "high", None, None, 1, None, None,
     "LC", None),
    ("S020", "I", "R", "personal",
     "Bassenese (ngoại văn bản — quote)", "med", None,
     "ngoại quy chiếu — người nói trong quote", 1, None, None, "LC",
     "E"),
    # S021
    ("S021", "My", "R", "personal",
     "Bassenese (ngoại văn bản — quote)", "med", None,
     "My expectation — ngoại quy chiếu", 1, None, None, "LC", "E"),
    # [Phase-2] further ← S020: quy chiếu so sánh (H&H §2.5 "more/
    # additional") — "two further rate cuts" = thêm hai lần cắt nữa SO
    # VỚI lần cắt tháng 2 đã nêu ở câu trước; VI 'thêm' (S017 TT) giữ 1-1.
    # 'further' lần 2 ('further declines') cùng chuỗi trong cùng câu →
    # không đánh thêm (precedent "không đánh thêm").
    ("S021", "further", "R", "comparative",
     "S020: an interest rate cut at the February 17-18 policy meeting",
     "med", None,
     "quy chiếu so sánh: further = thêm với lần cắt tháng 2 câu trước "
     "(H&H §2.5)", 1, None, None, "LC", "A"),
    # [Phase-2] declines ← eased (S002): mắt xích chuỗi động từ giảm bị
    # sót, được S026 'decline' cite làm tiền trạm (nhóm 12) — declines ≈
    # dropped/eased (H&H §6.2); VI 'tiếp tục giảm' (S017 TT) đã có hàng.
    ("S021", "declines", "L", "synonym",
     "S002: has eased to 3.2 per cent", "high", None,
     "declines ≈ eased/dropped — chuỗi động từ giảm; S026 'decline' truy "
     "hồi mắt xích này", 1, None, None, "LC", None),
    # [Phase-2] quarterly ← quarterly (S005): mắt xích chuỗi 'quarterly'
    # bị sót, được S034 'quarterly CPI' cite (nhóm 12) — H&H §6.2; VI
    # 'quý' (S017 TT) cũng thêm hàng.
    ("S021", "quarterly", "L", "repetition",
     "S005: the lowest quarterly rises", "high", None,
     "lặp quarterly (quarterly CPI reports)", 1, None, None, "LC",
     None),
    ("S021", "the RBA", "L", "repetition",
     "S013: The Reserve Bank of Australia (RBA)", "high", None, None,
     1, None, None, "LC", None),
    ("S021", "rate cuts", "L", "repetition",
     "S020: an interest rate cut", "high", None,
     "two further rate cuts", 1, None, None, "LC", None),
    ("S021", "inflation", "L", "repetition",
     "S020: these inflation results", "high", None,
     "declines in inflation", 1, None, None, "LC", None),
    ("S021", "CPI", "L", "repetition", "S016: CPI inflation", "high",
     None, "quarterly CPI reports", 1, None, None, "LC", None),
    # S022
    ("S022", "He", "R", "personal", "S020: I (Bassenese)", "high",
     None, None, 1, None, None, "LC", "A"),
    # [Phase-2] also ← S020–S021: nối additive liên câu (H&H §5.4) bị sót
    # — "He also flagged" bổ sung nhận định thứ hai của Bassenese; VI
    # 'cũng' (S018 TT) đối xứng 1-1 (bài học P22/P28 nhóm 11).
    ("S022", "also", "C", "additive",
     "S021: two further rate cuts this year", "high", None,
     "also = bổ sung yếu tố thứ hai (the fall) ngoài dự đoán cắt lãi "
     "suất; H&H §5.4", 1, None, None, "LC", None),
    ("S022", "underlying inflation", "L", "repetition",
     "S021: inflation", "high", None, None, 1, None, None, "LC",
     None),
    ("S022", "the fall", "L", "repetition",
     "S015: price falls", "high", None,
     "fall in underlying inflation", 1, None, None, "LC", None),
    # S023 — KHỐI CẮT
    ("S023", "trimmed mean", "L", "repetition",
     "S016: trimmed mean", "high", None,
     "nguồn lỗi 'fall back to with' + ngoặc kép lồng, ghi §8; khối cắt",
     1, None, None, "LC", None),
    ("S023", "inflation", "L", "repetition",
     "S022: underlying inflation", "high", None,
     "occ 1: lần 2 ('inflation target band' — hàng riêng) không đánh; "
     "khối cắt", 1, None, None, "LC", None),
    ("S023", "the RBA", "L", "repetition", "S021: the RBA", "high",
     None,
     "occ 1: lần 2 ('the RBA's current expectation') trong câu cùng "
     "chuỗi, không đánh; khối cắt", 1, None, None, "LC", None),
    ("S023", "fall back", "L", "repetition", "S022: the fall", "high",
     None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S023", "he", "R", "personal", "S022: He (Bassenese)", "high",
     None,
     "occ 3 vì 'The/the' chứa 'he'; lần 3 mới là đại từ; khối cắt", 3,
     None, None, "LC", "A"),
    # [Phase-2] expectation ← expectation (S021): chuỗi động từ expect bị
    # sót (H&H §6.2) — "the RBA's current expectation"; khối cắt; VI tân
    # từ phân tán (kỳ vọng/dự kiến) nên không có đối ứng, ghi §7.
    ("S023", "expectation", "L", "repetition",
     "S021: My expectation", "high", None,
     "lặp expectation; khối cắt, VI none", 1, None, None, "LC", None),
    # S024
    ("S024", "economist", "L", "repetition",
     "S018: chief economist David Bassenese", "high", None, None, 1,
     None, None, "LC", None),
    ("S024", "the RBA", "L", "repetition", "S023: the RBA", "high",
     None, "'the cash rate' khởi tạo chuỗi", 1, None, None, "LC",
     None),
    # [Phase-2] reduce ← rate cuts (S021): động từ chuỗi cắt giảm bị sót
    # (H&H §6.2 synonym) — "not reduce the cash rate" = không cắt lãi
    # suất tiền mặt; VI 'giảm lãi suất tiền mặt' (S019 TT) lặp chuỗi
    # 'giảm' — dịch chuyển EN synonym ↔ VI repetition, ghi §7.
    ("S024", "reduce", "L", "synonym",
     "S021: two further rate cuts", "high", None,
     "reduce the cash rate ≈ cut — đồng nghĩa chuỗi cắt giảm", 1, None,
     None, "LC", None),
    # S025
    ("S025", "A rate cut", "L", "repetition",
     "S021: rate cuts", "high", None, None, 1, None, None, "LC", None),
    ("S025", "policy meeting", "L", "repetition",
     "S020: the February 17-18 policy meeting", "high", None, None, 1,
     None, None, "LC", None),
    ("S025", "RBA", "L", "repetition", "S024: the RBA", "high", None,
     "trong 'the February RBA policy meeting'", 1, None, None, "LC",
     None),
    ("S025", "our", "R", "personal",
     "Shivadekar + đồng nghiệp (ngoại văn bản — quote)", "med", None,
     "in our opinion — ngoại quy chiếu", 1, None, None, "LC", "E"),
    ("S025", "she", "R", "personal",
     "S024: RSM Australia economist Devika Shivadekar", "high", None,
     None, 1, None, None, "LC", "A"),
    # S026
    ("S026", "The RBA", "L", "repetition", "S025: RBA", "high", None,
     None, 1, None, None, "LC", None),
    ("S026", "decline", "L", "repetition",
     "S021: declines in inflation", "high", None,
     "a 'sustainable' decline", 1, None, None, "LC", None),
    ("S026", "trimmed mean inflation", "L", "repetition",
     "S023: trimmed mean + inflation", "high", None,
     "kết 2 chuỗi trimmed mean + inflation", 1, None, None, "LC",
     None),
    ("S026", "data point", "L", "repetition",
     "S012: data", "high", None,
     "'that one additional data point' — 'that' hư chỉ giả định, "
     "không đánh", 1, None, None, "LC", None),
    # S027
    ("S027", "However", "C", "adversative",
     "S026: The RBA would err on the side of caution", "high", None,
     None, 1, None, None, "LC", None),
    # [Phase-2] broader ← S026: quy chiếu so sánh (H&H §2.5; tiền lệ P24
    # "broader", P28 "more realistic") — "the broader trend" = rộng hơn
    # mức giảm trimmed mean câu trước; VI 'rộng hơn' (S022 TT) đối xứng
    # 1-1; cùng NP có hàng L riêng trên 'disinflationary trend' (tiền lệ
    # P21 'lừa đảo'+'khác').
    ("S027", "broader", "R", "comparative",
     "S026: a 'sustainable' decline in trimmed mean inflation", "med",
     None,
     "so sánh phạm vi (H&H §2.5): broader = rộng hơn mức giảm đã nêu "
     "câu trước", 1, None, None, "LC", "A"),
    ("S027", "disinflationary trend", "L", "repetition",
     "S026: trimmed mean inflation", "high", None,
     "hình vị 'inflation' trong 'disinflationary'", 1, None, None,
     "LC", None),
    # S029
    ("S029", "the latest figures", "L", "repetition",
     "S018: the latest figures", "high", None, None, 1, None, None,
     "LC", None),
    ("S029", "a rate cut", "L", "repetition", "S025: A rate cut",
     "high", None, None, 1, None, None, "LC", None),
    ("S029", "a cash rate reduction", "L", "repetition",
     "S024: the cash rate", "high", None,
     "lặp 'cash rate'; 'reduction' ≈ 'cut' đồng nghĩa, ghi nhận", 1,
     None, None, "LC", None),
    ("S029", "the RBA", "L", "repetition", "S027: disinflationary "
     "trend — the RBA (S026)", "high", None, None, 1, None, None,
     "LC", None),
    # S030
    ("S030", "But", "C", "adversative",
     "S029: Westpac is predicting a rate cut", "high", None, None, 1,
     None, None, "LC", None),
    ("S030", "the cash rate target", "L", "repetition",
     "S029: a cash rate reduction", "high", None, None, 1, None, None,
     "LC", None),
    ("S030", "RBA meeting", "L", "repetition",
     "S025: policy meeting + S029: the RBA", "high", None,
     "kết chuỗi RBA + meeting", 1, None, None, "LC", None),
    # S031
    ("S031", "The big four", "L", "repetition",
     "S028: What are the 'big four' saying — tiểu đề", "high", None,
     "tiểu đề làm tiền trạm, không gán nhãn trên tiểu đề", 1, None,
     None, "LC", None),
    # [Phase-2] also ← S029–S030: nối additive liên câu (H&H §5.4) bị sót
    # — "The big four also have varying predictions"; VI 'cũng' (S036
    # TT) đối xứng 1-1 (nhóm 11 bài học P22/P28).
    ("S031", "also", "C", "additive",
     "S030: NAB disagrees and has predicted", "high", None,
     "bổ sung khía cạnh thứ hai (số lần cắt) ngoài dự đoán thời điểm; "
     "H&H §5.4", 1, None, None, "LC", None),
    ("S031", "predictions", "L", "repetition",
     "S029: Westpac is predicting", "high", None,
     "predicting → predictions", 1, None, None, "LC", None),
    ("S031", "rate cuts", "L", "repetition",
     "S030: the cash rate target", "high", None,
     "the number of rate cuts in 2025", 1, None, None, "LC", None),
    # S032
    ("S032", "the most cautious", "L", "repetition",
     "S024: the RBA may remain cautious", "high", None, None, 1, None,
     None, "LC", None),
    ("S032", "two cuts", "L", "repetition",
     "S031: rate cuts", "high", None, None, 1, None, None, "LC",
     None),
    ("S032", "CBA and Westpac", "L", "repetition",
     "S029: the Commonwealth Bank (CBA) and ANZ — Westpac (S029)",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] ANZ ← ANZ (S029): chuỗi tên riêng ANZ bị sót (H&H §6.2;
    # TNT §26) — VI 'ANZ' (S037 TT) đối xứng 1-1.
    ("S032", "ANZ", "L", "repetition",
     "S029: the Commonwealth Bank (CBA) and ANZ", "high", None,
     "lặp tên ngân hàng ANZ", 1, None, None, "LC", None),
    # [Phase-2] expecting ← expectation (S023): mắt xích chuỗi expect bị
    # sót (H&H §6.2) — VI tân từ phân tán (kỳ vọng S017 / dự kiến S037)
    # nên VI không có chuỗi lặp — dịch chuyển từ vựng, ghi §7.
    ("S032", "expecting", "L", "repetition",
     "S023: the RBA's current expectation", "med", None,
     "lặp hình vị expect (expectation → expecting)", 1, None, None,
     "LC", None),
    # [Phase-2] forecast ← predictions (S031): đồng nghĩa chuỗi dự đoán
    # bị sót (H&H §6.2) — VI 'dự báo' (S037 TT) đối xứng; 'predicting'
    # (S029) là lần đầu chuỗi nên không có hàng.
    ("S032", "forecast", "L", "synonym",
     "S031: varying predictions", "high", None,
     "forecast ≈ predicting/predictions — chuỗi dự đoán", 1, None,
     None, "LC", None),
    # [Phase-2] ∅ sau 'four' (H&H §4.2 nominal ellipsis: number + zero
    # head) — "forecast four ∅{cuts}"; VI hiện thực hóa 'bốn lần cắt
    # giảm' nên VI không có E (nguyên tắc không bịa ∅, NTT 2020 §2).
    ("S032", None, "E", "nominal",
     "S032: expecting two cuts (trong câu)", "high", None,
     "[TC] lược đầu từ sau four ∅ {cuts}; H&H §4.2", 1, "four",
     "{cuts}", "TC", None),
    # S033
    ("S033", "NAB", "L", "repetition",
     "S030: But NAB disagrees", "high", None, None, 1, None, None,
     "LC", None),
    ("S033", "predicting", "L", "repetition",
     "S029: Westpac is predicting", "high", None, None, 1, None,
     None, "LC", None),
    ("S033", "five cuts", "L", "repetition",
     "S032: two cuts", "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] ∅ sau 'the most' (H&H §4.2): "predicting the most ∅{cuts}"
    # — đầu từ bị lược, hồi phục được từ S031–S032 → [LC]; VI 'nhiều
    # nhất' (S038 TT) cùng tỉnh lược — cặp E↔E hiếm thấy đối xứng 1-1
    # (NTT 2020 §5: ellipsis khó chuyển nhất nhưng hai đầu cùng chọn ∅).
    ("S033", None, "E", "nominal",
     "S032: expecting two cuts, while CBA and Westpac forecast four",
     "high", None,
     "[LC] lược đầu từ sau the most ∅ {cuts} — H&H §4.2; VI đối xứng "
     "'nhiều nhất' ∅ (S038)", 1, "the most", "{cuts}", "LC", None),
    # S034 — KHỐI CẮT (tiểu đề + câu lồng)
    ("S034", "The ABS", "L", "repetition", "S014: the ABS", "high",
     None, "tiểu đề lồng câu; khối cắt, VI none", 1, None, None, "LC",
     None),
    ("S034", "the dip in quarterly CPI", "L", "repetition",
     "S021: quarterly CPI reports", "high", None,
     "tiểu đề lồng 'in quarterly CPI' — chọn phần câu; khối cắt", 1,
     None, None, "LC", None),
    ("S034", "to electricity and fuel prices falling", "L",
     "repetition", "S015: Electricity and Automotive fuel", "high",
     None,
     "kết chuỗi electricity + fuel + falling (S015 price falls); khối "
     "cắt", 1, None, None, "LC", None),
    # S035 — KHỐI CẮT
    ("S035", "Electricity prices", "L", "repetition",
     "S034: electricity and fuel prices", "high", None, "khối cắt", 1,
     None, None, "LC", None),
    ("S035", "fell", "L", "repetition",
     "S034: falling", "high", None, "khối cắt, VI none", 1, None,
     None, "LC", None),
    ("S035", "the December quarter", "L", "repetition",
     "S008: the December quarter", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    ("S035", "it", "R", "personal", "S034: The ABS", "high", None,
     "occ 2 vì 'Electricity' chứa 'it'; lần 2 mới là đại từ; khối cắt, "
     "VI none", 2, None, None, "LC", "A"),
    # S036 — KHỐI CẮT
    ("S036", "the fall in electricity prices", "L", "repetition",
     "S035: Electricity prices fell", "high", None,
     "kết 2 chuỗi fall + electricity prices; khối cắt", 1, None, None,
     "LC", None),
    ("S036", "this quarter", "L", "repetition",
     "S035: the December quarter", "high", None,
     "hậu chỉ 'this' + lặp 'quarter'; khối cắt", 1, None, None, "LC",
     None),
    # S037 — KHỐI CẮT
    ("S037", "Automotive fuel prices", "L", "repetition",
     "S034: electricity and fuel prices", "high", None,
     "kết chuỗi Automotive fuel (S015) + prices; khối cắt", 1, None,
     None, "LC", None),
    ("S037", "fell", "L", "repetition", "S035: fell", "high", None,
     "khối cắt, VI none", 1, None, None, "LC", None),
    ("S037", "the December quarter", "L", "repetition",
     "S035: the December quarter", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    ("S037", "global oil prices", "L", "repetition",
     "S036: electricity prices", "high", None,
     "lặp 'prices'; 'oil' từ mới; khối cắt", 1, None, None, "LC",
     None),
    # S038 — KHỐI CẮT (tiểu đề + câu lồng)
    ("S038", "Food prices", "L", "repetition",
     "S037: global oil prices", "high", None,
     "lặp 'prices'; tiểu đề lồng 'fruit and vegetable prices'; khối cắt",
     1, None, None, "LC", None),
    ("S038", "increased", "L", "repetition", "S009: the increase",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S038", "the December quarter", "L", "repetition",
     "S037: the December quarter", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    ("S038", "the September quarter", "L", "repetition",
     "S008: the September quarter", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    # S039 — KHỐI CẮT
    ("S039", "Price hikes", "L", "repetition",
     "S009: price rises", "high", None,
     "lặp 'price'; 'hikes' ≈ 'rises' đồng nghĩa; khối cắt", 1, None,
     None, "LC", None),
    ("S039", "food categories", "L", "repetition",
     "S038: Food prices", "high", None, "lặp 'food'; khối cắt", 1,
     None, None, "LC", None),
    ("S039", "lamb prices", "L", "repetition",
     "S038: Food prices", "high", None, "lặp 'prices'; khối cắt", 1,
     None, None, "LC", None),
    # S040 — KHỐI CẮT
    ("S040", "fruit and vegetable prices", "L", "repetition",
     "S038: Drop in fruit and vegetable prices (tiểu đề lồng)",
     "high", None,
     "'they' trong câu chỉ prices (trong câu), không đánh; khối cắt", 1,
     None, None, "LC", None),
    ("S040", "dropped", "L", "repetition",
     "S001: Underlying inflation dropped", "high", None, "khối cắt", 1,
     None, None, "LC", None),
    ("S040", "the latest quarter", "L", "repetition",
     "S029: the latest figures + S038: the December quarter", "high",
     None, "kết chuỗi latest + quarter; khối cắt", 1, None, None,
     "LC", None),
    # S041 — KHỐI CẮT
    ("S041", "prices falling", "L", "repetition",
     "S040: fruit and vegetable prices", "high", None,
     "lặp 'prices'; 'falling' tiếp chuỗi fall (S036); khối cắt", 1,
     None, None, "LC", None),
    ("S041", "the ABS", "L", "repetition", "S035: The ABS", "high",
     None, "khối cắt, VI none", 1, None, None, "LC", None),
    # S042 — KHỐI CẮT (tiểu đề + câu lồng)
    ("S042", "Tobacco prices", "L", "repetition",
     "S009: alcohol and tobacco + S039: lamb prices", "high", None,
     "kết chuỗi Tobacco + prices; tiểu đề lồng 'Alcohol, tobacco and "
     "travel prices increase'; khối cắt", 1, None, None, "LC", None),
    ("S042", "rose", "L", "repetition",
     "S004: rose by a modest 0.2 per cent", "high", None, "khối cắt",
     1, None, None, "LC", None),
    ("S042", "the quarter", "L", "repetition",
     "S040: the latest quarter", "high", None,
     "over the quarter; khối cắt", 1, None, None, "LC", None),
    ("S042", "alcoholic beverages", "L", "repetition",
     "S009: alcohol and tobacco", "high", None,
     "alcohol → alcoholic; khối cắt", 1, None, None, "LC", None),
    ("S042", "a narrower increase", "L", "repetition",
     "S038: increased", "high", None, "khối cắt, VI none", 1, None,
     None, "LC", None),
    # S043 — KHỐI CẮT
    ("S043", "tobacco", "L", "repetition",
     "S042: Tobacco prices", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", None),
    ("S043", "beer", "L", "repetition",
     "S042: driven by beer", "high", None, "khối cắt", 1, None, None,
     "LC", None),
    # [Phase-2] ∅ sau 'beer' (H&H §4.3 verbal ellipsis) — "and beer ∅{is
    # up} 4.3 per cent": vị ngữ lược trong phép đẳng lập, hồi phục từ vế
    # 'tobacco is up' cùng câu → [TC]; khối cắt, VI none.
    ("S043", None, "E", "verbal",
     "S043: tobacco is up 12.2 per cent (trong câu)", "high", None,
     "[TC] lược vị ngữ sau beer ∅ {is up}; H&H §4.3", 1, "beer ",
     "{is up}", "TC", None),
    # S044 — KHỐI CẮT
    ("S044", "Recreation and culture", "L", "repetition",
     "S009: recreation and culture", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    # [Phase-2] also ← S042–S043: nối additive liên câu (H&H §5.4) bị sót
    # — "Recreation and culture also witnessed" bổ sung nhóm tăng giá
    # thứ ba; khối cắt, VI none (nhóm 11 bài học P22/P28).
    ("S044", "also", "C", "additive",
     "S043: tobacco is up 12.2 per cent, and beer 4.3 per cent", "high",
     None, "bổ sung nhóm giá tăng thứ ba; H&H §5.4", 1, None, None,
     "LC", None),
    ("S044", "an increase", "L", "repetition",
     "S042: a narrower increase", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    ("S044", "the December quarter", "L", "repetition",
     "S038: the December quarter", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    ("S044", "the ABS", "L", "repetition", "S041: the ABS", "high",
     None,
     "'the holiday period' khởi tạo chuỗi; khối cắt", 1, None, None,
     "LC", None),
    # S045 — KHỐI CẮT
    ("S045", "the rise", "L", "repetition",
     "S042: Tobacco prices rose", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    ("S045", "holiday travel", "L", "repetition",
     "S042: Alcohol, tobacco and travel prices (tiểu đề lồng)",
     "high", None, "lặp 'travel'; khối cắt", 1, None, None, "LC",
     None),
    ("S045", "an increase", "L", "repetition",
     "S044: an increase", "high", None,
     "an increase in travel demand; khối cắt", 1, None, None, "LC",
     None),
    ("S045", "school holiday period", "L", "repetition",
     "S044: the holiday period", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    ("S045", "prices for airfares", "L", "repetition",
     "S041: prices falling", "high", None,
     "lặp 'prices'; 'accommodation' lặp 2 lần trong câu (TC) không "
     "đánh; khối cắt", 1, None, None, "LC", None),
    ("S045", "it", "R", "personal", "S044: the ABS", "high", None,
     "it said; khối cắt, VI none", 1, None, None, "LC", "A"),
    # S047
    ("S047", "The RBA", "L", "repetition",
     "S033: NAB is predicting — the RBA (S030)", "high", None,
     "'its' trong câu không đánh", 1, None, None, "LC", None),
    ("S047", "inflation", "L", "repetition",
     "S027: disinflationary trend", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] a key factor ← an important factor (S022): chuỗi 'factor'
    # bị sót (H&H §6.2) — cùng vai trò: lạm phát là yếu tố trong quyết
    # định lãi suất; VI 'yếu tố chính' (S053 TT) đối xứng 1-1.
    ("S047", "a key factor", "L", "repetition",
     "S022: an important factor", "med", None,
     "lặp factor (an important factor → a key factor)", 1, None, None,
     "LC", None),
    # [Phase-2] lower ← reduction (S029): đồng nghĩa chuỗi cắt giảm bị sót
    # (H&H §6.2) — "to raise or lower interest rates"; cặp raise↔lower
    # trong câu là phép đối [TC] (TNT §30); VI 'giảm' (S053 TT) lặp chuỗi
    # 'giảm'; 'raise' là lần đầu chuỗi tăng nên không có hàng.
    ("S047", "lower", "L", "synonym",
     "S029: a cash rate reduction", "med", None,
     "lower interest rates ≈ cut/reduce — đồng nghĩa chuỗi cắt giảm", 1,
     None, None, "LC", None),
    ("S047", "interest rates", "L", "repetition",
     "S021: rate cuts", "high", None, None, 1, None, None, "LC", None),
    # S048
    # [Phase-2] Australia's ← Australia's (S012): chuỗi Úc EN bị sót
    # (H&H §6.2) — VI chuỗi 'Úc' dày hơn; đối xứng VI 'Úc' (S054 TT).
    ("S048", "Australia's", "L", "repetition",
     "S012: Australia's capital cities", "high", None,
     "lặp Australia's (official inflation target)", 1, None, None,
     "LC", None),
    ("S048", "inflation target", "L", "repetition",
     "S023: inflation target band", "high", None, None, 1, None, None,
     "LC", None),
    ("S048", "reduce inflation", "L", "repetition",
     "S047: inflation", "high", None, None, 1, None, None, "LC",
     None),
    ("S048", "the RBA", "L", "repetition", "S047: The RBA", "high",
     None, None, 1, None, None, "LC", None),
    ("S048", "raising", "L", "repetition",
     "S047: to raise or lower interest rates", "high", None, None, 1,
     None, None, "LC", None),
    ("S048", "interest rates", "L", "repetition",
     "S047: interest rates", "high", None, None, 1, None, None, "LC",
     None),
    # S049
    ("S049", "increasing rates", "L", "repetition",
     "S048: interest rates", "high", None,
     "lặp 'rates'; increasing ≈ raising", 1, None, None, "LC", None),
    ("S049", "the RBA", "L", "repetition", "S048: the RBA", "high",
     None, "'in February' mốc thời gian, không đánh", 1, None, None,
     "LC", None),
    ("S049", "kept the rate steady", "L", "repetition",
     "S048: interest rates", "high", None,
     "lặp 'rate' (số ít)", 1, None, None, "LC", None),
    # [Phase-2] convene ← RBA meeting (S030): đồng nghĩa chuỗi họp bị sót
    # (H&H §6.2) — "will next convene in February"; VI 'sẽ họp' (S055
    # TT) đối xứng 1-1.
    ("S049", "convene", "L", "synonym",
     "S030: the third RBA meeting in May", "med", None,
     "convene ≈ hold a meeting — chuỗi họp", 1, None, None, "LC",
     None),
    # [Phase-2] Australia ← Australia's (S048): chuỗi Úc EN bị sót — đối
    # xứng VI 'Úc' (S055 TT).
    ("S049", "Australia", "L", "repetition",
     "S048: Australia's official inflation target", "high", None,
     "lặp Australia (could see a reduction)", 1, None, None, "LC",
     None),
    # [Phase-2] a reduction ← a cash rate reduction (S029): mắt xích chuỗi
    # cắt giảm bị sót (H&H §6.2; §6 liệt kê reduction S049) — VI 'giảm'
    # (S055 TT) lặp chuỗi 'giảm'.
    ("S049", "a reduction", "L", "repetition",
     "S029: a cash rate reduction", "high", None,
     "lặp reduction (a reduction in the cash rate target)", 1, None,
     None, "LC", None),
    ("S049", "the cash rate target", "L", "repetition",
     "S030: the cash rate target", "high", None, None, 1, None, None,
     "LC", None),
    # S050
    ("S050", "RBA", "L", "repetition", "S049: the RBA", "high", None,
     "RBA governor", 1, None, None, "LC", None),
    ("S050", "inflation", "L", "repetition",
     "S048: reduce inflation", "high", None, "taming inflation", 1,
     None, None, "LC", None),
    # S051
    ("S051", "inflation", "L", "repetition",
     "S050: taming inflation", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] coming down ← falling (S041): đồng nghĩa chuỗi giảm bị sót
    # (H&H §6.2) — Phase-1 ghi nhận là paraphrase không đánh; Phase-2 thêm
    # cho đối xứng VI 'đang giảm' (S057 TT) đã có hàng.
    ("S051", "coming down", "L", "synonym",
     "S041: prices falling in recent months", "med", None,
     "coming down ≈ falling — chuỗi động từ giảm", 1, None, None,
     "LC", None),
    ("S051", "we", "R", "personal",
     "RBA/Bullock (ngoại văn bản — quote)", "med", None,
     "ngoại quy chiếu; occ 1: lần 2 ('we remain') trong quote cùng "
     "chuỗi, không đánh", 1, None, None, "LC", "E"),
    ("S051", "she", "R", "personal",
     "S050: RBA governor Michele Bullock", "high", None, None, 1,
     None, None, "LC", "A"),
    ("S051", "RBA", "L", "repetition", "S050: RBA", "high", None,
     "RBA's December meeting; 'meeting' có hàng riêng Phase-2", 1, None,
     None, "LC", None),
    # [Phase-2] meeting ← convene/RBA meeting (S049/S030): mắt xích chuỗi
    # họp bị sót (H&H §6.2) — "RBA's December meeting"; VI 'cuộc họp'
    # (S057 TT) đã có hàng.
    ("S051", "meeting", "L", "repetition",
     "S049: will next convene in February — S030: the third RBA "
     "meeting", "high", None,
     "lặp meeting (December meeting)", 1, None, None, "LC", None),
]

TT = [
    # S002
    ("S002", "lạm phát căn bản", "L", "repetition",
     "S001: Lạm phát căn bản", "high", None, None, 1, None, None,
     "LC", None),
    ("S002", "mức thấp nhất", "L", "repetition",
     "S001: mức thấp nhất trong ba năm", "high", None, None, 1, None,
     None, "LC", None),
    ("S002", "giảm xuống", "L", "repetition",
     "S001: đã giảm xuống", "high", None, None, 1, None, None, "LC",
     None),
    # S003
    ("S003", "lạm phát", "L", "repetition",
     "S002: lạm phát căn bản", "high", None,
     "EN 'It' được hiện thực hóa thành 'lạm phát' nên không có R VI; "
     "'quý' lần đầu xuất hiện", 1, None, None, "LC", None),
    # S004
    ("S004", "Trong khi đó", "C", "temporal",
     "S003: Trong quý trước, lạm phát là 3,6%", "high", None, None, 1,
     None, None, "LC", None),
    ("S004", "tháng 12", "L", "repetition",
     "S002: trong tháng 12", "high", None,
     "VI dịch 'December quarter' thành 'tháng 12', ghi §8", 1, None,
     None, "LC", None),
    # S005
    ("S005", "ABS", "L", "repetition", "S002: (ABS)", "high", None,
     None, 1, None, None, "LC", None),
    ("S005", "đây", "R", "demonstrative",
     "S004: CPI tăng khiêm tốn 0,2 phần trăm", "high", None,
     "đây = mức tăng quý 12; đối ứng EN 'it'", 1, None, None, "LC",
     "A"),
    ("S005", "mức tăng hàng quý thấp nhất", "L", "repetition",
     "S002: mức thấp nhất", "high", None,
     "lặp 'thấp nhất'; 'tăng' khởi tạo chuỗi tăng", 1, None, None,
     "LC", None),
    # S006 (= EN S007)
    ("S006", "Những mức tăng này", "R", "demonstrative",
     "S005: những mức tăng hàng quý thấp nhất", "high", None,
     "hậu chỉ từ 'này'; đối ứng EN 'These rises'", 1, None, None,
     "LC", "A"),
    ("S006", "mức thấp nhất", "L", "repetition",
     "S005: mức tăng hàng quý thấp nhất", "high", None, None, 1, None,
     None, "LC", None),
    ("S006", "CPI giảm", "L", "repetition",
     "S002: giảm xuống", "high", None,
     "lặp chuỗi 'giảm'; 'CPI' lần đầu VI không đánh; đọc phụ: phép đối "
     "với 'Những mức tăng này' (TNT §30) — EN 'fell' (S007 ST) chọn phép "
     "đối, Phase-2 ghi §7", 1, None, None, "LC", None),
    # S007 (= EN S009)
    ("S007", "tăng nhiều nhất", "L", "repetition",
     "S005: mức tăng hàng quý thấp nhất", "high", None,
     "chuỗi 'tăng'; VI đảo cấu trúc (EN dùng bị động liệt kê)", 1,
     None, None, "LC", None),
    ("S007", "làm giảm mức tăng trưởng", "L", "repetition",
     "S006: CPI giảm", "high", None, "chuỗi 'giảm'", 1, None, None,
     "LC", None),
    # S008 (= EN S010)
    ("S008", "CPI", "L", "repetition", "S006: CPI", "high", None,
     None, 1, None, None, "LC", None),
    ("S008", "lạm phát", "L", "repetition",
     "S006: mức tăng — lạm phát (S002)", "high", None, None, 1, None,
     None, "LC", None),
    # [Phase-2] chi phí ← chi phí (S007): chuỗi 'chi phí' VI bị sót (TNT
    # §26 phép lặp) — VI tự thêm 'chi phí' ở S007 (EN dùng 'housing');
    # chuỗi VI: S007 → S008 → S028.
    ("S008", "chi phí", "L", "repetition",
     "S007: chi phí nhà ở và giao thông", "med", None,
     "lặp chi phí (chi phí hàng hóa và dịch vụ)", 1, None, None, "LC",
     None),
    # S009 (= EN S011)
    ("S009", "ABS", "L", "repetition", "S005: ABS", "high", None,
     None, 1, None, None, "LC", None),
    ("S009", "giá cả", "L", "repetition",
     "S007: Giá thuốc lá và rượu", "high", None,
     "biến động giá cả — lặp 'giá'", 1, None, None, "LC", None),
    ("S009", "hộ gia đình", "L", "repetition",
     "S008: hộ gia đình", "high", None, None, 1, None, None, "LC",
     None),
    ("S009", "nhà ở", "L", "repetition",
     "S007: chi phí nhà ở", "high", None, None, 1, None, None, "LC",
     None),
    ("S009", "phương tiện giao thông công cộng", "L", "repetition",
     "S007: giao thông", "high", None, None, 1, None, None, "LC",
     None),
    # S010 (= EN S012)
    ("S010", "Tuy nhiên", "C", "adversative",
     "S009: ABS thu thập dữ liệu", "high", None, None, 1, None, None,
     "LC", None),
    ("S010", "CPI", "L", "repetition", "S008: CPI", "high", None,
     None, 1, None, None, "LC", None),
    ("S010", "dữ liệu", "L", "repetition",
     "S009: thu thập dữ liệu", "high", None, None, 1, None, None,
     "LC", None),
    ("S010", "giá cả", "L", "repetition",
     "S009: biến động giá cả", "high", None, None, 1, None, None,
     "LC", None),
    ("S010", "thay đổi", "L", "repetition",
     "S008: tỷ lệ phần trăm thay đổi", "high", None,
     "những thay đổi về giá cả — hàng VI tách (EN gộp trong 'price "
     "changes')", 1, None, None, "LC", None),
    # S011 (= EN S013)
    ("S011", "lạm phát cơ bản", "L", "repetition",
     "S003: lạm phát", "high", None,
     "nguồn VI đổi 'căn bản'→'cơ bản', ghi §8", 1, None, None, "LC",
     None),
    ("S011", "biến động giá", "L", "repetition",
     "S010: biến động giá cả", "high", None,
     "lặp 'biến động giá' — đối ứng EN 'price swings'", 1, None,
     None, "LC", None),
    # S012 (= EN S014)
    ("S012", "mức này", "R", "demonstrative",
     "S011: mức trung bình cắt giảm", "high", None,
     "hậu chỉ từ 'này'; đối ứng EN 'It'", 1, None, None, "LC", "A"),
    ("S012", "ABS", "L", "repetition", "S010: ABS", "high", None,
     None, 1, None, None, "LC", None),
    ("S012", "tháng 12", "L", "repetition",
     "S004: trong tháng 12", "high", None,
     "đối ứng EN 'the December quarter'", 1, None, None, "LC", None),
    # S014 (= EN S018)
    # [Phase-2] những con số mới nhất ← dữ liệu (S010): mắt xích chuỗi
    # con số/dữ liệu bị sót, được S033 'số liệu mới nhất' cite (nhóm 12
    # bài học P28) — con số ≈ dữ liệu (H&H §6.2); EN 'the latest figures'
    # (S018 ST) cũng thêm hàng.
    ("S014", "những con số mới nhất", "L", "synonym",
     "S010: dữ liệu từ các thủ phủ của Úc", "med", None,
     "con số ≈ dữ liệu — đồng nghĩa chuỗi số liệu; ý chỉ toàn bộ số liệu "
     "lạm phát vừa công bố", 1, None, None, "LC", None),
    ("S014", "cắt giảm lãi suất", "L", "repetition",
     "S001: cắt giảm lãi suất", "high", None,
     "'những con số mới nhất' có hàng riêng Phase-2", 1, None, None,
     "LC", None),
    # S015 (= EN S019)
    ("S015", "cắt giảm lãi suất", "L", "repetition",
     "S014: hứa hẹn sẽ cắt giảm lãi suất", "high", None, None, 1,
     None, None, "LC", None),
    ("S015", "ông", "R", "personal",
     "S014: David Bassenese", "high", None, None, 1, None, None,
     "LC", "A"),
    # S016 (= EN S020)
    ("S016", "Tôi", "R", "personal",
     "Bassenese (ngoại văn bản — quote)", "med", None,
     "ngoại quy chiếu", 1, None, None, "LC", "E"),
    ("S016", "Ngân hàng trữ kim Úc", "L", "repetition",
     "S011: Ngân hàng trữ kim Úc (RBA)", "high", None, None, 1, None,
     None, "LC", None),
    ("S016", "những kết quả lạm phát này", "R", "demonstrative",
     "S002: lạm phát căn bản 3,2%", "high", None,
     "hậu chỉ từ 'này' + lặp 'lạm phát'", 1, None, None, "LC", "A"),
    ("S016", "hộ gia đình", "L", "repetition",
     "S009: hộ gia đình", "high", None, None, 1, None, None, "LC",
     None),
    ("S016", "cắt giảm lãi suất", "L", "repetition",
     "S015: cắt giảm lãi suất", "high", None,
     "câu quote kết bằng dấu phẩy như nguồn EN (S020), ghi §8", 1,
     None, None, "LC", None),
    # S017 (= EN S021)
    ("S017", "Tôi", "R", "personal",
     "Bassenese (ngoại văn bản — quote)", "med", None,
     "Tôi kỳ vọng — ngoại quy chiếu", 1, None, None, "LC", "E"),
    ("S017", "RBA", "L", "repetition", "S011: (RBA)", "high", None,
     None, 1, None, None, "LC", None),
    ("S017", "cắt giảm lãi suất", "L", "repetition",
     "S016: cắt giảm lãi suất", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] thêm ← S016: quy chiếu so sánh (H&H §2.5 "more") —
    # "thêm hai lần nữa" = thêm SO VỚI lần cắt tháng 2 đã nêu ở câu trước;
    # EN 'further' (S021 ST) đối xứng 1-1; 'thêm...nữa' S021 TT là NP hư chỉ
    # giả định nên không đánh, ghi §4.3.
    ("S017", "thêm", "R", "comparative",
     "S016: cắt giảm lãi suất tại cuộc họp chính sách ngày 17-18 tháng 2",
     "med", None,
     "quy chiếu so sánh: thêm = thêm với lần cắt tháng 2 câu trước (H&H "
     "§2.5)", 1, None, None, "LC", "A"),
    # [Phase-2] quý ← quý trước (S003): mắt xích chuỗi 'quý' VI bị sót —
    # EN 'quarterly' (S021 ST) cũng thêm hàng; hồi quy xa (liên kết bắc
    # cầu TNT §8).
    ("S017", "quý", "L", "repetition",
     "S003: trong quý trước", "high", None,
     "lặp quý (báo cáo CPI quý) — hồi quy xa S003", 1, None, None, "LC",
     None),
    ("S017", "lạm phát", "L", "repetition",
     "S016: những kết quả lạm phát này", "high", None, None, 1, None,
     None, "LC", None),
    ("S017", "CPI", "L", "repetition", "S010: CPI", "high", None,
     "báo cáo CPI quý", 1, None, None, "LC", None),
    ("S017", "tiếp tục giảm", "L", "repetition",
     "S012: đã tăng — chuỗi 'giảm' (S006)", "high", None,
     "chuỗi 'giảm' (khác 'cắt giảm'); EN 'declines' có hàng riêng "
     "Phase-2", 1, None, None, "LC", None),
    # S018 (= EN S022)
    ("S018", "Ông", "R", "personal",
     "S016: Tôi (Bassenese)", "high", None, None, 1, None, None,
     "LC", "A"),
    # [Phase-2] cũng ← S016–S017: nối additive liên câu (H&H §5.4) bị sót
    # — "Ông cũng đánh dấu" bổ sung nhận định thứ hai; EN 'also' (S022 ST)
    # đối xứng 1-1 (nhóm 11 bài học P22/P28).
    ("S018", "cũng", "C", "additive",
     "S017: RBA sẽ tiếp tục cắt giảm lãi suất thêm hai lần", "high",
     None, "bổ sung yếu tố thứ hai (sự sụt giảm); H&H §5.4", 1, None,
     None, "LC", None),
    ("S018", "lạm phát căn bản", "L", "repetition",
     "S011: lạm phát cơ bản", "high", None,
     "nguồn VI quay lại 'căn bản' sau 'cơ bản' (S011), ghi §8", 1,
     None, None, "LC", None),
    ("S018", "sụt giảm", "L", "repetition",
     "S017: tiếp tục giảm", "high", None, "chuỗi 'giảm'", 1, None,
     None, "LC", None),
    # S019 (= EN S024)
    ("S019", "Nhà kinh tế", "L", "repetition",
     "S014: Nhà kinh tế trưởng của Betashares", "high", None, None, 1,
     None, None, "LC", None),
    ("S019", "RBA", "L", "repetition", "S017: RBA", "high", None,
     "'lãi suất tiền mặt' khởi tạo chuỗi", 1, None, None, "LC", None),
    # [Phase-2] giảm ← sụt giảm (S018): mắt xích chuỗi 'giảm' bị sót (TNT
    # §26) — "không giảm lãi suất tiền mặt"; EN 'reduce' (S024 ST) là
    # đồng nghĩa chuỗi cut — dịch chuyển EN synonym ↔ VI repetition.
    ("S019", "giảm", "L", "repetition",
     "S018: sự sụt giảm", "med", None,
     "lặp chuỗi 'giảm' (không giảm lãi suất tiền mặt)", 1, None, None,
     "LC", None),
    # [Phase-2] lãi suất tiền mặt ← cắt giảm lãi suất (S017): mắt xích
    # chuỗi lãi suất bị sót, được S020 và S035 cite (nhóm 12 bài học
    # P28); 'tiền mặt' khởi tạo chuỗi lãi suất tiền mặt.
    ("S019", "lãi suất tiền mặt", "L", "repetition",
     "S017: tiếp tục cắt giảm lãi suất thêm hai lần", "high", None,
     "lặp 'lãi suất', thêm 'tiền mặt' khởi tạo chuỗi; được S020/S035 "
     "cite làm tiền trạm", 1, None, None, "LC", None),
    # S020 (= EN S025)
    ("S020", "cắt giảm lãi suất", "L", "repetition",
     "S019: không giảm lãi suất tiền mặt", "high", None, None, 1, None,
     None, "LC", None),
    ("S020", "họp chính sách", "L", "repetition",
     "S016: cuộc họp chính sách ngày 17-18 tháng 2", "high", None,
     "lặp 'họp chính sách'", 1, None, None, "LC", None),
    ("S020", "RBA", "L", "repetition", "S019: RBA", "high", None,
     "chương trình họp chính sách của RBA", 1, None, None, "LC",
     None),
    # [Phase-2] giữ nguyên ← không giảm (S019): mắt xích chuỗi 'giữ
    # nguyên' bị sót, được S055 'giữ nguyên lãi suất' cite (nhóm 12 bài
    # học P28) — giữ nguyên ≈ không giảm (phép thế đẳng nghĩa TNT §31;
    # H&H §6.2 synonym); EN 'a hold' (S025 ST) là lần đầu trong câu nên
    # không có hàng.
    ("S020", "giữ nguyên", "L", "synonym",
     "S019: không giảm lãi suất tiền mặt", "med", None,
     "giữ nguyên ≈ không giảm — đẳng nghĩa; hơi nghiêng về phía giữ "
     "nguyên", 1, None, None, "LC", None),
    ("S020", "chúng tôi", "R", "personal",
     "Shivadekar + đồng nghiệp (ngoại văn bản — quote)", "med", None,
     "theo quan điểm của chúng tôi — ngoại quy chiếu", 1, None, None,
     "LC", "E"),
    ("S020", "bà", "R", "personal",
     "S019: Devika Shivadekar", "high", None, None, 1, None, None,
     "LC", "A"),
    # S021 (= EN S026)
    ("S021", "RBA", "L", "repetition", "S020: RBA", "high", None,
     None, 1, None, None, "LC", None),
    ("S021", "lạm phát", "L", "repetition",
     "S018: lạm phát căn bản", "high", None, None, 1, None, None,
     "LC", None),
    ("S021", "trung bình được cắt giảm", "L", "repetition",
     "S011: mức trung bình cắt giảm", "high", None,
     "VI đảo cụm 'mức trung bình cắt giảm' → 'trung bình được cắt "
     "giảm', ghi §8", 1, None, None, "LC", None),
    ("S021", "điểm dữ liệu", "L", "repetition",
     "S010: dữ liệu", "high", None, None, 1, None, None, "LC", None),
    ("S021", "mức giảm", "L", "repetition",
     "S018: sự sụt giảm", "high", None,
     "mức giảm 'bền vững' — chuỗi giảm; chủ ngữ vế 'thích chờ' bị lược "
     "(ngữ pháp bắt buộc), không đánh", 1, None, None, "LC", None),
    # S022 (= EN S027)
    ("S022", "Nhưng", "C", "adversative",
     "S021: RBA thích chờ thêm dữ liệu", "high", None, None, 1, None,
     None, "LC", None),
    ("S022", "xu hướng giảm phát", "L", "repetition",
     "S021: lạm phát trung bình", "high", None,
     "cùng hình vị 'phát' (lạm phát→giảm phát) + 'giảm' tiếp chuỗi; "
     "đối ứng EN 'disinflationary'", 1, None, None, "LC", None),
    # [Phase-2] rộng hơn ← S021: quy chiếu so sánh (H&H §2.5; tiền lệ P28
    # 'thực tế hơn') — "rộng hơn" = rộng hơn mức giảm trimmed mean câu
    # trước; EN 'broader' (S027 ST) đối xứng 1-1; cùng NP có hàng L riêng
    # trên 'xu hướng giảm phát' (tiền lệ P21 'lừa đảo'+'khác').
    ("S022", "rộng hơn", "R", "comparative",
     "S021: mức giảm 'bền vững' trong lạm phát trung bình", "med", None,
     "so sánh phạm vi: rộng hơn = rộng hơn mức giảm đã nêu câu trước (H&H "
     "§2.5)", 1, None, None, "LC", "A"),
    # S023 — VI TỰ SINH (BDO Magnusson)
    ("S023", "tháng 12", "L", "repetition",
     "S012: trong tháng 12", "high", None,
     "câu VI tự sinh — không có EN; 'số liệu' lần đầu VI", 1, None,
     None, "LC", None),
    # [Phase-2] người nắm giữ thế chấp ← người nắm giữ thế chấp (S016):
    # chuỗi 'người nắm giữ thế chấp' bị sót (TNT §26 phép lặp) — câu VI
    # tự sinh bắc cầu về quote Bassenese ở vùng dùng chung.
    ("S023", "người nắm giữ thế chấp", "L", "repetition",
     "S016: người nắm giữ thế chấp đang gặp khó khăn", "med", None,
     "lặp NP người nắm giữ thế chấp; VI tự sinh", 1, None, None, "LC",
     None),
    ("S023", "cắt giảm lãi suất", "L", "repetition",
     "S020: cắt giảm lãi suất", "high", None, "VI tự sinh", 1, None,
     None, "LC", None),
    # S024 — VI TỰ SINH
    # [Phase-2] nền kinh tế ← nền kinh tế (S015): mắt xích chuỗi 'nền
    # kinh tế' bị sót, được S051 cite (nhóm 12 bài học P28) — TNT §26;
    # S015 là lần đầu chuỗi nên không có hàng.
    ("S024", "nền kinh tế", "L", "repetition",
     "S015: nền kinh tế xứng đáng được cắt giảm lãi suất", "high", None,
     "lặp nền kinh tế (nền kinh tế trong nước); VI tự sinh", 1, None,
     None, "LC", None),
    ("S024", "tôi", "R", "personal",
     "Magnusson (ngoại văn bản — quote)", "med", None,
     "VI tự sinh; 'chúng ta' hư chỉ chung, không đánh", 1, None, None,
     "LC", "E"),
    ("S024", "RBA", "L", "repetition", "S022: RBA (S021)", "high",
     None, "VI tự sinh", 1, None, None, "LC", None),
    ("S024", "cắt giảm lãi suất", "L", "repetition",
     "S023: cắt giảm lãi suất", "high", None,
     "đợt cắt giảm lãi suất đầu tiên; VI tự sinh", 1, None, None,
     "LC", None),
    ("S024", "cuộc họp", "L", "repetition",
     "S020: chương trình họp chính sách", "high", None,
     "cuộc họp sắp tới; VI tự sinh", 1, None, None, "LC", None),
    ("S024", "ông", "R", "personal",
     "S023: Anders Magnusson", "high", None,
     "occ 2 vì 'công bố' chứa 'ông'; lần 2 mới là đại từ; VI tự sinh",
     2, None, None, "LC", "A"),
    # S025 — VI TỰ SINH
    ("S025", "Tuy nhiên", "C", "adversative",
     "S024: cánh cửa đã mở cho đợt cắt giảm", "high", None,
     "VI tự sinh; 'chúng ta' hư chỉ, không đánh", 1, None, None, "LC",
     None),
    ("S025", "RBA", "L", "repetition", "S024: RBA", "high", None,
     "VI tự sinh", 1, None, None, "LC", None),
    ("S025", "lạm phát căn bản", "L", "repetition",
     "S018: lạm phát căn bản", "high", None,
     "'phạm vi mục tiêu 2-3%' khởi tạo chuỗi mục tiêu; VI tự sinh", 1,
     None, None, "LC", None),
    # [Phase-2] quý ← quý (S017): mắt xích chuỗi 'quý' bị sót (TNT §26) —
    # "đợi thêm một quý nữa"; VI tự sinh nên conf med.
    ("S025", "quý", "L", "repetition",
     "S017: báo cáo CPI quý tiếp theo", "med", None,
     "lặp quý (một quý nữa); VI tự sinh", 1, None, None, "LC", None),
    # S026 — VI TỰ SINH
    ("S026", "Nhưng", "C", "adversative",
     "S025: có thể cần đợi thêm một quý", "high", None, "VI tự sinh",
     1, None, None, "LC", None),
    ("S026", "ông", "R", "personal", "S024: ông (Magnusson)", "high",
     None, "VI tự sinh", 1, None, None, "LC", "A"),
    # [Phase-2] cũng ← S025: nối additive liên câu (H&H §5.4) bị sót —
    # "Nhưng ông cũng cho biết" bổ sung nhận định thứ hai của Magnusson;
    # VI tự sinh nên không có đối ứng EN (nhóm 11 bài học P22/P28).
    ("S026", "cũng", "C", "additive",
     "S025: có thể cần phải đợi thêm một quý", "med", None,
     "bổ sung nhận định (bất ổn toàn cầu) ngoài nhận định tích cực; H&H "
     "§5.4", 1, None, None, "LC", None),
    ("S026", "cắt giảm lãi suất", "L", "repetition",
     "S024: đợt cắt giảm lãi suất", "high", None, "VI tự sinh", 1,
     None, None, "LC", None),
    # S027 — VI TỰ SINH
    ("S027", "ông", "R", "personal", "S026: ông (Magnusson)", "high",
     None, "VI tự sinh", 1, None, None, "LC", "A"),
    ("S027", "Úc", "L", "repetition",
     "S010: các thủ phủ của Úc", "high", None,
     "Sự phụ thuộc của Úc; VI tự sinh", 1, None, None, "LC", None),
    # S028 — VI TỰ SINH
    ("S028", "Úc", "L", "repetition", "S027: của Úc", "high", None,
     "nền kinh tế Úc; VI tự sinh; 'những yếu tố này' trong câu không "
     "đánh", 1, None, None, "LC", None),
    ("S028", "tăng chi phí", "L", "repetition",
     "S007: tăng nhiều nhất", "med", None,
     "chuỗi 'tăng' — ngữ cảnh mới (chi phí nhập khẩu); VI tự sinh", 1,
     None, None, "LC", None),
    # S029 — VI TỰ SINH (VanEck)
    ("S029", "CPI", "L", "repetition", "S017: CPI", "high", None,
     "Bản công bố CPI hôm nay; VI tự sinh", 1, None, None, "LC",
     None),
    # [Phase-2] kết quả ← kết quả (S016): mắt xích chuỗi 'kết quả' bị sót
    # (TNT §26) — "một kết quả đáng mừng"; S031 'kết quả này' truy hồi
    # qua S029; VI tự sinh nên conf med.
    ("S029", "kết quả", "L", "repetition",
     "S016: những kết quả lạm phát này", "med", None,
     "lặp kết quả (kết quả đáng mừng); VI tự sinh", 1, None, None,
     "LC", None),
    ("S029", "RBA", "L", "repetition", "S026: RBA", "high", None,
     "VI tự sinh", 1, None, None, "LC", None),
    # S030 — VI TỰ SINH
    ("S030", "Tuy nhiên", "C", "adversative",
     "S029: kết quả đáng mừng", "high", None, "VI tự sinh", 1, None,
     None, "LC", None),
    ("S030", "Úc", "L", "repetition", "S028: nền kinh tế Úc", "high",
     None, "đồng đô la Úc; VI tự sinh", 1, None, None, "LC", None),
    ("S030", "RBA", "L", "repetition", "S029: RBA", "high", None,
     "VI tự sinh", 1, None, None, "LC", None),
    ("S030", "thận trọng", "L", "repetition",
     "S019: vẫn thận trọng", "high", None,
     "RBA sẽ thận trọng; VI tự sinh", 1, None, None, "LC", None),
    ("S030", "đợt cắt giảm", "L", "repetition",
     "S024: đợt cắt giảm lãi suất", "high", None,
     "đợt cắt giảm đầu tiên; VI tự sinh", 1, None, None, "LC", None),
    # [Phase-2] quý ← quý (S025): mắt xích chuỗi 'quý' bị sót (TNT §26) —
    # "cho đến quý 2 năm nay"; VI tự sinh nên conf med.
    ("S030", "quý", "L", "repetition",
     "S025: đợi thêm một quý nữa", "med", None,
     "lặp quý (quý 2 năm nay); VI tự sinh", 1, None, None, "LC", None),
    # S031 — VI TỰ SINH (IFM)
    ("S031", "nhà kinh tế trưởng", "L", "repetition",
     "S014: Nhà kinh tế trưởng của Betashares", "high", None,
     "VI tự sinh (IFM Joiner)", 1, None, None, "LC", None),
    ("S031", "kết quả này", "R", "demonstrative",
     "S029: Bản công bố CPI hôm nay", "high", None,
     "hậu chỉ từ 'này'; VI tự sinh", 1, None, None, "LC", "A"),
    ("S031", "lạm phát", "L", "repetition",
     "S025: lạm phát căn bản", "high", None, "VI tự sinh", 1, None,
     None, "LC", None),
    ("S031", "phạm vi mục tiêu", "L", "repetition",
     "S025: phạm vi mục tiêu từ 2 đến 3 phần trăm", "high", None,
     "VI tự sinh", 1, None, None, "LC", None),
    ("S031", "bền vững", "L", "repetition",
     "S021: mức giảm 'bền vững'", "high", None,
     "echo từ quote Shivadekar; VI tự sinh", 1, None, None, "LC",
     None),
    # S033 (= EN S029)
    ("S033", "số liệu mới nhất", "L", "repetition",
     "S014: những con số mới nhất", "high", None,
     "lặp 'mới nhất'; 'con số'→'số liệu' — nguồn VI đổi từ, ghi §8", 1,
     None, None, "LC", None),
    # [Phase-2] dự đoán ← tiểu đề S013: mắt xích chuỗi 'dự đoán' bị sót,
    # được S036 'dự đoán' cite (nhóm 12 bài học P28) — tiểu đề làm tiền
    # trạm, không gán nhãn trên tiểu đề (quy ước); TNT §26.
    ("S033", "dự đoán", "L", "repetition",
     "S013: 'Dự đoán của các nhà kinh tế' — tiểu đề", "med", None,
     "lặp dự đoán; tiểu đề làm tiền trạm; được S036 cite", 1, None,
     None, "LC", None),
    ("S033", "cắt giảm", "L", "repetition",
     "S031: cắt giảm lãi suất (S030)", "high", None,
     "lãi suất sẽ được cắt giảm", 1, None, None, "LC", None),
    ("S033", "lãi suất", "L", "repetition",
     "S031: cắt giảm lãi suất", "high", None,
     "occ 1: lần 2 ('lãi suất tiền mặt') trong câu cùng chuỗi, không "
     "đánh", 1, None, None, "LC", None),
    ("S033", "RBA", "L", "repetition", "S031: RBA", "high", None,
     "lần họp tiếp theo của RBA", 1, None, None, "LC", None),
    # S034 — VI TỰ SINH (Westpac Luci Ellis)
    ("S034", "Westpac", "L", "repetition",
     "S033: Westpac dự đoán", "high", None, "VI tự sinh", 1, None,
     None, "LC", None),
    ("S034", "cắt giảm lãi suất", "L", "repetition",
     "S033: cắt giảm", "high", None,
     "occ 1: lần 2 ('cắt giảm lãi suất tiền mặt') trong câu cùng "
     "chuỗi, không đánh; 'bà' trong câu chỉ Ellis, không đánh; VI tự "
     "sinh", 1, None, None, "LC", None),
    ("S034", "Ngân hàng Dự trữ", "L", "repetition",
     "S011: Ngân hàng trữ kim Úc (RBA)", "med", None,
     "biến thể tên (trữ kim → Dự trữ), ghi §8; VI tự sinh", 1, None,
     None, "LC", None),
    ("S034", "cuộc họp", "L", "repetition",
     "S024: cuộc họp sắp tới", "high", None,
     "cuộc họp hội đồng quản trị; VI tự sinh", 1, None, None, "LC",
     None),
    # S035 (= EN S030)
    ("S035", "Nhưng", "C", "adversative",
     "S034: Westpac dự đoán cắt giảm vào tháng 2", "high", None, None,
     1, None, None, "LC", None),
    ("S035", "cuộc họp thứ ba", "L", "repetition",
     "S020: họp chính sách — cuộc họp (S024)", "high", None,
     "lặp 'họp'; hàng VI tách (EN gộp trong 'RBA meeting')", 1, None,
     None, "LC", None),
    ("S035", "RBA", "L", "repetition", "S034: Ngân hàng Dự trữ",
     "high", None, None, 1, None, None, "LC", None),
    ("S035", "lãi suất tiền mặt", "L", "repetition",
     "S019: lãi suất tiền mặt", "high", None, None, 1, None, None,
     "LC", None),
    # S036 (= EN S031)
    ("S036", "Bốn ngân hàng lớn", "L", "repetition",
     "S032: 'Bốn ngân hàng lớn' — tiểu đề", "high", None,
     "tiểu đề làm tiền trạm", 1, None, None, "LC", None),
    # [Phase-2] cũng ← S035: nối additive liên câu (H&H §5.4) bị sót —
    # "Bốn ngân hàng lớn cũng có những dự đoán khác nhau"; EN 'also'
    # (S031 ST) đối xứng 1-1 (nhóm 11 bài học P22/P28).
    ("S036", "cũng", "C", "additive",
     "S035: NAB không đồng ý và dự đoán", "high", None,
     "bổ sung khía cạnh thứ hai (số lần cắt); H&H §5.4", 1, None, None,
     "LC", None),
    ("S036", "dự đoán", "L", "repetition",
     "S033: Westpac dự đoán", "high", None, None, 1, None, None,
     "LC", None),
    ("S036", "cắt giảm lãi suất", "L", "repetition",
     "S035: cắt giảm lãi suất — S033", "high", None,
     "số lần cắt giảm lãi suất vào năm 2025", 1, None, None, "LC",
     None),
    # S037 (= EN S032)
    # [Phase-2] ANZ ← ANZ (S033): chuỗi tên riêng ANZ bị sót — TNT §26;
    # EN 'ANZ' (S032 ST) đối xứng 1-1.
    ("S037", "ANZ", "L", "repetition",
     "S033: Ngân hàng Khối thịnh vượng chung (CBA) và ANZ", "high",
     None, "lặp tên ngân hàng ANZ", 1, None, None, "LC", None),
    # [Phase-2] dự báo ← dự đoán (S036): đồng nghĩa chuỗi dự đoán bị sót,
    # được S045 'dự báo' cite (nhóm 12 bài học P28) — H&H §6.2; EN
    # 'forecast' (S032 ST) đối xứng; 'dự kiến' là tân từ khác (không lặp
    # 'kỳ vọng') nên không đánh, ghi §7.
    ("S037", "dự báo", "L", "synonym",
     "S036: những dự đoán khác nhau", "high", None,
     "dự báo ≈ dự đoán — chuỗi dự đoán; được S045 cite", 1, None, None,
     "LC", None),
    ("S037", "thận trọng nhất", "L", "repetition",
     "S030: sẽ thận trọng", "high", None, None, 1, None, None, "LC",
     None),
    ("S037", "cắt giảm", "L", "repetition",
     "S036: cắt giảm lãi suất", "high", None,
     "occ 1: lần 2 ('bốn lần cắt giảm') trong câu cùng chuỗi, không "
     "đánh", 1, None, None, "LC", None),
    ("S037", "CBA và Westpac", "L", "repetition",
     "S033: CBA và ANZ — Westpac (S033)", "high", None, None, 1, None,
     None, "LC", None),
    # S038 (= EN S033)
    ("S038", "NAB", "L", "repetition",
     "S035: NAB không đồng ý", "high", None, None, 1, None, None,
     "LC", None),
    ("S038", "dự đoán", "L", "repetition",
     "S036: dự đoán", "high", None, None, 1, None, None, "LC", None),
    ("S038", "cắt giảm", "L", "repetition",
     "S037: cắt giảm", "high", None, "năm lần cắt giảm", 1, None,
     None, "LC", None),
    # [Phase-2] ∅ sau 'nhiều nhất' (H&H §4.2): "dự đoán nhiều nhất ∅{lần
    # cắt giảm}" — đầu từ lược hồi phục được từ S036–S037 → [LC] (tỉnh
    # lược yếu TNT §37); EN 'the most' ∅ (S033 ST) đối xứng 1-1 — cặp
    # E↔E hiếm (NTT 2020 §5: hai đầu cùng chọn ∅).
    ("S038", None, "E", "nominal",
     "S037: hai lần cắt giảm, bốn lần cắt giảm", "high", None,
     "[LC] lược đầu từ sau nhiều nhất ∅ {lần cắt giảm}; H&H §4.2; TNT "
     "§37", 1, "nhiều nhất", "{lần cắt giảm}", "LC", None),
    # S039 — VI TỰ SINH (khối Chính phủ; tiểu đề + câu lồng)
    ("S039", "Chính phủ Úc", "L", "repetition",
     "S030: đồng đô la Úc", "high", None,
     "lặp 'Úc'; tiểu đề lồng 'Chính phủ hoan nghênh…'; VI tự sinh", 1,
     None, None, "LC", None),
    ("S039", "lạm phát giảm", "L", "repetition",
     "S031: lạm phát", "high", None,
     "kết chuỗi lạm phát + giảm; chọn phần câu sau tiểu đề; VI tự sinh",
     1, None, None, "LC", None),
    ("S039", "mức thấp nhất", "L", "repetition",
     "S002: mức thấp nhất", "high", None,
     "hồi quy xa về S002; đối ứng EN 'its lowest rate' (S001); VI tự "
     "sinh", 1, None, None, "LC", None),
    # S040 — VI TỰ SINH
    ("S040", "dữ liệu", "L", "repetition",
     "S010: dữ liệu", "high", None,
     "dữ liệu từ ABS; VI tự sinh", 1, None, None, "LC", None),
    ("S040", "ABS", "L", "repetition", "S012: ABS", "high", None,
     "VI tự sinh", 1, None, None, "LC", None),
    ("S040", "bền vững", "L", "repetition",
     "S031: bền vững", "high", None,
     "echo quote Joiner/Shivadekar; VI tự sinh", 1, None, None, "LC",
     None),
    ("S040", "chống lạm phát", "L", "repetition",
     "S039: lạm phát giảm", "high", None, "lặp 'lạm phát'; VI tự sinh",
     1, None, None, "LC", None),
    ("S040", "chúng tôi", "R", "personal",
     "chính phủ/Chalmers (ngoại văn bản — quote)", "med", None,
     "VI tự sinh; 'ông' trong câu chỉ Chalmers, không đánh", 1, None,
     None, "LC", "E"),
    # S041 — VI TỰ SINH
    ("S041", "Ông Chalmers", "L", "repetition",
     "S040: Jim Chalmers", "high", None,
     "lặp tên riêng + danh xưng; VI tự sinh", 1, None, None, "LC",
     None),
    ("S041", "các con số này", "R", "demonstrative",
     "S040: dữ liệu từ ABS", "high", None,
     "hậu chỉ từ 'này' + lặp 'con số' (S014); VI tự sinh", 1, None,
     None, "LC", "A"),
    # S042 — VI TỰ SINH
    ("S042", "Đây", "R", "demonstrative",
     "S041: các con số này tốt hơn mong đợi", "high", None,
     "Đây = tình hình lạm phát; 'điều đó' trong câu không đánh; VI tự "
     "sinh; 'chúng ta' hư chỉ", 1, None, None, "LC", "A"),
    ("S042", "tiến bộ", "L", "repetition",
     "S040: tiến bộ đáng kể và bền vững", "high", None,
     "nhiều tiến bộ hơn; VI tự sinh", 1, None, None, "LC", None),
    ("S042", "ông", "R", "personal",
     "S041: Ông Chalmers", "high", None, "VI tự sinh", 1, None, None,
     "LC", "A"),
    # S043 — VI TỰ SINH
    ("S043", "Lạm phát", "L", "repetition",
     "S042: tiến bộ — lạm phát (S040 chống lạm phát)", "high", None,
     "VI tự sinh; câu quote chính trị so sánh hai đảng", 1, None, None,
     "LC", None),
    ("S043", "tăng", "L", "repetition",
     "S028: tăng chi phí", "high", None,
     "chuỗi 'tăng'; VI tự sinh", 1, None, None, "LC", None),
    ("S043", "giảm", "L", "repetition",
     "S039: lạm phát giảm", "high", None,
     "thấp hơn và giảm; VI tự sinh", 1, None, None, "LC", None),
    # S044 — VI TỰ SINH
    ("S044", "Lạm phát", "L", "repetition",
     "S043: Lạm phát", "high", None, "VI tự sinh", 1, None, None,
     "LC", None),
    # S045 — VI TỰ SINH
    ("S045", "Ông", "R", "personal",
     "S042: ông (Chalmers)", "high", None, "VI tự sinh", 1, None,
     None, "LC", "A"),
    ("S045", "lạm phát", "L", "repetition",
     "S044: Lạm phát", "high", None, "VI tự sinh", 1, None, None,
     "LC", None),
    ("S045", "đang giảm", "L", "repetition",
     "S043: giảm", "high", None,
     "chuỗi 'giảm'; EN paraphrase 'coming down' không đánh riêng; VI "
     "tự sinh", 1, None, None, "LC", None),
    ("S045", "dự báo", "L", "repetition",
     "S037: CBA và Westpac dự báo", "high", None,
     "dự báo của Bộ Tài chính; VI tự sinh", 1, None, None, "LC",
     None),
    ("S045", "Úc", "L", "repetition",
     "S039: Chính phủ Úc", "high", None, "VI tự sinh", 1, None, None,
     "LC", None),
    ("S045", "đi đúng hướng", "L", "repetition",
     "S025: lạm phát căn bản đang đi đúng hướng", "high", None,
     "echo quote Magnusson; VI tự sinh", 1, None, None, "LC", None),
    # S046 — VI TỰ SINH
    ("S046", "RBA", "L", "repetition",
     "S034: Ngân hàng Dự trữ", "high", None, "VI tự sinh", 1, None,
     None, "LC", None),
    ("S046", "cắt giảm lãi suất", "L", "repetition",
     "S045: cắt giảm lãi suất — S043 (S038)", "high", None,
     "VI tự sinh", 1, None, None, "LC", None),
    ("S046", "Đảng Lao động", "L", "repetition",
     "S043: Đảng Lao động", "high", None, "VI tự sinh", 1, None, None,
     "LC", None),
    # S047 — VI TỰ SINH
    ("S047", "Đảng Lao động", "L", "repetition",
     "S046: Đảng Lao động", "high", None, "VI tự sinh", 1, None, None,
     "LC", None),
    ("S047", "cắt giảm lãi suất", "L", "repetition",
     "S046: cắt giảm lãi suất", "high", None,
     "occ 1: lần 2 ('lãi suất khác') trong câu cùng chuỗi lãi suất, "
     "không đánh; VI tự sinh", 1, None, None, "LC", None),
    ("S047", "bầu cử", "L", "repetition",
     "S001: trước bầu cử", "high", None,
     "hồi quy xa về S001; VI tự sinh", 1, None, None, "LC", None),
    # [Phase-2] quyết định ← quyết định (S046): mắt xích chuỗi 'quyết
    # định' bị sót (TNT §26) — chuỗi VI tự sinh (S046 → S047 → S053)
    # không có đối ứng EN (EN chỉ có 'its decisions' trong câu, §4.3).
    ("S047", "quyết định", "L", "repetition",
     "S046: Bất kỳ quyết định nào của RBA", "med", None,
     "lặp quyết định (một quyết định về lãi suất khác); VI tự sinh", 1,
     None, None, "LC", None),
    # S048 — VI TỰ SINH
    ("S048", "Nhưng", "C", "adversative",
     "S047: hai cơ hội cắt giảm trước bầu cử", "high", None,
     "VI tự sinh", 1, None, None, "LC", None),
    ("S048", "dữ liệu", "L", "repetition",
     "S040: dữ liệu từ ABS", "high", None, "VI tự sinh", 1, None,
     None, "LC", None),
    ("S048", "tháng 12", "L", "repetition",
     "S023: các số liệu tháng 12", "high", None, "VI tự sinh", 1,
     None, None, "LC", None),
    ("S048", "lạm phát cơ bản", "L", "repetition",
     "S011: lạm phát cơ bản", "high", None,
     "nguồn VI đổi 'căn bản'→'cơ bản', ghi §8; VI tự sinh", 1, None,
     None, "LC", None),
    ("S048", "mục tiêu", "L", "repetition",
     "S031: phạm vi mục tiêu", "high", None,
     "vượt mục tiêu; VI tự sinh", 1, None, None, "LC", None),
    # S049 — VI TỰ SINH
    ("S049", "Nó", "R", "personal",
     "S048: lạm phát cơ bản", "high", None, "VI tự sinh", 1, None,
     None, "LC", "A"),
    ("S049", "người Úc", "L", "repetition",
     "S045: Úc", "high", None, "VI tự sinh", 1, None, None, "LC",
     None),
    ("S049", "thay đổi", "L", "repetition",
     "S010: những thay đổi về giá cả", "high", None,
     "không thay đổi nhiều; VI tự sinh", 1, None, None, "LC", None),
    ("S049", "ông Taylor", "L", "repetition",
     "S048: Angus Taylor", "high", None,
     "lặp tên riêng + danh xưng; VI tự sinh", 1, None, None, "LC",
     None),
    # S050 — VI TỰ SINH
    ("S050", "người Úc", "L", "repetition",
     "S049: người Úc", "high", None,
     "mức sống của người Úc; 'chúng ta' hư chỉ, 'nỗi đau đó' trong "
     "câu không đánh; VI tự sinh", 1, None, None, "LC", None),
    # S051 — VI TỰ SINH
    ("S051", "quốc gia ngang hàng", "L", "repetition",
     "S050: các quốc gia ngang hàng", "high", None, "VI tự sinh", 1,
     None, None, "LC", None),
    ("S051", "chứng kiến", "L", "repetition",
     "S050: đã chứng kiến", "high", None,
     "chứng kiến tình trạng đó — 'đó' trong câu không đánh; VI tự "
     "sinh", 1, None, None, "LC", None),
    ("S051", "nền kinh tế", "L", "repetition",
     "S024: nền kinh tế trong nước", "high", None, "VI tự sinh", 1,
     None, None, "LC", None),
    # [Phase-2] quý ← quý (S030): mắt xích chuỗi 'quý' bị sót (TNT §26)
    # — "bảy quý liên tiếp"; VI tự sinh nên conf med.
    ("S051", "quý", "L", "repetition",
     "S030: quý 2 năm nay", "med", None,
     "lặp quý (bảy quý liên tiếp); VI tự sinh", 1, None, None, "LC",
     None),
    # S053 (= EN S047)
    ("S053", "RBA", "L", "repetition", "S048: RBA", "high", None,
     None, 1, None, None, "LC", None),
    ("S053", "lạm phát", "L", "repetition",
     "S048: lạm phát cơ bản", "high", None,
     "'đây' và 'của họ' trong câu không đánh", 1, None, None, "LC",
     None),
    ("S053", "lãi suất", "L", "repetition",
     "S047: cắt giảm lãi suất", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] yếu tố chính ← yếu tố quan trọng (S018): chuỗi 'yếu tố' bị
    # sót (H&H §6.2) — EN 'a key factor' (S047 ST) đối xứng 1-1.
    ("S053", "yếu tố chính", "L", "repetition",
     "S018: một yếu tố quan trọng", "med", None,
     "lặp yếu tố (quan trọng → chính)", 1, None, None, "LC", None),
    # [Phase-2] quyết định ← quyết định (S047): mắt xích chuỗi 'quyết
    # định' (nhóm 4) — tiếp chuỗi khối tự sinh; EN 'its decisions' trong
    # câu → [TC], ghi §4.3.
    ("S053", "quyết định", "L", "repetition",
     "S047: một quyết định về lãi suất khác", "med", None,
     "lặp quyết định (quyết định tăng hoặc giảm lãi suất)", 1, None,
     None, "LC", None),
    # [Phase-2] tăng ← tăng (S043): mắt xích chuỗi 'tăng' bị sót, được
    # S054 'tăng lãi suất' cite (nhóm 12 bài học P28) — TNT §26; cặp
    # tăng↔giảm trong câu là phép đối [TC] (TNT §30).
    ("S053", "tăng", "L", "repetition",
     "S043: Lạm phát cao hơn và tăng", "high", None,
     "lặp chuỗi 'tăng' (tăng hoặc giảm lãi suất)", 1, None, None, "LC",
     None),
    # [Phase-2] giảm ← đang giảm (S045): mắt xích chuỗi 'giảm' bị sót
    # (TNT §26) — EN 'lower' (S047 ST) là đồng nghĩa chuỗi cut; dịch
    # chuyển EN synonym ↔ VI repetition, ghi §7.
    ("S053", "giảm", "L", "repetition",
     "S045: lạm phát đang giảm nhanh hơn", "med", None,
     "lặp chuỗi 'giảm' (tăng hoặc giảm lãi suất)", 1, None, None, "LC",
     None),
    # S054 (= EN S048)
    ("S054", "Mục tiêu lạm phát", "L", "repetition",
     "S031: phạm vi mục tiêu + S053: lạm phát", "high", None,
     "kết chuỗi mục tiêu + lạm phát; tiền trạm trong khối VI tự sinh "
     "(S025, S031)", 1, None, None, "LC", None),
    # [Phase-2] Úc ← người Úc (S050): mắt xích chuỗi 'Úc' bị sót (TNT
    # §26) — EN 'Australia's' (S048 ST) đối xứng 1-1.
    ("S054", "Úc", "L", "repetition",
     "S050: mức sống của người Úc", "high", None,
     "lặp Úc (Mục tiêu lạm phát chính thức của Úc)", 1, None, None,
     "LC", None),
    ("S054", "giảm lạm phát", "L", "repetition",
     "S053: lạm phát", "high", None, "nỗ lực giảm lạm phát", 1, None,
     None, "LC", None),
    ("S054", "RBA", "L", "repetition", "S053: RBA", "high", None,
     None, 1, None, None, "LC", None),
    ("S054", "tăng lãi suất", "L", "repetition",
     "S053: tăng hoặc giảm lãi suất", "high", None,
     "kết chuỗi tăng + lãi suất; EN 'raising' có hàng riêng", 1, None,
     None, "LC", None),
    # S055 (= EN S049)
    ("S055", "tăng lãi suất", "L", "repetition",
     "S054: tăng lãi suất", "high", None, None, 1, None, None, "LC",
     None),
    ("S055", "RBA", "L", "repetition", "S054: RBA", "high", None,
     None, 1, None, None, "LC", None),
    ("S055", "giữ nguyên lãi suất", "L", "repetition",
     "S020: hơi nghiêng về phía giữ nguyên", "high", None,
     "kết chuỗi giữ nguyên (S020) + lãi suất", 1, None, None, "LC",
     None),
    ("S055", "mục tiêu lãi suất tiền mặt", "L", "repetition",
     "S054: Mục tiêu lạm phát + S035: lãi suất tiền mặt", "high",
     None, "kết chuỗi mục tiêu + lãi suất tiền mặt", 1, None, None,
     "LC", None),
    # [Phase-2] họp ← cuộc họp (S035): mắt xích chuỗi 'họp' bị sót (TNT
    # §26) — "sẽ họp vào tháng 2"; EN 'convene' (S049 ST) đối xứng 1-1.
    ("S055", "họp", "L", "repetition",
     "S035: cuộc họp thứ ba của RBA", "high", None,
     "lặp 'họp' (sẽ họp vào tháng 2)", 1, None, None, "LC", None),
    # [Phase-2] Úc ← Úc (S054): mắt xích chuỗi 'Úc' bị sót — EN
    # 'Australia' (S049 ST) đối xứng 1-1.
    ("S055", "Úc", "L", "repetition",
     "S054: Mục tiêu lạm phát chính thức của Úc", "high", None,
     "lặp Úc (mà Úc có thể thấy)", 1, None, None, "LC", None),
    # [Phase-2] giảm ← giảm lạm phát (S054): mắt xích chuỗi 'giảm' bị sót
    # (TNT §26) — "mục tiêu lãi suất tiền mặt giảm" = đợt cắt giảm; EN 'a
    # reduction' (S049 ST) lặp chuỗi reduction — VI gom nghĩa 'cắt giảm'
    # vào hình vị 'giảm', ghi §7.
    ("S055", "giảm", "L", "repetition",
     "S054: nỗ lực giảm lạm phát", "med", None,
     "lặp chuỗi 'giảm' (mục tiêu lãi suất tiền mặt giảm)", 1, None,
     None, "LC", None),
    # S056 (= EN S050)
    ("S056", "RBA", "L", "repetition", "S055: RBA", "high", None,
     "Thống đốc RBA", 1, None, None, "LC", None),
    ("S056", "lạm phát", "L", "repetition",
     "S054: giảm lạm phát", "high", None, "kiềm chế lạm phát", 1,
     None, None, "LC", None),
    # S057 (= EN S051)
    ("S057", "lạm phát", "L", "repetition",
     "S056: kiềm chế lạm phát", "high", None,
     "Với lạm phát đang giảm", 1, None, None, "LC", None),
    ("S057", "chúng tôi", "R", "personal",
     "RBA/Bullock (ngoại văn bản — quote)", "med", None,
     "VI tách 'we' thành 'chúng tôi' (RBA) + 'chúng ta' (hư chỉ "
     "chung, không đánh)", 1, None, None, "LC", "E"),
    ("S057", "bà", "R", "personal",
     "S056: Thống đốc RBA Michele Bullock", "high", None, None, 1,
     None, None, "LC", "A"),
    ("S057", "cuộc họp", "L", "repetition",
     "S035: cuộc họp thứ ba", "high", None,
     "cuộc họp tháng 12 của RBA; EN gộp trong hàng 'RBA meeting'", 1,
     None, None, "LC", None),
    ("S057", "RBA", "L", "repetition", "S056: RBA", "high", None,
     None, 1, None, None, "LC", None),
    ("S057", "đang giảm", "L", "repetition",
     "S045: đang giảm", "high", None,
     "chuỗi 'giảm'; EN 'coming down' có hàng riêng Phase-2", 1,
     None, None, "LC", None),
    # [Phase-2] tăng ← tăng lãi suất (S055): mắt xích chuỗi 'tăng' bị sót
    # (TNT §26) — "việc làm tăng" mở rộng chuỗi sang tham số mới (việc
    # làm); EN 'growing' là lần đầu nên không có hàng.
    ("S057", "tăng", "L", "repetition",
     "S055: tăng lãi suất lên 4,35 phần trăm", "med", None,
     "lặp chuỗi 'tăng' (việc làm tăng) — tham số mới, cùng hình vị", 1,
     None, None, "LC", None),
]
