# Báo cáo tie / coverage / QC — Appendix 1 (Text 21–40)

Nguồn: `work/pairs/PXX/*_ties.json` sau khi annotate + render PASS cả EN lẫn VI.
Thang danh mục: R (quy chiếu) / L (từ vựng) / C (nối) / S (thế) / E (tỉnh lược).
Với R: ref A = hồi quy, C = tiền chỉ (không có), E = ngoại văn bản.

| Pair | EN tổng | R (A/E) | L | C | S | E | VI tổng | R (A/E) | L | C | S | E | Chênh EN−VI |
|---|---:|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| P21 | **75** | 11 (4/7) | 54 | 7 | 2 | 1 | **72** | 6 (2/4) | 61 | 4 | 0 | 1 | +3 |
| P22 | **104** | 18 (18/0) | 85 | 1 | 0 | 0 | **102** | 18 (18/0) | 83 | 1 | 0 | 0 | +2 |
| P23 | **108** | 24 (15/9) | 76 | 6 | 1 | 1 | **122** | 18 (15/3) | 96 | 7 | 0 | 1 | -14 |
| P24 | **292** | 58 (48/10) | 209 | 15 | 7 | 3 | **267** | 48 (39/9) | 200 | 12 | 1 | 6 | +25 |
| P25 | **155** | 17 (13/4) | 133 | 5 | 0 | 0 | **173** | 23 (17/6) | 142 | 8 | 0 | 0 | -18 |
| P26 | **74** | 9 (7/2) | 61 | 4 | 0 | 0 | **69** | 6 (5/1) | 60 | 3 | 0 | 0 | +5 |
| P27 | **223** | 79 (60/19) | 134 | 8 | 2 | 0 | **161** | 43 (36/7) | 108 | 8 | 2 | 0 | +62 |
| P28 | **168** | 54 (18/36) | 100 | 11 | 1 | 2 | **170** | 50 (14/36) | 105 | 11 | 1 | 3 | -2 |
| P29 | **86** | 2 (2/0) | 75 | 9 | 0 | 0 | **65** | 2 (2/0) | 54 | 7 | 0 | 2 | +21 |
| P30 | **110** | 25 (11/14) | 82 | 2 | 1 | 0 | **85** | 17 (9/8) | 65 | 2 | 1 | 0 | +25 |
| P31 | **67** | 1 (1/0) | 64 | 1 | 0 | 1 | **65** | 1 (1/0) | 61 | 2 | 0 | 1 | +2 |
| P32 | **77** | 14 (12/2) | 62 | 1 | 0 | 0 | **76** | 12 (12/0) | 63 | 1 | 0 | 0 | +1 |
| P33 | **139** | 24 (19/5) | 110 | 5 | 0 | 0 | **86** | 13 (10/3) | 71 | 2 | 0 | 0 | +53 |
| P34 | **18** | 1 (1/0) | 17 | 0 | 0 | 0 | **18** | 1 (1/0) | 17 | 0 | 0 | 0 | +0 |
| P35 | **32** | 1 (1/0) | 30 | 1 | 0 | 0 | **34** | 1 (1/0) | 31 | 1 | 0 | 1 | -2 |
| P36 | **107** | 13 (12/1) | 86 | 6 | 1 | 1 | **105** | 12 (11/1) | 85 | 5 | 0 | 3 | +2 |
| P37 | **121** | 19 (16/3) | 98 | 3 | 0 | 1 | **114** | 19 (16/3) | 92 | 3 | 0 | 0 | +7 |
| P38 | **81** | 7 (6/1) | 68 | 4 | 0 | 2 | **84** | 6 (5/1) | 72 | 4 | 0 | 2 | -3 |
| P39 | **60** | 9 (9/0) | 46 | 2 | 2 | 1 | **32** | 5 (5/0) | 24 | 1 | 1 | 1 | +28 |
| P40 | **17** | 0 (0/0) | 15 | 0 | 0 | 2 | **20** | 3 (3/0) | 15 | 0 | 0 | 2 | -3 |
| **TỔNG** | **2114** | 386 (273/113) | 1605 | 91 | 17 | 15 | **1920** | — | — | — | — | — | **4034** |

## Tổng quan

- **Tổng marker: 4.034** (EN 2.114 / VI 1.920) — `build_appendix` báo coverage 100%
  (mọi tie đều dựng lại được marker từ câu nguồn).
- **Phân loại EN:** L 1.605 (76%) · R 386 (18,3%: A 273 + E 113) · C 91 (4,3%) · S 17 · E 15.
- **Phân loại VI:** L 1.505 (78,4%) · R 304 (15,8%: A 222 + E 82) · C 82 (4,3%) · S 6 · E 23.
- **QC render từng cặp:** 20/20 PASS cả EN lẫn VI (occ case-sensitive, không chồng
  marker, tái tạo flow, hướng antecedent A luôn ở câu trước, mọi R có ref A/C/E).
- **Validate cuối:** 20/20 pairs OK; markers khớp `build_appendix` (2.114/1.920).
- **DOCX:** 22 bảng, 20 heading "Pair"; shading 5 màu: vàng 1.382 run (R),
  xanh lá 25 (S), xanh dương 40 (E), cam 175 (C), tím 3.112 (L); 690 superscript A/C/E
  (= đúng tổng R 690). Không còn placeholder.
- **Cặp chênh lệch lớn nhất:** P39 (+28, VI cắt mạnh) · P24 (+25) · P27 (+62 —
  VI tự sinh 2 câu, gộp 8 khối, cắt 14 câu) · ngược lại P23 (−14) và P25 (−18)
  (VI tự sinh nhiều câu).

## Ghi chú phương pháp

- Tie table 13 trường viết tay từng cặp từ phân tích 9 mục (`work/analysis/PXX_semantic.md`).
- Đại từ/từ nối trong câu chỉ ghi ở mục 4.3/5 của analysis, không lập hàng tie.
- Subhead, số liệu, mốc thời gian, tên riêng lần đầu không lập hàng.
- Các khối câu bị cắt phía VI vẫn đánh tie phía EN (ghi chú "câu cắt phía VI").
- occ là số lần gặp chuỗi con case-sensitive tính đến vị trí marker.