# Báo cáo tie / coverage / QC — Appendix 1 (Text 21–40) — Phase-2

Nguồn: `work/pairs/PXX/*_ties.json` sau khi annotate + render PASS cả EN lẫn VI
(Phase-1) rồi enrich theo 4 digests lý thuyết (Phase-2).
Thang danh mục: R (quy chiếu) / L (từ vựng) / C (nối) / S (thế) / E (tỉnh lược).
Với R: ref A = hồi quy (anaphoric), C = tiền chỉ (cataphoric), E = ngoại văn bản (exophoric).

| Pair | EN tổng | R (A/E/C) | L | C | S | E | VI tổng | R (A/E/C) | L | C | S | E | Chênh EN−VI |
|---|---:|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| P21 | **84** | 11 (4/7/0) | 63 | 7 | 2 | 1 | **82** | 7 (3/4/0) | 69 | 5 | 0 | 1 | +2 |
| P22 | **133** | 18 (18/0/0) | 112 | 3 | 0 | 0 | **130** | 18 (18/0/0) | 109 | 3 | 0 | 0 | +3 |
| P23 | **114** | 25 (16/8/1) | 80 | 7 | 1 | 1 | **126** | 19 (16/3/0) | 98 | 8 | 0 | 1 | -12 |
| P24 | **309** | 60 (50/10/0) | 223 | 16 | 7 | 3 | **284** | 49 (40/9/0) | 215 | 13 | 1 | 6 | +25 |
| P25 | **183** | 19 (15/4/0) | 153 | 8 | 0 | 3 | **204** | 25 (19/6/0) | 167 | 11 | 0 | 1 | -21 |
| P26 | **84** | 9 (7/2/0) | 71 | 4 | 0 | 0 | **74** | 6 (5/1/0) | 65 | 3 | 0 | 0 | +10 |
| P27 | **263** | 84 (65/19/0) | 169 | 8 | 2 | 0 | **186** | 46 (39/7/0) | 130 | 8 | 2 | 0 | +77 |
| P28 | **187** | 57 (20/36/1) | 116 | 11 | 1 | 2 | **187** | 53 (16/36/1) | 119 | 11 | 1 | 3 | +0 |
| P29 | **92** | 5 (5/0/0) | 78 | 9 | 0 | 0 | **71** | 5 (5/0/0) | 57 | 7 | 0 | 2 | +21 |
| P30 | **124** | 25 (12/13/0) | 95 | 3 | 1 | 0 | **100** | 19 (10/9/0) | 78 | 2 | 1 | 0 | +24 |
| P31 | **80** | 2 (2/0/0) | 75 | 2 | 0 | 1 | **73** | 2 (2/0/0) | 67 | 3 | 0 | 1 | +7 |
| P32 | **99** | 11 (9/2/0) | 87 | 1 | 0 | 0 | **91** | 12 (12/0/0) | 78 | 1 | 0 | 0 | +8 |
| P33 | **164** | 26 (21/5/0) | 130 | 8 | 0 | 0 | **111** | 13 (10/3/0) | 93 | 5 | 0 | 0 | +53 |
| P34 | **19** | 1 (1/0/0) | 18 | 0 | 0 | 0 | **18** | 1 (1/0/0) | 17 | 0 | 0 | 0 | +1 |
| P35 | **39** | 2 (2/0/0) | 36 | 1 | 0 | 0 | **41** | 2 (2/0/0) | 37 | 1 | 0 | 1 | -2 |
| P36 | **127** | 13 (12/1/0) | 106 | 6 | 1 | 1 | **128** | 13 (12/1/0) | 107 | 5 | 0 | 3 | -1 |
| P37 | **144** | 23 (20/3/0) | 117 | 3 | 0 | 1 | **139** | 23 (20/3/0) | 113 | 3 | 0 | 0 | +5 |
| P38 | **92** | 8 (7/1/0) | 78 | 4 | 0 | 2 | **93** | 6 (5/1/0) | 81 | 4 | 0 | 2 | -1 |
| P39 | **62** | 9 (9/0/0) | 48 | 2 | 2 | 1 | **32** | 5 (5/0/0) | 24 | 1 | 1 | 1 | +30 |
| P40 | **17** | 0 (0/0/0) | 15 | 0 | 0 | 2 | **22** | 3 (3/0/0) | 17 | 0 | 0 | 2 | -5 |
| **TỔNG** | **2.416** | 408 (295/111/2) | 1.870 | 103 | 17 | 18 | **2.192** | 327 (243/83/1) | 1.741 | 94 | 6 | 24 | **+224** |

## Tổng quan

