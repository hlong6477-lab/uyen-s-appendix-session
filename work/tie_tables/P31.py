# P31 tie table — WRITTEN BY HAND FROM work/analysis/P31_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Cặp CNN→Người Đưa Tin: VI cắt toàn bộ attribution (statement/CNN) — chuỗi
# đó chỉ tồn tại phía EN; ô VI dòng 12 (S014 EN) trống → tie EN-only.
#
# [Phase-2] Bổ sung theo PHASE2_PROTOCOL.md (references H&H 1976 / TNT
# 2006 / NTT 2020 / mapping): +13 hàng EN (R another H&H §2.5; C in fact
# H&H §5.8; L: flight, delayed [nhóm 12], people, passengers, arrival,
# take it off the plane, returned, well-being, arrived, authorities,
# Iraqi government) / +8 hàng VI (R khác H&H §2.5; C thực tế H&H §5.8;
# L: người, di chuyển, hành khách, cập cảng, cập bến, cơ quan); rút span
# "video khác" → "video" (TT S003) và bỏ alt "R: another" (ST S003) vì
# another/khác được đánh R riêng (mapping §3.13); không reclassify cat/sub.

ST = [
    # S002
    ("S002", "Iraqi Airways", "L", "repetition", "S001: an Iraqi Airways flight",
     "high", None, "tên hãng lặp", 1, None, None, "LC", None),
    ("S002", "Baghdad", "L", "repetition", "S001: from Baghdad to Dubai",
     "high", None, None, 1, None, None, "LC", None),
    ("S002", "bear", "L", "repetition", "S001: A bear", "high",
     "R: a", "trong quote hành khách: a bear in the cargo", 1, None, None,
     "LC", None),
    ("S002", "cargo", "L", "repetition", "S001: the cargo hold", "high",
     "R: the", None, 1, None, None, "LC", None),
    # [Phase-2] flight ← an Iraqi Airways flight (S001): mắt xích sót của
    # chuỗi flight (H&H §6.2 reiteration; TNT §26 phép lặp) — "the return
    # flight" trước đây mới đánh Baghdad; 'return' là thông tin mới, the
    # định danh → alt (mapping §3.6).
    ("S002", "flight", "L", "repetition", "S001: an Iraqi Airways flight",
     "high", "R: the",
     "lặp flight (the return flight); mắt xích S002 của chuỗi the flight "
     "(S006/S010/S012/S013); H&H §6.2", 1, None, None, "LC", None),
    # [Phase-2] delayed ← caused delays (S001): mắt xích chuỗi delay — "The
    # delay" (S007) cite S002 làm tiền trạm nhưng S002 chưa có hàng → rà
    # chuỗi ngược "ante không có hàng" (nhóm 12 checklist; H&H §6.2; TNT
    # §26 phép lặp).
    ("S002", "delayed", "L", "repetition", "S001: caused delays", "high",
     None,
     "lặp danh-động từ delays → delayed (was delayed); VI đối ứng trì hoãn "
     "(S002 TT) đã có từ trước", 1, None, None, "LC", None),
    # S003
    # [Phase-2] another ← a video (S002): quy chiếu so sánh H&H §2.5
    # ("other") — "một video khác" đối chiếu video câu trước; VI "khác"
    # giữ 1-1 (nhóm 1 checklist; ref bắt buộc theo protocol).
    ("S003", "another", "R", "comparative",
     "S002: a video circulated online", "high", None,
     "[LC] quy chiếu so sánh: another = video khác với video đã nêu ở câu "
     "trước (H&H §2.5); VI 'khác' 1-1", 1, None, None, "LC", "A"),
    # [Phase-2] bỏ alt "R: another" — 'another' được đánh R riêng ở trên
    # (mapping §3.13 một hình thức một hàng); hàng này giữ vai trò lặp
    # đầu từ 'video'.
    ("S003", "video", "L", "repetition", "S002: a video", "high",
     None, "another video — lặp đầu từ video; 'another' đánh R riêng", 1,
     None, None, "LC", None),
    ("S003", "bear", "L", "repetition", "S002: a bear", "high", "R: a",
     "a bear cub — thêm 'cub' (gấu con)", 1, None, None, "LC", None),
    ("S003", "crate", "L", "repetition", "S001: a crate", "high", "R: its",
     "its crate", 1, None, None, "LC", None),
    # [Phase-2] people ← a male passenger (S002): danh từ tổng quát (H&H
    # §6.1 general word; §6.2 superordinate) — tham chiếu mở rộng sang
    # những người có mặt quanh gấu con trên máy bay (như P21 người Úc ←
    # người tiêu dùng Úc); VI 'người' 1-1.
    ("S003", "people", "L", "superordinate", "S002: a male passenger",
     "med", None,
     "danh từ tổng quát chỉ người trên máy bay — mở rộng từ hành khách "
     "S002 (H&H §6.1); VI 'người' 1-1", 1, None, None, "LC", None),
    # S004
    ("S004", "The bear", "L", "repetition", "S003: a bear cub", "high", None,
     "đặt lại tên nhân vật chính", 1, None, None, "LC", None),
    ("S004", "Dubai", "L", "repetition", "S001: to Dubai", "high",
     "R: in", "a specialist team in Dubai", 1, None, None, "LC", None),
    ("S004", "the plane", "L", "repetition", "S003: on the plane", "high",
     None, "taken off the plane; lần đầu xuất hiện 'plane' là S003", 1, None,
     None, "LC", None),
    ("S004", "Iraqi Airways", "L", "repetition", "S002: Iraqi Airways",
     "high", None, "attribution cuối câu", 1, None, None, "LC", None),
    # S005
    ("S005", "The airline", "L", "superordinate",
     "S004: Iraqi Airways", "high", None,
     "danh từ tổng quát thay tên hãng", 1, None, None, "LC", None),
    ("S005", "apology", "L", "repetition", "S002: an apology", "high",
     "R: an", "issued an apology", 1, None, None, "LC", None),
    ("S005", "the bear", "L", "repetition", "S004: The bear", "high", None,
     None, 1, None, None, "LC", None),
    ("S005", "escaped", "L", "repetition", "S001: it escaped", "high", None,
     None, 1, None, None, "LC", None),
    ("S005", "the crate", "L", "repetition", "S003: its crate", "high", None,
     None, 1, None, None, "LC", None),
    ("S005", "Dubai Airport", "L", "repetition", "S004: Dubai", "med", None,
     "sân bay cụ thể hóa thành phố Dubai (bridging nhẹ)", 1, None, None,
     "LC", None),
    # S006
    ("S006", "The company", "L", "superordinate", "S005: The airline",
     "high", None,
     "trong quote công ty; lần 'the company' thứ hai trong câu không đánh",
     1, None, None, "LC", None),
    ("S006", "apologizes", "L", "repetition", "S005: an apology", "high",
     None, "động từ tái hiện danh từ apology", 1, None, None, "LC", None),
    # [Phase-2] passengers ← a male passenger (S002): chuỗi hành khách bị
    # sót (H&H §6.2; TNT §26 phép lặp) — the + chuyển số nhiều; VI
    # 'hành khách' (S006 TT) đồng bộ thêm.
    ("S006", "passengers", "L", "repetition", "S002: a male passenger",
     "high", "R: the",
     "lặp passenger + số nhiều (toàn bộ khách trên chuyến bay); the định "
     "danh → alt (mapping §3.6)", 1, None, None, "LC", None),
    ("S006", "the flight", "L", "repetition", "S001: an Iraqi Airways flight",
     "high", None, None, 1, None, None, "LC", None),
    ("S006", "Baghdad International Airport", "L", "repetition",
     "S002: to Baghdad", "med", None,
     "sân bay cụ thể hóa thành phố (bridging nhẹ)", 1, None, None, "LC",
     None),
    ("S006", "Dubai Airport", "L", "repetition", "S005: Dubai Airport",
     "high", None, None, 1, None, None, "LC", None),
    # S007
    ("S007", "The delay", "L", "repetition",
     "S002: the return flight ... was delayed", "high", None,
     "danh từ tái hiện động từ delayed", 1, None, None, "LC", None),
    ("S007", "the cargo hold", "L", "repetition", "S002: the cargo", "high",
     None, "S002 'cargo' là dạng rút của 'cargo hold'", 1, None, None, "LC",
     None),
    ("S007", "the statement", "L", "repetition",
     "S004: in a statement shared with CNN", "high", None,
     "VI cắt attribution nên chuỗi này không có phía VI", 1, None, None,
     "LC", None),
    # S008
    # [Phase-2] arrival ← upon arrival (S005): mắt xích giữa của chuỗi
    # đến arrival (S005) → arrived (S013) bị sót (H&H §6.2 reiteration;
    # TNT §26); VI đối ứng 'cập cảng' (S008 TT) cũng bị sót → thêm đồng bộ.
    ("S008", "arrival", "L", "repetition",
     "S005: upon arrival to Dubai Airport", "high", None,
     "lặp arrival (Upon arrival); chuỗi đến: arrival (S005) → arrival "
     "(S008) → arrived (S013); H&H §6.2", 1, None, None, "LC", None),
    ("S008", "Dubai Airport", "L", "repetition", "S006: Dubai Airport",
     "high", None, None, 1, None, None, "LC", None),
    ("S008", "the animal", "L", "superordinate", "S005: the bear", "high",
     None, "đổi danh hiệu: bear → animal", 1, None, None, "LC", None),
    ("S008", "escaped", "L", "repetition", "S005: escaped", "high", None,
     None, 1, None, None, "LC", None),
    ("S008", "the crate", "L", "repetition", "S005: the crate", "high",
     None, "the crate specified for its shipment", 1, None, None, "LC",
     None),
    ("S008", "the airline", "L", "superordinate", "S006: The company",
     "high", None, None, 1, None, None, "LC", None),
    ("S008", "transported", "L", "repetition",
     "S001: A bear being transported", "high", None,
     "it was being transported", 1, None, None, "LC", None),
    ("S008", "shipment", "L", "repetition", "S007: a shipment", "high",
     "R: its", None, 1, None, None, "LC", None),
    # S009
    ("S009", "plane", "L", "repetition", "S004: the plane", "med", None,
     "The plane crew — bộ phận 'plane' lặp, 'crew' là thông tin mới", 1,
     None, None, "LC", None),
    ("S009", "specialized team", "L", "repetition",
     "S004: a specialist team", "high", "R: a",
     "specialist → specialized; đội cũ", 1, None, None, "LC", None),
    ("S009", "the animal", "L", "superordinate", "S008: the animal", "high",
     None, None, 1, None, None, "LC", None),
    ("S009", "sedate", "L", "repetition", "S004: was sedated", "high", None,
     "to sedate the animal", 1, None, None, "LC", None),
    # [Phase-2] take it off the plane ← taken off the plane (S004): mắt
    # xích sót của chuỗi echo VP — chuỗi đang nhảy S004 → S011 bỏ qua S009
    # (H&H §6.2 reiteration; TNT §26 phép lặp); 'it' trong span là đại từ
    # trong câu (the animal), không đánh R riêng (quy ước [TC]).
    ("S009", "take it off the plane", "L", "repetition",
     "S004: taken off the plane", "high", None,
     "echo VP; mắt xích S009 cho chuỗi taken off (S004) → taken off "
     "(S011); VI gộp vào họ 'chuyển' (S010 TT 'chuyển')", 1, None, None,
     "LC", None),
    # S010
    ("S010", None, "E", "nominal", "S009: The plane crew", "med", None,
     "[LC] (biên) chủ ngữ mệnh đề danh động từ 'After ∅ checking ...' được "
     "điều khiển bằng 'The plane crew' ở câu trước", 1, "After ",
     "{the plane crew}", "LC", None),
    ("S010", "the plane", "L", "repetition", "S009: The plane crew", "high",
     None, "checking the plane", 1, None, None, "LC", None),
    ("S010", "this incident", "R", "demonstrative",
     "S001-S009: sự kiện gấu xổng chuồng", "med", None,
     "chỉ từ tóm lược toàn tình huống; VI chỉ còn 'vụ việc' (L)", 1, None,
     None, "LC", "A"),
    ("S010", "the flight", "L", "repetition", "S006: the flight", "high",
     None, None, 1, None, None, "LC", None),
    # [Phase-2] returned ← the return flight (S002): danh → động từ của
    # cùng hình vị return (H&H §6.2 reiteration; TNT §26 phép lặp); VI
    # từ vựng hóa bằng từ hướng 'về' — 'về' là từ chức năng tần suất cao,
    # không đủ trọng lượng làm hàng L riêng (xem analysis §7).
    ("S010", "returned", "L", "repetition", "S002: the return flight",
     "high", None,
     "lặp hình vị return (returned to Baghdad ← the return flight); H&H "
     "§6.2 danh-động từ", 1, None, None, "LC", None),
    ("S010", "Baghdad", "L", "repetition",
     "S006: Baghdad International Airport", "high", None,
     "returned to Baghdad", 1, None, None, "LC", None),
    ("S010", "the statement", "L", "repetition", "S007: the statement",
     "high", None, None, 1, None, None, "LC", None),
    # S011
    ("S011", "The airline", "L", "superordinate", "S008: the airline",
     "high", None, None, 1, None, None, "LC", None),
    ("S011", "the bear", "L", "repetition", "S009: the animal", "high", None,
     "đổi lại danh hiệu animal → bear", 1, None, None, "LC", None),
    ("S011", "transported", "L", "repetition", "S008: transported", "high",
     None, "was being transported to the United Arab Emirates", 1, None,
     None, "LC", None),
    ("S011", "the United Arab Emirates", "L", "repetition",
     "S009: UAE's authority", "high", "R: the",
     "UAE mở rộng thành tên đầy đủ", 1, None, None, "LC", None),
    # [Phase-2] well-being ↔ welfare (S008): đồng nghĩa (H&H §6.2
    # reiteration — synonym); VI đứt chuỗi (bảo vệ S009 TT ≠ an toàn S012
    # TT) → tie EN-only, dịch chuyển từ vựng theo NTT 2020 §5.
    ("S011", "well-being", "L", "synonym",
     "S008: international animal welfare guidelines", "high", None,
     "well-being ≈ welfare (information on its well-being ← animal "
     "welfare guidelines); VI dùng hai danh từ khác nhau nên không có "
     "hàng đối ứng", 1, None, None, "LC", None),
    ("S011", "sedated", "L", "repetition", "S009: sedate", "high", None,
     "after it was sedated", 1, None, None, "LC", None),
    ("S011", "taken off the plane", "L", "repetition",
     "S004: taken off the plane", "high", None,
     "echo nguyên văn VP", 1, None, None, "LC", None),
    # S012
    ("S012", "Later Monday", "C", "temporal",
     "S001: Friday (mốc thời gian sự kiện)", "med", None,
     "chuyển khung thời gian của bài (sự kiện → lời ministry); VI phải dùng "
     "'thứ Hai' vì S001 VI đã đổi ngày", 1, None, None, "LC", None),
    ("S012", "CNN", "L", "repetition", "S004: shared with CNN", "high", None,
     "told CNN", 1, None, None, "LC", None),
    # [Phase-2] in fact: continuative (H&H §5.8 — chuẩn sub nhóm 11
    # checklist): giữa câu nhưng mở lượt đính chính discours "thực ra có
    # HAI con" đối chiếu mạch 'a bear' (S001–S011); VI 'thực tế' giữ 1-1.
    ("S012", "in fact", "C", "continuative",
     "S001-S011: mạch 'một con gấu' (a bear, the bear, the animal)",
     "med", None,
     "continuative H&H §5.8: đính chính đếm số (in fact two bears); liên "
     "câu vì mạch bị đính chính nằm ở các câu trước", 1, None, None,
     "LC", None),
    ("S012", "bears", "L", "repetition", "S011: the bear", "high", None,
     "two bears — chuyển số nhiều, hé lộ thông tin mới", 1, None, None,
     "LC", None),
    ("S012", "the flight", "L", "repetition", "S010: the flight", "high",
     None, "on board the flight", 1, None, None, "LC", None),
    # S013
    ("S013", "bears", "L", "repetition", "S012: two bears", "high", None,
     "Two small, endangered bears; 'one of the bears' trong câu không đánh "
     "thêm", 1, None, None, "LC", None),
    ("S013", "shipped", "L", "repetition", "S008: shipment", "high", None,
     "động từ tái hiện danh từ shipment", 1, None, None, "LC", None),
    ("S013", "Baghdad", "L", "repetition", "S010: Baghdad", "high", None,
     "were shipped from Baghdad", 1, None, None, "LC", None),
    ("S013", "the flight", "L", "repetition", "S012: the flight", "high",
     None, None, 1, None, None, "LC", None),
    # [Phase-2] arrived ← Upon arrival (S008): mắt xích cuối chuỗi đến,
    # tiền trạm = nhắc gần nhất (H&H §6.2 reiteration; TNT §26); danh →
    # động từ; VI đối ứng 'cập bến' (S014 TT) đồng bộ thêm.
    ("S013", "arrived", "L", "repetition",
     "S008: Upon arrival to Dubai Airport", "high", None,
     "lặp arrival qua arrived (when the flight arrived); chuỗi đến S005 → "
     "S008 → S013", 1, None, None, "LC", None),
    ("S013", "Dubai", "L", "repetition", "S008: Dubai Airport", "high",
     None, "arrived in Dubai (lần 'at Dubai airport' trong câu không đánh "
     "thêm)", 1, None, None, "LC", None),
    ("S013", "cage", "L", "synonym", "S008: the crate", "high",
     "R: his", "broke his cage — đồng nghĩa crate", 1, None, None, "LC",
     None),
    # [Phase-2] authorities ← UAE's authority (S009): lặp + cụ thể hóa
    # (cơ quan UAE → cơ quan y tế-môi trường tại Dubai; H&H §6.2; TNT
    # §26 phép lặp); VI 'cơ quan' (S014 TT) đồng bộ thêm.
    ("S013", "authorities", "L", "repetition", "S009: UAE's authority",
     "med", None,
     "lặp authority, số nhiều + cụ thể hóa referent (health and "
     "environment authorities); tiền trạm S009", 1, None, None, "LC",
     None),
    ("S013", "sedate", "L", "repetition", "S011: sedated", "high", None,
     "to sedate it", 1, None, None, "LC", None),
    ("S013", "the statement", "L", "repetition", "S010: the statement",
     "high", None, None, 1, None, None, "LC", None),
    # S014 — không có bản dịch (ô VI trống)
    ("S014", "CNN", "L", "repetition", "S012: CNN", "high", None,
     "không có bản dịch", 1, None, None, "LC", None),
    # [Phase-2] the Iraqi government ← the Iraqi transport ministry
    # (S012): the + tổng quát hóa tham chiếu đã nêu (mapping §3.6; H&H §6.1
    # general noun) — nối chuỗi Iraq (S012 → S015 Iraq's prime minister);
    # không có bản dịch.
    ("S014", "Iraqi government", "L", "general word",
     "S012: the Iraqi transport ministry", "med", "R: the",
     "tổng quát hóa (bộ → chính phủ toàn thể); 'Iraqi' lặp hình vị nước "
     "trong chuỗi Iraq; the định danh → alt (mapping §3.6)", 1, None,
     None, "LC", None),
    ("S014", "the bears", "L", "repetition", "S013: bears", "high", None,
     "không có bản dịch", 1, None, None, "LC", None),
    # S015
    ("S015", "Iraq", "L", "repetition",
     "S012: the Iraqi transport ministry", "med", None,
     "Iraq's prime minister — chuỗi nước Iraq (khác chuỗi tên hãng Iraqi "
     "Airways)", 1, None, None, "LC", None),
    ("S015", "country", "L", "superordinate", "S012: the Iraqi transport "
     "ministry", "med", None,
     "the country's ministry of transport — danh từ tổng quát thay Iraq", 1,
     None, None, "LC", None),
    ("S015", "ministry of transport", "L", "repetition",
     "S012: the Iraqi transport ministry", "high", "R: the country's",
     "đảo trật tự transport ministry → ministry of transport", 1, None,
     None, "LC", None),
    ("S015", "bear", "L", "repetition", "S013: bears", "high",
     "R: the", "the bear's escape (danh từ hóa)", 1, None, None, "LC",
     None),
    ("S015", "escape", "L", "repetition", "S008: escaped", "high", None,
     "investigation into the bear's escape", 1, None, None, "LC", None),
]

