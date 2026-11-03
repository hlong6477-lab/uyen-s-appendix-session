# SESSION STATE — Appendix 1 (Text 21–40)

Repo này lưu toàn bộ phiên làm việc để sống sót qua các sandbox reset.
Sau khi reset: `git pull` repo này là lấy lại được toàn bộ trạng thái.

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
| prepare_input (chuẩn hoá 2 kiểu bảng, 3 repairs: swap P29-L466, swap P33-L586, fix `*,*` P30-L515) | ✅ | `work_input/prepared_input.md`, `work_input/repairs.json` |
| ingest → P01..P20 → renumber → **P21..P40** | ✅ | Text NN ↔ PNN |
| segment | ✅ | ST 801 câu / TT 731 câu |
| Phân tích tay + tie table từng cặp | ⏳ | xem bảng dưới |
| annotate + render từng cặp | ⏳ | |
| build_appendix → export DOCX/PDF → validate | ⏳ | |

## Bảng cặp (P21–P40)

| Pair | Text | ST/TT câu | Phân tích | Tie table | annotate | render EN/VI |
|---|---|---|---|---|---|---|
| P21 | Bunnings scam | 26/22 | ☐ | ☐ | ☐ | ☐ |
| P22 | Kid screen time | 60/60 | ☐ | ☐ | ☐ | ☐ |
| P23 | Shopping swap $4,000 | 41/45 | ☐ | ☐ | ☐ | ☐ |
| P24 | Migration 2025 | 118/114 | ☐ | ☐ | ☐ | ☐ |
| P25 | Inflation / RBA | 51/57 | ☐ | ☐ | ☐ | ☐ |
| P26 | Fastest-growing jobs | 20/19 | ☐ | ☐ | ☐ | ☐ |
| P27 | Overemployed | 105/84 | ☐ | ☐ | ☐ | ☐ |
| P28 | New Year resolution | 72/70 | ☐ | ☐ | ☐ | ☐ |
| P29 | Property prices | 27/21 | ☐ | ☐ | ☐ | ☐ |
| P30 | Optimistic trends 2025 | 55/44 | ☐ | ☐ | ☐ | ☐ |
| P31 | Escaped bear Dubai | 15/15 | ☐ | ☐ | ☐ | ☐ |
| P32 | BLM mural | 25/23 | ☐ | ☐ | ☐ | ☐ |
| P33 | Salt coffee VN | 45/33 | ☐ | ☐ | ☐ | ☐ |
| P34 | Russia fines Google | 6/6 | ☐ | ☐ | ☐ | ☐ |
| P35 | Maxar satellite | 8/8 | ☐ | ☐ | ☐ | ☐ |
| P36 | AI breast cancer | 33/32 | ☐ | ☐ | ☐ | ☐ |
| P37 | Nanoplastics | 41/37 | ☐ | ☐ | ☐ | ☐ |
| P38 | WHO salt | 25/25 | ☐ | ☐ | ☐ | ☐ |
| P39 | Bangladesh floods | 21/10 | ☐ | ☐ | ☐ | ☐ |
| P40 | Pope funds | 7/6 | ☐ | ☐ | ☐ | ☐ |

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

## Quy ước bắt buộc (tóm tắt từ SKILL.md — không được bỏ qua)

1. Không sinh tie bằng regex / danh sách đại từ-từ nối / đếm chuỗi / vòng lặp.
2. Mỗi R phải có ref ∈ {A,C,E} quyết bằng đọc hiểu; không mặc định "A".
3. Không bịa ∅ khi bản dịch đã lấp đầy chỗ trống; pro-form thay thế → ghi S.
4. Không copy tie/ghi chú từ cặp khác.
5. Row 13 trường: (sent, text, cat, sub, ante, conf, alt, note, occ,
   gap_after, recovered, level, ref). level ∈ LC/TC/TD.
6. Tie trong câu EN không có bản dịch (ô VI rỗng/none): đánh dấu ở EN, không bịa bên VI.
7. Câu VI tự sinh (ô EN none): không bắt cặp ngược về EN.
