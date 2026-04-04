#!/usr/bin/env python3
"""
Merge platonists.csv into philosophers-list.csv:
  1. Add "Gender" column to philosophers-list.csv
  2. Mark all known female philosophers as "female"
  3. Import every unique name from platonists.csv that isn't already present

Run from project root:
    python3 scripts/merge_platonists.py
"""

import csv
import re
from pathlib import Path

TARGET  = Path("static/sources/hellenic/philosophers-list.csv")
SOURCE  = Path("static/sources/hellenic/platonists.csv")

# ── Known female philosophers (all eras) ──────────────────────────────────────
FEMALE = {
    "aedesia",
    "aesara",
    "anne conway",
    "arignote",
    "arete of cyrene",
    "asclepigenia",
    "axiothea of phlius",
    "damo",
    "diotima of mantinea",
    "hipparchia of maroneia",
    "hypatia",
    "hypatia of alexandria",
    "lastheneia of mantinea",
    "leontion",
    "myia",
    "nicarete of megara",
    "penelope maddy",
    "phintys",
    "sosipatra",
    "sosipatra of ephesus",
    "themista of lampsacus",
    "timycha",
}

# ── Name normalisation: raw platonists.csv text → canonical form ──────────────
# Keys are lowercased text from the CSV; values are the canonical names to use.
CANONICALISE = {
    "antiochus":           "Antiochus of Ascalon",
    "augustine":           "Augustine of Hippo",
    "bernard":             "Bernard of Chartres",
    "carneades":           "Carneades of Carnea",
    "chrysanthius":        "Chrysanthius of Sardis",
    "coriscus":            "Coriscus of Scepsis",
    "eudoxus":             "Eudoxus of Cnidus",
    "gaius":               "Gaius the Platonist",
    "gilbert":             "Gilbert of Poitiers",
    "hegesinus":           "Hegesinus of Pergamon",
    "heraclides":          "Heraclides Ponticus",
    "hierocles":           "Hierocles of Alexandria",
    "hypatia":             "Hypatia of Alexandria",
    "iamblichus":          "Iamblichus Chalcidensis",
    "isidore":             "Isidore of Alexandria",
    "julian":              "Julian the Apostate",
    "lacydes":             "Lacydes of Cyrene",
    "macrobius":           "Ambrosius Theodosius Macrobius",
    "marinus":             "Marinus of Neapolis",
    "olympiodorus":        "Olympiodorus the Younger",
    "asclepiodotus":       "Asclepiodotus of Alexandria",
    "plutarch":            "Plutarch",
    "polemon":             "Polemon",
    "priscian":            "Priscian of Lydia",
    "proclus":             "Proclus Lycaeus",
    "salutius":            "Sallustius",
    "simplicius":          "Simplicius of Cilicia",
    "sopater":             "Sopater of Apamea",
    "sosipatra":           "Sosipatra of Ephesus",
    "telecles":            "Telecles of Phocis",
    "thierry":             "Thierry of Chartres",
    "xenocrates":          "Xenocrates of Chalcedon",
}

