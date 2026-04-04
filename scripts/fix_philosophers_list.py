#!/usr/bin/env python3
"""
Fix hellenic/philosophers-list.csv:
  1. Remove exact and near-duplicate rows
  2. Add 12 missing significant figures

Run from project root:
    python3 scripts/fix_philosophers_list.py
"""

import csv
from pathlib import Path

TARGET = Path("static/sources/hellenic/philosophers-list.csv")

# Specific rows to unconditionally drop (identified by name + period fragment)
DROP_SPECIFIC = {
    ("Aedesia",               "5th century"),        # keep "fl. 5th century"
    ("Antiochus of Ascalon",  "2nd / 1st century"),  # keep the precise dated row
    ("Telecles of Phocis",    "167/1666"),            # typo year; keep "167/166"
}

# Rows that are exact duplicates — drop on the SECOND encounter
DROP_EXACT_SECOND = {
    ("Plotinus",    "c. 204 – 270"),
    ("Plutarch",    "c. 46 – 120"),
    ("Speusippus",  "c. 407 BC – 339 BC"),
    ("Zenodotus",   "fl. c. 475"),
}

# Near-duplicates: remove these rows entirely (canonical form already present)
DROP_NEAR = {
    "Chrysanthius",   # keep "Chrysanthius of Sardis"
    "Porphyry",       # keep "Porphyry of Tyre"
    "Philo",          # keep "Philo of Alexandria"  (period "20 BC - 50 AD")
    "Polemon of Athens",  # keep "Polemon" (which has the dates)
}

# New rows to append: (Name, Period, Teacher, School, School2, Notes)
NEW_ROWS = [
    (
        "Musonius Rufus",
        "c. 20–101 CE",
        "",
        "Stoic",
        "",
        "Roman Stoic philosopher; teacher of Epictetus and Dio Chrysostom; exiled twice by Nero and Vespasian; advocated equal education for women",
    ),
    (
        "Seneca the Younger",
        "c. 4 BCE–65 CE",
        "Attalus; Sotion; Papirius Fabianus",
        "Stoic",
        "",
        "Roman statesman and playwright; wrote Letters to Lucilius and the Moral Essays; tutor to Nero; forced to commit suicide",
    ),
    (
        "Marcus Aurelius",
        "121–180 CE",
        "Fronto; Junius Rusticus; Apollonius of Chalcedon",
        "Stoic",
        "",
        "Roman emperor (161–180 CE); Stoic philosopher; author of the Meditations; last of the Five Good Emperors",
    ),
    (
        "Lucretius",
        "c. 99–55 BCE",
        "Epicurus (intellectual heir)",
        "Epicurean",
        "",
        "Roman Epicurean poet; author of De Rerum Natura, the most systematic exposition of Epicurean physics and ethics in Latin",
    ),
    (
        "John Philoponus",
        "c. 490–570 CE",
        "Ammonius Hermiae",
        "Neoplatonist",
        "Peripatetic",
        "Christian Neoplatonist; wrote commentaries on Aristotle; challenged Aristotle's doctrine of the eternity of the world; precursor of the cosmological argument",
    ),
    (
        "Critias",
        "c. 460–403 BCE",
        "Socrates; Gorgias",
        "Sophist",
        "",
        "Athenian oligarch and writer; one of the Thirty Tyrants; student of Socrates and relative of Plato; wrote tragedies and elegies with philosophical content",
    ),
    (
        "Antiphon",
        "c. 480–411 BCE",
        "",
        "Sophist",
        "",
        "Sophist and orator; wrote On Truth (fragment survives); argued for the natural equality of Greeks and barbarians; possibly the same as Antiphon the orator",
    ),
    (
        "Eratosthenes of Cyrene",
        "c. 276–194 BCE",
        "Ariston of Chios; Lysanias of Cyrene; Callimachus",
        "Peripatetic",
        "",
        "Polymath; head of the Library of Alexandria; calculated the circumference of the Earth; also studied ethics and cosmology; called 'Beta' (the all-rounder)",
    ),
    (
        "Theaetetus of Athens",
        "c. 417–369 BCE",
        "Plato; Theodorus of Cyrene",
        "Academy",
        "Platonic",
        "Mathematician and philosopher; Plato named a dialogue after him; contributed to the theory of irrational numbers and the theory of the five regular solids",
    ),
    (
        "Crito of Athens",
        "c. 469–399 BCE",
        "Socrates",
        "Socratic",
        "",
        "Wealthy friend and devoted disciple of Socrates; offered to finance his escape from prison; Plato's dialogue Crito is named after him",
    ),
    (
        "Arrian of Nicomedia",
        "c. 86–160 CE",
        "Epictetus",
        "Stoic",
        "",
        "Stoic philosopher and historian; compiled and edited the Discourses and Enchiridion of Epictetus; also wrote the Anabasis of Alexander",
    ),
    (
        "Julian the Apostate",
        "331–363 CE",
        "Maximus of Ephesus; Iamblichus (writings)",
        "Neoplatonist",
        "",
        "Roman emperor (361–363 CE); Neoplatonist philosopher; attempted to revive paganism; wrote Hymn to King Helios and Against the Galileans; patron of Sallustius",
    ),
]


def main():
    with TARGET.open(newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.reader(fh))

    header = rows[0]
    data = rows[1:]

    exact_seen: dict[tuple, int] = {}
    out_rows = []

    for row in data:
        name = row[0].strip()
        period = row[1].strip() if len(row) > 1 else ""

        # Near-duplicate: unconditional drop
        if name in DROP_NEAR:
            continue

        # Specific weaker rows: always drop
        if any(name == dn and dp in period for (dn, dp) in DROP_SPECIFIC):
            continue

        # Exact-duplicate: drop on the second encounter
        key = None
        for (dn, dp) in DROP_EXACT_SECOND:
            if name == dn and dp in period:
                key = (dn, dp)
                break
        if key:
            exact_seen[key] = exact_seen.get(key, 0) + 1
            if exact_seen[key] > 1:
                continue

        out_rows.append(row)

    # Add new rows only if not already present
    existing_names = {r[0].strip().lower() for r in out_rows}
    ncols = len(header)
    added = []
    for nr in NEW_ROWS:
        if nr[0].strip().lower() not in existing_names:
            padded = list(nr) + [""] * max(0, ncols - len(nr))
            out_rows.append(padded)
            added.append(nr[0])

    # Sort by name for readability (stable; header already removed)
    out_rows.sort(key=lambda r: r[0].strip().lower())

    with TARGET.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(out_rows)

    print(f"Original rows : {len(data)}")
    print(f"After dedup   : {len(out_rows) - len(added)}")
    print(f"Added          : {len(added)}")
    print(f"Final rows     : {len(out_rows)}  (+ header = {len(out_rows)+1} lines)")
    if added:
        print(f"\nAdded:")
        for n in added:
            print(f"  {n}")


if __name__ == "__main__":
    main()
