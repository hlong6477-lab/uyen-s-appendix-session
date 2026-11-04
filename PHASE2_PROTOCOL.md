# PHASE-2 PROTOCOL — Enrichment theo references (H&H 1976, Trần Ngọc Thêm 2006, NTT 2020)

Giao thức này áp dụng cho TỪNG cặp PXX. Mẫu hiệu chuẩn đã hoàn thành: **P21**
(commit `653f198`) — đọc `work/analysis/P21_semantic.md` + `work/tie_tables/P21.py`
trước khi làm việc. Mọi quyết định tie phải LÀM TAY; script chỉ được ĐỊNH VỊ
ứng viên (`python3 /home/z/my-project/scripts/locate_candidates.py PXX [ST|TT]`)
hoặc kiểm chuỗi (`python3 -m pipeline.locate`). CẤM sinh tie từ regex/danh sách.

## 0. Bắt buộc đọc trước (theo thứ tự)

1. `SKILL.md` (đặc biệt §2 Theoretical framing, §2.1 Four rules, §6 Tie table)
2. `references/halliday-hasan-1976.md` (đầy đủ)
3. `references/tran-ngoc-them-2006.md` (đầy đủ)
4. `references/translation-en-vi-2020.md` (đặc biệt §2, §5)
5. `references/en-vi-mapping.md` (§3 decision tests, §6 misclassifications)
6. `work/analysis/P21_semantic.md` + `work/tie_tables/P21.py` — MẪU
7. Cặp của mình: `work/analysis/PXX_semantic.md`, `work/tie_tables/PXX.py`,
   dump text: `python3 /home/z/my-project/scripts/dump_pair.py PXX both`

## 1. Checklist 10 nhóm ứng viên (săn theo references)

Mỗi nhóm: nguồn lý thuyết + ví dụ P21 + điều kiện nhận [LC].

1. **R so sánh** (H&H §2.5): EN `same/similar/different/other/else/more/
   fewer/less/such`, VI `khác/như vậy/tương tự/riêng` — khi đối tượng so sánh
   nằm ở CÂU TRƯỚC → R, sub `comparative`, ref bắt buộc. So sánh trong cùng
   câu → [TC] KHÔNG đánh, ghi §4.3. (P21: VI S010 "khác" ← S005.)
2. **Phép đối liên câu** (TNT §30; H&H §6.4 opposites): cặp đối nghĩa qua câu
   (thật–giả, chính thức–giả mạo, tăng–giảm, hợp pháp–bất hợp pháp, để dành–
   chi tiêu...) chưa đánh → L, sub `antonym`. (P21: EN real↔fake, VI chính
   thức↔giả mạo.)
3. **Danh từ tổng quát / bridging** (H&H §6.1): EN `the move/decision/issue/
   step/case/plan/advice/phenomenon`, VI `quyết định/vấn đề/bước/trường hợp/
   việc/hiện tượng` trỏ về tình huống câu trước → L, sub `general word`,
   alt `"R: the"` khi định danh rõ (mapping §3.6, §3.13: một hình thức một
   hàng — KHÔNG thêm hàng R thứ hai cho cùng NP).
4. **Chuỗi lặp bị sót** (H&H §6.2 reiteration; TNT §26 phép lặp): động từ/
   danh từ hóa/danh từ lặp liên câu chưa có hàng riêng (một dấu cho mỗi
   chuỗi trong mỗi câu; tiền trạm = nhắc gần nhất). (P21: promised←promising,
   returns, money, offers←offered, Australians, hứa hẹn, tiền, người Úc.)
5. **Continuatives** (H&H §5.8): EN `Now,/Well,/Anyway,/Still,/Indeed,/In
   fact,/Of course,/After all,` đầu câu; VI `Thế là,/Vậy là,/Dù sao,/Trên
   thực tế,/Đáng chú ý,/Theo đó,` → C, sub `continuative`. Nếu hàng cũ ghi
   `temporal` mà đúng nghĩa continuative → RECLASSIFY sub + ghi chú điều chỉnh.
6. **[TC]→[LC] do VI tách câu**: vế EN nằm trong câu thành câu VI riêng →
   tie VI tăng cấp liên câu. (P21: "còn" S002 VI.)
7. **Extended reference** (H&H §2.3.3, §2.4.1.4): `This/That/It` trỏ cả mệnh
   đề, VI `điều đó/việc này/nó` → R demonstrative — kiểm tra sót.
8. **Chỉ từ xác định the + rename** (mapping §3.6): NP "the X" đổi tên/tổng
   quát hóa tham chiếu đã nêu mà CHƯA có hàng nào → thêm hàng (L ưu tiên khi
   có quan hệ từ vựng, alt `"R: the"`); NP đã có hàng L → chỉ thêm alt nếu
   thiếu. (P21: organisation S017, companies S018, tổ chức S016 VI.)
