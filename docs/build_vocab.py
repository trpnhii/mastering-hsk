#!/usr/bin/env python3
"""Regenerate docs/vocab.json from Han1_Han2_Han3_tu_vung_gop.csv."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "Han1_Han2_Han3_tu_vung_gop.csv"
OUT_PATH = ROOT / "docs" / "vocab.json"


def main() -> None:
    rows = []
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
        for i, row in enumerate(csv.DictReader(f), 1):
            rows.append(
                {
                    "id": i,
                    "book": row["Sách"].strip(),
                    "lesson": row["Bài"].strip(),
                    "title": row["Tiêu đề"].strip(),
                    "hanzi": row["Hán tự"].strip(),
                    "pinyin": row["Pinyin"].strip(),
                    "meaning": row["Nghĩa"].strip(),
                }
            )
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(
        json.dumps(rows, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"Wrote {len(rows)} words -> {OUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
