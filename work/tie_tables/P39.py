# P39 tie table — WRITTEN BY HAND FROM work/analysis/P39_semantic.md.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
#
# - text tie: gap_after=None, recovered=None
# - ellipsis: text=None, gap_after="exact substring ending before ∅",
#             recovered="{meaning}"
# - level: "LC" intersentential / "TC" intra-sentential
# - ref: R only, manual A/C/E decision (P39: mọi R đều A — không có C/E)
# - occ: explicit; đếm chuỗi con phân biệt hoa/thường
#
# P39 = cặp cắt nặng nhất corpus: EN S005–S011 và S015–S018 (11 câu) không có
# bản dịch → tie phía EN với ghi chú "không có bản dịch", không bịa tie VI.
# Không có câu VI tự sinh; 10 câu VI dịch đều đối ứng 1–1 với EN.

ST = [
    # ---- S002: E [TC] sau lượng từ; VI lặp "người" (hiện thực hóa, không có E VI)
    ("S002", None, "E", "nominal",
     "S002: Dozens of people (trong câu)", "high", None,
     "[TC] lược danh từ sau lượng từ 'hundreds of thousands' ∅; hồi phục {people}; "
     "VI lặp 'người' nên không có E phía VI (hiện thực hóa)", 1,
     "hundreds of thousands", "{people}", "TC", None),
    ("S002", "flooding", "L", "repetition",
     "S001: devastating floods", "high", "R: the",
     "lặp hình vị flood (the worst flooding)", 1, None, None, "LC", None),
    ("S002", "Bangladesh", "L", "repetition",
     "S001: floods in Bangladesh", "high", None,
     "tên riêng lặp", 1, None, None, "LC", None),

    # ---- S003: 2 pro-form [TC] + chuỗi UNICEF/lũ/tình hình/trẻ em
    ("S003", "UNICEF", "L", "repetition",
     "S001: The U.N. Children's Fund", "high", None,
     "viết tắt lặp tên đầy đủ cơ quan", 1, None, None, "LC", None),
    ("S003", "flash floods", "L", "repetition",
     "S002: the worst flooding", "high", None,
     "chuỗi lũ; flash floods chuyên biệt hóa (VI lũ quét)", 1, None, None,
     "LC", None),
    ("S003", "situation", "L", "general word",
     "S002: flooding ... villages have been washed away", "med", "R: the",
     "danh từ tổng quát tóm chỉ tình huống lũ ở 2 câu trước", 1, None, None,
     "LC", None),
    ("S003", "that", "S", "nominal",
     "S003: the situation (trong câu)", "high", None,
     "[TC] 'so has that of the children': that thế cho 'the situation'", 1,
     None, None, "TC", None),
    ("S003", "so", "S", "verbal",
     "S003: has deteriorated rapidly (trong câu)", "high", None,
     "[TC] so thế vị ngữ 'has deteriorated rapidly'; VI nén 2 pro-form "
     "thành một 'vậy'", 1, None, None, "TC", None),
    ("S003", "children", "L", "repetition",
     "S001: millions of children", "high", "R: the",
     "that of the children — lặp chuỗi trẻ em", 1, None, None, "LC", None),

    # ---- S004
    ("S004", "UNICEF", "L", "repetition",
     "S003: UNICEF says", "high", None,
     "UNICEF Representative to Bangladesh — lặp viết tắt", 1, None, None,
     "LC", None),
    ("S004", "Bangladesh", "L", "repetition",
     "S002: Bangladesh", "high", None,
     "Representative to Bangladesh", 1, None, None, "LC", None),
    ("S004", "children", "L", "repetition",
     "S003: the children", "high", None,
     "3.5 million children", 1, None, None, "LC", None),
    ("S004", "in urgent need of", "L", "repetition",
     "S001: are in urgent need of lifesaving assistance", "high", None,
     "lặp nguyên khung vị ngữ của câu mở đầu", 1, None, None, "LC", None),

    # ---- S005 (khối cắt, quote 1 của Yett)
    ("S005", "That", "R", "demonstrative",
     "S004: 3.5 million children", "high", None,
     "chỉ từ tóm chỉ con số 3,5 triệu trẻ em ở câu trước; câu trong khối "
     "cắt, không có bản dịch", 1, None, None, "LC", "A"),
    ("S005", "children", "L", "repetition",
     "S004: 3.5 million children", "high", None,
     "a staggering number of children; không có bản dịch", 1, None, None,
     "LC", None),
    ("S005", "Yett", "L", "repetition",
     "S004: Sheldon Yett", "high", None,
     "họ sau tên đầy đủ; không có bản dịch", 1, None, None, "LC", None),

    # ---- S006 (khối cắt)
    ("S006", "safe drinking water", "L", "repetition",
     "S004: safe drinking water", "high", None,
     "lặp nguyên văn; không có bản dịch", 1, None, None, "LC", None),
    ("S006", "underwater", "L", "synonym",
     "S003: flash floods", "med", None,
     "completely underwater ≈ bị ngập lũ — tiếp chuỗi lũ; không có bản dịch",
     1, None, None, "LC", None),

    # ---- S007 (khối cắt)
    ("S007", "Children", "L", "repetition",
     "S005: a staggering number of children", "high", None,
     "không có bản dịch", 1, None, None, "LC", None),
    ("S007", "high risk", "L", "repetition",
     "S001: at high risk from devastating floods", "high", None,
     "at high risk — lặp khung rủi ro của câu mở đầu; không có bản dịch", 1,
     None, None, "LC", None),
    ("S007", "situation", "L", "repetition",
     "S003: the situation caused by flash floods", "high", "R: this",
     "this desperate situation; không có bản dịch", 1, None, None, "LC",
     None),

    # ---- S008 (khối cắt)
    ("S008", "deadly diseases", "L", "repetition",
     "S006: water borne diseases", "high", None,
     "lặp diseases; deadly là thông tin mới; không có bản dịch", 1, None,
     None, "LC", None),

    # ---- S009 (khối cắt)
    ("S009", "He", "R", "personal", "S005: said Yett", "high", None,
     "đại từ hồi quy chỉ ông Yett; không có bản dịch", 1, None, None, "LC",
     "A"),
    ("S009", "cases", "L", "repetition", "S008: Cases of diarrhea", "high",
     None, "some 2,700 cases; không có bản dịch", 1, None, None, "LC", None),

    # ---- S010 (khối cắt; chứa lỗi nguồn "Dakar" — xem analysis §8)
    ("S010", "UNICEF official", "L", "general word",
     "S005: said Yett", "high", "R: the",
     "danh hiệu thay tên chỉ ông Yett; lồng chuỗi UNICEF; không có bản dịch",
     1, None, None, "LC", None),
    ("S010", "water points", "L", "repetition",
     "S006: safe drinking water", "high", None,
     "lặp hình vị water — chuỗi nước; không có bản dịch", 1, None, None,
     "LC", None),

    # ---- S011 (khối cắt)
    ("S011", "He", "R", "personal", "S010: the UNICEF official", "high",
     None, "đại từ hồi quy; tiền trạm là danh hiệu; không có bản dịch", 1,
     None, None, "LC", "A"),
    ("S011", "water-borne diseases", "L", "repetition",
     "S006: water borne diseases", "high", None,
     "lặp chuỗi bệnh (biến thể có gạch nối); không có bản dịch", 1, None,
     None, "LC", None),
    ("S011", "contaminated water", "L", "repetition",
     "S010: water points", "med", None,
     "chuỗi nước; đối lập nước bẩn ↔ safe drinking water (phép đối); "
     "không có bản dịch", 1, None, None, "LC", None),
    ("S011", "people", "L", "repetition", "S002: Dozens of people", "med",
     None, "mở rộng referent sang dân vùng lũ; không có bản dịch", 1, None,
     None, "LC", None),

    # ---- S012
    ("S012", "Yett", "L", "repetition", "S005: said Yett", "high", None,
     "nối lại tên nhân vật sau các đại từ He (S009, S011)", 1, None, None,
     "LC", None),
    ("S012", "flooded", "L", "repetition", "S006: completely underwater",
     "high", None,
     "have been flooded — tiếp chuỗi lũ (floods/flooding/flash floods)", 1,
     None, None, "LC", None),

    # ---- S013
    ("S013", "He", "R", "personal", "S012: Yett says", "high", None,
     "đại từ hồi quy chỉ ông Yett; VI dịch bằng danh xưng Ông", 1, None,
     None, "LC", "A"),
    ("S013", "children", "L", "repetition",
     "S007: Children are at high risk", "high", None,
     "an estimated 2,000 children", 1, None, None, "LC", None),
    ("S013", "floods", "L", "repetition", "S012: have been flooded", "high",
     "R: the", "before the floods hit — tiếp chuỗi lũ", 1, None, None,
     "LC", None),

    # ---- S014
    ("S014", "He", "R", "personal", "S012: Yett says", "high", None,
     "tiếp chuỗi đại từ He", 1, None, None, "LC", "A"),
    ("S014", "lifesaving", "L", "repetition",
     "S001: lifesaving assistance", "med", None,
     "lặp hình vị lifesaving (lifesaving treatment)", 1, None, None, "LC",
     None),
    ("S014", "condition", "L", "general word",
     "S013: severe acute malnutrition", "high", "R: the",
     "danh từ tổng quát chỉ bệnh suy dinh dưỡng; VI dịch bằng chỉ từ "
     "'việc này' (R) — dịch chuyển loại hình L→R", 1, None, None, "LC",
     None),
    ("S014", "also", "C", "additive",
     "S012: interrupting immunization and other vital services", "high",
     None,
     "bổ sung việc điều trị bị gián đoạn vào việc tiêm chủng đã bị gián "
     "đoạn; đối ứng VI 'cũng'", 1, None, None, "LC", None),
    ("S014", "disrupted", "L", "synonym", "S012: interrupting", "high",
     None, "has been disrupted ≈ interrupting (đồng nghĩa)", 1, None, None,
     "LC", None),

    # ---- S015 (khối cắt, quote 2 của Yett)
    ("S015", "risk", "L", "repetition", "S007: at high risk", "high",
     "R: the", "The risk of drowning — chuỗi rủi ro; không có bản dịch", 1,
     None, None, "LC", None),

    # ---- S016 (khối cắt)
    ("S016", "children", "L", "repetition", "S013: 2,000 children", "high",
     None, "At least 15 children; không có bản dịch", 1, None, None, "LC",
     None),
    ("S016", "lost their lives", "L", "synonym",
     "S002: have been killed", "high", None,
     "đồng nghĩa giảm nhẹ (tử vong); their quy chiếu trong câu; không có "
     "bản dịch", 1, None, None, "LC", None),
    ("S016", "Yett", "L", "repetition", "S012: Yett says", "high", None,
     "nối lại tên sau 2 đại từ He (S013, S014); không có bản dịch", 1,
     None, None, "LC", None),

    # ---- S017 (khối cắt)
    ("S017", "people", "L", "repetition",
     "S011: people are forced to drink", "high", None,
     "half-a-million people; không có bản dịch", 1, None, None, "LC", None),

    # ---- S018 (khối cắt)
    ("S018", "And", "C", "additive",
     "S017: Nearly half-a-million people have been evacuated", "high",
     None,
     "And đầu câu nối quote với câu sơ tán trước đó; không có bản dịch", 1,
     None, None, "LC", None),
    ("S018", "I", "R", "personal", "S016: said Yett", "high", None,
     "đại từ ngôi 1 trong quote; attribution 'said Yett' nằm ở câu trước "
     "(S016) nên đủ điều kiện; không có bản dịch", 1, None, None, "LC",
     "A"),
    ("S018", "children", "L", "repetition",
     "S016: At least 15 children", "high", None,
     "concerned for children; 'Children and their families' cuối câu cùng "
     "chuỗi trong câu, không đánh lần 2; không có bản dịch", 1, None, None,
     "LC", None),
    ("S018", "need help", "L", "synonym",
     "S001: are in urgent need of lifesaving assistance", "med", None,
     "need lặp + help ≈ assistance; khép vòng về câu mở đầu; không có bản "
     "dịch", 1, None, None, "LC", None),

    # ---- S019
    ("S019", "Yett", "L", "repetition", "S016: said Yett", "high", None,
     "nối lại tên nhân vật", 1, None, None, "LC", None),
    ("S019", "UNICEF", "L", "repetition",
     "S010: the UNICEF official", "high", None,
     "UNICEF and partners", 1, None, None, "LC", None),
    ("S019", "support", "L", "synonym",
     "S001: lifesaving assistance", "low", None,
     "to support the government ≈ assistance (đồng nghĩa xa trong trường "
     "hỗ trợ)", 1, None, None, "LC", None),

    # ---- S020
    ("S020", "He", "R", "personal", "S019: Yett says", "high", None,
     "đại từ hồi quy chỉ ông Yett; VI dịch bằng 'Ông'", 1, None, None,
     "LC", "A"),
    ("S020", "they", "R", "personal", "S019: UNICEF and partners", "high",
     None,
     "they = UNICEF và các đối tác; VI bỏ chủ ngữ (E ở TT S009) — dịch "
     "chuyển R→E", 1, None, None, "LC", "A"),
    ("S020", "water purification tablets", "L", "repetition",
     "S011: contaminated water", "high", None,
     "lặp hình vị water — chuỗi nước", 1, None, None, "LC", None),
    ("S020", "hygiene kits", "L", "collocation",
     "S010: water points and toilets", "med", None,
     "liên tưởng vệ sinh: toilets → hygiene kits; VI mất mắt xích này "
     "(S010 bị cắt)", 1, None, None, "LC", None),
    ("S020", "supplies", "L", "repetition", "S006: food supplies", "high",
     None,
     "other crucial supplies; VI mất mắt xích này (S006 bị cắt)", 1, None,
     None, "LC", None),

    # ---- S021
    ("S021", "He", "R", "personal", "S019: Yett says", "high", None,
     "tiếp chuỗi đại từ He", 1, None, None, "LC", "A"),
    ("S021", "UNICEF", "L", "repetition",
     "S019: UNICEF and partners", "high", None,
     "lặp viết tắt", 1, None, None, "LC", None),
    ("S021", "urgently", "L", "repetition",
     "S004: in urgent need of safe drinking water", "med", None,
     "lặp hình vị urgent (urgently needs; 'needs' cùng chuỗi trong câu "
     "không đánh lần 2)", 1, None, None, "LC", None),
]

