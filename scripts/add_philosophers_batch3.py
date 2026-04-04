#!/usr/bin/env python3
"""
Batch 3 additions to philosophers-list.csv — thorough gap-fill across all schools.

Additions cover:
  - Sophists (Euthydemus, Dionysodorus)
  - Cynics (Onesicritus)
  - Ancient women (Aspasia, Perictione I & II, Ptolemaïs of Cyrene)
  - Middle Platonists (Taurus of Beirut, Severus, Harpocration)
  - Gnostic/Syncretic tradition (Valentinus, Basilides of Alexandria,
    Simon Magus, Bardaisan, Mani)
  - Late Neoplatonists (Zacharias Scholasticus, Stephanus, Elias)
  - Christian Neoplatonists (Macrina the Younger)
  - Jewish Philosophers (Isaac Israeli, Solomon ibn Gabirol, Maimonides)
  - Byzantine (Michael Psellus, Bessarion)
  - Islamic (Ibn Bajja / Avempace, Ibn Tufayl)
  - Scholastic Medieval (Albertus Magnus, Thomas Aquinas, Duns Scotus,
    William of Ockham)
  - Medieval women mystics (Hildegard of Bingen, Mechthild of Magdeburg,
    Marguerite Porete)
  - Renaissance (Francesco Patrizi)
  - Cambridge Platonist (Benjamin Whichcote)
  - Modern Platonists (Simone Weil, Iris Murdoch)

Run from project root:
    python3 scripts/add_philosophers_batch3.py
"""

import csv
from pathlib import Path

TARGET = Path("static/sources/hellenic/philosophers-list.csv")

