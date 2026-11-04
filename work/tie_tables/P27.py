# P27 tie table — WRITTEN BY HAND FROM work/analysis/P27_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# BẢN ĐỒ: ST 105 câu / TT 84 câu. VI TỰ SINH: S002 (thay EN S002),
#   subhead S015. KHỐI CẮT VI (tie chỉ EN): S002, S004–S005, S059,
#   S065, S068–S070, S080, S083–S084, S090–S092, S097 (15 câu, 42 hàng).
# GỘP: S013+S014→S011; S028+S029→S027; S035+S036→S033; S040+S041→S037;
#   S054+S055→S051; S073+S074+S075→S064; S076+S077→S065; S085+S086+S087→S070.
# TÁCH: S021→S019+S020; S051→S047+S048; S067→S060+S061.
# Subhead không gán nhãn (EN S030/S052/S071/S093; VI S015/S028/S049/S062/S073).

ST = [
    # S002 — KHỐI CẮT VI (tie chỉ EN)
    ("S002", "But", "C", "adversative", "S001: hiện tượng overemployed được mô tả", "high", None, "câu cắt phía VI (VI S002 tự sinh nội dung khác)", 1, None, None, "LC", None),
    # S003
    ("S003", "seven jobs", "L", "repetition", "S001: multiple full-time jobs", "high", None, None, 1, None, None, "LC", None),
    ("S003", "full-time", "L", "repetition", "S001: multiple full-time jobs", "high", None, None, 1, None, None, "LC", None),
    # S004 — KHỐI CẮT VI (tie chỉ EN)
    ("S004", "You", "R", "personal", "người nghe chung (ngoại văn bản — quote Ash)", "med", None, "câu cắt phía VI; 'You know how people…'", 1, None, None, "LC", "E"),
    # S005 — KHỐI CẮT VI (tie chỉ EN)
    ("S005", "I", "R", "personal", "S003: Ash", "high", None, "quote Ash; câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S005", "she", "R", "personal", "S003: Ash", "high", None, "'she told The Feed'; câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S005", "jobs", "L", "repetition", "S003: seven jobs", "high", None, "'f--- you' jobs; câu cắt phía VI", 1, None, None, "LC", None),
    # S006
    ("S006", "software industry worker", "L", "synonym", "S003: Ash (tên riêng)", "high", None, "danh từ mô tả lại Ash, không lặp tên", 1, None, None, "LC", None),
    ("S006", "multiple jobs", "L", "repetition", "S003: seven jobs", "high", None, None, 1, None, None, "LC", None),
    ("S006", "20 hours a day", "L", "repetition", "S002: working long hours", "high", None, "chuỗi giờ; tiền trạm ở câu bị cắt phía VI", 1, None, None, "LC", None),
    # S007
    ("S007", "she", "R", "personal", "S006: software industry worker (Ash)", "high", None, None, 1, None, None, "LC", "A"),
    ("S007", "Ash", "L", "repetition", "S003: Ash", "high", None, "'Ash's days'", 1, None, None, "LC", None),
    ("S007", "five jobs", "L", "repetition", "S006: multiple jobs", "high", None, None, 1, None, None, "LC", None),
    # S008
    ("S008", "She", "R", "personal", "S007: Ash", "high", None, None, 1, None, None, "LC", "A"),
    # S009
    ("S009", "she", "R", "personal", "S008: She", "high", None, None, 1, None, None, "LC", "A"),
    ("S009", "first job", "L", "repetition", "S007: five jobs", "high", None, "'worked her first job'", 1, None, None, "LC", None),
    # S010
    ("S010", "She", "R", "personal", "S009: she", "high", None, None, 1, None, None, "LC", "A"),
    ("S010", "government role", "L", "associative", "S009: first job", "med", None, "trường nghĩa việc làm", 1, None, None, "LC", None),
    # S011
    ("S011", "I", "R", "personal", "S007: Ash", "high", None, "quote; occ 1 vì 'I'd' là lần gặp 'I' thứ 2", 1, None, None, "LC", "A"),
    ("S011", "she said", "R", "personal", "S007: Ash", "high", None, None, 1, None, None, "LC", "A"),
    # S012
    ("S012", "She", "R", "personal", "S011: she said", "high", None, None, 1, None, None, "LC", "A"),
    ("S012", "meetings", "L", "repetition", "S011: my other meetings", "high", None, None, 1, None, None, "LC", None),
    # S013
    ("S013", "She", "R", "personal", "S012: She", "high", None, None, 1, None, None, "LC", "A"),
    # S014
    ("S014", "she", "R", "personal", "S013: She", "high", None, None, 1, None, None, "LC", "A"),
    # S015
    ("S015", "I", "R", "personal", "S007: Ash", "high", None, "quote; occ 1 ('I would not'), lần 2 'I would do'", 1, None, None, "LC", "A"),
    ("S015", "Ash said", "L", "repetition", "S007: Ash", "high", None, None, 1, None, None, "LC", None),
    # S016
    ("S016", "meeting clashes", "L", "associative", "S011–S012: meetings", "high", None, None, 1, None, None, "LC", None),
    # S017
    ("S017", "I", "R", "personal", "S015: Ash", "high", None, "quote liệt kê lý do", 1, None, None, "LC", "A"),
    # S018
    ("S018", "Ash", "L", "repetition", "S015: Ash said", "high", None, "'Ash said she was switching' — she trong câu", 1, None, None, "LC", None),
    # S019
    ("S019", "the tech [jobs]", "L", "associative", "S006: software industry worker", "high", None, "nguồn chèn ngoặc vuông '[jobs]'", 1, None, None, "LC", None),
    ("S019", "you", "R", "personal", "người làm công nghệ chung (ngoại văn bản)", "med", None, "occ 1 ('you are fast'), lần 2 'you have'", 1, None, None, "LC", "E"),
    # S020
    ("S020", "customer service role", "L", "associative", "S010: government role", "med", None, "trường nghĩa 'role'", 1, None, None, "LC", None),
    ("S020", "you're", "R", "personal", "người làm việc chung (ngoại văn bản — quote)", "med", None, None, 1, None, None, "LC", "E"),
    ("S020", "she said", "R", "personal", "S018: Ash", "high", None, None, 1, None, None, "LC", "A"),
    # S021
    ("S021", "I", "R", "personal", "S018: Ash", "high", None, "quote; 'that helped' chỉ AI trong câu", 1, None, None, "LC", "A"),
    # S022
    ("S022", "Ash says", "L", "repetition", "S018: Ash", "high", None, "'It can be' là it hư chỉ (không đánh)", 1, None, None, "LC", None),
    # S023
    ("S023", "The Feed", "L", "repetition", "S005: she told The Feed", "high", None, "tiền trạm ở câu bị cắt phía VI", 1, None, None, "LC", None),
    # S024
    ("S024", "Ash", "L", "repetition", "S022: Ash", "high", None, "'Ash's schedule'", 1, None, None, "LC", None),
    # S025
    ("S025", "She", "R", "personal", "S024: Ash", "high", None, None, 1, None, None, "LC", "A"),
    ("S025", "two full-time jobs", "L", "repetition", "S003: seven jobs / full-time", "high", None, None, 1, None, None, "LC", None),
    # S026
    ("S026", "I", "R", "personal", "S024: Ash", "high", None, "quote", 1, None, None, "LC", "A"),
    ("S026", "doing this", "R", "demonstrative", "S025: working two full-time jobs", "high", None, "'this' = làm nhiều việc; VI 'làm như vậy' đánh S — bất đối xứng R↔S", 1, None, None, "LC", "A"),
    # S027
    ("S027", "She", "R", "personal", "S026: I (Ash)", "high", None, None, 1, None, None, "LC", "A"),
    # S028
    ("S028", "Ash", "L", "repetition", "S024: Ash", "high", None, None, 1, None, None, "LC", None),
    ("S028", "their incomes", "L", "repetition", "S023: seven different income sources", "high", None, None, 1, None, None, "LC", None),
    # S031
    ("S031", "multiple full-time jobs", "L", "repetition", "S001: multiple full-time jobs", "high", None, "'secretly holding…'", 1, None, None, "LC", None),
    # S032
    ("S032", "Its", "R", "personal", "S031: an online Reddit forum", "high", None, "'Its tagline'", 1, None, None, "LC", "A"),
    # S033
    ("S033", "Members", "L", "associative", "S031: people have joined", "high", None, None, 1, None, None, "LC", None),
    ("S033", "this community", "R", "demonstrative", "S028: a growing international community", "high", None, None, 1, None, None, "LC", "A"),
    ("S033", "overemployed", "L", "repetition", "S001: 'overemployed'", "high", None, None, 1, None, None, "LC", None),
    # S034
    ("S034", "It's", "R", "personal", "S033: 'overemployed'", "high", None, "It = hiện tượng overemployment", 1, None, None, "LC", "A"),
    ("S034", "roles", "L", "associative", "S031: multiple full-time jobs", "med", None, "trường nghĩa việc làm", 1, None, None, "LC", None),
    ("S034", "after hours", "L", "associative", "S006: 20 hours a day", "med", None, "chuỗi giờ làm", 1, None, None, "LC", None),
    # S035
    ("S035", "Members", "L", "repetition", "S033: Members", "high", None, None, 1, None, None, "LC", None),
    ("S035", "Australians", "L", "repetition", "S001: some Australians", "high", None, None, 1, None, None, "LC", None),
    # S036
    ("S036", "They", "R", "personal", "S035: Members", "high", None, None, 1, None, None, "LC", "A"),
    ("S036", "also", "C", "additive", "S035: Members swap career advice", "high", None, "VI S033 gộp — 'và cả' trong câu", 1, None, None, "LC", None),
    ("S036", "employers", "L", "repetition", "S001: without their employers' knowledge", "high", None, None, 1, None, None, "LC", None),
    # S037
    ("S037", "Those", "S", "nominal", "S035: Members", "high", None, "[LC] Those ← Members; VI hiện thực hóa 'Những người'", 1, None, None, "LC", None),
    ("S037", "The Feed", "L", "repetition", "S023: The Feed", "high", None, None, 1, None, None, "LC", None),
    ("S037", "employers", "L", "repetition", "S036: their employers", "high", None, "'employers past and present'", 1, None, None, "LC", None),
    # S038
    ("S038", "retaliation", "L", "synonym", "S037: blowback", "high", None, None, 1, None, None, "LC", None),
    ("S038", "employers", "L", "repetition", "S037: employers", "high", None, None, 1, None, None, "LC", None),
    # S039
    ("S039", "fired", "L", "repetition", "S036: getting sacked", "high", None, None, 1, None, None, "LC", None),
    # S040
    ("S040", "One Australian", "L", "repetition", "S035: Australians", "high", None, None, 1, None, None, "LC", None),
    ("S040", "income", "L", "repetition", "S028: their incomes", "high", None, "'doubled their income'", 1, None, None, "LC", None),
    ("S040", "four full-time jobs", "L", "repetition", "S031: multiple full-time jobs", "high", None, "'juggling four full-time jobs'", 1, None, None, "LC", None),
    # S041
    ("S041", "them", "R", "personal", "S040: Jess", "high", None, "singular they; 'it was about' là it hư chỉ (không đánh)", 1, None, None, "LC", "A"),
    # S042
    ("S042", "I", "R", "personal", "S040: Jess", "high", None, "quote; occ 1 ('I always made'), lần 2 'I was producing'", 1, None, None, "LC", "A"),
    # S043
    ("S043", "This", "R", "demonstrative", "S042: producing good work", "high", None, None, 1, None, None, "LC", "A"),
    ("S043", "you", "R", "personal", "người làm nhiều việc chung (ngoại văn bản — quote)", "med", None, "'until you get caught and fired'", 1, None, None, "LC", "E"),
    ("S043", "caught and fired", "L", "repetition", "S035: getting caught / S039: fired", "high", None, None, 1, None, None, "LC", None),
    ("S043", "they told", "R", "personal", "S040: Jess", "high", None, "singular they", 1, None, None, "LC", "A"),
    # S044
    ("S044", "The CEOs", "L", "repetition", "S039: Silicon Valley chief executives", "high", None, None, 1, None, None, "LC", None),
    ("S044", "multiple jobs", "L", "repetition", "S040: four full-time jobs", "high", None, None, 1, None, None, "LC", None),
    ("S044", "we", "R", "personal", "người lao động chung (ngoại văn bản — quote Jess)", "med", None, "'why should we just follow'", 1, None, None, "LC", "E"),
    ("S044", "the rules", "L", "repetition", "S002: bending the company rules", "high", None, "tiền trạm ở câu bị cắt phía VI", 1, None, None, "LC", None),
    # S045
    ("S045", "employers", "L", "repetition", "S038: employers", "high", None, None, 1, None, None, "LC", None),
    ("S045", "full-time employees", "L", "repetition", "S001: multiple full-time jobs", "high", None, "chuỗi 'full-time'", 1, None, None, "LC", None),
    # S046
    ("S046", "They're", "R", "personal", "S045: most employers", "high", None, None, 1, None, None, "LC", "A"),
    ("S046", "employees", "L", "repetition", "S045: full-time employees", "high", None, None, 1, None, None, "LC", None),
    ("S046", "other jobs", "L", "repetition", "S040: four full-time jobs", "high", None, "'doing other jobs'", 1, None, None, "LC", None),
    ("S046", "he said", "R", "personal", "S045: Mark Wooden", "high", None, None, 1, None, None, "LC", "A"),
    # S047
    ("S047", "Jess", "L", "repetition", "S043: they told (Jess)", "high", None, None, 1, None, None, "LC", None),
    # S048
    ("S048", "meetings", "L", "repetition", "S012: meetings", "high", None, "'like going to meetings'", 1, None, None, "LC", None),
    ("S048", "Jess said", "L", "repetition", "S047: Jess", "high", None, None, 1, None, None, "LC", None),
    # S049
    ("S049", "you", "R", "personal", "người làm việc chung (ngoại văn bản — quote)", "med", None, None, 1, None, None, "LC", "E"),
    ("S049", "the 40 hours", "L", "repetition", "S034: after hours / S006: hours", "high", None, "chuỗi giờ chuẩn", 1, None, None, "LC", None),
    ("S049", "productivity", "L", "repetition", "S046: productivity on their first job", "high", None, "'level of productivity'; 'the same' so sánh trong câu", 1, None, None, "LC", None),
    ("S049", "we", "R", "personal", "người lao động chung (ngoại văn bản — quote Jess)", "med", None, "'we as free agents'", 1, None, None, "LC", "E"),
    ("S049", "do so", "S", "verbal", "S049: get the work done in less time", "high", None, "[TC] pro-form thế động từ — đối xứng VI 'làm vậy'", 1, None, None, "TC", None),
    # S050
    ("S050", "However", "C", "adversative", "S049: Jess lập luận tự do", "high", None, None, 1, None, None, "LC", None),
    ("S050", "Jess", "L", "repetition", "S048: Jess said", "high", None, None, 1, None, None, "LC", None),
    ("S050", "multi-tasking", "L", "associative", "S040: juggling four full-time jobs", "med", None, None, 1, None, None, "LC", None),
    # S051
    ("S051", "I", "R", "personal", "S050: Jess", "high", None, "quote; occ 1 ('I have done'), lần 2 'I wouldn't'", 1, None, None, "LC", "A"),
    ("S051", "the two meetings", "L", "repetition", "S048: meetings", "high", None, None, 1, None, None, "LC", None),
    ("S051", "you've", "R", "personal", "người làm việc chung (ngoại văn bản — quote)", "med", None, "'you've got one earpiece'", 1, None, None, "LC", "E"),
    # S053
    ("S053", "juggling full-time office jobs", "L", "repetition", "S040: juggling four full-time jobs", "high", None, None, 1, None, None, "LC", None),
    ("S053", "having multiple jobs", "L", "repetition", "S044: multiple jobs", "high", None, None, 1, None, None, "LC", None),
    # S054
    ("S054", "multiple jobs", "L", "repetition", "S053: having multiple jobs", "high", None, None, 1, None, None, "LC", None),
    # S055
    ("S055", "This rate", "R", "demonstrative", "S054: 6.5 per cent had multiple jobs", "high", None, None, 1, None, None, "LC", "A"),
    # S056
    ("S056", "Meanwhile", "C", "additive", "S054–S055: số liệu multi-job", "high", None, None, 1, None, None, "LC", None),
    # S057
    ("S057", "The Reddit community", "L", "repetition", "S031: online Reddit forum / S033: this community", "high", None, None, 1, None, None, "LC", None),
    ("S057", "overemployment", "L", "repetition", "S033: 'overemployed'", "high", None, None, 1, None, None, "LC", None),
    # S058
    ("S058", "Wooden said", "L", "repetition", "S045: Mark Wooden", "high", None, None, 1, None, None, "LC", None),
    ("S058", "overemployment", "L", "repetition", "S057: 'overemployment'", "high", None, None, 1, None, None, "LC", None),
    # S059 — KHỐI CẮT VI (tie chỉ EN)
    ("S059", "multiple job-holders", "L", "repetition", "S054: multiple jobs", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S059", "he said", "R", "personal", "S058: Wooden said", "high", None, "câu cắt phía VI", 1, None, None, "LC", "A"),
    # S060
    ("S060", "multiple job-holders", "L", "repetition", "S059: multiple job-holders", "high", None, "tiền trạm ở câu bị cắt phía VI", 1, None, None, "LC", None),
    ("S060", "overemployed", "L", "repetition", "S057: overemployment", "high", None, "'they are overemployed'", 1, None, None, "LC", None),
    ("S060", "fewer hours", "L", "repetition", "S058: working more hours", "high", None, None, 1, None, None, "LC", None),
    # S061
    ("S061", "However", "C", "adversative", "S060: quarter prefer fewer hours", "high", None, None, 1, None, None, "LC", None),
    ("S061", "multiple job-holders", "L", "repetition", "S060: multiple job-holders", "high", None, None, 1, None, None, "LC", None),
    ("S061", "working hours", "L", "repetition", "S060: fewer hours", "high", None, "'their working hours'", 1, None, None, "LC", None),
    ("S061", "people with multiple jobs", "L", "repetition", "S060: multiple job-holders", "high", None, None, 1, None, None, "LC", None),
    # S062
    ("S062", "salary package", "L", "associative", "S040: income / S023: income sources", "med", None, "chuỗi thu nhập", 1, None, None, "LC", None),
    ("S062", "a second full-time job", "L", "repetition", "S053: full-time office jobs", "high", None, None, 1, None, None, "LC", None),
    # S063
    ("S063", "He", "R", "personal", "S062: Adam", "high", None, None, 1, None, None, "LC", "A"),
    ("S063", "this", "R", "demonstrative", "S062: a second full-time job", "high", None, "'this will be his ticket'", 1, None, None, "LC", "A"),
    # S064
    ("S064", "he said", "R", "personal", "S063: He (Adam)", "high", None, None, 1, None, None, "LC", "A"),
    # S065 — KHỐI CẮT VI (tie chỉ EN)
    ("S065", "It's", "R", "personal", "S064: working harder and earning more", "high", None, "It = việc làm thêm; câu cắt phía VI", 1, None, None, "LC", "A"),
    # S066
    ("S066", "Software industry worker", "L", "synonym", "S006: software industry worker (Ash)", "high", None, None, 1, None, None, "LC", None),
    ("S066", "Ash", "L", "repetition", "S024: Ash", "high", None, None, 1, None, None, "LC", None),
    ("S066", "from seven jobs to two", "L", "repetition", "S003: seven jobs / S025: two full-time jobs", "high", None, None, 1, None, None, "LC", None),
    # S067
    ("S067", "She", "R", "personal", "S066: Ash", "high", None, None, 1, None, None, "LC", "A"),
    ("S067", "her family", "L", "repetition", "S024: support her family", "high", None, None, 1, None, None, "LC", None),
    ("S067", "one salary", "L", "repetition", "S062: salary package", "high", None, None, 1, None, None, "LC", None),
    # S068 — KHỐI CẮT VI (tie chỉ EN)
    ("S068", "That's", "R", "demonstrative", "S067: survive on a single salary", "high", None, "occ 1 ('That's weird'), lần 2 'that's like'; câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S068", "I", "R", "personal", "S066: Ash", "high", None, "occ 1 ('I feel'), lần 2 'I can'; câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S068", "multiple jobs", "L", "repetition", "S061: people with multiple jobs", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S068", "working three jobs to make ends meet", "L", "repetition", "S052: tiểu đề 'Working three jobs to make ends meet'", "high", None, "echo tiểu đề; câu cắt phía VI", 1, None, None, "LC", None),
    ("S068", "she said", "R", "personal", "S066: Ash", "high", None, "câu cắt phía VI", 1, None, None, "LC", "A"),
    # S069 — KHỐI CẮT VI (tie chỉ EN)
    ("S069", "she", "R", "personal", "S068: she said (Ash)", "high", None, "câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S069", "employer", "L", "repetition", "S045: employers", "high", None, "'one employer'; câu cắt phía VI", 1, None, None, "LC", None),
    ("S069", "Ash", "L", "repetition", "S066: Ash", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S069", "made redundant", "L", "synonym", "S036: getting sacked", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S070 — KHỐI CẮT VI (tie chỉ EN)
    ("S070", "I", "R", "personal", "S069: Ash", "high", None, "occ 1 ('I've been'), lần 2 'I can't'; câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S070", "let go", "L", "synonym", "S069: made redundant", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S070", "my family", "L", "repetition", "S067: her family", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S072
    ("S072", "overemployed", "L", "repetition", "S060: overemployed", "high", None, "'The so-called overemployed community'", 1, None, None, "LC", None),
    ("S072", "community", "L", "repetition", "S057: The Reddit community", "high", None, None, 1, None, None, "LC", None),
    # S073
    ("S073", "Mark Wooden", "L", "repetition", "S058: Wooden said", "high", None, "'Economist Mark Wooden'", 1, None, None, "LC", None),
    ("S073", "employed people", "L", "repetition", "S054: employed people", "high", None, None, 1, None, None, "LC", None),
    ("S073", "very long weeks", "L", "repetition", "S058: working more hours", "high", None, "chuỗi giờ", 1, None, None, "LC", None),
    # S074
    ("S074", "He said", "R", "personal", "S073: Mark Wooden", "high", None, None, 1, None, None, "LC", "A"),
    ("S074", "employed people", "L", "repetition", "S073: employed people", "high", None, None, 1, None, None, "LC", None),
    ("S074", "50 or more hours", "L", "repetition", "S073: very long weeks", "high", None, None, 1, None, None, "LC", None),
    # S075
    ("S075", "it", "R", "personal", "S074: just over 10 per cent", "high", None, None, 1, None, None, "LC", "A"),
    # S077
    ("S077", "We", "R", "personal", "xã hội chung (ngoại văn bản — quote Black)", "med", None, "occ 1 ('We think'), lần 2 'we overspend'", 1, None, None, "LC", "E"),
    ("S077", "productivity", "L", "repetition", "S049: productivity", "high", None, None, 1, None, None, "LC", None),
    ("S077", "make ends meet", "L", "repetition", "S052: tiểu đề 'make ends meet'", "high", None, "echo tiểu đề", 1, None, None, "LC", None),
    ("S077", "our health", "L", "repetition", "S076: health impacts", "high", None, None, 1, None, None, "LC", None),
    ("S077", "she said", "R", "personal", "S076: Nicole Black", "high", None, None, 1, None, None, "LC", "A"),
    # S078
    ("S078", "longer work hours", "L", "repetition", "S074: 50 or more hours", "high", None, None, 1, None, None, "LC", None),
    ("S078", "health outcomes", "L", "repetition", "S077: our health", "high", None, None, 1, None, None, "LC", None),
    # S079
    ("S079", "we know", "R", "personal", "chuyên gia/chúng ta chung (ngoại văn bản — quote Black)", "med", None, None, 1, None, None, "LC", "E"),
    ("S079", "your life", "R", "personal", "người đọc chung (ngoại văn bản — quote)", "med", None, "'aspects of your life'", 1, None, None, "LC", "E"),
    ("S079", "healthy meals", "L", "associative", "S078: poorer health outcomes", "med", None, "chuỗi sức khỏe", 1, None, None, "LC", None),
    # S080 — KHỐI CẮT VI (tie chỉ EN)
    ("S080", "you've", "R", "personal", "người đọc chung (ngoại văn bản — quote Black)", "med", None, "occ 1 ('you've got 24'), lần 2 'you've got less' + 'you're'; câu cắt phía VI", 1, None, None, "LC", "E"),
    ("S080", "24 hours a day", "L", "repetition", "S074: 50 or more hours", "high", None, "chuỗi giờ; câu cắt phía VI", 1, None, None, "LC", None),
    ("S080", "being healthy", "L", "repetition", "S079: healthy meals", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S081
    ("S081", "Ash said", "L", "repetition", "S066: Ash", "high", None, None, 1, None, None, "LC", None),
    ("S081", "burnout", "L", "repetition", "S036: burnout", "high", None, "'symptoms of burnout'", 1, None, None, "LC", None),
    # S082
    ("S082", "me", "R", "personal", "S081: Ash", "high", None, "quote; occ 1 ('impacted me'), lần 2 'telling me' + 'my kids'", 1, None, None, "LC", "A"),
    ("S082", "she said", "R", "personal", "S081: Ash", "high", None, None, 1, None, None, "LC", "A"),
    # S083 — KHỐI CẮT VI (tie chỉ EN)
    ("S083", "I", "R", "personal", "S082: she said (Ash)", "high", None, "occ 1 ('I had'), lần 2 'I would'; câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S083", "the seven jobs", "L", "repetition", "S066: from seven jobs to two", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S084 — KHỐI CẮT VI (tie chỉ EN)
    ("S084", "I", "R", "personal", "S083: I (Ash)", "high", None, "câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S084", "this", "R", "demonstrative", "S083: push them off to the side", "high", None, "'do this as much'; câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S084", "the kids", "L", "repetition", "S082: my kids", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S085
    ("S085", "Jess", "L", "repetition", "S050: Jess", "high", None, "'Jess the engineer said' — they trong câu", 1, None, None, "LC", None),
    ("S085", "four jobs", "L", "repetition", "S040: four full-time jobs", "high", None, "'juggling up to four jobs'", 1, None, None, "LC", None),
    # S086
    ("S086", "personal life", "L", "repetition", "S079: your life", "high", None, None, 1, None, None, "LC", None),
    # S087
    ("S087", "I", "R", "personal", "S085: Jess", "high", None, "occ 1 ('I guess'), lần 2 'I realised', lần 3 'I put'", 1, None, None, "LC", "A"),
    ("S087", "they said", "R", "personal", "S085: Jess", "high", None, "singular they", 1, None, None, "LC", "A"),
    # S088
    ("S088", "It", "R", "personal", "S085: juggling up to four jobs", "high", None, "It = việc multi-jobbing", 1, None, None, "LC", "A"),
    ("S088", "me", "R", "personal", "S087: I (Jess)", "high", None, "'burnt me out' + 'I'm' cùng quy Jess", 1, None, None, "LC", "A"),
    # S089
    ("S089", "Wooden said", "L", "repetition", "S073: Mark Wooden", "high", None, None, 1, None, None, "LC", None),
    ("S089", "overemployment", "L", "repetition", "S072: overemployed", "high", None, None, 1, None, None, "LC", None),
    ("S089", "mental health", "L", "repetition", "S078: health outcomes", "high", None, None, 1, None, None, "LC", None),
    # S090 — KHỐI CẮT VI (tie chỉ EN)
    ("S090", "you", "R", "personal", "người làm việc chung (ngoại văn bản — quote Wooden)", "med", None, "occ 1 ('you do'), lần 2 'you don't'; câu cắt phía VI", 1, None, None, "LC", "E"),
    ("S090", "it", "R", "personal", "S089: overemployment", "high", None, "'to do it'; câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S090", "Wooden explained", "L", "repetition", "S089: Wooden said", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S091 — KHỐI CẮT VI (tie chỉ EN)
    ("S091", "75 hours a week", "L", "repetition", "S074: 50 or more hours", "high", None, "chuỗi giờ; câu cắt phía VI", 1, None, None, "LC", None),
    ("S091", "you", "R", "personal", "người quan sát chung (ngoại văn bản — quote)", "med", None, "'you might think'; câu cắt phía VI", 1, None, None, "LC", "E"),
    ("S091", "mental health", "L", "repetition", "S089: mental health", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S092 — KHỐI CẮT VI (tie chỉ EN)
    ("S092", "But", "C", "adversative", "S091: người thích làm 75 giờ", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S092", "75 hours a week", "L", "repetition", "S091: 75 hours a week", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S092", "those people", "R", "demonstrative", "S091: The people who say", "high", None, "câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S092", "their jobs", "L", "repetition", "S091: their job satisfaction", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S092", "anxiety and symptoms of depression", "L", "associative", "S091: mental health", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S094
    ("S094", "you're", "R", "personal", "người đọc chung (ngoại văn bản)", "med", None, "'you're allowed' + 'your' trong câu", 1, None, None, "LC", "E"),
    ("S094", "multiple full-time jobs", "L", "repetition", "S061: people with multiple jobs", "high", None, None, 1, None, None, "LC", None),
    # S095
    ("S095", "You've", "R", "personal", "người đọc chung (ngoại văn bản — quote King)", "med", None, None, 1, None, None, "LC", "E"),
    ("S095", "it", "R", "personal", "S094: employment contract", "high", None, "'that it doesn't have'", 1, None, None, "LC", "A"),
    # S096
    ("S096", "And", "C", "additive", "S095: obligations of exclusivity", "high", None, None, 1, None, None, "LC", None),
    ("S096", "contract templates", "L", "repetition", "S094: employment contract", "high", None, None, 1, None, None, "LC", None),
    ("S096", "you'll", "R", "personal", "người đọc chung (ngoại văn bản — quote)", "med", None, "'you'll see' + 'you can't'", 1, None, None, "LC", "E"),
    ("S096", "King said", "L", "repetition", "S094: Danny King", "high", None, None, 1, None, None, "LC", None),
    # S097 — KHỐI CẮT VI (tie chỉ EN)
    ("S097", "Employees", "L", "repetition", "S045: full-time employees", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S097", "also", "C", "additive", "S096: hạn chế hợp đồng", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S097", "their role", "L", "repetition", "S053: office jobs", "med", None, "chuỗi 'role/việc'; câu cắt phía VI", 1, None, None, "LC", None),
    # S098
    ("S098", "you", "R", "personal", "người đọc chung (ngoại văn bản — quote King)", "med", None, "occ 1 ('you get caught'); 'you' ×6 trong câu", 1, None, None, "LC", "E"),
    ("S098", "get caught", "L", "repetition", "S043: you get caught", "high", None, None, 1, None, None, "LC", None),
    ("S098", "the contract", "L", "repetition", "S096: contract templates", "high", None, None, 1, None, None, "LC", None),
    ("S098", "King said", "L", "repetition", "S096: King said", "high", None, None, 1, None, None, "LC", None),
    # S099
    ("S099", "an employment contract", "L", "repetition", "S098: the contract", "high", None, None, 1, None, None, "LC", None),
    ("S099", "termination of employment", "L", "synonym", "S036: getting sacked", "high", None, None, 1, None, None, "LC", None),
    # S100
    ("S100", "employer", "L", "repetition", "S045: employers", "high", None, "'an employer'", 1, None, None, "LC", None),
    ("S100", "a case", "L", "repetition", "S098: you've got a case", "high", None, None, 1, None, None, "LC", None),
    ("S100", "King said", "L", "repetition", "S098: King said", "high", None, None, 1, None, None, "LC", None),
    # S101
    ("S101", "Ash", "L", "repetition", "S081: Ash said", "high", None, None, 1, None, None, "LC", None),
    ("S101", "Jess", "L", "repetition", "S087: they said (Jess)", "high", None, None, 1, None, None, "LC", None),
    ("S101", "breached their employment contracts", "L", "repetition", "S099: an employment contract", "high", None, None, 1, None, None, "LC", None),
    # S102
    ("S102", "I", "R", "personal", "S101: Ash", "high", None, "quote Ash", 1, None, None, "LC", "A"),
    ("S102", "my employers", "L", "repetition", "S100: an employer", "high", None, None, 1, None, None, "LC", None),
    ("S102", "insane hours", "L", "repetition", "S074: 50 or more hours", "high", None, "chuỗi giờ", 1, None, None, "LC", None),
    ("S102", "Ash said", "L", "repetition", "S101: Ash", "high", None, None, 1, None, None, "LC", None),
    # S103
    ("S103", "Jess said", "L", "repetition", "S101: Jess", "high", None, "VI bỏ attribution này (§8)", 1, None, None, "LC", None),
    ("S103", "you", "R", "personal", "người đọc chung (ngoại văn bản — quote Jess)", "med", None, "occ 1 ('you can get'); 'you/your' ×3 trong câu", 1, None, None, "LC", "E"),
    # S104
    ("S104", "I", "R", "personal", "S103: Jess", "high", None, "quote", 1, None, None, "LC", "A"),
    # S105
    ("S105", "I", "R", "personal", "S104: I (Jess)", "high", None, "occ 1 ('I just think'), lần 2 'I think'", 1, None, None, "LC", "A"),
    ("S105", "employers", "L", "repetition", "S102: my employers", "high", None, "'employers have had their day'", 1, None, None, "LC", None),
]

TT = [
    # S002 (VI TỰ SINH — thay EN S002)
    ("S002", "Việc này", "R", "demonstrative", "S001: làm nhiều việc toàn thời gian", "high", None, "câu VI tự sinh (§8)", 1, None, None, "LC", "A"),
    # S003 (= ST S003)
    ("S003", "bảy công việc", "L", "repetition", "S001: làm việc cho nhiều nơi", "high", None, None, 1, None, None, "LC", None),
    ("S003", "toàn thời gian", "L", "repetition", "S001: làm việc toàn thời gian", "high", None, None, 1, None, None, "LC", None),
    # S004 (= ST S006)
    ("S004", "Cô", "R", "personal", "S003: Nga", "high", None, None, 1, None, None, "LC", "A"),
    ("S004", "nhiều công việc", "L", "repetition", "S001: nhiều nơi / S003: bảy công việc", "high", None, "'xoay sở nhiều công việc'", 1, None, None, "LC", None),
    # S005 (= ST S007)
    ("S005", "năm công việc", "L", "repetition", "S004: nhiều công việc", "high", None, None, 1, None, None, "LC", None),
    ("S005", "Nga", "L", "repetition", "S003: Nga", "high", None, "'một ngày của Nga'", 1, None, None, "LC", None),
    # S006 (= ST S008)
    ("S006", "Cô", "R", "personal", "S005: Nga", "high", None, None, 1, None, None, "LC", "A"),
    # S007 (= ST S009)
    ("S007", "cô", "R", "personal", "S006: Cô", "high", None, None, 1, None, None, "LC", "A"),
    ("S007", "công việc đầu tiên", "L", "repetition", "S005: năm công việc", "high", None, None, 1, None, None, "LC", None),
    # S008 (= ST S010)
    ("S008", "cô", "R", "personal", "S007: cô", "high", None, None, 1, None, None, "LC", "A"),
    ("S008", "công việc chính thức", "L", "repetition", "S007: công việc đầu tiên", "high", None, None, 1, None, None, "LC", None),
    # S009 (= ST S011)
    ("S009", "Tôi", "R", "personal", "S005: Nga", "high", None, "quote", 1, None, None, "LC", "A"),
    ("S009", "cô kể", "R", "personal", "S005: Nga", "high", None, None, 1, None, None, "LC", "A"),
    # S010 (= ST S012)
    ("S010", "cô", "R", "personal", "S009: cô kể", "high", None, None, 1, None, None, "LC", "A"),
    ("S010", "họp", "L", "repetition", "S009: họp nhóm", "high", None, "'tranh thủ họp'", 1, None, None, "LC", None),
    # S011 (= ST S013+S014 gộp)
    ("S011", "cô", "R", "personal", "S010: cô", "high", None, None, 1, None, None, "LC", "A"),
    # S012 (= ST S015)
    ("S012", "tôi", "R", "personal", "S005: Nga", "high", None, "quote", 1, None, None, "LC", "A"),
    ("S012", "Nga nói", "L", "repetition", "S005: Nga", "high", None, None, 1, None, None, "LC", None),
    # S013 (= ST S016)
    ("S013", "lịch họp", "L", "repetition", "S009–S010: họp", "high", None, "'trùng lịch họp'", 1, None, None, "LC", None),
    # S014 (= ST S017)
    ("S014", "Tôi", "R", "personal", "S012: Nga nói", "high", None, "quote", 1, None, None, "LC", "A"),
    # S016 (= ST S018)
    ("S016", "Nga", "L", "repetition", "S012: Nga nói", "high", None, "'Nga cho biết cô thay đổi' — cô trong câu", 1, None, None, "LC", None),
    # S017 (= ST S019)
    ("S017", "ngành công nghệ", "L", "associative", "S004: ngành phần mềm", "high", None, None, 1, None, None, "LC", None),
    ("S017", "bạn", "R", "personal", "người làm công nghệ chung (ngoại văn bản)", "med", None, "'nếu bạn nhanh nhẹn'", 1, None, None, "LC", "E"),
    # S018 (= ST S020)
    ("S018", "cô giải thích", "R", "personal", "S016: Nga", "high", None, None, 1, None, None, "LC", "A"),
    # S019 (= ST S021a)
    ("S019", "Tôi", "R", "personal", "S016: Nga", "high", None, "quote", 1, None, None, "LC", "A"),
    # S020 (= ST S021b)
    ("S020", "việc này", "R", "demonstrative", "S019: học cách làm nhanh, tận dụng công cụ", "high", None, "EN không có R tương ứng (§4.3)", 1, None, None, "LC", "A"),
    # S021 (= ST S022)
    ("S021", "Công việc này", "R", "demonstrative", "S004: xoay sở nhiều công việc", "high", None, "EN 'It can be' là it hư chỉ — VI thêm demonstrative", 1, None, None, "LC", "A"),
    ("S021", "Nga nói", "L", "repetition", "S016: Nga", "high", None, None, 1, None, None, "LC", None),
    # S022 (= ST S023)
    # S023 (= ST S024)
    ("S023", "Nga nói", "L", "repetition", "S021: Nga nói", "high", None, "'mục tiêu của cô' trong câu", 1, None, None, "LC", None),
    # S024 (= ST S025)
    ("S024", "cô", "R", "personal", "S023: Nga nói", "high", None, None, 1, None, None, "LC", "A"),
    ("S024", "hai công việc toàn thời gian", "L", "repetition", "S003: bốn công việc toàn thời gian", "high", None, None, 1, None, None, "LC", None),
    # S025 (= ST S026)
    ("S025", "Tôi", "R", "personal", "S023: Nga", "high", None, "quote", 1, None, None, "LC", "A"),
    ("S025", "làm như vậy", "S", "verbal", "S024: hai công việc toàn thời gian", "high", None, "[LC] pro-form — EN 'doing this' đánh R (bất đối xứng §7)", 1, None, None, "LC", None),
    # S026 (= ST S027; VI thêm 'Nhưng')
    ("S026", "Nhưng", "C", "adversative", "S025: 'không làm như vậy mãi' ↔ không đơn độc", "high", None, "VI-only C — EN không có liên từ", 1, None, None, "LC", None),
    ("S026", "Nga", "L", "repetition", "S023: Nga", "high", None, None, 1, None, None, "LC", None),
    # S027 (= ST S028+S029 gộp)
    ("S027", "Cô", "R", "personal", "S026: Nga", "high", None, None, 1, None, None, "LC", "A"),
    ("S027", "thu nhập", "L", "repetition", "S022: bảy nguồn thu nhập", "high", None, "'nhân đôi, nhân ba thu nhập'", 1, None, None, "LC", None),
    ("S027", "chuyện này", "R", "demonstrative", "S024: hai công việc toàn thời gian", "high", None, "'giấu kín chuyện này'", 1, None, None, "LC", "A"),
    ("S027", "chủ lao động", "L", "repetition", "S001: chủ lao động", "high", None, "'bất chấp rủi ro' = EN S029 gộp", 1, None, None, "LC", None),
    # S029 (= ST S031)
    ("S029", "nhiều công việc toàn thời gian", "L", "repetition", "S024: hai công việc toàn thời gian", "high", None, "'bí mật giữ nhiều công việc toàn thời gian'", 1, None, None, "LC", None),
    # S030 (= ST S032)
    ("S030", "diễn đàn", "L", "repetition", "S029: diễn đàn Reddit", "high", None, "'Khẩu hiệu của diễn đàn'", 1, None, None, "LC", None),
    # S031 (= ST S033)
    ("S031", "thành viên", "L", "associative", "S029: người đã tham gia", "high", None, None, 1, None, None, "LC", None),
    ("S031", "overemployed", "L", "repetition", "S001: over-employed", "high", None, None, 1, None, None, "LC", None),
    # S032 (= ST S034)
    ("S032", "Đây", "R", "demonstrative", "S031: overemployed", "high", None, "'Đây là biến tấu hiện đại'", 1, None, None, "LC", "A"),
    ("S032", "làm nhiều việc", "L", "repetition", "S029: nhiều công việc", "high", None, None, 1, None, None, "LC", None),
    # S033 (= ST S035+S036 gộp)
    ("S033", "người Úc", "L", "repetition", "S001: người Úc", "high", None, None, 1, None, None, "LC", None),
    ("S033", "chủ lao động", "L", "repetition", "S027: chủ lao động", "high", None, None, 1, None, None, "LC", None),
    # S034 (= ST S037)
    ("S034", "The Feed", "L", "repetition", "S022: The Feed", "high", None, None, 1, None, None, "LC", None),
    ("S034", "chủ cũ", "L", "repetition", "S033: chủ lao động", "high", None, "'chủ cũ hay chủ hiện tại' — chủ ×2", 1, None, None, "LC", None),
    # S035 (= ST S038)
    ("S035", "bị lộ", "L", "synonym", "S033: bị phát hiện", "high", None, "VI dịch retaliation → 'bị lộ' (§8)", 1, None, None, "LC", None),
    # S036 (= ST S039)
    ("S036", "kỹ sư phần mềm", "L", "associative", "S004: ngành phần mềm", "high", None, "'ông ta' trong câu", 1, None, None, "LC", None),
    ("S036", "bị sa thải", "L", "repetition", "S033: bị sa thải", "high", None, None, 1, None, None, "LC", None),
    ("S036", "startup công nghệ", "L", "associative", "S017: ngành công nghệ", "high", None, None, 1, None, None, "LC", None),
    # S037 (= ST S040+S041 gộp)
    ("S037", "người Úc khác", "L", "repetition", "S033: người Úc", "high", None, None, 1, None, None, "LC", None),
    ("S037", "nhân đôi thu nhập", "L", "repetition", "S027: nhân đôi, nhân ba thu nhập", "high", None, None, 1, None, None, "LC", None),
    ("S037", "xoay sở", "L", "repetition", "S004: xoay sở nhiều công việc", "high", None, None, 1, None, None, "LC", None),
    ("S037", "bốn công việc toàn thời gian", "L", "repetition", "S024: hai công việc toàn thời gian", "high", None, "'họ' = Tài trong câu", 1, None, None, "LC", None),
    # S038 (= ST S042)
    ("S038", "Tôi", "R", "personal", "S037: Tài", "high", None, "quote; 'mình' trong câu", 1, None, None, "LC", "A"),
    # S039 (= ST S043)
    ("S039", "Đây", "R", "demonstrative", "S038: làm việc chất lượng", "high", None, None, 1, None, None, "LC", "A"),
    ("S039", "bị bắt", "L", "synonym", "S033: bị phát hiện", "high", None, None, 1, None, None, "LC", None),
    ("S039", "sa thải", "L", "repetition", "S036: bị sa thải", "high", None, None, 1, None, None, "LC", None),
    ("S039", "Tài nói", "L", "repetition", "S037: Tài", "high", None, None, 1, None, None, "LC", None),
    # S040 (= ST S044)
    ("S040", "Các CEO", "L", "repetition", "S036: CEO", "high", None, None, 1, None, None, "LC", None),
    ("S040", "nhiều công việc", "L", "repetition", "S037: bốn công việc", "high", None, None, 1, None, None, "LC", None),
    ("S040", "chúng ta", "R", "personal", "người lao động chung (ngoại văn bản — quote Tài)", "med", None, "'vậy tại sao chúng ta phải'", 1, None, None, "LC", "E"),
    # S041 (= ST S045)
    ("S041", "chủ lao động", "L", "repetition", "S034: chủ", "high", None, None, 1, None, None, "LC", None),
    ("S041", "nhân viên toàn thời gian", "L", "repetition", "S003: toàn thời gian", "high", None, None, 1, None, None, "LC", None),
    # S042 (= ST S046)
    ("S042", "Họ", "R", "personal", "S041: chủ lao động", "high", None, None, 1, None, None, "LC", "A"),
    ("S042", "nhân viên", "L", "repetition", "S041: nhân viên toàn thời gian", "high", None, None, 1, None, None, "LC", None),
    ("S042", "ông nói", "R", "personal", "S041: Giáo sư Mark Wooden", "high", None, None, 1, None, None, "LC", "A"),
    # S043 (= ST S047)
    ("S043", "Tài", "L", "repetition", "S039: Tài nói", "high", None, None, 1, None, None, "LC", None),
    ("S043", "sự trung thành với một công ty", "L", "repetition", "S002: sự trung thành với công ty", "high", None, "tiền trạm ở câu VI tự sinh (§8)", 1, None, None, "LC", None),
    # S044 (= ST S048)
    ("S044", "nhân viên", "L", "repetition", "S042: nhân viên", "high", None, "'nhân viên văn phòng'", 1, None, None, "LC", None),
    ("S044", "đi họp", "L", "repetition", "S010: họp", "high", None, None, 1, None, None, "LC", None),
    ("S044", "Tài nói", "L", "repetition", "S043: Tài", "high", None, None, 1, None, None, "LC", None),
    # S045 (= ST S049)
    ("S045", "bạn", "R", "personal", "người làm việc chung (ngoại văn bản — quote)", "med", None, None, 1, None, None, "LC", "E"),
    ("S045", "40 giờ", "L", "repetition", "S004: 20 giờ mỗi ngày", "high", None, "chuỗi giờ", 1, None, None, "LC", None),
    ("S045", "chúng ta", "R", "personal", "người lao động chung (ngoại văn bản — quote Tài)", "med", None, None, 1, None, None, "LC", "E"),
    ("S045", "làm vậy", "S", "verbal", "S045: hoàn thành công việc trong ít hơn 40 giờ", "high", None, "[TC] pro-form — đối xứng EN 'do so'", 1, None, None, "TC", None),
    # S046 (= ST S050)
    ("S046", "Tuy nhiên", "C", "adversative", "S045: Tài lập luận tự do", "high", None, None, 1, None, None, "LC", None),
    ("S046", "Tài", "L", "repetition", "S044: Tài nói", "high", None, None, 1, None, None, "LC", None),
    ("S046", "làm nhiều việc một lúc", "L", "repetition", "S037: xoay sở bốn công việc", "high", None, None, 1, None, None, "LC", None),
    # S047 (= ST S051a)
    ("S047", "Tôi", "R", "personal", "S046: Tài", "high", None, "quote", 1, None, None, "LC", "A"),
    ("S047", "hai cuộc họp", "L", "repetition", "S044: đi họp", "high", None, None, 1, None, None, "LC", None),
    # S049-S050 (= ST S052-S053)
    # S050 (= ST S053)
    ("S050", "xoay sở", "L", "repetition", "S037: xoay sở", "high", None, "'việc xoay sở nhiều công việc'", 1, None, None, "LC", None),
    ("S050", "làm nhiều việc", "L", "repetition", "S046: làm nhiều việc một lúc", "high", None, None, 1, None, None, "LC", None),
    # S051 (= ST S054+S055 gộp)
    ("S051", "làm nhiều công việc", "L", "repetition", "S050: làm nhiều việc", "high", None, "'mức cao nhất kể từ cuối năm 2022' = EN S055", 1, None, None, "LC", None),
    # S052 (= ST S056)
    ("S052", "Trong khi đó", "C", "additive", "S051: số liệu multi-job", "high", None, None, 1, None, None, "LC", None),
    # S053 (= ST S057; VI thêm 'Tuy nhiên')
    ("S053", "Tuy nhiên", "C", "adversative", "S051–S052: số liệu việc làm", "high", None, "VI-only C — EN không có liên từ", 1, None, None, "LC", None),
    ("S053", "overemployment", "L", "repetition", "S031: overemployed", "high", None, None, 1, None, None, "LC", None),
    ("S053", "cộng đồng Reddit", "L", "repetition", "S029–S030: diễn đàn Reddit", "high", None, None, 1, None, None, "LC", None),
    # S054 (= ST S058)
    ("S054", "giáo sư Wooden", "L", "repetition", "S041: Giáo sư Mark Wooden", "high", None, None, 1, None, None, "LC", None),
    ("S054", "overemployment", "L", "repetition", "S053: overemployment", "high", None, None, 1, None, None, "LC", None),
    ("S054", "nhiều giờ", "L", "repetition", "S045: 40 giờ", "high", None, "'làm nhiều giờ hơn mong muốn'", 1, None, None, "LC", None),
    ("S054", "thu nhập", "L", "repetition", "S037: thu nhập", "high", None, "'nhu cầu thu nhập'", 1, None, None, "LC", None),
    # S055 (= ST S060)
    ("S055", "người làm nhiều việc", "L", "repetition", "S051: làm nhiều công việc", "high", None, None, 1, None, None, "LC", None),
    ("S055", "giờ làm", "L", "repetition", "S054: nhiều giờ", "high", None, "'muốn giảm giờ làm'", 1, None, None, "LC", None),
    # S056 (= ST S061)
    ("S056", "Nhưng", "C", "adversative", "S055: 25% muốn giảm giờ", "high", None, None, 1, None, None, "LC", None),
    ("S056", "người làm nhiều việc", "L", "repetition", "S055: người làm nhiều việc", "high", None, None, 1, None, None, "LC", None),
    ("S056", "người làm một việc", "L", "associative", "S055: người chỉ làm một việc", "high", None, None, 1, None, None, "LC", None),
    ("S056", "số giờ làm", "L", "repetition", "S055: giờ làm", "high", None, None, 1, None, None, "LC", None),
    # S057 (= ST S062)
    ("S057", "gói lương", "L", "associative", "S054: nhu cầu thu nhập", "med", None, "chuỗi thu nhập", 1, None, None, "LC", None),
    ("S057", "công việc toàn thời gian", "L", "repetition", "S029: nhiều công việc toàn thời gian", "high", None, "'công việc toàn thời gian thứ hai'", 1, None, None, "LC", None),
    # S058 (= ST S063)
    ("S058", "Anh", "R", "personal", "S057: Thanh", "high", None, None, 1, None, None, "LC", "A"),
    ("S058", "đó", "R", "demonstrative", "S057: công việc toàn thời gian thứ hai", "high", None, "'hy vọng đó sẽ là tấm vé'", 1, None, None, "LC", "A"),
    # S059 (= ST S064)
    ("S059", "Tôi", "R", "personal", "S057: Thanh", "high", None, "quote", 1, None, None, "LC", "A"),
    ("S059", "anh nói", "R", "personal", "S058: Anh", "high", None, None, 1, None, None, "LC", "A"),
    # S060 (= ST S066+S067a)
    ("S060", "Nga", "L", "repetition", "S023: Nga nói", "high", None, None, 1, None, None, "LC", None),
    ("S060", "bảy công việc", "L", "repetition", "S003: bảy công việc", "high", None, "'từ bảy công việc giờ chỉ còn hai'", 1, None, None, "LC", None),
    ("S060", "gia đình", "L", "repetition", "S023: nuôi gia đình", "high", None, None, 1, None, None, "LC", None),
    # S061 (= ST S067b — vế tách thành câu riêng)
    ("S061", "lương", "L", "repetition", "S057: gói lương", "high", None, "'Một đầu lương chỉ đủ trả tiền thuê nhà'", 1, None, None, "LC", None),
    # S063 (= ST S072)
    ("S063", "Cộng đồng", "L", "repetition", "S053: cộng đồng Reddit", "high", None, "'Cộng đồng overemployed' — overemployed lặp chuỗi", 1, None, None, "LC", None),
    ("S063", "giờ làm", "L", "repetition", "S056: số giờ làm", "high", None, "'xu hướng giảm giờ làm'", 1, None, None, "LC", None),
    # S064 (= ST S073+S074+S075 gộp)
    ("S064", "Giáo sư Wooden", "L", "repetition", "S054: giáo sư Wooden", "high", None, None, 1, None, None, "LC", None),
    ("S064", "50 giờ/tuần", "L", "repetition", "S063: giờ làm", "high", None, "'làm việc 50 giờ/tuần trở lên'", 1, None, None, "LC", None),
    # S065 (= ST S076+S077 gộp, paraphrase)
    ("S065", "làm nhiều giờ", "L", "repetition", "S064: 50 giờ/tuần", "high", None, None, 1, None, None, "LC", None),
    ("S065", "nhiều việc", "L", "repetition", "S050: làm nhiều việc", "high", None, "'làm nhiều giờ hoặc nhiều việc'", 1, None, None, "LC", None),
    # S066 (= ST S079, VI đảo thứ tự)
    ("S066", "bạn", "R", "personal", "người đọc chung (ngoại văn bản — quote Black)", "med", None, "'bạn' ×2 trong câu", 1, None, None, "LC", "E"),
    # S067 (= ST S078, VI đảo thứ tự; VI thêm 'Và')
    ("S067", "Và", "C", "additive", "S066: thời gian tập thể dục, nấu ăn", "high", None, "VI-only C — EN không có And", 1, None, None, "LC", None),
    ("S067", "làm việc nhiều giờ", "L", "repetition", "S065: làm nhiều giờ", "high", None, None, 1, None, None, "LC", None),
    ("S067", "sức khỏe", "L", "repetition", "S065: hệ quả sức khỏe", "high", None, "'sức khỏe kém hơn'", 1, None, None, "LC", None),
    # S068 (= ST S081)
    ("S068", "Nga", "L", "repetition", "S060: Nga", "high", None, "'dù cô vẫn thích' — cô trong câu", 1, None, None, "LC", None),
    ("S068", "kiệt sức", "L", "repetition", "S033: bị kiệt sức", "high", None, "'dấu hiệu kiệt sức'", 1, None, None, "LC", None),
    # S069 (= ST S082)
    ("S069", "cô", "R", "personal", "S068: Nga", "high", None, None, 1, None, None, "LC", "A"),
    ("S069", "con", "L", "repetition", "S014: con cái", "high", None, "'lời con nói'", 1, None, None, "LC", None),
    # S070 (= ST S085+S086+S087 gộp; VI thêm 'cũng')
    ("S070", "Tài", "L", "repetition", "S046: Tài", "high", None, None, 1, None, None, "LC", None),
    ("S070", "xoay sở bốn công việc", "L", "repetition", "S037: xoay sở bốn công việc toàn thời gian", "high", None, None, 1, None, None, "LC", None),
    ("S070", "cũng", "C", "additive", "S068–S069: Nga kiệt sức", "high", None, "VI-only C — 'Tài cũng đã quyết định nghỉ'", 1, None, None, "LC", None),
    # S071 (= ST S088)
    ("S071", "Tôi", "R", "personal", "S070: Tài", "high", None, "quote", 1, None, None, "LC", "A"),
    ("S071", "kiệt sức", "L", "repetition", "S068: kiệt sức", "high", None, "'Tôi bị kiệt sức'", 1, None, None, "LC", None),
    # S072 (= ST S089)
    ("S072", "giáo sư Wooden", "L", "repetition", "S064: Giáo sư Wooden", "high", None, None, 1, None, None, "LC", None),
    ("S072", "làm việc quá nhiều", "L", "repetition", "S067: làm việc nhiều giờ", "high", None, None, 1, None, None, "LC", None),
    ("S072", "tác động", "L", "repetition", "S070: tác động tiêu cực", "high", None, "'tác động tinh thần'", 1, None, None, "LC", None),
    ("S072", "thất nghiệp", "L", "associative", "S052: tỷ lệ thất nghiệp", "med", None, "VI dịch underemployment → 'thất nghiệp' (lệch nghĩa, §8)", 1, None, None, "LC", None),
    # S074 (= ST S094)
    ("S074", "điều này", "R", "demonstrative", "S073: tiểu đề 'Làm nhiều công việc toàn thời gian có hợp pháp không?'", "high", None, None, 1, None, None, "LC", "A"),
    # S075 (= ST S095)
    ("S075", "Bạn", "R", "personal", "người đọc chung (ngoại văn bản — quote King)", "med", None, "đầu câu viết hoa", 1, None, None, "LC", "E"),
    ("S075", "hợp đồng", "L", "repetition", "S074: hợp đồng lao động cá nhân", "high", None, "'xem hợp đồng có điều khoản'", 1, None, None, "LC", None),
    # S076 (= ST S096)
    ("S076", "mẫu hợp đồng", "L", "repetition", "S075: hợp đồng", "high", None, None, 1, None, None, "LC", None),
    ("S076", "nhân viên", "L", "repetition", "S044: nhân viên", "high", None, None, 1, None, None, "LC", None),
    ("S076", "bà nói", "R", "personal", "S074: Danny King", "high", None, "VI 'bà nói' — EN 'King said' là L lặp tên", 1, None, None, "LC", "A"),
    # S077 (= ST S098)
    ("S077", "nhân viên", "L", "repetition", "S076: nhân viên", "high", None, None, 1, None, None, "LC", None),
    ("S077", "bị phát hiện", "L", "repetition", "S033: bị phát hiện / S039: bị bắt", "high", None, None, 1, None, None, "LC", None),
    ("S077", "hợp đồng", "L", "repetition", "S076: mẫu hợp đồng", "high", None, "'đúng như hợp đồng'", 1, None, None, "LC", None),
    # S078 (= ST S099; VI thêm 'Nhưng')
    ("S078", "Nhưng", "C", "adversative", "S077: trường hợp vẫn hợp lệ", "high", None, "VI-only C — EN không có But", 1, None, None, "LC", None),
    ("S078", "vi phạm hợp đồng", "L", "repetition", "S077: hợp đồng", "high", None, None, 1, None, None, "LC", None),
    ("S078", "sa thải", "L", "repetition", "S039: sa thải", "high", None, None, 1, None, None, "LC", None),
    # S079 (= ST S100)
    ("S079", "công ty", "L", "repetition", "S043: một công ty", "high", None, None, 1, None, None, "LC", None),
    ("S079", "nhân viên", "L", "repetition", "S077: nhân viên", "high", None, "'kiện nhân viên'", 1, None, None, "LC", None),
    ("S079", "bà King", "L", "repetition", "S074: Danny King", "high", None, None, 1, None, None, "LC", None),
    # S080 (= ST S101)
    ("S080", "Nga", "L", "repetition", "S068: Nga", "high", None, None, 1, None, None, "LC", None),
    ("S080", "Tài", "L", "repetition", "S070: Tài", "high", None, None, 1, None, None, "LC", None),
    ("S080", "vi phạm hợp đồng", "L", "repetition", "S078: vi phạm hợp đồng", "high", None, None, 1, None, None, "LC", None),
    # S081 (= ST S102)
    ("S081", "Tôi", "R", "personal", "S080: Nga", "high", None, "quote; 'mình' trong câu", 1, None, None, "LC", "A"),
    ("S081", "người chủ", "L", "repetition", "S034: chủ cũ / S033: chủ lao động", "high", None, None, 1, None, None, "LC", None),
    ("S081", "chị Nga", "L", "repetition", "S080: Nga", "high", None, "VI thêm danh xưng 'chị'", 1, None, None, "LC", None),
    # S082 (= ST S103)
    ("S082", "công ty", "L", "repetition", "S079: công ty", "high", None, None, 1, None, None, "LC", None),
    ("S082", "bạn", "R", "personal", "người đọc chung (ngoại văn bản — quote)", "med", None, "'bạn làm gì… bạn hoàn thành' — bạn ×2", 1, None, None, "LC", "E"),
    # S083 (= ST S104)
    ("S083", "Tôi", "R", "personal", "S080: Nga và Tài (nguồn EN: quote Jess — VI bỏ attribution, §8)", "med", None, "conf med: VI mất dấu 'Tài nói'", 1, None, None, "LC", "A"),
    # S084 (= ST S105)
    ("S084", "tôi", "R", "personal", "S083: Tôi", "high", None, "'còn tôi nghĩ'", 1, None, None, "LC", "A"),
    ("S084", "các công ty", "L", "repetition", "S082: công ty", "high", None, None, 1, None, None, "LC", None),
]
