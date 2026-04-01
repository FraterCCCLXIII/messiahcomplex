---
sidebar_position: 11
title: Research backlog
description: Queued topics, citation gaps, infrastructure, and hygiene—not commitments; use with AGENTS.md for self-guided work.
---

# Research backlog

Items tracked for **future** work—**not** commitments. Agents and humans: take **one** row or checklist block per pass when possible; run `npm run build` after edits. See [Method: evidence, influence, and milieu](method-evidence-and-influence.md) and repo root `AGENTS.md`.

**Legend:** **H** = high impact, **M** = medium, **L** = low / nice-to-have.

---

## 1. Citations, “Sources & dating,” and evidence hygiene

| ID | Priority | Task | Notes |
| --- | --- | --- | --- |
| C1 | **done** | Replace stub **Sources & dating** on first three figure pages | [Christianity: Parousia](../figures/christianity-parousia.md), [Zoroastrian: Saoshyant](../figures/zoroastrian-saoshyant.md), [Roman Mithraism](../figures/roman-mithraism.md). |
| C2 | H | **Context** + **Sources & dating** on **remaining figure pages** | Use [Curated page template](curated-page-template.md). See **§ Detailed checklists → Figure pages** below. |
| C3 | **done** | Site-wide **Sources** guidance + template | [About research notes](../research/about-research-notes.md), [curated-page-template](curated-page-template.md), AGENTS. |
| C4 | M | Overview pages: **non-obvious claims** need citations | Prioritize [Gandhara](gandhara-central-asian-transmission.md), [Achaemenid and West Asian Judaism](achaemenid-and-west-asian-judaism.md), [Measuring influence](measuring-influence-mitra-maitreya.md), [alternative Buddha–Jesus theories](alternative-buddha-jesus-transmission-theories.md), [Paul / Mithra notes](paul-mithraism-and-historicity-notes.md). |
| C5 | M | **Overview pages: Context block** where missing | [Curated page template](curated-page-template.md) **Audience / Question / Scope** on major overviews (see **§ Overview pages** below). |
| C6 | L | **External URLs** in `further-reading` and appendices | Periodic check for link rot; archive.org fallbacks where needed. |

---

## 2. Content depth (research topics)

| ID | Priority | Task | Notes |
| --- | --- | --- | --- |
| R1 | M | **Dioskouroi / Danubian** twin reliefs | Epigraphic and art-historical depth beyond [PIE twins](pie-twin-and-brother-archetypes.md). |
| R2 | M | **Islam — Mahdi** | Shiʿi nuance, literature surveys; overlaps [figures/islam-mahdi](../figures/islam-mahdi.md) + C2. |
| R3 | M | **Numismatics appendix** | Kushan radiate types, identification caveats; link from [Helios, Apollo, and Sol](helios-apollo-sol-syncretism.md) and [Gandhara](gandhara-central-asian-transmission.md). |
| R4 | L | **Syriac / Ethiopian** frontiers | Messianic and mediator idioms east of Greece—only if scope widens. |
| R5 | M | **Further reading** split | Subpages by topic if [further-reading](further-reading.md) exceeds easy maintenance. |
| R6 | M | **Eurasian wide-sample motif clustering** | Systematic corpus comparison (mystery cults, hagiography, epic) with explicit tiering; align with [Method](method-evidence-and-influence.md). |
| R7 | L | **Chronological map** / **Visual timeline** | Verify dates against sources; add “how to read”; citations for milestones. `visual-timeline.mdx` — keep MDX/React valid when editing. |
| R8 | M | **Mediterranean glossary** / **appendix** cross-check | [Mediterranean figure glossary](mediterranean-figure-glossary.md), [mystery sources appendix](mediterranean-mystery-sources-appendix.md) — dedupe, broken links. |
| R9 | L | **Intro** refresh | [intro.md](../intro.md): add any missing first-class entry points (e.g. [curated-page-template](curated-page-template.md), transmission pages). |
| R10 | L | **Method** page optional **Context** header | Parity with other hubs; short Audience / Question / Scope. |
| R11 | M | **Mythic biography patterns** page | Reduce excessive **bold**, add **Sources** subsection for typology references (Lopez, comparative handbooks). |
| R12 | L | **Research backlog** meta | Keep this file’s **§ Detailed checklists** in sync as rows close. |
| R13 | M | **Bardiya-Gaumāta / Buddha theory** | Expanded on [Śaka–Scythian hypotheses](saka-scythian-hypotheses.md); could benefit from additional primary Behistun refs and Indological responses. |
| R14 | M | **Barlaam & Josaphat (Bodhisattva)** | Added to [alternative theories](alternative-buddha-jesus-transmission-theories.md); expand with Arabic transmission details and hagiographic variants. |
| R15 | M | **Mahāyāna emergence & Silk Road** | Expanded on [Amitābha page](amitabha-maitreya-gandhara-transmission.md); deeper treatment of Khotan, Kucha, and Turfan manuscript evidence. |
| R16 | M | **Celestial savior motif** (Amitābha, Christ, Mithra, Osiris) | Comparative table added to Amitābha page; could become standalone typological article. |
| R17 | M | **Horseback heroes** (Michael, Dioscuri, Kalki, George, Thracian) | Comparative section on [Thracian horseman](thracian-horseman-paleo-balkan.md); potential for standalone article with iconographic evidence. |
| R18 | H | **More figures** | Added Heracles, Gilgamesh, Dumuzi/Tammuz, Orpheus, Elijah & Enoch. Still missing: Prometheus, Adonis, Baal (as figure page), Quetzalcoatl. |

