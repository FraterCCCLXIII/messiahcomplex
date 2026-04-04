---
title: Missing Cults & Traditions — Coverage Gap Notes
description: A working audit of religious traditions, mystery cults, and philosophical schools not yet systematically covered in the source data, organized by priority for the Messiah Complex research scope.
---

# Missing Cults & Traditions — Coverage Gap Notes

> **Status:** Working research note. Use this as a queue when deciding which new CSV files to build next.

---

## What is already well covered

| Block | Source files | Assessment |
|---|---|---|
| Egyptian mysteries | Osiris, Isis, Amun-Ra, Ptah, Thoth, Anubis, Hathor, Serapis, House of Life | Good |
| Greek mysteries | Eleusinian, Orphic, Dionysian, Samothracian, Apollonian, Heraclean, Despoina, Heroine cults | Good |
| Roman mysteries | Mithras, Cybele/Attis, Sol Invictus, Jupiter Dolichenus, Isis (Roman) | Good |
| Gnostic sects | Sethians, Valentinians, Basilidians, Naassenes, Ophites, Carpocratians, Cainites, Mandaeans | Good |
| Second Temple Judaism | Essenes, Pharisees, Sadducees, Zealots, Sicarii, Therapeutae, Qumran | Good |
| Jewish mysticism | Kabbalah, Hekhalot, Merkabah, Sefer Yetzirah, Shi'ur Qomah | Good |
| Christian heresies | 19+ sects in `heresies.csv` plus `all-christian-sects.csv` | Good |
| Early Buddhism | 25 schools, plus Mahayana sutras, Lotus, Avatamsaka, Dzogchen | Good |
| Persian / Zoroastrian | Avestan, Achaemenid, Zoroastrian gods, Saka religion | Good |
| Hermetic / esoteric | Hermeticism, tantra, Freemasonry, magic / necromancy | Good |
| Steppe / hero cults | Thracian horseman, Orpheus, Scythian kings, Sarmatian heroes | Partial |

---

## Critical gaps

### 🔴 High priority

#### 1. Mesopotamian / Sumerian religion
The foundational source layer for all Near Eastern tradition. The Descent of Inanna appears in `mystery-ritual.csv` but there is no systematic file.

- Sumerian pantheon: Anu, Enlil, Enki/Ea, Ninhursag, Inanna, Utu/Shamash, Nanna/Sin, Ereshkigal, Nergal, Dumuzi/Tammuz
- Akkadian/Babylonian layer: Marduk, Tiamat, Ishtar, Nabu, Nergal
- Key myth cycles: *Descent of Inanna*, *Enuma Elish*, *Epic of Gilgamesh*, *Etana*, *Adapa*
- Tammuz / Dumuzi as the prototype dying-and-rising god; earlier than Osiris, Adonis, Attis, and Dionysus in documentary record
- **Suggested files:** `pie-origins/mesopotamian-pantheon.csv`, `pie-origins/sumerian-myth-cycles.csv`

#### 2. Vedic / Hindu tradition
You have Buddhist–Hindu comparison tables but almost no Hindu-specific coverage. The Vedic tradition is the PIE sister religion to Avestan/Zoroastrian.

- Vedic religion: Rigveda gods (Indra, Varuna, Agni, Soma, Mitra, Yama, Rudra, Vishnu as solar servant)
- Upanishadic tradition: Atman/Brahman identity, the major Upanishads as sequence
- Six orthodox *darshanas*: Samkhya, Yoga, Nyaya, Vaisheshika, Mimamsa, Vedanta
- Living sectarian traditions: Vaishnavism, Shaivism, Shaktism, Smartism
- **Ajivika** — extinct fatalist sect exactly contemporary with the Buddha and Mahavira (c. 500 BCE); critical for the axial-age Indian context
- **Charvaka / Lokayata** — ancient Indian materialist/atheist school; refutes the idea that ancient India had no skeptics
- **Jainism** — 24 Tirthankaras, Mahavira, ahimsa doctrine, karma as physical substance; currently only mentioned in `tenet-systems.csv`
- **Suggested files:** `pie-origins/vedic-gods-and-schools.csv`, `buddhism-dharma/jainism-and-ajivika.csv`

#### 3. Celtic / Druidic religion
The western European counterpart to Vedic Brahmanism — both are priestly classes of the same PIE stock. Ancient sources (Caesar, Strabo, Diodorus) explicitly compare druids to Pythagoreans.

- Druidism: oral transmission, sacred groves, tripartite cosmology, metempsychosis
- Continental Celtic pantheon: Cernunnos, Epona, Lugus, Taranis, Esus, Sucellus
- Insular Celtic tradition: Irish mythological cycles, Welsh Mabinogion
- Parallels with Brahmin priestly function in the PIE lineage
- **Suggested file:** `pie-origins/celtic-druidic-religion.csv`

