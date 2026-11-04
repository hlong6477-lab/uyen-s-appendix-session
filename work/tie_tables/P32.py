# P32 tie table — WRITTEN BY HAND FROM work/analysis/P32_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Text/gap_after là chuỗi con nguyên văn trong câu (kiểm bằng pipeline.locate).
# Nguồn: TT S002–S003 là quote TIẾNG ANH NGUYÊN VĂN (không dịch) → không đánh tie VI;
# EN S016–S018 là khối cắt (VI none) → tie chỉ phía EN.
# Subhead: không có (bài không chia tiểu đề).
# [Phase-2] Bổ sung theo PHASE2_PROTOCOL.md (lượt 1 + lượt 2): 22 hàng mới EN /
# 15 hàng mới VI, 3 RECLASSIFY (S004/S022 "the move", S023 "reversal": R
# nominal → L theo H&H §6.1 + mapping §3.6 + protocol nhóm 3), 4 hàng cũ +alt
# "R: the" (nhóm 8), 1 hàng cũ cập nhật note (S021 TT "thay đổi"); lượt 2 thêm
# 6 EN + 5 VI (nhóm 2/4/12), 1 sửa ante (S019 "Bowser": S013→S015), 4 cập nhật
# note (S015 EN Home Rule; S006/S015/S017 TT).

