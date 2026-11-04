# P22 tie table — WRITTEN BY HAND FROM work/analysis/P22_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Bản đồ câu 1:1 (60↔60), không cắt/không tự sinh.
# Tiểu đề S009/S028/S038/S046/S055 + số danh sách S012/S015/S018/S021/S025: 0 tie.
# [Phase-2] enrichment theo PHASE2_PROTOCOL.md: hàng mới có comment
# '# [Phase-2]' + trích H&H §/TNT §/mapping § ngay trên hàng.

ST = [
    # S002
    ("S002", "Long summer days", "L", "repetition",
     "S001: during the summer holidays", "high", None, "lặp 'summer'", 1,
     None, None, "LC", None),
    ("S002", "devices", "L", "repetition",
     "S001: off their devices", "high", None, "wrestle devices off", 1,
     None, None, "LC", None),
    ("S002", "children", "L", "synonym",
     "S001: your kids", "high", None, "kids ≈ children", 1, None, None,
     "LC", None),
    ("S002", "screen time", "L", "repetition",
     "S001: limit screen use", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] wrestle ← battle (S001): lặp gần nghĩa cùng trường xung
    # đột (H&H §6.2 reiteration); 'fight' cùng chuỗi trong câu không
    # đánh thêm. VI S001 bỏ ẩn dụ 'battle' (dịch 'rất khó khăn') nên
    # không có hàng VI — dịch chuyển từ vựng, ghi §7.
    ("S002", "wrestle", "L", "synonym",
     "S001: It can be a battle to get your kids off their devices",
     "med", None,
     "wrestle ≈ battle (H&H §6.2 gần nghĩa, cùng trường xung đột); "
     "'fight' cùng chuỗi trong câu không đánh thêm", 1, None, None,
     "LC", None),
    # S003
    ("S003", "parents", "L", "repetition",
     "S002: a nightmare for parents", "high", None,
     "'enforcing these' trong câu không đánh", 1, None, None, "LC",
     None),
    ("S003", "other devices", "L", "repetition",
     "S002: wrestle devices", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] restrictions ← limit (S001): đồng nghĩa qua danh hóa
    # (H&H §6.2 reiteration) — mở chuỗi limit/restrictions; VI đối ứng
    # lặp nguyên hình 'hạn chế' (S003 TT), hai đầu khác cơ chế, ghi §7.
    ("S003", "restrictions", "L", "synonym",
     "S001: how you can limit screen use", "med", None,
     "restrictions ≈ limit (động từ → danh từ, H&H §6.2); 'other' so "
     "sánh trong câu (H&H §2.5) → [TC] không đánh, ghi §4.3", 1, None,
     None, "LC", None),
    # S004
    ("S004", "a mother of four", "L", "synonym",
     "S002: parents", "med", None,
     "mother ≈ parents; 'rules' khởi tạo chuỗi", 1, None, None, "LC",
     None),
    # S006
    ("S006", "young person", "L", "synonym",
     "S001: your kids", "high", None,
     "young person = con trẻ; VI 'trẻ' lần đầu nên không có hàng VI",
     1, None, None, "LC", None),
    ("S006", "digital media use", "L", "repetition",
     "S001: screen use", "med", None,
     "lặp 'use'; 'digital/media' từ mới; 'it' giả chủ ngữ không đánh",
     1, None, None, "LC", None),
    # S007
    ("S007", "Rhodes", "L", "repetition",
     "S004: Dr Anthea Rhodes", "high", None, None, 1, None, None,
     "LC", None),
    ("S007", "screen use", "L", "repetition",
     "S001: limit screen use", "high", None, None, 1, None, None,
     "LC", None),
    ("S007", "children", "L", "repetition",
     "S002: their children", "high", None,
     "'they are older' trong câu không đánh", 1, None, None, "LC",
     None),
    # [Phase-2] the rules ← rules (S004): chuỗi quy tắc bị sót + mạo từ
    # xác định đổi tên tham chiếu đã nêu (H&H §6.2; mapping §3.6
    # the+rename → alt 'R: the').
    ("S007", "rules", "L", "repetition",
     "S004: resistance or difficulty in sticking to rules", "high",
     "R: the",
     "lặp rules (the rules can be discussed) — H&H §6.2; 'the' định "
     "danh quy tắc đã nêu (mapping §3.6)", 1, None, None, "LC", None),
    # S008
    ("S008", "kids", "L", "repetition",
     "S001: your kids", "high", None, "kids' screen use", 1, None,
     None, "LC", None),
    ("S008", "screen use", "L", "repetition",
     "S007: screen use", "high", None, None, 1, None, None, "LC",
     None),
    ("S008", "parents", "L", "repetition",
     "S003: many parents", "high", None,
     "to help parents; 'it's problematic' trong câu không đánh", 1,
     None, None, "LC", None),
    # S010
    ("S010", "screen use", "L", "repetition",
     "S008: kids' screen use", "high", None, None, 1, None, None,
     "LC", None),
    ("S010", "children", "L", "repetition",
     "S007: with children", "high", None,
     "'Kids Research Institute' là tên riêng, không đánh", 1, None,
     None, "LC", None),
    # S011
    ("S011", "Her", "R", "personal",
     "S010: Dr Mary Brushe", "high", None, None, 1, None, None, "LC",
     "A"),
    ("S011", "tips", "L", "repetition",
     "S001: some tips", "high", None, None, 1, None, None, "LC",
     None),
    ("S011", "screen time", "L", "repetition",
     "S002: fight over screen time", "high", None, None, 1, None,
     None, "LC", None),
    # S013
    ("S013", "the screen", "L", "repetition",
     "S008: screen use", "high", None,
     "'turn it off' trong câu không đánh; VI đổi thành 'TV'", 1, None,
     None, "LC", None),
    # S014
    ("S014", "TV", "L", "repetition",
     "S003: TV, computers, mobile phones", "high", None,
     "Leaving a TV on; 'this' trong câu không đánh", 1, None, None,
     "LC", None),
    ("S014", "young children", "L", "repetition",
     "S010: children under five years old", "high", None, None, 1,
     None, None, "LC", None),
    # [Phase-2] on ↔ off (S013): phép đối liên câu (TNT §30; H&H §6.4
    # opposites) — lời khuyên 'turn it off' đối lập thói quen 'Leaving
    # a TV on'; VI tắt ↔ bật giữ 1-1.
    ("S014", "on", "L", "antonym",
     "S013: If no one is watching the screen, turn it off", "med",
     None,
     "occ 1 = 'a TV on' (occ 2 chuỗi con trong 'common', không dùng — "
     "tiền lệ P26); phép đối on ↔ off (TNT §30)", 1, None, None, "LC",
     None),
    # S017
    ("S017", "screens", "L", "repetition",
     "S013: the screen", "high", None,
     "screens at mealtime; VI đổi thành 'xem TV', ghi §8", 1, None,
     None, "LC", None),
    ("S017", "a boundary", "L", "repetition",
     "S016: setting boundaries", "high", None,
     "'make this…use it' trong câu không đánh", 1, None, None, "LC",
     None),
    # [Phase-2] For example ← S016: nối additive-minh dụ (H&H §5.4
    # exemplification) — S017 minh họa cho lời khuyên 'Start small' câu
    # trước; VI 'Ví dụ' giữ 1-1. (Phát hiện khi săn nhóm 5, ngoài 10
    # nhóm — H&H §5.)
    ("S017", "For example", "C", "additive",
     "S016: Start small when you're setting boundaries", "high", None,
     "H&H §5.4 additive (exemplification): mở câu minh họa lời khuyên "
     "S016; VI 'Ví dụ' 1-1", 1, None, None, "LC", None),
    # [Phase-2] the whole family ← many families (S014): chuỗi
    # family/gia đình bị sót (H&H §6.2 reiteration; TNT §26 phép lặp);
    # referent chuyển phổ quát → gia đình độc giả nên alt None.
    ("S017", "the whole family", "L", "repetition",
     "S014: quite common for many families", "med", None,
     "lặp family (families → the whole family) — H&H §6.2; 'this/it' "
     "trong câu không đánh", 1, None, None, "LC", None),
    # S020
    ("S020", "your kids", "L", "repetition",
     "S008: kids", "high", None, None, 1, None, None, "LC", None),
    ("S020", "being outside", "L", "repetition",
     "S019: Get outside", "high", None,
     "VI S019 bỏ 'outside' nên không có hàng VI", 1, None, None,
     "LC", None),
    # S022
    ("S022", "Young kids", "L", "repetition",
     "S020: your kids", "high", None, "'their' trong câu không đánh",
     1, None, None, "LC", None),
    # S023
    ("S023", "with them", "R", "personal",
     "S022: Young kids", "high", None, None, 1, None, None, "LC",
     "A"),
    # S024
    ("S024", "tips", "L", "repetition",
     "S011: Her tips", "high", None, "tips to build these activities",
     1, None, None, "LC", None),
    ("S024", "these activities", "R", "demonstrative",
     "S023: talking, playing, reading and singing", "high", None, None,
     1, None, None, "LC", "A"),
    # S029
    ("S029", "children", "L", "repetition",
     "S022: Young kids", "high", None,
     "Involving children; 'they will cooperate' trong câu không đánh",
     1, None, None, "LC", None),
    ("S029", "screen limits", "L", "repetition",
     "S007: time limits + S008: screen use", "high", None,
     "kết 2 chuỗi screen + limits", 1, None, None, "LC", None),
    # [Phase-2] cooperate ↔ resistance (S004): phép đối liên câu (TNT
    # §30; H&H §6.4 opposites) — 'resistance' (S004) đối lập
    # 'cooperate' khi trẻ được tham gia (S029); VI phản kháng ↔ hợp tác
    # giữ 1-1.
    ("S029", "cooperate", "L", "antonym",
     "S004: resistance or difficulty in sticking to rules", "med",
     None,
     "phép đối cooperate ↔ resistance (TNT §30; khoảng cách xa S004–"
     "S029 nhưng là bản lề lập luận của bài)", 1, None, None, "LC",
     None),
    # S030
    ("S030", "time limits", "L", "repetition",
     "S007: time limits on screen use", "high", None,
     "'setting' lặp (S016) trong cụm, ghi note", 1, None, None, "LC",
     None),
    ("S030", "devices", "L", "repetition",
     "S003: other devices", "high", None, "storing devices", 1, None,
     None, "LC", None),
    # [Phase-2] A plan ← S029: danh từ tổng quát bridging (H&H §6.1
    # general word; 'plan' thuộc danh sách gợi ý của protocol nhóm 3) —
    # tóm chỉ việc thiết lập giới hạn vừa nêu; VI 'kế hoạch' đối xứng.
    ("S030", "plan", "L", "general word",
     "S029: Involving children in setting screen limits", "med", None,
     "danh từ tổng quát tóm chỉ tình huống câu trước (H&H §6.1); mạo "
     "từ bất định nên alt None", 1, None, None, "LC", None),
    # S031
    ("S031", "younger children", "L", "repetition",
     "S029: children", "high", None,
     "'also' trong câu không đánh C", 1, None, None, "LC", None),
    ("S031", "the rules", "L", "repetition",
     "S004: sticking to rules", "high", None, None, 1, None, None,
     "LC", None),
    # S032
    ("S032", "children", "L", "repetition",
     "S031: younger children", "high", None,
     "'It's also important' — it giả chủ ngữ không đánh", 1, None,
     None, "LC", None),
    ("S032", "limits", "L", "repetition",
     "S029: screen limits", "high", None,
     "'sticking' lặp (S004) trong cụm, ghi note", 1, None, None,
     "LC", None),
    ("S032", "enforcing this", "L", "repetition",
     "S003: enforcing these", "high", None,
     "lặp 'enforcing'; 'this' trong cụm chỉ hậu quả (trong câu)", 1,
     None, None, "LC", None),
    # S033
    ("S033", "screen use", "L", "repetition",
     "S029: screen limits", "high", None,
     "alternatives to screen use", 1, None, None, "LC", None),
    ("S033", "your child", "L", "repetition",
     "S031: younger children", "high", None, None, 1, None, None,
     "LC", None),
    ("S033", "with screens", "L", "repetition",
     "S017: screens", "high", None,
     "engaged with screens; VI gộp vào occ-note 'sử dụng màn hình'",
     1, None, None, "LC", None),
    ("S033", "research fellow", "L", "repetition",
     "S010: a researcher", "high", None,
     "researcher → research fellow; 'Research Institute' là tên riêng",
     1, None, None, "LC", None),
    # S034
    ("S034", "She", "R", "personal",
     "S033: Dr Nandi Vijayakumar", "high", None, None, 1, None, None,
     "LC", "A"),
    ("S034", "they", "R", "personal",
     "S033: your child", "high", None,
     "activities they enjoy; VI hiện thực hóa thành 'trẻ' (L)", 1,
     None, None, "LC", "A"),
    ("S034", "online activities", "L", "repetition",
     "S024: these activities", "high", None, None, 1, None, None,
     "LC", None),
    # S035
    ("S035", "Engaging children", "L", "repetition",
     "S034: they", "high", None,
     "'them' trong câu chỉ children, không đánh", 1, None, None, "LC",
     None),
    ("S035", "this process", "R", "demonstrative",
     "S034: recreate some of the online activities", "high", None,
     None, 1, None, None, "LC", "A"),
    # S036
    ("S036", "Vijayakumar", "L", "repetition",
     "S033: Dr Nandi Vijayakumar", "high", None,
     "'they/their peers' trong câu không đánh", 1, None, None, "LC",
     None),
    ("S036", "adolescents", "L", "synonym",
     "S028: Tips for older children and teenagers — tiểu đề", "med",
     None, "tiểu đề làm tiền trạm", 1, None, None, "LC", None),
    # [Phase-2] connecting ← connect (S017): chuỗi connect bị sót (H&H
    # §6.2 reiteration) — kết nối gắn kết gia đình (S017) vọng lại kết
    # nối bạn bè trực tuyến (S036); VI 'kết nối' lặp nguyên hình.
    ("S036", "connecting", "L", "repetition",
     "S017: use it as a chance to connect and bond", "med", None,
     "lặp connect (connecting with their peers online) — H&H §6.2", 1,
     None, None, "LC", None),
    # S037
    ("S037", "They", "R", "personal",
     "S036: adolescents", "high", None,
     "mở quote; [Phase-2 đính chính] 'friends' occ 1 đã có hàng riêng "
     "(← peers S036), occ 2 trong câu không đánh", 1, None, None,
     "LC", "A"),
    # [Phase-2] in person ↔ online (S036): phép đối liên câu (TNT §30;
    # H&H §6.4 opposites) — VI bỏ 'in person' (dịch 'đi chơi với bạn
    # bè') nên tie EN-only; dịch chuyển từ vựng rơi, ghi §7.
    ("S037", "in person", "L", "antonym",
     "S036: connecting with their peers online", "high", None,
     "phép đối in person ↔ online (TNT §30); VI không có đối ứng từ "
     "vựng", 1, None, None, "LC", None),
    # [Phase-2] friends ← peers (S036): đồng nghĩa liên câu (H&H §6.2
    # reiteration); occ 2 'involve their friends' cùng chuỗi trong câu
    # không đánh thêm.
    ("S037", "friends", "L", "synonym",
     "S036: connecting with their peers online", "high", None,
     "friends ≈ peers (H&H §6.2); occ 1 (occ 2 trong câu không đánh "
     "thêm)", 1, None, None, "LC", None),
    # [Phase-2] extracurricular activities ← online activities (S034):
    # chuỗi activities bị sót ở S037 (H&H §6.2) — S059 đã có hàng,
    # S037 là mắt nối thiếu; VI 'hoạt động ngoại khóa' đối xứng.
    ("S037", "extracurricular activities", "L", "repetition",
     "S034: recreate some of the online activities", "high", None,
     "lặp activities (extracurricular activities) — H&H §6.2", 1,
     None, None, "LC", None),
    # S039
    ("S039", "Vijayakumar", "L", "repetition",
     "S036: Vijayakumar", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] content ← tiểu đề S038: tiểu đề làm tiền trạm (tiền lệ
    # adolescents ← S028) — H&H §6.2 reiteration; VI 'nội dung' đối
    # xứng.
    ("S039", "content", "L", "repetition",
     "S038: The type of content can make a difference — tiểu đề",
     "high", None,
     "lặp content (educational and interactive content) — H&H §6.2; "
     "tiểu đề S038 làm tiền trạm", 1, None, None, "LC", None),
    # S040
    ("S040", "However", "C", "adversative",
     "S039: positive impact if consumed in moderation", "high", None,
     None, 1, None, None, "LC", None),
    ("S040", "children", "L", "repetition",
     "S035: Engaging children", "high", None,
     "keep children engaged — 'engaged' lặp (S033) trong cụm, ghi note",
     1, None, None, "LC", None),
    # [Phase-2] video games ← games (S030): chuỗi games bị sót (H&H
    # §6.2 reiteration) — tiền trạm gần nhất 'websites or games'
    # (S030); VI 'trò chơi' đối xứng.
    ("S040", "video games", "L", "repetition",
     "S030: particular websites or games", "high", None,
     "lặp games (some video games) — H&H §6.2", 1, None, None, "LC",
     None),
    # S041
    # [Phase-2] RECLASSIFY sub nominal→comparative (H&H §2.5: 'such' =
    # quy chiếu so sánh similarity — nhóm 1 checklist); cat/ref giữ nguyên.
    ("S041", "Such constant stimulation", "R", "comparative",
     "S040: offering rewards such as positive comments", "high", None,
     "[Phase-2] H&H §2.5: 'Such' quy chiếu so sánh (similarity) tổng "
     "chỉ cơ chế phần thưởng vừa kể; trước đây ghi nominal", 1, None,
     None, "LC", "A"),
    ("S041", "these digital experiences", "R", "demonstrative",
     "S040: video games and social media platforms", "high", None,
     "'digital' lặp (S006) bên trong cụm, ghi note", 1, None, None,
     "LC", "A"),
    ("S041", "she says", "R", "personal",
     "S039: Vijayakumar", "high", None, None, 1, None, None, "LC",
     "A"),
    # [Phase-2] problematic ← problematic (S008): lặp liên câu xa (H&H
    # §6.2) — câu hỏi 'whether it's problematic' (S008) vọng lại
    # 'problematic outcomes' (S041); VI 'vấn đề' lặp tương tự.
    ("S041", "problematic", "L", "repetition",
     "S008: whether it's problematic", "med", None,
     "lặp problematic (problematic outcomes) — H&H §6.2; đối lập cục "
     "bộ với 'positive impact' (S039) là quan hệ phụ, ghi §6", 1, None,
     None, "LC", None),
    # S042
    ("S042", "social media", "L", "repetition",
     "S040: social media platforms", "high", None,
     "'also' trong câu không đánh C", 1, None, None, "LC", None),
    # S043
    ("S043", "kids", "L", "repetition",
     "S029: children", "high", None,
     "For most kids though; 'their' trong câu không đánh", 1, None,
     None, "LC", None),
    ("S043", "screen time", "L", "repetition",
     "S011: the amount of screen time", "high", None, None, 1, None,
     None, "LC", None),
    # [Phase-2] though ← S042: RECLASSIFY quyết định 'trong câu' của
    # Phase-1 (analysis §5 cũ) — 'though' là conjunct adversative (H&H
    # §5.5) đối lập cả loạt cảnh báo S040–S042 → [LC]; VI 'Tuy nhiên'
    # đầu câu (ngoài 10 nhóm — H&H §5, phát hiện khi săn nhóm 5).
    ("S043", "though", "C", "adversative",
     "S042: social comparisons, feelings of being left out and "
     "cyberbullying", "med", None,
     "H&H §5.5 adversative: 'For most kids though' nhượng bộ đối lập "
     "loạt cảnh báo câu trước; VI 'Tuy nhiên' đầu câu", 1, None, None,
     "LC", None),
    # [Phase-2] development ← development (S039): lặp liên câu (H&H
    # §6.2); VI 'sự phát triển' đối xứng 1-1.
    ("S043", "development", "L", "repetition",
     "S039: a positive impact on development", "high", None,
     "lặp development (their development and health) — H&H §6.2", 1,
     None, None, "LC", None),
    # [Phase-2] health ← healthy (S006): lặp hình vị qua chuyển từ loại
    # (H&H §6.2); VI 'sức khỏe' ← 'khỏe mạnh' cùng cơ chế.
    ("S043", "health", "L", "repetition",
     "S006: keeps your young person safe and healthy", "med", None,
     "lặp healthy → health (H&H §6.2); VI khỏe mạnh → sức khỏe", 1,
     None, None, "LC", None),
    # S044
    ("S044", "digital devices", "L", "repetition",
     "S003: other devices + S006: digital media", "high", None,
     "kết 2 chuỗi digital + devices", 1, None, None, "LC", None),
    ("S044", "Melbourne", "L", "repetition",
     "S004: The Royal Children's Hospital in Melbourne", "high", None,
     "trong 'The University of Melbourne'", 1, None, None, "LC",
     None),
    # S045
    ("S045", "They", "R", "personal",
     "S044: digital devices", "high", None,
     "mở quote 'They could be linked'", 1, None, None, "LC", "A"),
    ("S045", "the parents", "L", "repetition",
     "S008: parents", "high", None,
     "supervision of the parents", 1, None, None, "LC", None),
    ("S045", "reading", "L", "repetition",
     "S023: reading and singing", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] playing ← playing (S023): lặp động từ liên câu (H&H
    # §6.2) — hoạt động ngoài màn hình (S023) vọng lại trong hoạt động
    # có lợi trên màn hình (S045); VI 'chơi' ← 'chơi đùa' đối xứng.
    ("S045", "playing", "L", "repetition",
     "S023: talking, playing, reading and singing", "high", None,
     "lặp playing (playing some memory games) — H&H §6.2", 1, None,
     None, "LC", None),
    # [Phase-2] games ← video games (S040): chuỗi games khép vòng (H&H
    # §6.2) — video games (cần thận trọng) ↔ memory games (có lợi).
    ("S045", "games", "L", "repetition",
     "S040: some video games and social media platforms", "high",
     None, "lặp games (memory games) — H&H §6.2", 1, None, None, "LC",
     None),
    # S047
    ("S047", "four children", "L", "repetition",
     "S043: most kids", "high", None,
     "'early childhood education' cụm cố định, không đánh (VI khác — "
     "xem TT)", 1, None, None, "LC", None),
    # S048
    ("S048", "She", "R", "personal",
     "S047: Caroline Maxwell", "high", None, None, 1, None, None,
     "LC", "A"),
    ("S048", "her children", "L", "repetition",
     "S047: four children", "high", None,
     "'they are allowed', 'ask her' trong câu không đánh", 1, None,
     None, "LC", None),
    ("S048", "screen time", "L", "repetition",
     "S043: some amount of screen time", "high", None, None, 1, None,
     None, "LC", None),
    # S049
    ("S049", "screens", "L", "repetition",
     "S043: screen time", "high", None,
     "no screens during meals; VI đổi thành 'thiết bị điện tử'", 1,
     None, None, "LC", None),
    ("S049", "devices", "L", "repetition",
     "S044: digital devices", "high", None, "no devices after dinner",
     1, None, None, "LC", None),
    # [Phase-2] meals ← mealtime (S017): lặp liên câu (H&H §6.2) — VI
    # S017 bỏ 'mealtime' nên 'bữa ăn' (S049 TT) là nhắc đầu, không có
    # hàng VI; dịch chuyển từ vựng rơi/tái sinh, ghi §7.
    ("S049", "meals", "L", "repetition",
     "S017: if you don't want screens at mealtime", "med", None,
     "lặp mealtime → meals (during meals) — H&H §6.2; hàng EN-only",
     1, None, None, "LC", None),
    # S050
    ("S050", "Maxwell", "L", "repetition",
     "S047: Caroline Maxwell", "high", None,
     "'uses' động từ mờ, không đánh", 1, None, None, "LC", None),
    ("S050", "digital detoxes", "L", "repetition",
     "S044: digital devices", "high", None, "lặp 'digital'", 1, None,
     None, "LC", None),
    # [Phase-2] holidays ← summer holidays (S001): lặp liên câu xa (H&H
    # §6.2) — dịp nghỉ hè (S001) quay lại thành dịp 'cai nghiện'
    # (S050); VI 'ngày lễ' là từ mới nên hàng EN-only.
    ("S050", "holidays", "L", "repetition",
     "S001: during the summer holidays", "med", None,
     "lặp holidays (uses holidays) — H&H §6.2; VI 'ngày lễ' từ mới",
     1, None, None, "LC", None),
    # S051
    ("S051", "She", "R", "personal",
     "S050: Maxwell", "high", None,
     "'also' trong câu không đánh; 'it made' trong câu không đánh", 1,
     None, None, "LC", "A"),
    ("S051", "only TV", "L", "repetition",
     "S014: Leaving a TV on", "high", None, None, 1, None, None, "LC",
     None),
    ("S051", "her kids", "L", "repetition",
     "S047: four children", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] disconnected ← digital detoxes (S050): collocation quá
    # trình–cách thực hiện (H&H §6.4; TNT §32 phép liên tưởng) — 'cai
    # nghiện' được hiện thực hóa bằng 'ngắt kết nối TV'; VI đối xứng.
    ("S051", "disconnected", "L", "collocation",
     "S050: introduce digital detoxes", "med", None,
     "collocation detox ↔ disconnect (H&H §6.4; TNT §32)", 1, None,
     None, "LC", None),
    # [Phase-2] household ← house (S048): lặp hình vị qua chuyển từ
    # loại (H&H §6.2); VI 'trong nhà' lặp nguyên văn — ghi §7.
    ("S051", "household", "L", "repetition",
     "S048: tasks around the house", "med", None,
     "lặp house → household (her household's only TV) — H&H §6.2", 1,
     None, None, "LC", None),
    # S052
    ("S052", "They", "R", "personal",
     "S051: her kids", "high", None,
     "'they' viết thường lần 2, 3 trong quote cùng chuỗi, không đánh",
     1, None, None, "LC", "A"),
    ("S052", "reading", "L", "repetition",
     "S045: reading", "high", None, "they were reading more", 1, None,
     None, "LC", None),
    ("S052", "Maxwell", "L", "repetition",
     "S050: Maxwell", "high", None, None, 1, None, None, "LC", None),
    ("S052", "around the house", "L", "repetition",
     "S048: tasks around the house", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] the only downside ← S051: danh từ tổng quát bridging (H&H
    # §6.1 general word) + mạo từ xác định → alt 'R: the' (mapping
    # §3.6); VI 'nhược điểm duy nhất' đối xứng, định danh bằng ngữ cảnh
    # (mapping §4).
    ("S052", "downside", "L", "general word",
     "S051: disconnected her household's only TV for an entire school "
     "term", "med", "R: the",
     "danh từ tổng quát tóm chỉ tình huống ngắt TV câu trước (H&H "
     "§6.1)", 1, None, None, "LC", None),
    # S053
    ("S053", "She", "R", "personal",
     "S052: Maxwell says", "high", None,
     "'she still finds' viết thường trong câu không đánh", 1, None,
     None, "LC", "A"),
    ("S053", "her children", "L", "repetition",
     "S048: her children", "high", None, None, 1, None, None, "LC",
     None),
    ("S053", "physical activity", "L", "repetition",
     "S020: the benefits of physical activity", "high", None, None, 1,
     None, None, "LC", None),
    ("S053", "avoid screens", "L", "repetition",
     "S049: no screens", "high", None, None, 1, None, None, "LC",
     None),
    ("S053", "the rules", "L", "repetition",
     "S031: follow the rules", "high", None, None, 1, None, None,
     "LC", None),
    # S054
    ("S054", "Children", "L", "repetition",
     "S053: her children", "high", None, None, 1, None, None, "LC",
     None),
    ("S054", "boundaries", "L", "repetition",
     "S017: make this a boundary", "high", None,
     "push boundaries; 'it can feel' trong câu không đánh", 1, None,
     None, "LC", None),
    ("S054", "rules", "L", "repetition",
     "S053: maintain the rules", "high", None, "reinforce rules", 1,
     None, None, "LC", None),
    ("S054", "she says", "R", "personal",
     "S053: She (Maxwell)", "high", None, None, 1, None, None, "LC",
     "A"),
    # S056
    ("S056", "Sahlberg", "L", "repetition",
     "S044: Pasi Sahlberg", "high", None, None, 1, None, None, "LC",
     None),
    ("S056", "parents", "L", "repetition",
     "S045: the parents", "high", None, "urges parents", 1, None,
     None, "LC", None),
    ("S056", "their child", "L", "repetition",
     "S033: your child", "high", None,
     "'their' trong câu chỉ parents, không đánh", 1, None, None, "LC",
     None),
    ("S056", "the digital space", "L", "repetition",
     "S050: digital detoxes", "high", None,
     "lặp 'digital'; 'it's not seen' trong câu không đánh", 1, None,
     None, "LC", None),
    # [Phase-2] interest ← tiểu đề S055: tiểu đề làm tiền trạm (H&H
    # §6.2; tiền lệ adolescents ← S028) — 'Take an interest' (S055) lặp
    # ở 'show an interest' (S056); VI 'quan tâm' lặp nguyên hình.
    ("S056", "interest", "L", "repetition",
     "S055: Take an interest in what your kids do online — tiểu đề",
     "high", None,
     "lặp interest (show an interest) — H&H §6.2; tiểu đề S055 làm "
     "tiền trạm", 1, None, None, "LC", None),
    # S057
    ("S057", "kids", "L", "repetition",
     "S054: Children", "high", None,
     "leave kids by themselves; 'we' x3 hư chỉ cha mẹ, không đánh",
     1, None, None, "LC", None),
    ("S057", "these devices", "R", "demonstrative",
     "S044: digital devices", "high", None,
     "'that/they/those things' trong câu không đánh", 1, None, None,
     "LC", "A"),
    # [Phase-2] limit ← limits (S032): lặp hình vị khép chuỗi
    # limit/restrictions (S001→S003→S007→S029/S030/S032→S057; H&H §6.2);
    # VI 'hạn chế' khép chuỗi riêng (S001→S003→S057).
    ("S057", "limit", "L", "repetition",
     "S032: for not sticking to limits", "med", None,
     "lặp limit (we should limit that) — H&H §6.2; 'that' trong câu "
     "không đánh", 1, None, None, "LC", None),
    # [Phase-2] care ← interest (S056): đồng nghĩa (H&H §6.2) — 'show
    # an interest' → 'we care'; VI 'quan tâm' lặp nguyên hình (khác EN
    # đổi từ), ghi §7.
    ("S057", "care", "L", "synonym",
     "S056: to show an interest in what their child is doing", "med",
     None,
     "care ≈ interest (we care and are curious) — H&H §6.2", 1, None,
     None, "LC", None),
    # S058 (caption)
    ("S058", "Pasi Sahlberg", "L", "repetition",
     "S044: Pasi Sahlberg", "high", None,
     "caption trích dẫn; lặp cả danh xưng 'Professor'", 1, None, None,
     "LC", None),
    ("S058", "The University of Melbourne", "L", "repetition",
     "S044: The University of Melbourne", "high", None,
     "caption trích dẫn", 1, None, None, "LC", None),
    # S059
    ("S059", "a child", "L", "repetition",
     "S056: their child", "high", None,
     "'their' trong câu không đánh", 1, None, None, "LC", None),
    ("S059", "their activities", "L", "repetition",
     "S034: online activities", "high", None,
     "'this could be a sign' trong câu không đánh", 1, None, None,
     "LC", None),
    ("S059", "the parent", "L", "repetition",
     "S056: parents", "high", None,
     "số ít; 'with them' trong câu không đánh", 1, None, None, "LC",
     None),
    ("S059", "Sahlberg", "L", "repetition",
     "S056: Sahlberg", "high", None, None, 1, None, None, "LC", None),
    # S060
    ("S060", "this type of relationship", "R", "demonstrative",
     "S056–S059: sự quan tâm của cha mẹ đến việc con làm trên không "
     "gian số", "high", None,
     "'we…our' hư chỉ; 'it is that that' trong câu không đánh", 1,
     None, None, "LC", "A"),
    ("S060", "our kids", "L", "repetition",
     "S057: kids", "high", None, "'they grow older' trong câu", 1,
     None, None, "LC", None),
    # [Phase-2] sustain ← maintain (S053): đồng nghĩa liên câu (H&H
    # §6.2) — 'maintain the rules' (S053) vọng lại 'sustain and
    # continue' (S060); VI 'duy trì' lặp nguyên hình.
    ("S060", "sustain", "L", "synonym",
     "S053: difficult to maintain the rules", "med", None,
     "sustain ≈ maintain (will sustain and continue) — H&H §6.2", 1,
     None, None, "LC", None),
]

TT = [
    # S002
    ("S002", "Những ngày hè dài", "L", "repetition",
     "S001: kỳ nghỉ hè", "high", None, "lặp 'hè'", 1, None, None,
     "LC", None),
    ("S002", "thiết bị điện tử", "L", "repetition",
     "S001: các thiết bị điện tử", "high", None, None, 1, None, None,
     "LC", None),
    ("S002", "con cái", "L", "repetition",
     "S001: con bạn", "high", None, "lặp 'con'", 1, None, None, "LC",
     None),
    ("S002", "thời gian sử dụng màn hình", "L", "repetition",
     "S001: việc sử dụng màn hình", "high", None,
     "kết chuỗi thời gian + sử dụng màn hình", 1, None, None, "LC",
     None),
    # S003
    ("S003", "cha mẹ", "L", "repetition",
     "S002: các bậc cha mẹ", "high", None,
     "hiểu được lợi ích của việc; [Phase-2 đính chính] 'hạn chế' lặp "
     "S001 (hàng riêng), 'giới hạn' (S007) mới khởi tạo chuỗi", 1, None,
     None, "LC", None),
    ("S003", "các thiết bị khác", "L", "repetition",
     "S002: thiết bị điện tử", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] hạn chế ← hạn chế (S001): lặp nguyên hình bị sót (TNT
    # §26 phép lặp; H&H §6.2) — Phase-1 ghi nhầm "'hạn chế' khởi tạo
    # chuỗi" (S001 TT đã có 'hạn chế việc sử dụng màn hình'); EN đối ứng
    # limit (v.) → restrictions (n.) khác cơ chế.
    ("S003", "hạn chế", "L", "repetition",
     "S001: giúp bạn hạn chế việc sử dụng màn hình", "high", None,
     "occ 1 = 'việc hạn chế sử dụng TV' (TNT §26; occ 2 'những hạn chế "
     "này' là hậu chỉ trong câu, không đánh)", 1, None, None, "LC",
     None),
    # S004
    ("S004", "một bà mẹ bốn con", "L", "repetition",
     "S002: các bậc cha mẹ", "high", None,
     "lặp hình vị 'mẹ'; 'quy tắc' khởi tạo chuỗi", 1, None, None,
     "LC", None),
    # S006
    ("S006", "Đây", "R", "demonstrative",
     "S005: không có giải pháp toàn diện nào", "high", None,
     "VI tự sinh chỉ từ; EN đối ứng chỉ là it giả chủ ngữ", 1, None,
     None, "LC", "A"),
    ("S006", "sử dụng phương tiện truyền thông kỹ thuật số", "L",
     "repetition", "S001: việc sử dụng màn hình", "high", None,
     "lặp 'sử dụng'; 'kỹ thuật số/truyền thông' từ mới", 1, None,
     None, "LC", None),
    # S007
    ("S007", "Rhodes", "L", "repetition",
     "S004: Bác sĩ nhi khoa Anthea Rhodes", "high", None, None, 1,
     None, None, "LC", None),
    ("S007", "sử dụng màn hình", "L", "repetition",
     "S001: việc sử dụng màn hình", "high", None, None, 1, None, None,
     "LC", None),
    ("S007", "trẻ em", "L", "repetition",
     "S006: giúp trẻ an toàn", "high", None,
     "'trẻ đã lớn' lần 2 trong câu cùng chuỗi, không đánh", 1, None,
     None, "LC", None),
    # [Phase-2] các quy tắc ← các quy tắc (S004): chuỗi quy tắc bị sót
    # (TNT §26 phép lặp) — EN 'the rules' (S007) tương ứng 1-1; VI
    # không mạo từ (mapping §4).
    ("S007", "các quy tắc", "L", "repetition",
     "S004: tuân thủ các quy tắc", "high", None,
     "lặp các quy tắc (nếu các quy tắc có thể được thảo luận) — TNT "
     "§26", 1, None, None, "LC", None),
    # S008
    ("S008", "trẻ em", "L", "repetition",
     "S007: với trẻ em", "high", None, None, 1, None, None, "LC",
     None),
    ("S008", "sử dụng màn hình", "L", "repetition",
     "S007: sử dụng màn hình", "high", None, None, 1, None, None,
     "LC", None),
    ("S008", "phụ huynh", "L", "synonym",
     "S003: cha mẹ", "high", None,
     "phụ huynh ≈ cha mẹ; 'việc này' trong câu không đánh", 1, None,
     None, "LC", None),
    # S010
    ("S010", "sử dụng màn hình", "L", "repetition",
     "S008: sử dụng màn hình", "high", None,
     "'Viện nghiên cứu trẻ em Úc' là tên riêng, không đánh", 1, None,
     None, "LC", None),
    ("S010", "trẻ em dưới năm tuổi", "L", "repetition",
     "S008: trẻ em", "high", None, None, 1, None, None, "LC", None),
    # S011
    ("S011", "bà", "R", "personal",
     "S010: Tiến sĩ Mary Brushe", "high", None, "các mẹo của bà", 1,
     None, None, "LC", "A"),
    ("S011", "mẹo", "L", "repetition",
     "S001: một số mẹo", "high", None, None, 1, None, None, "LC",
     None),
    ("S011", "thời gian sử dụng màn hình", "L", "repetition",
     "S002: thời gian sử dụng màn hình", "high", None, None, 1, None,
     None, "LC", None),
    # S013
    ("S013", "TV", "L", "repetition",
     "S003: sử dụng TV", "high", None,
     "occ 1: lặp 2 lần trong câu (xem TV, tắt TV), chọn lần 1; EN dùng "
     "'the screen'", 1, None, None, "LC", None),
    # S014
    ("S014", "TV", "L", "repetition",
     "S013: TV", "high", None,
     "bật TV rồi làm việc (nguồn VI diễn đạt sai lệch, ghi §8)", 1,
     None, None, "LC", None),
    ("S014", "trẻ nhỏ", "L", "repetition",
     "S007: trẻ em", "high", None,
     "'điều này' trong câu không đánh", 1, None, None, "LC", None),
    # [Phase-2] bật ↔ tắt (S013): phép đối liên câu (TNT §30; H&H §6.4
    # opposites) — lời khuyên 'hãy tắt TV' đối lập thói quen 'bật TV'
    # (nguồn VI diễn đạt 'làm việc' sai lệch, ghi §8).
    ("S014", "bật", "L", "antonym",
     "S013: nếu không có ai xem TV, hãy tắt TV", "high", None,
     "phép đối bật ↔ tắt (Việc bật TV rồi làm việc) — TNT §30", 1,
     None, None, "LC", None),
    # S017
    ("S017", "xem TV", "L", "repetition",
     "S014: TV", "high", None,
     "VI đổi 'screens at mealtime' thành 'xem TV', ghi §8", 1, None,
     None, "LC", None),
    ("S017", "ranh giới này", "R", "demonstrative",
     "S016: ranh giới", "high", None,
     "hậu chỉ từ 'này' + lặp 'ranh giới'; EN 'a boundary' chỉ là L; "
     "'coi đó' trong câu không đánh", 1, None, None, "LC", "A"),
    # [Phase-2] Ví dụ ← S016: nối additive-minh dụ (H&H §5.4
    # exemplification) — đối xứng EN 'For example' 1-1. (Phát hiện khi
    # săn nhóm 5, ngoài 10 nhóm — H&H §5.)
    ("S017", "Ví dụ", "C", "additive",
     "S016: Hãy bắt đầu từ những điều nhỏ nhặt khi bạn đặt ra ranh "
     "giới", "high", None,
     "H&H §5.4 additive (exemplification): minh họa cho lời khuyên "
     "S016; EN 'For example' 1-1", 1, None, None, "LC", None),
    # [Phase-2] cả gia đình ← nhiều gia đình (S014): chuỗi gia đình bị
    # sót (TNT §26 phép lặp); referent phổ quát → gia đình độc giả.
    ("S017", "cả gia đình", "L", "repetition",
     "S014: khá phổ biến đối với nhiều gia đình", "med", None,
     "lặp gia đình (cho cả gia đình) — TNT §26", 1, None, None, "LC",
     None),
    # S020
    ("S020", "con bạn", "L", "repetition",
     "S001: con bạn", "high", None,
     "bạn và con bạn; EN còn có hàng 'being outside' — VI không có vì "
     "S019 bỏ 'outside'", 1, None, None, "LC", None),
    # [Phase-2] tận hưởng ← Tận hưởng (S019): lặp nguyên hình (TNT §26
    # phép lặp) — VI tự sinh chuỗi không có đối ứng EN (EN S019 'Get
    # outside' → S020 'enjoy', không lặp); dịch chuyển tự sinh, ghi §7.
    ("S020", "tận hưởng", "L", "repetition",
     "S019: Tận hưởng thiên nhiên", "high", None,
     "lặp tận hưởng (sẽ tận hưởng những lợi ích) — TNT §26; EN không "
     "có chuỗi tương ứng", 1, None, None, "LC", None),
    # S022
    ("S022", "Trẻ nhỏ", "L", "repetition",
     "S014: trẻ nhỏ", "high", None, "'của chúng' trong câu không đánh",
     1, None, None, "LC", None),
    # S023
    ("S023", "chúng", "R", "personal",
     "S022: Trẻ nhỏ", "high", None, "hát cùng chúng", 1, None, None,
     "LC", "A"),
    # S024
    ("S024", "các mẹo", "L", "repetition",
     "S011: Các mẹo", "high", None, None, 1, None, None, "LC", None),
    ("S024", "những hoạt động này", "R", "demonstrative",
     "S023: trò chuyện, chơi đùa, đọc sách và hát", "high", None,
     "hậu chỉ từ 'này'", 1, None, None, "LC", "A"),
    # S029
    ("S029", "trẻ", "L", "repetition",
     "S022: Trẻ nhỏ", "high", None,
     "occ 1: lần 2 ('giúp trẻ hợp tác') trong câu cùng chuỗi, không "
     "đánh", 1, None, None, "LC", None),
    ("S029", "thời gian sử dụng màn hình", "L", "repetition",
     "S011: thời gian sử dụng màn hình", "high", None,
     "'giới hạn' khởi tạo chuỗi VI", 1, None, None, "LC", None),
    # [Phase-2] hợp tác ↔ phản kháng (S004): phép đối liên câu (TNT
    # §30; H&H §6.4 opposites) — EN cooperate ↔ resistance đối xứng.
    ("S029", "hợp tác", "L", "antonym",
     "S004: việc phản kháng hoặc khó khăn trong việc tuân thủ các quy "
     "tắc", "med", None,
     "phép đối hợp tác ↔ phản kháng (giúp trẻ hợp tác nhiều hơn) — TNT "
     "§30", 1, None, None, "LC", None),
    # S030
    ("S030", "giới hạn thời gian", "L", "repetition",
     "S029: giới hạn thời gian sử dụng màn hình", "high", None, None,
     1, None, None, "LC", None),
    ("S030", "các thiết bị", "L", "repetition",
     "S003: các thiết bị khác", "high", None, "cất các thiết bị", 1,
     None, None, "LC", None),
    # [Phase-2] kế hoạch ← S029: danh từ tổng quát bridging (H&H §6.1
    # general word) — 'Một kế hoạch' tóm chỉ việc thiết lập giới hạn ở
    # câu trước; EN 'A plan' đối xứng.
    ("S030", "kế hoạch", "L", "general word",
     "S029: cho trẻ tham gia thiết lập giới hạn thời gian sử dụng màn "
     "hình", "med", None,
     "danh từ tổng quát tóm chỉ tình huống câu trước (H&H §6.1)", 1,
     None, None, "LC", None),
    # S031
    ("S031", "trẻ nhỏ", "L", "repetition",
     "S029: trẻ", "high", None,
     "'cũng' trong câu không đánh C", 1, None, None, "LC", None),
    ("S031", "các quy tắc", "L", "repetition",
     "S004: các quy tắc", "high", None, None, 1, None, None, "LC",
     None),
    # S032
    ("S032", "trẻ", "L", "repetition",
     "S031: trẻ nhỏ", "high", None,
     "'Điều quan trọng' là nominalizer, không đánh; 'điều này' trong "
     "câu không đánh", 1, None, None, "LC", None),
    ("S032", "giới hạn", "L", "repetition",
     "S030: giới hạn thời gian", "high", None,
     "không tuân thủ giới hạn", 1, None, None, "LC", None),
    ("S032", "thực thi", "L", "repetition",
     "S003: việc thực thi những hạn chế này", "high", None,
     "lặp 'thực thi'", 1, None, None, "LC", None),
    # S033
    ("S033", "sử dụng màn hình", "L", "repetition",
     "S029: sử dụng màn hình", "high", None,
     "occ 1: lần 2 ('thích sử dụng màn hình') trong câu cùng chuỗi, "
     "không đánh — EN có thêm hàng 'with screens' riêng", 1, None,
     None, "LC", None),
    ("S033", "con bạn", "L", "repetition",
     "S020: con bạn", "high", None, None, 1, None, None, "LC", None),
    ("S033", "nghiên cứu viên tâm lý", "L", "synonym",
     "S010: nhà nghiên cứu", "high", None,
     "nhà nghiên cứu → nghiên cứu viên; 'Viện nghiên cứu trẻ em "
     "Murdoch' là tên riêng", 1, None, None, "LC", None),
    # [Phase-2] giải pháp ← giải pháp (S005): lặp nguyên hình liên câu
    # xa (TNT §26 phép lặp) — VI tự sinh chuỗi mà EN không có đối ứng
    # từ vựng (EN 'silver bullet' → 'alternatives'); ghi §7.
    ("S033", "giải pháp", "L", "repetition",
     "S005: không có giải pháp toàn diện nào ở đây", "med", None,
     "lặp giải pháp (tìm giải pháp thay thế) — TNT §26; EN đổi từ "
     "'silver bullet' → 'alternatives'", 1, None, None, "LC", None),
    # S034
    ("S034", "Bà", "R", "personal",
     "S033: Tiến sĩ Nandi Vijayakumar", "high", None, None, 1, None,
     None, "LC", "A"),
    ("S034", "trẻ", "L", "repetition",
     "S032: trẻ", "high", None,
     "mà trẻ thích — VI hiện thực hóa đại từ EN 'they' thành danh từ",
     1, None, None, "LC", None),
    ("S034", "hoạt động trực tuyến", "L", "repetition",
     "S024: những hoạt động này", "high", None, None, 1, None, None,
     "LC", None),
    # S035
    ("S035", "trẻ", "L", "repetition",
     "S034: trẻ", "high", None,
     "occ 1: lần 2 ('giúp trẻ xao nhãng') trong câu cùng chuỗi, "
     "không đánh", 1, None, None, "LC", None),
    ("S035", "quá trình này", "R", "demonstrative",
     "S034: quá trình tái tạo hoạt động", "high", None,
     "hậu chỉ từ 'này'", 1, None, None, "LC", "A"),
    # S036
    ("S036", "thanh thiếu niên", "L", "repetition",
     "S028: Mẹo dành cho trẻ lớn và thanh thiếu niên — tiểu đề", "high",
     None, "tiểu đề làm tiền trạm; 'họ' trong câu không đánh", 1,
     None, None, "LC", None),
    ("S036", "Vijayakumar", "L", "repetition",
     "S033: Nandi Vijayakumar", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] kết nối ← kết nối (S017): lặp nguyên hình (TNT §26) —
    # kết nối gắn kết gia đình (S017) ↔ kết nối bạn bè trực tuyến
    # (S036); EN connect → connecting đối xứng.
    ("S036", "kết nối", "L", "repetition",
     "S017: cơ hội để kết nối và gắn kết", "med", None,
     "lặp kết nối (việc kết nối với bạn bè trực tuyến) — TNT §26", 1,
     None, None, "LC", None),
    # S037
    ("S037", "Họ", "R", "personal",
     "S036: thanh thiếu niên", "high", None,
     "mở quote; [Phase-2 đính chính] bạn bè occ 1 nối S036 đã có hàng "
     "riêng, occ 2 'của bạn bè' trong câu không đánh", 1,
     None, None, "LC", "A"),
    # [Phase-2] bạn bè ← bạn bè (S036): lặp nguyên hình liên câu (TNT
    # §26) — EN peers → friends đồng nghĩa; occ 2 'của bạn bè' cùng câu
    # không đánh thêm.
    ("S037", "bạn bè", "L", "repetition",
     "S036: kết nối với bạn bè trực tuyến", "high", None,
     "occ 1 = 'đi chơi với bạn bè' (TNT §26; occ 2 'có sự tham gia của "
     "bạn bè' trong câu không đánh thêm)", 1, None, None, "LC", None),
    # [Phase-2] hoạt động ngoại khóa ← hoạt động trực tuyến (S034): chuỗi
    # hoạt động bị sót ở S037 (TNT §26) — S059 đã có hàng, S037 là mắt
    # nối thiếu; EN 'extracurricular activities' đối xứng.
    ("S037", "hoạt động ngoại khóa", "L", "repetition",
     "S034: tái tạo một số hoạt động trực tuyến", "high", None,
     "lặp hoạt động (tham gia các hoạt động ngoại khóa) — TNT §26; "
     "'ngoại khóa' là thông tin mới", 1, None, None, "LC", None),
    # S039
    ("S039", "Vijayakumar", "L", "repetition",
     "S036: Vijayakumar", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] nội dung ← tiểu đề S038: tiểu đề làm tiền trạm (TNT
    # §26; tiền lệ thanh thiếu niên ← S028) — EN 'content' đối xứng.
    ("S039", "nội dung", "L", "repetition",
     "S038: Loại nội dung có thể tạo ra sự khác biệt — tiểu đề", "high",
     None,
     "lặp nội dung (nội dung giáo dục và tương tác) — TNT §26; tiểu đề "
     "S038 làm tiền trạm", 1, None, None, "LC", None),
    # S040
    ("S040", "Tuy nhiên", "C", "adversative",
     "S039: tác động tích cực nếu sử dụng vừa phải", "high", None,
     None, 1, None, None, "LC", None),
    ("S040", "trẻ em", "L", "repetition",
     "S010: trẻ em dưới năm tuổi", "high", None,
     "giữ trẻ em tham gia", 1, None, None, "LC", None),
    # [Phase-2] trò chơi ← trò chơi (S030): chuỗi trò chơi bị sót (TNT
    # §26 phép lặp) — tiền trạm gần nhất 'trò chơi cụ thể' (S030); EN
    # 'video games' (S040) đối xứng.
    ("S040", "trò chơi", "L", "repetition",
     "S030: các trang web hoặc trò chơi cụ thể", "high", None,
     "lặp trò chơi (một số trò chơi điện tử) — TNT §26", 1, None,
     None, "LC", None),
    # S041
    ("S041", "Bà", "R", "personal",
     "S039: Vijayakumar", "high", None, None, 1, None, None, "LC",
     "A"),
    # [Phase-2] RECLASSIFY sub nominal→comparative (H&H §2.5; nhóm 1:
    # VI 'như vậy' = quy chiếu so sánh similarity); cat/ref giữ nguyên.
    ("S041", "Sự kích thích liên tục như vậy", "R", "comparative",
     "S040: cơ chế phần thưởng giữ trẻ tham gia", "high", None,
     "[Phase-2] H&H §2.5: 'như vậy' quy chiếu so sánh (similarity) tổng "
     "chỉ cơ chế phần thưởng; trước đây ghi nominal — đối xứng EN 'Such'",
     1, None, None, "LC", "A"),
    ("S041", "những trải nghiệm kỹ thuật số này", "R", "demonstrative",
     "S040: trò chơi điện tử và nền tảng truyền thông xã hội",
     "high", None, "hậu chỉ từ 'này'", 1, None, None, "LC", "A"),
    # [Phase-2] vấn đề ← vấn đề (S008): lặp nguyên hình liên câu xa
    # (TNT §26) — 'gây ra vấn đề' (S008) vọng lại 'kết quả có vấn đề';
    # EN 'problematic' lặp tương tự.
    ("S041", "vấn đề", "L", "repetition",
     "S008: liệu việc này có gây ra vấn đề hay không", "med", None,
     "lặp vấn đề (kết quả có vấn đề) — TNT §26", 1, None, None, "LC",
     None),
    # S042
    ("S042", "phương tiện truyền thông xã hội", "L", "repetition",
     "S006: phương tiện truyền thông kỹ thuật số", "high", None,
     "lặp 'phương tiện truyền thông'; 'cũng' trong câu không đánh", 1,
     None, None, "LC", None),
    # S043
    ("S043", "trẻ em", "L", "repetition",
     "S040: trẻ em", "high", None,
     "'của chúng' trong câu không đánh", 1, None, None, "LC", None),
    ("S043", "thời gian sử dụng màn hình", "L", "repetition",
     "S029: thời gian sử dụng màn hình", "high", None, None, 1, None,
     None, "LC", None),
    # [Phase-2] Tuy nhiên ← S042: nối adversative đầu câu (H&H §5.5) —
    # RECLASSIFY quyết định Phase-1 (EN 'though' bị liệt 'trong câu'):
    # VI chuyển conjunct lồng câu của EN thành connector đầu câu liên
    # câu; dịch chuyển vị trí, ghi §7.
    ("S043", "Tuy nhiên", "C", "adversative",
     "S042: so sánh xã hội, cảm giác bị bỏ rơi và bắt nạt trên mạng",
     "high", None,
     "H&H §5.5 adversative: đối lập loạt cảnh báo S040–S042; EN "
     "'though' lồng giữa câu", 1, None, None, "LC", None),
    # [Phase-2] an toàn ← an toàn (S006): lặp nguyên hình liên câu xa
    # (TNT §26) — EN đổi từ safe → okay nên chuỗi này VI-only, ghi §7.
    ("S043", "an toàn", "L", "repetition",
     "S006: giúp trẻ an toàn và khỏe mạnh", "med", None,
     "lặp an toàn (là an toàn cho sự phát triển) — TNT §26; EN đổi "
     "safe → okay", 1, None, None, "LC", None),
    # [Phase-2] sự phát triển ← sự phát triển (S039): lặp nguyên hình
    # (TNT §26); EN 'development' đối xứng 1-1.
    ("S043", "sự phát triển", "L", "repetition",
     "S039: tác động tích cực đến sự phát triển", "high", None,
     "lặp sự phát triển (cho sự phát triển và sức khỏe) — TNT §26", 1,
     None, None, "LC", None),
    # [Phase-2] sức khỏe ← khỏe mạnh (S006): lặp hình vị qua chuyển từ
    # loại (TNT §26 phép lặp); EN health ← healthy cùng cơ chế.
    ("S043", "sức khỏe", "L", "repetition",
     "S006: giúp trẻ an toàn và khỏe mạnh", "med", None,
     "lặp hình vị khỏe (khỏe mạnh → sức khỏe) — TNT §26", 1, None,
     None, "LC", None),
    # S044
    ("S044", "các thiết bị kỹ thuật số", "L", "repetition",
     "S030: các thiết bị + S006: kỹ thuật số", "high", None,
     "kết 2 chuỗi thiết bị + kỹ thuật số", 1, None, None, "LC", None),
    ("S044", "Melbourne", "L", "repetition",
     "S004: Bệnh viện Nhi Hoàng gia Melbourne", "high", None,
     "trong 'Đại học Melbourne'", 1, None, None, "LC", None),
    # S045
    ("S045", "Chúng", "R", "personal",
     "S044: các thiết bị kỹ thuật số", "high", None,
     "mở quote 'Chúng có thể'", 1, None, None, "LC", "A"),
    ("S045", "cha mẹ", "L", "repetition",
     "S008: phụ huynh", "high", None, "của cha mẹ", 1, None, None,
     "LC", None),
    ("S045", "đọc", "L", "repetition",
     "S023: đọc sách", "high", None, "đọc hoặc học số", 1, None, None,
     "LC", None),
    # [Phase-2] chơi ← chơi đùa (S023): lặp nguyên hình (TNT §26) — occ
    # 1 là động từ trong 'việc chơi'; occ 2 là chuỗi con trong 'trò
    # chơi' đã có hàng riêng (tiền lệ P26: đếm substring + ghi chú).
    ("S045", "chơi", "L", "repetition",
     "S023: trò chuyện, chơi đùa, đọc sách và hát", "high", None,
     "occ 1 = động từ 'việc chơi một số' (TNT §26; occ 2 chuỗi con "
     "trong 'trò chơi' không dùng)", 1, None, None, "LC", None),
    # [Phase-2] trò chơi ← trò chơi điện tử (S040): lặp nguyên hình
    # (TNT §26) — khép chuỗi S030 → S040 → S045.
    ("S045", "trò chơi", "L", "repetition",
     "S040: một số trò chơi điện tử", "high", None,
     "lặp trò chơi (trò chơi trí nhớ) — TNT §26", 1, None, None, "LC",
     None),
    # S047
    ("S047", "giáo dục trẻ nhỏ", "L", "repetition",
     "S031: trẻ nhỏ", "high", None,
     "VI đánh hàng này vì 'trẻ nhỏ' lặp chuỗi; EN 'early childhood' "
     "là cụm cố định không đánh", 1, None, None, "LC", None),
    ("S047", "bốn đứa con", "L", "repetition",
     "S020: con bạn", "high", None, "lặp 'con'", 1, None, None, "LC",
     None),
    # S048
    ("S048", "Cô", "R", "personal",
     "S047: Caroline Maxwell", "high", None,
     "'cô' viết thường lần 2, 3 ('con cô', 'hỏi cô') trong câu cùng "
     "chuỗi, không đánh", 1, None, None, "LC", "A"),
    ("S048", "con cô", "L", "repetition",
     "S047: bốn đứa con", "high", None, None, 1, None, None, "LC",
     None),
    ("S048", "các thiết bị điện tử", "L", "repetition",
     "S002: thiết bị điện tử", "high", None,
     "VI đổi 'screen time' thành 'thiết bị điện tử' ở đây, ghi §8", 1,
     None, None, "LC", None),
    # S049
    ("S049", "sử dụng thiết bị điện tử", "L", "repetition",
     "S048: các thiết bị điện tử", "high", None,
     "EN có 2 hàng screens + devices, VI gộp thành 1", 1, None, None,
     "LC", None),
    # S050
    ("S050", "Maxwell", "L", "repetition",
     "S047: Caroline Maxwell", "high", None, None, 1, None, None,
     "LC", None),
    ("S050", "kỹ thuật số", "L", "repetition",
     "S044: các thiết bị kỹ thuật số", "high", None,
     "cai nghiện kỹ thuật số", 1, None, None, "LC", None),
    # S051
    ("S051", "Cô", "R", "personal",
     "S050: Maxwell", "high", None,
     "'cũng' trong câu không đánh; 'điều đó' trong câu không đánh", 1,
     None, None, "LC", "A"),
    ("S051", "chiếc TV duy nhất", "L", "repetition",
     "S017: xem TV", "high", None, None, 1, None, None, "LC", None),
    ("S051", "con cô", "L", "repetition",
     "S048: con cô", "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] ngắt kết nối ← cai nghiện (S050): collocation quá trình
    # –cách thực hiện (H&H §6.4; TNT §32 phép liên tưởng) — EN
    # 'disconnected' ↔ 'digital detoxes' đối xứng.
    ("S051", "ngắt kết nối", "L", "collocation",
     "S050: phương pháp cai nghiện kỹ thuật số", "med", None,
     "collocation cai nghiện ↔ ngắt kết nối (H&H §6.4; TNT §32)", 1,
     None, None, "LC", None),
    # [Phase-2] trong nhà ← trong nhà (S048): lặp nguyên hình (TNT §26)
    # — EN house → household chuyển từ loại, khác cơ chế hai đầu, ghi
    # §7.
    ("S051", "trong nhà", "L", "repetition",
     "S048: công việc nhất định trong nhà", "high", None,
     "lặp trong nhà (chiếc TV duy nhất trong nhà) — TNT §26", 1, None,
     None, "LC", None),
    # S052
    ("S052", "bọn trẻ", "L", "repetition",
     "S043: trẻ em", "high", None,
     "VI hiện thực hóa EN 'They' thành danh ngữ; 'chúng' lần 2, 3 "
     "trong quote trong câu, không đánh", 1, None, None, "LC", None),
    ("S052", "đọc", "L", "repetition",
     "S045: đọc", "high", None, "chúng đọc nhiều hơn", 1, None, None,
     "LC", None),
    ("S052", "Maxwell", "L", "repetition",
     "S050: Maxwell", "high", None, None, 1, None, None, "LC", None),
    ("S052", "khắp nhà", "L", "repetition",
     "S048: công việc nhất định trong nhà", "high", None,
     "lặp 'nhà'", 1, None, None, "LC", None),
    # [Phase-2] nhược điểm duy nhất ← S051: danh từ tổng quát bridging
    # (H&H §6.1 general word) — VI không mạo từ, định danh bằng ngữ
    # cảnh (mapping §4); EN 'the only downside' có alt 'R: the'.
    ("S052", "nhược điểm duy nhất", "L", "general word",
     "S051: ngắt kết nối chiếc TV duy nhất trong suốt một học kỳ",
     "med", None,
     "danh từ tổng quát tóm chỉ tình huống ngắt TV câu trước (H&H "
     "§6.1)", 1, None, None, "LC", None),
    # S053
    ("S053", "Cô", "R", "personal",
     "S052: Maxwell nói", "high", None,
     "'cô' viết thường lần 2, 3 ('giúp cô', 'cô vẫn thấy') trong câu "
     "cùng chuỗi, không đánh", 1, None, None, "LC", "A"),
    ("S053", "con cái cô", "L", "repetition",
     "S048: con cô — con cái (S002)", "high", None, None, 1, None,
     None, "LC", None),
    ("S053", "hoạt động thể chất", "L", "repetition",
     "S020: hoạt động thể chất", "high", None, None, 1, None, None,
     "LC", None),
    ("S053", "màn hình", "L", "repetition",
     "S043: thời gian sử dụng màn hình", "high", None,
     "tránh xa màn hình", 1, None, None, "LC", None),
    ("S053", "các quy tắc", "L", "repetition",
     "S031: các quy tắc", "high", None, None, 1, None, None, "LC",
     None),
    # S054
    ("S054", "Cô", "R", "personal",
     "S053: Cô (Maxwell)", "high", None,
     "'cô' viết thường lần 2 ('khiến cô') trong câu không đánh", 1,
     None, None, "LC", "A"),
    ("S054", "trẻ em", "L", "repetition",
     "S043: trẻ em", "high", None, None, 1, None, None, "LC", None),
    ("S054", "ranh giới", "L", "repetition",
     "S017: ranh giới này", "high", None, "vượt qua ranh giới", 1,
     None, None, "LC", None),
    ("S054", "các quy tắc", "L", "repetition",
     "S053: các quy tắc", "high", None, "củng cố các quy tắc", 1,
     None, None, "LC", None),
    # S056
    ("S056", "Sahlberg", "L", "repetition",
     "S044: Pasi Sahlberg", "high", None, None, 1, None, None, "LC",
     None),
    ("S056", "các bậc cha mẹ", "L", "repetition",
     "S002: các bậc cha mẹ", "high", None, None, 1, None, None, "LC",
     None),
    ("S056", "con mình", "L", "repetition",
     "S053: con cái cô — con (S048)", "high", None,
     "'mình' phản thân chỉ cha mẹ trong câu, ghi note", 1, None,
     None, "LC", None),
    ("S056", "không gian kỹ thuật số", "L", "repetition",
     "S050: cai nghiện kỹ thuật số", "high", None, "lặp 'kỹ thuật số'",
     1, None, None, "LC", None),
    # [Phase-2] quan tâm ← tiểu đề S055: tiểu đề làm tiền trạm (TNT
    # §26; tiền lệ thanh thiếu niên ← S028) — chuỗi quan tâm khởi đầu
    # ở S022 'được người chăm sóc quan tâm'; EN 'interest' đối xứng.
    ("S056", "quan tâm", "L", "repetition",
     "S055: Quan tâm đến những gì con bạn làm trực tuyến — tiểu đề",
     "high", None,
     "lặp quan tâm (thể hiện sự quan tâm) — TNT §26", 1, None, None,
     "LC", None),
    # S057
    ("S057", "trẻ em", "L", "repetition",
     "S054: trẻ em", "high", None,
     "để trẻ em một mình; 'Chúng ta' x3 hư chỉ, 'chúng' x2 và 'những "
     "thứ đó' trong câu không đánh", 1, None, None, "LC", None),
    ("S057", "những thiết bị này", "R", "demonstrative",
     "S048: các thiết bị điện tử", "high", None, "hậu chỉ từ 'này'", 1,
     None, None, "LC", "A"),
    # [Phase-2] hạn chế ← hạn chế (S003): khép chuỗi S001→S003→S057
    # (TNT §26 phép lặp) — VI tách hai chuỗi (hạn chế / giới hạn) nơi
    # EN gộp một chuỗi limit/limits, ghi §7.
    ("S057", "hạn chế", "L", "repetition",
     "S003: lợi ích của việc hạn chế sử dụng TV", "med", None,
     "lặp hạn chế (chúng ta nên hạn chế tối đa) — TNT §26", 1, None,
     None, "LC", None),
    # [Phase-2] quan tâm ← quan tâm (S056): lặp nguyên hình (TNT §26) —
    # EN đổi từ interest → care; VI lặp nguyên hình, ghi §7.
    ("S057", "quan tâm", "L", "repetition",
     "S056: thể hiện sự quan tâm đến những gì con mình đang làm",
     "high", None,
     "lặp quan tâm (chúng ta quan tâm và tò mò) — TNT §26; EN care ≈ "
     "interest đổi từ", 1, None, None, "LC", None),
    # S058 (caption)
    ("S058", "Pasi Sahlberg", "L", "repetition",
     "S044: Pasi Sahlberg", "high", None,
     "caption trích dẫn; lặp cả danh xưng 'Giáo sư'", 1, None, None,
     "LC", None),
    ("S058", "Đại học Melbourne", "L", "repetition",
     "S044: Đại học Melbourne", "high", None, "caption trích dẫn", 1,
     None, None, "LC", None),
    # S059
    ("S059", "một đứa trẻ", "L", "repetition",
     "S057: trẻ em", "high", None,
     "'đây có thể là dấu hiệu', 'chúng' trong câu không đánh", 1, None,
     None, "LC", None),
    ("S059", "các hoạt động", "L", "repetition",
     "S034: hoạt động trực tuyến", "high", None, None, 1, None, None,
     "LC", None),
    ("S059", "cha mẹ", "L", "repetition",
     "S056: các bậc cha mẹ", "high", None, None, 1, None, None, "LC",
     None),
    ("S059", "Sahlberg", "L", "repetition",
     "S057: Sahlberg (S056)", "high", None, None, 1, None, None,
     "LC", None),
    # S060
    ("S060", "mối quan hệ và kỳ vọng này", "R", "demonstrative",
     "S056–S059: sự quan tâm của cha mẹ đến việc con làm trên không "
     "gian số", "high", None,
     "hậu chỉ từ 'này'; 'Chúng ta' hư chỉ, 'mối quan hệ đó', 'chúng' "
     "trong câu không đánh", 1, None, None, "LC", "A"),
    ("S060", "con cái", "L", "repetition",
     "S053: con cái cô — con cái (S002)", "high", None,
     "với con cái", 1, None, None, "LC", None),
    # [Phase-2] duy trì ← duy trì (S053): lặp nguyên hình (TNT §26) —
    # EN sustain ≈ maintain đổi từ đồng nghĩa.
    ("S060", "duy trì", "L", "repetition",
     "S053: khó duy trì các quy tắc", "high", None,
     "lặp duy trì (khả năng duy trì và tiếp tục) — TNT §26", 1, None,
     None, "LC", None),
]