---

## 3. Mithra dossier and raw compilation

| ID | Priority | Task | Notes |
| --- | --- | --- | --- |
| M1 | M | ~~**Curate** excerpts from Mithras source compilation into overview pages~~ **Done** — compilation curated and removed | Tier-labeled moves complete. |
| M2 | L | **TOC / index** at top of raw compilation | ~800+ lines; anchor links to major sections. |
| M3 | M | [Mithra hub](/docs/mithras): **coverage** pass | Every row in topic table still valid; add missing cross-refs (e.g. [alternative theories](alternative-buddha-jesus-transmission-theories.md), [Paul notes](paul-mithraism-and-historicity-notes.md)). |
| M4 | L | **Figures** or **diagram** for Kushan / Gandhara timeline | Optional visual in [visual-timeline](visual-timeline.mdx) or map page. |

---

## 4. Site infrastructure and quality

| ID | Priority | Task | Notes |
| --- | --- | --- | --- |
| I1 | M | **CI** (GitHub Actions, etc.) | `npm run build` on push/PR; optional `npm run typecheck`. |
| I2 | L | **Internal link checker** | CI or script for `docs/**/*.md` + `.mdx`. |
| I3 | L | **Git** + **.gitignore** | If not versioned: `node_modules/`, `build/`, `.docusaurus/`; document workflow. |
| I4 | L | **README.md** (repo root) | Clone, `npm install`, `npm start`, `npm run build`, links to `AGENTS.md`, [Method](method-evidence-and-influence.md), [intro](../intro.md). |
| I5 | L | **SEO / social** | `docusaurus.config.*`: metadata, OG image, canonical URL if deployed. |
| I6 | L | **CONTRIBUTING.md** | How to propose edits, evidence tier rules, run build before PR. |
| I7 | L | **LICENSE** | Choose license if repo goes public. |
| I8 | L | **Dependabot** / **npm audit** | Periodic dependency updates; security alerts. |
| I9 | L | **Algolia DocSearch** or local **search** tuning | If site is public and large enough to qualify. |
| I10 | L | **i18n** | Only if non-English locales are planned. |

---

## 5. Editorial hygiene

| ID | Priority | Task | Notes |
| --- | --- | --- | --- |
| E1 | L | **Bold** normalization | Legacy per-word bold (e.g. [mythic biography](mythic-biography-patterns-prophet-and-buddha-analogy.md)); fix when touching files. |
| E2 | L | **Tier** disclaimer duplication | Short pointer to [Method](method-evidence-and-influence.md) vs repeating full paragraph on every page. |
| E3 | L | **Accessibility** | Heading order, table captions, `alt` on future images. |
| E4 | L | **MDX** validity | [visual-timeline.mdx](visual-timeline.mdx): no broken imports; build after edits. |

---

## 6. Detailed checklists (granular queues)

### Figure pages — Context + Sources & dating (C2)

Track in commits; remove lines here when done.

