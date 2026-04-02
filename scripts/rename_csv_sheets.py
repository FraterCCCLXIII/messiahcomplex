#!/usr/bin/env python3
"""
Rename split-sheet CSVs to clean, content-based names.

Rules applied:
  1. Long workbook prefixes → short abbreviations (removes double-dash separator)
  2. Redundant words inherited from workbook name are stripped from the sheet slug
  3. Generic sheet names (Sheet9, Sheet29, …) → descriptive names inferred from content
  4. Empty files are moved to archive/ instead of being renamed in place

Run from the project root:
    python3 scripts/rename_csv_sheets.py static/sources/
"""

import os
import re
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Workbook prefix → short prefix
# ---------------------------------------------------------------------------
PREFIX_MAP: dict[str, str] = {
    "greek-philosophers-list--": "greek-phil-",
    "interpretatio-universalis-daimonologia--": "daimonologia-",
    "kosmographica-christodex-alpha--": "christodex-",
    "kosmographica-indexes-beta--": "kindex-",
    "kosmographica-vol-2--": "kvol2-",
}

# ---------------------------------------------------------------------------
# Redundant slug prefixes that duplicate the short workbook prefix
# e.g. "daimonologia-interpretatio-universalis-all" → "daimonologia-all"
# ---------------------------------------------------------------------------
SLUG_STRIP: dict[str, list[str]] = {
    "daimonologia-": ["interpretatio-universalis-"],
    "christodex-": [],
    "kindex-": [],
    "kvol2-": [],
    "greek-phil-": ["philosophers-"],
}

# ---------------------------------------------------------------------------
# Explicit renames: old filename → new filename (both without directory)
# Covers generic sheet names and other clean-ups.
# ---------------------------------------------------------------------------
EXPLICIT: dict[str, str] = {
    # --- Interpretatio Universalis / Daimonologia ---
    "daimonologia-all.csv":                             "daimonologia-all-traditions.csv",
    "daimonologia-sheet9.csv":                          "daimonologia-two-brothers-pie-table-a.csv",
    "daimonologia-sheet10.csv":                         "daimonologia-two-brothers-chart.csv",
    "daimonologia-sheet13.csv":                         "daimonologia-two-brothers-pie-table-b.csv",

    # --- Kosmographica Indexes BETA ---
    "kindex-sheet29.csv":                               "kindex-danube-region-timeline.csv",
    "kindex-roman-emporers.csv":                        "kindex-roman-emperors.csv",   # typo fix

    # --- Kosmographica Vol 2 ---
    "kvol2-52-bodhisattva-stages-avatamsak.csv":        "kvol2-52-bodhisattva-stages-avatamsaka.csv",
    "kvol2-sudhodhans-53-teachers-lamp-li.csv":         "kvol2-53-teachers-lamp-list.csv",
    "kvol2-nagarjuna-doctrines-mind-only-s.csv":        "kvol2-nagarjuna-doctrines-mind-only.csv",
    "kvol2-lotus-7-parables-compared-to-bi.csv":        "kvol2-lotus-7-parables-compared-bible.csv",
    "kvol2-sheet88.csv":                                "kvol2-shakya-saka-scythian-evidence.csv",
    "kvol2-sheet110.csv":                               "kvol2-draft-unproofed.csv",
    "kvol2-sheet112.csv":                               "kvol2-world-stories-and-creatures.csv",
    "kvol2-sheet115.csv":                               "kvol2-pelagios-network-resources.csv",
    "kvol2-sheet116.csv":                               "kvol2-celestial-rivers.csv",
    "kvol2-sheet118.csv":                               "_empty_sheet118.csv",           # will be archived
    "kvol2-sheet119.csv":                               "kvol2-buddhas-life-timeline.csv",
    "kvol2-sheet120.csv":                               "kvol2-workbook-index.csv",
    "kvol2-sheet121.csv":                               "kvol2-avestan-language-timeline.csv",
    "kvol2-sheet122.csv":                               "kvol2-ai-research-notes.csv",
    "kvol2-roman-cults-and-early-christian.csv":        "kvol2-roman-cults-early-christianity.csv",
    "kvol2-avestan-and-ancient-language-ti.csv":        "kvol2-avestan-ancient-language-timeline.csv",
    "kvol2-lotus-7-parables-compared-to-bi.csv":        "kvol2-lotus-7-parables-compared-bible.csv",
    "kvol2-yama-satan-devil-timeilne.csv":              "kvol2-yama-satan-devil-timeline.csv",  # typo fix
    "kvol2-floodbabel-myths.csv":                       "kvol2-flood-babel-myths.csv",
    "kvol2-alladinhidden-prince.csv":                   "kvol2-aladdin-hidden-prince.csv",
    "kvol2-phrygian-cap-ushnisha.csv":                  "kvol2-phrygian-cap-and-ushnisha.csv",
    "kvol2-healing-serpent-staff-pillar.csv":           "kvol2-healing-serpent-staff-and-pillar.csv",
    "kvol2-3-sisters-and-prince-fables.csv":            "kvol2-three-sisters-and-prince-fables.csv",

    # --- Christodex Alpha ---
    "christodex-timeline-of-judaism-and-christi.csv":   "christodex-judaism-christianity-timeline.csv",
    "christodex-life-and-places-of-jesus.csv":          "christodex-life-and-places-of-jesus.csv",
    "christodex-development-stage-theories-1.csv":      "christodex-development-stage-theories.csv",
    "christodex-roman-cults-and-early-christian.csv":   "christodex-roman-cults-early-christianity.csv",

    # --- Greek Philosophers ---
    "greek-phil-works.csv":                             "greek-phil-works-index.csv",
    "greek-phil-ai-enabled-list.csv":                   "greek-phil-ai-enabled-list.csv",
    "greek-phil-chatgpt-list.csv":                      "greek-phil-chatgpt-list.csv",
    "greek-phil-sheet4.csv":                            "greek-phil-supplemental.csv",
}