TT = [
    # S002
    ("S002", "Iraqi Airways", "L", "repetition",
     "S001: một chuyến bay của Iraqi Airways", "high", None, None, 1, None,
     None, "LC", None),
    ("S002", "Baghdad", "L", "repetition", "S001: từ Baghdad", "high", None,
     None, 1, None, None, "LC", None),
    ("S002", "chuyến bay", "L", "repetition",
     "S001: một chuyến bay của Iraqi Airways", "high", None,
     "chuyến bay khứ hồi", 1, None, None, "LC", None),
    ("S002", "trì hoãn", "L", "repetition", "S001: khiến trì hoãn nhiều "
     "chuyến bay", "high", None, "bị trì hoãn", 1, None, None, "LC", None),
    ("S002", "gấu", "L", "repetition", "S001: Một chú gấu", "high", None,
     "trong quote: vì có gấu xổng chuồng", 1, None, None, "LC", None),
    ("S002", "xổng", "L", "repetition",
     "S001: đã xổng khỏi khu chứa hàng", "high", None, None, 1, None, None,
     "LC", None),
    # S003
    # [Phase-2] khác ← một video (S002): quy chiếu so sánh H&H §2.5 — đối
    # xứng EN 'another'; rút span hàng L "video khác" → "video" để không
    # chồng marker (mapping §3.13 một hình thức một hàng).
    ("S003", "khác", "R", "comparative", "S002: một video được đăng tải",
     "high", None,
     "[LC] quy chiếu so sánh: khác = khác với video đã nêu ở câu trước "
     "(H&H §2.5); EN 'another' 1-1", 1, None, None, "LC", "A"),
    # [Phase-2] span rút còn "video" — 'khác' được đánh R riêng ở trên
    # (tránh chồng marker, precedent P28).
    ("S003", "video", "L", "repetition", "S002: một video", "high",
     "R: một", "Trong một video khác — lặp video; 'khác' đánh R riêng", 1,
     None, None, "LC", None),
    ("S003", "gấu", "L", "repetition", "S002: gấu", "high", "R: một",
     "một gấu con — thêm 'con' (gấu non)", 1, None, None, "LC", None),
    ("S003", "chuồng", "L", "repetition", "S002: xổng chuồng", "high",
     None, "quay quanh chuồng", 1, None, None, "LC", None),
    ("S003", "máy bay", "L", "repetition", "S002: chuyến bay", "med", None,
     "chuyến bay → máy bay (dịch chuyển chỉ phương tiện)", 1, None, None,
     "LC", None),
    # [Phase-2] người ← một hành khách nam (S002): danh từ tổng quát (H&H
    # §6.1 general word; §6.2 superordinate) — mở rộng tham chiếu sang
    # những người quanh gấu con; đối xứng EN people (S003 ST).
    ("S003", "người", "L", "superordinate", "S002: một hành khách nam",
     "med", None,
     "danh từ tổng quát (nhiều người cố gắng xoa dịu nó) — mở rộng từ hành "
     "khách S002; H&H §6.1; EN 'people' 1-1", 1, None, None, "LC", None),
    # S004
    ("S004", "Chú gấu này", "L", "repetition", "S001: Một chú gấu", "high",
     "R: này", "chỉ từ 'này' thâu vào alt vì đầu ngữ lặp lại", 1, None, None,
     "LC", None),
    ("S004", "Dubai", "L", "repetition", "S001: tới Dubai", "high",
     "R: tại", None, 1, None, None, "LC", None),
    # [Phase-2] di chuyển ← được chuyển (S001): lặp hình vị lõi 'chuyển'
    # (TNT §26 phép lặp; H&H §6.2) — mắt xích sót của chuỗi VI: chuyển
    # (S001) → di chuyển (S004) → vận chuyển (S009) → chuyển (S010); VI
    # hội tụ họ 'chuyển' cho cả transported lẫn taken off (NTT 2020 §2.1).
    ("S004", "di chuyển", "L", "repetition", "S001: được chuyển", "med",
     None,
     "di chuyển (khỏi máy bay) — hiện thực hóa EN 'taken off the plane' "
     "bằng cùng họ 'chuyển' (TNT §26)", 1, None, None, "LC", None),
    ("S004", "máy bay", "L", "repetition", "S003: trên máy bay", "high",
     None, "di chuyển khỏi máy bay", 1, None, None, "LC", None),
    # S005
    ("S005", "Hãng hàng không", "L", "superordinate",
     "S002: Iraqi Airways", "high", None,
     "danh từ tổng quát thay tên hãng (EN: The airline)", 1, None, None,
     "LC", None),
    ("S005", "lời xin lỗi", "L", "repetition", "S002: lời xin lỗi", "high",
     None, "đưa ra lời xin lỗi", 1, None, None, "LC", None),
    ("S005", "chú gấu này", "L", "repetition", "S004: Chú gấu này", "high",
     "R: này", None, 1, None, None, "LC", None),
    ("S005", "xổng", "L", "repetition", "S002: xổng", "high", None,
     "đã xổng chuồng", 1, None, None, "LC", None),
    ("S005", "chuyến bay", "L", "repetition", "S002: chuyến bay", "high",
     None, "khi chuyến bay cập bến", 1, None, None, "LC", None),
    ("S005", "Cảng Hàng không Dubai", "L", "repetition", "S004: Dubai",
     "med", None, "sân bay cụ thể hóa thành phố (bridging nhẹ)", 1, None,
     None, "LC", None),
    # S006
    ("S006", "Công ty", "L", "superordinate", "S005: Hãng hàng không",
     "high", None,
     "trong quote; 'của công ty' cuối câu không đánh thêm", 1, None, None,
     "LC", None),
    ("S006", "lời xin lỗi", "L", "repetition", "S005: lời xin lỗi", "high",
     None, "xin gửi lời xin lỗi", 1, None, None, "LC", None),
    # [Phase-2] hành khách ← một hành khách nam (S002): chuỗi hành khách bị
    # sót (TNT §26 phép lặp; H&H §6.2) — chuyển số nhiều (những hành
    # khách = toàn bộ khách trên chuyến bay); EN 'passengers' (S006 ST)
    # đồng bộ thêm.
    ("S006", "hành khách", "L", "repetition", "S002: một hành khách nam",
     "high", None,
     "lặp hành khách + số nhiều (những hành khách); TNT §26 phép lặp từ "
     "vựng", 1, None, None, "LC", None),
    ("S006", "chuyến bay", "L", "repetition", "S005: chuyến bay", "high",
     None, "trên chuyến bay từ", 1, None, None, "LC", None),
    ("S006", "Cảng Hàng không Quốc tế Baghdad", "L", "repetition",
     "S002: Baghdad", "med", None,
     "sân bay cụ thể hóa thành phố (bridging nhẹ)", 1, None, None, "LC",
     None),
    ("S006", "Cảng Hàng không Dubai", "L", "repetition",
     "S005: Cảng Hàng không Dubai", "high", None, None, 1, None, None,
     "LC", None),
    # S007
    ("S007", "trì hoãn", "L", "repetition", "S002: bị trì hoãn", "high",
     "R: này",
     "Việc trì hoãn này — chỉ từ 'này' thâu vào alt vì đầu ngữ lặp", 1,
     None, None, "LC", None),
    ("S007", "khu chứa hàng", "L", "repetition", "S001: khu chứa hàng",
     "high", None, None, 1, None, None, "LC", None),
    # S008
    ("S008", "máy bay", "L", "repetition", "S004: máy bay", "high", None,
     "Khi máy bay cập cảng", 1, None, None, "LC", None),
    # [Phase-2] cập cảng ← cập bến (S005): lặp hình vị lõi 'cập', bến ≈
    # cảng (TNT §26 phép lặp; H&H §6.2) — mắt xích giữa chuỗi đến: cập
    # bến (S005) → cập cảng (S008) → cập bến (S014); EN đối ứng 'arrival'
    # (S008 ST) đồng bộ thêm.
    ("S008", "cập cảng", "L", "repetition", "S005: khi chuyến bay cập bến",
     "med", None,
     "lặp hình vị 'cập' (cập cảng ≈ cập bến); chuỗi đến của VI, H&H §6.2",
     1, None, None, "LC", None),
    ("S008", "Cảng Hàng không Dubai", "L", "repetition",
     "S006: Cảng Hàng không Dubai", "high", None, None, 1, None, None,
     "LC", None),
    ("S008", "con gấu này", "L", "repetition", "S005: chú gấu này", "high",
     "R: này", "đổi loại từ chú → con (ghi §4.3)", 1, None, None, "LC",
     None),
    ("S008", "thoát", "L", "synonym", "S005: xổng", "high", None,
     "xổng → thoát: đổi động từ một lần", 1, None, None, "LC", None),
    ("S008", "chuồng", "L", "repetition", "S005: xổng chuồng", "high",
     None, "thoát khỏi chuồng giữ", 1, None, None, "LC", None),
    # S009 — VI tách câu, 'cũng' trở thành nối liên câu (EN 'adding' trong câu)
    ("S009", "Công ty", "L", "superordinate", "S006: Công ty", "high", None,
     None, 1, None, None, "LC", None),
    ("S009", "cũng", "C", "additive",
     "S008: con gấu này đã thoát khỏi chuồng giữ (tuyên bố trước)", "high",
     None,
     "EN giải quyết quan hệ bổ sung trong câu ('adding that') → VI tách "
     "câu nên 'cũng' thành liên từ liên câu", 1, None, None, "LC", None),
    ("S009", "chú gấu này", "L", "repetition", "S008: con gấu này", "high",
     "R: này", None, 1, None, None, "LC", None),
    ("S009", "vận chuyển", "L", "repetition", "S001: được chuyển", "high",
     None, "được vận chuyển — chuyển mở rộng", 1, None, None, "LC", None),
    # S010
    ("S010", "một nhóm chuyên gia", "L", "repetition",
     "S004: một nhóm chuyên gia", "high", "R: một",
     "lặp nguyên văn", 1, None, None, "LC", None),
    ("S010", "tiêm thuốc an thần", "L", "repetition",
     "S004: tiêm thuốc an thần", "high", None, "lặp nguyên văn", 1, None,
     None, "LC", None),
    ("S010", "con gấu này", "L", "repetition", "S009: chú gấu này", "high",
     "R: này", None, 1, None, None, "LC", None),
    ("S010", "chuyển", "L", "repetition", "S009: vận chuyển", "med", None,
     "VI dùng lại họ 'chuyển' cho 'take off' (EN đổi động từ)", 1, None,
     None, "LC", None),
    ("S010", "máy bay", "L", "repetition", "S008: máy bay", "high", None,
     "ra khỏi máy bay", 1, None, None, "LC", None),
    # S011
    ("S011", None, "E", "nominal", "S010: Nhóm phi hành đoàn", "med", None,
     "[LC] (biên) chủ ngữ mệnh đề 'Sau khi ∅ kiểm tra ...' được điều khiển "
     "bằng 'Nhóm phi hành đoàn' ở câu trước; song song E-EN1", 1, "Sau khi ",
     "{nhóm phi hành đoàn}", "LC", None),
    ("S011", "máy bay", "L", "repetition", "S010: máy bay", "high", None,
     "kiểm tra máy bay", 1, None, None, "LC", None),
    ("S011", "vụ việc", "L", "general word",
     "S001-S010: sự kiện gấu xổng chuồng", "med", None,
     "danh từ tổng quát tóm chỉ tình huống; EN dùng chỉ từ 'this incident' "
     "(R) — dịch chuyển R→L", 1, None, None, "LC", None),
    ("S011", "chuyến bay", "L", "repetition", "S005: chuyến bay", "high",
     None, "chuyến bay đã tiếp tục cất cánh", 1, None, None, "LC", None),
    ("S011", "Baghdad", "L", "repetition",
     "S006: Cảng Hàng không Quốc tế Baghdad", "high", None,
     "cất cánh về Baghdad", 1, None, None, "LC", None),
    # S012
    ("S012", "Hãng Hàng không", "L", "repetition", "S005: Hãng hàng không",
     "high", "R: này",
     "viết hoa khác S005; 'này' thâu vào alt; VI bỏ 'told CNN'", 1, None,
     None, "LC", None),
    ("S012", "chú gấu", "L", "repetition", "S010: con gấu này", "high",
     None, "lần 1 trong câu (lần 2 'của chú gấu' không đánh thêm)", 1, None,
     None, "LC", None),
    ("S012", "vận chuyển", "L", "repetition", "S009: vận chuyển", "high",
     None, "lần 1 trong câu (lần 2 'vận chuyển khỏi' không đánh thêm)", 1,
     None, None, "LC", None),
    ("S012", "UAE", "L", "repetition", "S010: cơ quan chức năng của UAE",
     "high", None, None, 1, None, None, "LC", None),
    ("S012", "tiêm thuốc an thần", "L", "repetition",
     "S010: tiêm thuốc an thần", "high", None, None, 1, None, None, "LC",
     None),
    ("S012", "máy bay", "L", "repetition", "S011: máy bay", "high", None,
     "vận chuyển khỏi máy bay", 1, None, None, "LC", None),
    # S013
    ("S013", "Trong cuối ngày thứ Hai", "C", "temporal",
     "S001: trong thứ Hai vừa rồi (mốc sự kiện)", "med", None,
     "chuyển khung thời gian; EN đối ứng 'Later Monday' nhưng lệch ngày do "
     "lỗi dịch S001 (xem §8)", 1, None, None, "LC", None),
    ("S013", "chuyến bay", "L", "repetition", "S011: chuyến bay", "high",
     "R: này", "chuyến bay này", 1, None, None, "LC", None),
    # [Phase-2] thực tế: continuative (H&H §5.8 — chuẩn sub nhóm 11
    # checklist) — đính chính "thực tế có 2 con" đối chiếu mạch 'một chú
    # gấu' (S001–S012); giữa câu nhưng quan hệ đính chính là LIÊN CÂU; EN
    # 'in fact' (S012 ST) giữ 1-1.
    ("S013", "thực tế", "C", "continuative",
     "S001-S012: mạch 'một chú gấu'", "med", None,
     "continuative H&H §5.8: đính chính đếm số (thực tế vận chuyển hai "
     "chú gấu); mạch bị đính chính nằm ở các câu trước", 1, None, None,
     "LC", None),
    ("S013", "vận chuyển", "L", "repetition", "S012: vận chuyển", "high",
     None, "thực tế vận chuyển hai chú gấu", 1, None, None, "LC", None),
    ("S013", "chú gấu", "L", "repetition", "S012: chú gấu", "high", None,
     "hai chú gấu — chuyển số nhiều", 1, None, None, "LC", None),
    # S014
    ("S014", "Hai chú gấu", "L", "repetition", "S013: hai chú gấu", "high",
     None,
     "lặp nguyên văn + thêm 'nhỏ'; lần 'một trong hai chú gấu' trong câu "
     "không đánh thêm", 1, None, None, "LC", None),
    ("S014", "Baghdad", "L", "repetition", "S011: Baghdad", "high", None,
     "được gửi từ Baghdad", 1, None, None, "LC", None),
    ("S014", "chuyến bay", "L", "repetition", "S013: chuyến bay", "high",
     None, "khi chuyến bay cập bến", 1, None, None, "LC", None),
    # [Phase-2] cập bến ← cập cảng (S008): chuỗi đến quay về 'cập bến',
    # tiền trạm = nhắc gần nhất S008 (H&H §6.2; TNT §26 phép lặp); EN
    # 'arrived' (S013 ST) đồng bộ thêm.
    ("S014", "cập bến", "L", "repetition", "S008: máy bay cập cảng",
     "high", None,
     "lặp cập bến (khi chuyến bay cập bến) ← S005 cập bến qua S008 cập "
     "cảng; tiền trạm gần nhất S008", 1, None, None, "LC", None),
    ("S014", "Dubai", "L", "repetition", "S008: Cảng Hàng không Dubai",
     "high", None, "cập bến tại Dubai", 1, None, None, "LC", None),
    ("S014", "xổng chuồng", "L", "repetition", "S005: xổng chuồng", "high",
     None, None, 1, None, None, "LC", None),
    # [Phase-2] cơ quan ← cơ quan chức năng của UAE (S010): lặp + cụ thể
    # hóa (cơ quan chức năng UAE → các cơ quan y tế-môi trường tại Dubai;
    # H&H §6.2; TNT §26) — EN 'authorities' (S013 ST) đồng bộ thêm.
    ("S014", "cơ quan", "L", "repetition",
     "S010: cơ quan chức năng của UAE", "med", None,
     "lặp cơ quan, số nhiều + cụ thể hóa referent (các cơ quan về sức khỏe "
     "và môi trường); H&H §6.2", 1, None, None, "LC", None),
    ("S014", "tiêm thuốc an thần", "L", "repetition",
     "S012: tiêm thuốc an thần", "high", None,
     "EN 'sedate it' → VI 'cho chúng' (dịch chuyển số, ghi §4.3)", 1, None,
     None, "LC", None),
    # S015
    ("S015", "Bộ Giao thông Vận tải", "L", "repetition",
     "S013: Bộ Giao thông Vận tải Iraq", "high", "R: nước này",
     "lặp nguyên văn tên bộ; 'nước này' được đánh R riêng (chuỗi Iraq)", 1,
     None, None, "LC", None),
    ("S015", "nước này", "R", "demonstrative", "S013: Iraq", "high", None,
     "chỉ từ + danh từ tổng quát mới chỉ nước Iraq; EN đối ứng "
     "'the country's' (L)", 1, None, None, "LC", "A"),
    ("S015", "chú gấu", "L", "repetition", "S014: Hai chú gấu", "high",
     None, "EN 'the bear's escape' → VI mệnh đề đầy đủ", 1, None, None,
     "LC", None),
    ("S015", "xổng chuồng", "L", "repetition", "S014: xổng chuồng", "high",
     None, None, 1, None, None, "LC", None),
]
