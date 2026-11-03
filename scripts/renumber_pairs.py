#!/usr/bin/env python3
"""Doi so pair P01..P20 -> P21..P40 (theo so Text cua nguon) va cap nhat meta.json.

Bay gio vi tri: thu muc work/pairs/PNN va truong num trong meta.json.
Day chi la bookkeeping (ten + so hieu hien thi), khong doi noi dung rows.
Chay 1 lan sau ingest, TRUOC segment/annotate.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work" / "pairs"


def main() -> int:
    srcs = sorted(p for p in WORK.iterdir() if p.is_dir() and p.name.startswith("P"))
    if not srcs:
        print("ERROR: khong co pair nao trong work/pairs")
        return 2
    nums = sorted(int(p.name[1:]) for p in srcs)
    if nums != list(range(1, len(nums) + 1)):
        print(f"ERROR: dang ky pair khong lien tu 1..{len(nums)}: {nums}")
        return 2
    n = len(nums)
    done = []
    for i, p in enumerate(srcs, 1):
        new_num = 20 + i
        new_dir = WORK / f"P{new_num:02d}"
        if new_dir.exists():
            print(f"ERROR: {new_dir} da ton tai (da renumber chua?)")
            return 2
        meta = json.loads((p / "meta.json").read_text(encoding="utf-8"))
        meta["id"] = f"P{new_num:02d}"
        meta["num"] = new_num
        (p / "meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        shutil.move(str(p), str(new_dir))
        done.append((p.name, new_dir.name))
    print(f"Renumbered {n} pairs: P01->P21 ... P{n:02d}->P{20 + n:02d}")
    for a, b in done:
        print(f"  {a} -> {b}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