# ── New rows to add for entries that have no match in philosophers-list ────────
# Any name extracted from platonists.csv that doesn't exist will get a stub row;
# entries here get richer data instead.
ENRICHED: dict[str, tuple] = {
    # (Period, Teacher, School, School2, Notes, Gender)
    "Calcidius": (
        "fl. 4th century CE",
        "",
        "Middle Platonist",
        "",
        "Translated Plato's Timaeus into Latin with commentary; only substantial Latin translation of Plato before the Renaissance",
        "",
    ),
    "Alexander Peloplaton": (
        "fl. 2nd century CE",
        "",
        "Middle Platonist",
        "",
        "Minor Middle Platonist; nicknamed 'Peloplaton' (Clay-Plato)",
        "",
    ),
    "Gaius Marius Victorinus": (
        "c. 280–365 CE",
        "",
        "Neoplatonist",
        "Christian",
        "African rhetorician and Neoplatonist philosopher; converted to Christianity c. 355 CE; translated Porphyry and Plotinus into Latin; influenced Augustine",
        "",
    ),
    "David the Invincible": (
        "fl. 6th century CE",
        "Olympiodorus the Younger",
        "Neoplatonist",
        "Armenian",
        "Armenian Neoplatonist; translated Greek philosophical texts into Armenian; wrote Prolegomena to Philosophy; known as 'the Invincible'",
        "",
    ),
    "Cicero": (
        "106–43 BCE",
        "Philo of Larissa; Antiochus of Ascalon; Posidonius",
        "New Academy",
        "Eclectic",
        "Roman statesman and philosopher; Academic Skeptic; introduced Greek philosophy to Roman audiences; wrote De Natura Deorum, De Officiis, Tusculan Disputations",
        "",
    ),
    "Justin Martyr": (
        "c. 100–165 CE",
        "",
        "Middle Platonist",
        "Christian",
        "Christian apologist; studied Middle Platonism before conversion; employed Platonic philosophy in defence of Christianity; author of two Apologies and the Dialogue with Trypho",
        "",
    ),
    "Longinus": (
        "c. 213–273 CE",
        "Ammonius Saccas",
        "Middle Platonist",
        "Neoplatonist",
        "Philosopher and rhetorician; advisor to Queen Zenobia of Palmyra; teacher of Porphyry before Plotinus; possibly the author of On the Sublime",
        "",
    ),
    "John Scotus Eriugena": (
        "c. 815–877 CE",
        "",
        "Medieval Platonist",
        "",
        "Irish theologian and Neoplatonist; translated Pseudo-Dionysius into Latin; wrote Periphyseon (On the Division of Nature); most original Western philosopher of the early medieval period",
        "",
    ),
    "Al-Farabi": (
        "c. 872–950 CE",
        "",
        "Islamic Platonist",
        "Aristotelian",
        "First major Islamic philosopher; harmonised Plato and Aristotle; known as the 'Second Teacher' (after Aristotle); influenced Avicenna and Islamic political philosophy",
        "",
    ),
    "Anselm": (
        "1033–1109 CE",
        "Lanfranc",
        "Medieval Platonist",
        "Scholastic",
        "Archbishop of Canterbury; developed the ontological argument for God's existence; 'faith seeking understanding'; pivotal figure in Scholasticism",
        "",
    ),
    "Peter Abelard": (
        "1079–1142 CE",
        "Roscelin; William of Champeaux",
        "Medieval Platonist",
        "Scholastic",
        "French philosopher and theologian; pioneer of scholastic method; developed conceptualism on universals; known also for his relationship with Héloïse",
        "",
    ),
    "Bernard of Chartres": (
        "fl. c. 1080–1130 CE",
        "",
        "Medieval Platonist",
        "Chartrian",
        "Head of the Cathedral School of Chartres; reconciled Platonic and Christian cosmology; coined 'standing on the shoulders of giants'",
        "",
    ),
    "Gilbert of Poitiers": (
        "c. 1085–1154 CE",
        "Bernard of Chartres",
        "Medieval Platonist",
        "Chartrian",
        "Philosopher and Bishop of Poitiers; commentator on Boethius; his theology of universals was condemned at the Council of Reims (1148)",
        "",
    ),
    "Thierry of Chartres": (
        "died c. 1155 CE",
        "Bernard of Chartres",
        "Medieval Platonist",
        "Chartrian",
        "Head of the Cathedral School of Chartres after his brother Bernard; synthesised Platonic cosmology with Genesis in Tractatus de sex dierum operibus",
        "",
    ),
    "Henry of Ghent": (
        "c. 1217–1293 CE",
        "",
        "Medieval Platonist",
        "Scholastic",
        "Franciscan-influenced secular theologian at Paris; known as 'Doctor Solemnis'; Augustinian Platonist who opposed strict Aristotelianism",
        "",
    ),
    "Bonaventure": (
        "1221–1274 CE",
        "Alexander of Hales",
        "Medieval Platonist",
        "Scholastic",
        "Franciscan theologian; synthesised Augustine and Aristotle with Neoplatonic elements; wrote Itinerarium Mentis in Deum; Doctor Seraphicus",
        "",
    ),
    "Theodoric of Freiberg": (
        "c. 1250–1310 CE",
        "",
        "Medieval Platonist",
        "Dominican",
        "Dominican friar; gave the first correct mathematical explanation of the rainbow; Neoplatonist metaphysics influenced by Proclus via Meister Eckhart",
        "",
    ),
    "Meister Eckhart": (
        "c. 1260–1328 CE",
        "",
        "Medieval Platonist",
        "Mystical",
        "Dominican mystic and theologian; synthesised Neoplatonism with Christian theology; his mystical writings were condemned posthumously by Pope John XXII",
        "",
    ),
    "Berthold of Moosburg": (
        "c. 1300–1361 CE",
        "Dietrich of Freiberg; Meister Eckhart",
        "Medieval Platonist",
        "Dominican",
        "Dominican Neoplatonist; wrote the only surviving full medieval commentary on Proclus's Elementatio Theologica",
        "",
    ),
    "Paul of Venice": (
        "1369–1429 CE",
        "",
        "Medieval Platonist",
        "Augustinian",
        "Augustinian philosopher; wrote Summa Philosophiae Naturalis; important transmitter of Averroist and Platonic ideas in northern Italy",
        "",
    ),
    "Plethon": (
        "c. 1355–1452 CE",
        "",
        "Florentine Academy",
        "Neoplatonist",
        "Byzantine Platonist; sparked the Italian Renaissance revival of Plato; attended the Council of Florence; proposed replacing Christianity with a revived Platonic paganism",
        "",
    ),
    "Marsilio Ficino": (
        "1433–1499 CE",
        "Cosimo de' Medici (patron)",
        "Florentine Academy",
        "Neoplatonist",
        "Head of the Platonic Academy of Florence; translated the complete works of Plato and Plotinus into Latin; coined 'Platonic love'; wrote Theologia Platonica",
        "",
    ),
    "Cristoforo Landino": (
        "1425–1498 CE",
        "Marsilio Ficino",
        "Florentine Academy",
        "",
        "Florentine humanist and Platonist; wrote Disputationes Camaldulenses harmonising Plato with Virgil and Dante; professor at the Studio Fiorentino",
        "",
    ),
    "Giovanni Pico della Mirandola": (
        "1463–1494 CE",
        "Marsilio Ficino",
        "Florentine Academy",
        "Neoplatonist",
        "Renaissance polymath; proposed a universal synthesis of Platonism, Aristotelianism, Kabbalah, and Hermeticism; wrote the Oration on the Dignity of Man",
        "",
    ),
    "Ralph Cudworth": (
        "1617–1688 CE",
        "",
        "Cambridge Platonist",
        "",
        "English philosopher; leader of the Cambridge Platonists; wrote The True Intellectual System of the Universe defending Platonic theism against materialism",
        "",
    ),
    "Henry More": (
        "1614–1687 CE",
        "",
        "Cambridge Platonist",
        "",
        "English philosopher; Cambridge Platonist; corresponded with Descartes; developed concept of 'Spirit of Nature' as intermediary between God and matter",
        "",
    ),
    "Anne Conway": (
        "1631–1679 CE",
        "Henry More",
        "Cambridge Platonist",
        "",
        "English Platonist and metaphysician; wrote Principles of the Most Ancient and Modern Philosophy; influenced Leibniz; converted to Quakerism; first woman in the Cambridge Platonist circle",
        "female",
    ),
    "Thomas Taylor": (
        "1758–1835 CE",
        "",
        "Modern Platonist",
        "",
        "English translator and Neoplatonist; first to translate the complete works of Plato and Aristotle into English; translated Plotinus, Porphyry, Iamblichus, and Proclus",
        "",
    ),
    "Emanuel Swedenborg": (
        "1688–1772 CE",
        "",
        "Modern Platonist",
        "",
        "Swedish scientist and mystic; claimed direct spiritual visions; wrote Heaven and Hell; his Neoplatonic metaphysics influenced Blake, Kant, and the New Church",
        "",
    ),
    "Josiah Royce": (
        "1855–1916 CE",
        "",
        "Modern Platonist",
        "Idealist",
        "American idealist philosopher; taught at Harvard; wrote The World and the Individual; absolute idealism with Platonic influences",
        "",
    ),
    "Aleksei Losev": (
        "1893–1988 CE",
        "",
        "Modern Platonist",
        "",
        "Russian philosopher; last great classical Russian Platonist; wrote an 8-volume History of Ancient Aesthetics; persecuted during Stalin era; specialist in Plato and Neoplatonism",
        "",
    ),
    "Giordano Bruno": (
        "1548–1600 CE",
        "",
        "Renaissance Platonist",
        "Hermetic",
        "Italian philosopher and Dominican friar; synthesised Neoplatonism, Hermeticism, and Copernican cosmology; burned at the stake by the Inquisition for heresy",
        "",
    ),
    "Blaise Pascal": (
        "1623–1662 CE",
        "",
        "Renaissance Platonist",
        "Augustinian",
        "French mathematician and philosopher; Augustinian Christian with Platonic influences; wrote Pensées; developed early probability theory",
        "",
    ),
    "Gottlob Frege": (
        "1848–1925 CE",
        "",
        "Analytic Platonist",
        "",
        "German logician and philosopher; founded modern mathematical logic and philosophy of language; his Platonism posited abstract objects as real and mind-independent",
        "",
    ),
    "Bertrand Russell": (
        "1872–1970 CE",
        "Alfred North Whitehead",
        "Analytic Platonist",
        "",
        "British mathematician, logician, and philosopher; co-wrote Principia Mathematica; early Platonist about universals; later moved to neutral monism",
        "",
    ),
    "Kurt Gödel": (
        "1906–1978 CE",
        "",
        "Analytic Platonist",
        "",
        "Austrian-American logician; proved the incompleteness theorems; explicit mathematical Platonist who believed mathematical objects are mind-independently real",
        "",
    ),
    "Roderick Chisholm": (
        "1916–1999 CE",
        "",
        "Analytic Platonist",
        "",
        "American philosopher; specialist in epistemology and metaphysics; defended Platonic realism about properties and propositions",
        "",
    ),
    "W. V. O. Quine": (
        "1908–2000 CE",
        "Alfred North Whitehead; Bertrand Russell",
        "Analytic Platonist",
        "",
        "American logician and philosopher; defended a naturalised Platonism about abstract objects through the indispensability argument",
        "",
    ),
    "Jan Łukasiewicz": (
        "1878–1956 CE",
        "",
        "Analytic Platonist",
        "",
        "Polish logician; invented Polish notation and developed multi-valued logics; Platonist about logical laws",
        "",
    ),
    "Crispin Wright": (
        "born 1942 CE",
        "",
        "Analytic Platonist",
        "",
        "British philosopher; neo-Fregean Platonist; defends abstractionism about numbers; wrote Frege's Conception of Numbers as Objects",
        "",
    ),
    "Edward N. Zalta": (
        "born 1952 CE",
        "",
        "Analytic Platonist",
        "",
        "American philosopher; developed object theory to systematise Platonic abstract objects; principal editor of the Stanford Encyclopedia of Philosophy",
        "",
    ),
    "Penelope Maddy": (
        "born 1950 CE",
        "",
        "Analytic Platonist",
        "",
        "American philosopher of mathematics; developed set-theoretic naturalism; wrote Realism in Mathematics and Second Philosophy",
        "female",
    ),
    "Edmund Husserl": (
        "1859–1938 CE",
        "Franz Brentano; Carl Stumpf",
        "Continental Platonist",
        "Phenomenologist",
        "German philosopher; founded phenomenology; his theory of ideal meanings and essences has strong Platonic affinities; wrote Logical Investigations and Ideas I",
        "",
    ),
    "Leo Strauss": (
        "1899–1973 CE",
        "Edmund Husserl; Hermann Cohen",
        "Continental Platonist",
        "Political",
        "German-American political philosopher; advocated return to classical political philosophy; influential on neoconservative thought; wrote Natural Right and History",
        "",
    ),
    "Julius Evola": (
        "1898–1974 CE",
        "",
        "Continental Platonist",
        "Traditionalist",
        "Italian philosopher and esotericist; synthesised Neoplatonism, Hermeticism, and Tantra in a Traditionalist framework; wrote Revolt Against the Modern World",
        "",
    ),
}