ARCHIVE_PREFIX = "_empty_"


def apply_prefix(name: str) -> str:
    """Replace long workbook prefix with short one and strip redundant slug words."""
    for long, short in PREFIX_MAP.items():
        if name.startswith(long):
            slug = name[len(long):]
            # strip redundant slug prefixes
            for strip in SLUG_STRIP.get(short, []):
                if slug.startswith(strip):
                    slug = slug[len(strip):]
            return short + slug
    return name


def clean(sources_dir: Path) -> None:
    archive_dir = sources_dir / "archive"
    archive_dir.mkdir(exist_ok=True)

    csv_files = sorted(p.name for p in sources_dir.glob("*.csv"))

    renamed = []
    archived = []
    skipped = []

    for original in csv_files:
        # skip files that don't match any workbook prefix
        if not any(original.startswith(long) for long in PREFIX_MAP):
            skipped.append(original)
            continue

        step1 = apply_prefix(original)
        new_name = EXPLICIT.get(step1, step1)

        src = sources_dir / original

        if new_name.startswith(ARCHIVE_PREFIX):
            dest = archive_dir / new_name.lstrip("_")
            shutil.move(str(src), str(dest))
            archived.append(f"  ARCHIVE  {original} → archive/{dest.name}")
            continue

        if new_name == original:
            skipped.append(original)
            continue

        dest = sources_dir / new_name
        if dest.exists():
            print(f"  CONFLICT  {new_name} already exists — skipping {original}")
            continue

        os.rename(src, dest)
        renamed.append(f"  {original}\n    → {new_name}")

    print(f"\n{'='*60}")
    print(f"Renamed  : {len(renamed)}")
    print(f"Archived : {len(archived)}")
    print(f"Unchanged: {len(skipped)}\n")

    for line in renamed:
        print(line)
    for line in archived:
        print(line)


def main():
    sources_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("static/sources")
    if not sources_dir.is_dir():
        print(f"Directory not found: {sources_dir}")
        sys.exit(1)
    clean(sources_dir)


if __name__ == "__main__":
    main()
