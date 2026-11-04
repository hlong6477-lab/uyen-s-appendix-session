# P26 tie table — WRITTEN BY HAND FROM work/analysis/P26_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Text/gap_after là chuỗi con nguyên văn trong câu (kiểm bằng pipeline.locate).
# Quy ước cặp này:
# - S/E = 0/0 hai đầu: không có pro-form thế, không có ∅ thật (xem §2, §3 của analysis).
# - Quote có attribution cùng câu: we/you (EN S009) và bạn (VI S008) KHÔNG được
#   đánh dấu — liệt kê trong analysis §4.3.
# - occ ghi tường minh: "he" (EN S009) occ 2 và (EN S011) occ 4 vì "he" trùng
#   chuỗi con trong "then"/"the"; "jobs" (EN S019) occ 1/2; "kỹ năng" (VI S018) occ 1/2.
# - Hai khối cắt phía EN (S008 — mệnh đề "which..."; S020) đánh dấu ở EN, ghi chú
#   "không có bản dịch"; VI S013 là attribution tách câu (không ép đối ứng EN).
# - Từ khung "lĩnh vực" chỉ đánh 1 lần (VI S003); số năm (2025/2024) không là tie L.
# [Phase-2] Bổ sung theo PHASE2_PROTOCOL.md: 10 hàng mới EN / 5 hàng mới VI
# (nhóm 2 phép đối liên câu; nhóm 4 chuỗi lặp/danh hóa/đồng nghĩa sót; nhóm 9
# collocation quá trình–sản phẩm; nhóm 12 mắt xích "được cite làm tiền trạm
# nhưng chưa có hàng"). occ giữ tiền lệ cặp P26: đếm case-sensitive chuỗi con
# kể cả nằm trong từ khác, ghi chú vị trí — mọi hàng mới occ=1.

