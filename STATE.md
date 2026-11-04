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
| Clone skill repo + đọc SKILL.md + templates | ✅ | Phase-2: đồng bộ SKILL.md mới + references/ (H&H 1976, TNT 2006, NTT 2020, en-vi-mapping) |
| prepare_input | ✅ | `work_input/prepared_input.md`, `work_input/repairs.json` |
| ingest → P01..P20 → renumber → **P21..P40** | ✅ | Text NN ↔ PNN |
| segment | ✅ | ST 801 câu / TT 731 câu |
| Phân tích tay + tie table từng cặp (Phase-1) | 20/20 ✅ | 4.034 tie |
| annotate + render từng cặp (Phase-1) | 20/20 PASS | |
| **Phase-2 (references)**: enrichment 3 nguồn lý thuyết | 20/20 ✅ | +574 tie → 4.608; PHASE2_PROTOCOL.md 12 nhóm; analysis thêm khung lý thuyết + trích dẫn H&H §/TNT § + NTT (2020) dịch chuyển |
| build_appendix → export DOCX/PDF → validate (Phase-2) | ✅ | markers EN 2416 / VI 2192 = 4608; coverage 100%; validate 20/20 OK; DOCX 184KB + PDF 841KB |

## Bảng cặp (P21–P40)

| Pair | Text | ST/TT câu | Phân tích | Tie table | annotate | render EN/VI (Phase-1 → Phase-2) |
|---|---|---|---|---|---|---|
| P21 | Bunnings scam | 26/22 | ✅ | ✅ | ✅ | 75/72 → **PASS/PASS (84/82)** |
| P22 | Kid screen time | 60/60 | ✅ | ✅ | ✅ | 104/102 → **PASS/PASS (133/130)** |
| P23 | Shopping swap $4,000 | 41/45 | ✅ | ✅ | ✅ | 108/122 → **PASS/PASS (114/126)** |
| P24 | Migration 2025 | 118/114 | ✅ | ✅ | ✅ | 292/267 → **PASS/PASS (309/284)** |
| P25 | Inflation / RBA | 51/57 | ✅ | ✅ | ✅ | 155/173 → **PASS/PASS (183/204)** |
| P26 | Fastest-growing jobs | 20/19 | ✅ | ✅ | ✅ | 74/69 → **PASS/PASS (84/74)** |
| P27 | Overemployed | 105/84 | ✅ | ✅ | ✅ | 223/161 → **PASS/PASS (263/186)** |
| P28 | New Year resolution | 72/70 | ✅ | ✅ | ✅ | 168/170 → **PASS/PASS (187/187)** |
| P29 | Property prices | 27/21 | ✅ | ✅ | ✅ | 86/65 → **PASS/PASS (92/71)** |
| P30 | Optimistic trends 2025 | 55/44 | ✅ | ✅ | ✅ | 110/85 → **PASS/PASS (124/100)** |
| P31 | Escaped bear Dubai | 15/15 | ✅ | ✅ | ✅ | 67/65 → **PASS/PASS (80/73)** |
| P32 | BLM mural | 25/23 | ✅ | ✅ | ✅ | 77/76 → **PASS/PASS (99/91)** |
| P33 | Salt coffee VN | 45/33 | ✅ | ✅ | ✅ | 139/86 → **PASS/PASS (164/111)** |
| P34 | Russia fines Google | 6/6 | ✅ | ✅ | ✅ | 18/18 → **PASS/PASS (19/18)** |
| P35 | Maxar satellite | 8/8 | ✅ | ✅ | ✅ | 32/34 → **PASS/PASS (39/41)** |
| P36 | AI breast cancer | 33/32 | ✅ | ✅ | ✅ | 107/105 → **PASS/PASS (127/128)** |
| P37 | Nanoplastics | 41/37 | ✅ | ✅ | ✅ | 121/114 → **PASS/PASS (144/139)** |
| P38 | WHO salt | 25/25 | ✅ | ✅ | ✅ | 81/84 → **PASS/PASS (92/93)** |
| P39 | Bangladesh floods | 21/10 | ✅ | ✅ | ✅ | 60/32 → **PASS/PASS (62/32)** |
| P40 | Pope funds | 7/6 | ✅ | ✅ | ✅ | 17/20 → **PASS/PASS (17/22)** |

## TRẠNG THÁI: HOÀN THÀNH PHASE-2 ✅ (theo references H&H 1976 / TNT 2006 / NTT 2020)