#### 4. Norse / Germanic religion
Baldur is a dying-and-rising god figure that rarely appears in comparative religion surveys of the Mediterranean chain, but belongs to it structurally.

- Norse pantheon: Odin (wandering sage/shaman), Thor (storm), Freya (love/war/seiðr), Baldur (dying god), Loki (trickster), Tyr (law)
- Ragnarök eschatology: world-ending, rebirth cycle — structural parallel to Zoroastrian *Frashokereti*
- Yggdrasil world-tree: nine realms cosmology, parallel to other PIE cosmic trees
- Seiðr: Norse shamanic practice, linked via steppe tradition to Siberian shamanism
- Eddas (*Prose* and *Poetic*) as primary source material
- **Suggested files:** `pie-origins/norse-germanic-religion.csv`, `pie-origins/eddas-index.csv`

#### 5. Atenism / Amarna religion
The earliest documented state monotheism (c. 1353–1336 BCE). Freud's *Moses and Monotheism* argues direct continuity to Israelite monotheism; the scholarly debate is live.

- Aten as sole solar deity: no mythology, no image — purely abstract creator
- Akhenaten's *Great Hymn to Aten* as structural precursor to Psalm 104
- Sudden collapse under Tutankhamun and erasure from the record
- Possible diffusion into Levantine priestly traditions
- **Suggested file:** `abrahamic/atenism-timeline.csv` or `pie-origins/atenism-timeline.csv`

---

### 🟡 Medium priority

#### 6. Sufism / Islamic mysticism
You have Al-Farabi, Avicenna, Suhrawardi, and Averroes in the philosophers list, but no organized Sufi coverage despite Sufism being the direct descendant of Islamic Neoplatonism and having strong structural parallels to Gnostic and mystery-cult traditions.

- Major Sufi orders: Qadiriyya, Naqshbandiyya, Mevlevi (Rumi), Chishti, Suhrawardiyya
- Al-Hallaj (d. 922): executed for saying *"Ana'l-Haqq"* ("I am the Truth") — direct messianic parallel
- Ibn Arabi (1165–1240): *Fusus al-Hikam* — the most elaborate Islamic Neoplatonism; doctrine of *wahdat al-wujud* (unity of being)
- Rabia al-Adawiyya (c. 714–801): female Sufi saint, theology of divine love; predates most Western mystical women
- **Suggested file:** `mystery-cults/sufi-orders-and-figures.csv`

#### 7. Yazidism
A living syncretic religion in Kurdistan that preserves identifiable elements of Zoroastrianism, Mithraism, Neoplatonism, and angel-worship.

- Malak Tawus (Peacock Angel): rehabilitated Iblis / Lucifer figure; parallel to light-bearer traditions
- Connection to Melek Taus / Mithras solar symbolism
- Oral sacred texts: *Kitab al-Jilwa*, *Maṣḥaf Raš*
- Persecution history: declared heretics by Islamic authorities, recent genocide under ISIS (2014)
- **Suggested file:** `mystery-cults/yazidism.csv`

#### 8. Phoenician / Canaanite religion (beyond Baal cycle)
The Baal cycle is well covered. What is missing is the broader pantheon and its links to Israelite religion.

- **El** — head of the Ugaritic pantheon, father-god; cognate with Hebrew *Elohim*; merges with YHWH in later Israelite religion
- **Asherah** — consort of El; wooden pillar / tree cult; 40+ times mentioned in Hebrew Bible; actively suppressed by Deuteronomistic reform
- **Mot** — death god, Baal's antagonist; fully present in Baal cycle but not indexed separately
- **Tanit** — Carthaginian mother goddess; identified with the heavenly virgin; tophet sacrifice controversy
- **Kothar-wa-Khasis** — divine craftsman; parallel to Hephaestus, Ptah, Tvashtr
- **Suggested file:** `comparative-myths/phoenician-canaanite-gods.csv`

#### 9. Hittite / Anatolian religion
The Hittites are the documentary bridge between Mesopotamia and Greece. Several Greek myths have their earliest known form in Hittite tablets.

- **Tarhunt / Teshub** — storm god; cognate with Baal, Indra, Zeus; the Hittite version of the PIE storm god is the best attested early form
- **Disappearing god myth** (Telipinu): the deity vanishes, nature dies, ritual restores them — the earliest clearly attested dying-and-returning deity narrative
- **Myth of Illuyanka**: dragon-slaying myth; parallel to Baal–Yamm, Indra–Vritra, Zeus–Typhon; precursor to the Greek Typhon myth
- **Kubaba/Cybele origin**: Kubaba was a Hittite/Hurrian goddess who became the Phrygian Cybele, then the Roman Magna Mater
- **Kingship in Heaven**: Hittite succession myth, virtually identical to Hesiod's *Theogony* (Anu → Kumarbi → Teshub = Ouranos → Kronos → Zeus)
- **Suggested file:** `pie-origins/hittite-anatolian-religion.csv`