ST = [
    # S002 — quote Bowser (VI giữ nguyên tiếng Anh, không đánh phía TT)
    ("S002", "Bowser", "L", "repetition", "S001: Washington Mayor Muriel Bowser",
     "high", None, "tên riêng lặp", 1, None, None, "LC", None),
    # [Phase-2] +alt "R: the" (mapping §3.6): "The mural" = the + đổi tên
    # (painting → mural) — phần quy chiếu của mạo từ ghi vào alt.
    ("S002", "The mural", "L", "synonym", "S001: the large painting of the words",
     "high", "R: the", "mural ≈ large painting; mở quote", 1, None, None, "LC",
     None),
    # [Phase-2] Sửa occ 1→2 (bẫy chuỗi con, precedent P26 + protocol §2):
    # lần 1 "we" là chuỗi con trong "week" (offset 59), lần 2 mới là đại từ
    # trong quote (offset 167) — ghi chú vị trí theo quy ước.
    ("S002", "we", "R", "personal",
     "chính quyền/thành phố Washington (ngoại văn bản — quote Bowser)",
     "med", None, "ngoại quy chiếu; 'our city' cùng chuỗi trong câu không "
     "đánh; occ 2 vì lần 1 'we' nằm trong 'week'",
     2, None, None, "LC", "E"),
    # [Phase-2] the change ← S001: danh từ tổng quát / bridging (H&H §6.1;
    # mapping §3.6) — "the change" tóm chỉ việc xóa tranh; mạo từ the mang
    # quy chiếu → alt "R: the" (một hình thức một hàng, mapping §3.13).
    ("S002", "the change", "L", "general word",
     "S001: began removing the large painting", "med", "R: the",
     "danh từ tổng quát tóm chỉ sự kiện xóa tranh (H&H §6.1); nằm trong "
     "quote không dịch nên không có đối ứng VI", 1, None, None, "LC",
     None),
    # [Phase-2] congressional ← S001 Congress: lặp hình vị qua tính từ hóa
    # (H&H §6.2; TNT §26 phép lặp) — mắt xích chuỗi Quốc hội trong quote.
    ("S002", "congressional", "L", "repetition",
     "S001: the Republican-controlled Congress", "med", None,
     "tính từ congressional lặp hình vị Congress; quote không dịch phía "
     "VI", 1, None, None, "LC", None),
    # [Phase-2] interference ← S001 encroachment: đồng nghĩa theo ngữ cảnh
    # (H&H §6.2) — mở chuỗi xâm phạm encroachment → interference (S002) →
    # take over (S008) → interfere (S014); S014 cite S002 nên cần hàng
    # tiền trạm (protocol nhóm 12).
    ("S002", "interference", "L", "synonym",
     "S001: threats of encroachment", "med", None,
     "interference ≈ encroachment trong trường 'xâm phạm của liên bang'; "
     "VI hiện thực hóa sớm bằng 'can thiệp' (S001 TT)", 1, None, None,
     "LC", None),
    # S003 — câu 2 của quote (không dịch phía VI)
    ("S003", "our", "R", "personal",
     "chính quyền/thành phố Washington (ngoại văn bản — quote Bowser)",
     "med", None, "cùng chuỗi we (S002), câu mới nên đánh dấu", 1, None,
     None, "LC", "E"),
    # S004
    # [Phase-2] RECLASSIFY R nominal → L general word (H&H §6.1; mapping
    # §3.6; protocol nhóm 3 — "the move" là ví dụ chuẩn danh từ tổng quát
    # trỏ về tình huống câu trước): mạo từ the chuyển vào alt; VI đối ứng
    # "Động thái này" giữ R chỉ từ (the ↔ demonstrative, NTT 2020 §2.2).
    ("S004", "The move", "L", "general word",
     "S001: began removing the painting", "high", "R: the",
     "danh từ tổng quát tóm chỉ sự kiện xóa tranh (H&H §6.1); một hình "
     "thức một hàng — phần quy chiếu của 'the' ghi ở alt (mapping §3.13)",
     1, None, None, "LC", None),
    ("S004", "Bowser", "L", "repetition", "S002: Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S004", "Trump", "L", "repetition", "S001: President Donald Trump",
     "high", None, None, 1, None, None, "LC", None),
    ("S004", "congressional Republicans", "L", "repetition",
     "S001: the Republican-controlled Congress", "high", None,
     "lặp hình vị Congress + Republican", 1, None, None, "LC", None),
    # S005
    ("S005", "Bowser", "L", "repetition", "S004: Bowser's striking shift",
     "high", None, None, 1, None, None, "LC", None),
    ("S005", "the painting", "L", "repetition", "S001: the large painting",
     "high", None, "lặp NP 'the painting'", 1, None, None, "LC", None),
    ("S005", "Black Lives Matter", "L", "repetition",
     "S001: the words \"Black Lives Matter\"", "high", None,
     "tên phong trào lặp trong tên riêng Plaza", 1, None, None, "LC", None),
    # [Phase-2 lượt 2] a Democrat ↔ S004 congressional Republicans: phép đối
    # liên câu đảng đối lập (TNT §30; H&H §6.4 opposites — protocol nhóm 2);
    # VI đối xứng "đảng viên Dân chủ" ↔ "đảng viên Cộng hòa" (S005/S004 TT).
    ("S005", "a Democrat", "L", "antonym",
     "S004: congressional Republicans", "med", None,
     "phép đối Dân chủ ↔ Cộng hòa qua câu (TNT §30; H&H §6.4); đối xứng VI "
     "'đảng viên Dân chủ' (S005 TT)", 1, None, None, "LC", None),
    # [Phase-2] the intersection ← S001 street: bridging kết hợp (H&H
    # §6.4 collocation / phép liên tưởng TNT §32; mapping §3.6 the+rename)
    # — S006 'that location' cite mắt xích này (protocol nhóm 12); VI đối
    # ứng 'giao lộ này' là R chỉ từ.
    ("S005", "the intersection", "L", "collocation",
     "S001: on a street one block from the White House", "med",
     "R: the",
     "giao lộ kết hợp với con đường S001 (bridging); EN định danh bằng "
     "mạo từ, VI bằng chỉ từ 'này' — the ↔ demonstrative (NTT 2020 §2.2)",
     1, None, None, "LC", None),
    # S006
    ("S006", "It", "R", "personal", "S005: a public act of defiance",
     "high", None, "It = việc kẻ tranh/đổi tên (S005)", 1, None, None,
     "LC", "A"),
    ("S006", "that location", "R", "demonstrative", "S005: the intersection",
     "high", None, "chỉ từ hồi quy về giao lộ", 1, None, None, "LC", "A"),
    # S007
    ("S007", "Her", "R", "personal", "S006: George Floyd — không; Bowser (S005)",
     "high", None, "Her = Bowser; 'her' trong S008 mới là trong câu",
     1, None, None, "LC", "A"),
    ("S007", "the protests", "L", "repetition", "S006: chaotic protests",
     "high", None, None, 1, None, None, "LC", None),
    ("S007", "Trump", "L", "repetition", "S004: Trump", "high", None,
     None, 1, None, None, "LC", None),
    # S008
    # [Phase-2] +alt "R: the" (mapping §3.6): "The president" = the + đổi
    # tên (Trump → president) — quan hệ từ vựng giữ L, mạo từ vào alt.
    ("S008", "The president", "L", "repetition",
     "S004: the president's first term", "high", "R: the",
     "danh ngữ xác định chỉ Trump (S007); đầu từ lặp S004", 1, None, None,
     "LC", None),
    ("S008", "Bowser", "L", "repetition", "S007: Her", "high", None,
     None, 1, None, None, "LC", None),
    ("S008", "threatened", "L", "repetition", "S001: threats of encroachment",
     "high", None, "chuỗi đe dọa bắt đầu; hình vị threat lặp", 1, None,
     None, "LC", None),
    # [Phase-2] city ← S002 our city: mắt xích sót chuỗi 'city' (H&H §6.2;
    # protocol nhóm 12 — chuỗi city S002→S008→S014→S019→S020 mới kín).
    ("S008", "city", "L", "repetition", "S002: our city (quote)", "high",
     None,
     "lặp city ('her city'); tiền trạm nằm trong quote không dịch", 1,
     None, None, "LC", None),
    # [Phase-2 lượt 2] control ← S001 Republican-controlled: mắt xích sót
    # chuỗi control (H&H §6.2; TNT §26 — protocol nhóm 4/12): 'losing control
    # of her city' lặp hình vị controlled (S001) nhưng referent khác (Bowser
    # mất kiểm soát thành phố ↔ đảng Cộng hòa kiểm soát Quốc hội); chuỗi
    # S001→S008→S014 giờ kín, đối xứng VI kiểm soát S001→S008→S015.
    ("S008", "control", "L", "repetition",
     "S001: the Republican-controlled Congress", "med", None,
     "lặp hình vị control ('losing control'); referent khác S001 — TNT §26 "
     "phép lặp; nối kín chuỗi control 3 mắt (S001→S008→S014)", 1, None,
     None, "LC", None),
    # [Phase-2] take over ← S001 encroachment: mắt xích đầu chuỗi tiếp quản
    # (H&H §6.2 synonym) — S012 'takeover' cite S008; VI đối ứng 'tiếp
    # quản' ← 'can thiệp' cũng được bổ Phase-2.
    ("S008", "take over", "L", "synonym",
     "S001: threats of encroachment", "med", None,
     "đe dọa xâm phạm cụ thể hóa thành hành động chiếm quyền; chuỗi xâm "
     "phạm S001→S002→S008→S014", 1, None, None, "LC", None),
    # [Phase-2] Metropolitan Police Department ← S006 police: lặp hình vị
    # police (H&H §6.2) — đối xứng VI 'Cảnh sát' (S008 TT ← S006).
    ("S008", "Metropolitan Police Department", "L", "repetition",
     "S006: police brutality ... police officer", "high", None,
     "tên cơ quan chứa hình vị police; S006 police ×2 cùng câu nên chỉ "
     "đánh tiền trạm", 1, None, None, "LC", None),
    # S009
    ("S009", "He", "R", "personal", "S008: The president (Trump)",
     "high", None, None, 1, None, None, "LC", "A"),
    ("S009", "protesters", "L", "repetition", "S007: the protests", "high",
     None, "biểu tình → người biểu tình (thêm hậu tố -er)", 1, None, None,
     "LC", None),
    # S010
    ("S010", "Trump's", "L", "repetition", "S007: Trump", "high", None,
     None, 1, None, None, "LC", None),
    ("S010", "the White House", "L", "repetition", "S001: the White House",
     "high", None, None, 1, None, None, "LC", None),
    ("S010", "Bowser", "L", "repetition", "S008: Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S010", "conflict", "L", "repetition", "S007: direct conflict", "high",
     None, None, 1, None, None, "LC", None),
    ("S010", "second stint", "L", "repetition", "S004: first term", "med",
     None, "lặp trường 'nhiệm kỳ'; đối first ↔ second", 1, None, None,
     "LC", None),
    # S011
    ("S011", "She", "R", "personal", "S010: Bowser", "high", None,
     None, 1, None, None, "LC", "A"),
    ("S011", "Trump's", "L", "repetition", "S010: Trump's second stint",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] +alt "R: the" (mapping §3.6): "the president" = the + đổi
    # tên của Trump — mạo từ vào alt (như S008).
    ("S011", "the president", "L", "repetition", "S008: The president",
     "high", "R: the", "danh ngữ xác định chỉ Trump", 1, None, None, "LC",
     None),
    ("S011", "federal workers", "L", "collocation",
     "S003: the federal job cuts", "med", None,
     "trường nghĩa 'liên bang + việc/lao động' (quote không dịch phía VI)",
     1, None, None, "LC", None),
    # [Phase-2] points of agreement ← S010 points of contention: phép đối
    # liên câu (TNT §30; H&H §6.4 opposites) — cấu trúc song song 'points
    # of X' + đối nghĩa contention ↔ agreement; VI đối ứng 'đồng thuận' ↔
    # 'tranh cãi'; mở chuỗi agreed (S019).
    ("S011", "points of agreement", "L", "antonym",
     "S010: downplay any points of contention", "high", None,
     "phép đối contention ↔ agreement qua câu", 1, None, None, "LC",
     None),
    # S012
    ("S012", "Trump", "L", "repetition", "S011: Trump's Mar-a-Lago estate",
     "high", None, None, 1, None, None, "LC", None),
    ("S012", "takeover", "L", "repetition", "S008: take over", "high", None,
     "take over → takeover (đảo hình vị tạo danh từ)", 1, None, None,
     "LC", None),
    ("S012", "Washington", "L", "repetition", "S001: Washington Mayor",
     "high", None, "'the nation's capital' cùng câu là đồng nghĩa, không đánh",
     1, None, None, "LC", None),
    # S013
    ("S013", "Bowser", "L", "repetition", "S011: She", "high", None,
     None, 1, None, None, "LC", None),
    ("S013", "the White House", "L", "repetition", "S010: the White House",
     "high", None, "ẩn dụ chỉ chính quyền liên bang", 1, None, None,
     "LC", None),
    ("S013", "Washington", "L", "repetition", "S012: Washington", "high",
     None, None, 1, None, None, "LC", None),
    ("S013", "threat", "L", "repetition", "S008: threatened", "high", None,
     "chuỗi đe dọa: 'the greatest threat'", 1, None, None, "LC", None),
    ("S013", "Congress", "L", "repetition", "S001: Congress", "high", None,
     None, 1, None, None, "LC", None),
    # S014
    ("S014", "Republicans", "L", "repetition",
     "S004: congressional Republicans", "high", None, None, 1, None, None,
     "LC", None),
    ("S014", "Congress", "L", "repetition", "S013: Congress", "high", None,
     None, 1, None, None, "LC", None),
    ("S014", "threatened", "L", "repetition", "S013: threat", "high", None,
     "chuỗi đe dọa", 1, None, None, "LC", None),
    ("S014", "interfere", "L", "repetition", "S002: congressional interference",
     "med", None, "interference → interfere (quote không dịch phía VI)",
     1, None, None, "LC", None),
    # [Phase-2] city ← S008 her city: mắt xích sót chuỗi city (H&H §6.2;
    # protocol nhóm 12) — tiền trạm cho S019 'city finances'; VI thực hiện
    # chuỗi bằng 'thủ đô Washington' (S015 TT).
    ("S014", "city", "L", "repetition", "S008: her city", "high", None,
     "lặp city ('city affairs')", 1, None, None, "LC", None),
    # [Phase-2 lượt 2] control ← S001 Republican-controlled: mắt xích sót
    # chuỗi control (H&H §6.2 — protocol nhóm 4): 'who control both
    # chambers' trùng referent S001 (đảng Cộng hòa kiểm soát Quốc hội);
    # S008 'losing control' cùng hình vị nhưng referent khác; VI đối xứng
    # 'kiểm soát' (S015 TT).
    ("S014", "control", "L", "repetition",
     "S001: the Republican-controlled Congress", "high", None,
     "lặp control ('who control both chambers') — referent trùng S001; mắt "
     "S008 'losing control' cùng chuỗi hình vị, referent khác (ghi note)",
     1, None, None, "LC", None),
    # S015
    ("S015", "Congress", "L", "repetition", "S014: Congress", "high", None,
     "before Congress", 1, None, None, "LC", None),
    ("S015", "Bowser", "L", "repetition", "S013: Bowser", "high", None,
     "đạo luật mang tên đô trưởng", 1, None, None, "LC", None),
    ("S015", "Home Rule", "L", "repetition", "S013: Home Rule autonomy",
     "high", None, "lặp 'Home Rule'; 'autonomy' cùng câu có hàng riêng "
     "(lượt 2)", 1, None, None, "LC", None),
    # [Phase-2 lượt 2] autonomy ← S013 Home Rule autonomy: mắt xích sót chuỗi
    # autonomy (H&H §6.2 — protocol nhóm 4): 'grants the capital city
    # limited autonomy' lặp autonomy (S013); đối xứng VI 'quyền tự trị'
    # (S016 TT ← S014 TT).
    ("S015", "autonomy", "L", "repetition", "S013: Home Rule autonomy",
     "high", None,
     "lặp autonomy ('limited autonomy'); chuỗi tự trị — VI 'quyền tự trị' "
     "đối ứng (S016 TT)", 1, None, None, "LC", None),
    # [Phase-2] +alt "R: the" (mapping §3.6) + tiền trạm chốt về dạng đã
    # đánh: "the capital city" = the + đổi tên Washington; chuỗi tại S012
    # do hàng 'Washington' mang (the nation's capital là đồng vị trong
    # cùng câu S012).
    ("S015", "the capital city", "L", "synonym",
     "S012: Washington ('the nation's capital' đồng vị)", "med",
     "R: the", "đổi tên tổng quát hóa chỉ Washington", 1, None, None, "LC",
     None),
    # S016 — KHỐI CẮT (VI none): tie chỉ phía EN
    ("S016", "That", "R", "demonstrative",
     "S015: a measure ... the Bowser Act", "high", None,
     "khối cắt, VI none", 1, None, None, "LC", "A"),
    ("S016", "GOP", "L", "synonym", "S014: Republicans", "high", None,
     "viết tắt cùng chỉ đảng Cộng hoà; khối cắt, VI none", 1, None, None,
     "LC", None),
    # S017 — KHỐI CẮT
    ("S017", "representatives", "L", "collocation",
     "S014: Republicans, who control both chambers of Congress", "med", None,
     "nghị sĩ Hạ viện (nhóm Cộng hoà); khối cắt, VI none", 1, None, None,
     "LC", None),
    ("S017", "Washington", "L", "repetition", "S013: Washington", "high",
     None, "khối cắt, VI none", 1, None, None, "LC", None),
    # [Phase-2 lượt 2] target ← S013 targeting: lặp động từ (H&H §6.2 —
    # protocol nhóm 4): riders 'to target Washington policies' ← 'an
    # executive order targeting Washington' — cùng cấu trúc 'biện pháp liên
    # bang nhắm vào thủ đô'; khối cắt, VI none.
    ("S017", "target", "L", "repetition",
     "S013: an executive order targeting Washington", "high", None,
     "lặp target; song song targeting (S013) + cùng tân ngữ Washington; "
     "khối cắt, VI none", 1, None, None, "LC", None),
    # S018 — KHỐI CẮT
    ("S018", "And", "C", "additive", "S017: Some representatives ... budget riders",
     "high", None, "nối liên câu duy nhất của EN; khối cắt, VI none", 1,
     None, None, "LC", None),
    ("S018", "Congress", "L", "repetition", "S015: Congress", "high", None,
     "khối cắt, VI none", 1, None, None, "LC", None),
    ("S018", "Black Lives Matter", "L", "repetition", "S005: Black Lives Matter Plaza",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S018", "street painting", "L", "repetition", "S005: the painting",
     "high", None, "chuỗi tranh/dòng chữ; khối cắt, VI none", 1, None, None,
     "LC", None),
    # S019
    # [Phase-2 lượt 2] sửa ante S013 → S015 (tiền trạm = nhắc gần nhất,
    # protocol nhóm 4): nhắc Bowser gần nhất trước S019 là "the Bowser Act"
    # (S015 — đã có hàng riêng).
    ("S019", "Bowser", "L", "repetition", "S015: the Bowser Act", "high",
     None, None, 1, None, None, "LC", None),
    ("S019", "Trump", "L", "repetition", "S012: Trump", "high", None,
     "lần 2 trong câu (Trump's push) ghi note", 1, None, None, "LC", None),
    ("S019", "federal workers", "L", "repetition", "S011: federal workers",
     "high", None, None, 1, None, None, "LC", None),
    ("S019", "federal workforce", "L", "synonym", "S011: federal workers",
     "high", None, "workers ≈ workforce", 1, None, None, "LC", None),
    # [Phase-2] agreed ← S011 points of agreement: lặp hình vị agree qua
    # danh hóa ngược (H&H §6.2 reiteration) — VI đổi từ 'nhất trí' ≈ 'đồng
    # thuận' (S017 TT).
    ("S019", "agreed", "L", "repetition",
     "S011: their points of agreement", "high", None,
     "agreed ← agreement: lặp hình vị agree; đối xứng VI nhất trí ← đồng "
     "thuận", 1, None, None, "LC", None),
    # [Phase-2] returning ← S011 return: lặp động từ (H&H §6.2) — VI đối
    # ứng 'trở lại' (S017 TT).
    ("S019", "returning", "L", "repetition",
     "S011: a mutual desire to return federal workers", "high", None,
     "returning ← return: lặp động từ", 1, None, None, "LC", None),
    # [Phase-2] offices ← S011 their offices: mắt xích sót chuỗi văn phòng
    # (H&H §6.2) — VI đối ứng 'văn phòng toàn thời gian' đã có hàng (S017
    # TT).
    ("S019", "offices", "L", "repetition",
     "S011: back to their offices full time", "high", None,
     "lặp offices ('to their offices')", 1, None, None, "LC", None),
    # [Phase-2] city ← S014 city affairs: mắt xích sót chuỗi city (H&H
    # §6.2; protocol nhóm 12 — S020 'the city's' cite 'city finances').
    ("S019", "city", "L", "repetition",
     "S014: interfere in city affairs", "high", None,
     "lặp city ('city finances')", 1, None, None, "LC", None),
    # S020
    ("S020", "the city's", "L", "repetition", "S019: city finances", "med",
     None, "chuỗi 'city' (S008, S014, S015, S019)", 1, None, None, "LC",
     None),
    ("S020", "workers", "L", "repetition", "S019: the federal workforce",
     "high", None, "thousands of workers", 1, None, None, "LC", None),
    ("S020", "federal government", "L", "collocation",
     "S019: the federal workforce", "med", None,
     "trường 'liên bang'; 'last week' lặp S002 nhưng là thời gian, không đánh",
     1, None, None, "LC", None),
    # [Phase-2] financial ← S019 finances: lặp hình vị financ- (H&H §6.2)
    # — đối xứng VI 'tài chính' (S017→S018 TT).
    ("S020", "financial", "L", "repetition",
     "S019: roiling city finances", "med", None,
     "chief financial officer ← city finances: lặp hình vị financ-", 1,
     None, None, "LC", None),
    # [Phase-2] loss ← S019 slash: collocation quá trình–kết quả (H&H
    # §6.4) — VI đối ứng 'mất mát' ← 'cắt giảm' (S018 TT).
    ("S020", "loss", "L", "collocation",
     "S019: push to slash the federal workforce", "med", None,
     "'the loss of thousands of workers' = kết quả của 'slash'; VI 'mất "
     "mát' ← 'cắt giảm'", 1, None, None, "LC", None),
    # S021
    ("S021", "Bowser", "L", "repetition", "S019: Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S021", "Black Lives Matter", "L", "repetition",
     "S018: the Black Lives Matter street painting", "high", None,
     "tiền trạm nằm trong khối cắt (EN-only)", 1, None, None, "LC", None),
    # S022
    ("S022", "Black Lives Matter", "L", "repetition", "S021: Black Lives Matter activists",
     "high", None, "The local ... affiliate", 1, None, None, "LC", None),
    # [Phase-2] RECLASSIFY R nominal → L general word (H&H §6.1; mapping
    # §3.6; protocol nhóm 3): "the move" tóm chỉ động thái ủng hộ BLM của
    # Bowser (S021); VI lặp từ trần 'động thái' (L) — the ↔ zero/lặp từ
    # (NTT 2020 §2.2).
    ("S022", "the move", "L", "general word",
     "S021: Bowser publicly siding with ... activists", "high", "R: the",
     "danh từ tổng quát (H&H §6.1); VI 'động thái' không có chỉ từ — khác "
     "với S004 ('Động thái này'): cùng EN 'the move' dịch hai cách", 1,
     None, None, "LC", None),
    ("S022", "Bowser", "L", "repetition", "S021: Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S022", "police", "L", "repetition", "S006: police brutality", "high",
     None, "biased toward police; chuỗi cảnh sát", 1, None, None, "LC",
     None),
    # S023
    ("S023", "The same activists", "R", "comparative",
     "S022: The local Black Lives Matter affiliate", "high", None,
     "'the same' = quy chiếu so sánh", 1, None, None, "LC", "A"),
    ("S023", "Bowser", "L", "repetition", "S022: Bowser", "high", None,
     None, 1, None, None, "LC", None),
    # [Phase-2] RECLASSIFY R nominal → L synonym (mapping §3.6 nhóm 8: L
    # ưu tiên khi có quan hệ từ vựng): reversal ≈ shift (S004) — đối xứng
    # VI 'thay đổi' ← 'sự thay đổi đáng kể' (S004); sở hữu 'her' (trong
    # câu) chuyển vào alt; đọc bridging về sự kiện xóa tranh (S001) ghi
    # trong note.
    ("S023", "reversal", "L", "synonym",
     "S004: striking shift in tone", "med", "R: her",
     "reversal ≈ shift: tiếp chuỗi 'thay đổi lập trường' (S004), đồng "
     "thời tóm chỉ sự kiện xóa tranh (S001) — chọn quan hệ từ vựng theo "
     "mapping §3.6", 1, None, None, "LC", None),
    # [Phase-2 lượt 2] heaped scorn ← S022 decried: thế đẳng nghĩa liên câu
    # (TNT §31; H&H §6.2 synonym — protocol nhóm 4): heaped scorn ≈ decried
    # (trường 'lên án công khai'); 'dismissed' (S022) cùng trường; VI đối
    # xứng 'lên án' ← 'tố cáo' (S021 TT).
    ("S023", "heaped scorn", "L", "synonym", "S022: decried Bowser", "med",
     None,
     "heaped scorn ≈ decried (TNT §31 thế đẳng nghĩa → L); đối xứng VI lên "
     "án ← tố cáo (S021 TT)", 1, None, None, "LC", None),
    # S024
    ("S024", "Black Lives Matter affiliate", "L", "repetition",
     "S022: The local Black Lives Matter affiliate", "high", None,
     "D.C. ... affiliate; 'Black Lives Mattering' trong quote là chơi chữ -ing, ghi note",
     1, None, None, "LC", None),
    ("S024", "Bowser", "L", "repetition", "S023: Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S024", "X", "L", "repetition", "S002: the social platform X", "high",
     None, "nền tảng X lặp (quote S002 không dịch phía VI)", 1, None, None,
     "LC", None),
    # [Phase-2] D.C. ← Washington: viết tắt đồng danh (H&H §6.2 synonym,
    # như GOP ← Republicans) — VI hiện thực hóa 'thủ đô Washington'
    # (S022 TT) trong cùng chuỗi.
    ("S024", "D.C.", "L", "synonym", "S017: Washington policies", "med",
     None,
     "D.C. = Washington D.C. (viết tắt); VI dùng trường 'thủ đô "
     "Washington'", 1, None, None, "LC", None),
    # S025 — quote Taylor
    ("S025", "You", "R", "personal", "S024: addressed Bowser", "high", None,
     "người-nghe trong quote = Bowser (S024)", 1, None, None, "LC", "A"),
    ("S025", "those words", "R", "demonstrative",
     "S001: the words \"Black Lives Matter\"", "high", None,
     "hồi quy xa 24 câu về dòng chữ S001 — tie đẹp nhất cặp", 1, None, None,
     "LC", "A"),
    ("S025", "performative", "L", "repetition", "S022: performative wokeness",
     "high", None, "echo nguyên văn từ quote chi nhánh", 1, None, None,
     "LC", None),
    ("S025", "painting", "L", "repetition", "S018: street painting", "high",
     None, "You painting those words — gerund, cùng chuỗi tranh", 1, None,
     None, "LC", None),
]

