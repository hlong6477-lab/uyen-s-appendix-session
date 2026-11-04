# P38 tie table — WRITTEN BY HAND FROM work/analysis/P38_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Cặp VOA→VOA Tiếng Việt (WHO salt): 25 câu ↔ 25 câu, 1–1 sạch, subhead S013 không tie.
# EN tách 2 chuỗi sodium/salt; VI hội tụ 1 chuỗi "muối". EN "They" (S020) ↔ VI "Các giới
# hạn này" (L). "he said" EN ↔ "Ông nói" VI (danh xưng trần làm đại từ).
# occ ghi tường minh mọi dòng; "he" EN có va chạm substring trong "the/these/heart".

ST = [
    # S002
    ("S002", "But", "C", "adversative",
     "S001: Sodium is essential for the smooth functioning of muscles and nerves",
     "high", None,
     "[LC] nối tương phản: natri cần thiết (S001) nhưng quá nhiều thì chết",
     1, None, None, "LC", None),
    ("S002", "sodium", "L", "repetition", "S001: Sodium", "high", None,
     "[LC] chuỗi sodium mở bài; 'too much' là thông tin mới",
     1, None, None, "LC", None),
    # S003
    ("S003", "sodium", "L", "repetition", "S002: too much sodium", "high",
     None,
     "[LC] excessive sodium intake; 'excessive' diễn đạt lại 'too much' (S002)",
     1, None, None, "LC", None),
    # S004
    ("S004", "he", "R", "personal", "S003: Tedros Adhanom Ghebreyesus",
     "high", None,
     "[LC] đại từ chủ ngữ của attribution 'he said', tiền trạm Tedros ở S003; "
     "occ=2 vì 'he' còn gặp trong 'the'; VI dùng danh xưng 'Ông'",
     2, None, None, "LC", "A"),
    ("S004", "Too much sodium", "L", "repetition", "S002: too much sodium",
     "high", None, "[LC] echo nguyên văn cụm của S002",
     1, None, None, "LC", None),
    # S005
    ("S005", "And yet", "C", "adversative",
     "S004: Too much sodium can lead to high blood pressure and increase the risk",
     "high", None,
     "[LC] nối tương phản trong quote Tedros; VI tách 'Tuy nhiên' ra ngoài quote",
     1, None, None, "LC", None),
    ("S005", "sodium intake", "L", "repetition",
     "S003: excessive sodium intake", "high", None,
     "[LC] average sodium intake — lặp cụm 'sodium intake'",
     1, None, None, "LC", None),
    ("S005", "WHO", "L", "repetition",
     "S003: the World Health Organization", "high", None,
     "[LC] lần viết tắt WHO đầu tiên thay tên đầy đủ",
     1, None, None, "LC", None),
    # S006
    ("S006", "That", "R", "demonstrative",
     "S005: less than 2,000 milligrams per day, or 5 grams of salt "
     "(khuyến nghị của WHO)", "high", None,
     "[LC] chỉ từ tóm lại mốc khuyến nghị Tedros đưa ở S005; VI là 'Lượng này'",
     1, None, None, "LC", "A"),
    ("S006", "salt", "L", "repetition", "S005: 5 grams of salt", "high",
     None,
     "[LC] one teaspoon of salt — chuỗi salt (tách khỏi chuỗi sodium của EN)",
     1, None, None, "LC", None),
    # S007
    ("S007", "WHO", "L", "repetition", "S005: the WHO recommendation",
     "high", None, "[LC] A WHO report", 1, None, None, "LC", None),
    ("S007", "sodium intake", "L", "repetition",
     "S005: average sodium intake", "high", None,
     "[LC] sodium intake reduction policies — lặp 'sodium intake', thêm "
     "'reduction policies'",
     1, None, None, "LC", None),
    # S008
    ("S008", "WHO", "L", "repetition", "S007: A WHO report", "high", None,
     "[LC] WHO's 194 member states", 1, None, None, "LC", None),
    ("S008", "global", "L", "repetition", "S005: And yet globally", "med",
     None,
     "[LC] its global target — cùng gốc global/world; conf med vì đổi loại từ "
     "(adv → adj)",
     1, None, None, "LC", None),
    ("S008", "sodium intake", "L", "repetition",
     "S007: sodium intake reduction policies", "high", None,
     "[LC] reducing sodium intake by 30%", 1, None, None, "LC", None),
    # S009
    ("S009", "The report", "L", "repetition", "S007: A WHO report", "high",
     None, "[LC] đặt lại tên 'report' sau lần đầu S007",
     1, None, None, "LC", None),
    ("S009", "WHO member states", "L", "repetition",
     "S008: WHO's 194 member states", "high", None,
     "[LC] gộp chuỗi WHO + member states trong một tie; lần 2 trong câu "
     "(73% of WHO member states) không đánh thêm",
     1, None, None, "LC", None),
    ("S009", "sodium reduction policies", "L", "repetition",
     "S007: sodium intake reduction policies", "high", None,
     "[LC] gần nguyên văn (bỏ 'intake'); 'such policies' trong câu là quy "
     "chiếu nội câu, không đánh",
     1, None, None, "LC", None),
    # [Phase-2] implementation ← implementing (S007): chuỗi động từ implement
    # bị sót (H&H §6.2 reiteration — danh từ hóa; TNT §26 phép lặp từ vựng);
    # VI đối ứng bằng biến thể đồng nghĩa "thi hành".
    ("S009", "implementation", "L", "repetition",
     "S007: in implementing sodium intake reduction policies", "high",
     None,
     "[LC] full range of implementation — lặp danh từ hóa của động từ "
     "implementing (S007)",
     1, None, None, "LC", None),
    # S010
    ("S010", "WHO", "L", "repetition", "S009: WHO member states", "high",
     None, "[LC] WHO's Department of Nutrition", 1, None, None, "LC", None),
    ("S010", "reducing sodium intake", "L", "repetition",
     "S008: reducing sodium intake", "high", None,
     "[LC] echo nguyên văn cụm của S008", 1, None, None, "LC", None),
    ("S010", "cardiovascular events", "L", "repetition",
     "S004: cardiovascular diseases", "high", None,
     "[LC] xoay diseases → events, giữ tính từ cardiovascular",
     1, None, None, "LC", None),
    ("S010", "deaths", "L", "repetition", "S003: Almost 2 million deaths",
     "high", None, "[LC] chuỗi tử vong; VI gộp kill/deaths nên VI có thêm "
     "1 tie ở S003",
     1, None, None, "LC", None),
    # S011
    ("S011", "Cardiovascular diseases", "L", "repetition",
     "S010: cardiovascular events", "high", None,
     "[LC] xoay lại diseases", 1, None, None, "LC", None),
    ("S011", "death", "L", "repetition", "S010: deaths", "high", None,
     "[LC] the leading cause of death", 1, None, None, "LC", None),
    ("S011", "globally", "L", "repetition", "S008: its global target", "med",
     None,
     "[LC] echo nguyên văn 'globally' của S005; lần nhắc gần nhất của chuỗi "
     "global là S008",
     1, None, None, "LC", None),
    # S012
    ("S012", "WHO", "L", "repetition", "S010: WHO's Department", "high",
     None, "[LC] WHO reports", 1, None, None, "LC", None),
    ("S012", "these deaths", "L", "repetition",
     "S011: the leading cause of death", "high", "R: these",
     "[LC] đầu ngữ 'deaths' lặp, chỉ từ 'these' thâu vào alt; chỉ 17,9 triệu "
     "sinh mạng của S011",
     1, None, None, "LC", None),
    ("S012", "heart attacks and strokes", "L", "collocation",
     "S011: Cardiovascular diseases", "med", None,
     "[LC] cụ thể hóa bệnh tim mạch thành hai bệnh (bridging nhẹ)",
     1, None, None, "LC", None),
    # S014
    ("S014", "The report", "L", "repetition", "S009: The report finds",
     "high", None, "[LC]", 1, None, None, "LC", None),
    ("S014", "countries", "L", "repetition", "S007: countries", "high",
     None,
     "[LC] nine countries — 'nine' là thông tin mới; 9 tên quốc gia lần đầu "
     "không đánh",
     1, None, None, "LC", None),
    ("S014", "WHO", "L", "repetition", "S012: WHO reports", "high", None,
     "[LC] WHO's recommended policies", 1, None, None, "LC", None),
    ("S014", "policies", "L", "repetition",
     "S009: sodium reduction policies", "high", None,
     "[LC] recommended policies", 1, None, None, "LC", None),
    # [Phase-2] recommended ← recommendation (S005): lặp hình vị recommend
    # (H&H §6.2; TNT §26) — quan hệ TỪ VỰNG (referent dịch chuyển: mức
    # 2.000 mg ↔ chính sách được khuyến nghị) nên conf med; VI lặp nguyên từ
    # "khuyến nghị".
    ("S014", "recommended", "L", "repetition",
     "S005: the WHO recommendation for adults", "med", None,
     "[LC] WHO's recommended policies — lặp gốc recommend của "
     "'recommendation' (S005); lexical cohesion không đòi hỏi đồng nhất "
     "referent (H&H §6.2)",
     1, None, None, "LC", None),
    ("S014", "reduce sodium intake", "L", "repetition",
     "S010: reducing sodium intake", "high", None,
     "[LC] lặp gần nguyên văn (reducing → reduce)",
     1, None, None, "LC", None),
    # S015
    ("S015", "Chile", "L", "repetition", "S014: Chile", "high", None,
     "[LC] cites Chile as a leader — nhắc lại tên trong danh sách 9 quốc gia",
     1, None, None, "LC", None),
    ("S015", "sodium-reduction policies", "L", "repetition",
     "S014: WHO's recommended policies to reduce sodium intake", "high",
     None,
     "[LC] gộp chuỗi sodium + policies thành tính từ ghép",
     1, None, None, "LC", None),
    # [Phase-2] implementation ← implementation (S009): mắt xích giữa của
    # chuỗi implement (H&H §6.2); tiền trạm = nhắc gần nhất S009.
    ("S015", "implementation", "L", "repetition",
     "S009: lack full range of implementation", "high", None,
     "[LC] the implementation of lifesaving sodium-reduction policies — "
     "chuỗi implement (S007 → S009 → S015)",
     1, None, None, "LC", None),
    # S016
    ("S016", None, "E", "nominal", "S016 (trong câu): Frieden said", "med",
     None,
     "[TC] chủ ngữ mệnh đề phân từ 'Speaking in a webinar...' trống; hồi "
     "phục {Frieden} (điều khiển trong câu)",
     1, "", "{Frieden}", "TC", None),
    ("S016", "report", "L", "repetition", "S014: The report", "high", None,
     "[LC] the report's launch", 1, None, None, "LC", None),
    # [Phase-2] launch ← launched (S007): danh từ hóa của động từ launch
    # (H&H §6.2 reiteration; TNT §26) — cùng sự kiện công bố phúc trình; VI
    # đối ứng "công bố" lặp nguyên văn.
    ("S016", "launch", "L", "repetition",
     "S007: A WHO report launched Thursday", "high", None,
     "[LC] the report's launch — danh từ hóa của 'launched' (S007)",
     1, None, None, "LC", None),
    ("S016", "Frieden", "L", "repetition", "S015: Tom Frieden", "high",
     None,
     "[LC] họ trong attribution (bỏ tên đệm Tom); S017 sẽ tiếp bằng đại từ He",
     1, None, None, "LC", None),
    ("S016", "Chile", "L", "repetition", "S015: Chile", "high", None,
     "[LC] Chile had passed the law", 1, None, None, "LC", None),
    # [Phase-2] passed ← enacted (S014): đồng nghĩa lập pháp enact ≈ pass
    # (TNT §31 phép thế đẳng nghĩa; H&H §6.2 synonym) — nối báo cáo 9 nước
    # ban hành chính sách (S014) với việc Chile thông qua luật (S016).
    ("S016", "passed", "L", "synonym",
     "S014: have fully enacted WHO's recommended policies", "med", None,
     "[LC] passed the law ≈ enacted (S014); mắt xích mới của chuỗi enact/pass "
     "(S014 → S016 → S017)",
     1, None, None, "LC", None),
    ("S016", "mandatory", "L", "repetition",
     "S009: mandatory and comprehensive sodium reduction policies", "high",
     None,
     "[LC] mandatory front-of pack warning labels",
     1, None, None, "LC", None),
    ("S016", "sodium", "L", "repetition", "S015: sodium-reduction policies",
     "high", None,
     "[LC] including on sodium; 'those warning labels/those products' trong "
     "câu là quy chiếu nội câu, không đánh",
     1, None, None, "LC", None),
    # S017
    ("S017", "He", "R", "personal", "S016: Frieden", "high", None,
     "[LC] 'He noted' tiếp chuỗi Frieden; VI 'Ông lưu ý'",
     1, None, None, "LC", "A"),
    ("S017", "Brazil", "L", "repetition", "S014: Brazil", "high", None,
     "[LC] nhắc lại trong danh sách 9 quốc gia; Argentina lần đầu nên không "
     "đánh",
     1, None, None, "LC", None),
    ("S017", "Mexico", "L", "repetition", "S014: Mexico", "high", None,
     "[LC]", 1, None, None, "LC", None),
    ("S017", "Uruguay", "L", "repetition", "S014: Uruguay", "high", None,
     "[LC]", 1, None, None, "LC", None),
    ("S017", "passed", "L", "repetition", "S016: passed the law", "high",
     None,
     "[LC] động từ lập pháp lặp 'passed' (động từ nội dung, không phải "
     "động từ tường thuật)",
     1, None, None, "LC", None),
    # [Phase-2] similar (R so sánh, H&H §2.5 "similar"): chuẩn so sánh là bộ
    # chính sách Chile mô tả ở CÂU TRƯỚC (S016) → [LC] R, ref A — tie R so
    # sánh đầu tiên của cặp; VI "tương tự" trùng span hàng L nên thâu vào
    # alt "R: tương tự" (mapping §3.13 một hình thức một hàng).
    ("S017", "similar", "R", "comparative",
     "S016: Chile had passed the law of food labeling and advertising "
     "(bộ chính sách của Chile)", "med", None,
     "[LC] similar policies = chính sách TƯƠNG TỰ với bộ chính sách Chile "
     "đã mô tả ở S016; H&H §2.5 comparative; conf med vì 'Chile's lead' "
     "trong cùng câu cũng gợi chuẩn so sánh",
     1, None, None, "LC", "A"),
    ("S017", "policies", "L", "repetition",
     "S015: sodium-reduction policies", "high", None,
     "[LC] similar policies — 'similar' so với chính sách Chile (S016)",
     1, None, None, "LC", None),
    ("S017", "Chile", "L", "repetition", "S016: Chile", "high", None,
     "[LC] following Chile's lead", 1, None, None, "LC", None),
    # [Phase-2] lead (danh từ tổng quát, H&H §6.1): "Chile's lead" tóm cả
    # tình huống câu trước (Chile thông qua luật S016) — bridging; đọc phụ:
    # lặp gốc từ của "a leader" (S015).
    ("S017", "lead", "L", "general word",
     "S016: Chile had passed the law of food labeling and advertising",
     "med", None,
     "[LC] following Chile's lead — danh từ tổng quát tóm tình huống S016 "
     "(bridging H&H §6.1); đọc phụ: lặp gốc từ 'leader' (S015)",
     1, None, None, "LC", None),
    # S018
    ("S018", "Branca", "L", "repetition", "S010: Francesco Branca", "high",
     None,
     "[LC] họ trong attribution, bỏ tên đệm Francesco",
     1, None, None, "LC", None),
    ("S018", "sodium", "L", "repetition", "S016: including on sodium",
     "high", None,
     "[LC] a significant proportion of sodium", 1, None, None, "LC", None),
    ("S018", "the diet", "L", "repetition", "S002: in the diet", "high",
     None,
     "[LC] liên kết xa (16 câu): sodium in the diet",
     1, None, None, "LC", None),
    ("S018", "countries", "L", "repetition", "S014: nine countries", "high",
     None,
     "[LC] lần 1 trong câu (high-income countries); lần 2 (low- and "
     "middle-income countries) không đánh thêm",
     1, None, None, "LC", None),
    # [Phase-2] foods ← food labeling (S016): mắt xích chuỗi food được cite
    # làm tiền trạm ở hàng S019 (sodium-processed foods) nhưng chưa có hàng
    # (rà chuỗi ngược "ante không có hàng" — bài học P28); H&H §6.2.
    ("S018", "foods", "L", "repetition",
     "S016: the law of food labeling", "med", None,
     "[LC] processed and highly processed foods — nhánh mới của chuỗi food "
     "(food labeling S016 → foods S018 → sodium-processed foods S019); "
     "bổ sung hàng vì S019 cite S018 làm tiền trạm (P28)",
     1, None, None, "LC", None),
    # S019
    ("S019", "he", "R", "personal", "S018: Branca noted", "high", None,
     "[LC] 'he said' cuối quote Branca, tiền trạm S018; VI 'Ông nói'",
     1, None, None, "LC", "A"),
    ("S019", "mandatory", "L", "repetition",
     "S016: mandatory front-of pack warning labels", "high", None,
     "[LC] mandatory maximum limits", 1, None, None, "LC", None),
    ("S019", "sodium-processed foods", "L", "repetition",
     "S018: sodium ... processed and highly processed foods", "high", None,
     "[LC] gộp chuỗi sodium + processed foods thành tính từ ghép",
     1, None, None, "LC", None),
    # S020
    ("S020", "They", "R", "personal",
     "S019: Government-led mandatory maximum limits", "high", None,
     "[LC] đại từ [−người] chỉ 'limits' của S019; VI hiện thực hóa thành "
     "'Các giới hạn này' (L) — dịch chuyển R→L",
     1, None, None, "LC", "A"),
    # [Phase-2] restricts ← restricted (S016): chuỗi động từ restrict bị sót
    # (H&H §6.2 reiteration; TNT §26); VI đối ứng "hạn chế" lặp nguyên văn.
    ("S020", "restricts", "L", "repetition",
     "S016: restricted marketing of products", "high", None,
     "[LC] restricts the less healthy food options — lặp động từ restrict "
     "(restricted marketing S016)",
     1, None, None, "LC", None),
    ("S020", None, "E", "nominal", "S020 (trong câu): they (understand)",
     "med", None,
     "[TC] chủ ngữ vế tọa hợp thứ hai sau 'or' bị lược; hồi phục {they} "
     "(trong câu); song song phía VI 'hay ∅'",
     2, "or ", "{they}", "TC", None),
    ("S020", "labels", "L", "repetition", "S016: warning labels", "high",
     None,
     "[LC] information on labels", 1, None, None, "LC", None),
    ("S020", "food", "L", "repetition", "S019: sodium-processed foods",
     "med", None,
     "[LC] the less healthy food options — chuỗi food (phân nhánh từ "
     "'food labeling' S016)",
     1, None, None, "LC", None),
    # S021
    ("S021", "Frieden", "L", "repetition", "S016: Frieden said", "high",
     None,
     "[LC] tên trong attribution; S017 dùng đại từ He nên truy về nhắc tên "
     "gần nhất S016",
     1, None, None, "LC", None),
    ("S021", "food", "L", "repetition", "S020: food options", "high", None,
     "[LC] the food manufacturing industry", 1, None, None, "LC", None),
    ("S021", "industry", "L", "repetition", "S019: industrywide", "med",
     None,
     "[LC] lặp gốc 'industry' của 'industrywide'",
     1, None, None, "LC", None),
    # [Phase-2] ineffective ↔ cost-effective (S010): phép đối qua câu
    # effective ↔ ineffective (TNT §30 phép đối; H&H §6.4 opposites) — giảm
    # muối hiệu quả về chi phí (S010) đối lập tự điều chỉnh vô hiệu (S021).
    ("S021", "ineffective", "L", "antonym",
     "S010: one of the most cost-effective ways to improve health", "med",
     None,
     "[LC] phép đối effective ↔ ineffective (cost-effective S010 ↔ "
     "ineffective S021); conf med vì cách xa 11 câu",
     1, None, None, "LC", None),
    ("S021", "voluntary", "L", "antonym",
     "S019: mandatory maximum limits", "med", None,
     "[LC] phép đối: voluntary đối lập mandatory (chuỗi thuộc tính chính sách)",
     1, None, None, "LC", None),
    ("S021", "policies", "L", "repetition", "S017: similar policies",
     "high", None, "[LC] voluntary policies", 1, None, None, "LC", None),
    # S022 — [Phase-2] điều chỉnh sub: adversative → continuative theo
    # H&H §5.8 (chuẩn đã đồng bộ P21/P22/P24/P28): "In fact" mở lượt nói
    # củng cố lập luận (discourse organizer), không phải nối tương phản
    # mệnh đề trong thế giới.
    ("S022", "In fact", "C", "continuative",
     "S021: voluntary policies are often ignored", "high", None,
     "[LC] continuative (H&H §5.8): mở lượt củng cố lập luận chống chính "
     "sách tự nguyện (S021); trước Phase-2 ghi adversative — điều chỉnh "
     "theo chuẩn P21/P22/P24/P28; 'because' trong câu không đánh",
     1, None, None, "LC", None),
    ("S022", "mandatory", "L", "repetition",
     "S019: mandatory maximum limits", "high", None,
     "[LC] a mandatory approach — đối lập 'voluntary' của S021 (phép đối)",
     1, None, None, "LC", None),
    # S023
    ("S023", "In addition to", "C", "additive",
     "S022: a mandatory approach (bối cảnh các chiến lược hiện có)",
     "high", None,
     "[LC] nối bổ sung: ngoài các chiến lược đã bàn S016-S022",
     1, None, None, "LC", None),
    # [Phase-2] proven ← proven (S021): lặp phân từ prove (H&H §6.2) — echo
    # tương phản "proven ineffective" (S021) ↔ "proven strategies" (S023);
    # VI lược tính từ này (dịch chuyển EN lặp → VI lược, NTT 2020 §5).
    ("S023", "proven", "L", "repetition",
     "S021: has repeatedly proven to be ineffective", "med", None,
     "[LC] the existing proven strategies — lặp 'proven' (S021) với cực "
     "tính đảo (vô hiệu ↔ hiệu quả); VI không lặp ('các chiến lược hiện có')",
     1, None, None, "LC", None),
    ("S023", "reduce sodium", "L", "repetition",
     "S014: to reduce sodium intake", "high", None,
     "[LC] echo nguyên văn 'reduce sodium intake' (bỏ 'intake')",
     1, None, None, "LC", None),
    ("S023", "salt", "L", "repetition", "S006: one teaspoon of salt",
     "high", None,
     "[LC] salt substitutes — chuỗi salt thưa: S005→S006→S023; lần 'sodium' "
     "thứ 2 trong câu (sodium and salt substitutes) không đánh thêm",
     1, None, None, "LC", None),
    ("S023", "Frieden", "L", "repetition", "S021: Frieden said", "high",
     None, "[LC]", 1, None, None, "LC", None),
    ("S023", "countries", "L", "repetition",
     "S018: low- and middle-income countries", "high", None,
     "[LC]", 1, None, None, "LC", None),
    # S024
    ("S024", "these substitutes", "L", "repetition",
     "S023: sodium and salt substitutes", "high", "R: these",
     "[LC] đầu ngữ 'substitutes' lặp, chỉ từ 'these' thâu vào alt",
     1, None, None, "LC", None),
    ("S024", "blood pressure", "L", "repetition",
     "S004: high blood pressure", "high", None,
     "[LC] liên kết xa (20 câu)", 1, None, None, "LC", None),
    ("S024", "heart attack and strokes", "L", "repetition",
     "S012: heart attacks and strokes", "high", None,
     "[LC] heart attack đổi sang số ít", 1, None, None, "LC", None),
    ("S024", "death", "L", "repetition", "S012: these deaths", "high", None,
     "[LC] death from cardiovascular events", 1, None, None, "LC", None),
    ("S024", "cardiovascular events", "L", "repetition",
     "S011: Cardiovascular diseases", "high", None,
     "[LC] xoay lại 'events' (trùng cụm của S010)",
     1, None, None, "LC", None),
    ("S024", "he", "R", "personal", "S023: Frieden said", "high", None,
     "[LC] 'he said' cuối quote, tiếp chuỗi Frieden; VI 'Ông nói'; occ=3 vì "
     "'he' còn gặp trong 'these' và 'heart'",
     3, None, None, "LC", "A"),
    # S025
    ("S025", "salt", "L", "repetition", "S023: salt substitutes", "high",
     None,
     "[LC] the brand of salt — chuỗi salt chốt bài",
     1, None, None, "LC", None),
    ("S025", "you", "R", "personal",
     "ngoài văn bản: bạn đọc/người tiêu dùng nói chung (không có tiền trạm "
     "trong văn bản)", "high", None,
     "[LC] đại từ 2 ngôi trong quote Frieden; attribution nằm ở S024 (câu "
     "trước) nên đủ điều kiện đánh; hướng độc giả",
     1, None, None, "LC", "E"),
    ("S025", "risk", "L", "repetition",
     "S004: the risk of cardiovascular diseases", "med", None,
     "[LC] the risk of death — liên kết xa (21 câu)",
     1, None, None, "LC", None),
    ("S025", "death", "L", "repetition",
     "S024: death from cardiovascular events", "high", None,
     "[LC]", 1, None, None, "LC", None),
]