20/20 cặp PASS Phase-2 (sau khi đã PASS Phase-1). Đã build_appendix lại với
**4.608 markers** (EN 2.416 / VI 2.192), coverage 100%, validate 20/20 OK,
export DOCX 184KB + PDF 841KB, copy sang `/home/z/my-project/download/appendix1/`.

**Tổng tie 20 cặp (Phase-2): EN 2.416 / VI 2.192 / tổng 4.608**
(+574 tie so với Phase-1 = +14,2%).
Phân loại EN: L 1.870 / R 408 (A 295 + E 111 + C 2) / C 103 / S 17 / E 18.
Phân loại VI: L 1.741 / R 327 (A 243 + E 83 + C 1) / C 94 / S 6 / E 24.

### Phase-2 — enrichment theo references (commits 4ff0c71 → FINAL)

Nguồn lý thuyết (đồng bộ vào `references/` từ skill repo):
- `halliday-hasan-1976.md` — reference (personal/demonstrative/comparative +
  `the`), substitution, ellipsis, conjunction (4 loại + continuatives),
  lexical cohesion (reiteration + collocation/opposites).
- `tran-ngoc-them-2006.md` — phát ngôn, phép lặp (§26–29), phép đối (§30),
  phép thế đẳng nghĩa (§31), phép liên tưởng (§32), thế đại từ khiếm diện
  (§35–36), tỉnh lược (§37/§41), phép nối (§38/§43).
- `translation-en-vi-2020.md` — Nguyễn Thanh Tùng (2020): 6 dịch chuyển
  EN↔VI đặc trưng (pronoun↔repetition, the↔zero/demonstrative, ellipsis…).
- `en-vi-mapping.md` — 14 phép thử quyết định mã + 8 sai phân loại điển hình.

Giao thức: `PHASE2_PROTOCOL.md` (12 nhóm checklist; mọi hàng mới viết tay với
comment `# [Phase-2]` + trích dẫn mục lý thuyết). Điểm nhóm chính:
1. **R comparative** (H&H §2.5): khác/hơn nữa/other/further/broader/more/
   bigger/better/similar… — +25 cặp EN↔VI đối xứng.
2. **Phép đối liên câu** (TNT §30; H&H §6.4): thật–giả, tăng–giảm, lớn–nhỏ,
   nano–micro, cost-effective–ineffective, stranded–evacuated…
3. **General noun / bridging** (H&H §6.1): organisation/tổ chức, the
   legislation/luật, figures/con số, số tiền, venues/địa điểm…
4. **Chuỗi lặp sót** (H&H §6.2; TNT §26): promised←promising, money/tiền,
   Australians/người Úc, arrival/cập bến, doctors/bác sĩ…
5. **Continuatives** (H&H §5.8): Now/, In fact/Trên thực tế, At the end of
   the day/Cuối cùng, Today/Ngày nay (reclassify sub từ temporal/adversative).
6. **[TC]→[LC]** do VI tách câu: còn (P21), trứng (P33), đồng thời (P33).
7. **Extended reference** (H&H §2.3.3): this sort of thing, sự việc này…
8. **The+rename** (mapping §3.6): the company/công ty (P34), the latest
   figures (P25), Iraqi government (P31) + ~20 alt "R: the" bổ sung.
9. **Collocation** (H&H §6.4): disconnected↔detox, drowning←floods,
   excited←energize, business leaders←employer…
10. **Nối liên câu sót** (H&H §5.4/§5.5): For example/Ví dụ, though/Tuy
   nhiên, also/cũng ×~15 cặp.
11. **Rà chuỗi ngược ante-không-có-hàng**: +~30 mắt xích (rise S006, data
   S008, Việt Nam S011…).

Sửa lỗi/luyện chuẩn phát sinh: bản đồ câu P30 (S028 có bản dịch nhưng ghi
   CẮT — đã sửa bản đồ + bù 4 hàng VI), xóa 3 hàng "the same" [TC] của P30
   (mapping §3.14), RECLASSIFY In fact/Trên thực tế (P38), Meanwhile/Trong
   khi đó giữ temporal (H&H §5.7) ở P25/P29 nhưng adversative ở P23 (nghĩa
   đối lập cụ thể — ghi căn cứ từng cặp), 2 ứng viên we/chúng tôi của P23
   giữ quy ước loại (attribution cùng câu).

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
