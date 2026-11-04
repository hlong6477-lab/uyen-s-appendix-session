# P24 tie table — WRITTEN BY HAND FROM work/analysis/P24_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# BẢN ĐỒ: ST 118 câu / TT 114 câu. KHỐI CẮT VI (tie chỉ EN):
#   S004 (chiến lược di trú 2023), S099 (Dutton referred to pledge),
#   S104–S105 (người phát ngôn Dutton).
# Đối xứng ST→TT: S001–S003→S001–S003; S005–S098→S004–S097;
#   S100–S103→S098–S101; S106→S102; S107–S118→S103–S114.
# Subhead không gán nhãn (EN S011/S017/S037/S046/S057/S063/S074/S095/S107).

ST = [
    # S002
    ("S002", "these changes", "R", "demonstrative", "S001: a suite of reforms", "high", None, "hậu chỉ về gói cải cách", 1, None, None, "LC", "A"),
    # S003
    ("S003", "big changes", "L", "repetition", "S002: these changes", "high", None, None, 1, None, None, "LC", None),
    ("S003", "the government", "L", "repetition", "S001: The government", "high", None, None, 1, None, None, "LC", None),
    # S004 — KHỐI CẮT VI (tie chỉ EN)
    ("S004", "The long-awaited strategy", "L", "synonym", "S003: big changes (gói cải cách)", "med", None, "mô tả lại gói cải cách; câu cắt phía VI", 1, None, None, "LC", None),
    ("S004", "the migration system", "L", "repetition", "S003: Australia's migration system", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S004", "skilled migration", "L", "repetition", "S001: temporary skilled migration", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S004", "international education", "L", "associative", "S001: international students", "med", None, "trường nghĩa giáo dục quốc tế; câu cắt phía VI", 1, None, None, "LC", None),
    # S005
    ("S005", "the Albanese government", "L", "repetition", "S003: the government", "high", None, None, 1, None, None, "LC", None),
    # S006
    ("S006", "permanent temporariness", "L", "repetition", "S003: permanent temporariness", "high", None, None, 1, None, None, "LC", None),
    ("S006", "the changes", "L", "repetition", "S002: these changes", "high", None, None, 1, None, None, "LC", None),
    ("S006", "I", "R", "personal", "S005: Ben Watt", "high", None, "đại từ ngôi 1 trong quote của Watt", 1, None, None, "LC", "A"),
    ("S006", "they've", "R", "personal", "S005: the Albanese government", "high", None, None, 1, None, None, "LC", "A"),
    ("S006", "he", "R", "personal", "S005: Ben Watt", "high", None, "'he told SBS News'; occ 4 vì he gặp 3 lần trong The/the/they've trước đó", 4, None, None, "LC", "A"),
    # S007
    ("S007", "Permanent temporariness", "L", "repetition", "S006: permanent temporariness", "high", None, None, 1, None, None, "LC", None),
    # S008
    ("S008", "Watt", "L", "repetition", "S005: Ben Watt", "high", None, None, 1, None, None, "LC", None),
    ("S008", "the reforms", "L", "repetition", "S001: a suite of reforms", "high", None, None, 1, None, None, "LC", None),
    ("S008", "the system", "L", "repetition", "S003: Australia's migration system", "med", None, "danh từ tổng quát chỉ hệ thống di trú", 1, None, None, "LC", None),
    ("S008", None, "E", "nominal", "S008: the reforms", "high", None, "[TC] some ∅ will work — tỉnh lược {reforms}; VI lấp đầy 'một số cải cách'", 1, "some ", "{reforms}", "TC", None),
    # S009
    ("S009", "this discussion", "R", "demonstrative", "S008: Watt argues some will fine tune", "high", None, None, 1, None, None, "LC", "A"),
    ("S009", "permanent visas", "L", "associative", "S003: permanent temporariness", "med", None, "chuỗi 'permanent' đối lập 'temporary'", 1, None, None, "LC", None),
    ("S009", "he", "R", "personal", "S008: Watt", "high", None, "'he said'; occ 5 vì he gặp 4 lần trong The/the trước đó", 5, None, None, "LC", "A"),
    # S010
    ("S010", "this", "R", "demonstrative", "S009: permanent visas staying about the same", "high", None, "'agreed this is a concern'", 1, None, None, "LC", "A"),
    # S012
    ("S012", "The government", "L", "repetition", "S005: the Albanese government", "high", None, None, 1, None, None, "LC", None),
    ("S012", "the permanent migration program", "L", "associative", "S009: permanent visas", "med", None, "chuỗi 'permanent'", 1, None, None, "LC", None),
    # S013
    ("S013", "It", "R", "personal", "S012: The government", "high", None, None, 1, None, None, "LC", "A"),
    ("S013", "places", "L", "repetition", "S012: 185,000 places", "high", None, None, 1, None, None, "LC", None),
    ("S013", "skilled migrants", "L", "repetition", "S001: temporary skilled migration", "high", None, None, 1, None, None, "LC", None),
    # S014
    ("S014", "were allocated", "L", "repetition", "S012: has allocated", "high", None, None, 1, None, None, "LC", None),
    # S015
    ("S015", "The former", "R", "comparative", "S014: Business Innovation and Investment", "high", None, None, 1, None, None, "LC", "A"),
    ("S015", "the latter", "R", "comparative", "S014: Global Talent visa stream", "high", None, None, 1, None, None, "LC", "A"),
    # S016
    ("S016", "the announced changes", "L", "repetition", "S002: these changes", "high", None, None, 1, None, None, "LC", None),
    ("S016", "reforms", "L", "repetition", "S008: the reforms", "high", None, None, 1, None, None, "LC", None),
    ("S016", "the skilled visa program", "L", "associative", "S013: skilled migrants", "med", None, "chuỗi 'skilled'", 1, None, None, "LC", None),
    # S018
    ("S018", "the government", "L", "repetition", "S012: The government", "high", None, None, 1, None, None, "LC", None),
    ("S018", "international student enrolments", "L", "repetition", "S001: international students", "high", None, None, 1, None, None, "LC", None),
    # S019
    ("S019", "However", "C", "adversative", "S018: government proposed capping", "high", None, None, 1, None, None, "LC", None),
    ("S019", "the plan", "L", "synonym", "S018: proposed capping enrolments", "high", None, "mô tả lại đề xuất", 1, None, None, "LC", None),
    ("S019", "the government", "L", "repetition", "S018: the government", "high", None, None, 1, None, None, "LC", None),
    # S020
    ("S020", "In response", "C", "causal", "S019: Opposition blocked the plan", "high", None, "VI không hiện thực hóa nối (chỉ 'hiện đã')", 1, None, None, "LC", None),
    ("S020", "the government", "L", "repetition", "S019: the government", "high", None, None, 1, None, None, "LC", None),
    ("S020", "international students", "L", "repetition", "S018: international student enrolments", "high", None, None, 1, None, None, "LC", None),
    # S021
    ("S021", "student visa processing", "L", "associative", "S018: international student enrolments", "med", None, None, 1, None, None, "LC", None),
    ("S021", "capping", "L", "repetition", "S018: capping", "high", None, None, 1, None, None, "LC", None),
    # S022
    ("S022", "international education providers", "L", "associative", "S004: international education / S001: international students", "med", None, None, 1, None, None, "LC", None),
    ("S022", "high priority", "L", "repetition", "S021: high priority", "high", None, None, 1, None, None, "LC", None),
    # S023
    ("S023", "they", "R", "personal", "S022: All international education providers", "high", None, None, 1, None, None, "LC", "A"),
    ("S023", "standard priority", "L", "repetition", "S021: standard priority", "high", None, None, 1, None, None, "LC", None),
    # S024
    ("S024", "the change", "L", "synonym", "S020–S021: new way / direction 111", "med", None, None, 1, None, None, "LC", None),
    ("S024", "the cap", "L", "repetition", "S018: capping", "high", None, None, 1, None, None, "LC", None),
    ("S024", "this option", "R", "demonstrative", "S020–S021: new way / direction 111", "high", None, None, 1, None, None, "LC", "A"),
    ("S024", "us", "R", "personal", "S020: the government (phía Bộ trưởng Burke)", "high", None, "quote Burke; occ 2 vì us gặp trong 'use' ngay sau đó", 2, None, None, "LC", "A"),
    # S025
    ("S025", "The new scheme", "L", "synonym", "S021: ministerial direction 111", "high", None, None, 1, None, None, "LC", None),
    ("S025", "ministerial direction 107", "L", "repetition", "S021: ministerial direction 111", "high", None, "lặp khung 'ministerial direction'", 1, None, None, "LC", None),
    ("S025", "the government", "L", "repetition", "S020: the government", "high", None, None, 1, None, None, "LC", None),
    ("S025", "student numbers", "L", "repetition", "S021: capping numbers / S018: enrolments", "high", None, None, 1, None, None, "LC", None),
    ("S025", "visa processing", "L", "repetition", "S021: student visa processing", "high", None, None, 1, None, None, "LC", None),
    # S026
    ("S026", "changes", "L", "repetition", "S016: the announced changes", "high", None, None, 1, None, None, "LC", None),
    ("S026", "the student visa program", "L", "repetition", "S021: student visa processing", "high", None, None, 1, None, None, "LC", None),
    # S027
    ("S027", "This", "R", "demonstrative", "S026: several other changes", "high", None, None, 1, None, None, "LC", "A"),
    ("S027", "reforms", "L", "repetition", "S016: reforms", "high", None, None, 1, None, None, "LC", None),
    ("S027", "a student visa", "L", "repetition", "S026: the student visa program", "high", None, None, 1, None, None, "LC", None),
    ("S027", "temporary visa holders", "L", "associative", "S003: visa holders", "med", None, "chuỗi 'temporary' + 'visa holders'", 1, None, None, "LC", None),
    # S028
    ("S028", "temporary graduate", "L", "associative", "S027: temporary visa holders", "med", None, None, 1, None, None, "LC", None),
    ("S028", "apply", "L", "repetition", "S027: applying for a student visa", "high", None, None, 1, None, None, "LC", None),
    # S029
    ("S029", "The full list", "L", "synonym", "S027: restrictions barring visa holders", "med", None, "mô tả lại danh sách hạn chế", 1, None, None, "LC", None),
    # S030
    ("S030", "Visa hopping", "L", "repetition", "S007: visa hopping", "high", None, None, 1, None, None, "LC", None),
    ("S030", "permanently temporary", "L", "repetition", "S007: Permanent temporariness", "high", None, "biến thể của cụm then chốt", 1, None, None, "LC", None),
    ("S030", "former international students", "L", "repetition", "S018: international student enrolments", "high", None, None, 1, None, None, "LC", None),
    ("S030", "the department", "L", "repetition", "S029: the Department of Home Affairs", "high", None, None, 1, None, None, "LC", None),
    # S031
    ("S031", "These changes", "R", "demonstrative", "S027: restrictions introduced", "high", None, None, 1, None, None, "LC", "A"),
    ("S031", "this loophole", "R", "demonstrative", "S030: Visa hopping", "high", None, None, 1, None, None, "LC", "A"),
    ("S031", "this practice", "R", "demonstrative", "S030: Visa hopping", "high", None, None, 1, None, None, "LC", "A"),
    # S032
    ("S032", "Also", "C", "additive", "S028: From 1 July last year changes", "high", None, None, 1, None, None, "LC", None),
    ("S032", "international student visas", "L", "repetition", "S026: the student visa program", "high", None, None, 1, None, None, "LC", None),
    # S033
    ("S033", "student and student guardian visa applicants", "L", "repetition", "S027: applying for a student visa", "high", None, None, 1, None, None, "LC", None),
    # S034
    ("S034", "also", "C", "additive", "S032–S033: fee and capacity changes", "high", None, None, 1, None, None, "LC", None),
    ("S034", "requirements", "L", "repetition", "S033: requirement", "high", None, None, 1, None, None, "LC", None),
    ("S034", "came into effect", "L", "repetition", "S016: came into effect", "high", None, None, 1, None, None, "LC", None),
    # S035
    ("S035", "Rizvi", "L", "repetition", "S010: Abul Rizvi", "high", None, None, 1, None, None, "LC", None),
    ("S035", "the student visa policy changes", "L", "repetition", "S026: changes to the student visa program", "high", None, None, 1, None, None, "LC", None),
    # S036
    ("S036", "these", "R", "demonstrative", "S035: the student visa policy changes", "high", None, None, 1, None, None, "LC", "A"),
    ("S036", "he", "R", "personal", "S035: Rizvi", "high", None, "'he said'; occ 4 vì he gặp 3 lần trong these/the trước đó", 4, None, None, "LC", "A"),
    ("S036", "application rates", "L", "repetition", "S027: applying / S028: unable to apply", "high", None, None, 1, None, None, "LC", None),
    # S038
    ("S038", "changes", "L", "repetition", "S016: the announced changes", "high", None, None, 1, None, None, "LC", None),
    ("S038", "came into effect", "L", "repetition", "S034: came into effect", "high", None, None, 1, None, None, "LC", None),
    ("S038", "Temporary Graduate visa (TGV) holders", "L", "repetition", "S028: temporary graduate", "high", None, None, 1, None, None, "LC", None),
    ("S038", None, "E", "verbal", "S038: was reduced", "high", None, "[TC] and a new age limit ∅ imposed — tỉnh lược {was}", 1, "and a new age limit ", "{was}", "TC", None),
    # S039
    ("S039", "The Temporary Graduate Visa", "L", "repetition", "S038: Temporary Graduate visa (TGV)", "high", None, None, 1, None, None, "LC", None),
    ("S039", "streams", "L", "repetition", "S014: visa streams", "high", None, None, 1, None, None, "LC", None),
    # S040
    ("S040", "The age limit", "L", "repetition", "S038: a new age limit", "high", None, None, 1, None, None, "LC", None),
    # S041
    ("S041", "Those", "S", "nominal", "S038: Temporary Graduate visa (TGV) holders", "high", None, None, 1, None, None, "LC", None),
    ("S041", "eligible", "L", "repetition", "S033: to be eligible", "high", None, None, 1, None, None, "LC", None),
    # S042
    ("S042", "passport holders", "L", "repetition", "S038: (TGV) holders", "med", None, None, 1, None, None, "LC", None),
    ("S042", "still eligible until age 50", "L", "repetition", "S041: still eligible until the age of 50", "high", None, None, 1, None, None, "LC", None),
    ("S042", "also", "C", "additive", "S041: master's/PhD still eligible", "high", None, None, 1, None, None, "LC", None),
    # S043
    ("S043", "The length of stay", "L", "repetition", "S038: the length of stay", "high", None, None, 1, None, None, "LC", None),
    ("S043", "holders of a TGV", "L", "repetition", "S038: (TGV) holders", "high", None, None, 1, None, None, "LC", None),
    ("S043", "Post-Vocational Education Work stream", "L", "repetition", "S039: Post-Vocational Education Work", "high", None, None, 1, None, None, "LC", None),
    # S044
    ("S044", "But", "C", "adversative", "S043: length of stay doesn't change", "high", None, None, 1, None, None, "LC", None),
    ("S044", "those", "S", "nominal", "S038: Temporary Graduate visa (TGV) holders", "high", None, None, 1, None, None, "LC", None),
    ("S044", "the Post-Higher Education Work stream", "L", "repetition", "S039: Post-Higher Education", "high", None, None, 1, None, None, "LC", None),
    ("S044", "the length of stay", "L", "repetition", "S043: The length of stay", "high", None, None, 1, None, None, "LC", None),
    # S045
    ("S045", "a master's degree by coursework", "L", "repetition", "S041: a master's degree", "high", None, None, 1, None, None, "LC", None),
    ("S045", "the maximum stay", "L", "synonym", "S044: can stay up to two years", "high", None, None, 1, None, None, "LC", None),
    ("S045", None, "E", "nominal", "S045: the maximum stay will be up to", "high", None, "[TC] or a PhD, ∅ three years — tỉnh lược {the maximum stay will be up to}", 1, "or a PhD, ", "{the maximum stay will be up to}", "TC", None),
    # S047
    ("S047", "Watt", "L", "repetition", "S008: Watt", "high", None, None, 1, None, None, "LC", None),
    ("S047", "changes", "L", "repetition", "S016: the announced changes", "high", None, None, 1, None, None, "LC", None),
    ("S047", "employer-sponsored visas", "L", "repetition", "S013: employer-sponsored visas", "high", None, None, 1, None, None, "LC", None),
    # S048
    ("S048", "The new visa", "L", "synonym", "S047: a Skills in Demand (SID) visa", "high", None, None, 1, None, None, "LC", None),
    ("S048", "replaced", "L", "repetition", "S015: was replaced", "high", None, None, 1, None, None, "LC", None),
    ("S048", "an employer to sponsor", "L", "repetition", "S047: employer-sponsored visas", "high", None, None, 1, None, None, "LC", None),
    ("S048", "eligible worker", "L", "repetition", "S041: eligible", "med", None, "chuỗi 'eligible'", 1, None, None, "LC", None),
    # S049
    ("S049", "the SID", "L", "repetition", "S047: (SID) visa", "high", None, None, 1, None, None, "LC", None),
    ("S049", "streams", "L", "repetition", "S039: streams", "high", None, None, 1, None, None, "LC", None),
    ("S049", "took effect", "L", "synonym", "S034: came into effect", "high", None, None, 1, None, None, "LC", None),
    # S050
    ("S050", "Those who are eligible", "S", "nominal", "S048: an eligible worker", "high", None, None, 1, None, None, "LC", None),
    ("S050", "the visa", "L", "repetition", "S048: The new visa", "high", None, None, 1, None, None, "LC", None),
    ("S050", "Hong Kong passport holders", "L", "repetition", "S042: Hong Kong... passport holders", "high", None, None, 1, None, None, "LC", None),
    ("S050", "stay", "L", "repetition", "S043–S044: length of stay / can stay", "high", None, "occ=2: can stay + may stay", 2, None, None, "LC", None),
    # S051
    ("S051", "The visa", "L", "repetition", "S050: the visa", "high", None, None, 1, None, None, "LC", None),
    ("S051", "streams", "L", "repetition", "S049: streams", "high", None, None, 1, None, None, "LC", None),
    ("S051", "highly-skilled migrants", "L", "repetition", "S013: skilled migrants", "high", None, None, 1, None, None, "LC", None),
    ("S051", "shortages", "L", "repetition", "S048: Temporary Skills Shortage", "med", None, None, 1, None, None, "LC", None),
    ("S051", "those", "S", "nominal", "S051: highly-skilled migrants", "high", None, "[TC] those ← migrants", 1, None, None, "TC", None),
    # S052
    ("S052", "the core skills stream", "L", "repetition", "S051: Core Skills", "high", None, None, 1, None, None, "LC", None),
    ("S052", "eligible holders", "L", "repetition", "S050: Those who are eligible", "high", None, None, 1, None, None, "LC", None),
    ("S052", "sponsored", "L", "repetition", "S048: an employer to sponsor", "high", None, None, 1, None, None, "LC", None),
    ("S052", "the government's", "L", "repetition", "S025: the government", "high", None, None, 1, None, None, "LC", None),
    # S053
    ("S053", "They", "R", "personal", "S052: eligible holders", "high", None, None, 1, None, None, "LC", "A"),
    ("S053", "Core Skills Income Threshold", "L", "repetition", "S051–S052: Core Skills", "high", None, None, 1, None, None, "LC", None),
    ("S053", "Temporary Skilled Migration Income Threshold", "L", "repetition", "S001: temporary skilled migration", "high", None, None, 1, None, None, "LC", None),
    # S054
    ("S054", "Applicants", "L", "repetition", "S036: application rates / S027: applying", "med", None, None, 1, None, None, "LC", None),
    ("S054", "the specialist skills stream", "L", "repetition", "S051: Specialist Skills", "high", None, None, 1, None, None, "LC", None),
    ("S054", "must meet", "L", "repetition", "S053: must meet", "high", None, None, 1, None, None, "LC", None),
    ("S054", "occupation", "L", "repetition", "S052: an occupation", "high", None, None, 1, None, None, "LC", None),
    # S055
    ("S055", "Income thresholds", "L", "repetition", "S053–S054: Income Threshold", "high", None, None, 1, None, None, "LC", None),
    # S056
    ("S056", "The existing Labour Agreement stream", "L", "repetition", "S051: a labour agreement", "high", None, None, 1, None, None, "LC", None),
    ("S056", "the TSS visa", "L", "repetition", "S048: (TSS, subclass 482) visa", "high", None, None, 1, None, None, "LC", None),
    ("S056", "the SID visa", "L", "repetition", "S049: the SID", "high", None, None, 1, None, None, "LC", None),
    ("S056", "Home Affairs department", "L", "repetition", "S029: the Department of Home Affairs", "high", None, None, 1, None, None, "LC", None),
    # S058
    ("S058", "Also", "C", "additive", "S049–S052: December changes", "high", None, None, 1, None, None, "LC", None),
    ("S058", "a National Innovation visa", "L", "repetition", "S015: a new National Innovation visa", "high", None, None, 1, None, None, "LC", None),
    ("S058", "replaced", "L", "repetition", "S048: replaced", "high", None, None, 1, None, None, "LC", None),
    ("S058", "the Global Talent stream", "L", "repetition", "S014: Global Talent visa streams", "high", None, None, 1, None, None, "LC", None),
    ("S058", "a permanent visa", "L", "associative", "S012: the permanent migration program", "med", None, "chuỗi 'permanent'", 1, None, None, "LC", None),
    # S059
    ("S059", "applicants", "L", "repetition", "S054: Applicants", "high", None, None, 1, None, None, "LC", None),
    ("S059", "the Home Affairs department", "L", "repetition", "S056: Home Affairs department", "high", None, None, 1, None, None, "LC", None),
    # S060
    ("S060", "Global Talent", "L", "repetition", "S058: the Global Talent stream", "high", None, None, 1, None, None, "LC", None),
    ("S060", "applications", "L", "repetition", "S027: applying / S054: Applicants", "high", None, None, 1, None, None, "LC", None),
    ("S060", "processed", "L", "repetition", "S021: student visa processing", "high", None, None, 1, None, None, "LC", None),
    ("S060", "priorities", "L", "repetition", "S021: high/standard priority", "high", None, None, 1, None, None, "LC", None),
    # S061
    ("S061", "Watt", "L", "repetition", "S047: Watt", "high", None, None, 1, None, None, "LC", None),
    ("S061", "the new visa", "L", "synonym", "S058: a National Innovation visa", "high", None, None, 1, None, None, "LC", None),
    ("S061", "the previous visa", "R", "comparative", "S058: the Global Talent stream", "high", None, None, 1, None, None, "LC", "A"),
    # S062
    ("S062", "permanent visas", "L", "repetition", "S009: permanent visas", "high", None, None, 1, None, None, "LC", None),
    ("S062", "the same", "R", "comparative", "S009: staying about the same", "high", None, None, 1, None, None, "LC", "A"),
    # S064
    ("S064", "The government", "L", "repetition", "S052: the government's", "high", None, None, 1, None, None, "LC", None),
    ("S064", "those", "S", "nominal", "S064: certain kinds of visas", "high", None, "[TC] those ← certain kinds of visas", 1, None, None, "TC", None),
    # S065
    ("S065", "ballot registrations", "L", "repetition", "S064: a pre-application ballot process", "high", None, None, 1, None, None, "LC", None),
    ("S065", "visa applicants", "L", "repetition", "S054: Applicants", "high", None, None, 1, None, None, "LC", None),
    ("S065", "Work and Holiday", "L", "synonym", "S064: Working Holiday Maker program", "high", None, None, 1, None, None, "LC", None),
    # S066
    ("S066", "The department", "L", "repetition", "S059: the Home Affairs department", "high", None, None, 1, None, None, "LC", None),
    ("S066", "the process", "L", "repetition", "S064: a pre-application ballot process", "high", None, None, 1, None, None, "LC", None),
    ("S066", "applicants", "L", "repetition", "S065: visa applicants", "high", None, None, 1, None, None, "LC", None),
    ("S066", "places", "L", "repetition", "S012–S013: places", "high", None, None, 1, None, None, "LC", None),
    # S067
    ("S067", "A ballot", "L", "repetition", "S064–S066: ballot process", "high", None, None, 1, None, None, "LC", None),
    ("S067", "also", "C", "additive", "S065: ballot for Work and Holiday", "high", None, None, 1, None, None, "LC", None),
    ("S067", "a new temporary visa", "L", "associative", "S027: temporary visa holders", "med", None, "chuỗi 'temporary visa'", 1, None, None, "LC", None),
    # S068
    ("S068", "Indian", "L", "repetition", "S067: Indian nationals", "high", None, None, 1, None, None, "LC", None),
    ("S068", "register", "L", "repetition", "S065: ballot registrations", "high", None, None, 1, None, None, "LC", None),
    # S069
    ("S069", "places will be allocated", "L", "repetition", "S012–S013: allocated... places", "high", None, None, 1, None, None, "LC", None),
    # S070
    ("S070", "ballot", "L", "repetition", "S067: A ballot", "high", None, None, 1, None, None, "LC", None),
    ("S070", "registration", "L", "repetition", "S065: ballot registrations / S068: register", "high", None, None, 1, None, None, "LC", None),
    # S071
    ("S071", "It", "R", "personal", "S070: The first ballot", "high", None, None, 1, None, None, "LC", "A"),
    ("S071", "ballot", "L", "repetition", "S070: ballot", "high", None, None, 1, None, None, "LC", None),
    ("S071", "live and work in Australia", "L", "repetition", "S067: live and work in Australia", "high", None, None, 1, None, None, "LC", None),
    ("S071", "migrants", "L", "repetition", "S013: skilled migrants / S051: migrants", "high", None, None, 1, None, None, "LC", None),
    ("S071", "permanently", "L", "repetition", "S058: a permanent visa", "med", None, "chuỗi 'permanent'", 1, None, None, "LC", None),
    # S072
    ("S072", "Pacific", "L", "repetition", "S071: Pacific countries", "high", None, None, 1, None, None, "LC", None),
    ("S072", "permanent places", "L", "repetition", "S012: places / permanent chain", "high", None, None, 1, None, None, "LC", None),
    ("S072", "the permanent migration program", "L", "repetition", "S012: the permanent migration program", "high", None, None, 1, None, None, "LC", None),
    # S073
    ("S073", "the PEV", "L", "repetition", "S072: The Pacific Engagement visa (PEV)", "high", None, None, 1, None, None, "LC", None),
    ("S073", "a ballot", "L", "repetition", "S071: the first ballot", "high", None, None, 1, None, None, "LC", None),
    # S075
    ("S075", "The government", "L", "repetition", "S064: The government", "high", None, None, 1, None, None, "LC", None),
    ("S075", "strategy", "L", "repetition", "S004: The long-awaited strategy", "med", None, "tiền trạm nằm ở câu bị cắt phía VI", 1, None, None, "LC", None),
    ("S075", "migration", "L", "repetition", "S072: the permanent migration program", "high", None, None, 1, None, None, "LC", None),
    # S076
    ("S076", "pandemic", "L", "repetition", "S075: pre-pandemic levels", "high", None, None, 1, None, None, "LC", None),
    ("S076", "migration levels", "L", "repetition", "S075: return migration", "high", None, None, 1, None, None, "LC", None),
    # S077
    ("S077", "NOM", "L", "repetition", "S076: net overseas migration or NOM", "high", None, None, 1, None, None, "LC", None),
    ("S077", "migrants", "L", "repetition", "S071: migrants", "high", None, None, 1, None, None, "LC", None),
    # S078
    ("S078", "borders", "L", "repetition", "S076: close its borders", "high", None, None, 1, None, None, "LC", None),
    ("S078", "temporary and permanent migrants", "L", "repetition", "S077: migrants / temporary-permanent chains", "high", None, None, 1, None, None, "LC", None),
    # S079
    ("S079", "Net migration", "L", "repetition", "S076: net overseas migration", "high", None, None, 1, None, None, "LC", None),
    # S080
    ("S080", "That", "R", "demonstrative", "S079: went over half a million", "high", None, None, 1, None, None, "LC", "A"),
    # S081
    ("S081", "But", "C", "adversative", "S079–S080: panic over record migration", "high", None, None, 1, None, None, "LC", None),
    ("S081", "the level of migration", "L", "repetition", "S076: migration levels", "high", None, None, 1, None, None, "LC", None),
    ("S081", "the same", "R", "comparative", "S075: near pre-pandemic levels", "high", None, None, 1, None, None, "LC", "A"),
    ("S081", "you", "R", "personal", "người đọc chung (ngoại văn bản — quote McDonald)", "med", None, "'you' phiếm chỉ trong quote", 1, None, None, "LC", "E"),
    # S082
    ("S082", "It", "R", "personal", "S081: the level of migration", "high", None, None, 1, None, None, "LC", "A"),
    # S083
    ("S083", "The problem", "L", "synonym", "S079–S080: net migration surge / panic", "med", None, "mô tả lại tình trạng", 1, None, None, "LC", None),
    ("S083", "the government's", "L", "repetition", "S075: The government", "high", None, None, 1, None, None, "LC", None),
    # S084
    ("S084", "NOM", "L", "repetition", "S077: NOM", "high", None, None, 1, None, None, "LC", None),
    # S085
    ("S085", "This", "R", "demonstrative", "S084: 446,000 in 2023-24", "high", None, None, 1, None, None, "LC", "A"),
    ("S085", "forecast", "L", "repetition", "S083: the government's projections", "high", None, None, 1, None, None, "LC", None),
    # S086
    ("S086", "It", "R", "personal", "S084: annual NOM dropped", "high", None, None, 1, None, None, "LC", "A"),
    ("S086", "borders", "L", "repetition", "S078: the reopening of borders", "high", None, None, 1, None, None, "LC", None),
    # S087
    ("S087", "Migrant arrivals", "L", "repetition", "S078: arrivals of temporary and permanent migrants", "high", None, None, 1, None, None, "LC", None),
    ("S087", "departures", "L", "repetition", "S083: fewer departures", "high", None, None, 1, None, None, "LC", None),
    # S088
    ("S088", "Rizvi", "L", "repetition", "S035: Rizvi", "high", None, None, 1, None, None, "LC", None),
    ("S088", "this fall", "R", "demonstrative", "S087: arrivals fell 10 per cent", "high", None, None, 1, None, None, "LC", "A"),
    ("S088", "the government's", "L", "repetition", "S083: the government's", "high", None, None, 1, None, None, "LC", None),
    ("S088", "changes", "L", "repetition", "S016: the announced changes", "high", None, None, 1, None, None, "LC", None),
    # S089
    ("S089", "The government", "L", "repetition", "S088: the government's", "high", None, None, 1, None, None, "LC", None),
    ("S089", "NOM", "L", "repetition", "S084: NOM", "high", None, None, 1, None, None, "LC", None),
    ("S089", "projected", "L", "repetition", "S083: projections / S085: forecast", "high", None, None, 1, None, None, "LC", None),
    # S090
    ("S090", "Its", "R", "personal", "S089: The government", "high", None, "sở hữu cách", 1, None, None, "LC", "A"),
    ("S090", "this figure", "R", "demonstrative", "S089: 260,000 in 2024-25", "high", None, None, 1, None, None, "LC", "A"),
    ("S090", "revised", "L", "repetition", "S085: its revised projection", "high", None, None, 1, None, None, "LC", None),
    # S091
    ("S091", "The forecast", "L", "repetition", "S085: forecast / S089: projected", "high", None, None, 1, None, None, "LC", None),
    # S092
    ("S092", "It's", "R", "personal", "S090: 340,000 (revised NOM)", "high", None, "quote McDonald", 1, None, None, "LC", "A"),
    ("S092", "it's", "R", "personal", "S090: 340,000 (revised NOM)", "high", None, "quote McDonald; viết thường", 1, None, None, "LC", "A"),
    # S093
    ("S093", "And", "C", "additive", "S092: it's coming down", "high", None, None, 1, None, None, "LC", None),
    ("S093", "we", "R", "personal", "nước Úc/chúng ta chung (ngoại văn bản — quote McDonald)", "med", None, None, 1, None, None, "LC", "E"),
    ("S093", "it", "R", "personal", "S090: 340,000 (revised NOM)", "high", None, None, 1, None, None, "LC", "A"),
    ("S093", "panic", "L", "repetition", "S080: a bit of panic", "high", None, None, 1, None, None, "LC", None),
    ("S093", "departures", "L", "repetition", "S087: departures", "high", None, None, 1, None, None, "LC", None),
    # S094
    ("S094", "we'll", "R", "personal", "nước Úc/chúng ta chung (ngoại văn bản — quote McDonald)", "med", None, None, 1, None, None, "LC", "E"),
    ("S094", "back to normal", "L", "synonym", "S075: near pre-pandemic levels", "med", None, "normal ≈ mức trước đại dịch", 1, None, None, "LC", None),
    ("S094", "McDonald", "L", "repetition", "S080: Peter McDonald", "high", None, None, 1, None, None, "LC", None),
    ("S094", "MYEFO", "L", "repetition", "S090: Mid-Year Economic and Fiscal Outlook (MYEFO)", "high", None, None, 1, None, None, "LC", None),
    # S096
    ("S096", "Peter Dutton", "L", "repetition", "S024: Peter Dutton", "high", None, None, 1, None, None, "LC", None),
    ("S096", "permanent migration", "L", "repetition", "S072: the permanent migration program", "high", None, None, 1, None, None, "LC", None),
    # S097
    ("S097", "he", "R", "personal", "S096: Peter Dutton", "high", None, "'he also pledged'; occ 2 vì he gặp trong 'the following' trước đó", 2, None, None, "LC", "A"),
    ("S097", "also", "C", "additive", "S096: pledged to cut permanent migration", "high", None, None, 1, None, None, "LC", None),
    ("S097", "pledged", "L", "repetition", "S096: pledged", "high", None, None, 1, None, None, "LC", None),
    ("S097", "net overseas migration", "L", "repetition", "S076: net overseas migration or NOM", "high", None, None, 1, None, None, "LC", None),
    # S098
    ("S098", "Dutton", "L", "repetition", "S096: Peter Dutton", "high", None, None, 1, None, None, "LC", None),
    ("S098", "NOM", "L", "repetition", "S097: net overseas migration", "high", None, None, 1, None, None, "LC", None),
    # S099 — KHỐI CẮT VI (tie chỉ EN)
    ("S099", "Instead", "C", "adversative", "S098: repeatedly asked about NOM target", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S099", "he", "R", "personal", "S098: Dutton", "high", None, "câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S099", "permanent migration pledge", "L", "repetition", "S096–S097: pledged to cut permanent migration", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S100
    ("S100", "we", "R", "personal", "phe Dutton/Liên đảng (ngoại văn bản — quote)", "med", None, "occ=2: we've said + we want", 2, None, None, "LC", "E"),
    # S101
    ("S101", "And", "C", "additive", "S100: migration to step down", "high", None, None, 1, None, None, "LC", None),
    ("S101", "we", "R", "personal", "phe Dutton/Liên đảng (ngoại văn bản — quote)", "med", None, None, 1, None, None, "LC", "E"),
    ("S101", "the numbers", "L", "repetition", "S021: capping numbers / S062: numbers", "high", None, None, 1, None, None, "LC", None),
    ("S101", "Dutton said", "L", "repetition", "S098: Dutton", "high", None, None, 1, None, None, "LC", None),
    # S102
    ("S102", "That's", "R", "demonstrative", "S101: bring numbers to long-run average", "high", None, None, 1, None, None, "LC", "A"),
    ("S102", "our", "R", "personal", "nước Úc (ngoại văn bản — quote Dutton)", "med", None, "'our country'", 1, None, None, "LC", "E"),
    # S103
    ("S103", "Again", "C", "additive", "S100–S102: các cam kết", "high", None, "khẳng định lại", 1, None, None, "LC", None),
    ("S103", "we", "R", "personal", "phe Dutton/Liên đảng (ngoại văn bản — quote)", "med", None, "occ=4: we'll, we said, we come, we need", 4, None, None, "LC", "E"),
    ("S103", "the government", "L", "repetition", "S089: The government", "high", None, "'come into the government'", 1, None, None, "LC", None),
    # S104 — KHỐI CẮT VI (tie chỉ EN)
    ("S104", "Dutton", "L", "repetition", "S101: Dutton", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    ("S104", "permanent and net migration", "L", "repetition", "S096–S097: permanent migration / net overseas migration", "high", None, "câu cắt phía VI", 1, None, None, "LC", None),
    # S105 — KHỐI CẮT VI (tie chỉ EN)
    ("S105", "I", "R", "personal", "S104: A spokesperson for Dutton", "high", None, "quote người phát ngôn; câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S105", "he", "R", "personal", "S104: Dutton", "high", None, "they số ít; câu cắt phía VI; occ 1 vì 'he could' là lần gặp 'he' đầu tiên trong câu (lần 2 nằm trong 'they')", 1, None, None, "LC", "A"),
    ("S105", "that", "R", "demonstrative", "S104: stating the Coalition's figures", "high", None, "câu cắt phía VI", 1, None, None, "LC", "A"),
    ("S105", "they", "R", "personal", "S104: A spokesperson for Dutton", "high", None, "they số ít; câu cắt phía VI", 1, None, None, "LC", "A"),
    # S106
    ("S106", "Australians", "L", "repetition", "S077: Australians", "high", None, None, 1, None, None, "LC", None),
    # S108
    ("S108", "the government", "L", "repetition", "S103: the government", "high", None, None, 1, None, None, "LC", None),
    ("S108", "cap the number of international student enrolments", "L", "repetition", "S018: capping international student enrolments", "high", None, None, 1, None, None, "LC", None),
    ("S108", "the sector", "L", "associative", "S022: international education providers", "med", None, None, 1, None, None, "LC", None),
    # S109
    ("S109", "It", "R", "personal", "S108: the plan to cap enrolments", "high", None, None, 1, None, None, "LC", "A"),
    ("S109", "education providers", "L", "repetition", "S022: international education providers", "high", None, None, 1, None, None, "LC", None),
    ("S109", "concerns", "L", "repetition", "S010: a concern", "med", None, None, 1, None, None, "LC", None),
    # S110 — 'however' nối 2 vế TRONG CÂU (Senate report ↔ government changed course): không lập hàng
    ("S110", "the government", "L", "repetition", "S108: the government", "high", None, None, 1, None, None, "LC", None),
    ("S110", "the Coalition", "L", "repetition", "S104: the Coalition", "high", None, "tiền trạm nằm ở câu bị cắt phía VI", 1, None, None, "LC", None),
    # S111
    ("S111", "ministerial direction 111", "L", "repetition", "S021: The new ministerial direction 111", "high", None, None, 1, None, None, "LC", None),
    ("S111", "this change", "R", "demonstrative", "S110: the government changed course", "high", None, None, 1, None, None, "LC", "A"),
    ("S111", "the current approach", "L", "synonym", "S021: ministerial direction 111", "high", None, None, 1, None, None, "LC", None),
    ("S111", "our", "R", "personal", "Úc/cơ quan giáo dục (ngoại văn bản — quote Clare)", "med", None, "'our ability'", 1, None, None, "LC", "E"),
    ("S111", "international students", "L", "repetition", "S108: international student enrolments", "high", None, None, 1, None, None, "LC", None),
    ("S111", "regional education providers", "L", "repetition", "S109: education providers", "high", None, None, 1, None, None, "LC", None),
    # S112
    ("S112", "inner-city unis", "L", "associative", "S025: smaller universities", "med", None, None, 1, None, None, "LC", None),
    ("S112", "international education", "L", "repetition", "S022: international education providers", "high", None, None, 1, None, None, "LC", None),
    # S113
    ("S113", "unis", "L", "repetition", "S112: inner-city unis", "high", None, None, 1, None, None, "LC", None),
    ("S113", "benefit", "L", "repetition", "S112: benefit from international education", "high", None, None, 1, None, None, "LC", None),
    ("S113", "too", "C", "additive", "S112: big inner-city unis benefit", "high", None, None, 1, None, None, "LC", None),
    ("S113", "this new approach", "R", "demonstrative", "S111: the current approach", "high", None, None, 1, None, None, "LC", "A"),
    ("S113", "us", "R", "personal", "Úc/chúng tôi (ngoại văn bản — quote Clare)", "med", None, None, 1, None, None, "LC", "E"),
    ("S113", "do that", "S", "verbal", "S113: should benefit too", "high", None, "[TC] do that ← benefit", 1, None, None, "TC", None),
    # S114
    ("S114", "Rizvi", "L", "repetition", "S088: Rizvi", "high", None, None, 1, None, None, "LC", None),
    ("S114", "this", "R", "demonstrative", "S111–S113: the new approach", "high", None, None, 1, None, None, "LC", "A"),
    # S115
    ("S115", "temporary graduates and students", "L", "repetition", "S038: Temporary Graduate + S001: international students", "high", None, None, 1, None, None, "LC", None),
    ("S115", "a pathway to permanent residence", "L", "associative", "S071–S072: live... permanently / permanent places", "med", None, "chuỗi 'permanent'", 1, None, None, "LC", None),
    ("S115", "one", "S", "nominal", "S115: a pathway to permanent residence", "high", None, "[TC] one ← a pathway", 1, None, None, "TC", None),
    ("S115", "places", "L", "repetition", "S012: places / S066: places", "high", None, None, 1, None, None, "LC", None),
    # S116
    ("S116", "That's", "R", "demonstrative", "S115: graduates won't get a pathway", "high", None, None, 1, None, None, "LC", "A"),
    # S117
    ("S117", "Watt", "L", "repetition", "S061: Watt", "high", None, None, 1, None, None, "LC", None),
    ("S117", "We'll", "R", "personal", "chúng ta chung (ngoại văn bản — quote Watt)", "med", None, None, 1, None, None, "LC", "E"),
    ("S117", "what happens", "L", "repetition", "S115: What happens to all those", "med", None, None, 1, None, None, "LC", None),
    # S118
    ("S118", "I", "R", "personal", "S117: Watt", "high", None, None, 1, None, None, "LC", "A"),
    ("S118", "it", "R", "personal", "S117: what happens", "med", None, None, 1, None, None, "LC", "A"),
]

TT = [
    # S002 (= ST S002)
    ("S002", "những thay đổi này", "R", "demonstrative", "S001: một loạt cải cách", "high", None, None, 1, None, None, "LC", "A"),
    # S003 (= ST S003)
    ("S003", "những thay đổi lớn", "L", "repetition", "S002: những thay đổi này", "high", None, None, 1, None, None, "LC", None),
    ("S003", "chính phủ", "L", "repetition", "S001: Chính phủ", "high", None, None, 1, None, None, "LC", None),
    # S004 (= ST S005; ST S004 bị cắt)
    ("S004", "chính quyền Albanese", "L", "repetition", "S003: chính phủ", "high", None, None, 1, None, None, "LC", None),
    # S005 (= ST S006)
    ("S005", "tính tạm thời vĩnh viễn", "L", "repetition", "S003: tính tạm thời vĩnh viễn", "high", None, None, 1, None, None, "LC", None),
    ("S005", "những thay đổi", "L", "repetition", "S002: những thay đổi này", "high", None, None, 1, None, None, "LC", None),
    ("S005", "tôi", "R", "personal", "S004: Ben Watt", "high", None, "đại từ ngôi 1 trong quote", 1, None, None, "LC", "A"),
    ("S005", "họ", "R", "personal", "S004: chính quyền Albanese", "high", None, None, 1, None, None, "LC", "A"),
    ("S005", "ông Watt", "L", "repetition", "S004: Ben Watt", "high", None, "thêm danh xưng 'ông'", 1, None, None, "LC", None),
    # S006 (= ST S007)
    ("S006", "Tính tạm thời vĩnh viễn", "L", "repetition", "S005: tính tạm thời vĩnh viễn", "high", None, None, 1, None, None, "LC", None),
    # S007 (= ST S008)
    ("S007", "Ông Watt", "L", "repetition", "S005: ông Watt", "high", None, None, 1, None, None, "LC", None),
    ("S007", "các cải cách", "L", "repetition", "S001: một loạt cải cách", "high", None, None, 1, None, None, "LC", None),
    ("S007", "hệ thống", "L", "repetition", "S003: hệ thống di trú", "med", None, "danh từ tổng quát", 1, None, None, "LC", None),
    # S008 (= ST S009)
    ("S008", "những cuộc thảo luận này", "R", "demonstrative", "S007: Watt lập luận", "high", None, None, 1, None, None, "LC", "A"),
    ("S008", "thị thực vĩnh viễn", "L", "associative", "S003: tính tạm thời vĩnh viễn", "med", None, "chuỗi 'vĩnh viễn'", 1, None, None, "LC", None),
    ("S008", "ông", "R", "personal", "S007: Ông Watt", "high", None, None, 1, None, None, "LC", "A"),
    # S009 (= ST S010)
    ("S009", "đây", "R", "demonstrative", "S008: số lượng thị thực vĩnh viễn vẫn giữ nguyên", "high", None, None, 1, None, None, "LC", "A"),
    # S011 (= ST S012)
    ("S011", "Chính phủ", "L", "repetition", "S004: chính quyền Albanese", "high", None, None, 1, None, None, "LC", None),
    ("S011", "chương trình di trú vĩnh viễn", "L", "associative", "S008: thị thực vĩnh viễn", "med", None, "chuỗi 'vĩnh viễn'", 1, None, None, "LC", None),
    # S012 (= ST S013)
    ("S012", "Chương trình", "L", "repetition", "S011: chương trình di trú vĩnh viễn", "high", None, None, 1, None, None, "LC", None),
    ("S012", "suất", "L", "repetition", "S011: 185.000 suất", "high", None, "occ=2: 132.200 suất + 137.100 suất", 2, None, None, "LC", None),
    ("S012", "di dân có tay nghề", "L", "repetition", "S001: di dân có tay nghề tạm thời", "high", None, None, 1, None, None, "LC", None),
    # S013 (= ST S014)
    ("S013", "được phân bổ", "L", "repetition", "S011–S012: phân bổ", "high", None, None, 1, None, None, "LC", None),
    # S014 (= ST S015)
    ("S014", "Chương trình trước", "R", "comparative", "S013: Business Innovation and Investment", "high", None, None, 1, None, None, "LC", "A"),
    ("S014", "chương trình sau", "R", "comparative", "S013: Global Talent", "high", None, None, 1, None, None, "LC", "A"),
    # S015 (= ST S016)
    ("S015", "Nhiều thay đổi", "L", "repetition", "S003/S005: những thay đổi", "high", None, None, 1, None, None, "LC", None),
    ("S015", "các cải cách", "L", "repetition", "S007: các cải cách", "high", None, None, 1, None, None, "LC", None),
    ("S015", "chương trình visa có tay nghề", "L", "associative", "S012: di dân có tay nghề", "med", None, "chuỗi 'tay nghề'", 1, None, None, "LC", None),
    # S017 (= ST S018)
    ("S017", "chính phủ", "L", "repetition", "S011: Chính phủ", "high", None, None, 1, None, None, "LC", None),
    ("S017", "sinh viên quốc tế", "L", "repetition", "S001: sinh viên quốc tế", "high", None, None, 1, None, None, "LC", None),
    # S018 (= ST S019)
    ("S018", "Nhưng", "C", "adversative", "S017: chính phủ đề xuất giới hạn", "high", None, None, 1, None, None, "LC", None),
    ("S018", "kế hoạch này", "R", "demonstrative", "S017: đề xuất giới hạn 270.000", "high", None, None, 1, None, None, "LC", "A"),
    ("S018", "chính phủ", "L", "repetition", "S017: chính phủ", "high", None, None, 1, None, None, "LC", None),
    # S019 (= ST S020)
    ("S019", "Chính phủ", "L", "repetition", "S018: chính phủ", "high", None, None, 1, None, None, "LC", None),
    ("S019", "sinh viên quốc tế", "L", "repetition", "S017: sinh viên quốc tế", "high", None, None, 1, None, None, "LC", None),
    # S020 (= ST S021)
    ("S020", "visa du học", "L", "associative", "S017: sinh viên quốc tế", "med", None, None, 1, None, None, "LC", None),
    ("S020", "giới hạn số lượng", "L", "repetition", "S017: giới hạn số lượng sinh viên", "high", None, None, 1, None, None, "LC", None),
    # S021 (= ST S022)
    ("S021", "các nhà cung cấp giáo dục quốc tế", "L", "associative", "S001/S017: sinh viên quốc tế / giáo dục", "med", None, None, 1, None, None, "LC", None),
    ("S021", "ưu tiên cao", "L", "repetition", "S020: ưu tiên cao", "high", None, None, 1, None, None, "LC", None),
    # S022 (= ST S023)
    ("S022", "họ", "R", "personal", "S021: các nhà cung cấp giáo dục quốc tế", "high", None, None, 1, None, None, "LC", "A"),
    ("S022", "ưu tiên tiêu chuẩn", "L", "repetition", "S020: ưu tiên tiêu chuẩn", "high", None, None, 1, None, None, "LC", None),
    # S023 (= ST S024)
    ("S023", "thay đổi này", "R", "demonstrative", "S019–S020: cách mới / chỉ thị 111", "high", None, None, 1, None, None, "LC", "A"),
    ("S023", "mức giới hạn", "L", "repetition", "S017: giới hạn", "high", None, None, 1, None, None, "LC", None),
    ("S023", "lựa chọn này", "R", "demonstrative", "S020: chỉ thị 111", "high", None, None, 1, None, None, "LC", "A"),
    ("S023", "chúng tôi", "R", "personal", "S019: Chính phủ (phía Bộ trưởng Burke)", "high", None, "quote Burke", 1, None, None, "LC", "A"),
    # S024 (= ST S025)
    ("S024", "Chương trình mới", "L", "synonym", "S020: chỉ thị mới 111", "high", None, None, 1, None, None, "LC", None),
    ("S024", "chỉ thị 107 của bộ trưởng", "L", "repetition", "S020: chỉ thị mới 111 của bộ trưởng", "high", None, "lặp khung 'chỉ thị của bộ trưởng'", 1, None, None, "LC", None),
    ("S024", "chính phủ", "L", "repetition", "S019: Chính phủ", "high", None, None, 1, None, None, "LC", None),
    ("S024", "số lượng sinh viên", "L", "repetition", "S019: số lượng sinh viên quốc tế", "high", None, None, 1, None, None, "LC", None),
    ("S024", "xử lý thị thực", "L", "repetition", "S020: xử lý visa du học", "high", None, None, 1, None, None, "LC", None),
    # S025 (= ST S026)
    ("S025", "thay đổi", "L", "repetition", "S015: Nhiều thay đổi", "high", None, None, 1, None, None, "LC", None),
    ("S025", "chương trình visa sinh viên", "L", "repetition", "S020: visa du học", "high", None, None, 1, None, None, "LC", None),
    # S026 (= ST S027; VI tách câu khác vị trí EN)
    ("S026", None, "E", "nominal", "S025: một số thay đổi khác", "high", None, "[LC] bao gồm ∅ — lược chủ ngữ {một số thay đổi khác} do tách câu khác EN", 1, "bao gồm ", "{một số thay đổi khác}", "LC", None),
    ("S026", "cải cách", "L", "repetition", "S007: các cải cách", "high", None, None, 1, None, None, "LC", None),
    ("S026", "visa sinh viên", "L", "repetition", "S025: chương trình visa sinh viên", "high", None, None, 1, None, None, "LC", None),
    ("S026", "visa tạm thời", "L", "associative", "S003: người được cấp thị thực + chuỗi 'tạm thời'", "med", None, None, 1, None, None, "LC", None),
    # S027 (= ST S028)
    ("S027", "visa tạm thời sau đại học", "L", "repetition", "S026: visa tạm thời", "high", None, None, 1, None, None, "LC", None),
    ("S027", "visa du học", "L", "repetition", "S026: visa sinh viên", "high", None, "đồng nghĩa visa sinh viên = visa du học", 1, None, None, "LC", None),
    # S028 (= ST S029)
    ("S028", "Danh sách đầy đủ", "L", "synonym", "S026: các hạn chế cấm nộp đơn", "med", None, "mô tả lại danh sách hạn chế", 1, None, None, "LC", None),
    # S029 (= ST S030)
    ("S029", "Việc chuyển đổi visa", "L", "synonym", "S006: nhảy thị thực", "high", None, "visa hopping = chuyển đổi visa", 1, None, None, "LC", None),
    ("S029", "tạm thời vĩnh viễn", "L", "repetition", "S005: tính tạm thời vĩnh viễn", "high", None, None, 1, None, None, "LC", None),
    ("S029", "cựu sinh viên quốc tế", "L", "repetition", "S017: sinh viên quốc tế", "high", None, None, 1, None, None, "LC", None),
    ("S029", "Bộ Nội vụ", "L", "repetition", "S028: Bộ Nội vụ", "high", None, None, 1, None, None, "LC", None),
    # S030 (= ST S031)
    ("S030", "Những thay đổi này", "R", "demonstrative", "S025–S026: một số thay đổi khác", "high", None, None, 1, None, None, "LC", "A"),
    ("S030", "lỗ hổng", "L", "synonym", "S029: việc chuyển đổi visa", "med", None, "mô tả lại visa hopping", 1, None, None, "LC", None),
    ("S030", "tình trạng này", "R", "demonstrative", "S029: việc chuyển đổi visa / tạm thời vĩnh viễn", "high", None, None, 1, None, None, "LC", "A"),
    # S031 (= ST S032)
    ("S031", "Cũng", "C", "additive", "S027: từ 1 tháng 7 các thay đổi", "high", None, None, 1, None, None, "LC", None),
    ("S031", "thị thực sinh viên quốc tế", "L", "repetition", "S025–S026: visa sinh viên / sinh viên quốc tế", "high", None, None, 1, None, None, "LC", None),
    # S032 (= ST S033)
    ("S032", "người nộp đơn xin visa sinh viên", "L", "repetition", "S026: nộp đơn xin visa sinh viên", "high", None, None, 1, None, None, "LC", None),
    # S033 (= ST S034)
    ("S033", "cũng", "C", "additive", "S031–S032: lệ phí và năng lực tài chính", "high", None, None, 1, None, None, "LC", None),
    ("S033", "yêu cầu", "L", "repetition", "S032: yêu cầu về năng lực tài chính", "high", None, None, 1, None, None, "LC", None),
    ("S033", "có hiệu lực", "L", "repetition", "S015: có hiệu lực", "high", None, None, 1, None, None, "LC", None),
    # S034 (= ST S035)
    ("S034", "Rizvi", "L", "repetition", "S009: Abul Rizvi", "high", None, None, 1, None, None, "LC", None),
    ("S034", "thay đổi", "L", "repetition", "S030: Những thay đổi này", "high", None, None, 1, None, None, "LC", None),
    ("S034", "chính sách visa sinh viên", "L", "repetition", "S025–S026: chương trình visa sinh viên", "high", None, None, 1, None, None, "LC", None),
    # S035 (= ST S036)
    ("S035", "số này", "R", "demonstrative", "S034: thay đổi về chính sách visa sinh viên", "high", None, "'trong số này'", 1, None, None, "LC", "A"),
    ("S035", "ông", "R", "personal", "S034: Rizvi", "high", None, None, 1, None, None, "LC", "A"),
    ("S035", "tỷ lệ nộp đơn", "L", "repetition", "S026: nộp đơn", "high", None, None, 1, None, None, "LC", None),
    # S037 (= ST S038)
    ("S037", "những thay đổi", "L", "repetition", "S034: thay đổi", "high", None, None, 1, None, None, "LC", None),
    ("S037", "có hiệu lực", "L", "repetition", "S033: có hiệu lực", "high", None, None, 1, None, None, "LC", None),
    ("S037", "visa tạm thời sau đại học", "L", "repetition", "S027: visa tạm thời sau đại học", "high", None, None, 1, None, None, "LC", None),
    ("S037", None, "E", "verbal", "S037: đã được rút ngắn", "high", None, "[TC] và ∅ áp dụng giới hạn độ tuổi mới — tỉnh lược {đã được}", 1, "đã được rút ngắn và ", "{đã được}", "TC", None),
    # S038 (= ST S039)
    ("S038", "Visa tạm thời sau đại học", "L", "repetition", "S037: visa tạm thời sau đại học (TGV)", "high", None, None, 1, None, None, "LC", None),
    ("S038", "loại", "L", "synonym", "S013: các dòng visa", "med", None, "streams: dòng ↔ loại", 1, None, None, "LC", None),
    # S039 (= ST S040)
    ("S039", "Giới hạn độ tuổi", "L", "repetition", "S037: giới hạn độ tuổi mới", "high", None, None, 1, None, None, "LC", None),
    # S040 (= ST S041; EN 'Those' → VI hiện thực hóa 'Những người')
    ("S040", "đủ điều kiện", "L", "repetition", "S032: đủ điều kiện", "high", None, None, 1, None, None, "LC", None),
    # S041 (= ST S042)
    ("S041", "Người sở hữu", "L", "repetition", "S037: người sở hữu visa", "high", None, None, 1, None, None, "LC", None),
    ("S041", "vẫn đủ điều kiện cho đến khi 50 tuổi", "L", "repetition", "S040: đủ điều kiện cho đến khi 50 tuổi", "high", None, None, 1, None, None, "LC", None),
    # S042 (= ST S043)
    ("S042", "Thời hạn lưu trú", "L", "repetition", "S037: thời hạn lưu trú", "high", None, None, 1, None, None, "LC", None),
    ("S042", "người giữ visa TGV", "L", "synonym", "S037: người sở hữu visa TGV", "high", None, "sở hữu ↔ giữ", 1, None, None, "LC", None),
    ("S042", "Post-Vocational Education Work", "L", "repetition", "S038: Post-Vocational Education Work", "high", None, None, 1, None, None, "LC", None),
    # S043 (= ST S044)
    ("S043", "Nhưng", "C", "adversative", "S042: thời hạn lưu trú không thay đổi", "high", None, None, 1, None, None, "LC", None),
    ("S043", "Post-Higher Education Work", "L", "repetition", "S038: Post-Higher Education", "high", None, None, 1, None, None, "LC", None),
    ("S043", "thời hạn lưu trú", "L", "repetition", "S042: Thời hạn lưu trú", "high", None, None, 1, None, None, "LC", None),
    # S044 (= ST S045)
    ("S044", "bằng thạc sĩ", "L", "repetition", "S040: chương trình thạc sĩ", "high", None, None, 1, None, None, "LC", None),
    ("S044", "thời gian lưu trú tối đa", "L", "synonym", "S042–S043: thời hạn lưu trú", "high", None, None, 1, None, None, "LC", None),
    ("S044", None, "E", "nominal", "S044: thời gian lưu trú tối đa là", "high", None, "[TC] hoặc tiến sĩ ∅ là ba năm — tỉnh lược {thời gian lưu trú tối đa}", 1, "hoặc tiến sĩ ", "{thời gian lưu trú tối đa}", "TC", None),
    # S046 (= ST S047)
    ("S046", "Watt", "L", "repetition", "S007: Ông Watt", "high", None, None, 1, None, None, "LC", None),
    ("S046", "thay đổi", "L", "repetition", "S034: thay đổi", "high", None, None, 1, None, None, "LC", None),
    ("S046", "nhà tuyển dụng tài trợ", "L", "repetition", "S012: nhà tuyển dụng bảo lãnh", "med", None, "bảo lãnh ↔ tài trợ (sponsor)", 1, None, None, "LC", None),
    # S047 (= ST S048)
    ("S047", "Visa mới", "L", "synonym", "S046: visa Kỹ năng theo nhu cầu (SID)", "high", None, None, 1, None, None, "LC", None),
    ("S047", "thay thế", "L", "repetition", "S014: đã được thay thế", "high", None, None, 1, None, None, "LC", None),
    ("S047", "nhà tuyển dụng tài trợ", "L", "repetition", "S046: nhà tuyển dụng tài trợ", "high", None, None, 1, None, None, "LC", None),
    ("S047", "đủ điều kiện", "L", "repetition", "S040–S041: đủ điều kiện", "high", None, None, 1, None, None, "LC", None),
    # S048 (= ST S049)
    ("S048", "dòng visa SID", "L", "repetition", "S013: các dòng visa + S046: SID", "high", None, None, 1, None, None, "LC", None),
    ("S048", "có hiệu lực", "L", "repetition", "S033/S037: có hiệu lực", "high", None, None, 1, None, None, "LC", None),
    # S049 (= ST S050)
    ("S049", "visa này", "R", "demonstrative", "S046–S047: visa SID", "high", None, None, 1, None, None, "LC", "A"),
    ("S049", "ở lại", "L", "synonym", "S042–S043: lưu trú", "high", None, "occ=2: ở lại Úc + ở lại tối đa", 2, None, None, "LC", None),
    ("S049", "người có hộ chiếu Hồng Kông", "L", "repetition", "S041: hộ chiếu... Hồng Kông", "high", None, None, 1, None, None, "LC", None),
    # S050 (= ST S051)
    ("S050", "Visa này", "R", "demonstrative", "S049: visa này", "high", None, None, 1, None, None, "LC", "A"),
    ("S050", "dòng", "L", "repetition", "S048: dòng visa SID", "high", None, "occ=2: ba dòng mục tiêu + một dòng hiện có", 2, None, None, "LC", None),
    ("S050", "di cư", "L", "repetition", "S012: di dân có tay nghề", "high", None, "di dân ↔ di cư", 1, None, None, "LC", None),
    ("S050", "thiếu hụt", "L", "repetition", "S047: Thiếu hụt kỹ năng tạm thời", "med", None, None, 1, None, None, "LC", None),
    # S051 (= ST S052)
    ("S051", "dòng visa kỹ năng cốt lõi", "L", "repetition", "S050: Kỹ năng cốt lõi", "high", None, None, 1, None, None, "LC", None),
    ("S051", "người đủ điều kiện", "L", "repetition", "S049: Những người đủ điều kiện", "high", None, None, 1, None, None, "LC", None),
    ("S051", "được tài trợ", "L", "repetition", "S046–S047: tài trợ", "high", None, None, 1, None, None, "LC", None),
    ("S051", "của chính phủ", "L", "repetition", "S019: Chính phủ", "high", None, None, 1, None, None, "LC", None),
    # S052 (= ST S053)
    ("S052", "Họ", "R", "personal", "S051: những người đủ điều kiện", "high", None, None, 1, None, None, "LC", "A"),
    ("S052", "kỹ năng cốt lõi", "L", "repetition", "S050–S051: kỹ năng cốt lõi", "high", None, None, 1, None, None, "LC", None),
    ("S052", "di cư có tay nghề tạm thời", "L", "repetition", "S001: di dân có tay nghề tạm thời", "high", None, None, 1, None, None, "LC", None),
    # S053 (= ST S054)
    ("S053", "người nộp đơn", "L", "repetition", "S026/S032: nộp đơn", "high", None, None, 1, None, None, "LC", None),
    ("S053", "dòng kỹ năng chuyên môn", "L", "repetition", "S050: Kỹ năng chuyên môn", "high", None, None, 1, None, None, "LC", None),
    ("S053", "phải đáp ứng Ngưỡng thu nhập", "L", "repetition", "S052: phải đáp ứng Ngưỡng thu nhập", "high", None, None, 1, None, None, "LC", None),
    ("S053", "nghề", "L", "repetition", "S051: một nghề", "high", None, "occ=2: nghề nào + nghề thủ công", 2, None, None, "LC", None),
    # S054 (= ST S055)
    ("S054", "Ngưỡng thu nhập", "L", "repetition", "S052–S053: Ngưỡng thu nhập", "high", None, None, 1, None, None, "LC", None),
    # S055 (= ST S056)
    ("S055", "Dòng Thỏa thuận lao động", "L", "repetition", "S050: thỏa thuận lao động", "high", None, None, 1, None, None, "LC", None),
    ("S055", "visa TSS", "L", "repetition", "S047: visa Thiếu hụt kỹ năng tạm thời (TSS)", "high", None, None, 1, None, None, "LC", None),
    ("S055", "thị thực SID", "L", "repetition", "S048: visa SID", "high", None, None, 1, None, None, "LC", None),
    ("S055", "Bộ Nội vụ", "L", "repetition", "S029: Bộ Nội vụ", "high", None, None, 1, None, None, "LC", None),
    # S057 (= ST S058)
    ("S057", "Cũng", "C", "additive", "S048: có hiệu lực tháng 12", "high", None, None, 1, None, None, "LC", None),
    ("S057", "visa Đổi mới Quốc gia", "L", "repetition", "S014: visa National Innovation", "high", None, None, 1, None, None, "LC", None),
    ("S057", "thay thế", "L", "repetition", "S047: thay thế", "high", None, None, 1, None, None, "LC", None),
    ("S057", "dòng visa Tài năng toàn cầu", "L", "repetition", "S013: Global Talent", "high", None, None, 1, None, None, "LC", None),
    ("S057", "visa thường trú", "L", "synonym", "S008/S011: vĩnh viễn", "med", None, "thường trú ≈ vĩnh viễn (permanent)", 1, None, None, "LC", None),
    # S058 (= ST S059)
    ("S058", "ứng viên", "L", "synonym", "S053: người nộp đơn", "med", None, None, 1, None, None, "LC", None),
    ("S058", "nộp đơn", "L", "repetition", "S026/S053: nộp đơn", "high", None, None, 1, None, None, "LC", None),
    ("S058", "Bộ Nội vụ", "L", "repetition", "S055: Bộ Nội vụ", "high", None, None, 1, None, None, "LC", None),
    # S059 (= ST S060)
    ("S059", "Tài năng toàn cầu", "L", "repetition", "S057: dòng visa Tài năng toàn cầu", "high", None, None, 1, None, None, "LC", None),
    ("S059", "đơn xin", "L", "repetition", "S058: nộp đơn", "high", None, None, 1, None, None, "LC", None),
    ("S059", "được xử lý", "L", "repetition", "S024: xử lý thị thực", "high", None, None, 1, None, None, "LC", None),
    ("S059", "ưu tiên", "L", "repetition", "S021–S022: ưu tiên cao/tiêu chuẩn", "high", None, None, 1, None, None, "LC", None),
    # S060 (= ST S061)
    ("S060", "Watt", "L", "repetition", "S046: Watt", "high", None, None, 1, None, None, "LC", None),
    ("S060", "thị thực mới", "L", "synonym", "S057: visa Đổi mới Quốc gia", "high", None, None, 1, None, None, "LC", None),
    ("S060", "thị thực trước đây", "R", "comparative", "S057: dòng visa Tài năng toàn cầu", "high", None, None, 1, None, None, "LC", "A"),
    # S061 (= ST S062)
    ("S061", "visa thường trú", "L", "repetition", "S057: visa thường trú", "high", None, None, 1, None, None, "LC", None),
    ("S061", "giống nhau", "R", "comparative", "S008: vẫn giữ nguyên", "high", None, None, 1, None, None, "LC", "A"),
    # S063 (= ST S064)
    ("S063", "Chính phủ", "L", "repetition", "S051: chính phủ", "high", None, None, 1, None, None, "LC", None),
    ("S063", "nộp đơn", "L", "repetition", "S058: nộp đơn", "high", None, None, 1, None, None, "LC", None),
    # S064 (= ST S065)
    ("S064", "đăng ký bỏ phiếu", "L", "repetition", "S063: quy trình bỏ phiếu trước khi nộp đơn", "high", None, None, 1, None, None, "LC", None),
    ("S064", "người nộp đơn", "L", "repetition", "S053/S058: nộp đơn", "high", None, None, 1, None, None, "LC", None),
    ("S064", "Làm việc và Kỳ nghỉ", "L", "synonym", "S063: Làm việc kỳ nghỉ - Working Holiday Maker", "high", None, None, 1, None, None, "LC", None),
    # S065 (= ST S066)
    ("S065", "Bộ", "L", "repetition", "S055/S058: Bộ Nội vụ", "high", None, None, 1, None, None, "LC", None),
    ("S065", "quy trình này", "R", "demonstrative", "S063: quy trình bỏ phiếu", "high", None, None, 1, None, None, "LC", "A"),
    ("S065", "người nộp đơn", "L", "repetition", "S064: người nộp đơn", "high", None, None, 1, None, None, "LC", None),
    ("S065", "chỗ trống", "L", "synonym", "S011: suất", "med", None, None, 1, None, None, "LC", None),
    # S066 (= ST S067)
    ("S066", "cuộc bỏ phiếu", "L", "repetition", "S064: đăng ký bỏ phiếu", "high", None, None, 1, None, None, "LC", None),
    ("S066", "cũng", "C", "additive", "S064: bỏ phiếu cho Work and Holiday", "high", None, None, 1, None, None, "LC", None),
    ("S066", "visa tạm thời mới", "L", "associative", "S026: visa tạm thời", "med", None, "chuỗi 'visa tạm thời'", 1, None, None, "LC", None),
    # S067 (= ST S068)
    ("S067", "Ấn Độ", "L", "repetition", "S064: Ấn Độ", "high", None, None, 1, None, None, "LC", None),
    ("S067", "đăng ký", "L", "repetition", "S064: đăng ký", "high", None, None, 1, None, None, "LC", None),
    # S068 (= ST S069)
    ("S068", "suất được phân bổ", "L", "repetition", "S011–S012: suất / phân bổ", "high", None, None, 1, None, None, "LC", None),
    # S069 (= ST S070)
    ("S069", "Vòng bỏ phiếu", "L", "repetition", "S066: cuộc bỏ phiếu", "high", None, None, 1, None, None, "LC", None),
    ("S069", "đăng ký", "L", "repetition", "S067: đăng ký", "high", None, None, 1, None, None, "LC", None),
    # S070 (= ST S071)
    ("S070", "Vòng bỏ phiếu đầu tiên", "L", "repetition", "S069: Vòng bỏ phiếu đầu tiên", "high", None, "nguồn: hai 'vòng đầu tiên' (MATES và PEV)", 1, None, None, "LC", None),
    ("S070", "sinh sống và làm việc tại Úc", "L", "repetition", "S066: sống và làm việc tại Úc", "high", None, None, 1, None, None, "LC", None),
    ("S070", "người di cư", "L", "repetition", "S050: di cư", "high", None, None, 1, None, None, "LC", None),
    ("S070", "vĩnh viễn", "L", "repetition", "S011: di trú vĩnh viễn", "high", None, None, 1, None, None, "LC", None),
    # S071 (= ST S072)
    ("S071", "Thái Bình Dương", "L", "repetition", "S070: các nước Thái Bình Dương", "high", None, None, 1, None, None, "LC", None),
    ("S071", "suất thường trú", "L", "repetition", "S057: visa thường trú + S068: suất", "high", None, None, 1, None, None, "LC", None),
    ("S071", "chương trình di cư vĩnh viễn", "L", "repetition", "S011: chương trình di trú vĩnh viễn", "high", None, "di trú ↔ di cư", 1, None, None, "LC", None),
    # S072 (= ST S073)
    ("S072", "PEV", "L", "repetition", "S071: (PEV, loại phụ 192)", "high", None, None, 1, None, None, "LC", None),
    ("S072", "lá phiếu", "L", "synonym", "S063–S066: bỏ phiếu", "high", None, None, 1, None, None, "LC", None),
    # S074 (= ST S075)
    ("S074", "Chính phủ", "L", "repetition", "S063: Chính phủ", "high", None, None, 1, None, None, "LC", None),
    ("S074", "mức độ di trú", "L", "repetition", "S003: hệ thống di trú", "high", None, None, 1, None, None, "LC", None),
    # S075 (= ST S076)
    ("S075", "Đại dịch", "L", "repetition", "S074: trước đại dịch", "high", None, None, 1, None, None, "LC", None),
    ("S075", "mức độ di trú", "L", "repetition", "S074: mức độ di trú", "high", None, None, 1, None, None, "LC", None),
    # S076 (= ST S077)
    ("S076", "NOM", "L", "repetition", "S075: NOM", "high", None, None, 1, None, None, "LC", None),
    ("S076", "người di cư", "L", "repetition", "S070: người di cư", "high", None, None, 1, None, None, "LC", None),
    # S077 (= ST S078)
    ("S077", "biên giới", "L", "repetition", "S075: đóng cửa biên giới", "high", None, None, 1, None, None, "LC", None),
    ("S077", "di dân tạm thời và thường trú", "L", "repetition", "S070: người di cư + chuỗi tạm thời/thường trú", "high", None, None, 1, None, None, "LC", None),
    # S078 (= ST S079)
    ("S078", "người di cư ròng", "L", "repetition", "S075: di cư ròng ra nước ngoài", "high", None, None, 1, None, None, "LC", None),
    # S079 (= ST S080)
    ("S079", "Điều đó", "R", "demonstrative", "S078: vượt quá nửa triệu", "high", None, None, 1, None, None, "LC", "A"),
    # S080 (= ST S081)
    ("S080", "Nhưng", "C", "adversative", "S078–S079: con số chưa từng có", "high", None, None, 1, None, None, "LC", None),
    ("S080", "mức độ di cư", "L", "repetition", "S074–S075: mức độ di trú/di cư", "high", None, None, 1, None, None, "LC", None),
    ("S080", "mức trước đó", "R", "comparative", "S074: gần mức trước đại dịch", "high", None, None, 1, None, None, "LC", "A"),
    ("S080", "bạn", "R", "personal", "người đọc chung (ngoại văn bản — quote McDonald)", "med", None, "'bạn' phiếm chỉ trong quote", 1, None, None, "LC", "E"),
    # S081 (= ST S082; EN 'It' → VI lược chủ ngữ)
    ("S081", None, "E", "nominal", "S080: mức độ di cư", "high", None, "[LC] ∅ Chỉ là rất thấp — lược chủ ngữ câu đầu, hồi phục {mức độ di cư}; EN dùng 'It'", 1, "", "{mức độ di cư}", "LC", None),
    # S082 (= ST S083)
    ("S082", "Vấn đề", "L", "synonym", "S079: hoảng loạn", "med", None, "mô tả lại tình trạng", 1, None, None, "LC", None),
    ("S082", "chính phủ", "L", "repetition", "S074: Chính phủ", "high", None, "'dự báo của chính phủ'", 1, None, None, "LC", None),
    # S083 (= ST S084)
    ("S083", "NOM", "L", "repetition", "S076: NOM", "high", None, None, 1, None, None, "LC", None),
    # S084 (= ST S085)
    ("S084", "Con số này", "R", "demonstrative", "S083: 446.000 người", "high", None, None, 1, None, None, "LC", "A"),
    ("S084", "dự báo của chính phủ", "L", "repetition", "S082: dự báo của chính phủ", "high", None, None, 1, None, None, "LC", None),
    # S085 (= ST S086)
    ("S085", "Đây", "R", "demonstrative", "S083: NOM giảm xuống 446.000", "high", None, None, 1, None, None, "LC", "A"),
    ("S085", "biên giới", "L", "repetition", "S077: biên giới", "high", None, None, 1, None, None, "LC", None),
    # S086 (= ST S087)
    ("S086", "Lượng người di cư đến", "L", "repetition", "S077: lượng người đến", "high", None, None, 1, None, None, "LC", None),
    ("S086", "lượng người rời đi", "L", "repetition", "S082: ít người rời khỏi Úc", "high", None, None, 1, None, None, "LC", None),
    # S087 (= ST S088)
    ("S087", "Rizvi", "L", "repetition", "S034: Rizvi", "high", None, None, 1, None, None, "LC", None),
    ("S087", "sự sụt giảm này", "R", "demonstrative", "S086: di cư đến giảm 10%", "high", None, None, 1, None, None, "LC", "A"),
    ("S087", "chính phủ", "L", "repetition", "S082: chính phủ", "high", None, None, 1, None, None, "LC", None),
    ("S087", "thay đổi", "L", "repetition", "S034/S037: thay đổi", "high", None, None, 1, None, None, "LC", None),
    # S088 (= ST S089)
    ("S088", "Chính phủ", "L", "repetition", "S087: chính phủ", "high", None, None, 1, None, None, "LC", None),
    ("S088", "NOM", "L", "repetition", "S083: NOM", "high", None, None, 1, None, None, "LC", None),
    ("S088", "dự kiến", "L", "synonym", "S082/S084: dự báo", "high", None, None, 1, None, None, "LC", None),
    # S089 (= ST S090)
    ("S089", "của chính phủ", "L", "repetition", "S088: Chính phủ", "high", None, "EN dùng 'Its' (R sở hữu)", 1, None, None, "LC", None),
    ("S089", "con số này", "R", "demonstrative", "S088: 260.000", "high", None, None, 1, None, None, "LC", "A"),
    ("S089", "điều chỉnh", "L", "synonym", "S084: dự báo đã sửa đổi", "med", None, "sửa đổi ↔ điều chỉnh (revised)", 1, None, None, "LC", None),
    # S090 (= ST S091)
    ("S090", "Dự báo", "L", "repetition", "S084: dự báo", "high", None, None, 1, None, None, "LC", None),
    # S091 (= ST S092)
    ("S091", "Con số này", "R", "demonstrative", "S089: 340.000", "high", None, "quote McDonald", 1, None, None, "LC", "A"),
    ("S091", None, "E", "nominal", "S091: Con số này", "high", None, "[TC] nhưng ∅ đang giảm xuống — lược chủ ngữ {con số này}", 1, "nhưng ", "{con số này}", "TC", None),
    # S092 (= ST S093)
    ("S092", "Và", "C", "additive", "S091: đang giảm xuống", "high", None, None, 1, None, None, "LC", None),
    ("S092", "chúng ta", "R", "personal", "nước Úc/chúng ta chung (ngoại văn bản — quote McDonald)", "med", None, None, 1, None, None, "LC", "E"),
    ("S092", "con số này", "R", "demonstrative", "S089: 340.000", "high", None, None, 1, None, None, "LC", "A"),
    ("S092", "hoảng sợ", "L", "repetition", "S079: hoảng loạn", "high", None, None, 1, None, None, "LC", None),
    ("S092", "số lượng người rời đi", "L", "repetition", "S086: lượng người rời đi", "high", None, None, 1, None, None, "LC", None),
    # S093 (= ST S094)
    ("S093", "chúng ta", "R", "personal", "nước Úc/chúng ta chung (ngoại văn bản — quote McDonald)", "med", None, None, 1, None, None, "LC", "E"),
    ("S093", "trở lại bình thường", "L", "synonym", "S074: gần mức trước đại dịch", "med", None, "bình thường ≈ mức trước đại dịch", 1, None, None, "LC", None),
    ("S093", "McDonald", "L", "repetition", "S079: Peter McDonald", "high", None, None, 1, None, None, "LC", None),
    ("S093", "MYEFO", "L", "repetition", "S089: (MYEFO)", "high", None, None, 1, None, None, "LC", None),
    # S095 (= ST S096)
    ("S095", "Peter Dutton", "L", "repetition", "S023: Peter Dutton", "high", None, None, 1, None, None, "LC", None),
    ("S095", "lượng di cư vĩnh viễn", "L", "repetition", "S071: chương trình di cư vĩnh viễn", "high", None, None, 1, None, None, "LC", None),
    # S096 (= ST S097)
    ("S096", "ông", "R", "personal", "S095: Peter Dutton", "high", None, None, 1, None, None, "LC", "A"),
    ("S096", "cũng", "C", "additive", "S095: cam kết cắt giảm di cư vĩnh viễn", "high", None, None, 1, None, None, "LC", None),
    ("S096", "cam kết", "L", "repetition", "S095: cam kết", "high", None, None, 1, None, None, "LC", None),
    ("S096", "di cư ròng ra nước ngoài", "L", "repetition", "S075: di cư ròng ra nước ngoài", "high", None, None, 1, None, None, "LC", None),
    # S097 (= ST S098)
    ("S097", "Dutton", "L", "repetition", "S095: Peter Dutton", "high", None, None, 1, None, None, "LC", None),
    ("S097", "NOM", "L", "repetition", "S096: di cư ròng ra nước ngoài / S076: NOM", "high", None, None, 1, None, None, "LC", None),
    # S098 (= ST S100; ST S099 bị cắt)
    ("S098", "chúng tôi", "R", "personal", "phe Dutton/Liên đảng (ngoại văn bản — quote)", "med", None, "occ=2: chúng tôi đã nói + chúng tôi muốn", 2, None, None, "LC", "E"),
    # S099 (= ST S101)
    ("S099", "Và", "C", "additive", "S098: lượng di cư giảm xuống", "high", None, None, 1, None, None, "LC", None),
    ("S099", "chúng tôi", "R", "personal", "phe Dutton/Liên đảng (ngoại văn bản — quote)", "med", None, None, 1, None, None, "LC", "E"),
    ("S099", "số lượng người đến", "L", "repetition", "S077: lượng người đến", "high", None, None, 1, None, None, "LC", None),
    ("S099", "Dutton cho biết", "L", "repetition", "S097: Dutton", "high", None, None, 1, None, None, "LC", None),
    # S100 (= ST S102)
    ("S100", "Đó", "R", "demonstrative", "S099: đưa số lượng về mức trung bình", "high", None, None, 1, None, None, "LC", "A"),
    ("S100", "chúng ta", "R", "personal", "nước Úc (ngoại văn bản — quote Dutton)", "med", None, "'đất nước chúng ta' — inclusive, khác 'chúng tôi'", 1, None, None, "LC", "E"),
    # S101 (= ST S103)
    ("S101", "Một lần nữa", "C", "additive", "S098–S100: các cam kết", "high", None, "khẳng định lại", 1, None, None, "LC", None),
    ("S101", "chúng ta", "R", "personal", "phe Dutton (ngoại văn bản — quote; EN 'we' → VI 'chúng ta')", "med", None, "occ=4: xem xét, đã nói, vào chính phủ, cần phải làm", 4, None, None, "LC", "E"),
    ("S101", "chính phủ", "L", "repetition", "S088: Chính phủ", "high", None, "'khi chúng ta vào chính phủ'", 1, None, None, "LC", None),
    # S102 (= ST S106; ST S104–S105 bị cắt)
    ("S102", "Người dân Úc", "L", "repetition", "S076: người Úc", "med", None, None, 1, None, None, "LC", None),
    # S104 (= ST S108)
    ("S104", "chính phủ", "L", "repetition", "S101: chính phủ", "high", None, None, 1, None, None, "LC", None),
    ("S104", "kế hoạch hạn chế số lượng sinh viên quốc tế đăng ký", "L", "repetition", "S017: giới hạn số lượng sinh viên quốc tế đăng ký", "high", None, None, 1, None, None, "LC", None),
    ("S104", "lĩnh vực này", "R", "demonstrative", "S021: các nhà cung cấp giáo dục quốc tế", "med", None, None, 1, None, None, "LC", "A"),
    # S105 (= ST S109)
    ("S105", "Điều này", "R", "demonstrative", "S104: kế hoạch hạn chế", "high", None, None, 1, None, None, "LC", "A"),
    ("S105", "nhà cung cấp giáo dục", "L", "repetition", "S021: các nhà cung cấp giáo dục quốc tế", "high", None, None, 1, None, None, "LC", None),
    ("S105", "mối lo ngại", "L", "synonym", "S009: mối quan tâm", "med", None, None, 1, None, None, "LC", None),
    # S106 — 'tuy nhiên' nối 2 vế TRONG CÂU: không lập hàng
    ("S106", "chính phủ", "L", "repetition", "S104: chính phủ", "high", None, None, 1, None, None, "LC", None),
    # S107 (= ST S111)
    ("S107", "chỉ thị của bộ trưởng 111", "L", "repetition", "S020: chỉ thị mới 111 / S024: chỉ thị 107", "high", None, None, 1, None, None, "LC", None),
    ("S107", "sự thay đổi này", "R", "demonstrative", "S106: chính phủ thay đổi hướng đi", "high", None, None, 1, None, None, "LC", "A"),
    ("S107", "cách tiếp cận hiện tại", "L", "synonym", "S020: chỉ thị mới 111", "high", None, None, 1, None, None, "LC", None),
    ("S107", "sinh viên quốc tế", "L", "repetition", "S104: sinh viên quốc tế", "high", None, None, 1, None, None, "LC", None),
    ("S107", "các nhà cung cấp giáo dục khu vực", "L", "repetition", "S105: nhà cung cấp giáo dục", "high", None, None, 1, None, None, "LC", None),
    # S108 (= ST S112)
    ("S108", "các trường đại học lớn trong thành phố", "L", "associative", "S024: các trường đại học nhỏ hơn", "med", None, None, 1, None, None, "LC", None),
    ("S108", "giáo dục quốc tế", "L", "repetition", "S021: giáo dục quốc tế", "high", None, None, 1, None, None, "LC", None),
    # S109 (= ST S113)
    ("S109", "trường đại học khu vực và ngoại ô", "L", "repetition", "S108: các trường đại học lớn trong thành phố", "high", None, None, 1, None, None, "LC", None),
    ("S109", "được hưởng lợi", "L", "repetition", "S108: được hưởng lợi", "high", None, None, 1, None, None, "LC", None),
    ("S109", "cũng", "C", "additive", "S108: trường đại học lớn được hưởng lợi", "high", None, None, 1, None, None, "LC", None),
    ("S109", "cách tiếp cận mới này", "R", "demonstrative", "S107: cách tiếp cận hiện tại", "high", None, None, 1, None, None, "LC", "A"),
    ("S109", "chúng tôi", "R", "personal", "Úc/cơ quan giáo dục (ngoại văn bản — quote Clare)", "med", None, None, 1, None, None, "LC", "E"),
    ("S109", "điều đó", "S", "verbal", "S109: được hưởng lợi", "high", None, "[TC] thực hiện được điều đó ← được hưởng lợi", 1, None, None, "TC", None),
    # S110 (= ST S114)
    ("S110", "Rizvi", "L", "repetition", "S087: Rizvi", "high", None, None, 1, None, None, "LC", None),
    # S111 (= ST S115)
    ("S111", "những sinh viên tốt nghiệp tạm thời", "L", "repetition", "S037: visa tạm thời sau đại học + sinh viên", "high", None, None, 1, None, None, "LC", None),
    ("S111", "con đường trở thành thường trú nhân", "L", "associative", "S057/S071: thường trú", "med", None, "chuỗi 'thường trú'", 1, None, None, "LC", None),
    ("S111", None, "E", "nominal", "S111: con đường trở thành thường trú nhân", "high", None, "[TC] không có được ∅ — lược tân ngữ {con đường trở thành thường trú nhân}; EN dùng 'one'", 1, "không có được ", "{con đường trở thành thường trú nhân}", "TC", None),
    ("S111", "chỗ", "L", "synonym", "S065: chỗ trống / S011: suất", "med", None, None, 1, None, None, "LC", None),
    # S112 (= ST S116)
    ("S112", "Điều đó", "R", "demonstrative", "S111: không đủ chỗ cho sinh viên tốt nghiệp", "high", None, None, 1, None, None, "LC", "A"),
    # S113 (= ST S117)
    ("S113", "Watt", "L", "repetition", "S060: Watt", "high", None, None, 1, None, None, "LC", None),
    ("S113", "Chúng ta", "R", "personal", "chúng ta chung (ngoại văn bản — quote Watt)", "med", None, None, 1, None, None, "LC", "E"),
    ("S113", "điều gì sẽ xảy ra", "L", "repetition", "S111: Điều gì sẽ xảy ra", "med", None, None, 1, None, None, "LC", None),
    # S114 (= ST S118)
    ("S114", "Tôi", "R", "personal", "S113: Watt", "high", None, None, 1, None, None, "LC", "A"),
]
