# P37 tie table — WRITTEN BY HAND FROM work/analysis/P37_semantic.md.
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
# Text/gap_after là chuỗi con nguyên văn trong câu (kiểm bằng pipeline.locate).
# KHỐI CẮT VI: EN S025 (quote "no win") + EN S036–S038 (khối Hardesty)
# → tie chỉ phía EN; cụm "and bought at a WalMart" (S011) bị VI cắt.

ST = [
    # S002
    ("S002", "these microscopic plastic pieces", "R", "demonstrative",
     "S001: invisible pieces of ever so tiny nanoplastics", "high", None,
     "hậu chỉ từ + miêu tả lại; đồng thời lặp 'pieces' trong cụm, ghi note; "
     "'they/their' trong câu không đánh", 1, None, None, "LC", "A"),
    # S003
    ("S003", "researchers", "L", "repetition",
     "S002: researchers at Columbia and Rutgers universities", "high",
     None, None, 1, None, None, "LC", None),
    ("S003", "bottled water", "L", "repetition",
     "S001: The average liter of bottled water", "high", None,
     "trong 'bottled water brands'", 1, None, None, "LC", None),
    ("S003", "per liter", "L", "repetition", "S001: The average liter",
     "high", None, "đơn vị lặp", 1, None, None, "LC", None),
    # [Phase-2] particle ← S002 pieces: đồng nghĩa pieces ≈ particles (H&H
    # §6.2 reiteration; TNT §31 phép thế đẳng nghĩa) — mắt xích được S004
    # (These/particles) cite làm tiền trạm nhưng chưa có hàng (nhóm 12).
    ("S003", "particle", "L", "synonym",
     "S002: these microscopic plastic pieces", "med", None,
     "pieces ≈ particles (particle levels); mở chuỗi 'particles'", 1, None,
     None, "LC", None),
    # S004
    ("S004", "These", "R", "demonstrative",
     "S003: particle levels ranged from 110,000 to 400,000", "high", None,
     "chỉ về các hạt đo được", 1, None, None, "LC", "A"),
    ("S004", "particles", "L", "repetition", "S003: particle levels",
     "high", None, None, 1, None, None, "LC", None),
    # S005
    ("S005", "microns", "L", "repetition", "S004: less than a micron",
     "high", None,
     "'micrometers' trong câu là đổi tên trong câu (TC), không đánh; 'it' "
     "trong câu không đánh", 1, None, None, "LC", None),
    # S006
    ("S006", "microns", "L", "repetition", "S005: 25,400 microns",
     "high", None, None, 1, None, None, "LC", None),
    # S007
    ("S007", "Previous studies", "L", "repetition", "S003: a study",
     "high", None, "mở chuỗi 'studies'", 1, None, None, "LC", None),
    # [Phase-2] bigger: quy chiếu so sánh (H&H §2.5) — chuẩn so sánh là
    # hạt nano < 1 micron tả ở câu trước (S004) → [LC]; VI đối ứng "hơn".
    ("S007", "bigger", "R", "comparative",
     "S004: particles that are less than a micron in size", "med", None,
     "[LC] 'slightly bigger' = lớn hơn hạt nano đã tả ở S004; H&H §2.5 "
     "comparative (tính từ so sánh có chuẩn trong văn bản)", 1, None, None,
     "LC", "A"),
    # [Phase-2] tái phân loại sub collocation → antonym: micro ↔ nano là cặp
    # đối nghĩa kích thước qua câu (TNT §30 phép đối; H&H §6.4 opposites).
    ("S007", "microplastics", "L", "antonym",
     "S001: nanoplastics", "med", None,
     "phép đối micro ↔ nano (đối lập kích thước, TNT §30; H&H §6.4 "
     "opposites); 'micron' trong câu có hàng riêng", 1, None, None, "LC",
     None),
    ("S007", "micron", "L", "repetition", "S006: 83 microns", "high",
     None, "to one micron", 1, None, None, "LC", None),
    # S008
    # [Phase-2] sửa ante theo tiền trạm gần nhất (nhóm 4): nhắc gần nhất
    # của 'nanoplastics' là S001, không phải S007 microplastics (TNT §26).
    ("S008", "nanoplastics", "L", "repetition",
     "S001: ever so tiny nanoplastics", "high", None,
     "lặp nanoplastics (chuỗi từ S001)", 1, None, None, "LC", None),
    ("S008", "microplastics", "L", "repetition", "S007: microplastics",
     "high", None, None, 1, None, None, "LC", None),
    ("S008", "bottled water", "L", "repetition",
     "S003: three common bottled water brands", "high", None, None, 1,
     None, None, "LC", None),
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S008", "the study", "L", "repetition", "S003: a study", "high",
     "R: the", "mạo từ xác định — nghiên cứu đã được nhận diện", 1, None,
     None, "LC", None),
    # S009
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S009", "the plastic", "L", "repetition",
     "S008: nanoplastics than microplastics", "high", "R: the",
     "hình vị 'plastic' trong nanoplastics/microplastics", 1, None, None,
     "LC", None),
    ("S009", "the bottle", "L", "repetition",
     "S008: bottled water", "high", None, "bottled → bottle", 1, None,
     None, "LC", None),
    ("S009", "study", "L", "repetition", "S008: the study", "high",
     None, "study lead author", 1, None, None, "LC", None),
    ("S009", "Columbia", "L", "repetition",
     "S002: Columbia and Rutgers universities", "high", None,
     "a Columbia physical chemist", 1, None, None, "LC", None),
    # S010
    ("S010", "She", "R", "personal", "S009: Naixin Qian", "high", None,
     None, 1, None, None, "LC", "A"),
    ("S010", "the three brands", "R", "nominal",
     "S003: three common bottled water brands", "high", None,
     "danh ngữ xác định hồi quy; 'a brand/more brands' lần 2,3 trong câu "
     "không đánh; VI 'ba thương hiệu' không có tín hiệu quy chiếu", 1,
     None, None, "LC", "A"),
    ("S010", "researchers", "L", "repetition", "S003: researchers",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] more (occ 1, "more samples"): quy chiếu so sánh (H&H §2.5)
    # — chuẩn so sánh là 5 mẫu mỗi nhãn hiệu ở S003, câu trước → [LC];
    # "more brands" (occ 2) so với "the three brands" trong cùng câu →
    # [TC] không đánh (ghi §4.3 analysis).
    ("S010", "more", "R", "comparative",
     "S003: five samples each of three common bottled water brands", "med",
     None,
     "[LC] more samples = nhiều hơn 5 mẫu đã xem xét (S003); H&H §2.5 "
     "comparative; 'more brands' trong câu → [TC]", 1, None, None, "LC",
     "A"),
    # [Phase-2] samples ← S003 five samples: chuỗi 'samples' bị sót (H&H
    # §6.2 reiteration; TNT §26 phép lặp).
    ("S010", "samples", "L", "repetition",
     "S003: five samples each of three common bottled water brands",
     "high", None, "lặp samples (want more samples)", 1, None, None,
     "LC", None),
    ("S010", "study", "L", "repetition", "S009: study lead author",
     "med", None, "danh từ → động từ cùng hình vị", 1, None, None,
     "LC", None),
    # S011
    ("S011", "Still", "C", "adversative",
     "S010: She wouldn't reveal the three brands", "high", None,
     "nối nhượng bộ liên câu; VI 'Tuy nhiên' đối xứng", 1, None, None,
     "LC", None),
    ("S011", "she", "R", "personal", "S010: She (Qian)", "high", None,
     None, 1, None, None, "LC", "A"),
    ("S011", "they", "R", "personal", "S010: the three brands",
     "high", None, None, 1, None, None, "LC", "A"),
    ("S011", "common", "L", "repetition",
     "S003: three common bottled water brands", "high", None,
     "cụm 'bought at a WalMart' bị VI cắt, không tạo tie", 1, None,
     None, "LC", None),
    # S012
    ("S012", "Researchers", "L", "repetition", "S010: researchers",
     "high", None,
     "'still' là trạng từ thời gian (vẫn chưa), không phải nối", 1,
     None, None, "LC", None),
    ("S012", "those nanoplastic pieces", "R", "demonstrative",
     "S001: pieces of ever so tiny nanoplastics", "high", None,
     "hậu chỉ từ + lặp hình vị 'nanoplastic' trong cụm, ghi note", 1,
     None, None, "LC", "A"),
    # S013
    ("S013", "That", "R", "demonstrative",
     "S012: the big question — harmful to health?", "high", None,
     "đối ứng VI 'Điều đó'", 1, None, None, "LC", "A"),
    # S014
    ("S014", "We", "R", "personal",
     "giới nghiên cứu (ngoại văn bản — quote Stapleton)", "med", None,
     "ngoại quy chiếu", 1, None, None, "LC", "E"),
    ("S014", "it", "R", "personal",
     "S012: are those nanoplastic pieces harmful to health", "med",
     None, "it = vấn đề nhựa nano gây hại; 'dangerous' lần 2 trong câu "
     "(TC) không đánh; lần 1 có hàng [Phase-2] ← S012 harmful", 1, None,
     None, "LC", "A"),
    # [Phase-2] don't know ← S002 never knew: chuỗi 'know' (H&H §6.2; TNT
    # §26 phép lặp, liên kết bắc cầu TNT §8) — mắt xích được hàng "do know"
    # (S015) cite làm tiền trạm (nhóm 12).
    ("S014", "don’t know", "L", "repetition",
     "S002: they never knew how many or what kind", "med", None,
     "lặp know (cùng phủ định); bắc cầu xa (TNT §8)", 1, None, None,
     "LC", None),
    # [Phase-2] dangerous (occ 1) ← S012 harmful: đồng nghĩa (H&H §6.2) —
    # mắt xích được S027 "The danger" cite làm tiền trạm (nhóm 12).
    ("S014", "dangerous", "L", "synonym",
     "S012: Are those nanoplastic pieces harmful to health", "high",
     None,
     "dangerous ≈ harmful; lần 2 trong câu (TC) không đánh", 1, None,
     None, "LC", None),
    ("S014", "study", "L", "repetition", "S010: study", "high", None,
     "study co-author", 1, None, None, "LC", None),
    # [Phase-2] co-author ← S009 lead author: lặp hình vị author (H&H §6.2;
    # TNT §26) — mắt xích được S021 co-authors cite (nhóm 12).
    ("S014", "co-author", "L", "repetition",
     "S009: study lead author Naixin Qian", "med", None,
     "lặp hình vị author (lead author → co-author, đổi vai)", 1, None,
     None, "LC", None),
    ("S014", "Rutgers", "L", "repetition",
     "S002: Columbia and Rutgers universities", "high", None, None, 1,
     None, None, "LC", None),
    # S015
    ("S015", "We", "R", "personal",
     "giới nghiên cứu (ngoại văn bản — quote Stapleton)", "med", None,
     "câu mới trong cùng quote nên đánh dấu", 1, None, None, "LC", "E"),
    # [Phase-2] do know ↔ don't know (S014): phép đối phủ định–khẳng định
    # qua câu (TNT §30; H&H §6.4 opposites) — "We don't know X; we do
    # know Y"; VI đối ứng biết ↔ không biết.
    ("S015", "do know", "L", "antonym",
     "S014: We don't know if it's dangerous", "high", None,
     "phép đối do know ↔ don't know (không biết ↔ biết)", 1, None, None,
     "LC", None),
    ("S015", "they", "R", "personal",
     "S012: those nanoplastic pieces", "high", None,
     "occ 1: lần 2 ('they're doing') trong câu cùng chuỗi, không đánh",
     1, None, None, "LC", "A"),
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S015", "the current research", "L", "synonym",
     "S008: the study", "high", "R: the", "research ≈ study", 1, None,
     None, "LC", None),
    ("S015", "people", "L", "synonym", "S006: A human hair", "med",
     None, "human ↔ people (đồng nghĩa); VI 'con người' lặp nguyên từ",
     1, None, None, "LC", None),
    # S016
    ("S016", "Bottled Water", "L", "repetition",
     "S008: bottled water", "high", None,
     "tên tổ chức chứa chuỗi 'bottled water'", 1, None, None, "LC",
     None),
    ("S016", "nano-", "L", "repetition", "S012: those nanoplastic pieces",
     "high", None, "dấu gạch nối treo của nguồn, giữ nguyên văn", 1,
     None, None, "LC", None),
    ("S016", "microplastic", "L", "repetition", "S008: microplastics",
     "high", None, None, 1, None, None, "LC", None),
    ("S016", "particles", "L", "repetition", "S004: particles", "high",
     None, None, 1, None, None, "LC", None),
    ("S016", "health", "L", "repetition",
     "S012: harmful to health", "high", None, None, 1, None, None,
     "LC", None),
    # S017
    ("S017", "Therefore", "C", "causal",
     "S016: lack of standardized methods and consensus", "high", None,
     None, 1, None, None, "LC", None),
    ("S017", "these particles", "R", "demonstrative",
     "S016: nano- and microplastic particles", "high", None, None, 1,
     None, None, "LC", "A"),
    ("S017", "drinking water", "L", "superordinate",
     "S008: bottled water", "med", None,
     "nước uống ⊃ nước đóng chai (trường nước)", 1, None, None, "LC",
     None),
    # S018
    ("S018", "plastics", "L", "repetition", "S016: microplastic",
     "high", None, "plastics manufacturers", 1, None, None, "LC",
     None),
    # S019
    ("S019", "world", "L", "repetition", "S018: The American Chemistry "
     "Council — ngữ cảnh toàn cầu", "med", None,
     "occ 1: lần 2 ('the world's oceans') trong câu cùng chuỗi, không "
     "đánh", 1, None, None, "LC", None),
    ("S019", "plastic", "L", "repetition", "S018: plastics", "high",
     None,
     "occ 1 vì 'microplastics' cũng chứa 'plastic' (hàng riêng); lần 2 "
     "('tonnes of plastic') trong câu cùng chuỗi, không đánh", 1, None,
     None, "LC", None),
    ("S019", "microplastics", "L", "repetition", "S016: microplastic",
     "high", None, None, 1, None, None, "LC", None),
    ("S019", "drinking water", "L", "repetition", "S017: drinking water",
     "high", None, "'some of them' trong câu không đánh", 1, None, None,
     "LC", None),
    # S020
    ("S020", "plastics", "L", "repetition", "S019: plastic", "high",
     None, "a global plastics treaty", 1, None, None, "LC", None),
    # S021
    ("S021", "co-authors", "L", "repetition", "S014: study co-author",
     "high", None,
     "'they/their' trong câu chỉ 4 tác giả, không đánh", 1, None, None,
     "LC", None),
    ("S021", "bottled water", "L", "repetition", "S016: Bottled Water",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] sửa ante (nhóm 4/12): S016 không chứa 'the study'; nhắc gần
    # nhất là S014 study co-author; alt "R: the" (mapping §3.6).
    ("S021", "the study", "L", "repetition", "S014: study co-author",
     "high", "R: the",
     "nguồn lỗi chính tả 'conduced' (= conducted), ghi §8", 1, None,
     None, "LC", None),
    # S022
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S022", "the Columbia physical chemist", "L", "repetition",
     "S009: a Columbia physical chemist", "high", "R: the",
     "lặp cả cụm danh hiệu (chỉ Min); 'he/his' trong câu không đánh", 1,
     None, None, "LC", None),
    ("S022", "dual laser microscope technology", "L", "repetition",
     "S001: a microscope using dual lasers", "high", None,
     "lặp microscope + dual laser", 1, None, None, "LC", None),
    ("S022", "bottled water", "L", "repetition",
     "S021: their bottled water use", "high", None, None, 1, None,
     None, "LC", None),
    # [Phase-2] reduced ← S021 cutting back: đồng nghĩa (H&H §6.2) — chuỗi
    # 'giảm dùng nước đóng chai'; VI đối ứng 'giảm' ← 'cắt giảm'.
    ("S022", "reduced", "L", "synonym",
     "S021: cutting back on their bottled water use", "high", None,
     "reduced ≈ cutting back (reduced ... by half)", 1, None, None,
     "LC", None),
    # S023
    ("S023", "Stapleton", "L", "repetition",
     "S014: study co-author Phoebe Stapleton", "high", None,
     "'she' trong câu không đánh", 1, None, None, "LC", None),
    ("S023", "filtered water", "L", "repetition",
     "S009: the reverse osmosis membrane filter", "high", None,
     "filter → filtered; cùng trường nước", 1, None, None, "LC", None),
    # S024
    ("S024", "But", "C", "adversative",
     "S023: Stapleton relies more on filtered water", "high", None,
     "nối liên câu", 1, None, None, "LC", None),
    ("S024", "study co-author", "L", "repetition", "S021: co-authors",
     "high", None, "kết chuỗi co-author + study", 1, None, None, "LC",
     None),
    # [Phase-2] increased ↔ reduced (S022): phép đối tăng–giảm qua câu (TNT
    # §30; H&H §6.4 opposites) — nước đóng chai giảm ↔ nước máy tăng.
    ("S024", "increased", "L", "antonym",
     "S022: reduced his bottled water use by half", "high", None,
     "phép đối increased ↔ reduced (increased his tap water usage)", 1,
     None, None, "LC", None),
    ("S024", "a Columbia environmental chemist", "L", "repetition",
     "S022: the Columbia physical chemist", "high", None,
     "kết chuỗi Columbia + chemist; 'his' trong câu không đánh", 1,
     None, None, "LC", None),
    ("S024", "filters", "L", "repetition",
     "S009: the reverse osmosis membrane filter", "high", None, None,
     1, None, None, "LC", None),
    ("S024", "plastics", "L", "repetition", "S020: plastics", "high",
     None, "by introducing plastics", 1, None, None, "LC", None),
    # S025 — KHỐI CẮT (VI none): tie chỉ phía EN
    ("S025", "Stapleton", "L", "repetition", "S023: Stapleton", "high",
     None, "khối cắt, VI none", 1, None, None, "LC", None),
    # S026
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S026", "the study", "L", "repetition", "S021: the study",
     "high", "R: the",
     "VI đối ứng 'nghiên cứu này' là quy chiếu (R) — dịch chuyển", 1,
     None, None, "LC", None),
    # [Phase-2] perils ← S014 dangerous: đồng nghĩa (H&H §6.2) — chuỗi
    # 'nguy hiểm' harmful→dangerous→perils→danger; VI đối ứng mối nguy
    # hiểm (S025 TT) ← nguy hiểm (S014 TT).
    ("S026", "perils", "L", "synonym",
     "S014: if it's dangerous or how dangerous", "med", None,
     "perils ≈ danger; mắt xích giữa dangerous (S014) và The danger "
     "(S027)", 1, None, None, "LC", None),
    ("S026", "fine plastics particles", "L", "repetition",
     "S016: nano- and microplastic particles", "high", None,
     "kết chuỗi plastics + particles; 'it's too early' trong câu "
     "không đánh", 1, None, None, "LC", None),
    # S027
    # [Phase-2] cập nhật ante theo tiền trạm gần nhất (nhóm 4): S026 perils
    # là mắt xích gần hơn; danger ≈ perils → sub synonym; alt "R: the"
    # (mapping §3.6).
    ("S027", "The danger", "L", "synonym",
     "S026: perils of fine plastics particles", "high", "R: the",
     "danger ≈ perils (cùng chuỗi harmful→dangerous→perils); câu quote bị "
     "tách (mở lờ, ghi §8)", 1, None, None, "LC", None),
    ("S027", "the plastics", "L", "repetition",
     "S026: fine plastics particles", "high", None, None, 1, None,
     None, "LC", None),
    ("S027", "question", "L", "repetition", "S012: the big question",
     "high", None, "'unanswered' có hàng [Phase-2] riêng ← S012 answer", 1,
     None, None, "LC", None),
    # [Phase-2] unanswered ← S012 can't answer: lặp hình vị answer (H&H
    # §6.2; TNT §26) — chuỗi 'câu hỏi chưa có lời đáp'; VI đối ứng 'lời đáp'
    # ← 'trả lời'.
    ("S027", "unanswered", "L", "repetition",
     "S012: Researchers still can't answer the big question", "med",
     None, "answer → unanswered (phủ định hóa hình vị)", 1, None, None,
     "LC", None),
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S028", "the research", "L", "synonym", "S015: the current research",
     "high", "R: the", None, 1, None, None, "LC", None),
    # [Phase-2] concerning ← S026 unease: đồng nghĩa (H&H §6.2) — mở chuỗi
    # 'lo âu' unease→concerning→disturbing→worried; VI đối ứng 'lo ngại'.
    ("S028", "concerning", "L", "synonym",
     "S026: a general unease about perils", "med", None,
     "the most concerning ≈ unease (điều đáng lo ngại nhất)", 1, None,
     None, "LC", None),
    # S029
    ("S029", "We", "R", "personal",
     "Somarelli + giới nghiên cứu (ngoại văn bản — quote)", "med", None,
     "ngoại quy chiếu; 'and others', 'we' lần 2 trong câu không đánh",
     1, None, None, "LC", "E"),
    ("S029", "these nanoplastics", "R", "demonstrative",
     "S012: those nanoplastic pieces", "high", None,
     "lần 2 ('nanoplastics carry') trong câu cùng chuỗi, không đánh",
     1, None, None, "LC", "A"),
    ("S029", "cells", "L", "repetition", "S015: the cells", "high",
     None,
     "'cell stress', 'cell function' lần 2,3 trong câu cùng chuỗi "
     "(biến thể), không đánh", 1, None, None, "LC", None),
    ("S029", "chemical additives", "L", "repetition",
     "S028: the additives", "high", None,
     "lặp 'additives'; 'chemical' khởi tạo chuỗi hóa học", 1, None,
     None, "LC", None),
    # S030
    ("S030", "Somarelli", "L", "repetition", "S028: Jason Somarelli",
     "high", None, "'his own' trong câu không đánh", 1, None, None,
     "LC", None),
    ("S030", "chemicals", "L", "repetition",
     "S029: chemical additives", "high", None,
     "cancer-causing chemicals", 1, None, None, "LC", None),
    # [Phase-2] cancer-causing ← S028 oncology: collocation trường 'ung
    # thư' (H&H §6.4) — VI đối ứng lặp nguyên từ 'ung thư' (S027→S029 TT).
    ("S030", "cancer-causing", "L", "collocation",
     "S028: professor of medicine and comparative oncology", "med",
     None,
     "oncology ≈ cancer (cùng trường ung thư); chức danh Somarelli nêu "
     "ở câu trước", 1, None, None, "LC", None),
    ("S030", "these plastics", "R", "demonstrative",
     "S027: the plastics themselves", "high", None, None, 1, None,
     None, "LC", "A"),
    # S031
    ("S031", "small particles", "L", "repetition",
     "S026: fine plastics particles", "high", None,
     "lặp 'particles'; 'they' trong câu không đánh", 1, None, None,
     "LC", None),
    # [Phase-2] disturbing ← S028 concerning: đồng nghĩa (H&H §6.2) — tiếp
    # chuỗi 'lo âu'; VI đối ứng 'lo ngại' (S030 TT).
    ("S031", "disturbing", "L", "synonym",
     "S028: the additives are the most concerning", "med", None,
     "disturbing ≈ concerning (điều đáng lo ngại)", 1, None, None, "LC",
     None),
    # S032
    ("S032", "Diana", "L", "repetition",
     "S031: University of Toronto evolutionary biologist Zoie Diana",
     "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S032", "the study", "L", "repetition", "S026: the study",
     "high", "R: the",
     "occ 1: lần 2 ('the study of plastics' = lĩnh vực, nghĩa khác) "
     "không đánh", 1, None, None, "LC", None),
    ("S032", "researchers", "L", "repetition", "S012: Researchers",
     "high", None, "the new tool researchers used", 1, None, None,
     "LC", None),
    ("S032", "the new tool", "R", "nominal",
     "S022: dual laser microscope technology", "high", None,
     "danh ngữ tóm chỉ công cụ; 'makes this' trong câu không đánh", 1,
     None, None, "LC", "A"),
    ("S032", "plastics", "L", "repetition", "S030: these plastics",
     "high", None, "in the environment and body", 1, None, None, "LC",
     None),
    # S033
    ("S033", "Min", "L", "repetition", "S022: Wei Min", "high", None,
     None, 1, None, None, "LC", None),
    ("S033", "dual laser microscope technology", "L", "repetition",
     "S022: dual laser microscope technology", "high", None, None, 1,
     None, None, "LC", None),
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S033", "the lasers", "L", "repetition",
     "S001: a microscope using dual lasers", "high", "R: the",
     "exposed to the lasers", 1, None, None, "LC", None),
    ("S033", "chemical properties", "L", "repetition",
     "S030: cancer-causing chemicals", "med", None,
     "hình vị 'chemical' lặp (tính chất ↔ chất)", 1, None, None, "LC",
     None),
    # S034
    ("S034", "Yan", "L", "repetition",
     "S024: study co-author Beizhan Yan", "high", None, None, 1, None,
     None, "LC", None),
    ("S034", "Qian", "L", "repetition",
     "S009: study lead author Naixin Qian", "high", None, None, 1,
     None, None, "LC", None),
    ("S034", "him", "R", "personal", "S033: Min", "high", None,
     "VI hiện thực hóa thành 'ông Min' (L) — dịch chuyển", 1, None,
     None, "LC", "A"),
    ("S034", "that technique", "R", "demonstrative",
     "S033: dual laser microscope technology", "high", None, None, 1,
     None, None, "LC", "A"),
    ("S034", "plastics", "L", "repetition", "S032: plastics",
     "high", None, "find and identify plastics", 1, None, None, "LC",
     None),
    ("S034", "researchers", "L", "repetition", "S032: researchers",
     "high", None, None, 1, None, None, "LC", None),
    ("S034", "established methods", "L", "repetition",
     "S016: standardized (measuring) methods", "high", None,
     "lặp 'methods'", 1, None, None, "LC", None),
    # [Phase-2] identify ← S033 identifies: lặp động từ kỹ thuật (H&H §6.2;
    # TNT §26) — VI đối ứng 'xác định' lặp nguyên từ.
    ("S034", "identify", "L", "repetition",
     "S033: identifies specific compounds", "high", None,
     "identifies → identify (find and identify plastics)", 1, None,
     None, "LC", None),
    # S035
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S035", "the work", "L", "synonym", "S026: the study", "high",
     "R: the", "work ≈ study; VI 'công trình này' là quy chiếu (R)", 1,
     None, None, "LC", None),
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S035", "the detection", "L", "repetition",
     "S001: detected and categorized", "high", "R: the",
     "detect → detection", 1, None, None, "LC", None),
    ("S035", "nanoplastics", "L", "repetition", "S029: these "
     "nanoplastics", "high", None, None, 1, None, None, "LC", None),
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S035", "the technique", "L", "repetition",
     "S034: that technique", "high", "R: the",
     "'she said she'd' trong câu không đánh", 1, None, None, "LC",
     None),
    # [Phase-2] other: quy chiếu so sánh (H&H §2.5 "other") — "other
    # analytical chemists" = nhà hóa học khác VỚI các nhà hóa học của nghiên
    # cứu đã nêu ở câu trước → [LC]; VI đối ứng "khác" (S034 TT).
    ("S035", "other", "R", "comparative",
     "S024: a Columbia environmental chemist (các nhà hóa học của nghiên "
     "cứu)", "med", None,
     "[LC] other analytical chemists = khác với nhóm nhà hóa học của "
     "nghiên cứu; H&H §2.5 other", 1, None, None, "LC", "A"),
    # [Phase-2] advance ← S032 development: đồng nghĩa (H&H §6.2) — VI đối
    # ứng 'tiến bộ' ← 'bước phát triển'.
    ("S035", "advance", "L", "synonym",
     "S032: an exciting development", "high", None,
     "advance ≈ development (an important advance)", 1, None, None,
     "LC", None),
    # [Phase-2] results: danh từ tổng quát tóm kết quả đã báo ở S003 (H&H
    # §6.1 general word; mapping §3.6 → alt "R: the").
    ("S035", "results", "L", "general word",
     "S003: researchers found particle levels ranged from 110,000 to "
     "400,000", "med", "R: the",
     "the results = kết quả nghiên cứu (mức độ hạt) đã báo ở S003", 1,
     None, None, "LC", None),
    ("S035", "chemists", "L", "repetition",
     "S024: a Columbia environmental chemist", "high", None,
     "other analytical chemists", 1, None, None, "LC", None),
    # S036 — KHỐI CẮT (VI none)
    ("S036", "oceanographer", "L", "repetition",
     "S035: an oceanographer at the Sea Education Association",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S036", "plastic waste", "L", "repetition", "S034: plastics",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    # S037 — KHỐI CẮT
    # [Phase-2] alt "R: the": mạo từ xác định thâu vào hàng L (mapping §3.6).
    ("S037", "the nanoplastic", "L", "repetition",
     "S035: the detection of nanoplastics", "high", "R: the",
     "biến thể số ít; khối cắt, VI none", 1, None, None, "LC", None),
    # S038 — KHỐI CẮT
    ("S038", "Hardesty", "L", "repetition",
     "S036: Denise Hardesty", "high", None,
     "khối cắt, VI none; 'I' trong câu chỉ Hardesty, không đánh", 1,
     None, None, "LC", None),
    ("S038", "nanoplastics", "L", "repetition", "S037: the nanoplastic",
     "high", None, "khối cắt, VI none", 1, None, None, "LC", None),
    ("S038", "bottled water", "L", "repetition",
     "S022: his bottled water use", "high", None, "khối cắt, VI none",
     1, None, None, "LC", None),
    ("S038", "tap water", "L", "repetition",
     "S024: his tap water usage", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", None),
    ("S038", "drinking water", "L", "repetition",
     "S019: drinking water", "high", None, "khối cắt, VI none", 1,
     None, None, "LC", None),
    # S039
    ("S039", "Yan", "L", "repetition", "S034: Yan and Qian", "high",
     None, "'he…their' trong câu không đánh", 1, None, None, "LC",
     None),
    ("S039", "to study", "L", "repetition", "S032: the study", "med",
     None, "danh từ → động từ; 'water supplies' trường nước quá rộng, "
     "không đánh", 1, None, None, "LC", None),
    # [Phase-2] other: quy chiếu so sánh (H&H §2.5) — "other municipal water
    # supplies" = nguồn khác với nước đóng chai đã nghiên cứu; có thể đọc
    # ngoại cảnh ('thành phố khác') nên conf low (mapping §7).
    ("S039", "other", "R", "comparative",
     "S038: nanoplastics in bottled water", "low", None,
     "[LC] other municipal water supplies = nguồn nước khác với nước "
     "đóng chai của nghiên cứu (H&H §2.5); đọc phụ 'thành phố khác' → "
     "conf low", 1, None, None, "LC", "A"),
    # [Phase-2] plastics ← S034: mắt xích được S041 "single-use plastics"
    # cite làm tiền trạm nhưng chưa có hàng (nhóm 12; H&H §6.2; TNT §26).
    ("S039", "plastics", "L", "repetition",
     "S034: find and identify plastics", "high", None,
     "lặp plastics (how much plastics are in their tap water)", 1, None,
     None, "LC", None),
    ("S039", "tap water", "L", "repetition",
     "S038: 'clean' tap water (khối cắt)", "high", None, None, 1,
     None, None, "LC", None),
    # S040
    ("S040", "Previous studies", "L", "repetition",
     "S007: Previous studies", "high", None, "lặp nguyên cụm mở đầu",
     1, None, None, "LC", None),
    ("S040", "microplastics", "L", "repetition", "S019: microplastics",
     "high", None, None, 1, None, None, "LC", None),
    ("S040", "nanoplastic", "L", "repetition",
     "S037: the nanoplastic (khối cắt)", "high", None,
     "biến thể số ít", 1, None, None, "LC", None),
    ("S040", "tap water", "L", "repetition", "S039: their tap water",
     "high", None, None, 1, None, None, "LC", None),
    ("S040", None, "E", "nominal",
     "S038: nanoplastics in bottled water (khối cắt)", "high", None,
     "[LC] tỉnh lược 'water' sau 'bottled' (than bottled [∅ water]); VI "
     "lấp đầy 'nước đóng chai' nên không có E phía VI", 1, "bottled",
     "{water}", "LC", None),
    # S041
    ("S041", "human health", "L", "repetition",
     "S016: potential health impacts", "high", None,
     "lặp 'health'; 'he' trong câu không đánh", 1, None, None, "LC",
     None),
    # [Phase-2] unknowns ← S027 unanswered question: danh từ tổng quát tóm
    # 'vấn đề chưa có lời đáp' (H&H §6.1 general word; §6.2 synonym); VI
    # hiện thực hóa bằng cụm động từ 'chưa biết rõ' → không có hàng VI.
    ("S041", "unknowns", "L", "general word",
     "S027: still an unanswered question", "med", None,
     "unknowns ≈ unanswered question (vấn đề chưa biết); VI 'chưa biết "
     "rõ' hiện thực hóa", 1, None, None, "LC", None),
    # [Phase-2] worried ← S031 disturbing: đồng nghĩa (H&H §6.2) — khép chuỗi
    # 'lo âu' unease→concerning→disturbing→worried; VI 'lo lắng' ← 'lo
    # ngại'.
    ("S041", "worried", "L", "synonym",
     "S031: What's disturbing", "med", None,
     "worried ≈ disturbing/concerning (people who are worried)", 1,
     None, None, "LC", None),
    ("S041", "Yan", "L", "repetition", "S039: Yan said", "high", None,
     None, 1, None, None, "LC", None),
    ("S041", "reusable bottles", "L", "repetition",
     "S009: the bottle itself", "high", None, "hình vị 'bottle'", 1,
     None, None, "LC", None),
    ("S041", "single-use plastics", "L", "repetition",
     "S039: how much plastics are in their tap water", "high", None,
     None, 1, None, None, "LC", None),
]

TT = [
    # S002
    ("S002", "mảnh nhựa siêu nhỏ này", "R", "demonstrative",
     "S001: mảnh nhựa nano cực nhỏ vô hình", "high", None,
     "hậu chỉ từ 'này' + lặp 'mảnh nhựa'; 'họ' trong câu không đánh",
     1, None, None, "LC", "A"),
    # S003
    ("S003", "các nhà nghiên cứu", "L", "repetition",
     "S002: các nhà nghiên cứu tại trường đại học Columbia và Rutgers",
     "high", None, None, 1, None, None, "LC", None),
    ("S003", "nước đóng chai", "L", "repetition",
     "S001: một lít nước đóng chai", "high", None,
     "trong 'nhãn hiệu nước đóng chai phổ biến'", 1, None, None, "LC",
     None),
    ("S003", "mỗi lít", "L", "repetition", "S001: một lít nước đóng chai",
     "high", None, "đơn vị lặp", 1, None, None, "LC", None),
    # [Phase-2] hạt ← S002 mảnh: đồng nghĩa mảnh ≈ hạt (H&H §6.2; TNT §31
    # phép thế đẳng nghĩa) — mắt xích được S004 (Đây/những hạt) cite làm tiền
    # trạm nhưng chưa có hàng (nhóm 12).
    ("S003", "hạt", "L", "synonym",
     "S002: mảnh nhựa siêu nhỏ này", "med", None,
     "mảnh ≈ hạt (mức độ hạt); mở chuỗi 'hạt'", 1, None, None, "LC",
     None),
    # S004
    ("S004", "Đây", "R", "demonstrative", "S003: mức độ hạt dao động",
     "high", None, "đối ứng EN 'These'", 1, None, None, "LC", "A"),
    ("S004", "những hạt", "L", "repetition", "S003: mức độ hạt",
     "high", None, None, 1, None, None, "LC", None),
    # S005
    ("S005", "micron", "L", "repetition", "S004: một micron", "high",
     None,
     "'micromet' là đổi tên trong câu (TC), không đánh; 'nó' trong câu "
     "không đánh", 1, None, None, "LC", None),
    # S006
    ("S006", "micron", "L", "repetition", "S005: 25.400 micron",
     "high", None, None, 1, None, None, "LC", None),
    # S007
    ("S007", "Các nghiên cứu trước đây", "L", "repetition",
     "S003: một nghiên cứu", "high", None, "mở chuỗi 'nghiên cứu'", 1,
     None, None, "LC", None),
    # [Phase-2] hơn: quy chiếu so sánh (H&H §2.5) — 'lớn hơn' so với hạt nano
    # < 1 micron tả ở câu trước (S004) → [LC]; EN đối ứng "bigger" (S007 ST).
    ("S007", "hơn", "R", "comparative",
     "S004: những hạt có kích thước nhỏ hơn một micron", "med", None,
     "[LC] 'lớn hơn một chút' = lớn hơn hạt nano đã tả ở S004; H&H §2.5 "
     "comparative; 'nhỏ hơn' trong S004 là so sánh trong câu", 1, None,
     None, "LC", "A"),
    # [Phase-2] tái phân loại sub collocation → antonym: vi ↔ nano là cặp đối
    # nghĩa kích thước qua câu (TNT §30 phép đối; H&H §6.4 opposites).
    ("S007", "vi nhựa", "L", "antonym", "S001: mảnh nhựa nano",
     "med", None,
     "phép đối vi ↔ nano (đối lập kích thước, TNT §30; H&H §6.4)", 1,
     None, None, "LC", None),
    ("S007", "hạt", "L", "repetition", "S004: những hạt", "high", None,
     "trong 'các hạt vi nhựa'", 1, None, None, "LC", None),
    ("S007", "micron", "L", "repetition", "S006: 83 micron", "high",
     None, "đến 1 micron", 1, None, None, "LC", None),
    # S008
    ("S008", "Nghiên cứu", "L", "repetition",
     "S007: Các nghiên cứu trước đây", "high", None,
     "danh từ không xác định VI; mạo từ hiểu ngầm = nghiên cứu đã nhắc",
     1, None, None, "LC", None),
    ("S008", "nhựa nano", "L", "repetition",
     "S007: hạt vi nhựa — như S001: mảnh nhựa nano", "high", None,
     "lượng nhựa nano", 1, None, None, "LC", None),
    ("S008", "vi nhựa", "L", "repetition", "S007: vi nhựa", "high",
     None, "so với hạt vi nhựa", 1, None, None, "LC", None),
    ("S008", "nước đóng chai", "L", "repetition",
     "S003: nước đóng chai", "high", None, None, 1, None, None, "LC",
     None),
    # S009
    ("S009", "nghiên cứu", "L", "repetition", "S008: Nghiên cứu",
     "high", None, "Tác giả chính của nghiên cứu", 1, None, None, "LC",
     None),
    ("S009", "nhựa", "L", "repetition", "S008: nhựa nano", "high",
     None,
     "occ 1: lần 2 nằm trong 'chính chai nhựa' (hàng riêng), không đánh",
     1, None, None, "LC", None),
    ("S009", "chính chai nhựa", "L", "repetition",
     "S003: nước đóng chai", "high", None, "hình vị 'chai'", 1, None,
     None, "LC", None),
    ("S009", "Columbia", "L", "repetition",
     "S002: trường đại học Columbia và Rutgers", "high", None,
     "một nhà hóa học vật lý ở Columbia", 1, None, None, "LC", None),
    # S010
    ("S010", "Bà", "R", "personal", "S009: Naixin Qian", "high", None,
     "đối ứng EN 'She'", 1, None, None, "LC", "A"),
    ("S010", "thương hiệu", "L", "synonym",
     "S003: ba nhãn hiệu nước đóng chai", "high", None,
     "occ 1: lặp 3 lần trong câu (một thương hiệu, thương hiệu hơn) "
     "cùng chuỗi, không đánh; nguồn VI đổi 'nhãn hiệu'→'thương hiệu'",
     1, None, None, "LC", None),
    ("S010", "các nhà nghiên cứu", "L", "repetition",
     "S003: các nhà nghiên cứu", "high", None,
     "'họ' trong câu không đánh; EN 'the three brands' có hàng R nhưng "
     "VI 'ba thương hiệu' không tín hiệu — chỉ ghi nhận", 1, None,
     None, "LC", None),
    # [Phase-2] hơn (occ 1, "mẫu hơn"): quy chiếu so sánh (H&H §2.5) — chuẩn
    # so sánh là 5 mẫu (S003) ở câu trước → [LC]; 'thương hiệu hơn' (occ 2)
    # so với 'ba thương hiệu' trong cùng câu → [TC] (ghi §4.3 analysis).
    ("S010", "hơn", "R", "comparative",
     "S003: năm mẫu của ba nhãn hiệu nước đóng chai", "med", None,
     "[LC] 'nhiều mẫu hơn' = nhiều hơn 5 mẫu đã xem xét (S003); H&H §2.5; "
     "'thương hiệu hơn' trong câu → [TC]", 1, None, None, "LC", "A"),
    # [Phase-2] mẫu ← S003: chuỗi 'mẫu' bị sót (TNT §26 phép lặp; H&H §6.2).
    ("S010", "mẫu", "L", "repetition",
     "S003: năm mẫu của ba nhãn hiệu nước đóng chai", "high", None,
     "lặp mẫu (muốn có nhiều mẫu hơn)", 1, None, None, "LC", None),
    ("S010", "nghiên cứu", "L", "repetition", "S009: nghiên cứu",
     "med", None,
     "occ 2: lần 1 nằm trong 'các nhà nghiên cứu' (hàng riêng), lần 2 "
     "là động từ 'nghiên cứu' (danh từ → động từ)", 2, None, None,
     "LC", None),
    # S011
    ("S011", "Tuy nhiên", "C", "adversative",
     "S010: Bà sẽ không tiết lộ ba thương hiệu", "high", None,
     "đối ứng EN 'Still'; cụm 'bought at a WalMart' bị cắt", 1, None,
     None, "LC", None),
    ("S011", "bà", "R", "personal", "S010: Bà", "high", None, None, 1,
     None, None, "LC", "A"),
    ("S011", "chúng", "R", "personal", "S010: ba thương hiệu",
     "high", None, None, 1, None, None, "LC", "A"),
    ("S011", "phổ biến", "L", "repetition",
     "S003: nhãn hiệu nước đóng chai phổ biến", "high", None, None, 1,
     None, None, "LC", None),
    # S012
    ("S012", "Các nhà nghiên cứu", "L", "repetition",
     "S010: các nhà nghiên cứu", "high", None,
     "'vẫn chưa' là trạng từ, không phải nối", 1, None, None, "LC",
     None),
    ("S012", "Những mảnh nhựa nano đó", "R", "demonstrative",
     "S001: mảnh nhựa nano", "high", None,
     "hậu chỉ từ 'đó' + lặp 'mảnh nhựa nano'", 1, None, None, "LC",
     "A"),
    # S013
    ("S013", "Điều đó", "R", "demonstrative",
     "S012: câu hỏi lớn về mảnh nhựa nano", "high", None,
     "đối ứng EN 'That'", 1, None, None, "LC", "A"),
    # S014
    ("S014", "Chúng tôi", "R", "personal",
     "giới nghiên cứu (ngoại văn bản — quote Stapleton)", "med", None,
     "ngoại quy chiếu", 1, None, None, "LC", "E"),
    ("S014", "nó", "R", "personal",
     "S012: mảnh nhựa nano có gây hại cho sức khỏe không", "med",
     None,
     "occ 1 vì 'nói' chứa 'nó'; nó = vấn đề nhựa nano gây hại; "
     "'nguy hiểm' lần 2 trong câu (TC) không đánh; lần 1 có hàng "
     "[Phase-2] ← S012 gây hại", 1, None, None,
     "LC", "A"),
    ("S014", "nghiên cứu", "L", "repetition", "S010: nghiên cứu",
     "high", None,
     "occ 1: lần 2 nằm trong 'nhà nghiên cứu' (hàng riêng), không đánh",
     1, None, None, "LC", None),
    ("S014", "nhà nghiên cứu", "L", "repetition",
     "S012: Các nhà nghiên cứu", "med", None,
     "VI tự sinh lặp chuỗi trong chức danh 'một nhà nghiên cứu chất "
     "độc'; EN 'a toxicologist' không có", 1, None, None, "LC", None),
    # [Phase-2] không biết ← S002 chưa bao giờ biết: chuỗi 'biết' (TNT §26;
    # bắc cầu §8) — mắt xích được hàng "biết" (S015) cite (nhóm 12).
    ("S014", "không biết", "L", "repetition",
     "S002: họ chưa bao giờ biết có bao nhiêu và loại nào", "med",
     None,
     "lặp biết (cùng phủ định); bắc cầu xa (TNT §8)", 1, None, None,
     "LC", None),
    # [Phase-2] nguy hiểm (occ 1) ← S012 gây hại: đồng nghĩa (H&H §6.2) —
    # mắt xích được S026 "nguy hiểm" cite (nhóm 12).
    ("S014", "nguy hiểm", "L", "synonym",
     "S012: Những mảnh nhựa nano đó có gây hại cho sức khỏe không",
     "high", None,
     "nguy hiểm ≈ gây hại; lần 2 trong câu (TC) không đánh", 1, None,
     None, "LC", None),
    # [Phase-2] đồng tác giả ← S009 Tác giả chính: lặp hình vị 'tác giả'
    # (TNT §26) — mắt xích được S021 "đồng tác giả" cite (nhóm 12); EN đối
    # ứng co-author (S014 ST).
    ("S014", "đồng tác giả", "L", "repetition",
     "S009: Tác giả chính của nghiên cứu", "med", None,
     "lặp hình vị 'tác giả' (tác giả chính → đồng tác giả, đổi vai)", 1,
     None, None, "LC", None),
    ("S014", "Rutgers", "L", "repetition",
     "S002: trường đại học Columbia và Rutgers", "high", None, None,
     1, None, None, "LC", None),
    # S015
    ("S015", "Chúng ta", "R", "personal",
     "giới nghiên cứu (ngoại văn bản — quote)", "med", None,
     "ngoại quy chiếu; VI dùng 'chúng ta' thay cho EN 'we'", 1, None,
     None, "LC", "E"),
    # [Phase-2] biết ↔ không biết (S014): phép đối phủ định–khẳng định qua
    # câu (TNT §30; H&H §6.4 opposites) — đối xứng EN "do know" ↔ "don't
    # know" (S015/S014 ST).
    ("S015", "biết", "L", "antonym",
     "S014: Chúng tôi không biết", "high", None,
     "phép đối biết ↔ không biết ('Chúng ta biết' ↔ 'Chúng tôi không "
     "biết')", 1, None, None, "LC", None),
    ("S015", "chúng", "R", "personal",
     "S012: Những mảnh nhựa nano đó", "high", None,
     "occ 1: lần 2 ('chúng đang làm') trong câu cùng chuỗi, không đánh",
     1, None, None, "LC", "A"),
    ("S015", "nghiên cứu hiện tại", "L", "repetition",
     "S014: nghiên cứu", "high", None, None, 1, None, None, "LC",
     None),
    ("S015", "con người", "L", "repetition", "S006: con người",
     "high", None, "bao gồm cả con người", 1, None, None, "LC", None),
    # S016
    ("S016", "Nước đóng chai", "L", "repetition",
     "S008: nước đóng chai", "high", None,
     "tên tổ chức chứa chuỗi", 1, None, None, "LC", None),
    ("S016", "hạt", "L", "repetition", "S007: hạt", "high", None,
     "trong 'các hạt nano'", 1, None, None, "LC", None),
    ("S016", "nano", "L", "repetition", "S012: mảnh nhựa nano",
     "high", None, "trong 'các hạt nano'", 1, None, None, "LC", None),
    ("S016", "vi nhựa", "L", "repetition", "S008: vi nhựa", "high",
     None, None, 1, None, None, "LC", None),
    ("S016", "sức khỏe", "L", "repetition", "S012: sức khỏe",
     "high", None, None, 1, None, None, "LC", None),
    # S017
    ("S017", "Vì vậy", "C", "causal",
     "S016: thiếu phương pháp tiêu chuẩn và đồng thuận khoa học",
     "high", None, None, 1, None, None, "LC", None),
    ("S017", "những hạt này", "R", "demonstrative",
     "S016: các hạt nano và vi nhựa", "high", None, None, 1, None,
     None, "LC", "A"),
    ("S017", "nước uống", "L", "superordinate",
     "S003: nước đóng chai", "med", None,
     "nước uống ⊃ nước đóng chai", 1, None, None, "LC", None),
    # S018
    ("S018", "nhựa", "L", "repetition", "S016: vi nhựa", "high",
     None, "các nhà sản xuất nhựa", 1, None, None, "LC", None),
    # S019
    ("S019", "thế giới", "L", "repetition", "S018: Hội đồng Hóa học "
     "Mỹ — ngữ cảnh toàn cầu", "med", None,
     "occ 1: lần 2 ('trên thế giới') trong câu cùng chuỗi, không đánh",
     1, None, None, "LC", None),
    ("S019", "nhựa", "L", "repetition", "S018: nhựa", "high", None,
     "occ 1: lần 2 ('tấn nhựa') trong câu cùng chuỗi, không đánh", 1,
     None, None, "LC", None),
    ("S019", "hạt vi nhựa", "L", "repetition", "S016: vi nhựa",
     "high", None,
     "gộp 2 chuỗi hạt + vi nhựa; 'một số trong số đó' trong câu "
     "không đánh", 1, None, None, "LC", None),
    ("S019", "nước uống", "L", "repetition", "S017: nước uống",
     "high", None, None, 1, None, None, "LC", None),
    # S020
    ("S020", "nhựa", "L", "repetition", "S019: nhựa", "high", None,
     "hiệp ước nhựa toàn cầu", 1, None, None, "LC", None),
    # S021
    ("S021", "đồng tác giả", "L", "repetition",
     "S014: đồng tác giả nghiên cứu", "high", None,
     "'họ' trong câu không đánh", 1, None, None, "LC", None),
    ("S021", "nước đóng chai", "L", "repetition",
     "S016: Nước đóng chai", "high", None, None, 1, None, None, "LC",
     None),
    ("S021", "nghiên cứu", "L", "repetition", "S015: nghiên cứu hiện "
     "tại", "high", None, "tiến hành nghiên cứu", 1, None, None, "LC",
     None),
    # S022
    ("S022", "nhà hóa học vật lý ở Columbia", "L", "repetition",
     "S009: một nhà hóa học vật lý ở Columbia", "high", None,
     "lặp cả cụm danh hiệu (chỉ Min); 'ông' trong câu không đánh", 1,
     None, None, "LC", None),
    ("S022", "công nghệ kính hiển vi laser kép", "L", "repetition",
     "S001: kính hiển vi sử dụng tia laser kép", "high", None,
     "lặp kính hiển vi + laser kép; 'công nghệ' từ mới", 1, None,
     None, "LC", None),
    ("S022", "nước đóng chai", "L", "repetition",
     "S021: nước đóng chai", "high", None, None, 1, None, None, "LC",
     None),
    # [Phase-2] giảm ← S021 cắt giảm: lặp hình vị 'giảm' (TNT §26 phép lặp)
    # — đối xứng EN reduced (S022 ST) ← cutting back (S021 ST).
    ("S022", "giảm", "L", "repetition",
     "S021: cắt giảm việc sử dụng nước đóng chai", "high", None,
     "giảm một nửa ← cắt giảm", 1, None, None, "LC", None),
    # S023
    ("S023", "Stapleton", "L", "repetition",
     "S014: Phoebe Stapleton", "high", None,
     "'bà' trong câu không đánh", 1, None, None, "LC", None),
    ("S023", "nước lọc", "L", "repetition",
     "S009: bộ lọc màng thẩm thấu ngược", "high", None,
     "bộ lọc → nước lọc; cùng trường nước", 1, None, None, "LC",
     None),
    # S024
    ("S024", "Nhưng", "C", "adversative",
     "S023: bà phụ thuộc nhiều hơn vào nước lọc", "high", None,
     "nối liên câu", 1, None, None, "LC", None),
    ("S024", "đồng tác giả nghiên cứu", "L", "repetition",
     "S021: đồng tác giả", "high", None,
     "gộp chuỗi đồng tác giả + nghiên cứu", 1, None, None, "LC",
     None),
    ("S024", "một nhà hóa học môi trường ở Columbia", "L", "repetition",
     "S022: nhà hóa học vật lý ở Columbia", "high", None,
     "kết chuỗi nhà hóa học + Columbia", 1, None, None, "LC", None),
    # [Phase-2] tăng cường ↔ giảm (S022): phép đối tăng–giảm qua câu (TNT
    # §30; H&H §6.4 opposites) — nước máy tăng ↔ nước đóng chai giảm; đối
    # xứng EN increased ↔ reduced (S024/S022 ST).
    ("S024", "tăng cường", "L", "antonym",
     "S022: giảm một nửa lượng nước đóng chai", "high", None,
     "phép đối tăng cường ↔ giảm (tăng cường sử dụng nước máy)", 1,
     None, None, "LC", None),
    ("S024", "bộ lọc", "L", "repetition",
     "S009: bộ lọc màng thẩm thấu ngược", "high", None, None, 1, None,
     None, "LC", None),
    ("S024", "nhựa", "L", "repetition", "S020: nhựa", "high", None,
     "VI đổi 'introducing plastics' thành 'sử dụng nhựa'", 1, None,
     None, "LC", None),
    # S025 (= EN S026)
    ("S025", "nghiên cứu này", "R", "demonstrative",
     "S021: tiến hành nghiên cứu", "high", None,
     "hậu chỉ từ 'này'; EN đối ứng 'the study' là lặp từ (L) — dịch "
     "chuyển", 1, None, None, "LC", "A"),
    # [Phase-2] nguy hiểm ← S014: lặp nguyên từ trong 'mối nguy hiểm' (TNT
    # §26) — mắt xích giữa nguy hiểm (S014) và sự nguy hiểm (S026); đối
    # xứng EN perils (S026 ST).
    ("S025", "nguy hiểm", "L", "repetition",
     "S014: có nguy hiểm hay nguy hiểm đến mức nào", "high", None,
     "lặp nguy hiểm (mối nguy hiểm của các hạt nhựa mịn)", 1, None,
     None, "LC", None),
    ("S025", "các hạt nhựa mịn", "L", "repetition",
     "S019: hạt vi nhựa", "high", None,
     "kết chuỗi hạt + nhựa; 'mịn' từ mới; 'nhưng còn quá sớm' trong "
     "câu, không đánh", 1, None, None, "LC", None),
    # S026 (= EN S027)
    # [Phase-2] cập nhật ante theo tiền trạm gần nhất (nhóm 4): S025 'mối
    # nguy hiểm' là nhắc gần nhất (TNT §26).
    ("S026", "nguy hiểm", "L", "repetition",
     "S025: mối nguy hiểm của các hạt nhựa mịn", "high", None,
     "sự nguy hiểm; câu quote bị tách như EN, ghi §8", 1, None, None,
     "LC", None),
    ("S026", "nhựa", "L", "repetition", "S025: các hạt nhựa mịn",
     "high", None, None, 1, None, None, "LC", None),
    ("S026", "câu hỏi", "L", "repetition", "S012: câu hỏi lớn",
     "high", None, "'chưa có lời đáp' có hàng [Phase-2] riêng ← S012 "
     "trả lời", 1, None, None, "LC", None),
    # [Phase-2] lời đáp ← S012 trả lời: đồng nghĩa (H&H §6.2; TNT §31 phép
    # thế đẳng nghĩa) — đối xứng EN unanswered (S027 ST) ← answer.
    ("S026", "lời đáp", "L", "synonym",
     "S012: vẫn chưa thể trả lời câu hỏi lớn", "med", None,
     "lời đáp ≈ trả lời ('chưa có lời đáp')", 1, None, None, "LC",
     None),
    # S027 (= EN S028)
    ("S027", "nghiên cứu", "L", "repetition",
     "S025: nghiên cứu này", "high", None,
     "người không tham gia nghiên cứu; 'tôi' hư chỉ trong quote", 1,
     None, None, "LC", None),
    # [Phase-2] lo ngại ← S025: lặp nguyên từ ('đáng lo ngại nhất' ← 'sự
    # lo ngại') (TNT §26) — mở chuỗi 'lo' lo ngại→lo lắng; đối xứng EN
    # concerning (S028 ST) ← unease (S026 ST).
    ("S027", "lo ngại", "L", "repetition",
     "S025: có sự lo ngại chung", "high", None,
     "lặp lo ngại (điều đáng lo ngại nhất)", 1, None, None, "LC",
     None),
    # S028 (= EN S029)
    ("S028", "Chúng tôi", "R", "personal",
     "Somarelli + giới nghiên cứu (ngoại văn bản — quote)", "med",
     None,
     "ngoại quy chiếu; 'chúng tôi' lần 2 trong câu (viết thường) "
     "cùng chuỗi, không đánh", 1, None, None, "LC", "E"),
    ("S028", "những loại nhựa nano này", "R", "demonstrative",
     "S012: Những mảnh nhựa nano đó", "high", None,
     "lặp 'nhựa nano' trong cụm", 1, None, None, "LC", "A"),
    ("S028", "tế bào", "L", "repetition", "S015: tế bào", "high",
     None,
     "occ 1: lần 2, 3 ('cho tế bào', 'của tế bào') trong câu cùng "
     "chuỗi, không đánh", 1, None, None, "LC", None),
    ("S028", "phụ gia hóa học", "L", "repetition",
     "S027: các chất phụ gia", "high", None, None, 1, None, None,
     "LC", None),
    # [Phase-2] chỉ ra ← S024 đã chỉ ra: VI lặp nguyên cụm động từ (TNT
    # §26) — EN đổi 'pointed out' → 'shown' nên không có hàng EN đối ứng.
    ("S028", "chỉ ra", "L", "repetition",
     "S024: đã chỉ ra rằng bản thân các bộ lọc", "med", None,
     "lặp 'đã chỉ ra' (We and others have shown); EN đổi động từ", 1,
     None, None, "LC", None),
    # S029 (= EN S030)
    ("S029", "Somarelli", "L", "repetition",
     "S027: Jason Somarelli", "high", None,
     "'của ông' trong câu không đánh", 1, None, None, "LC", None),
    ("S029", "công trình nghiên cứu", "L", "repetition",
     "S027: nghiên cứu", "high", None,
     "VI tự sinh lặp chuỗi 'nghiên cứu'; EN 'his own work' không có",
     1, None, None, "LC", None),
    ("S029", "hóa chất", "L", "repetition",
     "S028: phụ gia hóa học", "high", None,
     "hóa chất gây ung thư", 1, None, None, "LC", None),
    # [Phase-2] ung thư ← S027 'nhóm ung thư đối chiếu': lặp nguyên từ
    # trong chức danh (TNT §26) — EN đối ứng là collocation oncology ≈
    # cancer (S028/S030 ST).
    ("S029", "ung thư", "L", "repetition",
     "S027: giám đốc nhóm ung thư đối chiếu", "med", None,
     "lặp ung thư (hóa chất gây ung thư ← chức danh Somarelli)", 1,
     None, None, "LC", None),
    ("S029", "những loại nhựa này", "R", "demonstrative",
     "S028: những loại nhựa nano này", "high", None,
     "lặp khung 'những loại … này'", 1, None, None, "LC", "A"),
    # S030 (= EN S031)
    ("S030", "các hạt nhỏ", "L", "repetition",
     "S025: các hạt nhựa mịn", "high", None,
     "lặp 'hạt'; 'nhỏ' tiếp trường kích thước; 'chúng' trong câu "
     "không đánh", 1, None, None, "LC", None),
    # [Phase-2] lo ngại ← S027 đáng lo ngại: lặp nguyên từ (TNT §26) — đối
    # xứng EN disturbing (S031 ST) ← concerning (S028 ST).
    ("S030", "lo ngại", "L", "repetition",
     "S027: điều đáng lo ngại nhất", "high", None,
     "lặp lo ngại (Điều đáng lo ngại)", 1, None, None, "LC", None),
    # S031 (= EN S032)
    ("S031", "Diana", "L", "repetition",
     "S030: nhà sinh vật học tiến hóa Zoie Diana", "high", None, None,
     1, None, None, "LC", None),
    # [Phase-2] tham gia ← S027 'không tham gia nghiên cứu': VI lặp nguyên
    # cụm khẳng định tính chuyên gia ngoài (TNT §26) — EN 'was/was not part
    # of' dùng giới từ chức năng nên không có hàng EN.
    ("S031", "tham gia", "L", "repetition",
     "S027: người không tham gia nghiên cứu", "med", None,
     "lặp 'không tham gia nghiên cứu' (công thức dẫn nguồn)", 1, None,
     None, "LC", None),
    ("S031", "nghiên cứu", "L", "repetition", "S029: công trình nghiên "
     "cứu", "high", None,
     "occ 1: lần 2 nằm trong 'các nhà nghiên cứu' (hàng riêng), lần 3 "
     "('nghiên cứu về nhựa' = lĩnh vực) không đánh", 1, None, None,
     "LC", None),
    # [Phase-2] sửa ante (nhóm 12): S021 không chứa 'các nhà nghiên cứu';
    # nhắc gần nhất là S012 (TNT §26).
    ("S031", "các nhà nghiên cứu", "L", "repetition",
     "S012: Các nhà nghiên cứu", "high", None,
     "công cụ mới mà các nhà nghiên cứu sử dụng", 1, None, None, "LC",
     None),
    ("S031", "công cụ mới", "R", "nominal",
     "S022: công nghệ kính hiển vi laser kép", "high", None,
     "danh ngữ tóm chỉ công cụ; 'đây' trong câu không đánh", 1, None,
     None, "LC", "A"),
    ("S031", "nhựa", "L", "repetition", "S029: những loại nhựa này",
     "high", None, None, 1, None, None, "LC", None),
    # S032 (= EN S033)
    ("S032", "Min", "L", "repetition", "S022: Ông Wei Min", "high",
     None, None, 1, None, None, "LC", None),
    ("S032", "công nghệ kính hiển vi laser kép", "L", "repetition",
     "S022: công nghệ kính hiển vi laser kép", "high", None, None, 1,
     None, None, "LC", None),
    ("S032", "tia laser", "L", "repetition",
     "S001: tia laser kép", "high", None, None, 1, None, None, "LC",
     None),
    ("S032", "tính chất hóa học", "L", "repetition",
     "S029: hóa chất", "med", None, "cùng gốc 'hóa'", 1, None, None,
     "LC", None),
    # S033 (= EN S034)
    ("S033", "Yan", "L", "repetition",
     "S024: đồng tác giả nghiên cứu Beizhan Yan", "high", None, None,
     1, None, None, "LC", None),
    ("S033", "Qian", "L", "repetition",
     "S009: Naixin Qian", "high", None, None, 1, None, None, "LC",
     None),
    ("S033", "ông Min", "L", "repetition", "S032: ông Min", "high",
     None,
     "VI hiện thực hóa đại từ EN 'him' thành danh ngữ — dịch chuyển",
     1, None, None, "LC", None),
    ("S033", "kỹ thuật đó", "R", "demonstrative",
     "S032: công nghệ kính hiển vi laser kép", "high", None, None, 1,
     None, None, "LC", "A"),
    ("S033", "nhựa", "L", "repetition", "S031: nhựa", "high", None,
     "các loại nhựa quá nhỏ", 1, None, None, "LC", None),
    # [Phase-2] xác định ← S032: lặp động từ kỹ thuật (TNT §26) — đối xứng
    # EN identify (S034 ST) ← identifies (S033 ST).
    ("S033", "xác định", "L", "repetition",
     "S032: giúp xác định các hợp chất cụ thể", "high", None,
     "lặp xác định (để tìm và xác định các loại nhựa)", 1, None, None,
     "LC", None),
    ("S033", "các nhà nghiên cứu", "L", "repetition",
     "S031: các nhà nghiên cứu", "high", None, None, 1, None, None,
     "LC", None),
    ("S033", "phương pháp đã được thiết lập", "L", "repetition",
     "S016: các phương pháp (đo lường) tiêu chuẩn hóa", "high", None,
     "lặp 'phương pháp'", 1, None, None, "LC", None),
    # S034 (= EN S035)
    ("S034", "công trình này", "R", "demonstrative",
     "S031: nghiên cứu về nhựa trong môi trường và cơ thể", "high",
     None,
     "hậu chỉ từ 'này'; EN đối ứng 'the work' là L synonym — dịch "
     "chuyển; 'bà' trong câu không đánh", 1, None, None, "LC", "A"),
    ("S034", "phát hiện", "L", "repetition",
     "S001: được phát hiện và phân loại", "high", None,
     "việc phát hiện nhựa nano", 1, None, None, "LC", None),
    ("S034", "nhựa nano", "L", "repetition", "S028: những loại nhựa "
     "nano này", "high", None, None, 1, None, None, "LC", None),
    ("S034", "kỹ thuật", "L", "repetition", "S033: kỹ thuật đó",
     "high", None, "nhân rộng kỹ thuật", 1, None, None, "LC", None),
    # [Phase-2] tiến bộ ← S031 'bước phát triển': đồng nghĩa (H&H §6.2) —
    # đối xứng EN advance (S035 ST) ← development (S032 ST).
    ("S034", "tiến bộ", "L", "synonym",
     "S031: một bước phát triển thú vị", "high", None,
     "tiến bộ ≈ phát triển (một tiến bộ quan trọng)", 1, None, None,
     "LC", None),
    # [Phase-2] kết quả: danh từ tổng quát tóm kết quả đã báo ở S003 (H&H
    # §6.1 general word); VI không có mạo từ, định danh bằng ngữ cảnh
    # (mapping §4) — đối xứng EN results (S035 ST).
    ("S034", "kết quả", "L", "general word",
     "S003: các nhà nghiên cứu nhận thấy mức độ hạt dao động", "med",
     None,
     "kết quả = kết quả nghiên cứu (mức độ hạt) đã báo ở S003; VI định "
     "danh bằng ngữ cảnh", 1, None, None, "LC", None),
    # [Phase-2] khác: quy chiếu so sánh (H&H §2.5 "other/khác") — 'các nhà
    # hóa học phân tích khác' = khác với các nhà hóa học của nghiên cứu đã
    # nêu → [LC]; EN đối ứng "other" (S035 ST).
    ("S034", "khác", "R", "comparative",
     "S024: một nhà hóa học môi trường ở Columbia (các nhà hóa học của "
     "nghiên cứu)", "med", None,
     "[LC] khác = nhà hóa học khác với nhóm của nghiên cứu; H&H §2.5 "
     "other", 1, None, None, "LC", "A"),
    ("S034", "nhà hóa học", "L", "repetition",
     "S024: nhà hóa học môi trường", "high", None,
     "các nhà hóa học phân tích", 1, None, None, "LC", None),
    # S035 (= EN S039)
    ("S035", "Yan", "L", "repetition", "S033: ông Yan", "high", None,
     "'ông…của họ' trong câu không đánh", 1, None, None, "LC", None),
    ("S035", "nghiên cứu", "L", "repetition",
     "S031: nghiên cứu", "med", None,
     "danh từ → động từ; 'nguồn cung cấp nước' trường nước quá rộng, "
     "không đánh", 1, None, None, "LC", None),
    # [Phase-2] khác (occ 1, "nước khác"): quy chiếu so sánh (H&H §2.5) —
    # nguồn khác với nước đóng chai đã nghiên cứu; occ 2 'những nơi khác'
    # so với các thành phố liệt kê trong cùng câu → [TC] (ghi §4.3);
    # conf low vì có thể đọc ngoại cảnh 'thành phố khác' (mapping §7);
    # EN đối ứng "other" (S039 ST).
    ("S035", "khác", "R", "comparative",
     "S022: nước đóng chai (của nghiên cứu)", "low", None,
     "[LC] 'nguồn cung cấp nước khác' = khác với nước đóng chai đã "
     "nghiên cứu; H&H §2.5; 'những nơi khác' (occ 2) trong câu → "
     "[TC]", 1, None, None, "LC", "A"),
    # [Phase-2] nhựa ← S033: lặp nguyên từ (TNT §26) — đối xứng EN plastics
    # (S039 ST) ← S034.
    ("S035", "nhựa", "L", "repetition",
     "S033: các loại nhựa quá nhỏ", "high", None,
     "lặp nhựa (có bao nhiêu nhựa trong nước máy)", 1, None, None,
     "LC", None),
    ("S035", "nước máy", "L", "repetition", "S024: nước máy",
     "high", None, None, 1, None, None, "LC", None),
    # S036 (= EN S040)
    ("S036", "Các nghiên cứu trước đây", "L", "repetition",
     "S007: Các nghiên cứu trước đây", "high", None,
     "lặp nguyên cụm mở đầu", 1, None, None, "LC", None),
    ("S036", "hạt vi nhựa", "L", "repetition", "S019: hạt vi nhựa",
     "high", None, None, 1, None, None, "LC", None),
    ("S036", "nhựa nano", "L", "repetition", "S034: nhựa nano",
     "high", None, None, 1, None, None, "LC", None),
    ("S036", "nước máy", "L", "repetition", "S035: nước máy",
     "high", None,
     "EN có E 'than bottled [∅ water]' nhưng VI lấp đầy 'nước đóng "
     "chai' nên không có E phía VI", 1, None, None, "LC", None),
    # [Phase-2] nước đóng chai ← S022: vế lấp E của EN (S040 "than bottled
    # [∅]") là lặp chuỗi 'nước đóng chai' (TNT §26) — dịch chuyển EN E ↔
    # VI L.
    ("S036", "nước đóng chai", "L", "repetition",
     "S022: giảm một nửa lượng nước đóng chai sử dụng", "high", None,
     "lặp nước đóng chai (vế lấp tỉnh lược EN)", 1, None, None, "LC",
     None),
    # S037 (= EN S041)
    ("S037", "sức khỏe con người", "L", "repetition",
     "S016: sức khỏe", "high", None,
     "lặp 'sức khỏe'; 'con người' tiếp chuỗi (S015)", 1, None, None,
     "LC", None),
    # [Phase-2] lo lắng ← S030 đáng lo ngại: lặp hình vị 'lo' (TNT §26) —
    # khép chuỗi lo ngại→lo lắng; đối xứng EN worried (S041 ST) ←
    # disturbing (S031 ST).
    ("S037", "lo lắng", "L", "repetition",
     "S030: Điều đáng lo ngại", "med", None,
     "lặp hình vị 'lo' (những người đang lo lắng)", 1, None, None,
     "LC", None),
    ("S037", "Yan", "L", "repetition", "S035: ông Yan", "high", None,
     "'ông' trong câu không đánh", 1, None, None, "LC", None),
    ("S037", "chai có thể tái sử dụng", "L", "repetition",
     "S009: chính chai nhựa", "high", None, "hình vị 'chai'", 1, None,
     None, "LC", None),
    ("S037", "đồ nhựa dùng một lần", "L", "repetition",
     "S036: nhựa nano", "high", None, None, 1, None, None, "LC",
     None),
]
