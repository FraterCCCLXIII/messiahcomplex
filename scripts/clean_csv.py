#!/usr/bin/env python3
"""
Phase 4: Clean every CSV under a directory tree:
  1. Strip trailing all-empty columns (e.g. 26-col Christodex schema padding)
  2. Extract single-cell note rows into a <name>-notes.csv sidecar
  3. Rewrite the data file with only true data rows

A row is a "note row" when:
  - Only col[0] is non-empty, AND
  - The row is NOT the very first row (which may be a section title / header)

Run from project root:
    python3 scripts/clean_csv.py static/sources/
"""

import csv
import sys
from pathlib import Path


def is_blank(row: list[str]) -> bool:
    return all(c.strip() == "" for c in row)


def is_note(row: list[str]) -> bool:
    filled = [c for c in row if c.strip()]
    return len(filled) == 1 and row[0].strip() != ""


def trim_cols(rows: list[list[str]]) -> list[list[str]]:
    """Remove trailing columns that are empty in every row."""
    if not rows:
        return rows
    max_cols = max(len(r) for r in rows)
    last_used = 0
    for r in rows:
        for i, cell in enumerate(r):
            if cell.strip():
                last_used = max(last_used, i)
    width = last_used + 1
    return [r[:width] + [""] * max(0, width - len(r)) for r in rows]


def clean_file(path: Path) -> dict:
    try:
        with path.open(newline="", encoding="utf-8-sig") as fh:
            rows = list(csv.reader(fh))
    except Exception as e:
        return {"path": path, "error": str(e)}

    if not rows:
        return {"path": path, "skipped": "empty"}

    original_cols = max((len(r) for r in rows), default=0)

    # Separate header (row 0), blank rows, note rows, data rows
    header = rows[0]
    rest = rows[1:]

    data_rows = []
    note_rows = []
    for r in rest:
        if is_blank(r):
            continue  # drop blank rows from data file; they'll be absent from notes too
        elif is_note(r):
            note_rows.append(r)
        else:
            data_rows.append(r)

    # Trim columns on the combined set
    combined = trim_cols([header] + data_rows)
    final_cols = max((len(r) for r in combined), default=0)

    # Only rewrite if something changed
    cols_stripped = original_cols - final_cols
    changed = cols_stripped > 0 or len(note_rows) > 0

    if not changed:
        return {"path": path, "skipped": "already_clean"}

    # Write cleaned data file
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerows(combined)

    result = {
        "path": path,
        "original_cols": original_cols,
        "final_cols": final_cols,
        "cols_stripped": cols_stripped,
        "notes_extracted": len(note_rows),
    }

    # Write notes sidecar if there are note rows
    if note_rows:
        notes_path = path.parent / (path.stem + "-notes.csv")
        with notes_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerows(note_rows)
        result["notes_path"] = notes_path

    return result


def main():
    sources = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("static/sources")
    if not sources.is_dir():
        print(f"Not found: {sources}")
        sys.exit(1)

    # Skip archive, ai-revisions, and notes sidecars (avoid double-processing)
    skip_dirs = {"archive", "ai-notes", "ai-revisions"}
    all_csvs = [
        p for p in sources.rglob("*.csv")
        if not any(part in skip_dirs for part in p.parts)
        and not p.stem.endswith("-notes")
        and not p.name.startswith("_")
    ]

    cleaned, skipped, errors = [], [], []

    for csv_path in sorted(all_csvs):
        result = clean_file(csv_path)
        if "error" in result:
            errors.append(f"  ERROR {csv_path.relative_to(sources)}: {result['error']}")
        elif result.get("skipped"):
            skipped.append(csv_path.relative_to(sources))
        else:
            rel = csv_path.relative_to(sources)
            parts = []
            if result.get("cols_stripped", 0) > 0:
                parts.append(f"-{result['cols_stripped']}cols")
            if result.get("notes_extracted", 0) > 0:
                parts.append(f"+{result['notes_extracted']}notes→{result['notes_path'].name}")
            cleaned.append(f"  {str(rel):<65} {' '.join(parts)}")

    print(f"\n{'='*60}")
    print(f"Cleaned : {len(cleaned)}")
    print(f"Skipped : {len(skipped)} (already clean)")
    print(f"Errors  : {len(errors)}")
    print(f"\n--- CLEANED ---")
    for line in cleaned:
        print(line)
    for line in errors:
        print(line)


if __name__ == "__main__":
    main()
