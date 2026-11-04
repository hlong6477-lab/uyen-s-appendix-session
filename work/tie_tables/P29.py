# P29 tie table — WRITTEN BY HAND FROM work/analysis/P29_semantic.md.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
#
# Cặp SBS EN→VI về giá nhà Úc. Đặc thù P29:
# - 7 dòng EN bị cắt (S002, S008, S011, S015, S016 subhead, S022, S025):
#   tie ở đó là EN-only, ghi chú "không có bản dịch".
# - VI tự sinh câu S002 "Tuy nhiên có một số thành phố lại đi ngược xu hướng."
# - Bẫy occ: EN S005 "he" xuất hiện 3 lần dưới dạng chuỗi (2 lần bên trong
#   "the") → occ=3; "growth" S022 ×2; "stock levels" S012 ×2; VI "mức giảm"
#   S008 ×2, "thị trường" S011 ×2, "tăng" S014 ×2, "giảm" S015 ×3,
#   "mức tăng" S017 ×3, "giảm" S021 ×2 → occ=1 (lần đầu).
# - Động từ khung reveals/shows/cho thấy và experienced KHÔNG lập tie (§6).
# - Subhead (EN S007/S016/S023, VI S007/S018) raw, không tie.
# - [Phase-2] theo PHASE2_PROTOCOL.md: +6 hàng EN / +6 hàng VI (mỗi hàng có
#   comment [Phase-2] kèm căn cứ references ngay phía trên).

