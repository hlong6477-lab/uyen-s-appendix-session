# P36 tie table — WRITTEN BY HAND FROM work/analysis/P36_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Text/gap_after là chuỗi con nguyên văn trong câu (kiểm bằng pipeline.locate).
# Gộp câu: EN S032+S033 → TT S032 (không có khối cắt).
# Khối quote dịch đủ cả hai phía; 5 hàng TC (S003 did-EN; E S013/S023 VI-only, E S022 đối xứng).
# [Phase-2] Bổ sung theo PHASE2_PROTOCOL.md: 20 hàng mới EN / 23 hàng mới VI;
# 1 RECLASSIFY (S009 ST "the cases": R nominal → L general word theo
# H&H §6.1 + mapping §3.6 + protocol nhóm 3), +alt "R: the" (S031 ST, nhóm 8),
# 3 note cũ cập nhật (TT S005 "của nghiên cứu", TT S009 "một nửa", TT S026 "vú").

ST = [
    # S002
    ("S002", "the study", "L", "repetition", "S001: A German study", "high",
     None, "danh ngữ xác định; đầu từ lặp", 1, None, None, "LC", None),
    ("S002", "artificial intelligence", "L", "repetition",
     "S001: artificial intelligence", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] doctors ← S001: mắt xích sót chuỗi doctors (H&H §6.2
    # reiteration; TNT §26 phép lặp) — doctors trong apposition của
    # radiologists trỏ về doctors của S001.
    ("S002", "doctors", "L", "repetition",
     "S001: when doctors get help from artificial intelligence", "high",
     None, "lặp doctors (apposition 'doctors who analyze…' = doctors của "
     "S001); H&H §6.2; TNT §26", 1, None, None, "LC", None),
    # S003
    ("S003", "They", "R", "personal", "S002: radiologists", "high", None,
     "hồi quy chủ ngữ = các bác sĩ X quang", 1, None, None, "LC", "A"),
    ("S003", "did", "S", "verbal", "S003: found (trong câu)", "high", None,
     "[TC] 'did' thế động từ 'found'; VI hiện thực hóa 'cách chỉ có con "
     "người…' nên không có S phía VI", 1, None, None, "TC", None),
    ("S003", "humans", "L", "collocation", "S001: artificial intelligence",
     "med", None,
     "trường nghĩa đối lập con người↔AI; 'one' là số từ, không phải phép thế",
     1, None, None, "LC", None),
    # [Phase-2] women ← S002: mắt xích sót chuỗi women (H&H §6.2; protocol
    # nhóm 12 — chuỗi S002→S003→S007→S010 mới kín).
    ("S003", "women", "L", "repetition",
     "S002: more than 460,000 German women", "high", None,
     "lặp women (for every 1,000 women); H&H §6.2; TNT §26", 1, None,
     None, "LC", None),
    # [Phase-2] cancer ← S001: mắt xích được S004 "breast cancer" cite làm
    # tiền trạm nhưng chưa có hàng (protocol nhóm 12) — hình vị cancer lặp
    # trong "cancer detection rate" (H&H §6.2; TNT §26).
    ("S003", "cancer", "L", "repetition",
     "S001: the cancer detection rate", "high", None,
     "lặp hình vị cancer (one more cancer ← cancer detection rate); "
     "H&H §6.2", 1, None, None, "LC", None),
    # S004
    ("S004", "It", "R", "personal", "S001: A German study", "high", None,
     "It = nghiên cứu", 1, None, None, "LC", "A"),
    ("S004", "AI", "L", "synonym", "S001: artificial intelligence", "high",
     None, "viết tắt cùng chỉ AI", 1, None, None, "LC", None),
    ("S004", "breast cancer", "L", "repetition", "S003: one more cancer",
     "high", None, "thêm 'breast' xác định; hình vị 'cancer' lặp chuỗi", 1,
     None, None, "LC", None),
    # [Phase-2] use ← S002 "used": mắt xích sót chuỗi use (H&H §6.2;
    # protocol nhóm 12 — S026 "use of AI" cite S004 nên mắt xích này phải
    # có hàng).
    ("S004", "use", "L", "repetition",
     "S002: used artificial intelligence", "high", None,
     "lặp use (the use of AI ← used); H&H §6.2; TNT §26", 1, None, None,
     "LC", None),
    # [Phase-2] exploration ← S001 study: the + đổi tên (mapping §3.6;
    # protocol nhóm 8) — study → real-world exploration, gần nghĩa theo
    # ngữ cảnh (H&H §6.2 synonym); mạo từ the → alt "R: the" (mapping
    # §3.13); VI "cuộc khám phá" đối xứng.
    ("S004", "exploration", "L", "synonym",
     "S001: A German study", "med", "R: the",
     "exploration ≈ study: đổi tên/tổng quát hóa (H&H §6.2; mapping "
     "§3.6)", 1, None, None, "LC", None),
    # [Phase-2] help ← S001: mắt xích sót chuỗi help (H&H §6.2) — chuỗi
    # S001→S004→S009→S015→S024 mới kín; VI lược 'giúp' (để phát hiện) nên
    # chỉ EN có hàng mắt xích này.
    ("S004", "help", "L", "repetition",
     "S001: get help from artificial intelligence", "high", None,
     "lặp help (to help detect); H&H §6.2; TNT §26", 1, None, None, "LC",
     None),
    # [Phase-2] detect ← S001 detection: danh từ hóa ngược (H&H §6.2
    # reiteration; TNT §26) — như offers ← offered (precedent P21).
    ("S004", "detect", "L", "repetition",
     "S001: the cancer detection rate", "high", None,
     "lặp hình vị detect- (detect ← detection rate); H&H §6.2", 1, None,
     None, "LC", None),
    # S005
    ("S005", "The breast cancer detection rate", "L", "repetition",
     "S001: the cancer detection rate", "high", None,
     "lặp chuỗi tỷ lệ phát hiện; 'this' trong câu chỉ vế đầu, không đánh",
     1, None, None, "LC", None),
    ("S005", "Germany", "L", "repetition", "S002: German women", "high",
     None, "chuỗi German/Germany", 1, None, None, "LC", None),
    ("S005", "the study’s", "L", "repetition", "S001: A German study",
     "high", None, "dấu nháy cong của nguồn", 1, None, None, "LC", None),
    # [Phase-2] better ← S001: quy chiếu so sánh (H&H §2.5; protocol nhóm
    # 1) — "better" so với mức cơ bản (không AI) đã lập ở S001; tie R so
    # sánh đầu tiên của cặp; VI "tốt hơn" đối xứng.
    ("S005", "better", "R", "comparative",
     "S001: the cancer detection rate improves by almost 18% when doctors "
     "get help", "med", None,
     "H&H §2.5 quy chiếu so sánh: is better = tốt hơn mức không AI "
     "(chuẩn hồi phục từ S001)", 1, None, None, "LC", "A"),
    # [Phase-2] investigator ← S003 researchers: đồng nghĩa (H&H §6.2
    # reiteration — synonym); VI lặp nguyên văn nhà nghiên cứu.
    ("S005", "investigator", "L", "synonym",
     "S003: according to researchers", "med", None,
     "investigator ≈ researcher (principal investigator); H&H §6.2", 1,
     None, None, "LC", None),
    # S006
    ("S006", "And", "C", "additive",
     "S005: tỷ lệ phát hiện tốt hơn (quote Katalinic)", "high", None,
     "nối liên câu trong quote", 1, None, None, "LC", None),
    ("S006", "this evidence", "R", "demonstrative",
     "S005: the detection rate is better — mức = bằng chứng", "high", None,
     "chỉ từ hồi quy; đồng thời lặp 'evidence' trong cụm, ghi note", 1,
     None, None, "LC", "A"),
    ("S006", "AI", "L", "repetition", "S004: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S006", "breast cancer screening", "L", "repetition",
     "S004: breast cancer", "high", None,
     "lặp 'breast cancer'; 'screening' khởi tạo chuỗi sàng lọc; 'we' hư "
     "chỉ, 'this should be standard' trong câu — không đánh", 1, None, None,
     "LC", None),
    # [Phase-2] use ← S004: mắt xích chuỗi use trong quote Katalinic (H&H
    # §6.2; tiền trạm = nhắc gần nhất).
    ("S006", "use", "L", "repetition", "S004: the use of AI", "high",
     None, "lặp use (start to use more AI); H&H §6.2", 1, None, None,
     "LC", None),
    # S007
    ("S007", "The mammograms", "L", "repetition", "S002: the mammograms",
     "high", None,
     "danh ngữ xác định hồi quy; 463,094 là số liệu, không phải tie", 1,
     None, None, "LC", None),
    ("S007", "German women", "L", "repetition",
     "S002: more than 460,000 German women", "high", None, None, 1, None,
     None, "LC", None),
    # [Phase-2] examined ← S002 examine: mắt xích sót chuỗi kiểm tra nhũ
    # ảnh (H&H §6.2 reiteration; TNT §26) — bị động hóa nhưng cùng hình vị.
    ("S007", "examined", "L", "repetition",
     "S002: used artificial intelligence to examine the mammograms",
     "high", None, "lặp examined (were examined ← to examine); H&H §6.2",
     1, None, None, "LC", None),
    # S008
    ("S008", "About half", "R", "nominal",
     "S007: The mammograms of 463,094 German women", "high", None,
     "quy chiếu lượng: nửa số nhũ ảnh", 1, None, None, "LC", "A"),
    ("S008", "radiologists", "L", "repetition", "S002: radiologists",
     "high", None, None, 1, None, None, "LC", None),
    ("S008", "standard", "L", "repetition", "S006: this should be standard",
     "med", None,
     "lặp từ, khác phát ngôn (khát vọng ↔ quy trình sẵn có); 'which' "
     "trong câu không đánh", 1, None, None, "LC", None),
    ("S008", "Germany", "L", "repetition", "S005: Germany", "high", None,
     None, 1, None, None, "LC", None),
    # S009
    ("S009", "half", "L", "repetition", "S008: About half", "high", None,
     "'just over half' đối lượng với 'About half'", 1, None, None, "LC",
     None),
    # [Phase-2] RECLASSIFY R nominal → L general word (H&H §6.1; mapping
    # §3.6; protocol nhóm 3 — "case" là danh từ tổng quát trỏ về các lần
    # chụp nhũ ảnh S007–S008): mạo từ the chuyển vào alt (mapping §3.13);
    # VI "trường hợp" thêm hàng L đối xứng (the ↔ zero, NTT 2020 §2.2).
    ("S009", "the cases", "L", "general word",
     "S007–S008: các lần chụp nhũ ảnh được xem xét", "high", "R: the",
     "danh từ tổng quát (H&H §6.1): mỗi lần chụp nhũ ảnh = một case; VI "
     "'trường hợp' có hàng riêng", 1, None, None, "LC", None),
    # [Phase-2] assisted ← S004 help: đồng nghĩa (H&H §6.2) — chuỗi help
    # S001→S004→S009→S015→S024 kín; VI "hỗ trợ" ← "trợ giúp" đối ứng.
    ("S009", "assisted", "L", "synonym",
     "S004: to help detect breast cancer", "med", None,
     "assisted ≈ helped (were assisted by AI ≈ get help); H&H §6.2", 1,
     None, None, "LC", None),
    ("S009", "the humans", "L", "repetition", "S003: humans", "high", None,
     "mạo từ xác định chỉ nhóm bác sĩ X quang", 1, None, None, "LC", None),
    ("S009", "AI", "L", "repetition", "S006: AI", "high", None, None, 1,
     None, None, "LC", None),
    # S010
    ("S010", "AI", "L", "repetition", "S009: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S010", "the breast cancer detection rate", "L", "repetition",
     "S005: The breast cancer detection rate", "high", None, None, 1,
     None, None, "LC", None),
    ("S010", "screened", "L", "repetition", "S006: breast cancer screening",
     "high", None, "screening → screened", 1, None, None, "LC", None),
    ("S010", "humans", "L", "repetition", "S009: the humans", "high",
     None, None, 1, None, None, "LC", None),
    ("S010", "women", "L", "repetition", "S007: German women", "high",
     None,
     "occ 1: lặp 2 lần trong câu (6.7 vs 5.7 per 1,000 women), chọn lần "
     "1; 'compared to' so sánh rút gọn trong câu, không đánh E", 1, None,
     None, "LC", None),
    # S011
    ("S011", "AI", "L", "repetition", "S010: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S011", "human readers", "L", "repetition", "S010: humans", "high",
     None,
     "'human' lặp chuỗi; 'readers' từ mới; VI 'người đọc' từ mới thuần — "
     "không có hàng VI", 1, None, None, "LC", None),
    ("S011", "Katalinic", "L", "repetition", "S005: Dr. Alexander Katalinic",
     "high", None, None, 1, None, None, "LC", None),
    # S012
    ("S012", "But", "C", "adversative",
     "S011: AI suitable for replacing human readers to a certain extent",
     "high", None, "nối liên câu trong quote; 'you' hư chỉ, không đánh", 1,
     None, None, "LC", None),
    # S013
    ("S013", "This", "R", "demonstrative",
     "S012: how far do you want to go?", "high", None,
     "chỉ từ hồi quy câu hỏi S012; 'not only…also' trong câu, không đánh",
     1, None, None, "LC", "A"),
    # S014
    ("S014", "society’s", "L", "repetition", "S013: a social question",
     "high", None, "social → society cùng gốc; dấu nháy cong của nguồn", 1, None,
     None, "LC", None),
    ("S014", "AI", "L", "repetition", "S011: AI", "high", None, None, 1,
     None, None, "LC", None),
    # S015
    ("S015", "The study", "L", "repetition", "S001: A German study",
     "high", None, None, 1, None, None, "LC", None),
    ("S015", "AI", "L", "repetition", "S014: AI", "high", None,
     "'also' trong câu, không đánh C", 1, None, None, "LC", None),
    ("S015", "helped", "L", "repetition",
     "S001: get help from artificial intelligence", "high", None,
     "chuỗi help; 'false positive results' khởi tạo chuỗi", 1, None, None,
     "LC", None),
    # [Phase-2] found ← S003: mắt xích sót chuỗi found (H&H §6.2; protocol
    # nhóm 12 — chuỗi S003→S015→S018 mới kín).
    ("S015", "found", "L", "repetition",
     "S003: They found one more cancer", "high", None,
     "lặp found (The study found that); H&H §6.2", 1, None, None, "LC",
     None),
    # S016
    ("S016", "Artificial intelligence", "L", "repetition",
     "S002: artificial intelligence", "high", None,
     "viết đầy đủ sau chuỗi viết tắt", 1, None, None, "LC", None),
    ("S016", "however", "C", "adversative",
     "S015: AI also helped reduce false positive results", "high", None,
     None, 1, None, None, "LC", None),
    ("S016", "cancers", "L", "repetition", "S004: breast cancer", "high",
     None, "chuỗi ung thư", 1, None, None, "LC", None),
    # [Phase-2] miss ↔ found (S003): phép đối liên câu phát hiện↔bỏ sót
    # (TNT §30; H&H §6.4 opposites) — S019 "missed" cite mắt xích này
    # (protocol nhóm 12).
    ("S016", "miss", "L", "antonym",
     "S003: They found one more cancer", "high", None,
     "phép đối found ↔ miss (AI phát hiện ↔ AI bỏ sót); TNT §30; H&H "
     "§6.4", 1, None, None, "LC", None),
    # S017
    ("S017", "The AI", "L", "repetition", "S016: Artificial intelligence",
     "high", None, None, 1, None, None, "LC", None),
    ("S017", "the humans", "L", "repetition", "S010: humans", "high", None,
     "'not perfect' lặp 2 lần trong câu (TC), không đánh thêm", 1, None,
     None, "LC", None),
    ("S017", "the artificial intelligence", "L", "repetition",
     "S016: Artificial intelligence", "high", None,
     "lần 2 của chuỗi AI trong câu, dạng đầy đủ — khác token nên đánh "
     "riêng (như federal workers/workforce ở P32)", 1, None, None, "LC",
     None),
    ("S017", "the study", "L", "repetition", "S015: The study", "high",
     None, None, 1, None, None, "LC", None),
    # [Phase-2] used ← S006 use: mắt xích sót chuỗi use (H&H §6.2) —
    # participle "used in the study"; chuỗi S002→S004→S006→S017→S026 kín.
    ("S017", "used", "L", "repetition", "S006: to use more AI", "high",
     None, "lặp used (the AI used in the study); H&H §6.2", 1, None,
     None, "LC", None),
    # S018
    ("S018", "our", "R", "personal",
     "nhóm nghiên cứu (ngoại văn bản — quote Bunk)", "med", None,
     "ngoại quy chiếu", 1, None, None, "LC", "E"),
    ("S018", "study", "L", "repetition", "S001: A German study", "high",
     None, None, 1, None, None, "LC", None),
    ("S018", "cases", "L", "repetition", "S009: the cases", "high", None,
     "'this case' lần 2 trong câu là chỉ từ trong câu, không đánh", 1,
     None, None, "LC", None),
    ("S018", "the AI", "L", "repetition", "S017: The AI", "high", None,
     None, 1, None, None, "LC", None),
    ("S018", "radiologist", "L", "repetition", "S008: radiologists",
     "high", None, "số ít trong tổ hợp 'a radiologist found cancer'", 1,
     None, None, "LC", None),
    ("S018", "found cancer", "L", "repetition",
     "S003: found one more cancer", "high", None,
     "lặp tổ hợp động từ + tân ngữ", 1, None, None, "LC", None),
    # S019
    ("S019", "however", "C", "adversative",
     "S018: the AI said normal but a radiologist found cancer", "high",
     None, None, 1, None, None, "LC", None),
    ("S019", "Humans", "L", "repetition", "S017: the humans", "high", None,
     None, 1, None, None, "LC", None),
    ("S019", "missed", "L", "repetition", "S016: did miss some cancers",
     "high", None, "chuỗi bỏ sót", 1, None, None, "LC", None),
    ("S019", "a malignancy", "L", "synonym", "S018: found cancer", "high",
     None, "malignancy ≈ cancer (đồng nghĩa trường ung thư)", 1, None,
     None, "LC", None),
    ("S019", "the AI", "L", "repetition", "S018: the AI", "high", None,
     None, 1, None, None, "LC", None),
    ("S019", "the study results", "L", "repetition",
     "S001: A German study", "high", None,
     "'study' lặp chuỗi; 'results' khởi tạo chuỗi kết quả; 'according "
     "to' động từ chức năng", 1, None, None, "LC", None),
    # S020
    ("S020", "AI", "L", "repetition", "S019: the AI", "high", None, None,
     1, None, None, "LC", None),
    ("S020", "humans", "L", "repetition", "S019: Humans", "high", None,
     "'unlike' so sánh trong câu, không đánh", 1, None, None, "LC", None),
    # S021
    ("S021", "Bunk", "L", "repetition", "S017: Stefan Bunk", "high", None,
     None, 1, None, None, "LC", None),
    # S022
    ("S022", "AI", "L", "repetition", "S020: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S022", None, "E", "verbal", "S022: AI works (trong câu)", "high",
     None,
     "[TC] tỉnh lược mệnh đề sau 'like', hồi phục {AI works}; VI đối "
     "xứng 'như' cũng có E; nguồn rườm 'in the same way…like', ghi §8",
     1, "like", "{AI works}", "TC", None),
    # S023
    ("S023", "So", "C", "causal",
     "S020–S022: AI không mệt, hoạt động ổn định mọi lúc", "high", None,
     None, 1, None, None, "LC", None),
    ("S023", "it", "R", "personal",
     "S020–S022: AI doesn't get tired, works the same way", "high", None,
     "occ 1: lần 2 trong câu ('it's also') cùng chuỗi, không đánh", 1,
     None, None, "LC", "A"),
    ("S023", "AI", "L", "repetition", "S022: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S023", "cancers", "L", "repetition", "S018: found cancer", "high",
     None, None, 1, None, None, "LC", None),
    ("S023", "humans", "L", "repetition", "S020: humans", "high", None,
     None, 1, None, None, "LC", None),
    ("S023", "miss", "L", "repetition", "S019: missed", "high", None,
     "missed → miss cùng hình vị", 1, None, None, "LC", None),
    # S024
    ("S024", "AI", "L", "repetition", "S023: AI", "high", None,
     "occ 1: lần 2 trong câu ('reliance on AI') cùng chuỗi, không đánh",
     1, None, None, "LC", None),
    ("S024", "help reduce", "L", "repetition",
     "S015: helped reduce the number of false positive results", "high",
     None, "lặp tổ hợp 'help(ed) reduce'", 1, None, None, "LC", None),
    ("S024", "radiologists", "L", "repetition", "S018: radiologist",
     "high", None,
     "'them' trong câu = radiologists, không đánh", 1, None, None, "LC",
     None),
    ("S024", "cases", "L", "repetition", "S018: cases", "high", None,
     "'complex' khởi tạo chuỗi phức tạp", 1, None, None, "LC", None),
    ("S024", "Bunk", "L", "repetition", "S021: Bunk", "high", None,
     "'according to' động từ chức năng, không đánh C", 1, None, None,
     "LC", None),
    ("S024", "human", "L", "repetition", "S023: humans", "high", None,
     "trong 'human expertise'; 'expertise' khởi tạo chuỗi chuyên môn", 1,
     None, None, "LC", None),
    # [Phase-2] risk ↔ advantage (S023): phép đối liên câu lợi thế↔nguy cơ
    # (TNT §30; H&H §6.4 opposites) — Bunk nêu lợi thế (S023) rồi bổ sung
    # nguy cơ (S024); VI "nguy cơ" đối xứng.
    ("S024", "risk", "L", "antonym",
     "S023: it's definitely an advantage", "med", None,
     "phép đối advantage ↔ risk (lợi thế ↔ nguy cơ); TNT §30; H&H §6.4",
     1, None, None, "LC", None),
    # S025
    ("S025", "Those complex cases", "R", "demonstrative",
     "S024: more complex cases", "high", None,
     "hậu chỉ từ 'those' + lặp 'complex cases', một hàng duy nhất; 'you' "
     "hư chỉ", 1, None, None, "LC", "A"),
    ("S025", "expertise", "L", "repetition", "S024: human expertise",
     "high", None, None, 1, None, None, "LC", None),
    ("S025", "radiologist", "L", "repetition", "S024: radiologists",
     "high", None,
     "an actual radiologist; lỗi hòa hợp chủ-vị của nguồn (cases…is), "
     "ghi §8", 1, None, None, "LC", None),
    ("S025", "Bunk", "L", "repetition", "S024: Bunk", "high", None,
     "'continue to be trained' khởi tạo chuỗi đào tạo", 1, None, None,
     "LC", None),
    # S026
    ("S026", "breast", "L", "repetition", "S006: breast cancer screening",
     "high", None,
     "trong 'breast radiology'; 'MD Anderson Cancer Center' là tên "
     "riêng, không tính tie", 1, None, None, "LC", None),
    ("S026", "use of AI", "L", "repetition", "S004: the use of AI",
     "high", None, "lặp cụm 'use of AI'", 1, None, None, "LC", None),
    ("S026", "radiologists", "L", "repetition", "S025: radiologist",
     "high", None, "could energize radiologists", 1, None, None, "LC",
     None),
    # [Phase-2] radiology ← S025 radiologist: lặp hình vị radiolog- (H&H
    # §6.2; TNT §26) như congressional ← Congress (precedent P32) — danh
    # từ trường chỉ nghề; VI "X quang" đối xứng.
    ("S026", "radiology", "L", "repetition",
     "S025: an actual radiologist", "high", None,
     "lặp hình vị radiolog- (breast radiology); H&H §6.2; TNT §26", 1,
     None, None, "LC", None),
    # S027
    ("S027", "AI", "L", "repetition", "S026: use of AI", "high", None,
     None, 1, None, None, "LC", None),
    ("S027", "us", "R", "personal",
     "S026: a professor in breast radiology — giới radiologists", "med",
     None,
     "occ 1 vì 'focus' chứa 'us'; 'our field' cùng chuỗi trong câu, "
     "không đánh", 1, None, None, "LC", "A"),
    ("S027", "radiologists", "L", "repetition", "S026: radiologists",
     "high", None, "highly trained radiologists", 1, None, None, "LC",
     None),
    ("S027", "trained", "L", "repetition",
     "S025: should continue to be trained", "high", None,
     "chuỗi đào tạo", 1, None, None, "LC", None),
    ("S027", "complex", "L", "repetition", "S024: complex cases", "high",
     None, "'tasks' thay 'cases' — cùng trường phức tạp", 1, None, None,
     "LC", None),
    ("S027", "focus on", "L", "repetition",
     "S024: to focus on more complex cases", "high", None, None, 1, None,
     None, "LC", None),
    ("S027", "Yang", "L", "repetition", "S026: Dr. Wei Yang", "high",
     None, None, 1, None, None, "LC", None),
    # [Phase-2] excited ← S026 energize: đồng nghĩa (H&H §6.2) — narration
    # "energize" được quote cụ thể hóa thành "excited"; VI "hứng thú" ↔
    # "tiếp thêm sinh lực" là liên tưởng (TNT §32) lỏng hơn.
    ("S027", "excited", "L", "synonym",
     "S026: could energize radiologists", "med", None,
     "excited ≈ energized (become more excited ← energize); H&H §6.2", 1,
     None, None, "LC", None),
    # S028
    ("S028", "a human radiologist", "L", "repetition",
     "S027: highly trained radiologists", "high", None,
     "kết 2 chuỗi human (S020) + radiologist; 'Using' đổi đối tượng nên "
     "không tính chuỗi 'use'", 1, None, None, "LC", None),
    ("S028", "artificial intelligence", "L", "repetition",
     "S017: the artificial intelligence", "high", None, "dạng đầy đủ", 1,
     None, None, "LC", None),
    ("S028", "Katalinic", "L", "repetition", "S011: Katalinic", "high",
     None, None, 1, None, None, "LC", None),
    # S029
    ("S029", "The combination", "R", "nominal",
     "S028: Using a human radiologist along with artificial intelligence",
     "high", None,
     "danh ngữ tóm chỉ; VI 'Sự kết hợp' hiện thực hóa trần — chỉ EN có "
     "hàng", 1, None, None, "LC", "A"),
    ("S029", "a human", "L", "repetition", "S028: a human radiologist",
     "high", None, None, 1, None, None, "LC", None),
    ("S029", "AI", "L", "repetition", "S028: artificial intelligence",
     "high", None, None, 1, None, None, "LC", None),
    ("S029", "the human reading", "L", "repetition", "S011: human readers",
     "high", None,
     "readers → reading (lặp hình vị read-); lần 2 'human' trong câu "
     "ghi note hàng 'a human'", 1, None, None, "LC", None),
    ("S029", "he", "R", "personal", "S028: Katalinic", "high", None,
     "occ 4 vì 'The/together/the' chứa 'he'; lần 4 mới là đại từ", 4,
     None, None, "LC", "A"),
    # S030
    ("S030", "Yang", "L", "repetition", "S027: Yang", "high", None, None,
     1, None, None, "LC", None),
    ("S030", "the study", "L", "repetition", "S001: A German study",
     "high", None, None, 1, None, None, "LC", None),
    ("S030", "the results", "L", "repetition", "S019: the study results",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] involved ← S010: mắt xích sót chuỗi involved (H&H §6.2) —
    # lặp với đảo chủ thể (AI tham gia ↔ Yang KHÔNG tham gia); VI "tham
    # gia" đối xứng.
    ("S030", "involved", "L", "repetition",
     "S010: When AI was involved", "med", None,
     "lặp involved (was not involved in the study); H&H §6.2", 1, None,
     None, "LC", None),
    # S031
    # [Phase-2] +alt "R: the" (mapping §3.6; protocol nhóm 8): "The data"
    # = the + đổi tên (results → data) — phần quy chiếu của mạo từ ghi vào
    # alt; VI "Dữ liệu" không có mạo từ — the ↔ zero (NTT 2020 §2.2).
    ("S031", "The data", "L", "synonym", "S030: the results", "high",
     "R: the", "data ≈ results (đồng nghĩa, đổi tên); H&H §6.2; VI "
     "'Dữ liệu' định danh bằng ngữ cảnh (mapping §4)", 1, None,
     None, "LC", None),
    ("S031", "she", "R", "personal", "S030: Yang", "high", None, None, 1,
     None, None, "LC", "A"),
    # S032
    ("S032", "The increased cancer detection rate", "L", "repetition",
     "S010: the breast cancer detection rate", "high", None,
     "'increased' lặp S026; 'this' trong câu chỉ danh sách, không đánh",
     1, None, None, "LC", None),
    ("S032", "the reduction", "L", "repetition",
     "S015: helped reduce the number of false positive results", "high",
     None, "reduce → reduction", 1, None, None, "LC", None),
    ("S032", "false positive", "L", "repetition",
     "S015: false positive results", "high", None, "'callbacks' từ mới",
     1, None, None, "LC", None),
    # [Phase-2] workforce ← radiologists: danh từ tổng quát (H&H §6.1;
    # mapping §3.6; protocol nhóm 8) — "the workforce" tổng quát hóa các
    # radiologists S024–S027; mạo từ the → alt "R: the"; VI "lực lượng
    # lao động" đối xứng.
    ("S032", "workforce", "L", "general word",
     "S026: could energize radiologists", "med", "R: the",
     "danh từ tổng quát chỉ lực lượng radiologists (H&H §6.1); mapping "
     "§3.6", 1, None, None, "LC", None),
    # S033
    ("S033", "So", "C", "causal",
     "S032: enumeration of benefits (rate, reduction, workforce)", "high",
     None,
     "'positive' không cùng trường với 'false positive' (đồng âm khác "
     "nghĩa), không đánh", 1, None, None, "LC", None),
]

TT = [
    # S002
    ("S002", "nghiên cứu này", "R", "demonstrative",
     "S001: Một nghiên cứu của Đức", "high", None,
     "hậu chỉ từ 'này'; đồng thời lặp 'nghiên cứu'; EN đối ứng chỉ là L "
     "'the study' — dịch chuyển", 1, None, None, "LC", "A"),
    ("S002", "trí tuệ nhân tạo", "L", "repetition",
     "S001: trí tuệ nhân tạo AI", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] bác sĩ ← S001: mắt xích sót chuỗi bác sĩ (H&H §6.2; TNT
    # §26) — occ 2: lần 1 nằm trong 'các bác sĩ X quang' (chuỗi X quang),
    # lần 2 trong apposition 'những bác sĩ phân tích…' mới là mắt xích này.
    ("S002", "bác sĩ", "L", "repetition",
     "S001: khi bác sĩ nhận được sự trợ giúp", "high", None,
     "lặp bác sĩ (apposition 'những bác sĩ phân tích' = bác sĩ của "
     "S001); H&H §6.2; TNT §26", 2, None, None, "LC", None),
    # S003
    ("S003", "cách này", "R", "demonstrative",
     "S002: cách dùng AI kiểm tra nhũ ảnh", "high", None,
     "VI tự sinh chỉ từ; EN không có đối ứng", 1, None, None, "LC", "A"),
    ("S003", "AI", "L", "repetition", "S001: trí tuệ nhân tạo AI",
     "high", None, None, 1, None, None, "LC", None),
    ("S003", "con người", "L", "collocation",
     "S001: trí tuệ nhân tạo AI", "med", None,
     "trường nghĩa đối lập con người↔AI; EN 'They' được VI hiện thực hóa "
     "thành 'Các nhà nghiên cứu' nên không có R VI", 1, None, None, "LC",
     None),
    # [Phase-2] phụ nữ ← S002: mắt xích sót chuỗi phụ nữ (H&H §6.2; protocol
    # nhóm 12 — chuỗi S002→S003→S007→S010 mới kín).
    ("S003", "phụ nữ", "L", "repetition",
     "S002: hơn 460.000 phụ nữ Đức", "high", None,
     "lặp phụ nữ (một ngàn phụ nữ); H&H §6.2; TNT §26", 1, None, None,
     "LC", None),
    # [Phase-2] ung thư ← S001: mắt xích được S004 "ung thư vú" cite làm
    # tiền trạm nhưng chưa có hàng (protocol nhóm 12) — hình vị ung thư lặp
    # trong 'tỷ lệ phát hiện ung thư' (H&H §6.2; TNT §26).
    ("S003", "ung thư", "L", "repetition",
     "S001: tỷ lệ phát hiện ung thư", "high", None,
     "lặp hình vị ung thư (một ca ung thư ← tỷ lệ phát hiện ung thư); "
     "H&H §6.2", 1, None, None, "LC", None),
    # [Phase-2] phát hiện ← S001: danh từ hóa ngược trong cụm (H&H §6.2;
    # TNT §26) — EN đối ứng S003 dùng 'found' (khác chuỗi detect).
    ("S003", "phát hiện", "L", "repetition",
     "S001: tỷ lệ phát hiện ung thư", "high", None,
     "lặp hình vị phát hiện (phát hiện thêm một ca ← tỷ lệ phát hiện); "
     "H&H §6.2", 1, None, None, "LC", None),
    # [Phase-2] hỗ trợ ← S001 trợ giúp: đồng nghĩa cùng hình vị 'trợ' (H&H
    # §6.2; TNT §26) — chuỗi giúp S001→S003→S009→S015→S024 mới kín.
    ("S003", "hỗ trợ", "L", "synonym",
     "S001: nhận được sự trợ giúp từ trí tuệ nhân tạo AI", "high",
     None,
     "hỗ trợ ≈ trợ giúp (không có AI hỗ trợ); lặp hình vị trợ; H&H "
     "§6.2; TNT §26", 1, None, None, "LC", None),
    # S004
    ("S004", "Đây", "R", "demonstrative", "S001: Một nghiên cứu",
     "high", None, "đối ứng EN 'It'", 1, None, None, "LC", "A"),
    ("S004", "AI", "L", "repetition", "S003: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S004", "ung thư vú", "L", "repetition", "S003: một ca ung thư",
     "high", None, "thêm 'vú' xác định; hình vị 'ung thư' lặp chuỗi", 1,
     None, None, "LC", None),
    # [Phase-2] việc sử dụng ← S002: mắt xích sót chuỗi sử dụng (H&H §6.2;
    # protocol nhóm 12 — S026 'việc sử dụng AI' cite S004 nên phải có hàng).
    ("S004", "việc sử dụng", "L", "repetition",
     "S002: đã sử dụng trí tuệ nhân tạo", "high", None,
     "lặp sử dụng (việc sử dụng AI ← đã sử dụng); TNT §26", 1, None,
     None, "LC", None),
    # [Phase-2] cuộc khám phá ← S001 nghiên cứu: đổi tên/tổng quát hóa
    # (mapping §3.6; protocol nhóm 8) — EN 'exploration' đối xứng; VI
    # không mạo từ, định danh bằng ngữ cảnh (mapping §4; NTT 2020 §2.2).
    ("S004", "cuộc khám phá", "L", "synonym",
     "S001: Một nghiên cứu của Đức", "med", None,
     "cuộc khám phá ≈ nghiên cứu (đổi tên theo mapping §3.6); H&H §6.2",
     1, None, None, "LC", None),
    # [Phase-2] phát hiện ← S003: mắt xích chuỗi phát hiện (H&H §6.2;
    # tiền trạm = nhắc gần nhất).
    ("S004", "phát hiện", "L", "repetition",
     "S003: phát hiện thêm một ca ung thư", "high", None,
     "lặp phát hiện (để phát hiện ung thư vú); H&H §6.2", 1, None, None,
     "LC", None),
    # S005
    ("S005", "Tỷ lệ phát hiện ung thư vú", "L", "repetition",
     "S001: tỷ lệ phát hiện ung thư", "high", None,
     "'đây' trong câu chỉ vế đầu, không đánh", 1, None, None, "LC", None),
    # [Phase-2] note cập nhật: 'nhà nghiên cứu' thuộc chuỗi researcher,
    # có hàng riêng ← S003; hàng này chỉ tính 'của nghiên cứu'.
    ("S005", "của nghiên cứu", "L", "repetition",
     "S002: nghiên cứu này", "high", None,
     "'nhà nghiên cứu' là chuỗi researcher — có hàng riêng [Phase-2] ← "
     "S003; hàng này chỉ tính 'của nghiên cứu' (chuỗi nghiên cứu, lần "
     "2 trong câu)", 1, None, None, "LC", None),
    ("S005", "Đức", "L", "repetition", "S002: phụ nữ Đức", "high", None,
     "chuỗi Đức", 1, None, None, "LC", None),
    # [Phase-2] tốt hơn ← S001: quy chiếu so sánh (H&H §2.5; protocol nhóm
    # 1) — 'tốt hơn' so với mức không AI đã lập ở S001; EN 'better' đối
    # xứng; tie R so sánh đầu tiên của cặp.
    ("S005", "tốt hơn", "R", "comparative",
     "S001: tỷ lệ phát hiện ung thư được cải thiện gần 18%", "med",
     None,
     "H&H §2.5 quy chiếu so sánh: tốt hơn = better so với mức cơ bản "
     "S001", 1, None, None, "LC", "A"),
    # [Phase-2] nhà nghiên cứu ← S003: mắt xích sót chuỗi nhà nghiên cứu
    # (H&H §6.2; TNT §26) — Phase-1 note gọi là 'từ mới', thực ra lặp S003;
    # EN đối ứng investigator ↔ researchers (đồng nghĩa).
    ("S005", "nhà nghiên cứu", "L", "repetition",
     "S003: Các nhà nghiên cứu cho biết", "high", None,
     "lặp nhà nghiên cứu (nhà nghiên cứu chính ← Các nhà nghiên cứu); "
     "H&H §6.2; TNT §26", 1, None, None, "LC", None),
    # S006
    ("S006", "Và", "C", "additive",
     "S005: tỷ lệ phát hiện tốt hơn (quote Katalinic)", "high", None,
     "nối liên câu trong quote", 1, None, None, "LC", None),
    ("S006", "bằng chứng này", "R", "demonstrative",
     "S005: tỷ lệ phát hiện ung thư vú tốt hơn", "high", None,
     "chỉ từ hồi quy; đồng thời lặp 'bằng chứng', ghi note", 1, None,
     None, "LC", "A"),
    ("S006", "AI", "L", "repetition", "S004: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S006", "ung thư vú", "L", "repetition", "S004: ung thư vú",
     "high", None,
     "'sàng lọc' khởi tạo chuỗi; 'chúng ta' hư chỉ, 'điều này' trong "
     "câu — không đánh", 1, None, None, "LC", None),
    # [Phase-2] sử dụng ← S004: mắt xích chuỗi sử dụng trong quote (H&H
    # §6.2; tiền trạm = nhắc gần nhất).
    ("S006", "sử dụng", "L", "repetition",
     "S004: việc sử dụng AI", "high", None,
     "lặp sử dụng (bắt đầu sử dụng nhiều AI hơn); TNT §26", 1, None,
     None, "LC", None),
    # S007
    ("S007", "nhũ ảnh", "L", "repetition", "S002: ảnh chụp nhũ ảnh",
     "high", None, "463.094 là số liệu, không phải tie", 1, None, None,
     "LC", None),
    ("S007", "phụ nữ Đức", "L", "repetition",
     "S002: hơn 460.000 phụ nữ Đức", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] kiểm tra ← S002: mắt xích sót chuỗi kiểm tra nhũ ảnh (H&H
    # §6.2; TNT §26) — bị động hóa nhưng cùng hình vị.
    ("S007", "kiểm tra", "L", "repetition",
     "S002: để kiểm tra ảnh chụp nhũ ảnh", "high", None,
     "lặp kiểm tra (đã được kiểm tra ← để kiểm tra); H&H §6.2", 1, None,
     None, "LC", None),
    # S008
    ("S008", "một nửa", "R", "nominal",
     "S007: Chụp nhũ ảnh của 463.094 phụ nữ Đức", "high", None,
     "quy chiếu lượng", 1, None, None, "LC", "A"),
    ("S008", "bác sĩ X quang", "L", "repetition",
     "S002: các bác sĩ X quang", "high", None, None, 1, None, None,
     "LC", None),
    ("S008", "chuẩn", "L", "repetition", "S006: tiêu chuẩn", "med", None,
     "lặp hình vị 'chuẩn', khác phát ngôn; 'đây là quy trình chuẩn' "
     "trong câu — đối ứng EN 'which' trong câu, không đánh", 1, None,
     None, "LC", None),
    ("S008", "Đức", "L", "repetition", "S007: phụ nữ Đức", "high", None,
     None, 1, None, None, "LC", None),
    # S009
    # [Phase-2] note cập nhật: 'trường hợp' có hàng riêng (L general word
    # theo nhóm 3); EN 'the cases' reclassify R→L tương ứng.
    ("S009", "một nửa", "L", "repetition", "S008: Khoảng một nửa",
     "high", None,
     "'hơn' đối với 'khoảng'; 'trường hợp' có hàng riêng [Phase-2] (L "
     "general word theo nhóm 3; EN 'the cases' reclassify R→L)", 1,
     None, None, "LC", None),
    ("S009", "con người", "L", "repetition", "S003: con người", "high",
     None, None, 1, None, None, "LC", None),
    ("S009", "AI", "L", "repetition", "S006: AI", "high", None, None, 1,
     None, None, "LC", None),
    # [Phase-2] hỗ trợ ← S003: mắt xích chuỗi giúp (H&H §6.2) — được AI
    # hỗ trợ ≈ AI hỗ trợ (S003); EN 'assisted' đồng nghĩa help.
    ("S009", "hỗ trợ", "L", "synonym",
     "S003: mà không có AI hỗ trợ", "high", None,
     "hỗ trợ lặp chuỗi trợ giúp (được AI hỗ trợ); H&H §6.2", 1, None,
     None, "LC", None),
    # [Phase-2] trường hợp ← S007: danh từ tổng quát/bridging (H&H §6.1;
    # protocol nhóm 3 — VI 'trường hợp' trỏ về các lần chụp nhũ ảnh);
    # Phase-1 ghi 'không có tín hiệu quy chiếu — chỉ ghi nhận', Phase-2
    # xếp L general word theo nhóm 3; EN 'the cases' reclassify tương ứng.
    ("S009", "trường hợp", "L", "general word",
     "S007: Chụp nhũ ảnh của 463.094 phụ nữ Đức", "med", None,
     "danh từ tổng quát (H&H §6.1): mỗi lần chụp nhũ ảnh = một trường "
     "hợp; VI định danh bằng ngữ cảnh (mapping §4)", 1, None, None,
     "LC", None),
    # S010
    ("S010", "AI", "L", "repetition", "S009: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S010", "tỷ lệ phát hiện ung thư vú", "L", "repetition",
     "S005: Tỷ lệ phát hiện ung thư vú", "high", None, None, 1, None,
     None, "LC", None),
    ("S010", "sàng lọc", "L", "repetition",
     "S006: việc sàng lọc ung thư vú", "high", None, None, 1, None,
     None, "LC", None),
    ("S010", "con người", "L", "repetition", "S009: con người", "high",
     None, None, 1, None, None, "LC", None),
    ("S010", "phụ nữ", "L", "repetition", "S007: phụ nữ Đức", "high",
     None,
     "occ 1: lặp 2 lần trong câu (6,7 vs 5,7 trên 1.000 phụ nữ), chọn "
     "lần 1; 'so với' so sánh rút gọn trong câu, không đánh E", 1, None,
     None, "LC", None),
    # S011
    ("S011", "AI", "L", "repetition", "S010: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S011", "Katalinic", "L", "repetition",
     "S005: Tiến sĩ Alexander Katalinic", "high", None,
     "'người đọc' từ mới thuần, không có hàng như EN 'human readers'", 1,
     None, None, "LC", None),
    # S012
    ("S012", "Nhưng", "C", "adversative",
     "S011: AI phù hợp thay thế ở mức độ nhất định", "high", None,
     "'bạn' hư chỉ, không đánh", 1, None, None, "LC", None),
    # S013
    ("S013", "Đây", "R", "demonstrative",
     "S012: bạn muốn đi xa đến đâu?", "high", None,
     "đối ứng EN 'This'; 'không chỉ…mà còn' trong câu, không đánh", 1,
     None, None, "LC", "A"),
    ("S013", None, "E", "nominal", "S013: Đây (trong câu)", "high", None,
     "[TC] tỉnh lược chủ ngữ vế tọa hợp, hồi phục {Đây}; EN dùng đại từ "
     "'it's' nên không có E phía EN", 1, "mà còn", "{Đây}", "TC", None),
    # S014
    ("S014", "xã hội", "L", "repetition", "S013: vấn đề xã hội",
     "high", None, None, 1, None, None, "LC", None),
    ("S014", "AI", "L", "repetition", "S011: AI", "high", None, None, 1,
     None, None, "LC", None),
    # S015
    ("S015", "Nghiên cứu", "L", "repetition", "S005: của nghiên cứu",
     "high", None, None, 1, None, None, "LC", None),
    ("S015", "AI", "L", "repetition", "S014: AI", "high", None,
     "'cũng' trong câu, không đánh C", 1, None, None, "LC", None),
    ("S015", "giúp", "L", "repetition", "S001: sự trợ giúp", "high",
     None, "chuỗi trợ giúp/giúp; 'dương tính giả' khởi tạo chuỗi", 1,
     None, None, "LC", None),
    # [Phase-2] phát hiện ← S004: mắt xích sót chuỗi phát hiện (H&H §6.2;
    # protocol nhóm 12 — chuỗi S003→S004→S015→S018 mới kín).
    ("S015", "phát hiện", "L", "repetition",
     "S004: để phát hiện ung thư vú", "high", None,
     "lặp phát hiện (Nghiên cứu phát hiện ra rằng); H&H §6.2", 1, None,
     None, "LC", None),
    # S016
    ("S016", "Tuy nhiên", "C", "adversative",
     "S015: AI cũng giúp giảm dương tính giả", "high", None, None, 1,
     None, None, "LC", None),
    ("S016", "trí tuệ nhân tạo", "L", "repetition",
     "S002: trí tuệ nhân tạo", "high", None,
     "viết đầy đủ sau chuỗi viết tắt", 1, None, None, "LC", None),
    ("S016", "ung thư", "L", "repetition",
     "S010: tỷ lệ phát hiện ung thư vú", "high", None,
     "'bệnh' thêm so với chuỗi", 1, None, None, "LC", None),
    # [Phase-2] bỏ sót ↔ phát hiện (S003): phép đối liên câu (TNT §30;
    # H&H §6.4 opposites) — S019 'bỏ sót' cite mắt xích này (protocol
    # nhóm 12); EN 'miss' đối xứng.
    ("S016", "bỏ sót", "L", "antonym",
     "S003: phát hiện thêm một ca ung thư", "high", None,
     "phép đối phát hiện ↔ bỏ sót (AI bỏ sót một số bệnh ung thư); TNT "
     "§30; H&H §6.4", 1, None, None, "LC", None),
    # S017
    ("S017", "AI", "L", "repetition", "S016: trí tuệ nhân tạo", "high",
     None, "'không hoàn hảo' lặp 2 lần trong câu (TC), không đánh thêm",
     1, None, None, "LC", None),
    ("S017", "con người", "L", "repetition", "S010: con người", "high",
     None, None, 1, None, None, "LC", None),
    ("S017", "trí tuệ nhân tạo", "L", "repetition",
     "S016: trí tuệ nhân tạo", "high", None,
     "lần 2 của chuỗi AI trong câu, dạng đầy đủ — đánh riêng (khác "
     "token với 'AI')", 1, None, None, "LC", None),
    ("S017", "nghiên cứu", "L", "repetition", "S015: Nghiên cứu",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] được sử dụng ← S006: mắt xích sót chuỗi sử dụng (H&H §6.2)
    # — participle bị động; chuỗi S002→S004→S006→S017→S026 kín; EN 'used'
    # đối xứng.
    ("S017", "được sử dụng", "L", "repetition",
     "S006: sử dụng nhiều AI hơn", "high", None,
     "lặp sử dụng (trí tuệ nhân tạo được sử dụng trong nghiên cứu); "
     "H&H §6.2", 1, None, None, "LC", None),
    # S018
    ("S018", "chúng tôi", "R", "personal",
     "nhóm nghiên cứu (ngoại văn bản — quote Bunk)", "med", None,
     "ngoại quy chiếu; đối ứng EN 'our'", 1, None, None, "LC", "E"),
    ("S018", "nghiên cứu", "L", "repetition", "S017: nghiên cứu",
     "high", None, None, 1, None, None, "LC", None),
    ("S018", "trường hợp", "L", "repetition", "S009: số trường hợp",
     "high", None,
     "occ 1: lần 2 ('trường hợp này') là chỉ từ trong câu, không đánh",
     1, None, None, "LC", None),
    ("S018", "AI", "L", "repetition", "S017: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S018", "bác sĩ X quang", "L", "repetition", "S008: bác sĩ X quang",
     "high", None, None, 1, None, None, "LC", None),
    ("S018", "phát hiện ra ung thư", "L", "repetition",
     "S003: phát hiện thêm một ca ung thư", "high", None,
     "lặp tổ hợp phát hiện + ung thư", 1, None, None, "LC", None),
    # S019
    ("S019", "Tuy nhiên", "C", "adversative",
     "S018: AI nói bình thường nhưng bác sĩ phát hiện ung thư", "high",
     None, None, 1, None, None, "LC", None),
    ("S019", "con người", "L", "repetition", "S017: con người", "high",
     None, None, 1, None, None, "LC", None),
    ("S019", "bỏ sót", "L", "repetition",
     "S016: bỏ sót một số bệnh ung thư", "high", None, "chuỗi bỏ sót", 1,
     None, None, "LC", None),
    ("S019", "khối u ác tính", "L", "synonym",
     "S018: phát hiện ra ung thư", "high", None,
     "khối u ác tính ≈ ung thư (đồng nghĩa)", 1, None, None, "LC", None),
    ("S019", "AI", "L", "repetition", "S018: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S019", "kết quả nghiên cứu", "L", "repetition",
     "S018: nghiên cứu", "high", None,
     "'nghiên cứu' lặp chuỗi; 'kết quả' khởi tạo chuỗi kết quả", 1,
     None, None, "LC", None),
    # S020
    ("S020", "AI", "L", "repetition", "S019: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S020", "con người", "L", "repetition", "S019: con người", "high",
     None, "'Không giống như' so sánh trong câu, không đánh", 1, None,
     None, "LC", None),
    # S021
    ("S021", "Bunk", "L", "repetition", "S017: Stefan Bunk", "high",
     None, "VI thêm danh xưng 'ông'", 1, None, None, "LC", None),
    # S022
    ("S022", "AI", "L", "repetition", "S020: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S022", None, "E", "verbal", "S022: AI hoạt động (trong câu)",
     "high", None,
     "[TC] tỉnh lược mệnh đề sau 'như', hồi phục {AI hoạt động}; đối "
     "xứng EN 'like'", 1, "như", "{AI hoạt động}", "TC", None),
    # S023
    ("S023", "Vì vậy", "C", "causal",
     "S020–S022: AI không mệt, hoạt động ổn định mọi lúc", "high", None,
     None, 1, None, None, "LC", None),
    ("S023", "đây", "R", "demonstrative",
     "S020–S022: AI không biết mệt mỏi, hoạt động cùng một cách",
     "high", None, "đối ứng EN 'it'", 1, None, None, "LC", "A"),
    ("S023", "AI", "L", "repetition", "S022: AI", "high", None, None, 1,
     None, None, "LC", None),
    ("S023", "ung thư", "L", "repetition", "S019: khối u ác tính",
     "high", None, None, 1, None, None, "LC", None),
    ("S023", "con người", "L", "repetition", "S020: con người", "high",
     None, None, 1, None, None, "LC", None),
    ("S023", "bỏ sót", "L", "repetition", "S019: bỏ sót", "high", None,
     None, 1, None, None, "LC", None),
    ("S023", None, "E", "nominal", "S023: đây (trong câu)", "high",
     None,
     "[TC] tỉnh lược chủ ngữ vế tọa hợp, hồi phục {đây}; EN dùng "
     "'it's also'", 1, "và cũng", "{đây}", "TC", None),
    # S024
    ("S024", "Bunk", "L", "repetition", "S021: Bunk", "high", None,
     "'Theo' động từ chức năng, không đánh C", 1, None, None, "LC",
     None),
    ("S024", "AI", "L", "repetition", "S023: AI", "high", None,
     "occ 1: lần 2 trong câu ('phụ thuộc vào AI') cùng chuỗi, không "
     "đánh", 1, None, None, "LC", None),
    ("S024", "giúp giảm", "L", "repetition",
     "S015: giúp giảm số lượng kết quả dương tính giả", "high", None,
     "lặp tổ hợp; hàng gộp 2 chuỗi giúp + giảm; 'giúp họ' lần 2 trong "
     "câu không đánh", 1, None, None, "LC", None),
    ("S024", "bác sĩ X quang", "L", "repetition",
     "S018: bác sĩ X quang", "high", None,
     "'họ' trong câu = bác sĩ X quang, không đánh", 1, None, None,
     "LC", None),
    ("S024", "trường hợp", "L", "repetition", "S018: trường hợp",
     "high", None, "'phức tạp' khởi tạo chuỗi", 1, None, None, "LC",
     None),
    ("S024", "con người", "L", "repetition", "S023: con người", "high",
     None, "trong 'chuyên môn của con người'", 1, None, None, "LC",
     None),
    # [Phase-2] nguy cơ ↔ lợi thế (S023): phép đối liên câu (TNT §30; H&H
    # §6.4) — Bunk nêu lợi thế (S023) rồi bổ sung nguy cơ (S024); EN
    # 'risk' đối xứng.
    ("S024", "nguy cơ", "L", "antonym",
     "S023: một lợi thế", "med", None,
     "phép đối lợi thế ↔ nguy cơ (nguy cơ mất đi chuyên môn); TNT §30; "
     "H&H §6.4", 1, None, None, "LC", None),
    # S025
    ("S025", "Những trường hợp phức tạp đó", "R", "demonstrative",
     "S024: các trường hợp phức tạp hơn", "high", None,
     "hậu chỉ từ 'đó' + lặp 'trường hợp phức tạp', một hàng duy nhất; "
     "'bạn' hư chỉ", 1, None, None, "LC", "A"),
    ("S025", "chuyên môn", "L", "repetition",
     "S024: chuyên môn của con người", "high", None, None, 1, None,
     None, "LC", None),
    ("S025", "bác sĩ X quang", "L", "repetition",
     "S024: bác sĩ X quang", "high", None,
     "'được đào tạo' khởi tạo chuỗi", 1, None, None, "LC", None),
    ("S025", "Bunk", "L", "repetition", "S024: Bunk", "high", None,
     None, 1, None, None, "LC", None),
    # S026
    # [Phase-2] note cập nhật: 'X quang' có hàng riêng ← S025 (ngay mặt
    # dưới).
    ("S026", "vú", "L", "repetition", "S010: tỷ lệ phát hiện ung thư vú",
     "high", None,
     "trong 'X quang vú'; 'X quang' có hàng riêng [Phase-2] ← S025; "
     "'Trung tâm Ung thư MD Anderson' là tên riêng, không tính tie", 1,
     None, None, "LC", None),
    ("S026", "việc sử dụng AI", "L", "repetition",
     "S004: việc sử dụng AI", "high", None, "lặp cụm", 1, None, None,
     "LC", None),
    ("S026", "bác sĩ X quang", "L", "repetition",
     "S025: bác sĩ X quang", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] X quang ← S025 bác sĩ X quang: lặp hình vị X quang (H&H
    # §6.2; TNT §26) — 'giáo sư về X quang vú' là trường nghề của bác sĩ
    # X quang; occ 1 trong 'giáo sư về X quang vú' (occ 2 nằm trong hàng
    # 'bác sĩ X quang' cuối câu); EN 'radiology' đối xứng.
    ("S026", "X quang", "L", "repetition",
     "S025: một bác sĩ X quang thực thụ", "high", None,
     "lặp hình vị X quang (X quang vú); H&H §6.2; TNT §26", 1, None,
     None, "LC", None),
    # S027
    ("S027", "AI", "L", "repetition", "S026: việc sử dụng AI", "high",
     None, None, 1, None, None, "LC", None),
    ("S027", "chúng ta", "R", "personal",
     "S026: giới bác sĩ X quang (nghề của Yang)", "med", None,
     "hư chỉ gắn nghề; 'lĩnh vực của mình' trong câu cùng chuỗi, không "
     "đánh", 1, None, None, "LC", "A"),
    ("S027", "bác sĩ X quang", "L", "repetition",
     "S026: bác sĩ X quang", "high", None,
     "'được đào tạo bài bản' lặp chuỗi đào tạo S025", 1, None, None,
     "LC", None),
    ("S027", "đào tạo", "L", "repetition", "S025: được đào tạo",
     "high", None, None, 1, None, None, "LC", None),
    ("S027", "phức tạp", "L", "repetition",
     "S025: trường hợp phức tạp", "high", None,
     "'nhiệm vụ' thay 'trường hợp' — cùng trường phức tạp", 1, None,
     None, "LC", None),
    ("S027", "tập trung vào", "L", "repetition",
     "S024: tập trung vào các trường hợp phức tạp hơn", "high", None,
     "'sự tập trung' lần 1 trong câu là danh từ mới, không đánh", 1,
     None, None, "LC", None),
    ("S027", "Yang", "L", "repetition", "S026: Tiến sĩ Wei Yang",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] hứng thú ← S026 tiếp thêm sinh lực: liên tưởng (TNT §32;
    # H&H §6.4 collocation) — narration 'tiếp thêm sinh lực' được quote
    # cụ thể hóa thành 'hứng thú'; EN cặp energize↔excited chặt hơn
    # (đồng nghĩa H&H §6.2).
    ("S027", "hứng thú", "L", "collocation",
     "S026: tiếp thêm sinh lực cho các bác sĩ X quang", "med", None,
     "liên tưởng sinh lực ↔ hứng thú (trở nên hứng thú hơn); TNT §32; "
     "H&H §6.4", 1, None, None, "LC", None),
    # S028
    ("S028", "bác sĩ X quang", "L", "repetition",
     "S027: bác sĩ X quang", "high", None,
     "'việc sử dụng' đổi đối tượng nên không tính chuỗi 'sử dụng'", 1,
     None, None, "LC", None),
    ("S028", "trí tuệ nhân tạo", "L", "repetition",
     "S017: trí tuệ nhân tạo", "high", None, "dạng đầy đủ", 1, None,
     None, "LC", None),
    ("S028", "Katalinic", "L", "repetition", "S011: Katalinic",
     "high", None, None, 1, None, None, "LC", None),
    # S029
    ("S029", "con người", "L", "repetition", "S024: con người", "high",
     None,
     "occ 1: lần 2 trong câu ('của con người') cùng chuỗi, không đánh; "
     "EN 'The combination' có hàng R nhưng VI 'Sự kết hợp' hiện thực "
     "hóa trần", 1, None, None, "LC", None),
    ("S029", "AI", "L", "repetition", "S028: trí tuệ nhân tạo", "high",
     None, None, 1, None, None, "LC", None),
    ("S029", "kết quả đọc", "L", "repetition", "S011: người đọc",
     "high", None,
     "'đọc' lặp 'người đọc'; đối ứng EN 'the human reading' ← 'human "
     "readers'", 1, None, None, "LC", None),
    ("S029", "ông", "R", "personal", "S028: ông Katalinic", "high",
     None, None, 1, None, None, "LC", "A"),
    # S030
    ("S030", "Yang", "L", "repetition", "S027: Yang", "high", None,
     None, 1, None, None, "LC", None),
    ("S030", "nghiên cứu", "L", "repetition",
     "S019: kết quả nghiên cứu", "high", None, None, 1, None, None,
     "LC", None),
    ("S030", "kết quả", "L", "repetition", "S019: kết quả nghiên cứu",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] tham gia ← S010: mắt xích sót chuỗi tham gia (H&H §6.2) —
    # lặp với đảo chủ thể (AI tham gia ↔ Yang KHÔNG tham gia); EN
    # 'involved' đối xứng.
    ("S030", "tham gia", "L", "repetition",
     "S010: Khi AI tham gia", "med", None,
     "lặp tham gia (người không tham gia vào nghiên cứu); H&H §6.2", 1,
     None, None, "LC", None),
    # S031
    ("S031", "Dữ liệu", "L", "synonym", "S030: kết quả", "high", None,
     "Dữ liệu ≈ kết quả (đồng nghĩa)", 1, None, None, "LC", None),
    ("S031", "bà", "R", "personal", "S030: Bà Yang", "high", None,
     None, 1, None, None, "LC", "A"),
    # S032
    ("S032", "Tỷ lệ phát hiện ung thư", "L", "repetition",
     "S010: tỷ lệ phát hiện ung thư vú", "high", None, None, 1, None,
     None, "LC", None),
    ("S032", "giảm", "L", "repetition",
     "S015: giúp giảm số lượng kết quả dương tính giả", "high", None,
     None, 1, None, None, "LC", None),
    ("S032", "dương tính sai", "L", "repetition",
     "S015: dương tính giả", "high", None,
     "nguồn VI đổi 'giả'→'sai', ghi §8; 'điều này' và 'nhìn chung' "
     "trong câu (sau gộp S033), không đánh", 1, None, None, "LC",
     None),
    # [Phase-2] lực lượng lao động ← bác sĩ X quang: danh từ tổng quát
    # (H&H §6.1; mapping §3.6; protocol nhóm 8) — tổng quát hóa các bác sĩ
    # X quang S024–S027; EN 'the workforce' có alt 'R: the', VI định danh
    # bằng ngữ cảnh (mapping §4; NTT 2020 §2.2).
    ("S032", "lực lượng lao động", "L", "general word",
     "S026: các bác sĩ X quang", "med", None,
     "danh từ tổng quát chỉ lực lượng bác sĩ X quang (H&H §6.1); "
     "mapping §3.6", 1, None, None, "LC", None),
    # [Phase-2] tăng lên ↔ giảm (S015): phép đối liên câu tăng–giảm (TNT
    # §30; H&H §6.4; protocol nhóm 2) — hai hiệu ứng đối lập của nghiên
    # cứu; EN 'increased' nằm trong span hàng cũ (S032 ST) nên không thêm
    # hàng EN; đọc khác có thể xem 'tăng lên' ≈ 'cải thiện' (S001) — chọn
    # phép đối vì cặp tăng–giảm là ví dụ chuẩn của nhóm 2.
    ("S032", "tăng lên", "L", "antonym",
     "S015: giúp giảm số lượng kết quả dương tính giả", "med", None,
     "phép đối tăng ↔ giảm (tỷ lệ tăng lên ↔ dương tính giả giảm); "
     "TNT §30; H&H §6.4", 1, None, None, "LC", None),
]