TT = [
    # S002–S003: quote Bowser giữ nguyên TIẾNG ANH trong nguồn — không đánh tie VI.
    # S004
    ("S004", "Động thái này", "R", "demonstrative",
     "S001: bắt đầu xóa bỏ dòng chữ", "high", None,
     "chỉ từ 'này' hồi quy về sự kiện xóa tranh", 1, None, None, "LC", "A"),
    ("S004", "Bowser", "L", "repetition", "S001: Muriel Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S004", "Trump", "L", "repetition", "S001: Tổng thống Donald Trump",
     "high", None, "VI thêm danh xưng 'ông'", 1, None, None, "LC", None),
    ("S004", "đảng viên Cộng hòa", "L", "repetition", "S001: Đảng Cộng hòa",
     "high", None, None, 1, None, None, "LC", None),
    ("S004", "Quốc hội", "L", "repetition", "S001: Quốc hội", "high", None,
     None, 1, None, None, "LC", None),
    # S005
    ("S005", "dòng chữ vừa kể", "R", "demonstrative", "S001: dòng chữ lớn",
     "high", None,
     "'vừa kể' = dấu hiệu hồi quy; đồng thời lặp 'dòng chữ'", 1, None, None,
     "LC", "A"),
    ("S005", "giao lộ này", "R", "demonstrative", "S001: một con đường",
     "high", None, "hậu chỉ từ 'này' về địa điểm", 1, None, None, "LC", "A"),
    ("S005", "Bowser", "L", "repetition", "S004: Bowser", "high", None,
     "VI thêm danh xưng 'Bà'", 1, None, None, "LC", None),
    ("S005", "Mạng sống người da đen quan trọng", "L", "repetition",
     "S001: Mạng sống của người da đen quan trọng", "high", None,
     "bỏ 'của' so với S001", 1, None, None, "LC", None),
    # [Phase-2 lượt 2] đảng viên Dân chủ ↔ S004 đảng viên Cộng hòa: phép đối
    # liên câu (TNT §30; H&H §6.4 — protocol nhóm 2); đối xứng EN "a
    # Democrat" ↔ "congressional Republicans" (S005/S004 ST).
    ("S005", "đảng viên Dân chủ", "L", "antonym",
     "S004: các đảng viên Cộng hòa", "med", None,
     "phép đối Dân chủ ↔ Cộng hòa qua câu (TNT §30); đối xứng EN 'a "
     "Democrat' (S005 ST)", 1, None, None, "LC", None),
    # [Phase-2] kẻ ← S001 xóa bỏ: phép đối liên câu (TNT §30; H&H §6.4
    # opposites) — kẻ (vẽ) ↔ xóa bỏ: dòng chữ được kẻ năm 2020 nay bị xóa;
    # EN không có cặp động từ (S005 dùng danh hóa "the painting").
    ("S005", "kẻ", "L", "antonym",
     "S001: bắt đầu xóa bỏ dòng chữ lớn", "med", None,
     "phép đối kẻ ↔ xóa bỏ qua câu (TNT §30); bản dịch tự sinh động từ "
     "'kẻ' cho 'painting' (NTT 2020 §2.1: VI hiện thực hóa bằng từ vựng)",
     1, None, None, "LC", None),
    # S006
    ("S006", "Việc này", "R", "demonstrative",
     "S005: hành động phản kháng công khai", "high", None,
     "đối ứng EN S006 'It'", 1, None, None, "LC", "A"),
    ("S006", "địa điểm này", "R", "demonstrative", "S005: giao lộ này",
     "high", None, "đối ứng EN 'that location'", 1, None, None, "LC", "A"),
    ("S006", "người da đen", "L", "repetition",
     "S001: người da đen", "high", None,
     "một người da đen tên George Floyd — referent khác S001 (trong tên "
     "slogan); VI tự sinh lặp 'người da đen', EN chỉ dùng tên riêng",
     1, None, None, "LC", None),
    # S007
    ("S007", "Bowser", "L", "repetition", "S005: Bà Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S007", "biểu tình", "L", "repetition", "S006: biểu tình hỗn loạn",
     "high", None, None, 1, None, None, "LC", None),
    ("S007", "Trump", "L", "repetition", "S004: ông Trump", "high", None,
     None, 1, None, None, "LC", None),
    ("S007", "nhiệm kỳ đầu", "L", "repetition", "S004: nhiệm kỳ đầu", "high",
     None,
     "VI tự sinh nhắc lại; EN chỉ có 'at the time' — mắt xích VI-only", 1,
     None, None, "LC", None),
    # S008
    ("S008", "Trump", "L", "repetition", "S007: Tổng thống Trump", "high",
     None, "đối ứng EN 'The president' (danh ngữ xác định)", 1, None, None,
     "LC", None),
    ("S008", "Bowser", "L", "repetition", "S007: bà Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S008", "đe dọa", "L", "repetition", "S001: các mối đe dọa", "high",
     None, "chuỗi đe dọa", 1, None, None, "LC", None),
    # [Phase-2 lượt 2] kiểm soát ← S001 kiểm soát: mắt xích sót chuỗi kiểm
    # soát (H&H §6.2; TNT §26 — protocol nhóm 4/12): 'mất kiểm soát thành
    # phố' lặp kiểm soát (S001) nhưng referent khác (bà Bowser mất kiểm
    # soát ↔ đảng kiểm soát Quốc hội); chuỗi S001→S008→S015 giờ kín.
    ("S008", "kiểm soát", "L", "repetition",
     "S001: Đảng Cộng hòa kiểm soát", "med", None,
     "lặp kiểm soát ('mất kiểm soát thành phố'); referent khác S001 — TNT "
     "§26 phép lặp; nối kín chuỗi kiểm soát 3 mắt (S001→S008→S015)", 1,
     None, None, "LC", None),
    ("S008", "Cảnh sát", "L", "repetition", "S006: cảnh sát", "high", None,
     "Sở Cảnh sát Đô thị", 1, None, None, "LC", None),
    # [Phase-2] tiếp quản ← S001 can thiệp: mắt xích đầu chuỗi tiếp quản
    # (S012 cite S008) — đe dọa can thiệp cụ thể hóa thành tiếp quản (H&H
    # §6.2 synonym); đối xứng EN take over ← encroachment.
    ("S008", "tiếp quản", "L", "synonym",
     "S001: các mối đe dọa can thiệp", "med", None,
     "tiếp quản = hình thức cụ thể của đe dọa can thiệp (S001); mở chuỗi "
     "tiếp quản cho S012", 1, None, None, "LC", None),
    # S009
    ("S009", "Tuy nhiên", "C", "adversative",
     "S008: đe dọa sử dụng quyền lực để tiếp quản", "high", None,
     "EN 'but' NỘI CÂU (didn't ... but declared) → VI nâng lên đầu câu thành liên kết LIÊN CÂU — dịch chuyển nổi bật",
     1, None, None, "LC", None),
    ("S009", "ông", "R", "personal", "S008: Ông Trump", "high", None,
     "VI giữ đại từ như EN 'He'", 1, None, None, "LC", "A"),
    ("S009", "lời đe dọa", "L", "repetition", "S008: đe dọa", "high", None,
     "'để đe dọa những người biểu tình' lần 2 trong câu, cùng chuỗi, ghi note",
     1, None, None, "LC", None),
    ("S009", "người biểu tình", "L", "repetition", "S007: biểu tình", "high",
     None, "biểu tình → người biểu tình", 1, None, None, "LC", None),
    # S010
    ("S010", "nhiệm kỳ", "L", "repetition", "S007: nhiệm kỳ đầu", "high",
     None, "đối 'đầu' ↔ 'thứ hai'", 1, None, None, "LC", None),
    # [Phase-2 lượt 2] cố gắng ← S001 cố gắng: lặp động từ (H&H §6.2; TNT
    # §26 — protocol nhóm 4): EN đổi từ (struggles → has worked) nên đây là
    # mắt xích VI-only — VI lặp từ nơi EN đổi từ (NTT 2020 §2.1).
    ("S010", "cố gắng", "L", "repetition",
     "S001: cố gắng chống lại các mối đe dọa", "med", None,
     "lặp cố gắng; EN struggles (S001) ↔ has worked (S010) — VI lặp từ nơi "
     "EN đổi từ (NTT 2020 §2.1)", 1, None, None, "LC", None),
    ("S010", "Trump", "L", "repetition", "S008: Ông Trump", "high", None,
     None, 1, None, None, "LC", None),
    ("S010", "Bowser", "L", "repetition", "S008: bà Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S010", "xung đột", "L", "repetition", "S007: xung đột trực tiếp",
     "high", None, None, 1, None, None, "LC", None),
    # S011
    ("S011", "Bà", "R", "personal", "S010: bà Bowser", "high", None,
     "đối ứng EN 'She'", 1, None, None, "LC", "A"),
    ("S011", "Trump", "L", "repetition", "S010: ông Trump", "high", None,
     None, 1, None, None, "LC", None),
    ("S011", "tổng thống", "L", "repetition", "S007: Tổng thống Trump",
     "high", None, "gặp gỡ tổng thống — danh ngữ xác định", 1, None, None,
     "LC", None),
    # [Phase-2] đồng thuận ← S010 tranh cãi: phép đối liên câu (TNT §30;
    # H&H §6.4 opposites) — đối xứng EN points of agreement ↔ points of
    # contention (S011 ST); mở chuỗi nhất trí (S017).
    ("S011", "đồng thuận", "L", "antonym",
     "S010: các vấn đề tranh cãi", "high", None,
     "phép đối tranh cãi ↔ đồng thuận ('các điểm đồng thuận của họ')", 1,
     None, None, "LC", None),
    # S012
    ("S012", "Trump", "L", "repetition", "S011: ông Trump", "high", None,
     None, 1, None, None, "LC", None),
    ("S012", "tiếp quản", "L", "repetition", "S008: tiếp quản", "high", None,
     "echo 1–1 với EN take over → takeover", 1, None, None, "LC", None),
    ("S012", "Washington", "L", "repetition", "S001: đô trưởng Washington",
     "high", None,
     "'thủ đô quốc gia'/'thủ đô' trong cùng câu là đồng nghĩa, không đánh thêm",
     1, None, None, "LC", None),
    # [Phase-2] dòng chữ ← S005 dòng chữ: lặp từ vựng với referent khác
    # (graffiti ≠ tranh BLM) (H&H §6.2; TNT §26 phép lặp) — EN dùng từ
    # mới 'graffiti' không lặp: VI lặp từ nơi EN đổi từ (NTT 2020 §2.1).
    ("S012", "dòng chữ", "L", "repetition",
     "S005: kẻ dòng chữ vừa kể", "med", None,
     "'dòng chữ vẽ bậy' lặp từ 'dòng chữ' nhưng chỉ graffiti — referent "
     "khác, ghi nhận phép lặp từ vựng thuần túy", 1, None, None, "LC",
     None),
    # S013 — EN S013 tách thành TT S013+S014
    ("S013", "Bowser", "L", "repetition", "S010: bà Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S013", "Tòa Bạch Ốc", "L", "repetition", "S001: Tòa Bạch Ốc", "high",
     None, "ẩn dụ chỉ chính quyền liên bang", 1, None, None, "LC", None),
    ("S013", "thủ đô Washington", "L", "repetition", "S012: thủ đô Washington",
     "high", None, None, 1, None, None, "LC", None),
    # S014
    ("S014", "Bà", "R", "personal", "S013: Bà Bowser", "high", None,
     "đối ứng EN 'she' (EN giữ trong câu bằng ';', VI tách câu nên thành liên câu)",
     1, None, None, "LC", "A"),
    ("S014", "mối đe dọa", "L", "repetition", "S008: đe dọa", "high", None,
     "mối đe dọa lớn nhất — chuỗi đe dọa", 1, None, None, "LC", None),
    ("S014", "thủ đô Washington", "L", "repetition", "S013: thủ đô Washington",
     "high", None, None, 1, None, None, "LC", None),
    ("S014", "Quốc hội", "L", "repetition", "S004: Quốc hội", "high", None,
     "một số người trong Quốc hội", 1, None, None, "LC", None),
    # S015
    ("S015", "đảng viên Cộng hòa", "L", "repetition",
     "S004: các đảng viên Cộng hòa", "high", None, None, 1, None, None,
     "LC", None),
    ("S015", "Quốc hội", "L", "repetition", "S014: Quốc hội", "high", None,
     "cả hai viện Quốc hội", 1, None, None, "LC", None),
    ("S015", "đe dọa", "L", "repetition", "S014: mối đe dọa", "high", None,
     "nhiều lần đe dọa can thiệp", 1, None, None, "LC", None),
    # [Phase-2] kiểm soát ← S001 kiểm soát: lặp động từ qua câu (H&H §6.2;
    # TNT §26) — đối xứng EN control ← Republican-controlled (S014 ST).
    ("S015", "kiểm soát", "L", "repetition",
     "S001: Quốc hội do Đảng Cộng hòa kiểm soát", "high", None,
     "'phe đang kiểm soát': lặp kiểm soát (S001) — trùng referent S001; "
     "'mất kiểm soát' (S008) cùng hình vị nhưng referent khác (bà Bowser), "
     "chọn tiền trạm theo referent (precedent graffiti S012)", 1, None,
     None, "LC", None),
    # [Phase-2] can thiệp ← S001 can thiệp: lặp động từ qua câu (H&H
    # §6.2) — mắt xích VI của chuỗi xâm phạm; EN đối ứng 'interfere'
    # (S014) nối về 'interference' trong quote S002.
    ("S015", "can thiệp", "L", "repetition",
     "S001: các mối đe dọa can thiệp", "high", None,
     "'đe dọa can thiệp': lặp can thiệp (S001)", 1, None, None, "LC",
     None),
    ("S015", "thủ đô Washington", "L", "repetition",
     "S014: thủ đô Washington", "high", None, None, 1, None, None, "LC",
     None),
    # S016
    ("S016", "Quốc hội", "L", "repetition", "S015: Quốc hội", "high", None,
     "đưa ra tại Quốc hội", 1, None, None, "LC", None),
    ("S016", "Bowser", "L", "repetition", "S013: Bà Bowser", "high", None,
     "đạo luật mang tên đô trưởng", 1, None, None, "LC", None),
    ("S016", "Tự quản", "L", "repetition", "S014: quyền tự trị", "high", None,
     "Đạo luật Tự quản ↔ quyền tự trị (cùng hình vị tự + quản/trị)", 1,
     None, None, "LC", None),
    ("S016", "thủ đô", "L", "repetition", "S015: thủ đô Washington", "high",
     None, "vùng thủ đô", 1, None, None, "LC", None),
    ("S016", "quyền tự trị", "L", "repetition", "S014: quyền tự trị", "high",
     None, "quyền tự trị có giới hạn", 1, None, None, "LC", None),
    # S017
    ("S017", "đô trưởng Bowser", "L", "repetition",
     "S001: đô trưởng Washington, Muriel Bowser", "high", None,
     "lặp cả danh hiệu 'đô trưởng' (hồi quy xa về S001)", 1, None, None,
     "LC", None),
    ("S017", "Trump", "L", "repetition", "S012: Tổng thống Trump", "high",
     None, "lần 2 trong câu (ông Trump thúc đẩy) ghi note", 1, None, None,
     "LC", None),
    ("S017", "nhân viên chính phủ liên bang", "L", "repetition",
     "S011: nhân viên liên bang", "high", None,
     "thêm 'chính phủ' so với S011; 'lực lượng lao động liên bang' có hàng "
     "riêng (lượt 2)",
     1, None, None, "LC", None),
    # [Phase-2 lượt 2] lực lượng lao động ← S011 nhân viên liên bang: thế
    # đẳng nghĩa (TNT §31; H&H §6.2 synonym) — đối xứng chuẩn EN "federal
    # workforce" ← "federal workers" (S019 ST đánh 2 hàng cho 2 lexeme);
    # trước ghi note "lần 2 trong câu" nhưng đây là lexeme khác nên có hàng
    # riêng theo mẫu S019 ST.
    ("S017", "lực lượng lao động", "L", "synonym",
     "S011: nhân viên liên bang", "med", None,
     "lực lượng lao động ≈ nhân viên (TNT §31 → L); đối xứng EN federal "
     "workforce ← federal workers (S019 ST)", 1, None, None, "LC", None),
    # [Phase-2] nhất trí ← S011 đồng thuận: thế đẳng nghĩa (TNT §31; H&H
    # §6.2 synonym) — VI đổi từ trong chuỗi (không lặp nguyên 'đồng
    # thuận'); đối xứng EN agreed ← agreement (S019 ST).
    ("S017", "nhất trí", "L", "synonym",
     "S011: các điểm đồng thuận của họ", "med", None,
     "nhất trí ≈ đồng thuận: cùng trường 'thống nhất' — VI đổi từ, EN lặp "
     "hình vị", 1, None, None, "LC", None),
    # [Phase-2] trở lại ← S011 trở lại làm việc: lặp động từ (H&H §6.2) —
    # đối xứng EN returning ← return (S019 ST).
    ("S017", "trở lại", "L", "repetition",
     "S011: trở lại làm việc tại văn phòng", "high", None,
     "'phải trở lại làm việc': lặp cụm 'trở lại làm việc' (S011)", 1, None,
     None, "LC", None),
    ("S017", "văn phòng toàn thời gian", "L", "repetition",
     "S011: văn phòng toàn thời gian", "high", None, None, 1, None, None,
     "LC", None),
    ("S017", "thành phố", "L", "repetition", "S008: thành phố", "med", None,
     "gây sóng gió tài chính cho thành phố", 1, None, None, "LC", None),
    # S018
    ("S018", "thành phố", "L", "repetition", "S017: thành phố", "med", None,
     "giám đốc tài chính của thành phố", 1, None, None, "LC", None),
    ("S018", "tài chính", "L", "repetition", "S017: sóng gió tài chính",
     "med", None, "giám đốc tài chính", 1, None, None, "LC", None),
    # [Phase-2] mất mát ← S017 cắt giảm: collocation quá trình–kết quả
    # (H&H §6.4) — đối xứng EN loss ← slash (S020 ST).
    ("S018", "mất mát", "L", "collocation",
     "S017: cắt giảm lực lượng lao động liên bang", "med", None,
     "'mất mát hàng ngàn công chức' = kết quả của 'cắt giảm'", 1, None,
     None, "LC", None),
    ("S018", "công chức", "L", "synonym",
     "S017: nhân viên chính phủ liên bang", "med", None,
     "VI đổi từ: nhân viên → công chức", 1, None, None, "LC", None),
    ("S018", "chính phủ liên bang", "L", "repetition",
     "S017: nhân viên chính phủ liên bang", "high", None,
     "từ chính phủ liên bang", 1, None, None, "LC", None),
    # S019
    ("S019", "Bowser", "L", "repetition", "S017: đô trưởng Bowser", "high",
     None, None, 1, None, None, "LC", None),
    ("S019", "Mạng sống người da đen quan trọng", "L", "repetition",
     "S005: Mạng sống người da đen quan trọng", "high", None, None, 1, None,
     None, "LC", None),
    # S020
    ("S020", "Chi nhánh phong trào này", "R", "demonstrative",
     "S019: các nhà hoạt động \"Mạng sống người da đen quan trọng\"", "high",
     None,
     "'này' hồi quy; 'phong trào' là danh từ mới chỉ BLM", 1, None, None,
     "LC", "A"),
    ("S020", "động thái", "L", "repetition", "S004: Động thái này", "high",
     None,
     "lặp từ; EN đối ứng 'the move' (S022) là quy chiếu — dịch chuyển", 1,
     None, None, "LC", None),
    ("S020", "Bowser", "L", "repetition", "S019: bà Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S020", "cảnh sát", "L", "repetition", "S008: Cảnh sát", "high", None,
     "thiên vị cảnh sát", 1, None, None, "LC", None),
    # S021
    ("S021", "Những nhà hoạt động này", "R", "demonstrative",
     "S019: các nhà hoạt động", "high", None,
     "'này' + lặp danh từ; EN đối ứng 'The same activists' (comparative)",
     1, None, None, "LC", "A"),
    # [Phase-2 lượt 2] lên án ← S020 tố cáo/chỉ trích: thế đẳng nghĩa liên
    # câu (TNT §31; H&H §6.2 — protocol nhóm 4): 'tiếp tục' (VI tự sinh)
    # đánh dấu nối tiếp hành động phê phán; EN đối xứng heaped scorn ←
    # decried (S023 ST).
    ("S021", "lên án", "L", "synonym",
     "S020: tố cáo ... chỉ trích bà", "med", None,
     "lên án ≈ tố cáo/chỉ trích (TNT §31 → L); 'tiếp tục' VI tự sinh đánh "
     "dấu nối tiếp; EN heaped scorn ← decried (S023 ST)", 1, None, None,
     "LC", None),
    ("S021", "Bowser", "L", "repetition", "S020: bà Bowser", "high", None,
     None, 1, None, None, "LC", None),
    ("S021", "thay đổi", "L", "repetition", "S004: sự thay đổi đáng kể",
     "med", None,
     "hồi quy xa về S004; 'lập trường' ≈ 'thái độ' (S004) đồng nghĩa; EN "
     "'reversal' (S023 ST) Phase-2 cũng chốt về S004 'shift'", 1, None,
     None, "LC", None),
    # S022
    ("S022", "chi nhánh phong trào", "L", "repetition",
     "S020: Chi nhánh phong trào này", "high", None, None, 1, None, None,
     "LC", None),
    ("S022", "Mạng sống người da đen quan trọng", "L", "repetition",
     "S019: Mạng sống người da đen quan trọng", "high", None,
     "trong tên chi nhánh; lần 2 trong quote ('Mạng sống của người...') có thêm 'của', ghi note",
     1, None, None, "LC", None),
    ("S022", "thủ đô Washington", "L", "repetition", "S016: vùng thủ đô",
     "high", None, None, 1, None, None, "LC", None),
    ("S022", "X", "L", "repetition", "S002: the social platform X", "med",
     None,
     "viết trên X — nền tảng lặp từ khối quote chưa dịch (giữ nguyên EN)",
     1, None, None, "LC", None),
    ("S022", "Bà", "R", "personal", "S021: bà Bowser", "high", None,
     "người được xưng hô trong quote Taylor = Bowser", 1, None, None, "LC",
     "A"),
    # S023
    ("S023", "bà", "R", "personal", "S022: Bà (quote)", "high", None,
     "tiếp tục chuỗi người được xưng hô; EN đối ứng 'You'", 1, None, None,
     "LC", "A"),
    ("S023", "dòng chữ", "L", "repetition", "S005: dòng chữ vừa kể", "high",
     None,
     "kẻ dòng chữ này; đối ứng EN 'those words' hồi quy S001", 1, None,
     None, "LC", None),
    ("S023", "trình diễn", "L", "synonym", "S020: diễn kịch", "med", None,
     "diễn kịch ↔ trình diễn; EN lặp nguyên văn 'performative'", 1, None,
     None, "LC", None),
    # [Phase-2] kẻ ← S005 kẻ: lặp động từ (H&H §6.2; TNT §26) — tiếp phép
    # đối kẻ ↔ xóa bỏ (S001) đã mở ở S005.
    ("S023", "kẻ", "L", "repetition", "S005: ra lệnh kẻ dòng chữ", "high",
     None,
     "'cho kẻ dòng chữ này': lặp kẻ; tiếp chuỗi phép đối kẻ ↔ xóa bỏ "
     "(TNT §30)", 1, None, None, "LC", None),
]