TT = [
    # S002
    ("S002", "Nhưng", "C", "adversative",
     "S001: Muối cần thiết cho hoạt động trơn tru", "high", None,
     "[LC] nối tương phản, song song EN 'But'",
     1, None, None, "LC", None),
    ("S002", "muối", "L", "repetition", "S001: Muối", "high", None,
     "[LC] chuỗi muối mở bài; EN tách sodium/salt, VI chỉ có một chuỗi muối",
     1, None, None, "LC", None),
    # S003
    ("S003", "tử vong", "L", "repetition", "S002: gây tử vong", "high",
     None,
     "[LC] 2 triệu ca tử vong — VI gộp kill/deaths EN vào một từ nên có "
     "thêm tie này (EN 'deaths' S003 là lần đầu)",
     1, None, None, "LC", None),
    ("S003", "quá nhiều muối", "L", "repetition",
     "S002: quá nhiều muối", "high", None,
     "[LC] ăn quá nhiều muối — lặp nguyên văn cụm trong quote Tedros",
     1, None, None, "LC", None),
    # S004
    ("S004", "Ông", "R", "personal",
     "S003: Ông Tedros Adhanom Ghebreyesus", "high", None,
     "[LC] danh xưng trần 'Ông' làm đại từ chủ ngữ 'Ông nói' (EN dùng 'he'); "
     "chữ Ông viết hoa phân biệt với 'ông + tên'",
     1, None, None, "LC", "A"),
    ("S004", "Quá nhiều muối", "L", "repetition",
     "S003: ăn quá nhiều muối", "high", None,
     "[LC] lặp nguyên văn cụm (viết hoa đầu quote)",
     1, None, None, "LC", None),
    # S005
    ("S005", "Tuy nhiên", "C", "adversative",
     "S004: Quá nhiều muối có thể dẫn đến huyết áp cao và tăng nguy cơ",
     "high", None,
     "[LC] EN 'And yet' nằm trong quote, VI tách 'Tuy nhiên' ra ngoài (VI "
     "không mở lại dấu quote — xem §8)",
     1, None, None, "LC", None),
    ("S005", "muối", "L", "repetition", "S004: Quá nhiều muối", "high",
     None,
     "[LC] lần 1 trong câu (lượng muối trung bình); lần 2 ('5 g muối') "
     "không đánh thêm",
     1, None, None, "LC", None),
    ("S005", "WHO", "L", "repetition", "S003: Tổ chức Y tế Thế giới",
     "high", None,
     "[LC] lần viết tắt WHO đầu tiên thay tên đầy đủ (song song EN)",
     1, None, None, "LC", None),
    # S006
    ("S006", "Lượng này", "R", "demonstrative",
     "S005: dưới 2.000 mg mỗi ngày, hoặc 5 g muối (khuyến nghị của WHO)",
     "high", None,
     "[LC] chỉ từ + danh từ tổng quát tóm lại mốc khuyến nghị (EN chỉ từ "
     "đơn 'That')",
     1, None, None, "LC", "A"),
    ("S006", "muối", "L", "repetition",
     "S005: lượng muối trung bình / 5 g muối", "high", None,
     "[LC] một muỗng cà phê muối", 1, None, None, "LC", None),
    # S007
    ("S007", "WHO", "L", "repetition", "S005: khuyến nghị của WHO", "high",
     None,
     "[LC] Một phúc trình của WHO", 1, None, None, "LC", None),
    ("S007", "lượng muối", "L", "repetition",
     "S005: lượng muối trung bình", "high", None,
     "[LC] các chính sách giảm lượng muối — tái lập cụm 'lượng muối', thêm "
     "chuỗi 'giảm'",
     1, None, None, "LC", None),
    # S008
    ("S008", "WHO", "L", "repetition", "S007: Một phúc trình của WHO",
     "high", None,
     "[LC] 194 quốc gia thành viên của WHO", 1, None, None, "LC", None),
    ("S008", "quốc gia thành viên", "L", "repetition",
     "S007: các quốc gia", "high", None,
     "[LC] thêm 'thành viên' (member states là thông tin mới); VI chồng "
     "chuỗi 'quốc gia' nên có tie, EN 'member states' S008 là lần đầu",
     1, None, None, "LC", None),
    ("S008", "toàn cầu", "L", "repetition", "S005: trên toàn cầu", "med",
     None,
     "[LC] mục tiêu toàn cầu; 'thế giới' trong câu cùng chuỗi, không đánh "
     "thêm",
     1, None, None, "LC", None),
    ("S008", "lượng muối", "L", "repetition", "S007: giảm lượng muối",
     "high", None,
     "[LC] lượng muối tiêu thụ ('tiêu thụ' = intake; S005 VI dùng 'hấp thụ')",
     1, None, None, "LC", None),
    # S009
    ("S009", "Phúc trình", "L", "repetition",
     "S007: Một phúc trình của WHO", "high", None,
     "[LC]", 1, None, None, "LC", None),
    ("S009", "các quốc gia thành viên", "L", "repetition",
     "S008: 194 quốc gia thành viên", "high", None,
     "[LC] lần 1 trong câu (5%); lần 2 (73%) không đánh thêm",
     1, None, None, "LC", None),
    ("S009", "WHO", "L", "repetition", "S008: quốc gia thành viên của WHO",
     "high", None,
     "[LC] lần 1 trong câu; lần 2 không đánh thêm",
     1, None, None, "LC", None),
    ("S009", "các chính sách giảm muối", "L", "repetition",
     "S007: các chính sách giảm lượng muối", "high", None,
     "[LC] gộp chuỗi chính sách + muối trong một tie; 'các chính sách đó' "
     "trong câu là quy chiếu nội câu, không đánh",
     1, None, None, "LC", None),
    # [Phase-2] thi hành ← thực hiện (S007): mắt xích chuỗi implement bằng biến
    # thể đồng nghĩa (TNT §31 phép thế đẳng nghĩa; H&H §6.2) — EN lặp nguyên
    # từ "implementation" còn VI đổi từ (dịch chuyển NTT 2020 §5).
    ("S009", "thi hành", "L", "synonym",
     "S007: trong việc thực hiện các chính sách giảm lượng muối", "med",
     None,
     "[LC] thiếu thi hành đầy đủ — đồng nghĩa với 'thực hiện' (S007); "
     "chuỗi thực hiện (S007) → thi hành (S009) → thực hiện (S015)",
     1, None, None, "LC", None),
    # S010
    ("S010", "WHO", "L", "repetition",
     "S009: các quốc gia thành viên của WHO", "high", None,
     "[LC] Ban Dinh dưỡng vì Sức khỏe và Phát triển của WHO",
     1, None, None, "LC", None),
    ("S010", "giảm ăn muối", "L", "repetition",
     "S009: các chính sách giảm muối", "high", None,
     "[LC] chuỗi giảm + muối; VI lược cụm 'at very low program costs' (xem §8)",
     1, None, None, "LC", None),
    ("S010", "bệnh tim mạch", "L", "repetition",
     "S004: các bệnh tim mạch", "high", None,
     "[LC] các ca bệnh tim mạch", 1, None, None, "LC", None),
    ("S010", "tử vong", "L", "repetition", "S003: 2 triệu ca tử vong",
     "high", None,
     "[LC] chuỗi tử vong quay lại sau S003",
     1, None, None, "LC", None),
    # S011
    ("S011", "Các bệnh tim mạch", "L", "repetition",
     "S010: các ca bệnh tim mạch", "high", None,
     "[LC]", 1, None, None, "LC", None),
    ("S011", "tử vong", "L", "repetition",
     "S010: bệnh tim mạch và tử vong", "high", None,
     "[LC] nguyên nhân gây tử vong hàng đầu", 1, None, None, "LC", None),
    ("S011", "trên toàn cầu", "L", "repetition",
     "S008: mục tiêu toàn cầu", "med", None,
     "[LC] echo nguyên văn 'trên toàn cầu' của S005; lần nhắc gần nhất của "
     "chuỗi toàn cầu là S008",
     1, None, None, "LC", None),
    # S012
    ("S012", "WHO", "L", "repetition", "S010: của WHO", "high", None,
     "[LC] WHO báo cáo", 1, None, None, "LC", None),
    ("S012", "ca tử vong", "L", "repetition",
     "S011: nguyên nhân gây tử vong", "high", "R: này",
     "[LC] đầu ngữ lặp, chỉ từ 'này' thâu vào alt; 'năm ca tử vong này' chỉ "
     "17,9 triệu ca của S011; VI tái cấu trúc 'four out of five'",
     1, None, None, "LC", None),
    ("S012", "đau tim và đột quỵ", "L", "collocation",
     "S011: Các bệnh tim mạch", "med", None,
     "[LC] cụ thể hóa bệnh tim mạch thành hai bệnh (bridging nhẹ)",
     1, None, None, "LC", None),
    # S014
    ("S014", "Phúc trình", "L", "repetition", "S009: Phúc trình", "high",
     None, "[LC]", 1, None, None, "LC", None),
    ("S014", "quốc gia", "L", "repetition",
     "S009: các quốc gia thành viên", "high", None,
     "[LC] 9 quốc gia; 9 tên riêng lần đầu không đánh",
     1, None, None, "LC", None),
    ("S014", "WHO", "L", "repetition", "S012: WHO báo cáo", "high", None,
     "[LC] chính sách khuyến nghị của WHO", 1, None, None, "LC", None),
    ("S014", "chính sách", "L", "repetition",
     "S009: các chính sách giảm muối", "high", None,
     "[LC] các chính sách khuyến nghị", 1, None, None, "LC", None),
    # [Phase-2] khuyến nghị ← khuyến nghị (S005): lặp nguyên từ (TNT §26 phép
    # lặp từ vựng; H&H §6.2) — quan hệ TỪ VỰNG, referent dịch chuyển (mức
    # 2.000 mg ↔ chính sách được khuyến nghị); đối xứng EN "recommended".
    ("S014", "khuyến nghị", "L", "repetition",
     "S005: khuyến nghị của WHO đối với người lớn", "med", None,
     "[LC] các chính sách khuyến nghị của WHO — lặp 'khuyến nghị' (S005); "
     "lexical cohesion không đòi hỏi đồng nhất referent (H&H §6.2)",
     1, None, None, "LC", None),
    ("S014", "giảm lượng muối", "L", "repetition",
     "S007: giảm lượng muối", "high", None,
     "[LC] tái lập cụm nguyên văn của S007 (S010 VI dùng 'giảm ăn muối')",
     1, None, None, "LC", None),
    # S015
    ("S015", "Chile", "L", "repetition", "S014: Chile", "high", None,
     "[LC] Chile là quốc gia đi đầu", 1, None, None, "LC", None),
    ("S015", "quốc gia", "L", "repetition", "S014: 9 quốc gia", "med",
     None,
     "[LC] VI tự sinh danh từ tổng quát 'quốc gia' (EN chỉ có 'a leader')",
     1, None, None, "LC", None),
    ("S015", "các chính sách giảm muối", "L", "repetition",
     "S014: các chính sách khuyến nghị của WHO để giảm lượng muối", "high",
     None,
     "[LC] gộp chuỗi chính sách + muối; EN là 'sodium-reduction policies'",
     1, None, None, "LC", None),
    # [Phase-2] thực hiện ← thi hành (S009): mắt xích giữa của chuỗi thực
    # hiện/thi hành (TNT §26; tiền trạm = nhắc gần nhất S009); 'thực hiện'
    # ở S022 (các bước tích cực) là động từ đa dụng, ngoài chuỗi (xem §6).
    ("S015", "thực hiện", "L", "repetition",
     "S009: thiếu thi hành đầy đủ (≈ thực hiện S007)", "high", None,
     "[LC] trong việc thực hiện các chính sách giảm muối cứu sinh — chuỗi "
     "thực hiện (S007) → thi hành (S009) → thực hiện (S015)",
     1, None, None, "LC", None),
    # S016
    ("S016", None, "E", "nominal", "S016 (trong câu): ông Frieden nói",
     "med", None,
     "[TC] chủ ngữ mệnh đề 'Phát biểu trong một hội thảo trực tuyến...' "
     "trống; hồi phục {ông Frieden} (điều khiển trong câu); song song E-EN "
     "'Speaking'",
     1, "", "{ông Frieden}", "TC", None),
    ("S016", "phúc trình", "L", "repetition", "S014: Phúc trình", "high",
     None,
     "[LC] sau khi phúc trình được công bố", 1, None, None, "LC", None),
    # [Phase-2] công bố ← công bố (S007): lặp nguyên văn (TNT §26 phép lặp
    # từ vựng); đối xứng EN launch ← launched (EN danh từ hóa, VI giữ nguyên
    # dạng động từ).
    ("S016", "công bố", "L", "repetition",
     "S007: Một phúc trình của WHO được công bố hôm 9/3", "high", None,
     "[LC] sau khi phúc trình được công bố — lặp 'công bố' (S007)",
     1, None, None, "LC", None),
    ("S016", "Frieden", "L", "repetition", "S015: Ông Tom Frieden", "high",
     None,
     "[LC] họ trong attribution (bỏ tên đệm Tom); S017 sẽ tiếp bằng 'Ông'",
     1, None, None, "LC", None),
    ("S016", "Chile", "L", "repetition", "S015: Chile", "high", None,
     "[LC] Chile đã thông qua luật", 1, None, None, "LC", None),
    # [Phase-2] thông qua ← ban hành (S014): đồng nghĩa lập pháp (TNT §31
    # phép thế đẳng nghĩa); đối xứng EN passed ← enacted (S014).
    ("S016", "thông qua", "L", "synonym",
     "S014: đã ban hành đầy đủ các chính sách khuyến nghị", "med", None,
     "[LC] Chile đã thông qua luật ≈ ban hành (S014); mắt xích mới của "
     "chuỗi ban hành/thông qua (S014 → S016 → S017)",
     1, None, None, "LC", None),
    ("S016", "bắt buộc", "L", "repetition",
     "S009: các chính sách giảm muối bắt buộc", "high", None,
     "[LC] nhãn cảnh báo bắt buộc", 1, None, None, "LC", None),
    ("S016", "muối", "L", "repetition", "S015: các chính sách giảm muối",
     "high", None,
     "[LC] trước bao bì về muối (EN 'including on sodium'); 'nhãn cảnh báo "
     "đó / những sản phẩm đó' trong câu không đánh",
     1, None, None, "LC", None),
    # S017
    ("S017", "Ông", "R", "personal", "S016: ông Frieden nói", "high",
     None,
     "[LC] danh xưng trần làm đại từ, tiếp chuỗi Frieden; EN 'He noted'",
     1, None, None, "LC", "A"),
    ("S017", "Brazil", "L", "repetition", "S014: Brazil", "high", None,
     "[LC] nhắc lại trong danh sách 9 quốc gia; Argentina lần đầu nên "
     "không đánh",
     1, None, None, "LC", None),
    ("S017", "Mexico", "L", "repetition", "S014: Mexico", "high", None,
     "[LC]", 1, None, None, "LC", None),
    ("S017", "Uruguay", "L", "repetition", "S014: Uruguay", "high", None,
     "[LC]", 1, None, None, "LC", None),
    ("S017", "thông qua", "L", "repetition",
     "S016: thông qua luật dán nhãn", "high", None,
     "[LC] động từ lập pháp lặp (động từ nội dung)",
     1, None, None, "LC", None),
    # [Phase-2] thêm alt "R: tương tự": "tương tự" là quy chiếu so sánh
    # (H&H §2.5) chỉ bộ chính sách Chile (S016) nhưng nằm trùng span hàng L
    # nên thâu vào alt (mapping §3.13 một hình thức một hàng) — đối xứng EN
    # có hàng R "similar" riêng (tránh chồng marker).
    ("S017", "các chính sách tương tự", "L", "repetition",
     "S015: các chính sách giảm muối", "high", "R: tương tự",
     "[LC] 'tương tự' so sánh với chính sách Chile (S016) — H&H §2.5 "
     "comparative; thâu vào alt vì trùng span",
     1, None, None, "LC", None),
    ("S017", "Chile", "L", "repetition", "S016: Chile", "high", None,
     "[LC] sau khi Chile dẫn đầu", 1, None, None, "LC", None),
    # [Phase-2] dẫn đầu ← đi đầu (S015): đồng nghĩa (TNT §31 phép thế đẳng
    # nghĩa) — đối ứng EN dùng danh từ tổng quát "lead" (H&H §6.1): dịch
    # chuyển loại từ EN danh từ ↔ VI động từ (NTT 2020 §5).
    ("S017", "dẫn đầu", "L", "synonym",
     "S015: Chile là quốc gia đi đầu", "med", None,
     "[LC] sau khi Chile dẫn đầu — đồng nghĩa với 'đi đầu' (S015); EN "
     "'Chile's lead' là danh từ tổng quát",
     1, None, None, "LC", None),
    # S018
    ("S018", "Branca", "L", "repetition", "S010: Ông Francesco Branca",
     "high", None,
     "[LC] họ trong attribution, bỏ tên đệm Francesco",
     1, None, None, "LC", None),
    ("S018", "muối", "L", "repetition", "S016: về muối", "high", None,
     "[LC] một tỷ lệ muối đáng kể", 1, None, None, "LC", None),
    ("S018", "chế độ ăn uống", "L", "repetition",
     "S002: trong chế độ ăn uống", "high", None,
     "[LC] liên kết xa (16 câu)", 1, None, None, "LC", None),
    ("S018", "nước", "L", "superordinate", "S015: quốc gia đi đầu",
     "med", None,
     "[LC] danh từ tổng quát 'nước' thay 'quốc gia'; lần 1 trong câu, lần 2 "
     "(các nước thu nhập thấp) không đánh thêm",
     1, None, None, "LC", None),
    # [Phase-2] thực phẩm ← thực phẩm (S016): mắt xích chuỗi thực phẩm được
    # cite làm tiền trạm ở hàng S019 nhưng chưa có hàng (rà chuỗi ngược
    # "ante không có hàng" — bài học P28); TNT §26 phép lặp từ vựng.
    ("S018", "thực phẩm", "L", "repetition",
     "S016: luật dán nhãn và quảng cáo thực phẩm", "med", None,
     "[LC] thực phẩm chế biến và chế biến cao — nhánh mới của chuỗi thực "
     "phẩm (S016 → S018 → S019); bổ sung hàng vì S019 cite S018 làm tiền "
     "trạm (P28)",
     1, None, None, "LC", None),
    # S019
    ("S019", "Ông", "R", "personal", "S018: Ông Branca lưu ý", "high",
     None,
     "[LC] 'Ông nói' đầu quote Branca (EN 'he said' cuối quote)",
     1, None, None, "LC", "A"),
    ("S019", "bắt buộc", "L", "repetition",
     "S016: nhãn cảnh báo bắt buộc", "high", None,
     "[LC] các giới hạn tối đa bắt buộc", 1, None, None, "LC", None),
    ("S019", "thực phẩm chế biến bằng muối", "L", "repetition",
     "S018: một tỷ lệ muối ... thực phẩm chế biến và chế biến cao", "high",
     None,
     "[LC] gộp chuỗi thực phẩm + muối; EN là 'sodium-processed foods'",
     1, None, None, "LC", None),
    # S020
    ("S020", "Các giới hạn này", "L", "repetition",
     "S019: Các giới hạn tối đa bắt buộc", "high", "R: này",
     "[LC] đầu ngữ 'giới hạn' lặp + chỉ từ 'này' thâu vào alt; EN dùng đại "
     "từ 'They' (R) → dịch chuyển R→L",
     1, None, None, "LC", None),
    # [Phase-2] hạn chế ← hạn chế (S016): lặp nguyên văn động từ (TNT §26
    # phép lặp; H&H §6.2) — đối xứng EN restricts ← restricted (S016).
    ("S020", "hạn chế", "L", "repetition",
     "S016: hạn chế tiếp thị các sản phẩm", "high", None,
     "[LC] thị trường hạn chế các lựa chọn thực phẩm — lặp 'hạn chế' "
     "(hạn chế tiếp thị S016)",
     1, None, None, "LC", None),
    ("S020", None, "E", "nominal", "S020 (trong câu): họ (hiểu)", "med",
     None,
     "[TC] chủ ngữ vế tọa hợp thứ hai sau 'hay' bị lược; hồi phục {họ} "
     "(trong câu); song song E-EN 'or ∅'",
     1, "hay ", "{họ}", "TC", None),
    ("S020", "nhãn", "L", "repetition", "S016: nhãn cảnh báo bắt buộc",
     "high", None,
     "[LC] thông tin trên nhãn", 1, None, None, "LC", None),
    ("S020", "thực phẩm", "L", "repetition",
     "S019: thực phẩm chế biến bằng muối", "med", None,
     "[LC] các lựa chọn thực phẩm kém lành mạnh",
     1, None, None, "LC", None),
    # S021
    ("S021", "Frieden", "L", "repetition", "S016: ông Frieden nói",
     "high", None,
     "[LC] tên trong attribution; S017 dùng 'Ông' nên truy về nhắc tên gần "
     "nhất S016",
     1, None, None, "LC", None),
    ("S021", "ngành", "L", "repetition", "S019: trên toàn ngành", "med",
     None,
     "[LC] lặp gốc 'ngành' của 'toàn ngành'",
     1, None, None, "LC", None),
    ("S021", "thực phẩm", "L", "repetition",
     "S020: các lựa chọn thực phẩm", "high", None,
     "[LC] ngành sản xuất thực phẩm", 1, None, None, "LC", None),
    # [Phase-2] không hiệu quả ↔ hiệu quả (S010): phép đối qua câu (TNT §30
    # phép đối; H&H §6.4 opposites) — VI phủ định bằng 'không'; đối xứng EN
    # ineffective ↔ cost-effective.
    ("S021", "không hiệu quả", "L", "antonym",
     "S010: cách hiệu quả nhất về chi phí", "med", None,
     "[LC] phép đối hiệu quả ↔ không hiệu quả (S010 ↔ S021); cách xa 11 câu "
     "nên conf med",
     1, None, None, "LC", None),
    ("S021", "tự nguyện", "L", "antonym",
     "S019: Các giới hạn tối đa bắt buộc", "med", None,
     "[LC] phép đối: tự nguyện đối lập bắt buộc (chuỗi thuộc tính chính sách)",
     1, None, None, "LC", None),
    ("S021", "các chính sách", "L", "repetition",
     "S017: các chính sách tương tự", "high", None,
     "[LC] các chính sách tự nguyện", 1, None, None, "LC", None),
    # S022 — [Phase-2] điều chỉnh sub: adversative → continuative theo
    # H&H §5.8 (chuẩn đã đồng bộ P21/P22/P24/P28): "Trên thực tế" mở lượt
    # củng cố lập luận, không phải nối tương phản mệnh đề.
    ("S022", "Trên thực tế", "C", "continuative",
     "S021: các chính sách tự nguyện thường bị bỏ qua", "high", None,
     "[LC] continuative (H&H §5.8); trước Phase-2 ghi adversative — điều "
     "chỉnh theo chuẩn P21/P22/P24/P28; 'bởi vì' trong câu không đánh",
     1, None, None, "LC", None),
    ("S022", "bắt buộc", "L", "repetition",
     "S019: Các giới hạn tối đa bắt buộc", "high", None,
     "[LC] một cách tiếp cận bắt buộc — đối lập 'tự nguyện' S021 (phép đối)",
     1, None, None, "LC", None),
    # S023
    ("S023", "Frieden", "L", "repetition", "S021: Ông Frieden cho biết",
     "high", None, "[LC]", 1, None, None, "LC", None),
    ("S023", "ngoài", "C", "additive",
     "S022: một cách tiếp cận bắt buộc (bối cảnh các chiến lược hiện có)",
     "high", None,
     "[LC] nối bổ sung ngoài các chiến lược đã bàn; song song EN 'In "
     "addition to'",
     1, None, None, "LC", None),
    ("S023", "giảm muối", "L", "repetition",
     "S019: thực phẩm chế biến bằng muối", "high", None,
     "[LC] tái lập cụm 'giảm muối' đã dùng ở S009/S015; lần 'chất thay thế "
     "muối' trong câu không đánh thêm",
     1, None, None, "LC", None),
    ("S023", "các quốc gia", "L", "repetition",
     "S018: các nước thu nhập thấp và trung bình", "med", None,
     "[LC] nước (S018) → quốc gia; quay lại cách dùng của S014",
     1, None, None, "LC", None),
    # S024
    ("S024", "Ông", "R", "personal", "S023: Ông Frieden cho biết", "high",
     None,
     "[LC] 'Ông nói' đầu câu, tiếp chuỗi Frieden (EN 'he said' cuối quote)",
     1, None, None, "LC", "A"),
    ("S024", "những chất thay thế này", "L", "repetition",
     "S023: các chất thay thế muối", "high", "R: này",
     "[LC] đầu ngữ lặp, chỉ từ 'này' thâu vào alt; EN 'these substitutes'",
     1, None, None, "LC", None),
    ("S024", "huyết áp", "L", "repetition", "S004: huyết áp cao", "high",
     None,
     "[LC] liên kết xa (20 câu)", 1, None, None, "LC", None),
    ("S024", "đau tim và đột quỵ", "L", "repetition",
     "S012: đau tim và đột quỵ", "high", None,
     "[LC] lặp nguyên văn", 1, None, None, "LC", None),
    ("S024", "tử vong", "L", "repetition", "S012: năm ca tử vong",
     "high", None,
     "[LC] giảm tử vong do các biến cố tim mạch",
     1, None, None, "LC", None),
    ("S024", "biến cố tim mạch", "L", "repetition",
     "S011: Các bệnh tim mạch", "high", None,
     "[LC] bệnh → biến cố (events), giữ gốc 'tim mạch'",
     1, None, None, "LC", None),
    # S025
    ("S025", "muối", "L", "repetition",
     "S023: các chất thay thế muối", "high", None,
     "[LC] nhãn hiệu muối — chuỗi muối chốt bài (EN 'brand of salt' thuộc "
     "chuỗi salt riêng)",
     1, None, None, "LC", None),
    ("S025", "bạn", "R", "personal",
     "ngoài văn bản: bạn đọc/người tiêu dùng nói chung (không có tiền trạm "
     "trong văn bản)", "high", None,
     "[LC] đại từ 2 ngôi trong quote Frieden; attribution nằm ở S024 (câu "
     "trước) nên đủ điều kiện đánh; hướng độc giả",
     1, None, None, "LC", "E"),
    ("S025", "nguy cơ", "L", "repetition",
     "S004: tăng nguy cơ mắc các bệnh tim mạch", "med", None,
     "[LC] liên kết xa (21 câu)", 1, None, None, "LC", None),
    ("S025", "tử vong", "L", "repetition", "S024: giảm tử vong", "high",
     None,
     "[LC] nguy cơ tử vong", 1, None, None, "LC", None),
]