ST = [
    # S002 — Key Points 1: chỉ hiring lặp về S001
    ("S002", "hiring", "L", "repetition",
     "S001: fuel hiring in retail and hospitality", "high", None,
     "lặp hiring trong hiring boom; đối ứng VI tuyển dụng (S002)",
     1, None, None, "LC", None),
    # S003 — Key Points 2
    ("S003", "But", "C", "adversative",
     "S002: The job market is still stabilising following the post-COVID-19 "
     "pandemic hiring boom", "high", None,
     "đối lập: thị trường đang ổn định ↔ tuyển dụng chăm sóc không chậm lại; "
     "đối ứng VI Tuy nhiên", 1, None, None, "LC", None),
    ("S003", "hiring", "L", "repetition",
     "S002: post-COVID-19 pandemic hiring boom", "high", None, None,
     1, None, None, "LC", None),
    ("S003", "the care economy", "L", "repetition",
     "S001: Care economy and technology roles", "high", None,
     "lặp nguyên NP; VI đổi tên thành chăm sóc sức khoẻ và giữ trẻ "
     "(phân rã chuỗi)", 1, None, None, "LC", None),
    # S005
    ("S005", "you", "R", "personal",
     "độc giả/người tìm việc (ngoại văn bản — khung lời khuyên)", "high", None,
     "ngoại quy chiếu; nằm trong you're; không phải quote nên được đánh dấu; "
     "đối ứng VI bạn", 1, None, None, "LC", "E"),
    # [Phase-2] job ← job market (S002): mắt xích giữa bị sót của chuỗi việc
    # làm (H&H §6.2 reiteration; TNT §26 phép lặp từ vựng) — lặp hình vị job;
    # VI đối ứng việc làm (S005 TT) cũng được bổ sung vì S006 TT cite nó làm
    # tiền trạm (nhóm 12, bài học P28).
    ("S005", "job", "L", "repetition",
     "S002: The job market is still stabilising", "med", None,
     "lặp hình vị job (looking for a job) — chuỗi EN roles → job market → "
     "a job; đối ứng VI việc làm (S005 TT)", 1, None, None, "LC", None),
    ("S005", "retail", "L", "repetition",
     "S001: retail and hospitality", "high", None, None, 1, None, None,
     "LC", None),
    ("S005", "tech", "L", "repetition",
     "S001: technology roles", "high", None,
     "tech là dạng rút gọn của technology", 1, None, None, "LC", None),
    ("S005", "the care economy", "L", "repetition",
     "S003: the care economy", "high", None, None, 1, None, None, "LC", None),
    # S006
    ("S006", "economist", "L", "repetition",
     "S005: economists say", "med", None,
     "Chapman là hiện thân của economists nêu ở S005", 1, None, None,
     "LC", None),
    ("S006", "hopes", "L", "synonym",
     "S001: are expected to be in demand", "med", None,
     "hopes ≈ expected — chuỗi động từ dự báo; đối ứng VI kỳ vọng (S006)",
     1, None, None, "LC", None),
    ("S006", "hiring", "L", "repetition",
     "S003: hiring in the care economy", "high", None, "strong hiring",
     1, None, None, "LC", None),
    ("S006", "roles", "L", "repetition",
     "S001: technology roles", "med", None,
     "consumer-facing là thông tin mới", 1, None, None, "LC", None),
    # S007 — nửa đầu của câu bị tách dòng
    ("S007", "However", "C", "adversative",
     "S006: hopes to see strong hiring in consumer-facing roles", "high",
     None, "kỳ vọng mạnh ↔ phụ thuộc điều kiện; đối ứng VI Tuy nhiên",
     1, None, None, "LC", None),
    ("S007", "that", "R", "demonstrative",
     "S006: hopes to see strong hiring in consumer-facing roles", "high",
     None, "that = kỳ vọng tuyển dụng mạnh; đối ứng VI điều này",
     1, None, None, "LC", "A"),
    ("S007", "expected", "L", "repetition",
     "S001: are expected to be in demand", "med", None,
     "chuỗi động từ dự báo (widely expected)", 1, None, None, "LC", None),
    # S008 — KHỐI CẮT: không có bản dịch
    ("S008", "which", "R", "personal",
     "S007: widely expected rate cuts from the Reserve Bank of Australia",
     "high", None,
     "quan hệ từ truy hồi rate cuts — câu nguồn bị tách dòng nên tiền trạm ở "
     "S007; không có bản dịch", 1, None, None, "LC", "A"),
    ("S008", "anticipated", "L", "synonym",
     "S007: widely expected", "med", None,
     "anticipated ≈ expected; dòng không có bản dịch", 1, None, None,
     "LC", None),
    # S009 — quote Chapman; we/you không đánh (attribution "he said" cùng câu)
    ("S009", "those", "R", "demonstrative",
     "áp lực chi phí sinh hoạt ngoài văn bản (bối cảnh Úc; sát nghĩa "
     "sluggish spending ở S008)", "med", None,
     "ngoại quy chiếu, chỉ từ định ngữ; VI lược hẳn chỉ từ, giữ NP",
     1, None, None, "LC", "E"),
    # [Phase-2] ease ← ease (S008): chuỗi ease (H&H §6.2 reiteration; TNT
    # §26) — S008 thuộc khối cắt nên chuỗi không có đối ứng VI.
    ("S009", "ease", "L", "repetition",
     "S008: anticipated to ease employer concerns", "high", None,
     "lặp ease (continue to ease) — chuỗi ease (S008) → ease (S009) → "
     "easing (S011); dòng S008 không có bản dịch", 1, None, None, "LC",
     None),
    ("S009", "expect", "L", "synonym",
     "S008: anticipated", "med", None,
     "chuỗi dự báo expected→anticipated→expect", 1, None, None, "LC", None),
    ("S009", "rate cuts", "L", "repetition",
     "S007: widely expected rate cuts", "high", None,
     "interest là bổ sung (interest rate cuts)", 1, None, None, "LC", None),
    ("S009", "retail and hospitality", "L", "repetition",
     "S001: hiring in retail and hospitality", "high", None,
     "lặp nguyên cặp; đối ứng VI bán lẻ và nhà hàng khách sạn (S008)",
     1, None, None, "LC", None),
    ("S009", "demand", "L", "repetition",
     "S001: are expected to be in demand", "med", None, None, 1, None,
     None, "LC", None),
    # [Phase-2] pick up ↔ slow down (S003): phép đối liên câu (TNT §30; H&H
    # §6.4 opposites) — tăng ↔ giảm; VI không có hàng đối ứng ở S008 vì
    # "tăng mạnh" là lần đầu chuỗi tăng (phép đối VI giảm ↔ tăng nằm ở
    # S010 TT).
    ("S009", "pick up", "L", "antonym",
     "S003: is unlikely to slow down", "med", None,
     "phép đối pick up ↔ slow down — nhu cầu tăng đối lập nhịp chậm đã nêu "
     "ở S003", 1, None, None, "LC", None),
    ("S009", "he", "R", "personal",
     "S006: SEEK senior economist Blair Chapman", "high", None,
     "he said — truy hồi Chapman; occ 2 vì he gặp trước đó trong then; "
     "we/you trong quote không đánh (attribution cùng câu)",
     2, None, None, "LC", "A"),
    # S010 — echo nguyên văn Key Points S002
    # [Phase-2] expectations ← expect (S009): chuỗi động từ dự báo thêm mắt
    # xích danh hóa (H&H §6.2 reiteration — precedent P21 promised ←
    # promising; TNT §26); vế "Outlining his expectations..." bị VI lược.
    ("S010", "expectations", "L", "repetition",
     "S009: you can expect retail and hospitality demand", "high", None,
     "expect → expectations (danh hóa động từ) — chuỗi expected (S001, S007) "
     "→ anticipated (S008) → expect (S009) → expectations; VI lược cả vế",
     1, None, None, "LC", None),
    ("S010", "Chapman", "L", "repetition",
     "S006: Blair Chapman", "high", None,
     "họ lặp; his trong câu không đánh (tiền trạm cùng câu)",
     1, None, None, "LC", None),
    ("S010", "the job market", "L", "repetition",
     "S002: The job market", "high", None, "echo nguyên văn Key Points",
     1, None, None, "LC", None),
    ("S010", "still stabilising", "L", "repetition",
     "S002: is still stabilising", "high", None, "echo nguyên văn Key Points",
     1, None, None, "LC", None),
    ("S010", "post-COVID-19 pandemic hiring boom", "L", "repetition",
     "S002: post-COVID-19 pandemic hiring boom", "high", None,
     "echo nguyên văn Key Points; hiring trong span cũng nối chuỗi S006",
     1, None, None, "LC", None),
    # S011 — VI lược attribution he said nên chỉ còn tie L phía VI
    ("S011", "he", "R", "personal",
     "S010: Chapman said", "high", None,
     "he said; occ 4 vì he gặp 3 lần trong the trước đó; VI lược attribution",
     4, None, None, "LC", "A"),
    ("S011", "positions", "L", "synonym",
     "S006: consumer-facing roles", "med", None,
     "available là bổ sung; positions ≈ roles trong chuỗi việc làm",
     1, None, None, "LC", None),
    ("S011", "slowed", "L", "repetition",
     "S003: is unlikely to slow down", "med", None,
     "lặp hình vị slow", 1, None, None, "LC", None),
    ("S011", "normalising", "L", "synonym",
     "S010: still stabilising", "med", None,
     "normalising ≈ stabilising; VI bình thường (S010)", 1, None, None,
     "LC", None),
    ("S011", "demand", "L", "repetition",
     "S009: retail and hospitality demand", "high", None,
     "labour là bổ sung (labour demand)", 1, None, None, "LC", None),
    # [Phase-2] easing ← ease (S009): mắt xích cuối chuỗi ease (H&H §6.2;
    # TNT §26) — "labour demand easing from a very high base"; VI lược
    # (đổi thành trở lại mức bình thường).
    ("S011", "easing", "L", "repetition",
     "S009: continue to ease", "med", None,
     "lặp hình vị ease (easing) — tiền trạm = nhắc gần nhất S009; EN-only "
     "không có đối ứng VI", 1, None, None, "LC", None),
    # S012 — echo nguyên văn Key Points S003
    ("S012", "But", "C", "adversative",
     "S011: the number of advertisements ... slowed towards the end of 2024",
     "high", None,
     "đối lập quảng cáo giảm ↔ nhu cầu chăm sóc không chậm; đối ứng VI "
     "Tuy nhiên (S011)", 1, None, None, "LC", None),
    ("S012", "hiring", "L", "repetition",
     "S010: post-COVID-19 pandemic hiring boom", "high", None, None,
     1, None, None, "LC", None),
    ("S012", "the care economy", "L", "repetition",
     "S005: the care economy", "high", None,
     "echo nguyên văn S003 (Key Points)", 1, None, None, "LC", None),
    ("S012", "jobs", "L", "repetition",
     "S011: available positions", "med", None,
     "chuỗi việc làm jobs/roles/positions", 1, None, None, "LC", None),
    ("S012", "health care", "L", "repetition",
     "S003: jobs in health care and child care", "high", None,
     "echo nguyên văn Key Points", 1, None, None, "LC", None),
    ("S012", "child care", "L", "repetition",
     "S003: health care and child care", "high", None,
     "echo nguyên văn Key Points", 1, None, None, "LC", None),
    ("S012", "unlikely to slow down", "L", "repetition",
     "S003: is unlikely to slow down", "high", None,
     "echo nguyên văn Key Points; slow cũng nối slowed (S011); VI đổi thành "
     "khẳng định", 1, None, None, "LC", None),
    # S013 — quote Chapman
    ("S013", "That", "R", "demonstrative",
     "S012: hiring in the care economy ... unlikely to slow down", "high",
     None,
     "chỉ từ định ngữ tóm chỉ nhu cầu chăm sóc vừa nêu; VI bỏ chỉ từ, đặt lại "
     "bằng Những nhu cầu; that's x2 trong câu không đánh",
     1, None, None, "LC", "A"),
    ("S013", "demand", "L", "repetition",
     "S011: labour demand", "high", None, "ongoing là bổ sung",
     1, None, None, "LC", None),
    ("S013", "care workers", "L", "repetition",
     "S012: jobs in health care and child care", "med", None,
     "lặp hình vị care; workers nối chuỗi jobs (S012)", 1, None, None,
     "LC", None),
    # [Phase-2] drive ← fuel (S001): chuỗi động từ thúc đẩy (H&H §6.2
    # reiteration — synonym; TNT §31 phép thế đẳng nghĩa) — drive ≈ fuel;
    # VI đối ứng động lực (S012 TT) ← thúc đẩy (S001 TT, danh hóa).
    ("S013", "drive", "L", "synonym",
     "S001: tipped to fuel hiring in retail and hospitality", "med",
     None,
     "drive employment ← fuel hiring: động từ thúc đẩy; VI hiện thực hóa "
     "bằng danh từ động lực", 1, None, None, "LC", None),
    ("S013", "employment", "L", "synonym",
     "S012: hiring in the care economy", "med", None,
     "employment ≈ hiring/jobs trong chuỗi việc làm; VI thị trường việc làm",
     1, None, None, "LC", None),
    ("S013", "Chapman", "L", "repetition",
     "S010: Chapman said", "high", None,
     "attribution cuối quote; VI tách attribution thành câu riêng (S013 VI)",
     1, None, None, "LC", None),
    # S014 — echo Key Points S004, lộ diện KPMG
    ("S014", "survey", "L", "repetition",
     "S004: a survey has shown", "high", None,
     "Key Points nói chung, câu này lộ diện KPMG; VI lược khảo sát ở S004 "
     "nên phía VI đây là lần đầu", 1, None, None, "LC", None),
    # [Phase-2] business leaders ← employer (S008): mắt xích được cite làm
    # tiền trạm 3 lần (S015 CEOs, S016 businesses, S018 business leaders)
    # nhưng trước đây chưa có hàng (nhóm 12, bài học P28) — TNT §32 phép
    # liên tưởng + H&H §6.4: employer ≈ business, cùng trường phía doanh
    # nghiệp.
    ("S014", "business leaders", "L", "collocation",
     "S008: employer concerns about sluggish spending", "med", None,
     "liên tưởng employer → business leaders — mở lại chuỗi phía doanh "
     "nghiệp bằng tên gọi mới; VI lược ở S014 nên chuỗi VI đi vòng qua "
     "CEO (S015 TT)", 1, None, None, "LC", None),
    ("S014", "digital transformation", "L", "repetition",
     "S004: Digital transformation", "high", None,
     "echo nguyên văn Key Points", 1, None, None, "LC", None),
    ("S014", "cybersecurity", "L", "repetition",
     "S004: cybersecurity", "high", None, "echo nguyên văn Key Points",
     1, None, None, "LC", None),
    ("S014", "artificial intelligence (AI)", "L", "repetition",
     "S004: AI", "high", None,
     "AI lần đầu (S004) nay viết đầy đủ + viết tắt", 1, None, None,
     "LC", None),
    ("S014", "challenges", "L", "repetition",
     "S004: will challenge the private sector", "high", None,
     "động từ → danh từ; pressing là bổ sung", 1, None, None, "LC", None),
    ("S014", "private sector", "L", "repetition",
     "S004: the private sector", "high", "R: the", None, 1, None, None,
     "LC", None),
    # S015
    ("S015", "technology", "L", "repetition",
     "S005: tech", "med", None, "chuỗi technology/tech", 1, None, None,
     "LC", None),
    ("S015", "concern", "L", "repetition",
     "S008: employer concerns about sluggish spending", "med", None,
     "top concern; S008 là dòng không có bản dịch nên chuỗi concern không "
     "có phía VI", 1, None, None, "LC", None),
    ("S015", "CEOs", "L", "synonym",
     "S014: Australian business leaders", "med", None,
     "CEO = nhóm lãnh đạo doanh nghiệp được khảo sát", 1, None, None,
     "LC", None),
    # S016
    ("S016", "Chapman", "L", "repetition",
     "S013: Chapman said", "high", None, "attribution đầu câu",
     1, None, None, "LC", None),
    ("S016", "that", "R", "demonstrative",
     "S015: Skills gaps ... a top concern for CEOs", "high", None,
     "that means — quy chiếu mệnh đề (discourse deictic); đối ứng VI điều này",
     1, None, None, "LC", "A"),
    ("S016", "demand", "L", "repetition",
     "S013: That ongoing demand", "high", None, None, 1, None, None,
     "LC", None),
    ("S016", "data scientists", "L", "repetition",
     "S015: data science", "high", None,
     "data science → data scientists", 1, None, None, "LC", None),
    # [Phase-2] grow ← pick up (S009): chuỗi động từ tăng (H&H §6.2
    # reiteration — synonym; TNT §31) — grow ≈ pick up; EN phân tán từ
    # vựng nơi VI lặp nguyên từ tăng (NTT 2020 §2.1 chiều ngược).
    ("S016", "grow", "L", "synonym",
     "S009: demand to pick up in 2025", "med", None,
     "will likely grow ≈ pick up — mắt xích chuỗi tăng EN; VI giữ nguyên "
     "từ tăng (tăng lên, S016 TT)", 1, None, None, "LC", None),
    ("S016", "businesses", "L", "repetition",
     "S014: business leaders", "med", None,
     "lặp hình vị business (phía doanh nghiệp)", 1, None, None, "LC", None),
    ("S016", "technologies", "L", "repetition",
     "S015: technology", "high", None,
     "new là bổ sung (new technologies)", 1, None, None, "LC", None),
    # S017
    ("S017", "tech", "L", "repetition",
     "S016: new technologies", "high", None, None, 1, None, None, "LC", None),
    ("S017", "generative AI", "L", "repetition",
     "S014: artificial intelligence (AI)", "high", None,
     "generative là hạn định mới; VI lược generative", 1, None, None,
     "LC", None),
    ("S017", "in turn", "C", "causal",
     "S016: demand for programmers and data scientists will likely grow",
     "med", None,
     "nối hệ quả dây chuyền từ S016; VI lược bỏ (không có tie C đối ứng)",
     1, None, None, "LC", None),
    # [Phase-2] strengthen ← grow (S016): tiếp chuỗi động từ tăng bằng đồng
    # nghĩa (H&H §6.2; TNT §31) — strengthen ≈ grow; VI làm tăng (giữ
    # chuỗi tăng nguyên vẹn).
    ("S017", "strengthen", "L", "synonym",
     "S016: will likely grow", "med", None,
     "strengthen demand ≈ grow — Phase-1 ghi EN đổi từ nên khó thành chuỗi "
     "liền; Phase-2 đánh từng mắt xích đồng nghĩa, tiền trạm = nhắc gần "
     "nhất", 1, None, None, "LC", None),
    ("S017", "demand", "L", "repetition",
     "S016: demand for programmers", "high", None,
     "VI thay bằng làm tăng giá trị nên mất đối ứng từ vựng",
     1, None, None, "LC", None),
    ("S017", "skills", "L", "repetition",
     "S015: Skills gaps", "med", None,
     "soft là hạn định mới (thuật ngữ trong ngoặc kép)", 1, None, None,
     "LC", None),
    # S018 — quote Dengate
    ("S018", "business leaders", "L", "repetition",
     "S014: Australian business leaders", "high", None, "trong quote",
     1, None, None, "LC", None),
    ("S018", "AI", "L", "repetition",
     "S017: generative AI", "high", None, None, 1, None, None, "LC", None),
    ("S018", "skills", "L", "repetition",
     "S017: soft skills", "high", None,
     "core competencies trong câu là đồng nghĩa cùng chuỗi, không đánh thêm",
     1, None, None, "LC", None),
    ("S018", "she", "R", "personal",
     "S017: LinkedIn career expert Cayla Dengate", "high", None,
     "she said — truy hồi Dengate; đối ứng VI bà", 1, None, None,
     "LC", "A"),
    # S019
    ("S019", "career platform", "L", "general word",
     "S017: LinkedIn career expert Cayla Dengate", "med", "R: the",
     "career platform = LinkedIn (tổng quát hóa); VI lược hẳn",
     1, None, None, "LC", None),
    ("S019", "jobs", "L", "repetition",
     "S013: care workers / employment (chuỗi việc làm)", "med", None,
     "list of jobs on the rise; such jobs cuối câu là lặp trong câu "
     "(occ 2) không đánh dấu riêng", 1, None, None, "LC", None),
    ("S019", "demand", "L", "repetition",
     "S017: demand for \"soft skills\"", "high", None, None, 1, None,
     None, "LC", None),
    ("S019", "skills", "L", "repetition",
     "S018: skills such as communication", "high", None,
     "trong interpersonal skills; interpersonal ≈ soft", 1, None, None,
     "LC", None),
    # S020 — KHỐI CẮT: không có bản dịch
    ("S020", "English teachers", "L", "repetition",
     "S019: English teachers", "high", None, "dòng không có bản dịch",
     1, None, None, "LC", None),
    ("S020", "ranking", "L", "synonym",
     "S019: the career platform's list of jobs on the rise", "med",
     "R: the", "ranking ≈ list; dòng không có bản dịch", 1, None, None,
     "LC", None),
    # [Phase-2] specialists ← specialists (S019): lặp danh từ chức danh
    # (H&H §6.2 reiteration; TNT §26 phép lặp từ vựng) — dòng không có
    # bản dịch (khối cắt S020).
    ("S020", "specialists", "L", "repetition",
     "S019: employee relations specialists", "med", None,
     "lặp specialists (travel specialists); dòng không có bản dịch",
     1, None, None, "LC", None),
]

