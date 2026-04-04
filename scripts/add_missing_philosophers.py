#!/usr/bin/env python3
"""
Add a second batch of missing philosophers to philosophers-list.csv.
Also renames the ambiguous "Nicomachus" → "Nicomachus of Gerasa".

Run from project root:
    python3 scripts/add_missing_philosophers.py
"""

import csv
from pathlib import Path

TARGET = Path("static/sources/hellenic/philosophers-list.csv")

# (Name, Period, Teacher, School, School2, Notes, Gender)
NEW_ENTRIES = [
    (
        "Thrasyllus of Mendes",
        "d. 36 CE",
        "Unknown",
        "Neopythagorean",
        "Middle Platonist",
        "Egyptian-born Platonist and astrologer; arranged Plato's dialogues into the nine tetralogies still used today; court astrologer to the emperor Tiberius; also arranged the works of Democritus",
        "",
    ),
    (
        "Lucius Annaeus Cornutus",
        "c. 20–65 CE",
        "",
        "Stoic",
        "",
        "Roman Stoic philosopher; freedman of the Seneca family; teacher of the poets Persius and Lucan; wrote Theologiae Graecae Compendium, a Stoic allegorical interpretation of Greek mythology; exiled by Nero",
        "",
    ),
    (
        "Theon of Alexandria",
        "c. 335–405 CE",
        "",
        "Neoplatonist",
        "",
        "Mathematician and Neoplatonist at Alexandria; father and teacher of Hypatia; edited and commented on Euclid's Elements and Ptolemy's Almagest; his editions became the standard transmission texts for centuries",
        "",
    ),
    (
        "Nicholas of Cusa",
        "1401–1464 CE",
        "Heymeric de Campo",
        "Neoplatonist",
        "Renaissance Platonist",
        "German cardinal, mathematician, and philosopher; wrote De Docta Ignorantia (On Learned Ignorance); developed the doctrine of coincidentia oppositorum (coincidence of opposites); precursor of Copernican cosmology and Reformation thought",
        "",
    ),
    (
        "Avicenna",
        "980–1037 CE",
        "Al-Farabi (writings)",
        "Islamic Platonist",
        "Peripatetic",
        "Persian polymath; full name Ibn Sina; most influential Islamic philosopher; his Neoplatonist emanation cosmology shaped medieval Islamic and Jewish theology; developed the 'floating man' argument for the self-evident nature of the soul; wrote the Book of Healing and the Canon of Medicine",
        "",
    ),
    (
        "Averroes",
        "1126–1198 CE",
        "Ibn Tufayl",
        "Islamic Platonist",
        "Peripatetic",
        "Andalusian-Arab philosopher; full name Ibn Rushd; known in Latin West as 'The Commentator' on Aristotle; his commentaries profoundly shaped Latin Scholasticism; wrote The Incoherence of the Incoherence against Al-Ghazali",
        "",
    ),
    (
        "Al-Kindi",
        "c. 801–873 CE",
        "",
        "Islamic Platonist",
        "",
        "Arab polymath; known as the 'First Arab Philosopher'; synthesised Greek philosophy (especially Neoplatonism and Aristotelianism) with Islamic theology; wrote On First Philosophy; first systematic translator and transmitter of Greek philosophy into Arabic",
        "",
    ),
    (
        "Suhrawardi",
        "1154–1191 CE",
        "Majd al-Din al-Jili",
        "Islamic Platonist",
        "Illuminationist",
        "Persian philosopher; founded the Ishraqiyyah (Illuminationist) school of Islamic philosophy; synthesised Zoroastrian light-symbolism, Neoplatonism, and Islamic mysticism; wrote Hikmat al-Ishraq (Philosophy of Illumination); executed for alleged heresy at age 38; known as Shaykh al-Maqtul (the Murdered Master)",
        "",
    ),
    (
        "Gregory of Nyssa",
        "c. 335–395 CE",
        "Basil of Caesarea (brother)",
        "Neoplatonist",
        "Christian",
        "Bishop of Nyssa; one of the Cappadocian Fathers; deeply influenced by Origen and Neoplatonism; wrote Life of Moses and Homilies on the Song of Songs; developed apophatic theology and the concept of epektasis (perpetual spiritual ascent); canonised by both Catholic and Orthodox churches",
        "",
    ),
    (
        "Publius Nigidius Figulus",
        "c. 100–45 BCE",
        "",
        "Neopythagorean",
        "",
        "Roman senator and polymath; described by Cicero as the foremost scholar after Varro; revived Pythagoreanism in Rome; wrote on theology, augury, grammar, and natural science; companion of Caesar before falling from favour; died in exile",
        "",
    ),
]

RENAME = {
    "nicomachus": "Nicomachus of Gerasa",
}


def main():
    with TARGET.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))

    header = rows[0]
    data   = rows[1:]

    # Ensure Gender column exists
    if "Gender" not in header:
        header.append("Gender")
        for r in data:
            r.append("")

    ncols = len(header)
    for r in data:
        while len(r) < ncols:
            r.append("")

    # Rename disambiguation
    renamed = []
    for r in data:
        key = r[0].strip().lower()
        if key in RENAME:
            old = r[0]
            r[0] = RENAME[key]
            renamed.append(f"  {old!r} → {r[0]!r}")

    # Existing names for dedup
    existing = {r[0].strip().lower() for r in data}

    added = []
    gi = header.index("Gender")
    for entry in NEW_ENTRIES:
        name = entry[0]
        if name.strip().lower() in existing:
            continue
        row = list(entry[:6]) + [""] * max(0, ncols - 7) + [entry[6]]
        while len(row) < ncols:
            row.append("")
        data.append(row)
        existing.add(name.strip().lower())
        added.append(name)

    data.sort(key=lambda r: r[0].strip().lower())

    with TARGET.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(data)

    if renamed:
        print("Renamed:")
        for r in renamed:
            print(r)
    print(f"\nAdded {len(added)} entries:")
    for n in added:
        print(f"  {n}")
    print(f"\nFinal: {len(data)} entries")


if __name__ == "__main__":
    main()