- [ ] [Judaism: Mashiach](../figures/judaism-mashiach.md)
- [ ] [Buddhism: Maitreya](../figures/buddhism-maitreya.md)
- [ ] [Islam: Mahdi](../figures/islam-mahdi.md)
- [ ] [Hinduism: Kalki](../figures/hinduism-kalki.md)
- [ ] [Taoism: Li Hong](../figures/taoism-li-hong.md)
- [ ] [Norse: Baldr](../figures/norse-baldr.md)
- [ ] [Arthurian: King Arthur](../figures/arthurian-king-arthur.md)
- [ ] [Dionysus / Bacchus](../figures/greco-roman-dionysus.md)
- [ ] [Asclepius](../figures/greco-roman-asclepius.md)

### Overview pages — optional Context block (C5)

Add **Audience / Question / Scope** where it helps; not every sub-appendix needs full treatment.

**Start here:** [method-evidence-and-influence](method-evidence-and-influence.md) (optional R10), [exploring-transmission-and-deep-patterns](exploring-transmission-and-deep-patterns.md), [mythic-biography-patterns](mythic-biography-patterns-prophet-and-buddha-analogy.md), [eurasian-mediator-figures-assessment](eurasian-mediator-figures-assessment.md), [messiah-language-greek-civic-context](messiah-language-greek-civic-context.md), [emperor-cult-and-civic-soter](emperor-cult-and-civic-soter.md).

**Transmission & influence:** [saoshyant-influence-hypotheses](saoshyant-influence-hypotheses.md), [achaemenid-and-west-asian-judaism](achaemenid-and-west-asian-judaism.md), [evidence-leads-persian-milieu-and-mitra-cluster](evidence-leads-persian-milieu-and-mitra-cluster.md), [measuring-influence-mitra-maitreya](measuring-influence-mitra-maitreya.md), [indo-iranian-mitra-contract](indo-iranian-mitra-contract.md), [gandhara-central-asian-transmission](gandhara-central-asian-transmission.md), [amitabha-maitreya-gandhara-transmission](amitabha-maitreya-gandhara-transmission.md), [saka-scythian-hypotheses](saka-scythian-hypotheses.md), [alternative-buddha-jesus-transmission-theories](alternative-buddha-jesus-transmission-theories.md), [paul-mithraism-and-historicity-notes](paul-mithraism-and-historicity-notes.md).

**Mithra & Roman:** [mithra-roman-manichaean](mithra-roman-manichaean.md), [manichaean-mihr-soteriology](manichaean-mihr-soteriology.md).

**Mediterranean & Paleo-Balkan:** [pie-twin-and-brother-archetypes](pie-twin-and-brother-archetypes.md), [pie-motifs-atu-thompson-and-hero-traditions](pie-motifs-atu-thompson-and-hero-traditions.md), [greek-wandering-gods-initiation](greek-wandering-gods-initiation.md), [hermes-mediator-and-initiation](hermes-mediator-and-initiation.md), [thracian-horseman-paleo-balkan](thracian-horseman-paleo-balkan.md), [philippi-via-egnatia-religious-milieu](philippi-via-egnatia-religious-milieu.md), [helios-apollo-sol-syncretism](helios-apollo-sol-syncretism.md), [attis-and-cybele](attis-and-cybele.md), [isis-osiris-serapis](isis-osiris-serapis.md), [demeter-eleusis-mysteries](demeter-eleusis-mysteries.md), [mediterranean-mystery-sources-appendix](mediterranean-mystery-sources-appendix.md), [hero-cult-and-mystery-cult-atlas](hero-cult-and-mystery-cult-atlas.md), [mediterranean-figure-glossary](mediterranean-figure-glossary.md).

**Time & maps:** [chronological-map](chronological-map.md), [visual-timeline](visual-timeline.mdx) (R7, E4).

---

## 7. Quick checklist (agent-friendly)

- [ ] Pick **one** ID (e.g. C2 + one figure) or **one** checklist line  
- [ ] Update **See also** / hubs if cross-refs added  
- [ ] Run **`npm run build`** (and fix MDX if `visual-timeline` touched)  
- [ ] Mark checklist lines or table rows done in this file when finished  

---

## See also

- [Curated page template](curated-page-template.md)  
- [Method: evidence, influence, and milieu](method-evidence-and-influence.md)  
- [About research notes](../research/about-research-notes.md)  
- [Further reading](further-reading.md)  