9. **Collocation** (H&H §6.4): cặp từ hệ thống đồng xuất hiện qua câu
   (whole–part, process–product) — chỉ thêm khi RÕ, conf `med`, tránh
   "topic continuity" (mapping §6 cấm L từ chủ đề).
10. **Đối chiếu NTT (2020) §5**: mỗi dịch chuyển EN↔VI tìm được (pronoun↔
    repetition, the↔zero/demonstrative, pro-form↔hiện thực hóa, nối rơi/
    tự sinh) → ghi §7 với tên loại dịch chuyển.

## 2. Quy tắc cứng (không vi phạm)

- R/C/L chỉ [LC]; [TC] chỉ dành cho S/E (theo precedent) → mọi ứng viên
  R/C/L trong câu: KHÔNG đánh, ghi chú analysis.
- ref chỉ có ở R (A/C/E; A = câu TRƯỚC); hàng cat="E" thì ref=None.
- KHÔNG đánh: số liệu, subhead, động từ chức năng báo chí (said/told/
   reported/according to), quan hệ từ trong câu, đại từ trong câu (ghi §4.3),
   lần 2 cùng chuỗi trong cùng câu ("không đánh thêm" precedent).
- KHÔNG xóa/hàng cũ trừ khi reclassify có căn cứ references (ghi rõ trong
  analysis + comment).
- Hàng chồng marker → rút ngắn text hàng E để không đè hàng L (precedent P28).
- Nháy cong ’ (U+2019) giữ nguyên như nguồn; occ đếm case-sensitive substring
  tính cả chuỗi con trong từ khác (precedent P26) + ghi chú vị trí.
- VI tự sinh câu vẫn đánh tie; khối cắt → tie chỉ phía còn câu.

## 3. Mọi hàng mới phải có

- Comment `# [Phase-2] <lý do — trích H&H §… / TNT §… / mapping §…>` ngay
  trên hàng trong file tie table.
- note tiếng Việt có trích dẫn mục lý thuyết; conf trung thực (med/low khi
  dịch chuyển tự sinh hoặc đọc mờ).
- text/gap_after nguyên văn; occ tường minh; kiểm tra bằng pipeline.locate
  khi nghi ngờ trùng chuỗi con.

## 4. Cập nhật analysis (PXX_semantic.md)

- Chèn khung lý thuyết (blockquote giống P21, SAU dòng Nguồn) — chèn ĐÚNG
  MỘT LẦN.
- §2–§6: mỗi mục thêm 1–3 câu "**Theo H&H §… / Theo TNT §…:**" bám sát nội
  dung CẶP MÌNH (cấm copy nguyên đoạn P21 — chỉ mượn khung lý thuyết).
- §4.3: liệt kê ứng viên so sánh/quy chiếu bị loại vì [TC].
- §6: chuỗi mới + hàng mới; §7: dòng dịch chuyển mới theo NTT (2020) §5.
- §9: heading đổi "… (đã cập nhật Phase-2 theo references)"; đếm lại KHỚP
  tie table (lấy số từ pipeline.annotate); ghi rõ "+N hàng Phase-2: …".
- Kết luận: thêm mục cuối "Phase-2 (theo references): N tie mới (EN x / VI
  y) gồm: …; … đúng bảng dịch chuyển NTT (2020) §5."

## 5. Bẫy kỹ thuật (đã gặp ở P21)

- Tie table .py: chuỗi dài tách dòng phải là implicit concatenation — MỖI
  dòng MỞ+ĐÓNG ngoặc kép: `"...chưa hết "`\n`     "tiếp"`. Quên đóng ngoặc
  = SyntaxError. Sau khi edit: `python3 -c "import ast; ast.parse(open(
  'work/tie_tables/PXX.py').read())"`.
- Analysis .md: TRỘN dấu “cong” và "thẳng" — trước khi Edit, in repr dòng
  đích: `python3 - <<'EOF' ... print(repr(line))`. MultiEdit dừng khi old_str
  sai và CÓ THỂ đã áp các edit trước đó — sau lỗi phải kiểm lại trạng thái.
- Chạy gate:
  `cd /home/z/my-project/session && python3 -m pipeline.annotate --work work --pair PXX`
  rồi `python3 -m pipeline.render --work work --pair PXX` — phải PASS cả EN
  và VI. FAIL → sửa HÀNG (occ/span/text), cấm sửa renderer.

## 6. Phạm vi cho phép

CHỈ sửa: `work/analysis/PXX_semantic.md`, `work/tie_tables/PXX.py`, và
outputs `work/pairs/PXX/` do annotate/render sinh ra.
CẤM: git commit/push, sửa pipeline/, templates/, references/, SKILL.md,
file của cặp khác.

## 7. Báo cáo cuối (agent trả về coordinator)

1. PASS? số cũ → mới (EN/VI từng cat R/S/E/C/L).
2. Danh sách hàng mới (sent, text, cat, sub, nhóm checklist nào).
3. Reclassification (nếu có, kèm căn cứ).
4. Ứng viên loại [TC] (dòng ngắn).
5. Vướng mắc (nếu có).
