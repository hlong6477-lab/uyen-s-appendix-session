#!/usr/bin/env python3
"""Chuan hoa upload/target_appendix.md ve dang canonical cua skill (input contract).

File goc co 2 kieu khoi:
  Style A (Text 21-27):  | SL | TL | -> | **Text NN** | | -> title (bold) -> body
                         -> dong URL cuoi khoi.
  Style B (Text 28-40):  dong index | NN | (VI title) | [EN](url) | [VI](url) |
                         (so cot 3 hoac 4), roi bang | Eng | Vie | (hoac khong
                         co header), title, body. Khoi moi bat dau o dong index
                         so nguyen ke tiep.

Output: work_input/prepared_input.md, moi pair:
  ## Pair NN
  | en-url | vi-url |
  | :--- | :--- |
  | **EN title** | **VI title** |
  | body | body |

Day chi la buoc "repair row order / merged cells / escaping" cua SKILL.md §3
(input contract), KHONG sinh tie. Moi repair noi dung duoc ghi vao
work_input/repairs.json va phai duoc ghi lai o muc 8 cua phan tich pair tuong ung.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pipeline.common import is_separator, split_table_row  # noqa: E402

UNESCAPE_RE = re.compile(r"\\([\[\]{}()|*_$.!<>+\-#~`'\"\\])")
INDEX_RE = re.compile(r"^\d+$")
URL_RE = re.compile(r"\((https?://[^)]+)\)")
LINK_RE = re.compile(r"^\[[^\]]*\]\(https?://[^)]+\)$")


def unescape(cell: str) -> str:
    return UNESCAPE_RE.sub(r"\1", cell)


def is_url_cell(cell: str) -> bool:
    return bool(LINK_RE.match(cell.strip()))


def strip_bold(cell: str) -> str:
    c = cell.strip()
    if c.startswith("**") and c.endswith("**") and len(c) > 4:
        c = c[2:-2].strip()
    return c


def read_rows(path: Path):
    rows = []
    for ln, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line.startswith("|"):
            continue
        cells = split_table_row(line)
        if is_separator(cells):
            continue
        rows.append((ln, cells))
    return rows


def main() -> int:
    src = ROOT / "upload" / "target_appendix.md"
    rows = read_rows(src)

    pairs = []
    repairs = []
    cur = None
    expect = None  # 'label' | 'titleA' | 'bodyA' | 'titleB' | 'bodyB'
    notes_all = []

    def close_pair():
        nonlocal cur
        if cur is not None and cur.get("num") is not None:
            pairs.append(cur)
        cur = None

    for ln, cells in rows:
        first = cells[0].strip()

        # ---- dong index style B (so nguyen o cot 1) ----
        if INDEX_RE.match(first) and cur is None or (
                INDEX_RE.match(first) and cur is not None and cur["style"] == "B"):
            if INDEX_RE.match(first):
                close_pair()
                links = [c for c in cells[1:] if is_url_cell(c)]
                if len(links) < 2:
                    notes_all.append(f"line {ln}: index row chi co {len(links)} link")
                cur = {
                    "num": int(first), "style": "B",
                    "en_url": URL_RE.search(links[0]).group(1) if len(links) > 0 else "",
                    "vi_url": URL_RE.search(links[1]).group(1) if len(links) > 1 else "",
                    "body": [], "notes": [f"index row line {ln}"],
                }
                expect = "titleB"
                continue

        # ---- header SL|TL cua style A ----
        if len(cells) >= 2 and first.lower() == "sl" and cells[1].strip().lower() == "tl":
            close_pair()
            cur = {"style": "A", "body": [], "notes": [], "num": None}
            expect = "label"
            continue

        if cur is None:
            continue

        if expect == "label":
            m = re.fullmatch(r"\*\*Text (\d+)\*\*", first)
            if m:
                cur["num"] = int(m.group(1))
            else:
                cur["notes"].append(f"line {ln}: thieu dong label Text NN")
            expect = "titleA"
            continue

        if expect == "titleA":
            if is_url_cell(cells[0]) and is_url_cell(cells[1]):
                cur["notes"].append(f"line {ln}: pair style A khong co title")
                cur["_pending_title"] = ("", "")
            else:
                cur["_pending_title"] = (cells[0], cells[1])
            expect = "bodyA"
            continue

        if expect == "titleB":
            if len(cells) >= 2 and first.lower() == "eng" and cells[1].strip().lower() == "vie":
                continue  # header Eng|Vie, title o dong ke tiep
            cur["_pending_title"] = (cells[0], cells[1])
            expect = "bodyB"
            continue

        # ---- body style A: dong URL 2 cot -> ket thuc pair ----
        if expect == "bodyA" and len(cells) >= 2 and is_url_cell(cells[0]) and is_url_cell(cells[1]):
            cur["en_url"] = URL_RE.search(cells[0]).group(1)
            cur["vi_url"] = URL_RE.search(cells[1]).group(1)
            close_pair()
            continue

        # ---- body row thuong ----
        if len(cells) >= 2 and expect in ("bodyA", "bodyB"):
            cur["body"].append((ln, unescape(cells[0]), unescape(cells[1])))

    close_pair()

    # ---------------- repairs noi dung (log day du) ----------------
    def repair_cells(num, ln, en, vi):
        if num == 33 and en.strip().startswith("Mặc dù cái tên"):
            repairs.append({"pair": 33, "line": ln, "type": "swap_en_vi_columns",
                            "en_before": en[:90], "vi_before": vi[:90]})
            en, vi = vi, en
        if num == 29 and en.strip().startswith("**Giá tại các khu vực nông thôn**"):
            repairs.append({"pair": 29, "line": ln, "type": "swap_en_vi_columns",
                            "en_before": en[:90], "vi_before": vi[:90]})
            en, vi = vi, en
        for side, txt in (("en", en), ("vi", vi)):
            if "*,*" in txt:
                fixed = txt.replace("*,*", ",")
                repairs.append({"pair": num, "line": ln, "type": "fix_escape",
                                "side": side, "before": txt[:90], "after": fixed[:90]})
                if side == "en":
                    en = fixed
                else:
                    vi = fixed
        return en, vi

    out_dir = ROOT / "work_input"
    out_dir.mkdir(exist_ok=True)
    parts, stats = [], []
    for p in pairs:
        if p.get("num") is None or "_pending_title" not in p:
            notes_all.append(f"pair bi bo (num={p.get('num')}): "
                             f"{p['notes']}; {len(p['body'])} rows")
            continue
        num = p["num"]
        t_en, t_vi = p["_pending_title"]
        title_en, title_vi = unescape(strip_bold(t_en)), unescape(strip_bold(t_vi))
        body = []
        for ln, en, vi in p["body"]:
            en, vi = repair_cells(num, ln, en, vi)
            body.append((en, vi))
        parts.append(f"## Pair {num}")
        parts.append("")
        parts.append(f"| {p['en_url']} | {p['vi_url']} |")
        parts.append("| :--- | :--- |")
        parts.append(f"| **{title_en.replace('|', chr(92) + '|')}** | "
                     f"**{title_vi.replace('|', chr(92) + '|')}** |")
        for en, vi in body:
            parts.append(f"| {en.replace('|', chr(92) + '|')} | "
                         f"{vi.replace('|', chr(92) + '|')} |")
        parts.append("")
        stats.append({"num": num, "style": p["style"], "rows": len(body),
                      "title_en": title_en[:75],
                      "en_url": p["en_url"], "vi_url": p["vi_url"],
                      "notes": p["notes"]})

    (out_dir / "prepared_input.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    (out_dir / "pair_stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=1), encoding="utf-8")
    (out_dir / "repairs.json").write_text(
        json.dumps({"repairs": repairs, "notes": notes_all}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    for s in stats:
        print(f"Text {s['num']:02d} [{s['style']}] rows={s['rows']:3d} | {s['title_en']}")
    print(f"\nrepairs: {len(repairs)} | notes: {len(notes_all)}")
    for n in notes_all:
        print("  NOTE: " + n)
    print(f"Wrote {out_dir / 'prepared_input.md'}")
    return 0 if len(stats) == 20 else 1


if __name__ == "__main__":
    sys.exit(main())
