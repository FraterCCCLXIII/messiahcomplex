#!/usr/bin/env python3
"""
Phases 1 & 2: Create taxonomy subdirectories, move CSVs into families,
archive irrelevant files, delete the empty file.

Run from project root:
    python3 scripts/organize_sources.py static/sources/
"""

import shutil
import sys
from pathlib import Path

FAMILIES: dict[str, list[str]] = {
    "messiah-prophets": [
        "bardiya-timeline",
        "kvol2-bardiya",
        "kvol2-bardiya-2",
        "kindex-bardiya",
        "kindex-bardiya-notes",
        "kvol2-buddha-jesus-bardiya-table",
        "kvol2-biblical-messiahs",
        "kvol2-all-prophets",
        "kvol2-zoroastrian-prophets",
        "christodex-prophets",
        "kvol2-apollonius-of-tyana",
        "kvol2-mithras-maitreya",
        "kvol2-maitreya-timeline",
        "kvol2-bard-prophet-list",
        "kvol2-historical-problems-of-prophets",
        "kvol2-sudhodhana",
        "kvol2-prophet-visions",
        "kvol2-bible-prophet-and-villains",
        "kvol2-vision-motifs",
    ],
    "pie-origins": [
        "kvol2-pie-myths",
        "daimonologia-all-traditions",
        "daimonologia-pie-comparisons",
        "daimonologia-pie-2",
        "daimonologia-primordial-man",
        "daimonologia-ages",
        "daimonologia-two-brothers-chart",
        "daimonologia-two-brothers-pie-table-a",
        "daimonologia-two-brothers-pie-table-b",
        "kvol2-two-brothers",
        "kvol2-divine-twins",
        "kvol2-dyads-triads-more",
        "kvol2-core-myths",
        "kvol2-flood-babel-myths",
        "daimonologia-celestial-pairs",
        "daimonologia-giants",
        "daimonologia-realms",
        "daimonologia-americas",
        "daimonologia-cult-timeline",
        "kvol2-phrygian-cap-and-ushnisha",
        "kindex-turans-and-danavas",
        "daimonologia-sources",
    ],
    "mystery-cults": [
        "kvol2-mithras-timeline",
        "kvol2-mithras-2",
        "kvol2-mithras-in-bible",
        "kvol2-mystery-ritual",
        "kindex-roman-cults-and-early-christian",
        "kvol2-eurasian-cult-timeline",
        "kvol2-steppe-cult-timeline",
        "christodex-inquisitions",
        "kindex-inquisitions",
        "kindex-tenet-systems",
        "kindex-saint-collections",
        "kindex-semitic-saints",
        "christodex-gods-of-light",
        "christodex-variations-index",
        "christodex-heresies",
        "christodex-schisms",
    ],
    "buddhism-dharma": [
        "kvol2-dharma-numbers",
        "kvol2-dharma-numbers-2",
        "kvol2-52-bodhisattva-stages-avatamsaka",
        "kvol2-avatamsaka-sutra",
        "kvol2-avatamsaka-sutra-contents",
        "kvol2-48-vows-of-amitabha",
        "kvol2-lamps-of-dzogchen",
        "kvol2-227-patimokkha",
        "kvol2-7-halls-of-hekhalot",
        "kvol2-hekhalot",
        "kvol2-hekhalot-stages",
        "kvol2-53-teachers-lamp-list",
        "kvol2-nagarjuna-doctrines-mind-only",
        "kvol2-early-buddhist-schools",
        "kvol2-east-asian-buddhist-schools",
        "kvol2-buddhist-schools",
        "kvol2-buddhist-hindu-tables",
        "kvol2-buddhas-life-timeline",
        "kvol2-buddhas-life-in-parables",
        "kvol2-meditation-timeline",
        "kvol2-dream-yogas",
        "kvol2-lucid-dreaming",
        "kvol2-dream-sleep-and-darkness",
        "kindex-past-buddhas",
        "kvol2-lotus-sutra",
        "kvol2-lotus-7-parables-compared-bible",
        "kvol2-muslim-illuminationism",
    ],
    "persian-achaemenid": [
        "kvol2-saka-scythian-timeline",
        "kvol2-saka-scythian",
        "kvol2-saka-religion",
        "kvol2-shakya-saka-scythian-evidence",
        "kvol2-achaemenid-kings",
        "kvol2-achaemenid-dynasty",
        "kindex-persian-battles",
        "kindex-mithridates",
        "kvol2-avestan-language-timeline",
        "kvol2-avestan-ancient-language-timeline",
        "kvol2-zor-gods",
        "kvol2-aramaic-timeline",
        "kvol2-beckwith-notes",
        "kvol2-seljuks",
        "kindex-crimean-tartars",
        "kindex-tartaria",
        "kvol2-civilization-timeline",
    ],
    "abrahamic": [
        "kvol2-613-mitzvot",
        "kvol2-jewish-practices",
        "kvol2-jewish-hellenization-timeline",
        "kvol2-contemporary-jewish-leaders",
        "kvol2-bible-figures",
        "kvol2-bible-tables",
        "kvol2-bible-lights",
        "kvol2-biblical-law-timeline",
        "kvol2-all-bible-and-medieval-parables",
        "kvol2-all-bible-visions",
        "kvol2-72-angels",
        "kindex-apocrypha",
        "kindex-apocrypha-2",
        "christodex-apocryphon",
        "christodex-biblical-prophecies",
        "christodex-biblical-textual-history",
        "christodex-canon",
        "christodex-judaism-christianity-timeline",
        "christodex-early-church-fathers",
        "christodex-early-religion-timeline",
        "christodex-all-christian-sects",
        "christodex-alt-authors",
        "christodex-life-and-places-of-jesus",
        "christodex-life-of-paul",
        "christodex-roman-emperors",
        "kindex-early-church",
        "kindex-early-christians",
        "kindex-hellenic-judaism-timeline",
        "kindex-jewish-battles",
        "kvol2-jesus-life-parables",
        "kvol2-koran-tables",
        "kvol2-islam-tables",
        "christodex-muslim-texts",
        "christodex-muslim-names-of-god",
        "kvol2-sibylline-oracles",
        "kvol2-biblical-parables",
    ],
    "hellenic": [
        "greek-phil-ai-enabled-list",
        "greek-phil-chatgpt-list",
        "greek-phil-female-philosophers",
        "greek-phil-supplemental",
        "greek-phil-works-index",
        "kvol2-apollo-timeline",
        "kvol2-dionysus-timeline",
        "kvol2-pan-timeline",
        "kvol2-hellenic-hymns",
        "kvol2-all-greek-texts",
        "kvol2-petosyris-and-hermeticism",
        "kvol2-dionysus-christ-parallels",
        "kvol2-flavians",
    ],
    "comparative-myths": [
        "kvol2-fables-and-myths",
        "kvol2-world-stories-and-creatures",
        "kvol2-three-sisters-and-prince-fables",
        "kvol2-aladdin-hidden-prince",
        "kvol2-comparison-table",
        "kvol2-christian-comparison-tables",
        "kvol2-serpent-deities",
        "kvol2-nagas",
        "kvol2-healing-serpent-staff-and-pillar",
        "kvol2-tree-of-life",
        "kvol2-celestial-rivers",
        "kvol2-elements-timeline",
        "kvol2-demons-and-angels",
        "kvol2-baal-cycle",
        "kvol2-yama-satan-devil-timeline",
        "kvol2-golden-chain",
        "kvol2-temples",
        "kvol2-sacred-text-indexes",
    ],
    "esoteric": [
        "kvol2-tantric-traditions-timeline",
        "kvol2-tantric-lineages",
        "kvol2-tantric-practice-index",
        "kvol2-tantric-sex-index",
        "kvol2-sex-rites-timeline",
        "kindex-freemasonry",
        "kindex-fraternal-orders",
        "kindex-sacred-architecture",
        "kindex-magic-and-necromancy",
        "kindex-hermetic-texts",
        "kvol2-nonduality-development-timeline",
        "christodex-dst-2",
        "christodex-development-stage-theories",
    ],
    "military-political": [
        "kindex-roman-battles",
        "kindex-jewish-battles",
        "kindex-england",
        "kindex-brennus",
        "kvol2-mixed-timeline",
        "kindex-wallachia",
        "kindex-roman-emperors",
        "kindex-master",
        "kindex-schools",
        "kindex-east-asian-ancestors",
    ],
    "meta": [
        "kvol2-workbook-index",
        "kvol2-indexes",
        "kindex-indexes",
        "kvol2-draft-unproofed",
        "kvol2-ai-research-notes",
        "kvol2-pelagios-network-resources",
        "kindex-sources",
        "christodex-introduction",
        "christodex-critical-theory",
        "christodex-large-time-scales",
    ],
}