def parse_platonists(path: Path) -> list[tuple[str, str, str]]:
    """
    Return list of (raw_name, era_label, school_label) from platonists.csv.
    Handles compound entries like 'Coriscus and Erastus of Scepsis'.
    """
    era_map = {
        "Ancient":          "ancient",
        "Old":              "Old Academy",
        "Middle":           "Middle Academy",
        "New":              "New Academy",
        "Academy":          "Late Academy",
        "Neoplatonists":    "Neoplatonist",
        "Middle Platonists": "Middle Platonist",
        "Skeptics":         "Skeptic",
        "Medieval":         "Medieval",
        "Modern":           "Modern",
        "Renaissance":      "Renaissance",
        "Cambridge":        "Cambridge Platonist",
        "Florentine Academy": "Florentine Academy",
        "Analytic":         "Analytic",
        "Continental":      "Continental",
        "Contemporary":     "Contemporary",
    }
    results = []
    current_school = ""
    rows = list(csv.reader(path.open(newline="", encoding="utf-8-sig")))
    for r in rows:
        if not r:
            continue
        cell0 = r[0].strip()
        cell1 = r[1].strip() if len(r) > 1 else ""
        # Category row (left cell is an era label, right cell is content or [TABLE])
        if cell0 in era_map:
            current_school = era_map[cell0]
            text = cell1
        elif cell0 == "" and cell1:
            text = cell1
        else:
            continue
        if not text or text.strip() == "[TABLE]":
            continue
        # Extract bullet-point names
        for line in text.splitlines():
            line = re.sub(r"^\s*-\s*", "", line).strip()
            line = re.sub(r"^\s*-\s*Students\s*$", "", line)
            if not line:
                continue
            # Split compound entries
            parts = re.split(r"\s+and\s+", line)
            for part in parts:
                part = part.strip()
                if part and not part.startswith("["):
                    results.append((part, current_school))
    return results


