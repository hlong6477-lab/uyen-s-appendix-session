# P28 tie table — WRITTEN BY HAND FROM work/analysis/P28_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# KHỐI CẮT VI: EN S012, S039 (tie chỉ EN). Subhead không gán nhãn.
# Quy ước ngôi: you/bạn, we-us/chúng ta — 1 dấu/câu (lần đầu), các lần
# khác trong câu ghi note. VI S029 "chúng ta" ↔ EN S030; bản đồ dịch −1/−2.
# [Phase-2] Bổ sung theo PHASE2_PROTOCOL.md: 19 hàng mới EN / 17 hàng mới
# VI; 2 reclassify L→R comparative (H&H §2.5); sub→demonstrative (H&H
# §2.4) + additive→continuative (H&H §5.8); rút span VI S038 (precedent
# chồng marker); +alt EN S012/S024 (mapping §3.6).

ST = [
    # S001
    ("S001", "of us", "R", "personal",
     "cộng đồng (ngoại văn bản — feature khuyến nghị)", "med", None,
     "chuỗi ngôi 1 số nhiều xuyên bài, 1 dấu/câu", 1, None, None, "LC",
     "E"),
    # S002
    ("S002", "But", "C", "adversative",
     "S001: Around 74 per cent are making a resolution", "high", None,
     None, 1, None, None, "LC", None),
    ("S002", "we strive", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None,
     "'our pledges', 'for us', 'many of us' trong câu không đánh "
     "(quy ước 1 dấu/câu)", 1, None, None, "LC", "E"),
    # [Phase-2] pledges ← resolution (S001): chuỗi đồng nghĩa resolution↔
    # pledges (H&H §6.2 reiteration — synonym); VI "lời cam kết" (S002 TT).
    ("S002", "pledges", "L", "synonym",
     "S001: a New Year's resolution", "high", None,
     "pledges ≈ resolution (our pledges); 'them' cuối câu quy chiếu "
     "trong câu không đánh", 1, None, None, "LC", None),
    # S004
    ("S004", "we can improve", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    # S003
    ("S003", "new year", "L", "repetition",
     "S001: a New Year's resolution", "high", None,
     "lặp 'new year' trong tục ngữ 'new year, new me'", 1, None, None,
     "LC", None),
    # S005
    ("S005", "It", "R", "personal",
     "S004: how we can improve our lives", "high", None,
     "It = cách cải thiện cuộc sống; VI rơi chủ ngữ → E phía VI", 1,
     None, None, "LC", "A"),
    # S006
    ("S006", "It", "R", "personal",
     "S004: how we can improve our lives", "high", None, None, 1, None,
     None, "LC", "A"),
    # S007
    ("S007", "It", "R", "personal",
     "S004: how we can improve our lives", "high", None, None, 1, None,
     None, "LC", "A"),
    ("S007", "you've", "R", "personal",
     "độc giả (ngoại văn bản — feature khuyến nghị)", "med", None,
     "chuỗi ngôi 2 xuyên bài, 1 dấu/câu", 1, None, None, "LC", "E"),
    # S008
    ("S008", "it", "R", "personal",
     "S004: how we can improve our lives", "med", None,
     "Whatever it is; VI hấp thụ bằng 'Dù là gì đi nữa' → không có hàng",
     1, None, None, "LC", "A"),
    ("S008", "a New Year's resolution", "L", "repetition",
     "S001: a New Year's resolution", "high", None, None, 1, None,
     None, "LC", None),
    # S009
    ("S009", "a New Year's resolution", "L", "repetition",
     "S008: making a New Year's resolution", "high", None, None, 1,
     None, None, "LC", None),
    # S010
    ("S010", "New Year's resolutions", "L", "repetition",
     "S009: a New Year's resolution", "high", None, None, 1, None,
     None, "LC", None),
    ("S010", "improve", "L", "repetition",
     "S004: improve our lives", "high", None,
     "occ 1: lần 2 ('improve their fitness levels') trong câu cùng "
     "chuỗi, không đánh", 1, None, None, "LC", None),
    ("S010", "healthier", "L", "repetition",
     "S006: eating healthier", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] Australians ← Australians (S009): chuỗi người Úc lặp liên
    # câu (H&H §6.2 reiteration); VI "người Úc" (S010 TT).
    ("S010", "Australians", "L", "repetition",
     "S009: 74 per cent of Australians", "high", None,
     "lặp Australians (39 per cent of Australians)", 1, None, None,
     "LC", None),
    # S011
    ("S011", "travel overseas", "L", "repetition",
     "S007: finally travelling to that country", "high", None,
     "travel ≈ travelling", 1, None, None, "LC", None),
    # S012 — KHỐI CẮT (VI none)
    # [Phase-2] +alt "R: the" (mapping §3.6): the + tổng quát hóa tham chiếu
    # đã nêu (resolutions → resolution hype).
    ("S012", "the resolution hype", "L", "repetition",
     "S010: New Year's resolutions", "high", "R: the",
     "khối cắt, VI none; the định danh cuộc hype quanh quyết tâm", 1,
     None, None, "LC", None),
    # S013
    ("S013", "But", "C", "adversative",
     "S011: 20 per cent hope to travel overseas", "high", None, None,
     1, None, None, "LC", None),
    ("S013", "the New Year", "L", "repetition",
     "S009: a New Year's resolution", "high", None,
     "occ 1: lần 2 ('your New Year's resolution') trong câu cùng chuỗi, "
     "không đánh", 1, None, None, "LC", None),
    ("S013", "your", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('your New Year's resolution') trong câu không đánh",
     1, None, None, "LC", "E"),
    # [Phase-2] New Year's resolution ← the resolution hype (S012): chuỗi
    # quyết tâm bị sót ở S013 (H&H §6.2 reiteration; tiền trạm = nhắc
    # gần nhất — S012 nằm trong khối cắt).
    ("S013", "New Year's resolution", "L", "repetition",
     "S012: the resolution hype", "high", None,
     "lặp chuỗi resolution (your New Year's resolution); 'the New Year' "
     "đầu câu là chuỗi năm mới, đã có hàng riêng", 1, None, None, "LC",
     None),
    # [Phase-2] transform ← improve (S010): mắt xích sót của chuỗi đổi mới
    # improve→transform→change (H&H §6.2 — synonym); VI "thay đổi"
    # (S012 TT).
    ("S013", "transform", "L", "synonym",
     "S010: aiming to improve their diet", "med", None,
     "transform ≈ improve (transform your life)", 1, None, None, "LC",
     None),
    # S014 — [Phase-2] "Here" = chỉ từ trỏ toàn bộ phần giải thích theo
    # sau: quy chiếu mở rộng CATAPHORIC (H&H §2.4 demonstrative adverb +
    # §2.4.1.4 extended reference); VI "Đây" (S013 TT) giữ 1–1.
    ("S014", "Here", "R", "demonstrative",
     "S015–S072: bốn khối subhead giải thích lý do", "med", None,
     "tiền chỉ hiếm: Here's why = phần giải thích nằm sau; 'why' là "
     "pro-form tóm lý do", 1, None, None, "LC", "C"),
    # S016
    ("S016", "health", "L", "repetition",
     "S010: health-based", "high", None,
     "trong 'health behavioural change'", 1, None, None, "LC", None),
    # [Phase-2] change ← transform (S013): mắt xích sót chuỗi đổi mới
    # (H&H §6.2 — transform ≈ change); S031 self-change quy về đây.
    ("S016", "change", "L", "synonym",
     "S013: transform your life", "med", None,
     "health behavioural change; 'behavioural' thuộc chuỗi hành vi "
     "(S033 that behaviour)", 1, None, None, "LC", None),
    # S017
    ("S017", "He", "R", "personal",
     "S016: Ron Borland", "high", None,
     "VI thêm danh xưng 'Ông'", 1, None, None, "LC", "A"),
    ("S017", "a New Year's resolution", "L", "repetition",
     "S013: your New Year's resolution", "high", None, None, 1, None,
     None, "LC", None),
    # S018
    ("S018", "They're", "R", "personal",
     "S017: a New Year's resolution", "high", None,
     "số nhiều về danh từ số ít — quy chiếu về loại", 1, None, None,
     "LC", "A"),
    ("S018", "you've", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "'you're prepared' lần 2 trong câu không đánh", 1, None, None,
     "LC", "E"),
    ("S018", "Borland", "L", "repetition",
     "S016: Ron Borland", "high", None, None, 1, None, None, "LC",
     None),
    # S019
    ("S019", "they", "R", "personal",
     "S018: They're bad", "high", None, None, 1, None, None, "LC",
     "A"),
    # S020
    ("S020", "New Year's resolutions", "L", "repetition",
     "S017: a New Year's resolution", "high", None, None, 1, None,
     None, "LC", None),
    ("S020", "fail", "L", "repetition",
     "S002: will fail to make good on them", "high", None, None, 1,
     None, None, "LC", None),
    # [Phase-2] Studies ← research (S009): đồng nghĩa (H&H §6.2
    # reiteration) — EN đổi từ nơi VI lặp nguyên văn "nghiên cứu"
    # (S019 TT; NTT 2020 §2.1).
    ("S020", "Studies", "L", "synonym",
     "S009: research from comparison site Finder", "high", None,
     "Studies ≈ research (Studies show 88 per cent)", 1, None, None,
     "LC", None),
    # S021
    ("S021", "Additionally", "C", "additive",
     "S020: Studies show 88 per cent fail", "high", None, None, 1,
     None, None, "LC", None),
    ("S021", "their resolutions", "L", "repetition",
     "S020: New Year's resolutions", "high", None, None, 1, None,
     None, "LC", None),
    # [Phase-2] achieve ↔ fail (S020): phép đối liên câu (TNT §30; H&H
    # §6.4 opposites) — 88% fail đối lập 8% achieve; VI "đạt được"
    # (S020 TT).
    ("S021", "achieve", "L", "antonym",
     "S020: fail them within the first two weeks", "high", None,
     "phép đối fail ↔ achieve (actually achieve); mở đầu chuỗi achieve → "
     "accomplish (S042) → achieve (S053)", 1, None, None, "LC", None),
    ("S021", "research", "L", "repetition",
     "S009: research from comparison site Finder", "high", None, None,
     1, None, None, "LC", None),
    # S022
    # [Phase-2] RECLASSIFY sub personal → demonstrative (H&H §2.4;
    # §2.4.1.4 extended reference): "That means" trỏ cả mệnh đề bằng chỉ
    # từ, không phải đại từ nhân xưng.
    ("S022", "That", "R", "demonstrative",
     "S020–S021: 88 per cent fail, only 8 per cent achieve", "high",
     None, "quy chiếu mệnh đề (extended reference)", 1, None, None, "LC",
     "A"),
    ("S022", "of us", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None,
     "'we may be setting' lần 2 trong câu không đánh", 1, None, None,
     "LC", "E"),
    ("S022", "the new year", "L", "repetition",
     "S013: the New Year", "high", None, "going into the new year", 1,
     None, None, "LC", None),
    # [Phase-2] failure ← fail (S020): danh hóa lặp chuỗi thất bại bị sót
    # (H&H §6.2 reiteration; TNT §26 phép lặp) — S024 "this failure" quy
    # về đây.
    ("S022", "failure", "L", "repetition",
     "S020: fail them within the first two weeks", "high", None,
     "danh hóa failure ← fail (setting ourselves up for failure)", 1,
     None, None, "LC", None),
    # [Phase-2] intentions ← resolutions (S021): danh từ tổng quát hóa
    # (H&H §6.1 general word) — good intentions = các quyết tâm đã nêu.
    ("S022", "intentions", "L", "general word",
     "S021: achieve their resolutions", "med", None,
     "tổng quát hóa resolution → intention (good intentions); S060 "
     "intentions lặp tiếp chuỗi; VI 'ý định' (S021 TT)", 1, None, None,
     "LC", None),
    # S023
    ("S023", "failing", "L", "repetition",
     "S020: fail them within the first two weeks", "high", None,
     "occ 1: 'failing quite miserably' lần 2 trong quote không đánh",
     1, None, None, "LC", None),
    ("S023", "Borland", "L", "repetition",
     "S018: Borland told SBS News", "high", None, None, 1, None, None,
     "LC", None),
    # S024
    ("S024", "But", "C", "adversative",
     "S023: the most negative impact is failing", "high", None, None,
     1, None, None, "LC", None),
    ("S024", "this failure", "R", "demonstrative",
     "S022–S023: setting ourselves up for failure", "high", None,
     "demonstrative; VI dùng hậu chỉ từ 'này'", 1, None, None, "LC",
     "A"),
    # [Phase-2] the journey ← S001–S002 (toàn mạch quyết tâm/tự hoàn
    # thiện): "the + danh từ tổng quát ẩn dụ" đổi tên tham chiếu đã nêu
    # (H&H §6.1 general noun; mapping §3.6 → alt "R: the"); neo chuỗi
    # journey → process (S072); VI "hành trình" (S023 TT) vô định —
    # dịch chuyển the ↔ zero (NTT 2020 §2.2).
    ("S024", "the journey", "L", "general word",
     "S001–S002: a New Year's resolution / self-improvement (toàn mạch)",
     "med", "R: the",
     "accept it as part of the journey — tổng quát hóa toàn mạch cải "
     "thiện bản thân; VI 'một phần của hành trình' vô định", 1, None,
     None, "LC", None),
    # S025
    ("S025", "you're", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None, None, 1, None,
     None, "LC", "E"),
    ("S025", "fail", "L", "repetition",
     "S023: failing quite miserably", "high", None,
     "you're going to fail", 1, None, None, "LC", None),
    # S026 — [Phase-2] success ↔ fail (S025): phép đối liên câu (TNT §30;
    # H&H §6.4 opposites) trong quote; VI "thành công" (S025 TT).
    ("S026", "success", "L", "antonym",
     "S025: sometimes you're going to fail", "high", None,
     "phép đối fail ↔ success (100 per cent success rate); mở đầu chuỗi "
     "success (S040 quy về đây)", 1, None, None, "LC", None),
    # S028
    ("S028", "New Year's resolutions", "L", "repetition",
     "S021: their resolutions", "high", None, None, 1, None, None,
     "LC", None),
    ("S028", "fail", "L", "repetition",
     "S025: you're going to fail", "high", None, None, 1, None, None,
     "LC", None),
    ("S028", "planned", "L", "repetition",
     "S018: a very clear plan", "high", None,
     "poorly planned — đối lập nghĩa trong cùng chuỗi", 1, None, None,
     "LC", None),
    ("S028", "Borland", "L", "repetition",
     "S023: Borland said", "high", None, None, 1, None, None, "LC",
     None),
    # S029
    ("S029", "New Year's resolutions", "L", "repetition",
     "S028: Most New Year's resolutions", "high", None, None, 1, None,
     None, "LC", None),
    ("S029", "a good plan", "L", "repetition",
     "S028: poorly planned", "high", None,
     "đối poor ↔ good; 'they/them' trong câu không đánh", 1, None,
     None, "LC", None),
    # [Phase-2] implementing ← follow through (S018): mắt xích sót của
    # chuỗi thực hiện (H&H §6.2 — synonym); S034 implementing quy về đây;
    # VI lặp nguyên văn "thực hiện" (S028 TT).
    ("S029", "implementing", "L", "synonym",
     "S018: prepared to follow through", "high", None,
     "implementing ≈ follow through (for implementing them)", 1, None,
     None, "LC", None),
    # S030
    ("S030", "we're", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    # S031
    ("S031", "This", "R", "demonstrative",
     "S030: we're still deep in holiday mode", "high", None,
     "quy chiếu mệnh đề", 1, None, None, "LC", "A"),
    ("S031", "self-change", "L", "repetition",
     "S016: health behavioural change", "high", None,
     "radical self-change; EN time-it 'it can be' không đánh (VI có "
     "'đây' — bất đối xứng có chủ đích)", 1, None, None, "LC", None),
    # S032
    ("S032", "holiday season", "L", "repetition",
     "S030: holiday mode", "high", None,
     "It's = time-it, không đánh", 1, None, None, "LC", None),
    # S033
    ("S033", "You", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "'you go back…your normal lifestyle' lần 2, 3 trong câu không đánh",
     1, None, None, "LC", "E"),
    ("S033", "no plan", "L", "repetition",
     "S029: a good plan", "high", None, None, 1, None, None, "LC",
     None),
    ("S033", "that behaviour", "L", "repetition",
     "S016: health behavioural change", "high", None, None, 1, None,
     None, "LC", None),
    ("S033", "Borland", "L", "repetition",
     "S028: Borland said", "high", None, None, 1, None, None, "LC",
     None),
    # S034
    ("S034", "those strategies", "R", "demonstrative",
     "S033: something that works for two weeks", "high", None,
     "VI hậu chỉ từ 'đó'", 1, None, None, "LC", "A"),
    ("S034", "You", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None, None, 1, None,
     None, "LC", "E"),
    ("S034", "a plan", "L", "repetition",
     "S033: no plan", "high", None, None, 1, None, None, "LC", None),
    ("S034", "implementing", "L", "repetition",
     "S029: implementing them", "high", None, None, 1, None, None,
     "LC", None),
    ("S034", "day-to-day lifestyle", "L", "repetition",
     "S033: your normal lifestyle", "high", None,
     "'lifestyle' lần 2 trong câu, cùng chuỗi, ghi note", 1, None,
     None, "LC", None),
    # S035
    ("S035", "And", "C", "additive",
     "S034: You need a plan for implementing those strategies",
     "high", None, "câu 2 của quote", 1, None, None, "LC", None),
    # S037
    ("S037", "you stick", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "stick — khởi tạo chuỗi; VI đổi 'kiên trì'", 1, None, None,
     "LC", "E"),
    ("S037", "your resolution", "L", "repetition",
     "S028: Most New Year's resolutions", "high", None,
     "'keep it going' — it trong câu không đánh", 1, None, None, "LC",
     None),
    # S038
    ("S038", "following through", "L", "repetition",
     "S018: follow through", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] achievable ← achieve (S021): biến hình thức của chuỗi
    # achieve (H&H §6.2 reiteration; analysis §6 đã ghi "thêm achievable
    # ← achieve (S021)"); nhãn Achievable (S047) quy về đây.
    ("S038", "achievable", "L", "repetition",
     "S021: actually achieve", "high", None,
     "lặp hình vị achieve trong định nghĩa SMART", 1, None, None, "LC",
     None),
    # S039 — KHỐI CẮT (VI none)
    ("S039", "this approach", "R", "demonstrative",
     "S038: set a 'SMART' goal", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", "A"),
    ("S039", "Borland", "L", "repetition",
     "S034: Borland said — S028", "high", None, "khối cắt", 1, None,
     None, "LC", None),
    ("S039", "goal-setting", "L", "repetition",
     "S038: a 'SMART' goal", "high", None, "khối cắt", 1, None, None,
     "LC", None),
    ("S039", "smart", "L", "repetition",
     "S038: 'SMART'", "high", None,
     "chơi chữ SMART↔smart của nguồn; khối cắt, VI none", 1, None,
     None, "LC", None),
    # S040
    ("S040", "you don't", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "'you can increase' lần 2 trong câu không đánh", 1, None, None,
     "LC", "E"),
    # [Phase-2] give up ↔ stick (S037): phép đối liên câu có phủ định
    # (TNT §30; H&H §6.4 opposites) — "don't give up" = "stick"; VI
    # "bỏ cuộc" (S038 TT).
    ("S040", "give up", "L", "antonym",
     "S037: ensure you stick to your resolution", "med", None,
     "phép đối stick ↔ give up (make sure you don't give up)", 1, None,
     None, "LC", None),
    ("S040", "planning", "L", "repetition",
     "S028: poorly planned", "high", None,
     "a little bit of planning beforehand", 1, None, None, "LC",
     None),
    ("S040", "a clear plan", "L", "repetition",
     "S034: a plan", "high", None, "lặp 'clear' (S018) trong cụm", 1,
     None, None, "LC", None),
    ("S040", "success", "L", "repetition",
     "S026: a 100 per cent success rate", "high", None,
     "chance of success", 1, None, None, "LC", None),
    # S042
    ("S042", "Specific:", "L", "repetition",
     "S038: specific, measurable, achievable", "high", None,
     "nhãn liệt kê giữ nguyên văn; 'really specific' lần 2 trong câu "
     "không đánh", 1, None, None, "LC", None),
    ("S042", "you want", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    ("S042", "accomplish", "L", "synonym",
     "S021: actually achieve", "high", None, "accomplish ≈ achieve", 1,
     None, None, "LC", None),
    # S043
    ("S043", "you want", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2, 3 ('you might instead say you want') trong câu "
     "không đánh", 1, None, None, "LC", "E"),
    ("S043", "eat healthier", "L", "repetition",
     "S006: eating healthier", "high", None,
     "trích lại nguyên văn trong ngoặc đơn", 1, None, None, "LC",
     None),
    # S044
    ("S044", "Measurable:", "L", "repetition",
     "S038: specific, measurable, achievable", "high", None,
     "nhãn liệt kê", 1, None, None, "LC", None),
    ("S044", "you'll", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    # S045
    ("S045", "For example", "C", "additive",
     "S044: Decide how you'll track your progress", "high", None,
     "kiểu ví dụ", 1, None, None, "LC", None),
    ("S045", "you commit", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "'you'll know…you're slightly off track' trong câu không đánh", 1,
     None, None, "LC", "E"),
    ("S045", None, "E", "nominal",
     "S045: running four times a week (trong câu)", "high", None,
     "[TC] lược {times a week} sau 'three'; VI lấp đầy 'chỉ chạy ba "
     "lần' nên không có E phía VI", 1, "three", "{times a week}",
     "TC", None),
    ("S045", "off track", "L", "repetition",
     "S044: track your progress", "high", None,
     "idiom vang nhau 'track'", 1, None, None, "LC", None),
    # S046
    # [Phase-2] RECLASSIFY sub nominal → demonstrative (H&H §2.4): "this +
    # danh từ" — khớp quy ước "this failure/these moments".
    ("S046", "this clarity", "R", "demonstrative",
     "S042–S043: Specific — make it really specific", "high", None,
     "bridging bằng danh từ tổng quát; VI 'sự rõ ràng này'", 1, None,
     None, "LC", "A"),
    ("S046", "you're", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "'when you need to recalibrate' lần 2 trong câu không đánh", 1,
     None, None, "LC", "E"),
    ("S046", "Borland", "L", "repetition",
     "S039: Borland said", "high", None, None, 1, None, None, "LC",
     None),
    ("S046", "succeeding", "L", "repetition",
     "S040: chance of success", "high", None, None, 1, None, None,
     "LC", None),
    ("S046", "recalibrate", "L", "synonym",
     "S045: a small adjustment", "med", None,
     "recalibrate ≈ adjustment — EN đổi từ", 1, None, None, "LC",
     None),
    # S047
    ("S047", "Achievable:", "L", "repetition",
     "S038: specific, measurable, achievable", "high", None,
     "nhãn liệt kê; 'It's great' expletive không đánh", 1, None, None,
     "LC", None),
    ("S047", "your goal", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "'your circumstances' lần 2 trong câu không đánh", 1, None, None,
     "LC", "E"),
    ("S047", "realistic", "L", "repetition",
     "S038: realistic", "high", None,
     "make sure your goal is realistic — lặp cả nhãn", 1, None, None,
     "LC", None),
    # S048
    ("S048", "you've", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    ("S048", "aiming", "L", "repetition",
     "S047: aim high", "high", None, None, 1, None, None, "LC", None),
    ("S048", "gourmet meals", "L", "repetition",
     "S043: each meal", "high", None,
     "meal → meals; 'cook' khởi tạo chuỗi", 1, None, None, "LC",
     None),
    # S049
    ("S049", "Instead", "C", "adversative",
     "S048: aiming to cook gourmet meals might be a stretch", "high",
     None, "thay thế đề xuất", 1, None, None, "LC", None),
    # [Phase-2] more manageable ← S048 "might be a stretch": quy chiếu so
    # sánh (H&H §2.5 "more") — chuẩn so sánh nằm ở CÂU TRƯỚC; VI giữ cấu
    # trúc so sánh "dễ quản lý hơn" (S047 TT).
    ("S049", "more manageable", "R", "comparative",
     "S048: aiming to cook gourmet meals every night might be a stretch",
     "high", None,
     "[LC] quy chiếu so sánh: more manageable = dễ quản lý HƠN so với "
     "mục tiêu nấu bữa ngon mỗi tối (S048); H&H §2.5", 1, None, None,
     "LC", "A"),
    ("S049", "a goal", "L", "repetition",
     "S047: your goal", "high", None, None, 1, None, None, "LC",
     None),
    ("S049", "cooking", "L", "repetition",
     "S048: cook gourmet meals", "high", None, None, 1, None, None,
     "LC", None),
    ("S049", "dinners", "L", "repetition",
     "S048: gourmet meals", "high", None, None, 1, None, None, "LC",
     None),
    ("S049", "you", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "sets you up for success", 1, None, None, "LC", "E"),
    ("S049", "success", "L", "repetition",
     "S046: when you're succeeding", "high", None, None, 1, None,
     None, "LC", None),
    # S050
    ("S050", "Realistic:", "L", "repetition",
     "S038: realistic — S047", "high", None, "nhãn liệt kê", 1, None,
     None, "LC", None),
    ("S050", "your", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('your lifestyle') trong câu không đánh", 1, None,
     None, "LC", "E"),
    ("S050", "goal fits", "L", "repetition",
     "S049: a goal like cooking", "high", None, None, 1, None, None,
     "LC", None),
    ("S050", "your lifestyle", "L", "repetition",
     "S034: day-to-day lifestyle", "high", None, None, 1, None, None,
     "LC", None),
    # S051
    ("S051", "For instance", "C", "additive",
     "S050: Consider whether your goal fits", "high", None,
     "kiểu ví dụ", 1, None, None, "LC", None),
    ("S051", "you've", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    # S052
    ("S052", "You", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "'you need' lần 2, 3 trong câu không đánh; 'that' trong câu "
     "không đánh", 1, None, None, "LC", "E"),
    ("S052", "a realistic goal", "L", "repetition",
     "S050: Realistic", "high", None, None, 1, None, None, "LC",
     None),
    # S053
    ("S053", "you can", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None, None, 1, None,
     None, "LC", "E"),
    # [Phase-2] RECLASSIFY L repetition → R comparative (H&H §2.5 "more"):
    # "more realistic" so sánh với "not quite a realistic goal" (S052) ở
    # câu trước — quan hệ so sánh trội hơn phép lặp (mapping §3.13 một
    # hình thức một hàng); VI "thực tế hơn" (S051 TT) đồng bộ reclassify.
    ("S053", "more realistic", "R", "comparative",
     "S052: that's not quite a realistic goal", "high", None,
     "[LC] quy chiếu so sánh: more realistic = thực tế HƠN so với mục "
     "tiêu vừa bị bác (S052); mặt lặp realistic ghi ở analysis §6", 1,
     None, None, "LC", "A"),
    ("S053", "achieve", "L", "repetition",
     "S021: actually achieve", "high", None, None, 1, None, None,
     "LC", None),
    ("S053", "Borland", "L", "repetition",
     "S046: Borland suggests", "high", None, None, 1, None, None,
     "LC", None),
    # S054
    ("S054", "Time-bound:", "L", "repetition",
     "S038: time-bound", "high", None,
     "nhãn liệt kê; 'time frame' trong câu ghi note", 1, None, None,
     "LC", None),
    # [Phase-2] a clear deadline ← a clear plan (S040): mắt xích sót của
    # chuỗi "clear" (S018→S040→S054→S057; H&H §6.2 reiteration; TNT §26
    # phép lặp); "deadline/time frame" trong câu là apposition; VI
    # "rõ ràng" (S052 TT) đã có hàng riêng.
    ("S054", "a clear deadline", "L", "repetition",
     "S040: a clear plan", "high", None,
     "lặp 'clear' trong cụm 'a clear deadline'; VI đánh 'rõ ràng' "
     "(S052)", 1, None, None, "LC", None),
    ("S054", "your goal", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, "achieving your goal", 1,
     None, None, "LC", "E"),
    ("S054", "achieving", "L", "repetition",
     "S053: actually achieve", "high", None, None, 1, None, None,
     "LC", None),
    # S055
    ("S055", "you'll", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('you'll run 5K') trong câu không đánh", 1, None,
     None, "LC", "E"),
    ("S055", "get fit", "L", "repetition",
     "S010: improve their fitness levels", "high", None, None, 1,
     None, None, "LC", None),
    # [Phase-2] run ← running (S045): chuỗi chạy (H&H §6.2 reiteration) —
    # ví dụ chạy bộ lặp qua khối SMART; VI "chạy" (S053 TT).
    ("S055", "run", "L", "repetition",
     "S045: commit to running four times a week", "high", None,
     "lặp run/running (you'll run 5K)", 1, None, None, "LC", None),
    ("S055", "specify", "L", "repetition",
     "S042: Specific — make it really specific", "high", None,
     "hình vị speci-", 1, None, None, "LC", None),
    # S056
    ("S056", "your", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "your resolution; 'you track progress' lần 2 trong câu không "
     "đánh", 1, None, None, "LC", "E"),
    ("S056", "a timeline", "L", "repetition",
     "S054: Time-bound — time frame", "high", None, None, 1, None,
     None, "LC", None),
    ("S056", "resolution", "L", "repetition",
     "S037: your resolution", "high", None, None, 1, None, None,
     "LC", None),
    ("S056", "track progress", "L", "repetition",
     "S044: track your progress", "high", None, None, 1, None, None,
     "LC", None),
    # S057
    ("S057", "you'll turn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "'yourself' phản thân không đánh", 1, None, None, "LC", "E"),
    ("S057", "your resolution this way", "L", "repetition",
     "S056: Giving your resolution a timeline", "high", None, None, 1,
     None, None, "LC", None),
    ("S057", "a vague idea", "L", "repetition",
     "S055: vaguely saying", "high", None, None, 1, None, None, "LC",
     None),
    ("S057", "a clear, actionable plan", "L", "repetition",
     "S040: a clear plan", "high", None, None, 1, None, None, "LC",
     None),
    ("S057", "sticking", "L", "repetition",
     "S037: you stick to your resolution", "high", None,
     "sticking with it — VI đổi từ 'gắn bó'", 1, None, None, "LC",
     None),
    # S059
    ("S059", "you fail", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "'you're not alone' lần 2 trong câu không đánh", 1, None, None,
     "LC", "E"),
    ("S059", "your New Year's resolution", "L", "repetition",
     "S056: Giving your resolution a timeline", "high", None, None, 1,
     None, None, "LC", None),
    # S060
    ("S060", "goals", "L", "repetition",
     "S057: a vague idea into a clear plan — goal (S049)", "high",
     None, None, 1, None, None, "LC", None),
    ("S060", "intentions", "L", "repetition",
     "S022: good intentions", "high", None, None, 1, None, None,
     "LC", None),
    ("S060", "fall short", "L", "synonym",
     "S002: will fail to make good on them", "high", None,
     "fall short ≈ fail", 1, None, None, "LC", None),
    # S061
    ("S061", "these moments", "R", "demonstrative",
     "S060: fall short when faced with the realities", "high", None,
     "bridging", 1, None, None, "LC", "A"),
    ("S061", "Borland", "L", "repetition",
     "S053: Borland said", "high", None,
     "'it's important' expletive không đánh", 1, None, None, "LC",
     None),
    # S062
    ("S062", "completely change", "L", "repetition",
     "S031: radical self-change", "high", None,
     "'Realistically,' là trạng từ câu, không thuộc chuỗi realistic "
     "(ghi §8)", 1, None, None, "LC", None),
    ("S062", "Borland", "L", "repetition",
     "S061: Borland emphasises", "high", None, None, 1, None, None,
     "LC", None),
    # S063
    ("S063", "it happens", "R", "personal",
     "S062: to completely change and become a different person",
     "high", None, "quy chiếu mệnh đề", 1, None, None, "LC", "A"),
    ("S063", "do it and do it", "S", "verbal",
     "S062: to completely change", "high", None,
     "[LC] 'do' thế động từ cho 'change'; lần 2 cùng cụm thế không "
     "đánh thêm", 1, None, None, "LC", None),
    ("S063", "succeed", "L", "repetition",
     "S049: sets you up for success", "high", None, None, 1, None,
     None, "LC", None),
    # S064
    ("S064", "He", "R", "personal",
     "S062: Borland explains", "high", None, None, 1, None, None,
     "LC", "A"),
    ("S064", "personal change", "L", "repetition",
     "S062: completely change", "high", None, None, 1, None, None,
     "LC", None),
    ("S064", "transform oneself", "L", "repetition",
     "S013: transform your life", "high", None, None, 1, None, None,
     "LC", None),
    # S065
    ("S065", "however", "C", "adversative",
     "S064: change driven by adversity", "high", None,
     "EN để giữa câu, VI đảo lên đầu", 1, None, None, "LC", None),
    ("S065", "of us", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None, "For most of us", 1,
     None, None, "LC", "E"),
    ("S065", "resolutions", "L", "repetition",
     "S059: your New Year's resolution", "high", None, None, 1, None,
     None, "LC", None),
    ("S065", "adversity", "L", "repetition",
     "S064: significant adversity", "high", None, None, 1, None,
     None, "LC", None),
    ("S065", "striving", "L", "repetition",
     "S002: we strive for self-improvement", "high", None,
     "hồi quy xa 63 câu", 1, None, None, "LC", None),
    # S066
    ("S066", "But", "C", "adversative",
     "S065: resolutions about striving towards an idealised version",
     "high", None, None, 1, None, None, "LC", None),
    ("S066", "Borland", "L", "repetition",
     "S064: He points out — Borland (S062)", "high", None, None, 1,
     None, None, "LC", None),
    ("S066", "cautions against", "L", "repetition",
     "S017: He cautions against", "high", None,
     "lặp nguyên cụm", 1, None, None, "LC", None),
    ("S066", "aiming", "L", "repetition",
     "S048: aiming to cook", "high", None, "aiming for perfection", 1,
     None, None, "LC", None),
    ("S066", "perfection", "L", "synonym",
     "S065: an idealised version", "med", None,
     "perfection ≈ idealised — chuỗi lý tưởng", 1, None, None, "LC",
     None),
    # S067
    ("S067", "current you", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "'you' danh hóa; 'fantasised you', 'you'll' lần 2, 3 trong câu "
     "không đánh", 1, None, None, "LC", "E"),
    ("S067", "change", "L", "repetition",
     "S064: profound personal change", "high", None, None, 1, None,
     None, "LC", None),
    ("S067", "fantasised", "L", "synonym",
     "S065: an idealised version of ourselves", "med", None,
     "fantasised ≈ idealised", 1, None, None, "LC", None),
    # S068
    # [Phase-2] RECLASSIFY sub nominal → demonstrative (H&H §2.4) — đồng bộ
    # với "these lofty goals" cùng câu.
    ("S068", "This disconnect", "R", "demonstrative",
     "S067: current you vs fantasised you", "high", None,
     "danh từ tổng quát tóm chỉ", 1, None, None, "LC", "A"),
    ("S068", "these lofty goals", "R", "demonstrative",
     "S060: Many people set goals", "high", None,
     "hai hậu chỉ từ trong một câu VI (occ 1–2)", 1, None, None, "LC",
     "A"),
    ("S068", "we", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None,
     "when we realise; VI 'chúng ta' gánh", 1, None, None, "LC", "E"),
    ("S068", "failure", "L", "repetition",
     "S024: this failure", "high", None,
     "frustration and failure", 1, None, None, "LC", None),
    # [Phase-2] the sacrifices ← S067 "things you really don't want to
    # do": danh từ tổng quát bridging (H&H §6.1 general word); the định
    # danh → alt (mapping §3.6); VI "hy sinh" (S066 TT) — dịch chuyển
    # the ↔ zero (NTT 2020 §2.2).
    ("S068", "sacrifices", "L", "general word",
     "S067: a whole lot of things you really don't want to do", "med",
     "R: the",
     "danh từ tổng quát chỉ các thứ phải đánh đổi của 'fantasised you'", 1,
     None, None, "LC", None),
    # S069
    ("S069", "of us", "R", "personal",
     "cộng đồng (ngoại văn bản — quote)", "med", None, None, 1, None,
     None, "LC", "E"),
    ("S069", "ideal", "L", "repetition",
     "S065: an idealised version", "high", None, None, 1, None, None,
     "LC", None),
    # S070
    # [Phase-2] RECLASSIFY sub additive → continuative (H&H §5.8; protocol
    # nhóm 5): "In fact," đầu câu mở lượt nhấn mạnh discours (tăng tiến
    # 'rất ít' → 'không ai'), không thêm nội dung mệnh đề — trước đây ghi
    # additive (nhấn mạnh); VI "Trên thực tế" (S068 TT) đồng bộ.
    ("S070", "In fact", "C", "continuative",
     "S069: Very few of us are ideal", "high", None,
     "continuative tăng tiến: chỉnh sub từ 'additive' theo H&H §5.8", 1,
     None, None, "LC", None),
    ("S070", "of us", "R", "personal",
     "cộng đồng (ngoại văn bản — quote)", "med", None, "none of us", 1,
     None, None, "LC", "E"),
    ("S070", None, "E", "verbal",
     "S069: Very few of us are ideal", "high", None,
     "[LC] tỉnh lược vị ngữ ∅ {are ideal}; VI lấp đầy 'thực sự hoàn "
     "hảo' nên không có E phía VI", 1, "really", "{are ideal}", "LC",
     None),
    # S071
    ("S071", "your", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, "Look at your failure", 1,
     None, None, "LC", "E"),
    ("S071", "failure as a learning opportunity", "L", "repetition",
     "S068: frustration and failure", "high", None, None, 1, None,
     None, "LC", None),
    # S072
    ("S072", "failure", "L", "repetition",
     "S071: your failure as a learning opportunity", "high", None,
     None, 1, None, None, "LC", None),
    ("S072", "process", "L", "synonym",
     "S024: part of the journey", "med", None,
     "process ≈ journey", 1, None, None, "LC", None),
]

TT = [
    # S001
    ("S001", "chúng ta", "R", "personal",
     "cộng đồng (ngoại văn bản — feature khuyến nghị)", "med", None,
     "chuỗi ngôi 1 số nhiều xuyên bài, 1 dấu/câu", 1, None, None, "LC",
     "E"),
    # S002
    ("S002", "Nhưng", "C", "adversative",
     "S001: 74 phần trăm đang đưa ra quyết tâm", "high", None, None, 1,
     None, None, "LC", None),
    ("S002", "chúng ta", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None,
     "occ 1: lần 2, 3, 4 ('của chúng ta', 'cho chúng ta', 'trong chúng "
     "ta') trong câu không đánh", 1, None, None, "LC", "E"),
    # [Phase-2] lời cam kết ← quyết tâm (S001): chuỗi đồng nghĩa (H&H §6.2
    # reiteration — synonym) đối ứng EN pledges (S002 ST); occ 1 tường minh.
    ("S002", "lời cam kết", "L", "synonym",
     "S001: quyết tâm cho năm mới 2025", "high", None,
     "lời cam kết ≈ quyết tâm (những lời cam kết của chúng ta); occ 1 — "
     "lần 2 ('những lời cam kết đó') trong câu không đánh", 1, None, None,
     "LC", None),
    # S003
    ("S003", "năm mới", "L", "repetition",
     "S001: quyết tâm cho năm mới 2025", "high", None,
     "lặp 'năm mới' trong tục ngữ", 1, None, None, "LC", None),
    # S004
    ("S004", "chúng ta", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('cách chúng ta') trong câu không đánh", 1, None,
     None, "LC", "E"),
    # [Phase-2] cải thiện ← tự hoàn thiện (S002): lặp hình vị "thiện"
    # (TNT §26 phép lặp từ vựng); EN improve nằm trong span R "we can
    # improve" (S004 ST) nên không có hàng L riêng phía EN.
    ("S004", "cải thiện", "L", "repetition",
     "S002: chúng ta phấn đấu để tự hoàn thiện", "med", None,
     "lặp hình vị thiện (tự hoàn thiện → cải thiện); mở chuỗi cải thiện "
     "đến S010", 1, None, None, "LC", None),
    # S005
    ("S005", None, "E", "nominal",
     "S004: cách chúng ta có thể cải thiện cuộc sống của mình",
     "high", None,
     "[LC] rơi chủ ngữ ∅ ở đầu câu, hồi phục {cách cải thiện cuộc "
     "sống}; EN giữ 'It' (R-A)", 1, "", "{cách cải thiện cuộc sống}",
     "LC", None),
    # S006
    ("S006", None, "E", "nominal",
     "S004: cách chúng ta có thể cải thiện cuộc sống của mình",
     "high", None,
     "[LC] rơi chủ ngữ ∅ ở đầu câu; đối ứng EN 'It could be'", 1, "",
     "{cách cải thiện cuộc sống}", "LC", None),
    # S007
    ("S007", None, "E", "nominal",
     "S004: cách chúng ta có thể cải thiện cuộc sống của mình",
     "high", None,
     "[LC] rơi chủ ngữ ∅ ở đầu câu; đối ứng EN 'It might be'", 1, "",
     "{cách cải thiện cuộc sống}", "LC", None),
    ("S007", "bạn luôn muốn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    # S008
    ("S008", "năm mới", "L", "repetition",
     "S003: 'năm mới, tôi cũng mới'", "high", None,
     "lập mục tiêu cho năm mới; 'mục tiêu' khởi tạo chuỗi", 1, None,
     None, "LC", None),
    # S009
    ("S009", "mục tiêu", "L", "repetition",
     "S008: việc lập mục tiêu cho năm mới", "high", None, None, 1,
     None, None, "LC", None),
    ("S009", "năm mới", "L", "repetition",
     "S008: cho năm mới", "high", None, None, 1, None, None, "LC",
     None),
    # S010
    ("S010", "mục tiêu", "L", "repetition",
     "S009: lập mục tiêu cho năm mới", "high", None,
     "Các mục tiêu phổ biến nhất", 1, None, None, "LC", None),
    ("S010", "năm mới", "L", "repetition",
     "S009: cho năm mới", "high", None, None, 1, None, None, "LC",
     None),
    ("S010", "cải thiện", "L", "repetition",
     "S004: cải thiện cuộc sống của mình", "high", None,
     "occ 1: lần 2 ('cải thiện mức độ thể lực') trong câu không đánh",
     1, None, None, "LC", None),
    # [Phase-2] người Úc ← người Úc (S009): chuỗi người Úc (H&H §6.2
    # reiteration); EN "Australians" (S010 ST).
    ("S010", "người Úc", "L", "repetition",
     "S009: khoảng 74 phần trăm người Úc", "high", None,
     "lặp người Úc (39 phần trăm người Úc)", 1, None, None, "LC", None),
    ("S010", "lành mạnh hơn", "L", "repetition",
     "S006: ăn uống lành mạnh hơn", "high", None,
     "lựa chọn thực phẩm lành mạnh hơn", 1, None, None, "LC", None),
    # S011
    ("S011", "đi du lịch", "L", "repetition",
     "S007: cuối cùng là đi du lịch", "high", None, None, 1, None,
     None, "LC", None),
    # S012 (= EN S013)
    ("S012", "Nhưng", "C", "adversative",
     "S011: 20 phần trăm hy vọng đi du lịch nước ngoài", "high", None,
     None, 1, None, None, "LC", None),
    ("S012", "Năm mới", "L", "repetition",
     "S010: cho năm mới", "high", None,
     "occ 1: lần 2 ('năm mới của bạn') nằm trong hàng 'quyết tâm năm "
     "mới', ghi note", 1, None, None, "LC", None),
    ("S012", "quyết tâm năm mới", "L", "repetition",
     "S001: quyết tâm cho năm mới", "high", None, None, 1, None, None,
     "LC", None),
    ("S012", "của bạn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('quyết tâm năm mới của bạn') trong câu không đánh",
     1, None, None, "LC", "E"),
    # [Phase-2] thay đổi ← cải thiện (S010): mắt xích sót chuỗi đổi mới
    # (H&H §6.2 — synonym); S015 'thay đổi' quy về đây; EN "transform"
    # (S013 ST).
    ("S012", "thay đổi", "L", "synonym",
     "S010: muốn cải thiện chế độ ăn uống", "med", None,
     "thay đổi ≈ cải thiện (thay đổi cuộc sống của bạn)", 1, None, None,
     "LC", None),
    # S013 — [Phase-2] "Đây" = chỉ từ trỏ toàn bộ phần giải thích theo
    # sau: quy chiếu mở rộng CATAPHORIC (H&H §2.4 + §2.4.1.4 extended
    # reference); EN "Here" (S014 ST) giữ 1–1.
    ("S013", "Đây", "R", "demonstrative",
     "S014–S070: bốn khối subhead giải thích lý do", "med", None,
     "tiền chỉ hiếm: Đây là lý do tại sao = phần giải thích nằm sau", 1,
     None, None, "LC", "C"),
    # S015 (= EN S016)
    ("S015", "sức khỏe", "L", "repetition",
     "S010: các mục tiêu phổ biến nhất là về sức khỏe", "high", None,
     "thay đổi hành vi sức khỏe", 1, None, None, "LC", None),
    ("S015", "thay đổi", "L", "repetition",
     "S012: một thời điểm tuyệt vời để thay đổi cuộc sống", "high",
     None, None, 1, None, None, "LC", None),
    # S016 (= EN S017)
    ("S016", "Ông", "R", "personal",
     "S015: Ron Borland", "high", None,
     "VI thêm danh xưng lễ phép; EN chỉ 'He'", 1, None, None, "LC",
     "A"),
    ("S016", "quyết tâm năm mới", "L", "repetition",
     "S012: quyết tâm năm mới của bạn", "high", None, None, 1, None,
     None, "LC", None),
    # S017 (= EN S018)
    ("S017", "Chúng", "R", "personal",
     "S016: một quyết tâm năm mới", "high", None,
     "số nhiều về danh từ số ít", 1, None, None, "LC", "A"),
    ("S017", "bạn có", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "'bạn sẵn sàng' lần 2 trong câu không đánh", 1, None, None, "LC",
     "E"),
    ("S017", "Borland", "L", "repetition",
     "S015: Ron Borland", "high", None, None, 1, None, None, "LC",
     None),
    # S018 (= EN S019)
    ("S018", "chúng", "R", "personal",
     "S017: Chúng không tốt", "high", None, None, 1, None, None,
     "LC", "A"),
    # S019 (= EN S020)
    ("S019", "quyết tâm", "L", "repetition",
     "S016: một quyết tâm năm mới", "high", None,
     "'năm mới' lặp trong cụm 'quyết tâm cho năm mới', ghi note", 1,
     None, None, "LC", None),
    ("S019", "thất bại", "L", "synonym",
     "S002: không thực hiện được những lời cam kết", "high", None,
     "thất bại ≈ không thực hiện được — VI 2 chuỗi song song", 1,
     None, None, "LC", None),
    ("S019", "nghiên cứu", "L", "repetition",
     "S009: Theo nghiên cứu từ trang web so sánh Finder", "high",
     None, "Các nghiên cứu cho thấy", 1, None, None, "LC", None),
    # S020 (= EN S021)
    ("S020", "Ngoài ra", "C", "additive",
     "S019: 88 phần trăm thất bại trong hai tuần", "high", None,
     "VI đảo attribution lên đầu câu", 1, None, None, "LC", None),
    ("S020", "quyết tâm", "L", "repetition",
     "S019: quyết tâm cho năm mới", "high", None,
     "đạt được quyết tâm của mình", 1, None, None, "LC", None),
    # [Phase-2] đạt được ↔ thất bại (S019): phép đối liên câu (TNT §30;
    # H&H §6.4 opposites) — 88% thất bại đối lập 8% đạt được; EN
    # "achieve" (S021 ST).
    ("S020", "đạt được", "L", "antonym",
     "S019: đều thất bại trong vòng hai tuần đầu tiên", "high", None,
     "phép đối thất bại ↔ đạt được; mở đầu chuỗi đạt được của VI", 1,
     None, None, "LC", None),
    ("S020", "nghiên cứu", "L", "repetition",
     "S019: Các nghiên cứu cho thấy", "high", None, None, 1, None,
     None, "LC", None),
    # S021 (= EN S022)
    # [Phase-2] RECLASSIFY sub personal → demonstrative (H&H §2.4.1.4):
    # "Điều đó" = chỉ từ + danh từ tổng quát trỏ cả mệnh đề.
    ("S021", "Điều đó", "R", "demonstrative",
     "S019–S020: 88 phần trăm thất bại, 8 phần trăm đạt được",
     "high", None, "quy chiếu mệnh đề (extended reference)", 1, None,
     None, "LC", "A"),
    ("S021", "chúng ta", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('chúng ta có thể đang') trong câu không đánh", 1,
     None, None, "LC", "E"),
    ("S021", "thất bại", "L", "repetition",
     "S019: đều thất bại trong vòng hai tuần", "high", None,
     "tự chuốc lấy thất bại", 1, None, None, "LC", None),
    ("S021", "năm mới", "L", "repetition",
     "S019: quyết tâm cho năm mới", "high", None, "bước vào năm mới", 1,
     None, None, "LC", None),
    # [Phase-2] ý định ← quyết tâm (S020): danh từ tổng quát hóa (H&H §6.1
    # general word) — ý định tốt = các quyết tâm đã nêu; EN "intentions"
    # (S022 ST); S058 'ý định tốt' lặp tiếp chuỗi.
    ("S021", "ý định", "L", "general word",
     "S020: đạt được quyết tâm của mình", "med", None,
     "tổng quát hóa quyết tâm → ý định (ý định tốt)", 1, None, None,
     "LC", None),
    # S022 (= EN S023)
    ("S022", "mục tiêu", "L", "repetition",
     "S010: Các mục tiêu phổ biến nhất", "high", None,
     "VI tự sinh danh từ 'mục tiêu' — EN chỉ có 'to do something'", 1,
     None, None, "LC", None),
    ("S022", "thất bại", "L", "repetition",
     "S021: tự chuốc lấy thất bại", "high", None,
     "occ 1: 'thất bại thảm hại' lần 2 trong quote không đánh", 1,
     None, None, "LC", None),
    ("S022", "Borland", "L", "repetition",
     "S017: Borland nói với SBS News", "high", None, None, 1, None,
     None, "LC", None),
    # S023 (= EN S024)
    ("S023", "Nhưng", "C", "adversative",
     "S022: tác động tiêu cực nhất là thất bại", "high", None, None, 1,
     None, None, "LC", None),
    ("S023", "thất bại này", "R", "demonstrative",
     "S021: tự chuốc lấy thất bại", "high", None,
     "hậu chỉ từ 'này'; 'chấp nhận…chấp nhận' lặp trong câu (TC) ghi "
     "note; 'nó' trong câu không đánh", 1, None, None, "LC", "A"),
    # S024 (= EN S025)
    ("S024", "bạn sẽ", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None, None, 1, None,
     None, "LC", "E"),
    ("S024", "thất bại", "L", "repetition",
     "S023: thất bại này", "high", None, None, 1, None, None, "LC",
     None),
    # S025 — [Phase-2] thành công ↔ thất bại (S024): phép đối liên câu
    # (TNT §30; H&H §6.4 opposites) trong quote; EN "success" (S026 ST).
    ("S025", "thành công", "L", "antonym",
     "S024: đôi khi bạn sẽ thất bại", "high", None,
     "phép đối thất bại ↔ thành công (tỷ lệ thành công 100 phần trăm); "
     "mở đầu chuỗi thành công (S038 quy về đây)", 1, None, None, "LC",
     None),
    # S027 (= EN S028)
    ("S027", "Borland", "L", "repetition",
     "S022: Borland nói", "high", None, None, 1, None, None, "LC",
     None),
    ("S027", "quyết tâm năm mới", "L", "repetition",
     "S020: quyết tâm của mình", "high", None, None, 1, None, None,
     "LC", None),
    ("S027", "thất bại", "L", "repetition",
     "S024: bạn sẽ thất bại", "high", None, None, 1, None, None,
     "LC", None),
    ("S027", "lên kế hoạch kém", "L", "repetition",
     "S017: một kế hoạch rất rõ ràng", "high", None,
     "đối lập nghĩa 'kém ↔ rõ ràng/tốt' trong cùng chuỗi", 1, None,
     None, "LC", None),
    # S028 (= EN S029)
    ("S028", "quyết tâm năm mới", "L", "repetition",
     "S027: các quyết tâm năm mới", "high", None, None, 1, None, None,
     "LC", None),
    ("S028", "kế hoạch tốt", "L", "repetition",
     "S027: lên kế hoạch kém", "high", None,
     "đối 'kém ↔ tốt'; 'chúng' trong câu không đánh", 1, None, None,
     "LC", None),
    # [Phase-2] thực hiện ← thực hiện (S017): mắt xích sót của chuỗi thực
    # hiện (H&H §6.2 reiteration; TNT §26 phép lặp) — đối ứng EN
    # implementing (S029 ST); S033 triển khai + S037 thực hiện đều trích
    # S028 làm tiền trạm nên mắt xích này phải có hàng riêng.
    ("S028", "thực hiện", "L", "repetition",
     "S017: bạn sẵn sàng thực hiện", "high", None,
     "kế hoạch tốt để thực hiện chúng — mắt xích bị sót của chuỗi thực "
     "hiện", 1, None, None, "LC", None),
    # S029 (= EN S030)
    ("S029", "chúng ta", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    # S030 (= EN S031)
    # [Phase-2] RECLASSIFY sub personal → demonstrative (H&H §2.4.1.4):
    # "Điều này" = chỉ từ + danh từ tổng quát trỏ cả mệnh đề.
    ("S030", "Điều này", "R", "demonstrative",
     "S029: chúng ta vẫn đang chìm đắm trong chế độ nghỉ lễ",
     "high", None, "quy chiếu mệnh đề (extended reference)", 1, None,
     None, "LC", "A"),
    ("S030", "đây", "R", "demonstrative",
     "S029: Vào ngày 1 tháng 1… nghỉ lễ", "high", None,
     "VI hiện thực hóa time-it bằng chỉ từ — EN không có (bất đối xứng "
     "có chủ đích)", 1, None, None, "LC", "A"),
    ("S030", "thay đổi", "L", "repetition",
     "S015: thay đổi hành vi sức khỏe", "high", None,
     "thay đổi bản thân triệt để", 1, None, None, "LC", None),
    # S031 (= EN S032)
    ("S031", "mùa nghỉ lễ", "L", "repetition",
     "S029: chế độ nghỉ lễ", "high", None,
     "VI không chủ ngữ — EN time-it cũng không đánh", 1, None, None,
     "LC", None),
    # S032 (= EN S033)
    ("S032", "Khi bạn tắm nắng", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "occ 1: lần 2, 3 ('bạn có thể thử', 'bạn lại quay lại') trong "
     "câu không đánh", 1, None, None, "LC", "E"),
    ("S032", "kế hoạch nào", "L", "repetition",
     "S028: kế hoạch tốt", "high", None, None, 1, None, None, "LC",
     None),
    ("S032", "hành vi đó", "L", "repetition",
     "S015: thay đổi hành vi sức khỏe", "high", None,
     "'đó' trong câu chỉ 'một phương pháp' (trong câu); 'duy trì' khởi "
     "tạo chuỗi", 1, None, None, "LC", None),
    # S033 (= EN S034)
    ("S033", "các chiến lược đó", "R", "demonstrative",
     "S032: một phương pháp hiệu quả trong hai tuần", "high", None,
     "hậu chỉ từ 'đó'", 1, None, None, "LC", "A"),
    ("S033", "Bạn", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None, None, 1, None,
     None, "LC", "E"),
    ("S033", "kế hoạch", "L", "repetition",
     "S032: kế hoạch nào", "high", None, None, 1, None, None, "LC",
     None),
    ("S033", "triển khai", "L", "synonym",
     "S028: để thực hiện chúng", "high", None,
     "triển khai ≈ thực hiện (thay đổi từ trong cùng chuỗi)", 1, None,
     None, "LC", None),
    # [Phase-2] lối sống hàng ngày ← thói quen thường ngày (S032): mắt xích
    # sót chuỗi lối sống (H&H §6.2 — VI đổi thói quen → lối sống, lặp hình
    # vị 'ngày'); EN lặp nguyên văn lifestyle (S033–S034 ST).
    ("S033", "lối sống hàng ngày", "L", "synonym",
     "S032: thói quen thường ngày", "med", None,
     "thói quen ≈ lối sống; lặp hình vị ngày (thường ngày ↔ hàng ngày)",
     1, None, None, "LC", None),
    # S034 (= EN S035)
    ("S034", "Và", "C", "additive",
     "S033: Bạn cần có kế hoạạạch để triển khai", "high", None,
     "câu 2 của quote", 1, None, None, "LC", None),
    # S036 (= EN S037)
    ("S036", "bạn kiên trì", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "VI đổi 'stick' thành 'kiên trì' — mất chuỗi 'stick'", 1, None,
     None, "LC", "E"),
    ("S036", "quyết tâm", "L", "repetition",
     "S027: các quyết tâm năm mới", "high", None,
     "kiên trì với quyết tâm của mình", 1, None, None, "LC", None),
    ("S036", "duy trì", "L", "repetition",
     "S032: để duy trì hành vi đó", "high", None,
     "mắt xích VI tự sinh — EN S037 không có từ 'sustain' nào", 1,
     None, None, "LC", None),
    # S037 (= EN S038)
    ("S037", "thực hiện", "L", "repetition",
     "S028: kế hoạch tốt để thực hiện", "high", None, None, 1, None,
     None, "LC", None),
    ("S037", "mục tiêu", "L", "repetition",
     "S022: tự đặt ra mục tiêu", "high", None,
     "occ 1: lần 2 ('một mục tiêu cụ thể') trong câu không đánh", 1,
     None, None, "LC", None),
    # [Phase-2] đạt được ← đạt được (S020): lặp nguyên văn (H&H §6.2;
    # TNT §26 phép lặp) — gloss SMART nối về 'đạt được quyết tâm'; EN
    # achievable ← achieve (S038 ST).
    ("S037", "đạt được", "L", "repetition",
     "S020: thực sự đạt được quyết tâm của mình", "high", None,
     "lặp đạt được (có thể đạt được trong định nghĩa SMART); nhãn S045 "
     "quy về đây", 1, None, None, "LC", None),
    # S038 (= EN S040)
    # [Phase-2] rút span "bạn không bỏ cuộc" → "bạn" (precedent chồng
    # marker của chính P28) để đặt hàng L "bỏ cuộc" không đè hàng R;
    # occ 1 tường minh vì "bạn" xuất hiện 2 lần trong câu.
    ("S038", "bạn", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "occ 1 ('đảm bảo bạn không bỏ cuộc'); lần 2 ('bạn có thể tăng') "
     "trong câu không đánh", 1, None, None, "LC", "E"),
    # [Phase-2] bỏ cuộc ↔ kiên trì (S036): phép đối liên câu có phủ định
    # (TNT §30; H&H §6.4 opposites) — "không bỏ cuộc" = "kiên trì"; EN
    # "give up" (S040 ST).
    ("S038", "bỏ cuộc", "L", "antonym",
     "S036: đảm bảo bạn kiên trì với quyết tâm", "med", None,
     "phép đối kiên trì ↔ bỏ cuộc (đảm bảo bạn không bỏ cuộc)", 1, None,
     None, "LC", None),
    ("S038", "kế hoạch", "L", "repetition",
     "S033: Bạn cần có kế hoạch", "high", None,
     "occ 1: lần 2 ('một kế hoạch rõ ràng' — có hàng 'rõ ràng' riêng) "
     "trong câu", 1, None, None, "LC", None),
    ("S038", "rõ ràng", "L", "repetition",
     "S017: một kế hoạch rất rõ ràng", "high", None,
     "một kế hoạch rõ ràng — VI chuỗi 'rõ' mạnh hơn EN", 1, None, None,
     "LC", None),
    ("S038", "thành công", "L", "repetition",
     "S025: tỷ lệ thành công 100 phần trăm", "high", None,
     "cơ hội thành công của mình", 1, None, None, "LC", None),
    # S040 (= EN S042)
    ("S040", "Cụ thể", "L", "repetition",
     "S037: một mục tiêu cụ thể", "high", None,
     "VI giữ nhãn EN + chú giải (song ngữ); 'thực sự cụ thể' lần 2 "
     "trong câu không đánh", 1, None, None, "LC", None),
    ("S040", "bạn muốn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    ("S040", "đạt được", "L", "repetition",
     "S037: có thể đạt được", "high", None,
     "muốn đạt được; VI lặp từ nơi EN đổi (accomplish)", 1, None,
     None, "LC", None),
    # S041 (= EN S043)
    ("S041", "bạn muốn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2, 3 trong câu không đánh", 1, None, None, "LC", "E"),
    ("S041", "ăn uống lành mạnh hơn", "L", "repetition",
     "S006: Có thể là ăn uống lành mạnh hơn", "high", None,
     "trích lại nguyên văn", 1, None, None, "LC", None),
    # S042 (= EN S044)
    ("S042", "đo lường", "L", "repetition",
     "S037: có thể đo lường được", "high", None,
     "VI giữ nhãn EN + chú giải", 1, None, None, "LC", None),
    ("S042", "bạn sẽ theo dõi", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    # S043 (= EN S045)
    ("S043", "Ví dụ", "C", "additive",
     "S042: Quyết định cách bạn sẽ theo dõi tiến trình", "high",
     None, "kiểu ví dụ; VI lấp đầy E ('chỉ chạy ba lần')", 1, None,
     None, "LC", None),
    ("S043", "bạn cam kết", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "'bạn sẽ biết', 'mình hơi chệch hướng' trong câu không đánh "
     "(reflexive)", 1, None, None, "LC", "E"),
    # S044 (= EN S046)
    ("S044", "sự rõ ràng này", "R", "demonstrative",
     "S040: Specific (Cụ thể)", "high", None,
     "hậu chỉ từ 'này' — danh từ tổng quát bridging", 1, None, None,
     "LC", "A"),
    ("S044", "bạn nhận ra", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "'khi nào bạn cần' lần 2 trong câu không đánh", 1, None, None,
     "LC", "E"),
    ("S044", "Borland", "L", "repetition",
     "S038: Borland (quote) — S027", "high", None, None, 1, None,
     None, "LC", None),
    ("S044", "thành công", "L", "repetition",
     "S038: cơ hội thành công", "high", None,
     "khi nào bạn đang thành công", 1, None, None, "LC", None),
    ("S044", "hiệu chỉnh", "L", "repetition",
     "S043: có thể điều chỉnh một chút", "high", None,
     "lặp hình vị 'chỉnh' (điều chỉnh ↔ hiệu chỉnh)", 1, None, None,
     "LC", None),
    # S045 (= EN S047)
    ("S045", "đạt được", "L", "repetition",
     "S037: có thể đạt được", "high", None,
     "VI giữ nhãn 'Achievable (Có thể đạt được)' song ngữ", 1, None,
     None, "LC", None),
    ("S045", "mục tiêu", "L", "repetition",
     "S037: đặt ra một mục tiêu 'SMART'", "high", None,
     "occ 1: lần 2 ('mục tiêu của bạn') trong câu không đánh", 1,
     None, None, "LC", None),
    ("S045", "thực tế", "L", "repetition",
     "S037: thực tế", "high", None,
     "mục tiêu của bạn thực tế với hoàn cảnh", 1, None, None, "LC",
     None),
    ("S045", "của bạn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('hoàn cảnh của bạn') trong câu không đánh", 1,
     None, None, "LC", "E"),
    # S046 (= EN S048)
    ("S046", "bạn đã sống", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    ("S046", "mục tiêu", "L", "repetition",
     "S045: đặt mục tiêu cao", "high", None,
     "việc đặt mục tiêu nấu", 1, None, None, "LC", None),
    ("S046", "bữa ăn", "L", "repetition",
     "S041: mỗi bữa ăn", "high", None,
     "những bữa ăn ngon mỗi tối", 1, None, None, "LC", None),
    # S047 (= EN S049)
    ("S047", "Thay vào đó", "C", "adversative",
     "S046: việc đặt mục tiêu nấu bữa ăn ngon có thể quá sức",
     "high", None, "thay thế đề xuất", 1, None, None, "LC", None),
    # [Phase-2] dễ quản lý hơn ← S046 "một điều quá sức": quy chiếu so
    # sánh (H&H §2.5) — "hơn" so với mục tiêu nấu bữa ngon mỗi tối ở câu
    # trước; EN "more manageable" (S049 ST).
    ("S047", "dễ quản lý hơn", "R", "comparative",
     "S046: việc đặt mục tiêu nấu những bữa ăn ngon mỗi tối có thể là "
     "một điều quá sức", "high", None,
     "[LC] quy chiếu so sánh: dễ quản lý HƠN so với việc nấu bữa ăn "
     "ngon mỗi tối (S046); H&H §2.5", 1, None, None, "LC", "A"),
    ("S047", "một mục tiêu", "L", "repetition",
     "S046: việc đặt mục tiêu", "high", None,
     "'mục tiêu này dễ quản lý' lần 2 trong câu là apposition, "
     "không đánh", 1, None, None, "LC", None),
    ("S047", "nấu", "L", "repetition",
     "S046: đặt mục tiêu nấu", "high", None, "tự nấu ba bữa tối", 1,
     None, None, "LC", None),
    ("S047", "bữa tối", "L", "repetition",
     "S046: những bữa ăn ngon", "high", None, None, 1, None, None,
     "LC", None),
    ("S047", "giúp bạn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    ("S047", "thành công", "L", "repetition",
     "S044: khi nào bạn đang thành công", "high", None, None, 1,
     None, None, "LC", None),
    # S048 (= EN S050)
    ("S048", "Thực tế", "L", "repetition",
     "S045: thực tế với hoàn cảnh", "high", None,
     "VI giữ nhãn 'Realistic (Thực tế)' song ngữ", 1, None, None,
     "LC", None),
    ("S048", "mục tiêu", "L", "repetition",
     "S047: một mục tiêu", "high", None, "xem mục tiêu của bạn", 1,
     None, None, "LC", None),
    ("S048", "của bạn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('lối sống của bạn') trong câu không đánh", 1, None,
     None, "LC", "E"),
    # [Phase-2] lối sống ← lối sống hàng ngày (S033): mắt xích sót chuỗi
    # lối sống (H&H §6.2 reiteration); EN "your lifestyle" (S050 ST).
    ("S048", "lối sống", "L", "repetition",
     "S033: lối sống hàng ngày của mình", "high", None,
     "lặp lối sống (phù hợp với lối sống của bạn)", 1, None, None, "LC",
     None),
    # S049 (= EN S051)
    ("S049", "Ví dụ", "C", "additive",
     "S048: Hãy cân nhắc xem mục tiêu của bạn", "high", None,
     "kiểu ví dụ", 1, None, None, "LC", None),
    ("S049", "bạn chưa bao giờ", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None, None, 1, None, None,
     "LC", "E"),
    # S050 (= EN S052)
    ("S050", "Bạn", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "'bạn có cần' lần 2, 3 trong câu không đánh", 1, None, None,
     "LC", "E"),
    ("S050", "mục tiêu thực tế", "L", "repetition",
     "S048: Thực tế", "high", None,
     "'mục tiêu đó' trong câu (hậu chỉ) không đánh", 1, None, None,
     "LC", None),
    # S051 (= EN S053)
    ("S051", "bạn thực sự có thể", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None, None, 1, None,
     None, "LC", "E"),
    # [Phase-2] RECLASSIFY L repetition → R comparative (H&H §2.5):
    # "thực tế hơn" so với "không phải là mục tiêu thực tế" (S050) ở câu
    # trước (mapping §3.13 một hình thức một hàng); EN "more realistic"
    # (S053 ST) đồng bộ reclassify.
    ("S051", "thực tế hơn", "R", "comparative",
     "S050: đó không phải là mục tiêu thực tế", "high", None,
     "[LC] quy chiếu so sánh: thực tế HƠN so với mục tiêu vừa bị bác "
     "(S050); mặt lặp thực tế ghi ở analysis §6", 1, None, None, "LC",
     "A"),
    ("S051", "đạt được", "L", "repetition",
     "S045: Có thể đạt được", "high", None, None, 1, None, None,
     "LC", None),
    ("S051", "Borland", "L", "repetition",
     "S044: Borland cho rằng", "high", None, None, 1, None, None,
     "LC", None),
    # S052 (= EN S054)
    ("S052", "Có giới hạn thời gian", "L", "repetition",
     "S037: có giới hạn thời gian", "high", None,
     "VI giữ nhãn 'Time-bound' + chú giải; 'khung thời gian' lần 2 "
     "trong câu ghi note", 1, None, None, "LC", None),
    ("S052", "của bạn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('mục tiêu của bạn') trong câu không đánh", 1,
     None, None, "LC", "E"),
    ("S052", "rõ ràng", "L", "repetition",
     "S038: một kế hoạch rõ ràng", "high", None,
     "khung thời gian rõ ràng", 1, None, None, "LC", None),
    ("S052", "đạt được", "L", "repetition",
     "S051: có thể đạt được", "high", None,
     "để đạt được mục tiêu", 1, None, None, "LC", None),
    ("S052", "mục tiêu", "L", "repetition",
     "S048: xem mục tiêu của bạn", "high", None, None, 1, None, None,
     "LC", None),
    # S053 (= EN S055)
    ("S053", "bạn sẽ", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('bạn sẽ chạy được') trong câu không đánh", 1,
     None, None, "LC", "E"),
    ("S053", "khỏe mạnh", "L", "repetition",
     "S010: lựa chọn thực phẩm lành mạnh hơn — sức khỏe", "high",
     None, "khỏe mạnh ≈ fit/lành mạnh", 1, None, None, "LC", None),
    ("S053", "nêu rõ", "L", "repetition",
     "S044: sự rõ ràng này", "high", None,
     "chuỗi 'rõ' VI; EN dùng 'specify' (hình vị speci-)", 1, None,
     None, "LC", None),
    # [Phase-2] chạy ← chạy (S043): chuỗi chạy (H&H §6.2 reiteration) —
    # ví dụ chạy bộ lặp qua khối Time-bound; EN "run" (S055 ST).
    ("S053", "chạy", "L", "repetition",
     "S043: cam kết chạy bốn lần một tuần", "high", None,
     "lặp chạy (bạn sẽ chạy được 5 km)", 1, None, None, "LC", None),
    # S054 (= EN S056)
    ("S054", "của bạn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('giúp bạn') trong câu không đánh", 1, None, None,
     "LC", "E"),
    ("S054", "quyết tâm", "L", "repetition",
     "S052: mốc thời gian cho quyết tâm", "high", None,
     "mốc thời gian cho quyết tâm của bạn", 1, None, None, "LC",
     None),
    ("S054", "mốc thời gian", "L", "repetition",
     "S052: Có giới hạn thời gian", "high", None, None, 1, None,
     None, "LC", None),
    ("S054", "theo dõi tiến trình", "L", "repetition",
     "S042: theo dõi tiến trình của mình", "high", None, None, 1,
     None, None, "LC", None),
    # S055 (= EN S057)
    ("S055", "bạn sẽ biến", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "'giúp bạn' lần 2 trong câu không đánh; 'của mình' phản thân", 1,
     None, None, "LC", "E"),
    ("S055", "quyết tâm", "L", "repetition",
     "S054: mốc thời gian cho quyết tâm", "high", None,
     "lập cấu trúc cho quyết tâm của mình", 1, None, None, "LC",
     None),
    ("S055", "kế hoạch", "L", "repetition",
     "S038: một kế hoạch rõ ràng", "high", None,
     "một kế hoạch rõ ràng, có thể thực hiện được", 1, None, None,
     "LC", None),
    ("S055", "rõ ràng", "L", "repetition",
     "S053: nêu rõ", "high", None, None, 1, None, None, "LC", None),
    ("S055", "thực hiện được", "L", "repetition",
     "S037: để thực hiện một điều gì đó", "high", None,
     "'gắn bó' — VI đổi từ nơi EN lặp 'stick'", 1, None, None, "LC",
     None),
    # S057 (= EN S059)
    ("S057", "bạn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "occ 1: lần 2 ('bạn không đơn độc') trong câu không đánh", 1,
     None, None, "LC", "E"),
    ("S057", "quyết tâm năm mới", "L", "repetition",
     "S055: quyết tâm của mình", "high", None, None, 1, None, None,
     "LC", None),
    ("S057", "không thực hiện được", "L", "repetition",
     "S002: không thực hiện được những lời cam kết", "high", None,
     "hồi quy xa 55 câu — VI quay lại chuỗi 'không thực hiện được' "
     "sau chuỗi 'thất bại'", 1, None, None, "LC", None),
    # S058 (= EN S060)
    ("S058", "mục tiêu", "L", "repetition",
     "S052: đạt được mục tiêu", "high", None,
     "Nhiều người đặt ra mục tiêu", 1, None, None, "LC", None),
    ("S058", "ý định tốt", "L", "repetition",
     "S021: ý định tốt", "high", None, "với ý định tốt nhất", 1,
     None, None, "LC", None),
    ("S058", "thất bại", "L", "repetition",
     "S027: đều thất bại vì", "high", None,
     "'thực tế trong cuộc sống' — realities ≠ realistic, không đánh "
     "(ghi §8)", 1, None, None, "LC", None),
    # S059 (= EN S061)
    ("S059", "những khoảnh khắc này", "R", "demonstrative",
     "S058: thất bại khi đối mặt với thực tế", "high", None,
     "hậu chỉ từ 'này' — bridging", 1, None, None, "LC", "A"),
    ("S059", "Borland", "L", "repetition",
     "S051: Borland nói", "high", None, None, 1, None, None, "LC",
     None),
    # S060 (= EN S062)
    ("S060", "thay đổi", "L", "repetition",
     "S030: thay đổi bản thân triệt để", "high", None,
     "rất khó để thay đổi hoàn toàn; 'Thực tế,' trạng từ câu không "
     "đánh (ghi §8)", 1, None, None, "LC", None),
    ("S060", "Borland", "L", "repetition",
     "S059: Borland nhấn mạnh", "high", None, None, 1, None, None,
     "LC", None),
    # S061 (= EN S063)
    # [Phase-2] RECLASSIFY sub personal → demonstrative (H&H §2.4.1.4):
    # "điều đó" = danh từ tổng quát + chỉ từ trỏ cả mệnh đề — đồng bộ với
    # "Điều đó/Điều này" (S021/S030 TT); EN "it happens" (S063 ST) giữ
    # sub personal vì 'it' là đại từ nhân xưng (mở rộng nghĩa §2.3.3).
    ("S061", "điều đó", "R", "demonstrative",
     "S060: thay đổi hoàn toàn và trở thành người khác", "high",
     None, "quy chiếu mệnh đề (extended reference)", 1, None, None,
     "LC", "A"),
    ("S061", "làm điều đó", "S", "verbal",
     "S060: thay đổi hoàn toàn", "high", None,
     "[LC] 'làm' thế động từ — VI giữ pro-form hiếm hoi (VI gộp 2 lần "
     "EN 'do it and do it' thành 1)", 1, None, None, "LC", None),
    ("S061", "thành công", "L", "repetition",
     "S047: giúp bạn thành công", "high", None,
     "'họ' VI tự thêm trong câu, không đánh", 1, None, None, "LC",
     None),
    # S062 (= EN S064)
    ("S062", "Ông", "R", "personal",
     "S060: Borland giải thích", "high", None,
     "VI giữ danh xưng 'Ông'", 1, None, None, "LC", "A"),
    ("S062", "thay đổi", "L", "repetition",
     "S060: thay đổi hoàn toàn", "high", None,
     "occ 1: lần 2, 3 ('sự kiện thay đổi cuộc sống', 'thay đổi bản "
     "thân') trong câu không đánh", 1, None, None, "LC", None),
    # S063 (= EN S065)
    ("S063", "Tuy nhiên", "C", "adversative",
     "S062: sự thay đổi được thúc đẩy bởi nghịch cảnh", "high",
     None, "VI đảo connective lên đầu câu", 1, None, None, "LC",
     None),
    ("S063", "chúng ta", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None,
     "đối với hầu hết chúng ta", 1, None, None, "LC", "E"),
    ("S063", "quyết tâm", "L", "repetition",
     "S057: quyết tâm năm mới", "high", None, "các quyết tâm", 1,
     None, None, "LC", None),
    ("S063", "nghịch cảnh", "L", "repetition",
     "S062: nghịch cảnh đáng kể", "high", None, None, 1, None, None,
     "LC", None),
    ("S063", "phấn đấu", "L", "repetition",
     "S002: chúng ta phấn đấu để tự hoàn thiện", "high", None,
     "hồi quy xa 61 câu", 1, None, None, "LC", None),
    # S064 (= EN S066)
    ("S064", "Nhưng", "C", "adversative",
     "S063: phấn đấu hướng tới phiên bản tốt hơn", "high", None,
     None, 1, None, None, "LC", None),
    ("S064", "Borland", "L", "repetition",
     "S062: Borland giải thích — Ông", "high", None, None, 1, None,
     None, "LC", None),
    ("S064", "cảnh báo không nên", "L", "repetition",
     "S016: Ông cảnh báo không nên", "high", None,
     "lặp nguyên cụm", 1, None, None, "LC", None),
    ("S064", "hướng tới", "L", "repetition",
     "S063: phấn đấu hướng tới", "high", None, None, 1, None, None,
     "LC", None),
    # S065 (= EN S067)
    ("S065", "bạn thường thấy", "R", "personal",
     "độc giả (ngoại văn bản — quote)", "med", None,
     "'mà bạn thực sự không muốn' lần 2 trong câu không đánh; VI mất "
     "ẩn dụ 'fantasised'", 1, None, None, "LC", "E"),
    ("S065", "thay đổi", "L", "repetition",
     "S062: sự thay đổi cá nhân sâu sắc", "high", None,
     "cố gắng thay đổi từ con người hiện tại", 1, None, None, "LC",
     None),
    ("S065", "phiên bản tốt hơn", "L", "repetition",
     "S063: một phiên bản tốt hơn của chính mình", "high", None,
     "'con người' lặp 2 lần trong câu (TC) ghi note", 1, None, None,
     "LC", None),
    # S066 (= EN S068)
    # [Phase-2] RECLASSIFY sub nominal → demonstrative (H&H §2.4) — đồng bộ
    # với EN "This disconnect" (S068 ST) và quy ước "sự rõ ràng này/
    # những khoảnh khắc này".
    ("S066", "Sự ngắt kết nối này", "R", "demonstrative",
     "S065: con người hiện tại thành con người tốt hơn", "high",
     None, "danh từ tổng quát tóm chỉ; hậu chỉ từ 'này'", 1, None,
     None, "LC", "A"),
    ("S066", "những mục tiêu cao cả này", "R", "demonstrative",
     "S058: Nhiều người đặt ra mục tiêu", "high", None,
     "hai hậu chỉ từ 'này' trong một câu (occ 1–2)", 1, None, None,
     "LC", "A"),
    ("S066", "chúng ta", "R", "personal",
     "cộng đồng (ngoại văn bản)", "med", None,
     "khi chúng ta nhận ra", 1, None, None, "LC", "E"),
    ("S066", "thất bại", "L", "repetition",
     "S058: thất bại khi đối mặt", "high", None,
     "sự thất vọng và thất bại", 1, None, None, "LC", None),
    ("S066", "đạt được", "L", "repetition",
     "S052: để đạt được mục tiêu", "high", None,
     "VI lặp từ nơi EN đổi ('meet')", 1, None, None, "LC", None),
    # [Phase-2] hy sinh ← S065 "rất nhiều thứ mà bạn thực sự không muốn
    # làm": danh từ tổng quát bridging (H&H §6.1 general word) — đối ứng
    # EN "the sacrifices" (S068 ST, alt "R: the"); VI vô định — dịch
    # chuyển the ↔ zero (NTT 2020 §2.2).
    ("S066", "hy sinh", "L", "general word",
     "S065: rất nhiều thứ mà bạn thực sự không muốn làm", "med", None,
     "những hy sinh cần thiết — tổng quát hóa các thứ phải đánh đổi của "
     "'phiên bản tốt hơn'", 1, None, None, "LC", None),
    # S067 (= EN S069)
    ("S067", "chúng ta", "R", "personal",
     "cộng đồng (ngoại văn bản — quote)", "med", None, None, 1, None,
     None, "LC", "E"),
    ("S067", "phiên bản", "L", "repetition",
     "S065: phiên bản tốt hơn của bản thân", "high", None,
     "đạt được phiên bản hoàn hảo", 1, None, None, "LC", None),
    ("S067", "hoàn hảo", "L", "repetition",
     "S064: hướng tới sự hoàn hảo", "high", None, None, 1, None,
     None, "LC", None),
    # S068 (= EN S070)
    # [Phase-2] RECLASSIFY sub additive → continuative (H&H §5.8; protocol
    # nhóm 5): "Trên thực tế," đầu câu mở lượt nhấn mạnh discours — trước
    # đây ghi additive; EN "In fact" (S070 ST) đồng bộ.
    ("S068", "Trên thực tế", "C", "continuative",
     "S067: Rất ít người trong chúng ta đạt được phiên bản hoàn hảo",
     "high", None,
     "continuative tăng tiến: chỉnh sub từ 'additive' theo H&H §5.8", 1,
     None, None, "LC", None),
    ("S068", "chúng ta", "R", "personal",
     "cộng đồng (ngoại văn bản — quote)", "med", None,
     "không ai trong chúng ta — VI lấp đầy E nên không có E phía VI",
     1, None, None, "LC", "E"),
    # [Phase-2] hoàn hảo ← phiên bản hoàn hảo (S067): mắt xích sót chuỗi
    # hoàn hảo (H&H §6.2 reiteration; TNT §26 phép lặp) — từ lấp đầy vị
    # ngữ ∅ của EN S070 ('thực sự hoàn hảo'); EN đối ứng nằm trong hàng E
    # nên không có hàng L riêng phía EN.
    ("S068", "hoàn hảo", "L", "repetition",
     "S067: phiên bản hoàn hảo của chính bản thân", "high", None,
     "lặp hoàn hảo — VI hiện thực hóa ∅ vị ngữ của EN S070", 1, None,
     None, "LC", None),
    # S069 (= EN S071)
    ("S069", "của bạn", "R", "personal",
     "độc giả (ngoại văn bản)", "med", None,
     "Hãy coi thất bại của bạn", 1, None, None, "LC", "E"),
    ("S069", "thất bại", "L", "repetition",
     "S066: sự thất vọng và thất bại", "high", None, None, 1, None,
     None, "LC", None),
    # S070 (= EN S072)
    ("S070", "thất bại", "L", "repetition",
     "S069: thất bại của bạn", "high", None, None, 1, None, None,
     "LC", None),
    ("S070", "quá trình", "L", "synonym",
     "S023: một phần của hành trình", "med", None,
     "quá trình ≈ hành trình — lặp hình vị 'trình'", 1, None, None,
     "LC", None),
]