ST = [
    # S002 — dòng cắt (ô VI trống): nội dung "Nearly two years ... ended"
    # được VI hút vào S001 (xem phân tích §1/§8).
    ("S002", "home prices", "L", "synonym",
     "S001: home values", "high", None,
     "không có bản dịch; chuỗi GIÁ đổi đầu từ values → prices", 1,
     None, None, "LC", None),
    ("S002", "new data", "L", "repetition",
     "S001: New data reveals", "high", None,
     "không có bản dịch; lặp 'data'", 1, None, None, "LC", None),
    ("S002", "decline", "L", "synonym",
     "S001: decreased", "high", None,
     "không có bản dịch; chuỗi GIẢM (decreased → decline)", 1, None,
     None, "LC", None),
    # S003
    ("S003", "home values", "L", "repetition",
     "S002: home prices", "high", None,
     "chuỗi GIÁ luân phiên values/prices; 'prices stalling' trong câu "
     "không đánh thêm ('price increases' có hàng riêng chuỗi TĂNG — "
     "Phase-2)", 1, None, None, "LC", None),
    ("S003", "dropped", "L", "synonym",
     "S002: a national decline", "high", None,
     "chuỗi GIẢM: decline → dropped", 1, None, None, "LC", None),
    # [Phase-2] price increases ← rising (S002): mắt xích chuỗi TĂNG bị sót
    # (H&H §6.2 reiteration; TNT §26 phép lặp) — danh từ hóa "increases"
    # nối rising (S002) → Growth (S006); VI đối ứng "tăng" (S003 TT) đã có
    # hàng riêng, thêm hàng này để chuỗi TĂNG liền mạch hai đầu.
    ("S003", "price increases", "L", "synonym",
     "S002: rising home prices", "high", None,
     "chuỗi TĂNG: rising → price increases (danh từ hóa); đầu từ là TĂNG "
     "nên tách khỏi chuỗi GIÁ trong câu", 1, None, None, "LC", None),
    # S004
    ("S004", "CoreLogic", "L", "repetition",
     "S003: property analytics provider CoreLogic", "high", None,
     "lần đầu là S003; 'he' trong câu (Tim Lawless cùng câu) không đánh "
     "theo quy ước liên câu", 1, None, None, "LC", None),
    ("S004", "the latest data", "L", "repetition",
     "S002: new data", "high", None,
     "chuỗi data: 'new' đổi thành 'the latest'", 1, None, None, "LC",
     None),
    # S005
    ("S005", "This result", "R", "demonstrative",
     "S001-S003: giá trị nhà giảm trong tháng 12 (kết quả số liệu)",
     "high", None,
     "chỉ từ + danh từ tổng quát tóm tình huống mở bài; VI 'Kết quả này' "
     "song song", 1, None, None, "LC", "A"),
    ("S005", "he", "R", "personal", "S004: Tim Lawless", "high", None,
     "đại từ trong attribution 'he said'; occ 3 vì 'he' trùng chuỗi bên "
     "trong 'the' ×2 trong câu", 3, None, None, "LC", "A"),
    ("S005", "the housing market", "L", "repetition",
     "S001: the \"market [is] catching up", "med", None,
     "đầu ngữ 'market' lặp từ quote mở bài (thêm 'housing'); VI không có "
     "vì VI S001 đã cắt quote", 1, None, None, "LC", None),
    ("S005", "the reality of market dynamics", "L", "repetition",
     "S001: the reality of market dynamics", "high", None,
     "echo gần nguyên văn cụm quote mở bài", 1, None, None, "LC", None),
    # S006
    ("S006", "housing values", "L", "repetition",
     "S003: home values", "high", None,
     "chuỗi GIÁ (values); 'housing' lặp từ S005 'housing market'", 1,
     None, None, "LC", None),
    ("S006", "Growth", "L", "repetition",
     "S002: rising home prices", "med", None,
     "chuỗi TĂNG: rising → Growth", 1, None, None, "LC", None),
    # S008 — dòng cắt
    ("S008", "CoreLogic", "L", "repetition",
     "S004: CoreLogic's research director", "high", None,
     "không có bản dịch", 1, None, None, "LC", None),
    # [Phase-2] data ← the latest data (S004): mắt xích chuỗi data được
    # "The data" (S017) cite làm tiền trạm nhưng chính nó chưa có hàng —
    # rà chuỗi ngược "ante không có hàng" (bài học P28, nhóm 12 checklist;
    # H&H §6.2 reiteration; TNT §26 phép lặp).
    ("S008", "data", "L", "repetition",
     "S004: the latest data", "high", None,
     "không có bản dịch; chuỗi data: new data (S001) → new data (S002) → "
     "the latest data (S004) → data (S008) → The data (S017)", 1, None,
     None, "LC", None),
    ("S008", "house prices", "L", "synonym",
     "S006: housing values", "high", None,
     "không có bản dịch; chuỗi GIÁ quay về 'prices'", 1, None, None,
     "LC", None),
    ("S008", "fell", "L", "synonym", "S003: dropped", "high", None,
     "không có bản dịch; chuỗi GIẢM", 1, None, None, "LC", None),
    # S009
    ("S009", "drop", "L", "synonym", "S008: fell", "high", None,
     "'decreasing' và 'decline' trong câu cùng chuỗi GIẢM, không đánh "
     "thêm", 1, None, None, "LC", None),
    ("S009", "home values", "L", "synonym",
     "S008: house prices", "high", None,
     "chuỗi GIÁ: prices → values", 1, None, None, "LC", None),
    ("S009", "housing market", "L", "repetition",
     "S005: the housing market", "high", None,
     "appositive 'Australia's largest housing market'", 1, None, None,
     "LC", None),
    ("S009", "Australia's", "L", "repetition",
     "S001: across Australia", "high", None,
     "chuỗi nước Úc (khác chuỗi tên bang Western/South Australia)", 1,
     None, None, "LC", None),
    # S010
    ("S010", "Meanwhile", "C", "temporal",
     "S009: Melbourne experienced the largest drop", "high", None,
     "đối lập giảm (S009) với tăng (S010); VI 'Trong khi đó' song song",
     1, None, None, "LC", None),
    ("S010", "values", "L", "repetition", "S009: home values", "high",
     None, "chuỗi GIÁ", 1, None, None, "LC", None),
    ("S010", "increased", "L", "repetition",
     "S006: Growth in housing values", "high", None,
     "chuỗi TĂNG; liệt kê dùng chung một động từ nên EN không có ∅", 1,
     None, None, "LC", None),
    # S011 — dòng cắt
    ("S011", "capital city", "L", "repetition",
     "S008: all five largest capital cities", "high", None,
     "không có bản dịch; chuỗi thủ phủ (chỉ tồn tại phía EN)", 1, None,
     None, "LC", None),
    ("S011", "Adelaide", "L", "repetition", "S010: Adelaide", "high",
     None, "không có bản dịch", 1, None, None, "LC", None),
    ("S011", "Perth", "L", "repetition", "S010: Perth", "high", None,
     "không có bản dịch", 1, None, None, "LC", None),
    ("S011", "market", "L", "repetition", "S009: housing market", "high",
     None, "không có bản dịch; 'the strongest market' — danh từ tổng quát "
     "trong chuỗi thị trường", 1, None, None, "LC", None),
    ("S011", "also", "C", "additive",
     "S010: values increased in Adelaide, Brisbane and Perth", "med",
     None,
     "không có bản dịch; nối cộng thêm với diễn biến giá tháng 12", 1,
     None, None, "LC", None),
    # S012
    ("S012", "stock levels", "L", "repetition",
     "S006: advertised supply levels", "high", None,
     "chuỗi cung: supply → stock; lần 2 'with stock levels tracking' "
     "trong câu không đánh thêm", 1, None, None, "LC", None),
    ("S012", "growth", "L", "repetition", "S010: increased", "high",
     None, "chuỗi TĂNG ('strong growth conditions')", 1, None, None,
     "LC", None),
    ("S012", "Adelaide", "L", "repetition", "S011: Adelaide", "high",
     None, None, 1, None, None, "LC", None),
    ("S012", "decrease", "L", "synonym",
     "S009: the largest drop", "med", None,
     "chuỗi GIẢM dùng cho số lượng nhà (khác giá) — vẫn cùng trường từ "
     "vựng", 1, None, None, "LC", None),
    ("S012", "Lawless", "L", "repetition", "S004: Tim Lawless", "high",
     None, "đặt lại tên nhân vật sau quote", 1, None, None, "LC", None),
    # S013
    ("S013", "on the other hand", "C", "adversative",
     "S012: Extremely low advertised stock levels ... across Adelaide",
     "high", None,
     "đối lập Adelaide (ít hàng) ↔ Perth (nhiều hàng); VI 'Mặt khác' "
     "song song", 1, None, None, "LC", None),
    ("S013", "Perth", "L", "repetition", "S011: Perth", "high", None,
     None, 1, None, None, "LC", None),
    ("S013", "advertised supply", "L", "synonym",
     "S012: advertised stock levels", "high", None,
     "chuỗi cung: stock → supply", 1, None, None, "LC", None),
    ("S013", "buyers", "L", "repetition",
     "S006: buyer demand", "high", None,
     "chuỗi người mua: buyer → buyers", 1, None, None, "LC", None),
    # [Phase-2] more ← S012: quy chiếu so sánh lượng (H&H §2.5 more/less) —
    # chuẩn so sánh là tình trạng nguồn cung cực thấp đã nêu ở CÂU TRƯỚC
    # (S012), không nằm trong câu; VI đối ứng "nhiều ... hơn" (S012 TT).
    ("S013", "more", "R", "comparative",
     "S012: Extremely low advertised stock levels", "med", None,
     "[LC] more choice = nhiều lựa chọn hơn so với khi nguồn cung cực "
     "thấp (S012); H&H §2.5", 1, None, None, "LC", "A"),
    # [Phase-2] less ← S012: quy chiếu so sánh lượng (H&H §2.5) — cùng
    # chuẩn so sánh với hàng "more" trên; VI đối ứng "ít ... hơn".
    ("S013", "less", "R", "comparative",
     "S012: Extremely low advertised stock levels", "med", None,
     "[LC] less urgency = ít cấp bách hơn so với khi nguồn cung cực thấp "
     "(S012); H&H §2.5", 1, None, None, "LC", "A"),
    ("S013", "value growth", "L", "repetition",
     "S012: strong growth conditions", "high", None,
     "chuỗi TĂNG; 'slowdown' là nghĩa GIẢM kề bên, không đánh", 1,
     None, None, "LC", None),
    ("S013", "Adelaide", "L", "repetition", "S012: across Adelaide",
     "high", None, None, 1, None, None, "LC", None),
    ("S013", "Lawless", "L", "repetition", "S012: Lawless said", "high",
     None, "lặp tên trong attribution", 1, None, None, "LC", None),
    # S014
    # [Phase-2] another ← S010: quy chiếu so sánh "other" (H&H §2.5) —
    # Darwin là thành phố KHÁC với nhóm thành phố tăng giá đã nêu ở câu
    # trước; VI đối ứng "một thành phố khác" (S013 TT).
    ("S014", "another", "R", "comparative",
     "S010: values increased in Adelaide, Brisbane and Perth", "high",
     None,
     "[LC] another city = một thành phố khác (ngoài Adelaide/Brisbane/"
     "Perth tăng giá ở S010); H&H §2.5 other", 1, None, None, "LC", "A"),
    ("S014", "city", "L", "repetition",
     "S011: capital city rankings", "med", None,
     "'another city' nối chuỗi city; câu EN gãy bằng dấu phẩy (xem §8)",
     1, None, None, "LC", None),
    ("S014", "growth", "L", "repetition", "S013: value growth", "high",
     None, "chuỗi TĂNG", 1, None, None, "LC", None),
    # S015 — dòng cắt; bản dịch bị dịch vị vào dòng S009 (thành câu VI S009)
    ("S015", "while", "C", "adversative",
     "S014: Darwin was another city that experienced a 0.4 per cent "
     "growth", "high", None,
     "không có bản dịch; VI hiện thực hóa nội dung này bằng 'Ngoài ra' "
     "(additive) trong S009 — đổi kiểu nối + dịch vị", 1, None, None,
     "LC", None),
    ("S015", "prices", "L", "repetition", "S010: values", "high", None,
     "không có bản dịch; chuỗi GIÁ", 1, None, None, "LC", None),
    ("S015", "dropped", "L", "synonym", "S012: decrease", "high", None,
     "không có bản dịch; chuỗi GIẢM", 1, None, None, "LC", None),
    # S017
    ("S017", "The data", "L", "repetition",
     "S008: CoreLogic data", "high", None,
     "chuỗi data; VI S014 đổi thành 'Báo cáo' nên không có đối vocab",
     1, None, None, "LC", None),
    ("S017", "house prices", "L", "repetition", "S015: prices", "high",
     None,
     "chuỗi GIÁ; 'median values' cuối câu cùng chuỗi, không đánh thêm",
     1, None, None, "LC", None),
    ("S017", "rose", "L", "repetition", "S014: growth", "high", None,
     "chuỗi TĂNG", 1, None, None, "LC", None),
    # S018
    ("S018", "In contrast", "C", "adversative",
     "S017: annual house prices rose by 4.9 per cent", "high", None,
     "tương phản 2024 (4,9%) với 2023 (8,1%); VI gộp S017+S018 và đảo "
     "trật tự nên nối này mất hẳn", 1, None, None, "LC", None),
    ("S018", "CoreLogic", "L", "repetition",
     "S008: CoreLogic data", "high", None,
     "'CoreLogic's report' — lần đầu xuất hiện 'report'", 1, None,
     None, "LC", None),
    ("S018", "increase", "L", "repetition", "S017: rose", "high", None,
     "chuỗi TĂNG", 1, None, None, "LC", None),
    ("S018", "house prices", "L", "repetition",
     "S017: annual house prices", "high", None, "chuỗi GIÁ", 1, None,
     None, "LC", None),
    # S019
    ("S019", "house prices", "L", "repetition",
     "S018: increase in house prices", "high", None, "chuỗi GIÁ", 1,
     None, None, "LC", None),
    ("S019", "fell", "L", "synonym", "S015: dropped", "high", None,
     "chuỗi GIẢM; liệt kê dùng chung 'fell in' nên EN không có ∅", 1,
     None, None, "LC", None),
    ("S019", "Melbourne", "L", "repetition", "S009: Melbourne", "high",
     None, None, 1, None, None, "LC", None),
    ("S019", "Hobart", "L", "repetition", "S015: Hobart", "high", None,
     "lần đầu EN nằm trong dòng cắt S015 nhưng vẫn là tiền trạm hợp lệ",
     1, None, None, "LC", None),
    ("S019", "Canberra", "L", "repetition", "S015: Canberra", "high",
     None,
     "lần đầu EN nằm trong dòng cắt S015 nhưng vẫn là tiền trạm hợp lệ",
     1, None, None, "LC", None),
    # S020
    ("S020", "Meanwhile", "C", "temporal",
     "S019: house prices fell in Melbourne, Hobart and Canberra",
     "high", None,
     "đối lập giảm với tăng của Perth; VI 'Trong khi đó' song song", 1,
     None, None, "LC", None),
    ("S020", "Perth", "L", "repetition", "S013: Perth", "high", None,
     None, 1, None, None, "LC", None),
    ("S020", "growth", "L", "repetition", "S018: increase", "high",
     None,
     "chuỗi TĂNG ('the largest growth'); 'increase' cuối câu không đánh "
     "thêm", 1, None, None, "LC", None),
    ("S020", "the country", "L", "superordinate",
     "S009: Australia's largest housing market", "high", None,
     "danh từ tổng quát thay 'Australia'; VI 'cả nước' song song", 1,
     None, None, "LC", None),
    ("S020", "home values", "L", "synonym", "S019: house prices", "high",
     None, "chuỗi GIÁ", 1, None, None, "LC", None),
    # S021
    ("S021", "Adelaide", "L", "repetition", "S013: Adelaide", "high",
     None, None, 1, None, None, "LC", None),
    ("S021", "Brisbane", "L", "repetition", "S010: Brisbane", "high",
     None, None, 1, None, None, "LC", None),
    ("S021", "also", "C", "additive",
     "S020: Perth experienced the largest growth", "high", None,
     "nối cộng thêm với mức tăng của Perth; VI 'cũng' song song", 1,
     None, None, "LC", None),
    ("S021", "gains", "L", "synonym", "S020: growth", "high", None,
     "chuỗi TĂNG; 'rising' trong câu không đánh thêm", 1, None, None,
     "LC", None),
    ("S021", "prices", "L", "synonym", "S020: home values", "high",
     None, "chuỗi GIÁ ('with prices rising by')", 1, None, None, "LC",
     None),
    ("S021", "Darwin", "L", "repetition", "S014: Darwin", "high", None,
     "'while Darwin' là nối trong câu, không đánh", 1, None, None, "LC",
     None),
    # S022 — dòng cắt
    ("S022", "capitals", "L", "repetition",
     "S011: capital city rankings", "high", None,
     "không có bản dịch; chuỗi thủ phủ ('the mid-sized capitals')", 1,
     None, None, "LC", None),
    ("S022", "growth", "L", "repetition", "S021: gains", "high", None,
     "không có bản dịch; lần 2 'peak rate of growth' trong câu không "
     "đánh thêm", 1, None, None, "LC", None),
    # [Phase-2] peak ← peaking (S001): chuỗi danh từ hóa peaking → peak
    # (H&H §6.2 reiteration; TNT §26 phép lặp) — khoảng cách xa (S001 →
    # S022), referent khác (đỉnh giá toàn quốc ↔ đỉnh tăng trưởng của các
    # thủ phủ vừa) nên conf med; S022 là dòng cắt → tie EN-only.
    ("S022", "peak", "L", "repetition",
     "S001: after peaking in October", "med", None,
     "không có bản dịch; lặp hình vị peak qua danh từ hóa (passed their "
     "peak)", 1, None, None, "LC", None),
    ("S022", "CoreLogic", "L", "repetition",
     "S018: CoreLogic's report", "high", None,
     "không có bản dịch; 'said' là attribution không đánh; 'these "
     "markets'/'it is clear' trong câu không đánh (§4.3)", 1, None,
     None, "LC", None),
    # S024
    ("S024", "housing markets", "L", "repetition",
     "S011: the strongest market", "high", None,
     "chuỗi thị trường; 'Regional' là lần đầu thân bài chuỗi vùng", 1,
     None, None, "LC", None),
    ("S024", "also", "C", "additive",
     "S021: Adelaide and Brisbane also recorded significant gains",
     "high", None,
     "đối chiếu thị trường vùng với thủ phủ; VI 'cũng' song song", 1,
     None, None, "LC", None),
    ("S024", "increase", "L", "repetition", "S021: gains", "high", None,
     "chuỗi TĂNG", 1, None, None, "LC", None),
    ("S024", "value", "L", "repetition", "S021: prices", "high", None,
     "chuỗi GIÁ ('increase in value')", 1, None, None, "LC", None),
    # S025 — dòng cắt
    ("S025", "compared to", "C", "adversative",
     "S024: Regional housing markets also finished the year with a 0.6 "
     "per cent increase in value", "med", None,
     "không có bản dịch; nối so sánh tương phản vùng 0,6% với thủ phủ "
     "4,5%", 1, None, None, "LC", None),
    ("S025", "rise", "L", "repetition", "S024: increase", "high", None,
     "không có bản dịch; chuỗi TĂNG", 1, None, None, "LC", None),
    ("S025", "capital", "L", "repetition",
     "S022: the mid-sized capitals", "high", None,
     "không có bản dịch; chuỗi thủ phủ ('combined capital index')", 1,
     None, None, "LC", None),
    # S026
    ("S026", "The report", "L", "repetition",
     "S018: CoreLogic's report", "high", None,
     "chuỗi báo cáo; động từ khung 'shows' không đánh (§6)", 1, None,
     None, "LC", None),
    ("S026", "prices", "L", "repetition", "S024: value", "high", None,
     "chuỗi GIÁ", 1, None, None, "LC", None),
    ("S026", "increased", "L", "repetition", "S025: rise", "high", None,
     "chuỗi TĂNG; tiền trạm S025 là dòng cắt nhưng vẫn hợp lệ", 1,
     None, None, "LC", None),
    ("S026", "regional areas", "L", "repetition",
     "S024: Regional housing markets", "high", None,
     "chuỗi vùng; 'Western Australia/South Australia' là tên bang, "
     "không tính chuỗi nước Úc", 1, None, None, "LC", None),
    # S027
    ("S027", "Regional", "L", "repetition",
     "S026: regional areas", "high", None,
     "chuỗi vùng ('Regional Victoria')", 1, None, None, "LC", None),
    ("S027", "markets", "L", "repetition",
     "S024: Regional housing markets", "high", None,
     "chuỗi thị trường ('\"rest of state\" markets' — VI lược cụm này)",
     1, None, None, "LC", None),
    ("S027", "drop", "L", "synonym", "S019: fell", "high", None,
     "chuỗi GIẢM; 'decline' cuối câu không đánh thêm", 1, None, None,
     "LC", None),
    ("S027", "values", "L", "repetition", "S026: prices", "high", None,
     "chuỗi GIÁ ('a drop in values')", 1, None, None, "LC", None),
]

