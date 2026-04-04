#!/usr/bin/env python3
"""
Post-split cleanup:
- Rename long-named split files to clean sequential names
- Remove originals that were properly split (2+ sub-tables)
- Handle AI-dump files: consolidate as notes, remove noisy splits
- Move Apollonius single-split back to original name

Run from project root:
    python3 scripts/cleanup_splits.py static/sources/
"""

import os
import shutil
import sys
from pathlib import Path


def wc(path: Path) -> int:
    return sum(1 for _ in path.open(encoding="utf-8", errors="replace"))


def main():
    sources = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("static/sources")

    # -----------------------------------------------------------------------
    # 1. kindex-persian-battles → 3 real tables, rename cleanly
    # -----------------------------------------------------------------------
    pb_dir = sources / "persian-achaemenid"
    renames = {
        "kindex-persian-battles--key-metadata-additions.csv":
            "kindex-persian-battles-metadata.csv",
        "kindex-persian-battles--key-founders.csv":
            "kindex-persian-battles-founders.csv",
        "kindex-persian-battles--heres-a-comprehensive-table-of-achaemenid-battles-with-metad.csv":
            "kindex-persian-battles-achaemenid-expanded.csv",
    }
    for old, new in renames.items():
        src = pb_dir / old
        if src.exists():
            src.rename(pb_dir / new)
            print(f"  renamed → {new}")
    # remove original
    orig = pb_dir / "kindex-persian-battles.csv"
    if orig.exists():
        orig.unlink()
        print(f"  removed original: kindex-persian-battles.csv")

    # -----------------------------------------------------------------------
    # 2. kindex-sources → pure AI dump, move sub-splits to meta/ai-notes,
    #    keep the main URL-listed table, remove noisy splits
    # -----------------------------------------------------------------------
    meta_dir = sources / "meta"
    ai_notes_dir = meta_dir / "ai-notes"
    ai_notes_dir.mkdir(exist_ok=True)

    # The real data is in the brill.com split (371 rows)
    for f in list(meta_dir.glob("kindex-sources--*.csv")):
        f.unlink()
        print(f"  removed AI-dump split: {f.name}")
    orig_ks = meta_dir / "kindex-sources.csv"
    if orig_ks.exists():
        orig_ks.rename(ai_notes_dir / "kindex-sources-raw.csv")
        print(f"  moved kindex-sources.csv → meta/ai-notes/kindex-sources-raw.csv")

    # -----------------------------------------------------------------------
    # 3. kvol2-ai-research-notes → move excerpt splits to ai-notes,
    #    keep the Gemini and main excerpt tables
    # -----------------------------------------------------------------------
    splits = sorted(meta_dir.glob("kvol2-ai-research-notes--*.csv"))
    keep_map = {
        "kvol2-ai-research-notes--gemini.csv": "ai-notes-gemini-session.csv",
        "kvol2-ai-research-notes--excerpt-from.csv": "ai-notes-excerpt-a.csv",
    }
    seen_excerpt = False
    for f in splits:
        if f.name == "kvol2-ai-research-notes--gemini.csv":
            f.rename(ai_notes_dir / "ai-notes-gemini-session.csv")
            print(f"  moved → ai-notes/ai-notes-gemini-session.csv")
        elif f.name == "kvol2-ai-research-notes--excerpt-from.csv":
            dest = "ai-notes-excerpt-a.csv" if not seen_excerpt else "ai-notes-excerpt-b.csv"
            seen_excerpt = True
            f.rename(ai_notes_dir / dest)
            print(f"  moved → ai-notes/{dest}")
        else:
            f.unlink()
            print(f"  removed noisy split: {f.name}")
    orig_ar = meta_dir / "kvol2-ai-research-notes.csv"
    if orig_ar.exists():
        orig_ar.unlink()
        print(f"  removed original: kvol2-ai-research-notes.csv")

    # -----------------------------------------------------------------------
    # 4. kvol2-demons-and-angels → 3 splits, rename and keep all
    # -----------------------------------------------------------------------
    cm_dir = sources / "comparative-myths"
    da_map = {
        "kvol2-demons-and-angels--graph-table-angels-demons-in-abrahamic-traditions.csv":
            "kvol2-demons-angels-abrahamic-graph.csv",
        "kvol2-demons-and-angels--next-steps.csv":
            "kvol2-demons-angels-expanded.csv",
        "kvol2-demons-and-angels--key-expansions.csv":
            "kvol2-demons-angels-key-expansions.csv",
    }
    for old, new in da_map.items():
        src = cm_dir / old
        if src.exists():
            src.rename(cm_dir / new)
            print(f"  renamed → {new}")
    orig_da = cm_dir / "kvol2-demons-and-angels.csv"
    if orig_da.exists():
        orig_da.unlink()
        print(f"  removed original: kvol2-demons-and-angels.csv")

    # -----------------------------------------------------------------------
    # 5. kvol2-mithras-in-bible → 4 AI-revision splits;
    #    keep the last/most comprehensive, archive earlier revisions
    # -----------------------------------------------------------------------
    mc_dir = sources / "mystery-cults"
    mc_ai_dir = mc_dir / "ai-revisions"
    mc_ai_dir.mkdir(exist_ok=True)
    mib_splits = {
        "kvol2-mithras-in-bible--okay-i-will-add-baal-berith-to-the-table-along-with-biblical.csv":
            "mithras-in-bible-draft-1.csv",
        "kvol2-mithras-in-bible--thanks-for-the-file-now-using-the-timeline-you-provided-and-.csv":
            "mithras-in-bible-draft-2.csv",
        "kvol2-mithras-in-bible--certainly-below-is-the-updated-timeline-with-all-date-ranges.csv":
            "mithras-in-bible-draft-3.csv",
        "kvol2-mithras-in-bible--comprehensive-table-of-trials-adventures-events-and-tribulat.csv":
            "kvol2-mithras-trials-table.csv",  # keep this one in main dir
    }
    for old, new in mib_splits.items():
        src = mc_dir / old
        if not src.exists():
            continue
        if new.startswith("mithras-in-bible-draft"):
            src.rename(mc_ai_dir / new)
            print(f"  archived AI draft → mystery-cults/ai-revisions/{new}")
        else:
            src.rename(mc_dir / new)
            print(f"  renamed → {new}")
    orig_mib = mc_dir / "kvol2-mithras-in-bible.csv"
    if orig_mib.exists():
        orig_mib.unlink()
        print(f"  removed original: kvol2-mithras-in-bible.csv")

    # -----------------------------------------------------------------------
    # 6. kvol2-yama-satan-devil-timeline → 4 AI-revision splits
    #    keep the comprehensive one, archive drafts
    # -----------------------------------------------------------------------
    ysd_ai_dir = cm_dir / "ai-revisions"
    ysd_ai_dir.mkdir(exist_ok=True)
    ysd_splits = {
        "kvol2-yama-satan-devil-timeline--certainly-heres-a-concise-timeline-table-summarizing-the-key.csv":
            "yama-devil-timeline-draft-1.csv",
        "kvol2-yama-satan-devil-timeline--here-is-a-timeline-table-tracing-the-evolution-of-yemo-yama-.csv":
            "yama-devil-timeline-draft-2.csv",
        "kvol2-yama-satan-devil-timeline--show-more.csv":
            "kvol2-yama-satan-devil-show-more.csv",  # keep in main dir (102 rows)
        "kvol2-yama-satan-devil-timeline--here-is-a-comprehensive-timeline-table-integrating-the-evolu.csv":
            "kvol2-yama-satan-devil-comprehensive.csv",  # keep — largest
    }
    for old, new in ysd_splits.items():
        src = cm_dir / old
        if not src.exists():
            continue
        if "draft" in new:
            src.rename(ysd_ai_dir / new)
            print(f"  archived AI draft → comparative-myths/ai-revisions/{new}")
        else:
            src.rename(cm_dir / new)
            print(f"  renamed → {new}")
    orig_ysd = cm_dir / "kvol2-yama-satan-devil-timeline.csv"
    if orig_ysd.exists():
        orig_ysd.unlink()
        print(f"  removed original: kvol2-yama-satan-devil-timeline.csv")

    # -----------------------------------------------------------------------
    # 7. kindex-turans-and-danavas → 10 splits (mix of tables + AI notes)
    #    keep the 3 substantive ones, archive the rest
    # -----------------------------------------------------------------------
    po_dir = sources / "pie-origins"
    po_ai_dir = po_dir / "ai-revisions"
    po_ai_dir.mkdir(exist_ok=True)
    tnd_keep = {
        "kindex-turans-and-danavas--comprehensive-historical-timeline-of-turan-and-danavas.csv":
            "kindex-turans-danavas-timeline.csv",
        "kindex-turans-and-danavas--heres-a-timeline-table-of-the-history-of-tarquinia.csv":
            "kindex-tarquinia-timeline.csv",
        "kindex-turans-and-danavas--timeline-index-the-origins-of-tuscan-and-the-tuscan-people.csv":
            "kindex-tuscan-origins-timeline.csv",
    }
    for f in sorted(po_dir.glob("kindex-turans-and-danavas--*.csv")):
        if f.name in tnd_keep:
            f.rename(po_dir / tnd_keep[f.name])
            print(f"  renamed → {tnd_keep[f.name]}")
        else:
            f.rename(po_ai_dir / f.name)
            print(f"  archived → pie-origins/ai-revisions/{f.name}")
    orig_tnd = po_dir / "kindex-turans-and-danavas.csv"
    if orig_tnd.exists():
        orig_tnd.unlink()
        print(f"  removed original: kindex-turans-and-danavas.csv")

    # -----------------------------------------------------------------------
    # 8. kvol2-dionysus-timeline → 2 real splits, rename
    # -----------------------------------------------------------------------
    h_dir = sources / "hellenic"
    dt_map = {
        "kvol2-dionysus-timeline--here-is-a-comprehensive-table-summarizing-the-cross-cultural.csv":
            "kvol2-dionysus-syncretic-influences.csv",
        "kvol2-dionysus-timeline--shared-messianic-and-salvific-roles.csv":
            "kvol2-dionysus-messianic-roles.csv",
    }
    for old, new in dt_map.items():
        src = h_dir / old
        if src.exists():
            src.rename(h_dir / new)
            print(f"  renamed → {new}")
    orig_dt = h_dir / "kvol2-dionysus-timeline.csv"
    if orig_dt.exists():
        orig_dt.unlink()
        print(f"  removed original: kvol2-dionysus-timeline.csv")

    # -----------------------------------------------------------------------
    # 9. kvol2-elements-timeline → 4 splits, rename, keep all
    # -----------------------------------------------------------------------
    et_map = {
        "kvol2-elements-timeline--to-improve-the-accuracy-and-expand-your-table-to-include-all.csv":
            "kvol2-elements-chakra-systems.csv",
        "kvol2-elements-timeline--these-associations-are-not-found-in-ancient-indian-texts-but.csv":
            "kvol2-elements-modern-associations.csv",
        "kvol2-elements-timeline--certainly-here-is-an-integrated-chronological-overview-of-th.csv":
            "kvol2-elements-kabbalah-note.csv",
        "kvol2-elements-timeline--summary-of-kabbalah-systems-and-tree-of-life-evolution.csv":
            "kvol2-elements-kabbalah-summary.csv",
    }
    for old, new in et_map.items():
        src = cm_dir / old
        if src.exists():
            src.rename(cm_dir / new)
            print(f"  renamed → {new}")
    orig_et = cm_dir / "kvol2-elements-timeline.csv"
    if orig_et.exists():
        orig_et.unlink()
        print(f"  removed original: kvol2-elements-timeline.csv")

    # -----------------------------------------------------------------------
    # 10. kvol2-apollonius-of-tyana → 1 split, rename to replace original
    # -----------------------------------------------------------------------
    mp_dir = sources / "messiah-prophets"
    aot_split = mp_dir / "kvol2-apollonius-of-tyana--apollonius-of-tyanas-life-with-historical-sources-parable-li.csv"
    if aot_split.exists():
        orig_aot = mp_dir / "kvol2-apollonius-of-tyana.csv"
        if orig_aot.exists():
            orig_aot.unlink()
        aot_split.rename(mp_dir / "kvol2-apollonius-of-tyana.csv")
        print(f"  replaced original with clean split: kvol2-apollonius-of-tyana.csv")

    # -----------------------------------------------------------------------
    # 11. kvol2-sudhodhana → 2 real splits, rename
    # -----------------------------------------------------------------------
    sdh_map = {
        "kvol2-sudhodhana--complete-timeline-of-sudhanas-life-spiritual-journey.csv":
            "kvol2-sudhodhana-life-timeline.csv",
        "kvol2-sudhodhana--complete-table-of-sudhanas-53-teachers-in-the-gaṇḍavyūha-sūt.csv":
            "kvol2-sudhodhana-53-teachers.csv",
    }
    for old, new in sdh_map.items():
        src = mp_dir / old
        if src.exists():
            src.rename(mp_dir / new)
            print(f"  renamed → {new}")
    orig_sdh = mp_dir / "kvol2-sudhodhana.csv"
    if orig_sdh.exists():
        orig_sdh.unlink()
        print(f"  removed original: kvol2-sudhodhana.csv")

    # -----------------------------------------------------------------------
    # 12. daimonologia-two-brothers-chart → 1 split (just "Brother 1")
    #     replace original with the split
    # -----------------------------------------------------------------------
    dtbc_split = po_dir / "daimonologia-two-brothers-chart--brother-1.csv"
    if dtbc_split.exists():
        orig = po_dir / "daimonologia-two-brothers-chart.csv"
        if orig.exists():
            orig.unlink()
        dtbc_split.rename(po_dir / "daimonologia-two-brothers-chart.csv")
        print(f"  replaced original: daimonologia-two-brothers-chart.csv")

    # -----------------------------------------------------------------------
    # 13. greek-phil-supplemental → 1 split (Platonists table)
    # -----------------------------------------------------------------------
    gps_split = h_dir / "greek-phil-supplemental--v-t-e-platonists.csv"
    if gps_split.exists():
        orig = h_dir / "greek-phil-supplemental.csv"
        if orig.exists():
            orig.unlink()
        gps_split.rename(h_dir / "greek-phil-platonists.csv")
        print(f"  renamed → greek-phil-platonists.csv")

    print("\nDone.")


if __name__ == "__main__":
    main()
