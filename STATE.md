# SESSION STATE — Appendix 1 (Text 21–40)

Repo này lưu toàn bộ phiên làm việc để sống sót qua các sandbox reset.
Sau reset sandbox: `git clone` repo này lại là lấy lại toàn bộ trạng thái; không cần chạy lại prepare/ingest/segment đã commit.

## Nhiệm vụ
Chạy toàn bộ quy trình manual-first của skill COHESION EN–VI
(SKILL.md ở repo này, copy từ github.com/longme179/Cohesive-Devices-in-English-and-Vietnamese-Analyzing-SKILL)
trên file `upload/target_appendix.md` (20 text: Text 21–40):
ingest → segment → (mỗi cặp: analysis 9 mục + tie table 13 trường viết tay) →
annotate → render (PASS cả EN & VI) → build_appendix → export DOCX + PDF → validate.
Sản phẩm: `out/appendix1/Appendix1.docx` + `.pdf` (bản giao: `/home/z/my-project/download/`).

## Tiến độ

| Bước | Trạng thái | Ghi chú |
|---|---|---|
| Clone skill repo + đọc SKILL.md + templates | ✅ | skill-repo ngoài (chỉ tham chiếu); bản pipeline/templates dùng ở đây |
| prepare_input | ✅ | `work_input/prepared_input.md`, `work_input/repairs.json` |
| ingest → P01..P20 → renumber → **P21..P40** | ✅ | Text NN ↔ PNN |
| segment | ✅ | ST 801 câu / TT 731 câu |
| Phân tích tay + tie table từng cặp | 18/20 ✅ | P24 + P27 còn lại — 2 cặp dài nhất |
| annotate + render từng cặp | 18/20 PASS | |
| build_appendix → export DOCX/PDF → validate | ⏳ | cần 20/20 PASS trước |

## Bảng cặp (P21–P40)

| Pair | Text | ST/TT câu | Phân tích | Tie table | annotate | render EN/VI |
|---|---|---|---|---|---|---|
| P21 | Bunnings scam | 26/22 | ✅ | ✅ | ✅ | PASS/PASS (75/72) |
| P22 | Kid screen time | 60/60 | ✅ | ✅ | ✅ | PASS/PASS (104/102) |
| P23 | Shopping swap $4,000 | 41/45 | ✅ | ✅ | ✅ | PASS/PASS (108/122) |
| P24 | Migration 2025 | 118/114 | ☐ | ☐ | ☐ | ☐ — **CHƯA BẮT ĐẦU** (dài nhất) |
| P25 | Inflation / RBA | 51/57 | ✅ | ✅ | ✅ | PASS/PASS (155/173) |
| P26 | Fastest-growing jobs | 20/19 | ✅ | ✅ | ✅ | PASS/PASS (74/69) |
| P27 | Overemployed | 105/84 | ☐ | ☐ | ☐ | ☐ — **CHƯA BẮT ĐẦU** (thứ 2 dài nhất) |
| P28 | New Year resolution | 72/70 | ✅ | ✅ | ✅ | PASS/PASS (168/170) |
| P29 | Property prices | 27/21 | ✅ | ✅ | ✅ | PASS/PASS (86/65) |
| P30 | Optimistic trends 2025 | 55/44 | ✅ | ✅ | ✅ | PASS/PASS (110/85) |
| P31 | Escaped bear Dubai | 15/15 | ✅ | ✅ | ✅ | PASS/PASS (67/65) |
| P32 | BLM mural | 25/23 | ✅ | ✅ | ✅ | PASS/PASS (77/76) |
| P33 | Salt coffee VN | 45/33 | ✅ | ✅ | ✅ | PASS/PASS (139/86) |
| P34 | Russia fines Google | 6/6 | ✅ | ✅ | ✅ | PASS/PASS (18/18) |
| P35 | Maxar satellite | 8/8 | ✅ | ✅ | ✅ | PASS/PASS (32/34) |
| P36 | AI breast cancer | 33/32 | ✅ | ✅ | ✅ | PASS/PASS (107/105) |
| P37 | Nanoplastics | 41/37 | ✅ | ✅ | ✅ | PASS/PASS (121/114) |
| P38 | WHO salt | 25/25 | ✅ | ✅ | ✅ | PASS/PASS (81/84) |
| P39 | Bangladesh floods | 21/10 | ✅ | ✅ | ✅ | PASS/PASS (60/32) |
| P40 | Pope funds | 7/6 | ✅ | ✅ | ✅ | PASS/PASS (17/20) |

## Còn lại (ưu tiên)

1. **P24** (Migration 2025) — 118/114 câu, dài nhất toàn bộ. Dump: `python3 scripts/dump_pair.py P24 both`
2. **P27** (Overemployed) — 105/84 câu. Dump: `python3 scripts/dump_pair.py P27 both`
3. Khi 20/20 PASS: `python3 -m pipeline.build_appendix --work work --out out/appendix1` → `export_docx` → `export_pdf` → `validate`
4. Copy sản phẩm sang `/home/z/my-project/download/`, commit + push cuối
5. Báo cáo tổng: số tie mỗi cặp/tổng, coverage, kết quả QC/validate

## Lệnh chuẩn (chạy từ gốc repo này)

```bash
python3 -m pipeline.annotate --work work --pair PXX   # gate: cần work/analysis/PXX*.md
python3 -m pipeline.render   --work work --pair PXX   # phải PASS cả EN và VI
# khi mọi cặp PASS:
python3 -m pipeline.build_appendix --work work --out out/appendix1
python3 -m pipeline.export_docx    --out out/appendix1
python3 -m pipeline.export_pdf     --out out/appendix1
python3 -m pipeline.validate       --work work --out out/appendix1
```

## Quy ước đã hiệu chuẩn (từ P21–P40, cập nhật phiên này)

- R/C/L chỉ LIÊN CÂU (LC); đại từ trong câu → chỉ ghi §4.3
- Subhead không gán nhãn
- Số liệu không phải tie L
- Động từ chức năng (said/told/according to) không đánh C
- ref A/C/E quyết bằng đọc hiểu từng R; A = antecedent ở câu TRƯỚC (BẮT BUỘC)
- occ đếm case-sensitive substring; chuỗi text phải là chuỗi con nguyên văn
- EN pro-form → VI hiện thực hóa → chỉ đánh phía EN (nguyên tắc "không bịa ∅")
- Khối cắt VI → tie chỉ EN; VI tự sinh → tie vẫn đánh
- Tiểu đề lồng câu (P30, P33) → tie đánh phần thân câu, không đánh phần tiểu đề
- "The same X" = R comparative; ref="A" (trừ khi so sánh thuần trong câu → dùng ref="E" hoặc ante từ câu trước)
- occ cho đại từ ngắn (he, it, us): cẩn thận chữ nằm trong từ khác ("the" chứa "he", "focus" chứa "us", "công" chứa "ông" v.v.)