# (Name, Period, Teacher, School, School2, Notes, Gender)
NEW_ENTRIES = [

    # ── Sophists ──────────────────────────────────────────────────────────────
    (
        "Euthydemus of Chios",
        "fl. c. 400 BCE",
        "",
        "Sophist",
        "",
        "Itinerant Sophist; brother of Dionysodorus; appeared with his brother in Plato's dialogue Euthydemus; taught eristic argumentation for a fee",
        "",
    ),
    (
        "Dionysodorus",
        "fl. c. 400 BCE",
        "",
        "Sophist",
        "",
        "Itinerant Sophist; brother of Euthydemus; appeared in Plato's Euthydemus as a master of misleading argumentation and word-play",
        "",
    ),

    # ── Cynics ────────────────────────────────────────────────────────────────
    (
        "Onesicritus of Astypalaea",
        "fl. c. 325 BCE",
        "Diogenes of Sinope",
        "Cynic",
        "",
        "Cynic philosopher and admiral in Alexander the Great's fleet; recorded the gymnosophists (Indian naked philosophers) he met in the Punjab; wrote How Alexander Was Educated; conflated Cynic and Indian asceticism",
        "",
    ),

    # ── Ancient women philosophers ────────────────────────────────────────────
    (
        "Aspasia of Miletus",
        "c. 470–400 BCE",
        "Unknown",
        "Sophist",
        "",
        "Intellectual companion of Pericles; ran a school of philosophy and rhetoric in Athens; cited by Plato as Socrates' teacher of rhetoric and erotics (Menexenus, Symposium); first woman associated with Socratic circles",
        "female",
    ),
    (
        "Perictione I",
        "fl. 5th century BCE",
        "",
        "Pythagorean",
        "",
        "Pythagorean philosopher; mother of Plato; attributed author of On the Harmony of Women and On Wisdom; argued for rational self-discipline as the foundation of womanly virtue",
        "female",
    ),
    (
        "Perictione II",
        "fl. 3rd century BCE",
        "",
        "Pythagorean",
        "",
        "Later Pythagorean philosopher (distinct from Plato's mother); wrote On Wisdom, a Neopythagorean text arguing that philosophy is the way to contemplate god and all things",
        "female",
    ),
    (
        "Ptolemaïs of Cyrene",
        "fl. 1st century CE",
        "",
        "Neopythagorean",
        "",
        "Female Pythagorean music theorist; wrote Pythagorean Principles of Music (cited by Porphyry in his Commentary on Ptolemy's Harmonics); synthesised Pythagorean and Aristoxenian theories of musical proportion",
        "female",
    ),

    # ── Middle Platonists ─────────────────────────────────────────────────────
    (
        "Taurus of Beirut",
        "fl. c. 145 CE",
        "Unknown",
        "Middle Platonist",
        "",
        "Platonic philosopher who taught in Athens; teacher of Aulus Gellius (who recorded his lectures in Noctes Atticae); wrote commentaries on Plato's Timaeus and Gorgias; distinguished between different types of soul-entry into the body",
        "",
    ),
    (
        "Severus",
        "fl. 2nd century CE",
        "",
        "Middle Platonist",
        "",
        "Middle Platonist commentator; wrote on Plato's Timaeus; cited by Proclus; held an intermediate position between Albinus and Numenius on the interpretation of the Demiurge",
        "",
    ),
    (
        "Harpocration of Argos",
        "fl. 2nd century CE",
        "Atticus",
        "Middle Platonist",
        "",
        "Student of Atticus; wrote a multi-volume commentary on Plato; known only through citations in later authors; contributed to the debate on the eternity of the world",
        "",
    ),

    # ── Gnostic / Syncretic tradition ─────────────────────────────────────────
    (
        "Simon Magus",
        "fl. c. 35–65 CE",
        "John the Baptist (tradition)",
        "Gnostic",
        "",
        "Samaritan proto-Gnostic; considered by early church fathers the father of all heresy; claimed divine status; his follower Menander developed his ideas; the simony of purchasing spiritual gifts is named after him; Acts 8:9–24",
        "",
    ),
    (
        "Basilides of Alexandria",
        "fl. c. 117–138 CE",
        "Matthias the Apostle (claimed)",
        "Gnostic",
        "",
        "Alexandrian Gnostic philosopher (distinct from Basilides the Stoic and Basilides the Epicurean); taught under Hadrian and Antoninus Pius; developed one of the first systematic Gnostic cosmologies with 365 heavens and the Abraxas deity; his son Isidore continued his school",
        "",
    ),
    (
        "Valentinus",
        "c. 100–180 CE",
        "Theudas (claimed disciple of Paul)",
        "Gnostic",
        "",
        "Egyptian Gnostic philosopher; most influential Gnostic thinker; founded the Valentinian school; came close to becoming Bishop of Rome c. 143 CE; developed elaborate Pleroma cosmology of divine emanations (Aeons); deeply influenced by Neoplatonism and Platonism",
        "",
    ),
    (
        "Bardaisan",
        "154–222 CE",
        "",
        "Gnostic",
        "Syriac",
        "Syriac philosopher, poet, and theologian; founded a dualist school in Edessa; wrote The Book of the Laws of the Countries; synthesised Chaldean astrology, Stoic cosmology, and Christian theology; a key transmitter of Greek philosophy into Syriac culture",
        "",
    ),
    (
        "Mani",
        "216–274 CE",
        "Baptists (early community)",
        "Manichaean",
        "",
        "Founder of Manichaeism; synthesised Zoroastrian dualism, Buddhist ethics, and Christian Gnostic elements into a world religion; called himself the 'Seal of the Prophets'; his religion spread from Spain to China; executed by the Sasanian king Bahram I",
        "",
    ),

    # ── Late antique Christian Neoplatonists ─────────────────────────────────
    (
        "Macrina the Younger",
        "c. 330–379 CE",
        "Gregory of Nazianzus (spiritual direction)",
        "Neoplatonist",
        "Christian",
        "Elder sister and teacher of Gregory of Nyssa; founded a monastic community on the family estate; Gregory cast her as the lead philosopher in his dialogue On the Soul and the Resurrection, modelled on Plato's Phaedo; the first woman in Christian tradition clearly depicted as a philosopher",
        "female",
    ),
    (
        "Zacharias Scholasticus",
        "c. 465–536 CE",
        "Ammonius Hermiae",
        "Neoplatonist",
        "Christian",
        "Christian Neoplatonist philosopher from Caesarea; studied under Ammonius in Alexandria; wrote the philosophical dialogue Ammonius (against eternal matter) and a Life of Severus of Antioch; his Ecclesiastical History preserves important information about late antique philosophy",
        "",
    ),
    (
        "Stephanus of Alexandria",
        "fl. c. 610–641 CE",
        "Olympiodorus the Younger",
        "Neoplatonist",
        "",
        "Last known Neoplatonist from Alexandria; invited to Constantinople by Emperor Heraclius; wrote commentaries on Aristotle and Plato; also wrote on alchemy and astronomy; his philosophical lectures mark the transition from Alexandrian to Byzantine Neoplatonism",
        "",
    ),
    (
        "Elias of Alexandria",
        "fl. 6th century CE",
        "Olympiodorus the Younger",
        "Neoplatonist",
        "Armenian",
        "Neoplatonist philosopher; probably the same as Elias bar Shinaya of the Armenian tradition; wrote commentaries on Porphyry's Isagoge and Aristotle's Categories; contemporary of Olympiodorus and David the Invincible",
        "",
    ),

    # ── Jewish Philosophy ─────────────────────────────────────────────────────
    (
        "Isaac Israeli ben Solomon",
        "c. 832–932 CE",
        "",
        "Neoplatonist",
        "Jewish",
        "Egyptian-born Jewish physician and philosopher; wrote Book of Definitions and Book on the Elements; first systematic Jewish Neoplatonist; transmitted Neoplatonic emanation theory into Jewish philosophy; influenced both Jewish and Islamic Scholasticism",
        "",
    ),
    (
        "Solomon ibn Gabirol",
        "c. 1021–1058 CE",
        "",
        "Neoplatonist",
        "Jewish",
        "Andalusian Jewish philosopher and poet; known in the Latin West as Avicebron; wrote Fons Vitae (Source of Life) in Arabic, translated into Latin and widely read by Scholastics; Neoplatonist theory of matter and form; also wrote the ethical treatise On the Improvement of the Moral Qualities",
        "",
    ),
    (
        "Maimonides",
        "1135–1204 CE",
        "Ibn Rushd (indirect influence)",
        "Jewish",
        "Aristotelian",
        "Full name Moses ben Maimon or Rambam; greatest medieval Jewish philosopher; synthesised Aristotelian rationalism with Jewish theology in The Guide for the Perplexed; also wrote the Mishneh Torah; his negative theology influenced both Jewish and Christian Scholasticism",
        "",
    ),

    # ── Byzantine Philosophy ──────────────────────────────────────────────────
    (
        "Michael Psellus",
        "1017–1078 CE",
        "Various",
        "Neoplatonist",
        "Byzantine",
        "Byzantine scholar and statesman; revived the study of Plato and Neoplatonism in Constantinople after centuries of neglect; wrote De Omnifaria Doctrina and commentaries on Aristotle; drew on Proclus and Iamblichus for his theurgical interests; court intellectual under multiple emperors",
        "",
    ),
    (
        "Bessarion",
        "c. 1403–1472 CE",
        "Plethon",
        "Neoplatonist",
        "Byzantine",
        "Byzantine cardinal and Platonic philosopher; student of Plethon; defended Plato against Aristotle in the controversy with George of Trebizond; brought Greek manuscripts to Italy; his library became the foundation of the Biblioteca Marciana in Venice; key figure in transmission of Greek philosophy to the Renaissance",
        "",
    ),

    # ── Islamic Philosophy ────────────────────────────────────────────────────
    (
        "Ibn Bajja",
        "c. 1085–1138 CE",
        "",
        "Islamic Platonist",
        "Peripatetic",
        "Andalusian philosopher; known in Latin West as Avempace; wrote Governance of the Solitary (Tadbir al-Mutawahhid); influenced Averroes and Maimonides; developed theory of the solitary philosopher achieving contemplative union with the Active Intellect without religious community",
        "",
    ),
    (
        "Ibn Tufayl",
        "c. 1105–1185 CE",
        "Ibn Bajja",
        "Islamic Platonist",
        "",
        "Andalusian philosopher and physician; wrote Hayy ibn Yaqzan, the first philosophical novel; depicts a child raised in isolation achieving philosophical enlightenment through reason alone; synthesised Avicenna, Sufism, and Neoplatonism; his work influenced Spinoza and Locke",
        "",
    ),

    # ── Scholastic Medieval ───────────────────────────────────────────────────
    (
        "Albertus Magnus",
        "c. 1200–1280 CE",
        "",
        "Scholastic",
        "Peripatetic",
        "Dominican friar and polymath; teacher of Thomas Aquinas; first to systematically introduce Aristotelian philosophy into Latin Christendom; wrote commentaries on all of Aristotle; patron saint of natural scientists; also interested in Neoplatonism and Pseudo-Dionysius",
        "",
    ),
    (
        "Thomas Aquinas",
        "1225–1274 CE",
        "Albertus Magnus",
        "Scholastic",
        "Peripatetic",
        "Dominican friar and theologian; synthesised Aristotelian philosophy with Christian theology in the Summa Theologica; developed natural theology and the Five Ways for God's existence; Doctor Angelicus; most influential Scholastic philosopher",
        "",
    ),
    (
        "Duns Scotus",
        "c. 1266–1308 CE",
        "",
        "Scholastic",
        "",
        "Scottish Franciscan philosopher; known as Doctor Subtilis; developed formal distinction and the univocity of being (ens commune applies to both God and creatures); precursor of Ockham; innovator in epistemology and metaphysics; beatified 1993",
        "",
    ),
    (
        "William of Ockham",
        "c. 1287–1347 CE",
        "Duns Scotus (indirect)",
        "Nominalist",
        "Scholastic",
        "English Franciscan friar; father of nominalism; Ockham's Razor (entities should not be multiplied beyond necessity); challenged papal authority; rejected universals as mental concepts only; his voluntarist theology influenced Protestant Reformation",
        "",
    ),

    # ── Medieval Women Mystics ────────────────────────────────────────────────
    (
        "Hildegard of Bingen",
        "1098–1179 CE",
        "Jutta of Sponheim",
        "Mystical",
        "Medieval Platonist",
        "German Benedictine abbess, mystic, and polymath; wrote Scivias (Know the Ways) recording her visions; Neoplatonic viriditas (greening power) of divine presence in nature; also wrote on medicine, music, cosmology, and natural history; first female Doctor of the Church",
        "female",
    ),
    (
        "Mechthild of Magdeburg",
        "c. 1207–1282 CE",
        "",
        "Mystical",
        "",
        "German Beguine mystic; wrote The Flowing Light of the Godhead, one of the first mystical works in the German vernacular; bridal mysticism and direct union with the divine; influenced by Neoplatonism through Pseudo-Dionysius; influenced Dante",
        "female",
    ),
    (
        "Marguerite Porete",
        "c. 1250–1310 CE",
        "",
        "Mystical",
        "",
        "French Beguine mystic; wrote The Mirror of Simple Souls arguing for the annihilation of the will in union with God; condemned as heretical and burned at the stake in Paris 1310; her work circulated anonymously and influenced Meister Eckhart and the Rhineland mystics",
        "female",
    ),

    # ── Renaissance Platonists ────────────────────────────────────────────────
    (
        "Francesco Patrizi",
        "1529–1597 CE",
        "Marsilio Ficino (writings)",
        "Neoplatonist",
        "Renaissance Platonist",
        "Italian philosopher; the most systematic Renaissance Platonist; wrote Nova de Universis Philosophia (A New Universal Philosophy); proposed panpsychism and an infinite universe anticipating Bruno and Spinoza; clashed with Jesuit Aristotelians",
        "",
    ),

    # ── Cambridge Platonists ──────────────────────────────────────────────────
    (
        "Benjamin Whichcote",
        "1609–1683 CE",
        "",
        "Cambridge Platonist",
        "",
        "English clergyman; considered the founding father of the Cambridge Platonist movement; provost of King's College Cambridge; his Aphorisms crystallised the group's core tenets: reason as the candle of the Lord, moral religion over dogma, latitude and toleration",
        "",
    ),

    # ── Modern Platonists ─────────────────────────────────────────────────────
    (
        "Simone Weil",
        "1909–1943 CE",
        "",
        "Modern Platonist",
        "",
        "French philosopher and mystic; explicit Platonist who saw Plato as a proto-Christian; wrote Waiting for God and The Need for Roots; developed a spirituality of affliction (malheur) and decreation (kenotic union); also wrote brilliant political philosophy; died of self-imposed deprivation during WWII",
        "female",
    ),
    (
        "Iris Murdoch",
        "1919–1999 CE",
        "",
        "Modern Platonist",
        "",
        "Irish-British philosopher and novelist; explicit Platonist; argued against linguistic philosophy and for a return to the Good as the central concept of moral philosophy; wrote The Sovereignty of Good and The Fire and the Sun (on Plato's theory of art); Platonic love as selfless attention to reality",
        "female",
    ),
]


def main():
    with TARGET.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))

    header = rows[0]
    data   = rows[1:]

    if "Gender" not in header:
        header.append("Gender")
        for r in data:
            r.append("")

    ncols = len(header)
    for r in data:
        while len(r) < ncols:
            r.append("")

    existing = {r[0].strip().lower() for r in data}
    gi = header.index("Gender")

    added = []
    for entry in NEW_ENTRIES:
        name = entry[0]
        if name.strip().lower() in existing:
            print(f"  SKIP (exists): {name}")
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

    females_total = sum(
        1 for r in data
        if len(r) > gi and r[gi].strip().lower() == "female"
    )

    print(f"\nAdded {len(added)} new entries:")
    for n in added:
        print(f"  {n}")
    print(f"\nFemale philosophers total : {females_total}")
    print(f"Total entries             : {len(data)}")


if __name__ == "__main__":
    main()
