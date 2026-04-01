---
sidebar_position: 2
title: Curated page template
description: Standard sections for overview and figure pages — opening orientation, numbered content, tier statement, sources — with guidance on each element.
---

# Curated page template

Use this pattern for **overview** and **figure** pages. The best pages on this site share a consistent structure: a single strong opening paragraph, numbered content sections, an explicit tier statement, and organized sources. The three-bullet "Context" format is retired — it produced lists where paragraphs belong.

**Worked examples of pages that follow this pattern well:**
- [The PIE cosmic combat myth](pie-cosmic-combat-myth.md) — opening paragraph + numbered sections + tier table
- [Daniel and Iranian eschatology](daniel-and-iranian-eschatology.md) — opening paragraph + crisis framing + numbered content
- [Dead Sea Scrolls dualism and Iranian parallels](dead-sea-scrolls-dualism-and-iranian-parallels.md) — concise opener + structured parallels + tier-aware conclusion

---

## Template (copy from here)

````markdown
---
title: …
description: One sentence: what this page covers and why it matters for the site's argument.
---

# Page title

One or two sentences that immediately state what this page is about and why it exists on this site specifically. Do not open with a definition. Open with the thesis relevance: what question does this page answer, and how does it connect to the site's structural argument (porous milieu, cosmic mediator slot, empire–crisis–translation, two-wave model, etc.).

> **Scope note.** What this page does *not* cover — link to the pages that do handle those adjacent topics.

---

## 1. [First major section — what specialists broadly agree on]

Write two or three paragraphs of dense explanatory prose — not a bullet list of accepted facts. Explain *why* the consensus holds: what the evidence is, what it would take to overturn it, and why this stability matters for the argument you are building. Bold key technical terms on first use. Label tier inline at the end of the relevant paragraph.

For example: *"The book of Daniel is almost universally dated by critical scholars to the Maccabean crisis (~167–164 BCE) rather than the 6th-century Babylonian setting it claims. The grounds are decisive: the historical detail in Daniel 8–12 is accurate to within a year for events up to the desecration of the Temple by Antiochus IV Epiphanes, then vague and factually wrong for events after that date — exactly the pattern produced by a writer narrating the past as prophecy rather than predicting the future. Additionally, Daniel does not appear in Ben Sira's list of great Israelites (~190 BCE), a near-certain sign it had not yet been composed. (Tier A.)"*

---

## 2. [Second section — the main comparative or historical argument]