TT = [
    # S002 — Key Points 1
    ("S002", "tuyển dụng", "L", "repetition",
     "S001: nhu cầu tuyển dụng", "high", None,
     "lặp tuyển dụng trong tuyển dụng ồ ạt; đối ứng EN hiring (S002)",
     1, None, None, "LC", None),
    # S003 — Key Points 2
    ("S003", "Tuy nhiên", "C", "adversative",
     "S002: Thị trường lao động Úc vẫn đang ổn định sau giai đoạn tuyển "
     "dụng ồ ạt", "high", None,
     "đối ứng EN But (S003)", 1, None, None, "LC", None),
    ("S003", "tuyển dụng", "L", "repetition",
     "S002: tuyển dụng ồ ạt", "high", None, None, 1, None, None, "LC", None),
    ("S003", "lĩnh vực", "L", "repetition",
     "S001: lĩnh vực y tế và công nghệ", "med", None,
     "lặp từ khung lĩnh vực; nội dung đổi tên (chăm sóc sức khoẻ lần đầu); "
     "các lần lĩnh vực sau là chuỗi khung, không đánh dấu riêng",
     1, None, None, "LC", None),
    # [Phase-2] chăm sóc sức khoẻ ← y tế (S001): mắt xích được cite làm tiền
    # trạm ở S005 nhưng trước đây chưa có hàng (nhóm 12, bài học P28) — VI
    # đặt lại tên trong chuỗi chăm sóc (TNT §31 phép thế đẳng nghĩa; H&H
    # §6.2 synonym); đây là điểm phân rã chuỗi đặc trưng của cặp.
    ("S003", "chăm sóc sức khoẻ", "L", "synonym",
     "S001: lĩnh vực y tế và công nghệ", "med", None,
     "y tế → chăm sóc sức khoẻ (EN giữ nguyên the care economy) — lần đổi "
     "tên đầu tiên, chuỗi VI dao động hai cái tên", 1, None, None,
     "LC", None),
    # S005
    ("S005", "bạn", "R", "personal",
     "độc giả/người tìm việc (ngoại văn bản — khung lời khuyên)", "high",
     None,
     "ngoại quy chiếu; đối ứng EN you (S005); đây trong vế tự sinh cuối câu "
     "là quy chiếu trong câu, không đánh", 1, None, None, "LC", "E"),
    # [Phase-2] việc làm ← ngành nghề (S001): mắt xích được cite làm tiền trạm
    # ở S006 (công việc) nhưng trước đây chưa có hàng (nhóm 12, bài học
    # P28) — việc làm ≈ ngành nghề (TNT §31; H&H §6.2 synonym); đối ứng
    # EN job (S005 ST).
    ("S005", "việc làm", "L", "synonym",
     "S001: Các ngành nghề thuộc lĩnh vực y tế và công nghệ", "med",
     None,
     "chuỗi việc làm VI: ngành nghề (S001) → thị trường lao động (S002) → "
     "việc làm → công việc (S006)", 1, None, None, "LC", None),
    ("S005", "bán lẻ", "L", "repetition",
     "S001: ngành bán lẻ và nhà hàng khách sạn", "high", None, None,
     1, None, None, "LC", None),
    ("S005", "công nghệ", "L", "repetition",
     "S001: lĩnh vực y tế và công nghệ", "high", None, None, 1, None,
     None, "LC", None),
    ("S005", "chăm sóc sức khoẻ", "L", "repetition",
     "S003: lĩnh vực chăm sóc sức khoẻ và giữ trẻ", "high", None,
     "đối ứng EN the care economy (S005)", 1, None, None, "LC", None),
    # S006
    ("S006", "kinh tế", "L", "repetition",
     "S005: các nhà kinh tế", "med", None,
     "Chapman là hiện thân của các nhà kinh tế (S005); nằm trong Chuyên gia "
     "kinh tế cao cấp", 1, None, None, "LC", None),
    ("S006", "nhu cầu tuyển dụng", "L", "repetition",
     "S001: nhu cầu tuyển dụng", "high", None,
     "lặp nguyên cụm (đặc trưng VI: gom cụm cố định)", 1, None, None,
     "LC", None),
    ("S006", "công việc", "L", "synonym",
     "S005: việc làm", "med", None,
     "công việc ≈ việc làm (lặp hình vị việc)", 1, None, None, "LC", None),
    ("S006", "kỳ vọng", "L", "synonym",
     "S001: được dự đoán", "med", None,
     "kỳ vọng ≈ dự đoán — chuỗi động từ dự báo; đối ứng EN hopes (S006)",
     1, None, None, "LC", None),
    # S007
    ("S007", "Tuy nhiên", "C", "adversative",
     "S006: kỳ vọng sẽ thấy nhu cầu tuyển dụng mạnh mẽ", "high", None,
     "đối ứng EN However (S007)", 1, None, None, "LC", None),
    ("S007", "điều này", "R", "demonstrative",
     "S006: kỳ vọng sẽ thấy nhu cầu tuyển dụng mạnh mẽ", "high", None,
     "điều này = kỳ vọng tuyển dụng mạnh; đối ứng EN that (S007)",
     1, None, None, "LC", "A"),
    # S008 — quote Chapman; bạn không đánh (attribution ông nói cùng câu)
    ("S008", "lãi suất", "L", "repetition",
     "S007: cắt giảm lãi suất", "high", None, None, 1, None, None,
     "LC", None),
    ("S008", "kỳ vọng", "L", "repetition",
     "S006: kỳ vọng", "high", None, None, 1, None, None, "LC", None),
    ("S008", "nhu cầu tuyển dụng", "L", "repetition",
     "S006: nhu cầu tuyển dụng", "high", None,
     "VI tự sinh cụm này trong quote (EN chỉ có retail and hospitality "
     "demand)", 1, None, None, "LC", None),
    ("S008", "bán lẻ và nhà hàng khách sạn", "L", "repetition",
     "S001: ngành bán lẻ và nhà hàng khách sạn", "high", None,
     "echo nguyên văn lede; EN those cost of living pressures mất chỉ từ "
     "phía VI", 1, None, None, "LC", None),
    # [Phase-2] mạnh ← mạnh mẽ (S006): lặp hình vị mạnh (TNT §26 phép lặp từ
    # vựng; H&H §6.2) — VI tự sinh cụm tăng mạnh echo tính từ mạnh mẽ; tăng
    # trong cụm là lần đầu chuỗi tăng nên không có hàng riêng (occ 1: mạnh
    # nằm trong tăng mạnh).
    ("S008", "mạnh", "L", "repetition",
     "S006: nhu cầu tuyển dụng mạnh mẽ", "med", None,
     "lặp hình vị mạnh (tăng mạnh ← mạnh mẽ); EN đối ứng dùng pick up nên "
     "không có hình vị strong lặp phía EN", 1, None, None, "LC", None),
    ("S008", "ông", "R", "personal",
     "S006: ông Blair Chapman", "high", None,
     "ông nói — danh xưng đại từ truy hồi Chapman; đối ứng EN he said "
     "(S009); bạn trong quote không đánh", 1, None, None, "LC", "A"),
    # S009 — VI tách đề tài, echo một phần Key Points S002
    ("S009", "thị trường lao động", "L", "repetition",
     "S002: Thị trường lao động Úc", "high", None,
     "VI tách thành đề tài (Nói về thị trường lao động); echo Key Points",
     1, None, None, "LC", None),
    ("S009", "Chapman", "L", "repetition",
     "S006: ông Blair Chapman", "high", None, None, 1, None, None,
     "LC", None),
    ("S009", "tuyển dụng", "L", "repetition",
     "S008: nhu cầu tuyển dụng", "high", None, "việc tuyển dụng",
     1, None, None, "LC", None),
    ("S009", "ổn định", "L", "repetition",
     "S002: vẫn đang ổn định", "high", None,
     "echo nguyên văn Key Points; VI thêm dần", 1, None, None, "LC", None),
    # [Phase-2] thời kỳ ← giai đoạn (S002): echo một phần Key Points — VI dụ
    # lại thay vì lặp nguyên văn (TNT §31 đồng nghĩa; H&H §6.2) — hoàn tất
    # cửa sổ echo S009←S002 (ổn định, bùng nổ, COVID-19 đã có từ Phase-1).
    ("S009", "thời kỳ", "L", "synonym",
     "S002: sau giai đoạn tuyển dụng ồ ạt", "med", None,
     "thời kỳ ≈ giai đoạn — echo từng phần Key Points (EN lặp nguyên văn "
     "post-COVID-19 pandemic hiring boom)", 1, None, None, "LC", None),
    ("S009", "bùng nổ", "L", "synonym",
     "S002: tuyển dụng ồ ạt", "med", None,
     "bùng nổ ≈ ồ ạt (boom); VI dụ lại thay vì lặp nguyên văn như EN",
     1, None, None, "LC", None),
    ("S009", "COVID-19", "L", "repetition",
     "S002: đại dịch COVID-19", "high", None,
     "hậu COVID-19; tên riêng lặp", 1, None, None, "LC", None),
    # S010 — VI lược attribution he said của EN S011
    ("S010", "tuyển dụng", "L", "repetition",
     "S009: việc tuyển dụng", "high", None,
     "quảng cáo tuyển dụng; VI lược attribution", 1, None, None, "LC", None),
    ("S010", "nhu cầu", "L", "repetition",
     "S008: nhu cầu tuyển dụng", "high", None,
     "lao động là bổ sung (nhu cầu lao động)", 1, None, None, "LC", None),
    ("S010", "giảm", "L", "antonym",
     "S008: tăng mạnh", "med", None, "phép đối giảm ↔ tăng",
     1, None, None, "LC", None),
    ("S010", "bình thường", "L", "synonym",
     "S009: ổn định", "med", None,
     "trở lại mức bình thường ≈ ổn định; đối ứng EN normalising ← "
     "stabilising; lỗi chính tả nguồn: phản ảnh (đúng: phản ánh)",
     1, None, None, "LC", None),
    # S011 — VI tự sinh attribution ông dự đoán
    ("S011", "Tuy nhiên", "C", "adversative",
     "S010: Số lượng quảng cáo tuyển dụng đã giảm", "high", None,
     "đối ứng EN But (S012)", 1, None, None, "LC", None),
    ("S011", "ông", "R", "personal",
     "S009: ông Chapman", "high", None,
     "VI tự sinh attribution ông dự đoán (EN S012 không có attribution)",
     1, None, None, "LC", "A"),
    ("S011", "dự đoán", "L", "synonym",
     "S008: kỳ vọng", "med", None,
     "trùng nguyên văn S001 dự đoán; chuỗi dự báo", 1, None, None,
     "LC", None),
    ("S011", "nhu cầu tuyển dụng", "L", "repetition",
     "S008: nhu cầu tuyển dụng", "high", None, None, 1, None, None,
     "LC", None),
    ("S011", "y tế", "L", "repetition",
     "S001: lĩnh vực y tế", "med", None,
     "đổi tên so với chăm sóc sức khoẻ (S003/S005) — chuỗi chăm sóc phân "
     "rã, dao động hai tên", 1, None, None, "LC", None),
    ("S011", "giữ trẻ", "L", "repetition",
     "S003: chăm sóc sức khoẻ và giữ trẻ", "high", None, None, 1, None,
     None, "LC", None),
    ("S011", "tăng", "L", "repetition",
     "S008: tăng mạnh", "high", None,
     "EN phủ định (unlikely to slow down) → VI khẳng định (sẽ tiếp tục tăng)",
     1, None, None, "LC", None),
    # S012 — quote, VI lược chỉ từ That của EN S013
    ("S012", "nhu cầu", "L", "repetition",
     "S011: nhu cầu tuyển dụng", "high", None,
     "EN dùng chỉ từ That (S013) — VI lược chỉ từ, đặt lại bằng số nhiều "
     "Những; dài hạn thay ongoing", 1, None, None, "LC", None),
    ("S012", "nhân lực", "L", "synonym",
     "S010: nhu cầu lao động", "med", None,
     "nhân lực ≈ lao động; đối ứng EN care workers", 1, None, None,
     "LC", None),
    ("S012", "chăm sóc sức khoẻ", "L", "repetition",
     "S011: y tế (cùng chuỗi chăm sóc; nguyên văn ở S005)", "high", None,
     "S011 gọi là y tế — chuỗi đổi tên qua lại trong hai câu liền",
     1, None, None, "LC", None),
    ("S012", "tiếp tục", "L", "repetition",
     "S011: sẽ tiếp tục tăng", "high", None,
     "vẫn + tiếp tục gom nghĩa EN isn't going away / continuing / continue "
     "(3 hình thức trong 1 câu)", 1, None, None, "LC", None),
    # [Phase-2] động lực ← thúc đẩy (S001): cặp quá trình–sản phẩm (H&H §6.4
    # collocation; TNT §32 phép liên tưởng) — động lực ≈ cái thúc đẩy, danh
    # hóa động từ; đối xứng EN drive (S013 ST) ← fuel (S001 ST); vế S001
    # VI tự sinh nên đây là chuỗi VI-only.
    ("S012", "động lực", "L", "collocation",
     "S001: nền kinh tế phục hồi cũng thúc đẩy nhu cầu tuyển dụng", "med",
     None,
     "động lực lớn ← thúc đẩy: quá trình (động từ) → sản phẩm (danh từ); "
     "EN giữ động từ drive", 1, None, None, "LC", None),
    ("S012", "thị trường việc làm", "L", "repetition",
     "S009: thị trường lao động", "med", None,
     "ghép lại thị trường (S009) + việc làm (S005); đối ứng EN employment",
     1, None, None, "LC", None),
    # S013 — attribution tách thành câu riêng (mảnh câu không có dấu chấm)
    ("S013", "Blair Chapman", "L", "repetition",
     "S009: ông Chapman", "high", None,
     "attribution bị tách khỏi quote; tên đầy đủ quay lại như S006",
     1, None, None, "LC", None),
    ("S013", "chuyên gia kinh tế cao cấp", "L", "repetition",
     "S006: Chuyên gia kinh tế cao cấp của SEEK", "high", None,
     "echo nguyên văn danh hiệu", 1, None, None, "LC", None),
    ("S013", "SEEK", "L", "repetition",
     "S006: của SEEK", "high", None, None, 1, None, None, "LC", None),
    # S014 — echo gần nguyên văn Key Points S004
    ("S014", "chuyển đổi số", "L", "repetition",
     "S004: chuyển đổi số", "high", None, "echo nguyên văn Key Points",
     1, None, None, "LC", None),
    ("S014", "an ninh mạng", "L", "repetition",
     "S004: an ninh mạng", "high", None, "echo nguyên văn Key Points",
     1, None, None, "LC", None),
    ("S014", "trí tuệ nhân tạo (AI)", "L", "repetition",
     "S004: trí tuệ nhân tạo", "high", None,
     "echo Key Points; S004 chưa có (AI), câu này thêm", 1, None, None,
     "LC", None),
    ("S014", "thách thức", "L", "repetition",
     "S004: đặt ra nhiều thách thức", "high", None, None, 1, None, None,
     "LC", None),
    ("S014", "khu vực tư nhân", "L", "repetition",
     "S004: khu vực tư nhân", "high", None, None, 1, None, None,
     "LC", None),
    # S015 — VI lược business leaders (S014) nên CEO là lần đầu
    ("S015", "công nghệ", "L", "repetition",
     "S005: công nghệ", "high", None, None, 1, None, None, "LC", None),
    # S016
    ("S016", "Chapman", "L", "repetition",
     "S013: Blair Chapman", "high", None,
     "attribution đảo lên đầu (Theo ông Chapman); ông kèm tên trong câu "
     "không đánh", 1, None, None, "LC", None),
    ("S016", "điều này", "R", "demonstrative",
     "S015: Khoảng cách về kỹ năng ... mối lo ngại hàng đầu", "high", None,
     "quy chiếu mệnh đề; đối ứng EN that means (S016)", 1, None, None,
     "LC", "A"),
    ("S016", "nhu cầu", "L", "repetition",
     "S012: Những nhu cầu dài hạn", "high", None, None, 1, None, None,
     "LC", None),
    ("S016", "khoa học dữ liệu", "L", "repetition",
     "S015: khoa học dữ liệu", "high", None,
     "trong nhà khoa học dữ liệu (= data scientists; EN data scientists ← "
     "data science)", 1, None, None, "LC", None),
    ("S016", "doanh nghiệp", "L", "collocation",
     "S015: các CEO", "med", None,
     "liên tưởng CEO → doanh nghiệp (cùng trường phía doanh nghiệp); EN nối "
     "thẳng business leaders (S014) nhưng VI lược ở S014",
     1, None, None, "LC", None),
    ("S016", "công nghệ", "L", "repetition",
     "S015: công nghệ", "high", None, "mới là bổ sung (công nghệ mới)",
     1, None, None, "LC", None),
    ("S016", "tăng", "L", "repetition",
     "S011: sẽ tiếp tục tăng", "high", None,
     "tăng lên; EN dùng grow — VI giữ chuỗi tăng nguyên vẹn",
     1, None, None, "LC", None),
    # S017 — VI lược in turn và generative
    ("S017", "công nghệ", "L", "repetition",
     "S016: công nghệ mới", "high", None, None, 1, None, None, "LC", None),
    ("S017", "AI", "L", "repetition",
     "S014: trí tuệ nhân tạo (AI)", "high", None,
     "VI lược hạn định generative của EN", 1, None, None, "LC", None),
    ("S017", "tăng", "L", "repetition",
     "S016: tăng lên", "med", None,
     "làm tăng giá trị; EN dùng strengthen — VI giữ chuỗi tăng",
     1, None, None, "LC", None),
    ("S017", "kỹ năng", "L", "repetition",
     "S015: Khoảng cách về kỹ năng", "high", None,
     "mềm là hạn định mới (= soft, trong ngoặc kép); EN in turn bị VI lược "
     "nên không có tie C ở câu này", 1, None, None, "LC", None),
    # S018 — quote Dengate
    ("S018", "lãnh đạo doanh nghiệp", "L", "synonym",
     "S015: các CEO", "med", None,
     "lãnh đạo doanh nghiệp = business leaders; EN nối S014 business "
     "leaders nhưng VI lược ở S014 nên chuỗi đi vòng qua CEO",
     1, None, None, "LC", None),
    ("S018", "AI", "L", "repetition",
     "S017: AI", "high", None, None, 1, None, None, "LC", None),
    ("S018", "kỹ năng", "L", "repetition",
     "S017: kỹ năng mềm", "high", None,
     "occ 1 (những kỹ năng cốt lõi ≈ EN core competencies); kỹ năng lần 2 "
     "trong câu không đánh thêm", 1, None, None, "LC", None),
    ("S018", "giá trị", "L", "repetition",
     "S017: làm tăng giá trị", "high", None,
     "chuỗi giá trị do VI tự sinh (EN S017 là strengthen demand, không có "
     "value)", 1, None, None, "LC", None),
    ("S018", "bà", "R", "personal",
     "S017: Chuyên gia về nghề nghiệp Cayla Dengate đến từ LinkedIn",
     "high", None,
     "bà nói — danh xưng đại từ nữ truy hồi Dengate; đối ứng EN she said",
     1, None, None, "LC", "A"),
    # S019 — VI lược career platform's của EN
    ("S019", "công việc", "L", "synonym",
     "S012: thị trường việc làm (chuỗi việc làm; nguyên văn công việc ở "
     "S006)", "med", None,
     "VI lược career platform's của EN nên chuỗi LinkedIn đứt",
     1, None, None, "LC", None),
    ("S019", "nhu cầu", "L", "repetition",
     "S016: nhu cầu cho các lập trình viên", "high", None, "nhu cầu cao",
     1, None, None, "LC", None),
    ("S019", "kỹ năng", "L", "repetition",
     "S018: các kỹ năng như giao tiếp", "high", None,
     "trong kỹ năng giao tiếp giữa người với người (EN interpersonal "
     "skills)", 1, None, None, "LC", None),
]