TT = [
    # ---- S002: VI lấp chỗ trống EN bằng lặp 'người' → không có E
    ("S002", "lũ lụt", "L", "repetition", "S001: đợt lũ lụt tàn phá",
     "high", None, "trận lũ lụt tồi tệ nhất", 1, None, None, "LC", None),
    ("S002", "Bangladesh", "L", "repetition",
     "S001: lũ lụt tàn phá ở Bangladesh", "high", None,
     "tên riêng lặp", 1, None, None, "LC", None),

    # ---- S003
    ("S003", "UNICEF", "L", "repetition",
     "S001: Quỹ Nhi đồng Liên Hợp Quốc (UNICEF)", "high", None,
     "viết tắt đã được giới thiệu trong ngoặc ở câu đầu", 1, None, None,
     "LC", None),
    ("S003", "lũ quét", "L", "repetition",
     "S002: trận lũ lụt tồi tệ nhất", "high", None,
     "chuyên biệt hóa chuỗi lũ (đối ứng EN flash floods)", 1, None, None,
     "LC", None),
    ("S003", "tình hình", "L", "general word",
     "S002: thiệt mạng ... mắc kẹt ... cuốn trôi", "med", None,
     "danh từ tổng quát tóm chỉ tình huống lũ (đối ứng EN the situation)",
     1, None, None, "LC", None),
    ("S003", "vậy", "S", "verbal",
     "S003: đã xấu đi nhanh chóng (trong câu)", "high", None,
     "[TC] 'cũng vậy' thay cho vị ngữ 'đã xấu đi nhanh chóng'; EN dùng 2 "
     "pro-form (so + that)", 1, None, None, "TC", None),
    ("S003", "trẻ em", "L", "repetition", "S001: hàng triệu trẻ em", "high",
     None, "và trẻ em cũng vậy — lặp chuỗi trẻ em", 1, None, None, "LC",
     None),

    # ---- S004
    ("S004", "UNICEF", "L", "repetition", "S003: UNICEF cho biết", "high",
     None, "Đại diện UNICEF tại Bangladesh", 1, None, None, "LC", None),
    ("S004", "Bangladesh", "L", "repetition", "S002: ở Bangladesh", "high",
     None, "tại Bangladesh", 1, None, None, "LC", None),
    ("S004", "trẻ em", "L", "repetition", "S003: trẻ em cũng vậy", "high",
     None, "3,5 triệu trẻ em", 1, None, None, "LC", None),
    ("S004", "cần", "L", "repetition",
     "S001: đang cần được hỗ trợ khẩn cấp", "med", None,
     "lặp khung 'đang cần' (đang cần ngay) — đối ứng EN 'in urgent need "
     "of'", 1, None, None, "LC", None),

    # ---- S005 (← EN S012)
    ("S005", "Yett", "L", "repetition", "S004: Sheldon Yett", "high", None,
     "lặp tên riêng; VI thêm danh xưng 'Ông' trước tên (EN chỉ 'Yett')", 1,
     None, None, "LC", None),
    ("S005", "ngập lụt", "L", "repetition", "S003: lũ quét", "high", None,
     "bị ngập lụt — tiếp chuỗi lũ (đối ứng EN flooded)", 1, None, None,
     "LC", None),

    # ---- S006 (← EN S013)
    ("S006", "Ông", "R", "personal", "S005: Ông Yett", "high", None,
     "danh xưng hồi quy không tên — công cụ liên kết riêng của VI (đối ứng "
     "EN He)", 1, None, None, "LC", "A"),
    ("S006", "trẻ em", "L", "repetition", "S004: 3,5 triệu trẻ em", "high",
     None, "2.000 trẻ em", 1, None, None, "LC", None),
    ("S006", "lũ lụt", "L", "repetition", "S005: bị ngập lụt", "high",
     None, "trước khi lũ lụt ập đến — tiếp chuỗi lũ", 1, None, None, "LC",
     None),

    # ---- S007 (← EN S014)
    ("S007", "Ông", "R", "personal", "S006: Ông lưu ý", "high", None,
     "tiếp chuỗi danh xưng Ông", 1, None, None, "LC", "A"),
    ("S007", "này", "R", "demonstrative",
     "S006: suy dinh dưỡng cấp tính nghiêm trọng", "high", None,
     "chỉ từ 'việc này' thay cho danh từ tổng quát EN 'the condition' — "
     "dịch chuyển L→R", 1, None, None, "LC", "A"),
    ("S007", "cũng", "C", "additive",
     "S005: làm gián đoạn việc tiêm chủng", "high", None,
     "bổ sung việc điều trị bị gián đoạn; đối ứng EN also (S014)", 1,
     None, None, "LC", None),
    ("S007", "gián đoạn", "L", "repetition",
     "S005: làm gián đoạn việc tiêm chủng", "high", None,
     "bị gián đoạn — lặp nguyên văn", 1, None, None, "LC", None),

    # ---- S008 (← EN S019)
    ("S008", "Yett", "L", "repetition", "S005: Ông Yett", "high", None,
     "nối lại tên sau 2 danh xưng trần Ông (S006, S007)", 1, None, None,
     "LC", None),
    ("S008", "UNICEF", "L", "repetition",
     "S004: Đại diện UNICEF tại Bangladesh", "high", None,
     "UNICEF và các đối tác", 1, None, None, "LC", None),
    ("S008", "Bangladesh", "L", "repetition", "S004: tại Bangladesh", "high",
     None,
     "chính phủ Bangladesh — VI tự sinh 'Bangladesh' (EN chỉ 'the "
     "government')", 1, None, None, "LC", None),
    ("S008", "hỗ trợ", "L", "repetition",
     "S001: đang cần được hỗ trợ khẩn cấp", "high", None,
     "để hỗ trợ cho chính phủ; EN dùng support ≈ assistance (conf low "
     "phía EN)", 1, None, None, "LC", None),

    # ---- S009 (← EN S020)
    ("S009", "Ông", "R", "personal", "S008: Ông Yett", "high", None,
     "tiếp chuỗi danh xưng Ông", 1, None, None, "LC", "A"),
    ("S009", None, "E", "nominal", "S008: UNICEF và các đối tác", "high",
     None,
     "[LC] lược chủ ngữ vế báo cáo gián tiếp sau 'cho biết' ∅; hồi phục "
     "{UNICEF và các đối tác}; EN giữ đại từ they (S020) — dịch chuyển "
     "R→E", 1, "cho biết", "{UNICEF và các đối tác}", "LC", None),
    ("S009", "viên lọc nước", "L", "repetition",
     "S004: nước uống an toàn", "high", None,
     "lặp hình vị nước — chuỗi nước (đối ứng EN water purification "
     "tablets)", 1, None, None, "LC", None),
    ("S009", "trẻ em", "L", "repetition", "S006: 2.000 trẻ em", "low",
     None,
     "trẻ em gái vị thành niên — lặp hình vị trẻ em nhưng thu hẹp "
     "referent; EN chỉ 'adolescent girls' (VI tự sinh echo)", 1, None,
     None, "LC", None),

    # ---- S010 (← EN S021)
    ("S010", "Ông", "R", "personal", "S009: Ông cho biết", "high", None,
     "tiếp chuỗi danh xưng Ông", 1, None, None, "LC", "A"),
    ("S010", "UNICEF", "L", "repetition",
     "S008: UNICEF và các đối tác", "high", None,
     "lặp viết tắt", 1, None, None, "LC", None),
    ("S010", "cần", "L", "repetition",
     "S004: đang cần ngay nước uống an toàn", "high", None,
     "cần gấp — lặp động từ cần (đối ứng EN urgently needs)", 1, None,
     None, "LC", None),
    ("S010", "khẩn cấp", "L", "repetition",
     "S001: đang cần được hỗ trợ khẩn cấp", "high", None,
     "ứng phó khẩn cấp; EN tách khái niệm thành urgent (S004) + emergency "
     "(S021), VI hội tụ vào 'khẩn cấp'", 1, None, None, "LC", None),
]
