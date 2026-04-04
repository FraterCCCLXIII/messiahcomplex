#!/usr/bin/env python3
"""
Strip workbook prefixes from all CSV filenames under static/sources/,
excluding archive/.

Prefixes removed: christodex-, kindex-, kvol2-, daimonologia-, greek-phil-

Conflicts (same new name in same dir) are resolved via EXPLICIT_RENAMES.

Run from project root:
    python3 scripts/strip_prefixes.py static/sources/
"""

import sys
from pathlib import Path

PREFIXES = ["christodex-", "kindex-", "kvol2-", "daimonologia-", "greek-phil-"]

# Explicit overrides for the 4 conflict files — keyed by their CURRENT name
EXPLICIT_RENAMES: dict[str, str] = {
    # messiah-prophets/: kvol2-bardiya wins "bardiya"; kindex-bardiya → bardiya-index
    "kindex-bardiya.csv":        "bardiya-index.csv",
    "kindex-bardiya-notes.csv":  "bardiya-index-notes.csv",
    # meta/: kvol2-indexes wins "indexes"; kindex-indexes → indexes-alt
    "kindex-indexes.csv":        "indexes-alt.csv",
    "kindex-indexes-notes.csv":  "indexes-alt-notes.csv",
}


def target_name(f: Path) -> str:
    if f.name in EXPLICIT_RENAMES:
        return EXPLICIT_RENAMES[f.name]
    for p in PREFIXES:
        if f.name.startswith(p):
            return f.name[len(p):]
    return f.name  # unchanged


def main():
    sources = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("static/sources")
    skip_dirs = {"archive"}

    all_csvs = sorted(
        p for p in sources.rglob("*.csv")
        if not any(part in skip_dirs for part in p.parts)
        and not p.name.startswith("_")
    )

    renamed, unchanged = [], []
    for f in all_csvs:
        new_name = target_name(f)
        if new_name == f.name:
            unchanged.append(f)
            continue
        dest = f.parent / new_name
        if dest.exists():
            print(f"  SKIP (dest exists): {f.relative_to(sources)} → {new_name}")
            continue
        f.rename(dest)
        renamed.append((f.relative_to(sources), new_name))

    print(f"Renamed  : {len(renamed)}")
    print(f"Unchanged: {len(unchanged)}")
    for old, new in renamed:
        print(f"  {str(old):<75} → {new}")


if __name__ == "__main__":
    main()