TT = [
    # S002 — câu VI tự sinh (không có câu EN tương ứng tại vị trí này)
    ("S002", "Tuy nhiên", "C", "adversative",
     "S001: giá nhà trung bình đã bắt đầu giảm", "high", None,
     "VI tự sinh cả câu lẫn nối; phản chiếu vế 'rise in others' của "
     "subhead EN S007 nhưng đẩy lên đầu bài (xem §1)", 1, None, None,
     "LC", None),
    # [Phase-2] xu hướng ← S001: danh từ tổng quát trỏ về tình huống câu
    # trước (H&H §6.1 general word; checklist nhóm 3) — "xu hướng" = xu
    # hướng giảm giá vừa nêu; câu tự sinh nên conf med.
    ("S002", "xu hướng", "L", "general word",
     "S001: giá nhà trung bình đã bắt đầu giảm", "med", None,
     "danh từ tổng quát tóm xu hướng giảm giá của S001 (đi ngược xu "
     "hướng); EN đối ứng là subhead S007 raw nên không có tie EN", 1,
     None, None, "LC", None),
    # S003
    ("S003", "giá nhà trung bình", "L", "repetition",
     "S001: giá nhà trung bình", "high", None,
     "chuỗi GIÁ; 'và giá bắt đầu đình trệ' trong câu là chủ ngữ rút gọn "
     "đã hiện thực hóa, không có ∅", 1, None, None, "LC", None),
    ("S003", "giảm", "L", "repetition",
     "S001: đã bắt đầu giảm", "high", None, "chuỗi GIẢM", 1, None,
     None, "LC", None),
    ("S003", "tăng", "L", "repetition",
     "S001: tăng trưởng liên tục", "high", None,
     "chuỗi TĂNG ('liên tục tăng')", 1, None, None, "LC", None),
    # S004
    ("S004", "CoreLogic", "L", "repetition",
     "S003: Theo CoreLogic", "high", None, None, 1, None, None, "LC",
     None),
    ("S004", "dữ liệu mới nhất", "L", "synonym",
     "S001: Số liệu mới", "high", None,
     "chuỗi số liệu: số liệu → dữ liệu; 'ông' trong câu (Tim Lawless "
     "cùng câu) không đánh theo quy ước liên câu", 1, None, None, "LC",
     None),
    # S005
    ("S005", "Kết quả này", "R", "demonstrative",
     "S001-S003: giá nhà trung bình giảm trong tháng 12 (kết quả số "
     "liệu)", "high", None,
     "chỉ từ + danh từ tổng quát; song song EN 'This result'", 1, None,
     None, "LC", "A"),
    ("S005", "ông", "R", "personal", "S004: Tim Lawless", "high", None,
     "đại từ trong attribution 'ông nói'; tiền trạm ở câu trước", 1,
     None, None, "LC", "A"),
    # S006
    ("S006", "Tăng trưởng", "L", "repetition",
     "S003: liên tục tăng", "high", None, "chuỗi TĂNG", 1, None, None,
     "LC", None),
    ("S006", "giá nhà", "L", "repetition",
     "S003: giá nhà trung bình toàn quốc", "high", None,
     "chuỗi GIÁ; 'thị trường nhà ở'/'động lực thị trường' trong câu là "
     "lần đầu chuỗi thị trường (VI S001 đã cắt quote nên không có echo "
     "như EN)", 1, None, None, "LC", None),
    # S008
    ("S008", "mức giảm", "L", "repetition",
     "S003: đã giảm 0,1%", "high", None,
     "danh từ hóa động từ 'giảm'; lần 2 'mức giảm 0,6%' và 'giá trị nhà "
     "giảm' trong câu không đánh thêm", 1, None, None, "LC", None),
    ("S008", "giá trị nhà", "L", "synonym",
     "S006: Tăng trưởng giá nhà", "high", None,
     "chuỗi GIÁ: giá nhà → giá trị nhà", 1, None, None, "LC", None),
    ("S008", "thị trường nhà ở", "L", "repetition",
     "S005: thị trường nhà ở", "high", None,
     "chuỗi thị trường; 'Úc' lần đầu (không đánh); 'trong khi' là nối "
     "trong câu", 1, None, None, "LC", None),
    # S009 — dịch vị của dòng cắt EN S015
    ("S009", "Ngoài ra", "C", "additive",
     "S008: Melbourne ... Sydney ... có mức giảm 0,6%", "high", None,
     "VI tự sinh nối cộng thêm thay cho EN 'while' (adversative, S015) "
     "— đổi kiểu nối + dịch vị (xem §5)", 1, None, None, "LC", None),
    ("S009", "giá nhà", "L", "repetition",
     "S008: giá trị nhà", "high", None, "chuỗi GIÁ", 1, None, None,
     "LC", None),
    ("S009", "giảm", "L", "repetition", "S008: mức giảm", "high", None,
     "chuỗi GIẢM; Canberra/Hobart lần đầu nên không đánh", 1, None,
     None, "LC", None),
    # S010
    ("S010", "Trong khi đó", "C", "temporal",
     "S009: Ngoài ra giá nhà giảm 0,5 phần trăm ở Canberra và Hobart",
     "high", None,
     "song song EN 'Meanwhile' (S010)", 1, None, None, "LC", None),
    ("S010", "giá nhà", "L", "repetition", "S009: giá nhà", "high", None,
     "chuỗi GIÁ; Adelaide/Brisbane/Perth lần đầu nên không đánh", 1,
     None, None, "LC", None),
    ("S010", "tăng", "L", "repetition", "S006: Tăng trưởng", "high",
     None, "chuỗi TĂNG", 1, None, None, "LC", None),
    ("S010", None, "E", "nominal",
     "S010: giá nhà tăng 0,6% (trong câu)", "high", None,
     "[TC] tỉnh lược động từ 'tăng' trong vế tọa hợp; lỗ trống sau "
     "'Perth' tương tự không đánh thêm; EN dùng phối liệt gộp chung động "
     "từ nên không có E", 1, "Brisbane", "{tăng}", "TC", None),
    # S011
    ("S011", "Số lượng nhà", "L", "synonym",
     "S006: mức cung được quảng cáo", "med", None,
     "chuỗi cung: mức cung → số lượng nhà rao bán; lần 2 'số lượng nhà "
     "trên thị trường' trong câu không đánh thêm", 1, None, None, "LC",
     None),
    ("S011", "thị trường", "L", "repetition",
     "S008: thị trường nhà ở", "high", None,
     "lần 2 'trên thị trường' trong câu không đánh thêm", 1, None,
     None, "LC", None),
    ("S011", "tăng trưởng", "L", "repetition", "S010: tăng", "high",
     None,
     "chuỗi TĂNG ('các điều kiện tăng trưởng'); câu thiếu dấu chấm cuối "
     "(xem §8)", 1, None, None, "LC", None),
    ("S011", "Adelaide", "L", "repetition", "S010: Adelaide", "high",
     None, None, 1, None, None, "LC", None),
    ("S011", "giảm", "L", "repetition", "S009: giảm", "med", None,
     "chuỗi GIẢM dùng cho số lượng nhà (khác giá) — vẫn cùng trường từ "
     "vựng", 1, None, None, "LC", None),
    ("S011", "Lawless", "L", "repetition", "S004: Tim Lawless", "high",
     None,
     "danh xưng 'ông' + tên; 'cho biết' là attribution không đánh", 1,
     None, None, "LC", None),
    # S012
    # [retry] ante viết lại theo nguyên văn VI S011 (bản cũ trích "Extremely
    # low" — cụm tiếng Anh không có trong câu VI).
    ("S012", "Mặt khác", "C", "adversative",
     "S011: Số lượng nhà rao bán ... cực kỳ thấp ... điều kiện tăng "
     "trưởng mạnh mẽ trên khắp Adelaide", "high", None,
     "song song EN 'on the other hand' (S013); VI cắt attribution "
     "'Lawless said'", 1, None, None, "LC", None),
    ("S012", "Perth", "L", "repetition", "S010: Perth", "high", None,
     None, 1, None, None, "LC", None),
    ("S012", "nguồn cung nhà", "L", "synonym",
     "S011: Số lượng nhà rao bán", "high", None,
     "chuỗi cung: số lượng nhà → nguồn cung; 'điều này' trong câu chỉ "
     "chính mệnh đề này nên không đánh (§4.3)", 1, None, None, "LC",
     None),
    ("S012", "người mua", "L", "repetition", "S006: người mua", "high",
     None, None, 1, None, None, "LC", None),
    # [Phase-2] hơn (lần 1, "nhiều sự lựa chọn hơn") ← S011: quy chiếu so
    # sánh lượng (H&H §2.5; mapping §1 "hơn") — chuẩn so sánh là tình trạng
    # nguồn cung "cực kỳ thấp" của câu trước; đối xứng EN more (S013 ST).
    ("S012", "hơn", "R", "comparative",
     "S011: Số lượng nhà rao bán ... quảng cáo cực kỳ thấp", "med", None,
     "[LC] nhiều sự lựa chọn hơn = nhiều hơn so với khi cung cực kỳ thấp "
     "(S011); H&H §2.5", 1, None, None, "LC", "A"),
    # [Phase-2] hơn (lần 2, "ít cấp bách hơn") ← S011: cùng chuẩn so sánh;
    # lần 3 ("chậm hơn so với Adelaide") so sánh trong câu → [TC] không
    # đánh (ghi §4.3 analysis).
    ("S012", "hơn", "R", "comparative",
     "S011: Số lượng nhà rao bán ... quảng cáo cực kỳ thấp", "med", None,
     "[LC] ít cấp bách hơn = ít hơn so với khi cung cực kỳ thấp (S011); "
     "H&H §2.5; EN đối ứng less (S013 ST)", 2, None, None, "LC", "A"),
    ("S012", "giá nhà", "L", "repetition", "S010: giá nhà", "high", None,
     "chuỗi GIÁ", 1, None, None, "LC", None),
    ("S012", "tăng chậm hơn", "L", "repetition",
     "S011: các điều kiện tăng trưởng", "high", None,
     "chuỗi TĂNG; 'gia tăng' trong câu không đánh thêm", 1, None, None,
     "LC", None),
    ("S012", "Adelaide", "L", "repetition", "S011: Adelaide", "high",
     None, None, 1, None, None, "LC", None),
    # S013
    ("S013", "tăng trưởng", "L", "repetition",
     "S012: tăng chậm hơn", "high", None,
     "chuỗi TĂNG ('mức tăng trưởng 0,4 phần trăm')", 1, None, None,
     "LC", None),
    ("S013", "thành phố", "L", "repetition",
     "S002: một số thành phố", "high", None,
     "chuỗi thành phố ('một thành phố khác'); tiền trạm là câu VI tự "
     "sinh", 1, None, None, "LC", None),
    # [Phase-2] khác ← S010: quy chiếu so sánh (H&H §2.5 "other"; precedent
    # P21 VI S010 "khác") — "thành phố khác" = khác với các thành phố tăng
    # giá đã nêu; đối xứng EN another (S014 ST).
    ("S013", "khác", "R", "comparative",
     "S010: giá nhà tăng tại Adelaide, Brisbane và Perth", "high", None,
     "[LC] một thành phố khác = ngoài các thành phố tăng giá của S010; "
     "H&H §2.5 other", 1, None, None, "LC", "A"),
    # S014 — gộp EN S017+S018, đảo trật tự 2023/2024
    ("S014", "CoreLogic", "L", "repetition",
     "S004: giám đốc nghiên cứu của CoreLogic", "high", None,
     "'Báo cáo' lần đầu (chuỗi báo cáo bắt đầu ở đây); 'cho thấy' là "
     "động từ khung không đánh (§6)", 1, None, None, "LC", None),
    ("S014", "giá nhà trung bình", "L", "repetition",
     "S012: giá nhà", "high", None,
     "chuỗi GIÁ; 'giá trị trung bình' cuối câu cùng chuỗi, không đánh "
     "thêm; 'In contrast' của EN mất do gộp câu", 1, None, None, "LC",
     None),
    # [Phase-2] toàn quốc ← S003: lặp cụm "toàn quốc" trong chuỗi quốc gia
    # (H&H §6.2 reiteration; TNT §26 phép lặp) — cùng trường với "cả nước"
    # (S016); EN đối ứng "nationally" (S017) là trạng từ nên không đánh
    # bên EN (dịch chuyển lớp từ, ghi §7 analysis).
    ("S014", "toàn quốc", "L", "repetition",
     "S003: giá nhà trung bình toàn quốc", "high", None,
     "lặp cụm toàn quốc (S003 → S014); chuỗi quốc gia: Úc (S008) → cả "
     "nước (S016) → toàn quốc", 1, None, None, "LC", None),
    ("S014", "tăng", "L", "repetition", "S013: tăng trưởng", "high",
     None,
     "chuỗi TĂNG; lần 2 'tăng thêm' trong câu không đánh thêm", 1,
     None, None, "LC", None),
    # S015
    ("S015", "giá nhà", "L", "repetition",
     "S014: giá nhà trung bình", "high", None, "chuỗi GIÁ", 1, None,
     None, "LC", None),
    ("S015", "Melbourne", "L", "repetition", "S008: Melbourne", "high",
     None, None, 1, None, None, "LC", None),
    ("S015", "giảm", "L", "repetition",
     "S011: đã giảm 34% so với mức trung bình", "high", None,
     "chuỗi GIẢM; VI lặp 'giảm' cả 3 vế (lấp chỗ EN dùng chung động từ) "
     "nên không có ∅; 2 lần sau không đánh thêm", 1, None, None, "LC",
     None),
    ("S015", "Hobart", "L", "repetition", "S009: Hobart", "high", None,
     None, 1, None, None, "LC", None),
    ("S015", "Canberra", "L", "repetition", "S009: Canberra", "high",
     None, None, 1, None, None, "LC", None),
    # S016
    ("S016", "Trong khi đó", "C", "temporal",
     "S015: giá nhà ở Melbourne giảm 3%, Hobart giảm 0,6% và Canberra "
     "giảm 0,4%", "high", None,
     "song song EN 'Meanwhile' (S020)", 1, None, None, "LC", None),
    ("S016", "Perth", "L", "repetition", "S012: Perth", "high", None,
     None, 1, None, None, "LC", None),
    ("S016", "tăng trưởng", "L", "repetition", "S014: tăng", "high",
     None,
     "chuỗi TĂNG ('mức tăng trưởng lớn nhất'); 'mức tăng' trong câu "
     "không đánh thêm", 1, None, None, "LC", None),
    ("S016", "cả nước", "L", "superordinate",
     "S008: thị trường nhà ở lớn nhất của Úc", "high", None,
     "danh từ tổng quát thay 'Úc'; song song EN 'the country'", 1,
     None, None, "LC", None),
    ("S016", "giá trị nhà", "L", "synonym", "S015: giá nhà", "high",
     None, "chuỗi GIÁ ('về giá trị nhà')", 1, None, None, "LC", None),
    # S017
    ("S017", "Adelaide", "L", "repetition", "S012: Adelaide", "high",
     None, None, 1, None, None, "LC", None),
    ("S017", "Brisbane", "L", "repetition", "S010: Brisbane", "high",
     None, None, 1, None, None, "LC", None),
    ("S017", "cũng", "C", "additive",
     "S016: Perth có mức tăng trưởng lớn nhất cả nước", "high", None,
     "song song EN 'also' (S021)", 1, None, None, "LC", None),
    ("S017", "mức tăng", "L", "repetition", "S016: tăng trưởng", "high",
     None,
     "chuỗi TĂNG; 3 lần 'mức tăng/tăng trưởng' trong câu, chỉ đánh lần "
     "đầu", 1, None, None, "LC", None),
    ("S017", "Darwin", "L", "repetition", "S013: Darwin", "high", None,
     "'trong khi Darwin' là nối trong câu, không đánh", 1, None, None,
     "LC", None),
    # S019
    ("S019", "Thị trường nhà ở", "L", "repetition",
     "S011: trên thị trường", "high", None,
     "chuỗi thị trường; 'vùng nông thôn' là lần đầu thân bài chuỗi "
     "vùng", 1, None, None, "LC", None),
    ("S019", "cũng", "C", "additive",
     "S017: adelaide và Brisbane cũng ghi nhận mức tăng đáng kể", "high",
     None, "song song EN 'also' (S024)", 1, None, None, "LC", None),
    ("S019", "mức tăng", "L", "repetition", "S017: mức tăng", "high",
     None, "chuỗi TĂNG ('mức tăng 0,6%')", 1, None, None, "LC", None),
    ("S019", "giá trị", "L", "repetition",
     "S016: giá trị nhà", "high", None,
     "chuỗi GIÁ ('về giá trị')", 1, None, None, "LC", None),
    # S020 — câu thiếu dấu chấm cuối (xem §8)
    ("S020", "Báo cáo", "L", "repetition",
     "S014: Báo cáo của CoreLogic", "high", None,
     "chuỗi báo cáo; 'cho thấy' là động từ khung không đánh (§6)", 1,
     None, None, "LC", None),
    ("S020", "giá", "L", "repetition", "S019: giá trị", "high", None,
     "chuỗi GIÁ — VI dùng 'giá' đơn lẻ; Tây Úc/Nam Úc/Queensland lần "
     "đầu (tên bang, không tính chuỗi Úc)", 1, None, None, "LC", None),
    # [Phase-2] tăng ← S019 (mức tăng): mắt xích chuỗi TĂNG bị sót — đối
    # xứng EN "increased" (S026 ST) đã đánh và VI S010 "tăng" đã đánh cùng
    # cấu trúc (H&H §6.2; TNT §26); "tăng" đồng thời là động từ chung cho
    # các vế tọa hợp sau (∅ đã có hàng E riêng [TC]).
    ("S020", "tăng", "L", "repetition", "S019: mức tăng", "high", None,
     "chuỗi TĂNG (giá tăng tại ...); ∅ sau 'Nam Úc'/'Queensland' đã có "
     "hàng E riêng", 1, None, None, "LC", None),
    ("S020", "vùng nông thôn", "L", "repetition",
     "S019: vùng nông thôn", "high", None, "chuỗi vùng", 1, None, None,
     "LC", None),
    ("S020", None, "E", "nominal",
     "S020: giá tăng tại các khu vực vùng nông thôn (trong câu)",
     "high", None,
     "[TC] tỉnh lược động từ 'tăng' trong vế tọa hợp; lỗ trống sau "
     "'Queensland' không đánh thêm; EN dùng phối liệt gộp chung động từ",
     1, "Nam Úc", "{tăng}", "TC", None),
    # S021
    ("S021", "Vùng nông thôn", "L", "repetition",
     "S020: vùng nông thôn", "high", None,
     "chuỗi vùng; Victoria/Lãnh thổ phía Bắc lần đầu", 1, None, None,
     "LC", None),
    ("S021", "thị trường", "L", "repetition",
     "S019: Thị trường nhà ở", "high", None,
     "chuỗi thị trường ('những thị trường có giá nhà giảm' — VI lược "
     "cụm 'rest of state')", 1, None, None, "LC", None),
    ("S021", "giá nhà", "L", "repetition", "S020: giá", "high", None,
     "chuỗi GIÁ", 1, None, None, "LC", None),
    ("S021", "giảm", "L", "repetition", "S015: giảm 3%", "high", None,
     "chuỗi GIẢM; 'mức giảm' trong câu không đánh thêm", 1, None, None,
     "LC", None),
]