#### 10. Jainism and Ajivika
Both are 6th-century BCE Indian movements directly contemporary with the Buddha's reform, and together they define the full spectrum of heterodox Indian thought.

- Jainism: 24 Tirthankaras, Mahavira's life parallel to the Buddha, ahimsa, karma as physical substance
- Ajivika: founded by Makkhali Gosala; absolute determinism (niyati); denied free will entirely; now extinct; referenced in Buddhist and Jain sources as a major rival
- **Suggested file:** `buddhism-dharma/jainism-and-ajivika.csv`

#### 11. Ismaili cosmology / Druzism
Ismaili Islam is the most thoroughly Neoplatonist branch of Islamic thought.

- Ismaili emanation cosmology: almost identical in structure to Plotinus's hypostases
- Fatimid caliphate (909–1171): Ismaili theocracy in Cairo
- Druzism (11th century, Lebanon/Syria): offshoot emphasizing secret scripture, transmigration of souls, cyclic cosmic history
- Assassins / Nizari Ismailis: Hassan-i Sabbah's esoteric hierarchical order
- **Suggested file:** `mystery-cults/ismaili-druzism.csv`

---

### 🟢 Lower priority (but worth queuing)

| Tradition | Why relevant | Suggested file |
|---|---|---|
| **Daoism** | Chinese correlate to logos, wu-wei as grace; Daoist immortality parallels; complete absence is notable | `east-asian/daoist-traditions.csv` |
| **Bon religion** | Pre-Buddhist Tibet; connection to steppe shamanism; how absorbed into Vajrayana | `buddhism-dharma/bon-religion.csv` |
| **Tengrism** | Sky-god religion of Mongols and Turks; underlies steppe-cult coverage | `pie-origins/tengrism-steppe-shamanism.csv` |
| **Siberian shamanism** | Source layer for many Eurasian religious motifs (three worlds, spirit journeys) | `pie-origins/siberian-shamanism.csv` |
| **Michael Psellus / Byzantine Neoplatonism** | Byzantine transmission of Neoplatonism; revival of Iamblichan theurgy | philosophers-list.csv ✓ |
| **Sikhism** | 16th-century synthesis of Hinduism and Islam; Guru Granth Sahib as comparative text | `abrahamic/sikhism.csv` |
| **Yoruba / Ifá** | Extensive angel/orisha hierarchy; divination system; diaspora (Candomblé, Santería, Vodou) | `comparative-myths/yoruba-ifa.csv` |
| **Aztec / Mesoamerican religion** | Independent development of sacrificial soteriologies, calendrical eschatology | `pie-origins/mesoamerican-religion.csv` |
| **Rosicrucianism** | 17th-century synthesis of Hermeticism, Kabbalah, alchemy; predecessor to Theosophy | `esoteric/rosicrucianism.csv` |
| **Theosophy** | 19th-century synthesis of Eastern and Western esotericism; highly relevant to modern perennialism | `esoteric/theosophy.csv` |
| **Confucianism** | State ideology; ritual propriety as religious practice; comparative heaven (Tian) | `east-asian/confucianism.csv` |

---

## Recommended build order

1. `pie-origins/mesopotamian-pantheon.csv` — the missing foundation layer
2. `pie-origins/sumerian-myth-cycles.csv` — Inanna, Gilgamesh, Enuma Elish
3. `pie-origins/hittite-anatolian-religion.csv` — Telipinu, Kingship in Heaven, Kubaba→Cybele
4. `comparative-myths/phoenician-canaanite-gods.csv` — El, Asherah, Mot, Tanit
5. `abrahamic/atenism-timeline.csv` — Akhenaten's monotheistic revolution
6. `pie-origins/celtic-druidic-religion.csv` — western PIE priestly tradition
7. `pie-origins/norse-germanic-religion.csv` — Baldur, Ragnarök, Yggdrasil
8. `pie-origins/vedic-gods-and-schools.csv` — Rigveda pantheon + six darshanas
9. `buddhism-dharma/jainism-and-ajivika.csv` — axial-age Indian heterodox schools
10. `mystery-cults/sufi-orders-and-figures.csv` — Islamic mysticism
11. `mystery-cults/yazidism.csv` — surviving syncretic light-cult
12. `mystery-cults/ismaili-druzism.csv` — Neoplatonist Islam and its offshoots