ARCHIVE_IRRELEVANT = [
    "christodex-vampire-history",
    "kindex-vampire-history",
    "christodex-witch-trials",
    "kindex-witches",
]

DELETE = [
    "kvol2-thracian-horseman",
]


def build_assignment(families: dict[str, list[str]]) -> dict[str, str]:
    assignment: dict[str, str] = {}
    for family, stems in families.items():
        for stem in stems:
            if stem not in assignment:
                assignment[stem] = family
    return assignment


def main():
    sources = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("static/sources")
    if not sources.is_dir():
        print(f"Not found: {sources}")
        sys.exit(1)

    for family in FAMILIES:
        (sources / family).mkdir(exist_ok=True)
    (sources / "archive" / "irrelevant").mkdir(parents=True, exist_ok=True)

    assignment = build_assignment(FAMILIES)
    moved, archived, deleted, unassigned = [], [], [], []

    for csv in sorted(sources.glob("*.csv")):
        stem = csv.stem
        if stem.startswith("_"):
            continue

        if stem in DELETE:
            csv.unlink()
            deleted.append(csv.name)
            continue

        if stem in ARCHIVE_IRRELEVANT:
            dest = sources / "archive" / "irrelevant" / csv.name
            shutil.move(str(csv), str(dest))
            archived.append(f"  {csv.name} → archive/irrelevant/")
            continue

        if stem in assignment:
            family = assignment[stem]
            dest = sources / family / csv.name
            shutil.move(str(csv), str(dest))
            moved.append(f"  {csv.name:<60} → {family}/")
        else:
            unassigned.append(csv.name)

    print(f"\n{'='*60}")
    print(f"Moved     : {len(moved)}")
    print(f"Archived  : {len(archived)}")
    print(f"Deleted   : {len(deleted)}")
    print(f"Unassigned: {len(unassigned)}")

    if unassigned:
        print(f"\n--- UNASSIGNED (still in sources/ root) ---")
        for f in unassigned:
            print(f"  {f}")

    print(f"\n--- MOVED ---")
    for line in moved:
        print(line)
    for line in archived:
        print(line)
    for f in deleted:
        print(f"  DELETED: {f}")


if __name__ == "__main__":
    main()