- **Tổng marker: 4.608** (EN 2.416 / VI 2.192) — Phase-1 đạt 4.034, Phase-2 bổ sung **+574 tie** theo khung lý thuyết → `build_appendix` báo coverage 100% (mọi tie đều dựng lại được marker từ câu nguồn).
- **Phân loại EN:** L 1.870 (77,4%) · R 408 (16,9%: A 295 + E 111 + C 2) · C 103 (4,3%) · S 17 · E 18.
- **Phân loại VI:** L 1.741 (79,4%) · R 327 (14,9%: A 243 + E 83 + C 1) · C 94 (4,3%) · S 6 · E 24.
- **Cả hai thứ tiếng:** L 3.611 (78,4%) · R 735 (16,0%) · C 197 (4,3%) · S 23 · E 42.
- **QC render từng cặp:** 20/20 PASS cả EN lẫn VI (occ case-sensitive, không chồng
  marker, tái tạo flow, hướng antecedent A luôn ở câu trước, mọi R có ref A/C/E).
- **Validate cuối:** 20/20 pairs OK; markers khớp `build_appendix` (2.416/2.192)
  và khớp `match_stats.json` từng cặp (đã đối chiếu chéo khi sinh báo cáo này).
- **DOCX:** 22 bảng, 20 heading "Pair"; shading 5 màu: tím (L) 3.615 run, vàng (R) 1.474 run, cam (C) 201 run, xanh dương (E) 46 run, xanh lá (S) 27 run
  (mã fill thật trong file); 735 superscript A/C/E = đúng tổng R (735).
  Không còn placeholder.
- **Cặp chênh lệch lớn nhất (EN nhiều hơn VI):** P27 (+77) · P33 (+53) · P39 (+30) · P24 (+25) (P27/P33/P39: VI gộp khối, cắt câu; P39 VI cắt mạnh nhất 21→10 câu).
- **Ngược lại (VI nhiều hơn EN):** P25 (-21) · P23 (-12) · P40 (-5) (VI tự sinh câu chuyển ý, tách câu dài thành nhiều câu ngắn).

## Nguồn lý thuyết Phase-2 (+574 tie)

| Nguồn | Dùng cho |
|---|---|
| Halliday & Hasan, *Cohesion in English* (Longman, 1976) | Danh mục EN: reference §2 (comparative §2.5), substitution §3, ellipsis §4, conjunction §5 (continuative §5.8, additive §5.4), lexical §6 (general word §6.1) |
| Trần Ngọc Thêm, *Hệ thống liên kết văn bản tiếng Việt* (NXB GD; 1985/2006) | Danh mục VI: phép lặp (§30 phép đối), phép thế đẳng nghĩa, phép tỉnh lược (yếu/liên kết/mạnh), phép nối (lỏng/liên kết/chặt) |
| Nguyễn Thanh Tùng, HCMUE J. of Science 17(2), 2020, 305–320 | Dịch chuyển EN↔VI thực tế: tách/gộp câu, chủ ngữ khuyết, chuyển danh mục |
| `references/en-vi-mapping.md` (tổng hợp skill) | Decision tests 5 mã: cùng quy chiếu → R, thay lời → S, lượt lời recoverable → E, quan hệ liên vế → C, quan hệ từ vựng → L |

12 nhóm quyết định enrichment ghi tại `PHASE2_PROTOCOL.md` (R comparative H&H §2.5,
general word H&H §6.1, continuative H&H §5.8, phép đối TNT §30, dịch chuyển NTT 2020, ...).
Digest chỉ **giải thích** danh mục; không tự sinh tie. Khi EN và VI đọc khác nhau
(kiểu chủ ngữ khuyết), analysis ghi cả hai cách đọc, bảng giữ **một** mã (SKILL.md §2.4).

## Ghi chú phương pháp

- Tie table 13 trường viết tay từng cặp từ phân tích 9 mục (`work/analysis/PXX_semantic.md`);
  analysis Phase-2 thêm khung lý thuyết + trích dẫn H&H §/TNT §/NTT (2020) từng quyết định.
- Đại từ/từ nối trong câu chỉ ghi ở mục 4.3/5 của analysis, không lập hàng tie.
- Subhead, số liệu, mốc thời gian, tên riêng lần đầu không lập hàng.
- Các khối câu bị cắt phía VI vẫn đánh tie phía EN (ghi chú "câu cắt phía VI").
- occ là số lần gặp chuỗi con case-sensitive tính đến vị trí marker.
- Số liệu thống kê, shading và superscript trong báo cáo này được tính lại bằng
  `scripts/gen_tie_report.py` trực tiếp từ `*_ties.json` + DOCX thật, có đối chiếu
  chéo `match_stats.json` từng cặp (20/20 khớp).