def normalise(name: str) -> str:
    """Return a canonical name given raw platonists.csv text."""
    lower = name.lower()
    return CANONICALISE.get(lower, name)


def existing_key(name: str) -> str:
    """Lowercase key for dedup comparison."""
    return name.strip().lower()


def main():
    # ── Load target ───────────────────────────────────────────────────────────
    with TARGET.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    header = rows[0]
    data   = rows[1:]

    # Add Gender column if not present
    if "Gender" not in header:
        header.append("Gender")
        for r in data:
            r.append("")

    ncols = len(header)

    # Ensure all rows are padded to ncols
    for r in data:
        while len(r) < ncols:
            r.append("")

    gender_idx = header.index("Gender")

    # Mark existing females
    marked = 0
    for r in data:
        n = r[0].strip().lower()
        if n in FEMALE and r[gender_idx] != "female":
            r[gender_idx] = "female"
            marked += 1

    # ── Parse platonists.csv ──────────────────────────────────────────────────
    entries = parse_platonists(SOURCE)
    print(f"Extracted {len(entries)} name entries from platonists.csv")

    existing = {existing_key(r[0]) for r in data}

    added = []
    skipped = []
    for raw_name, school in entries:
        canonical = normalise(raw_name)
        key = existing_key(canonical)
        if key in existing:
            skipped.append(canonical)
            continue
        existing.add(key)

        # Build row
        if canonical in ENRICHED:
            period, teacher, sch, sch2, notes, gender = ENRICHED[canonical]
        else:
            period, teacher, sch, sch2, notes = "", "", school, "", ""
            gender = "female" if key in FEMALE else ""

        row = [canonical, period, teacher, sch, sch2, notes]
        while len(row) < ncols - 1:
            row.append("")
        row.append(gender)
        data.append(row)
        added.append(canonical)

    # Sort alphabetically
    data.sort(key=lambda r: r[0].strip().lower())

    # Write
    with TARGET.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(data)

    print(f"\nGender column added / updated")
    print(f"  Females marked (pre-existing)  : {marked}")
    print(f"  New entries added              : {len(added)}")
    print(f"  Already-present entries skipped: {len(skipped)}")
    print(f"  Final row count                : {len(data)}  (+ header)")

    if added:
        print("\nAdded:")
        for n in sorted(added):
            print(f"  {n}")


if __name__ == "__main__":
    main()