Write the core argument in paragraphs. When the argument makes a claim that depends on a prior claim, name the dependency: "this matters because," "the implication is," "notice that." Subsections (### 2a, ### 2b) are fine when the section covers genuinely distinct components — but the subsections should each be paragraphs, not labeled bullet points.

Use tables for structured comparisons across multiple traditions or time periods — they are far more readable than parallel bullets. But always precede a table with a paragraph that explains what the table is showing and what conclusion to draw from it.

| Tradition | Figure | Key feature | Source |
| --- | --- | --- | --- |
| … | … | … | … |

Label tier inline at the end of each paragraph where the tier is less than A: *(Tier B: specialist debate, directional evidence.)*

---

## 3. [Third section — debates, minority views, methodological limits]

Name the actual schools of thought, including the scholars who hold them. Write the position of each school as a paragraph, not a bullet. State what would need to be true for each position to be correct, and what evidence would falsify it. Avoid phrases like "some scholars argue" — name the scholars. This is where *Tier C* (working hypothesis; named mechanism) and *Tier D* (analogy only; no documented transmission) claims belong, and they should be explicitly labeled as such.

---

## 4. Tier statement

A summary table of the page's key claims and their evidential status. Every substantive page should have one.

| Claim | Tier | Notes |
| --- | --- | --- |
| [Specific claim] | **Tier A** | Philologically/archaeologically secure |
| [Specific claim] | **Tier B** | Probable; directional evidence; specialist debate |
| [Specific claim] | **Tier C** | Working hypothesis; named mechanism; falsifiable |
| [Specific claim] | **Tier D** | Analogy / heuristic only |

See [Method: evidence, influence, and milieu](method-evidence-and-influence.md) for tier definitions.

---

## 5. Implications for the site's thesis *(optional but encouraged)*

A short section connecting this page's content back to the site's structural arguments. Which of these applies?

- Does this page supply evidence for the **empire–crisis–translation model**? Name the empire, the crisis, and the translation event.
- Does this page populate the **cosmic mediator slot** or the **cosmic adversary slot**? Where does this figure sit in the comparative table?
- Does this page exemplify **Wave 1 (PIE pastoralist dispersal)** or **Wave 2 (Axial Age imperial contact)**?
- Does this page illustrate the **porous milieu model** — shared conceptual environment rather than direct borrowing?

---

## See also

3–8 internal links. Include the relevant hub page(s), the closest sibling pages, and the method page if the tier situation is complex.

---

## Sources & dating

### Tier A — primary evidence

| Witness / work | Language | Approx. date | Notes |
| --- | --- | --- | --- |
| … | … | … | Edition, standard translation, key caveats |

### Tier B — specialist analyses

Monographs and journal articles that constitute the scholarly debate (full bibliographic lines).

### Standard reference works

Encyclopaedia Iranica entries, Oxford Classical Dictionary, etc.

---

*Raw research material belongs in `docs/research/` with a link back from this page. See [About research notes](../research/about-research-notes.md).*
````

---

## Guidance notes

### Write in paragraphs — this is the most important rule

The single biggest difference between a useful page on this site and a forgettable one is whether it is written in **explanatory prose paragraphs** or in bullet lists. Bullets are a writing shortcut that strips out all the connective tissue — the "because," "this matters because," "notice that," "the consequence is" — that makes an argument comprehensible. Pages written as bullet lists feel like outlines. Pages written as paragraphs carry the reader through the logic.

**The rule:** If something can be stated as a bullet, ask whether it should instead be a sentence inside a paragraph. The answer is almost always yes.

**Bullets are appropriate only for:**
- Genuinely enumerable items with no argumentative sequence (e.g., a list of known archaeological sites at a location, a list of 7 textual witnesses)
- Comparative tables, where the grid structure IS the argument
- "See also" link lists

**Bullets are not appropriate for:**
- The consensus snapshot — this should be a paragraph explaining what scholars agree on and why, not a list of checked boxes
- The context or opening orientation — this should be a paragraph framing the question, not a form to fill in
- Any argument that builds across multiple claims — the connections between claims are where the understanding lives

**What dense explanatory prose looks like:** When explaining a concept, don't just state it — explain *why* it is what it is, what the alternative would be, and what it implies for the adjacent argument. For example, instead of:

> - The Yamnaya were a mixed EHG + CHG population (~50%/50%)

write:

> The Yamnaya — the archaeological population whose dispersal carried the PIE religious grammar across Eurasia — were not an original pure source. They were themselves the product of a prior contact event between Eastern European Hunter-Gatherers from the Russian steppe and a distinct Caucasus Hunter-Gatherer population, each contributing roughly half the genetic ancestry. This matters for how the site's argument is framed: there is no clean "Aryan original" at any layer of the chronology. Even the substrate was a synthesis. The porous milieu model applies recursively from the earliest recoverable layer.

The second version takes longer to read but actually teaches something. That density is the target.

---

### The opening paragraph
This is the most important sentence on the page. It should do three things: (1) name the subject clearly, (2) state immediately why it matters for this site's comparative argument, (3) orient the reader toward the specific question the page answers. Do not open with "X is a concept in tradition Y." Open with the thesis relevance. Write it as a paragraph — never as labeled bullets.

### The scope note
A blockquote `> **Scope note.**` near the top explicitly names what the page does *not* cover and links to the pages that do. This prevents content duplication and makes the page easier to navigate. It is especially important for pages that cover one zone of a larger multi-page topic.

### The consensus snapshot — write it as prose
The consensus snapshot should be **two or three explanatory paragraphs**, not a bullet list of accepted facts. Explain *why* scholars accept what they accept — what the evidence is, what would overturn it, and why the consensus matters for the page's argument. A bullet list of datings and attributions is an index, not an explanation.

### Numbered sections
Numbering content sections (## 1, ## 2, ## 3) makes pages easier to cite, cross-link, and navigate. Use subsection headers (### 2a, ### 2b) freely when a section has multiple distinct components. Don't add numbers to See also, Sources, or the Tier statement.

### The tier statement table
Every substantive page should end its content with a tier statement table that summarizes the page's key claims and their evidential status. This is not a summary of the page — it is a transparent accounting of what the page is and is not claiming. The tier definitions are at [Method: evidence, influence, and milieu](method-evidence-and-influence.md). Inline tier labels *(Tier B: ...)* in prose are also encouraged but don't replace the summary table.

### Inline vs. deferred tier labeling
Label tier inline as the claim is made — *(Tier B: specialist debate, directional evidence)* appended to the relevant paragraph — and use a dedicated debates section only for extended treatment of genuine scholarly disagreement where the evidence is genuinely unresolved. Do not defer all qualifications to the end: it makes the main content read as more confident than it is.

### Tables vs. bullets for comparisons
For parallel comparisons across traditions (same figure in five traditions, same concept across five time periods), a table is almost always more readable than bullet lists. Use bullets only for genuinely non-parallel enumerations. When a comparison has a column structure, use a table.

### Shared milieu — do not duplicate
Long background blocks (e.g., the Achaemenid administrative context, the Kushan trade infrastructure, the Roman mystery ecology) should live on **one** hub page. Leaf pages link there rather than duplicating. The main hubs are: [Messianic archetypes](messianic-archetypes.md), [Mithra cluster hub](/docs/mithras), [Gandhāra and Central Asian transmission](gandhara-central-asian-transmission.md), [Achaemenid empire and West Asian Judaism](achaemenid-and-west-asian-judaism.md), [PIE & ANE deep grammar](pie-ane-deep-grammar.md).

---

## See also

- [Method: evidence, influence, and milieu](method-evidence-and-influence.md) — tier definitions and the typology vs. genealogy distinction
- [About research notes](../research/about-research-notes.md) — when to use `docs/research/` instead
- [Research backlog](research-backlog.md) — queued topics
