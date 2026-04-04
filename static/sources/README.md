# static/sources — Data Files

CSV data supporting the Messiah Complex documentation site.
Files are served at `/sources/<family>/<name>.csv` by Docusaurus static hosting.

---

## Directory structure

```
static/sources/
├── abrahamic/          # Jewish, Christian, Islamic texts, timelines, figures
├── buddhism-dharma/    # Buddhism, dharma numbers, sutras, schools, meditation
├── comparative-myths/  # Cross-cultural myths, PIE parallels, angels/demons
├── esoteric/           # Tantra, hermeticism, freemasonry, nonduality, DST
├── hellenic/           # Greek philosophy, Apollo, Dionysus, Flavians
├── messiah-prophets/   # Bardiya, Buddha, prophets, Apollonius, messianic timelines
├── meta/               # Indexes, workbook maps, AI research notes
├── military-political/ # Roman/Jewish battles, empires, political history
├── mystery-cults/      # Mithras, Gnostics, inquisitions, cults, saints
├── persian-achaemenid/ # Achaemenid dynasty, Saka/Scythian, Avestan, Persian battles
├── pie-origins/        # Proto-Indo-European myths, Two Brothers, Turanians, Tuscans
└── archive/            # Historical versions and irrelevant files (not served)
    └── irrelevant/     # Vampire, witch-trial, and other off-topic files
```

---

## File count by family

| Family | Primary CSVs | Notes sidecars |
|---|---:|---:|
| `abrahamic/` | 36 | 19 |
| `buddhism-dharma/` | 27 | 20 |
| `comparative-myths/` | 25 | 21 |
| `esoteric/` | 13 | 9 |
| `hellenic/` | 13 | 6 |
| `messiah-prophets/` | 19 | 12 |
| `meta/` | 8 | 7 |
| `military-political/` | 9 | 6 |
| `mystery-cults/` | 15 | 5 |
| `persian-achaemenid/` | 18 | 18 |
| `pie-origins/` | 24 | 13 |
| **Total** | **207** | **136** |

---

## Naming conventions

- **Primary files**: `<workbook-abbrev>-<content-slug>.csv`
  - `christodex-` → Christodex workbook
  - `kindex-` → Kosmographica Index workbook
  - `kvol2-` → Kosmographica Vol 2 workbook
  - `daimonologia-` → Interpretatio Universalis – Daimonologia workbook
  - `greek-phil-` → Greek Philosophers List workbook
- **Notes sidecars**: `<name>-notes.csv` — single-column prose rows extracted from the primary file during cleaning; kept for reference, not tabular data.
- **Dropped-dupes sidecars**: `<name>-dropped-dupes.csv` — rows removed during a merge deduplication pass.
- **ai-revisions/**: subdirectory holding earlier AI draft iterations of a file (not canonical data).
- **ai-notes/**: subdirectory holding raw AI conversation dumps (not structured tables).

---

## Referencing files in MDX

```jsx
import { CsvTable } from '@site/src/components/CsvTable';

<CsvTable
  src="/sources/messiah-prophets/bardiya-timeline.csv"
  caption="Achaemenid / Bardiya timeline."
/>
```

---

## Source workbooks

These `.xlsx` originals are in `archive/` after being split into individual CSV sheets:

| Abbreviation | Original workbook |
|---|---|
| `christodex-` | Kosmographica - Christodex (Alpha) - DST 2.xlsx |
| `kindex-` | Kosmographica Indexes BETA.xlsx |
| `kvol2-` | Kosmographica Vol 2.xlsx |
| `daimonologia-` | Interpretatio Universalis Daimonologia.xlsx |
| `greek-phil-` | Greek Philosophers List.xlsx |

---

## Data quality

All primary CSV files have been through a cleaning pass:
- Trailing all-empty columns stripped
- Prose note rows moved to `-notes.csv` sidecars
- Blank rows removed
- Multi-table files split into individual files (one logical table per file)

Files under `ai-revisions/` and `ai-notes/` are **uncleaned AI conversation outputs**
and should be treated as raw leads, not verified data.
