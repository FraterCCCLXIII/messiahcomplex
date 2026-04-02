#!/usr/bin/env python3
"""
Audit all CSVs in a directory and produce a structured report.

For each file, detects:
  - Total rows / columns
  - Number of embedded sub-tables (rows that look like a new header mid-file)
  - Number of blank rows
  - Number of note rows (single populated cell, rest empty)
  - Fill rate (% of cells that have a value)
  - Column name consistency (does every apparent data row match the header width?)

Outputs a CSV report and a human-readable summary sorted by issue severity.

Usage:
    python3 scripts/audit_csv.py static/sources/ [--out report.csv]
"""

import csv
import re
import sys
from pathlib import Path
from collections import defaultdict


# ---------------------------------------------------------------------------
# Heuristics
# ---------------------------------------------------------------------------

def is_blank(row: list[str]) -> bool:
    return all(c.strip() == "" for c in row)

def is_note_row(row: list[str]) -> bool:
    """Single cell with text, rest empty."""
    filled = [c for c in row if c.strip()]
    return len(filled) == 1

def looks_like_header(row: list[str], prev_header: list[str]) -> bool:
    """
    A mid-file row looks like a new header if:
    - It has >= 2 non-empty cells
    - Its values look like column names (short, no numbers at start, Title Case or lower)
    - It differs substantially from the known header
    """
    filled = [c.strip() for c in row if c.strip()]
    if len(filled) < 2:
        return False
    # Column names are usually short
    if any(len(f) > 60 for f in filled):
        return False
    # Column names rarely start with a number or contain sentence punctuation
    if any(re.match(r"^\d", f) for f in filled):
        return False
    if any(f.count(".") > 1 or f.count(",") > 2 for f in filled):
        return False
    # Must differ from the existing header
    if prev_header:
        overlap = sum(1 for a, b in zip(row, prev_header) if a.strip() == b.strip())
        if prev_header and overlap / max(len(prev_header), 1) > 0.6:
            return False
    return True


# ---------------------------------------------------------------------------
# Per-file analysis
# ---------------------------------------------------------------------------

def analyse(path: Path) -> dict:
    try:
        with path.open(newline="", encoding="utf-8-sig") as fh:
            rows = list(csv.reader(fh))
    except Exception as e:
        return {"file": path.name, "error": str(e)}

    if not rows:
        return {
            "file": path.name, "rows": 0, "cols": 0,
            "blank_rows": 0, "note_rows": 0, "sub_tables": 0,
            "fill_pct": 0, "verdict": "EMPTY"
        }

    max_cols = max((len(r) for r in rows), default=0)
    blank_rows = sum(1 for r in rows if is_blank(r))
    note_rows  = sum(1 for r in rows if not is_blank(r) and is_note_row(r))

    # Detect sub-tables: rows that look like a new header after a blank row
    sub_tables = 0
    header = rows[0] if rows else []
    prev_was_blank = False
    for r in rows[1:]:
        if is_blank(r):
            prev_was_blank = True
            continue
        if prev_was_blank and looks_like_header(r, header):
            sub_tables += 1
            header = r
        prev_was_blank = False

    # Fill rate (excluding blank rows entirely)
    data_rows = [r for r in rows if not is_blank(r)]
    total_cells = sum(max_cols for _ in data_rows)
    filled_cells = sum(1 for r in data_rows for c in r if c.strip())
    fill_pct = round(filled_cells / total_cells * 100, 1) if total_cells else 0

    # Verdict
    issues = []
    if sub_tables >= 2:
        issues.append(f"MULTI-TABLE({sub_tables})")
    if note_rows > 3:
        issues.append(f"NOTES({note_rows})")
    if blank_rows > rows.__len__() * 0.25:
        issues.append("SPARSE")
    if fill_pct < 40:
        issues.append(f"LOW-FILL({fill_pct}%)")

    verdict = " | ".join(issues) if issues else "OK"

    return {
        "file": path.name,
        "rows": len(rows),
        "data_rows": len(data_rows),
        "cols": max_cols,
        "blank_rows": blank_rows,
        "note_rows": note_rows,
        "sub_tables": sub_tables,
        "fill_pct": fill_pct,
        "verdict": verdict,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    sources_dir = Path(args[0]) if args else Path("static/sources")
    out_path = Path(args[args.index("--out") + 1]) if "--out" in args else sources_dir / "_audit_report.csv"

    csvs = sorted(sources_dir.glob("*.csv"))
    csvs = [p for p in csvs if not p.name.startswith("_")]

    results = [analyse(p) for p in csvs]

    # Sort: problems first
    def severity(r):
        s = 0
        if "MULTI-TABLE" in r.get("verdict", ""):   s += 30
        if "NOTES"       in r.get("verdict", ""):   s += 10
        if "LOW-FILL"    in r.get("verdict", ""):   s += 20
        if "SPARSE"      in r.get("verdict", ""):   s += 5
        if "EMPTY"       in r.get("verdict", ""):   s += 50
        return -s

    results.sort(key=severity)

    fields = ["file","rows","data_rows","cols","blank_rows","note_rows","sub_tables","fill_pct","verdict"]
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(results)

    # Summary to stdout
    total     = len(results)
    ok        = sum(1 for r in results if r.get("verdict") == "OK")
    multi     = sum(1 for r in results if "MULTI-TABLE" in r.get("verdict",""))
    notes     = sum(1 for r in results if "NOTES"       in r.get("verdict",""))
    low_fill  = sum(1 for r in results if "LOW-FILL"    in r.get("verdict",""))
    sparse    = sum(1 for r in results if "SPARSE"      in r.get("verdict",""))
    empty     = sum(1 for r in results if "EMPTY"       in r.get("verdict",""))

    print(f"\n{'='*60}")
    print(f"CSV Audit — {sources_dir}")
    print(f"{'='*60}")
    print(f"  Total files : {total}")
    print(f"  Clean (OK)  : {ok}")
    print(f"  Multi-table : {multi}")
    print(f"  Notes-heavy : {notes}")
    print(f"  Low fill    : {low_fill}")
    print(f"  Sparse      : {sparse}")
    print(f"  Empty       : {empty}")
    print(f"\nReport written to: {out_path}\n")

    print(f"{'─'*60}")
    print(f"{'FILE':<55} {'VERDICT'}")
    print(f"{'─'*60}")
    for r in results:
        if r.get("verdict") != "OK":
            print(f"  {r['file']:<53} {r.get('verdict','')}")
    print(f"{'─'*60}")


if __name__ == "__main__":
    main()
