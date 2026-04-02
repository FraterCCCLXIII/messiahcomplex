---
sidebar_position: 1
title: Contributing — humans and AI
description: How to add evidence, expand pages, and run AI agents against the research backlog. Both manual and AI-assisted contributions are welcome and expected.
---

# Contributing — humans and AI

Messiah Complex is a living research compilation, not a finished encyclopedia. Every page carries unresolved debates, citation gaps, and queued investigations. The [research backlog](research-backlog.md) makes those gaps explicit. This page explains how to close them — whether you are a human researcher, a developer, or someone who wants to point an AI agent at the queue and let it run.

> **Scope note.** This page covers contribution *workflow* — how to submit work and what standards it must meet. Editorial tone, evidence tiers, and page structure are governed by [Curated page template](curated-page-template.md) and [Method: evidence, influence, and milieu](method-evidence-and-influence.md). Read both before writing new pages.

---

## 1. What this project needs

The site spans three thousand years of religious history across a dozen traditions. No single person can maintain it at depth. The most useful contributions fall into four categories, roughly ordered by impact:

**Evidence and citations.** Most pages carry claims that are plausible but unsourced, or that cite secondary summaries rather than primary witnesses. The highest-value work is finding the actual Greek text, the actual excavation report, the actual journal article, and attaching it with the page number. Backlog item [C4](research-backlog.md) tracks the highest-priority pages for this work.

**New pages and expanded sections.** The [figures checklist](research-backlog.md#figure-pages--context--sources--dating-c2) names figure pages that need full treatment. The [overview checklist](research-backlog.md#overview-pages--optional-context-block-c5) names overview pages that need a proper opening and context. Item R18 and R19 name entirely new figures and survey pages that have never been started.

**Data review.** Several pages contain claims from popular sources that have not been checked against primary scholarship. Backlog item [R21](research-backlog.md) lists them individually with the specific questions that need answering. Finding that a claim is wrong is as valuable as finding that it is correct — the site's usefulness depends on distinguishing between them.

**Infrastructure.** The [§ 4 table](research-backlog.md#4-site-infrastructure-and-quality) lists CI, link checking, SEO, and dependency hygiene tasks that a developer can resolve without touching any content at all.

---

## 2. Manual contribution

### Getting started

The repository is a standard Git project. The workflow is:

1. Fork the repository on GitHub.
2. Run `npm install` and `npm start` to get a local preview.
3. Take **one** backlog item — one row from a table, one line from a checklist — not a broad sweep of the site.
4. Make the change, run `npm run build`, fix any errors.
5. Open a pull request describing what you changed and why the evidence supports it.

### Editorial standards

Every substantive addition should cite a source. The tier system makes this concrete:

| Tier | What it requires |
| --- | --- |
| **Tier A** | Primary witness — inscription, manuscript, excavation report, coin catalog — with the standard edition, folio, or accession number |
| **Tier B** | Peer-reviewed monograph or journal article; full bibliographic line |
| **Tier C** | A named hypothesis with a stated mechanism and a stated falsifier; labeled explicitly as hypothesis |
| **Tier D** | Structural analogy only; no claimed transmission; labeled as analogy |

**Do not assert Tier C claims without the label.** The most common error in popular comparative religion writing is presenting structural analogy as historical transmission. This site's value proposition is precisely that it names the difference.

The [curated page template](curated-page-template.md) explains the required prose style: explanatory paragraphs, not bullet lists; the opening paragraph carries the thesis relevance; numbered sections; a tier statement table at the end.

### Submitting raw research

If you have a collection of sources, a set of notes, or a transcript from a research session that has not been curated into clean prose, the right place for it is `docs/research/`. Raw material goes there; curated argument goes in `docs/overview/` or `docs/figures/`. See [About research notes](../research/about-research-notes.md) for the distinction. A link from the relevant curated page into the raw file is encouraged; the reverse (raw pages asserting conclusions) is not.

---

## 3. AI-assisted contribution

### The basic idea

The [research backlog](research-backlog.md) is structured specifically so that an AI agent can take a single item and execute it end-to-end. Each row has an ID, a priority, a task description, and notes pointing to the relevant page. Each checklist line names a single file. An agent that reads `AGENTS.md`, reads the backlog, picks one item, implements it, runs `npm run build`, and stops has done the canonical unit of useful work.

If you have access to an AI coding assistant (Cursor, Claude, GPT-4, Gemini, or any tool that can read files, write files, and run shell commands), you can point it at this repository with the following instruction pattern:

```
Read AGENTS.md and docs/overview/research-backlog.md.
Pick one item from the backlog — preferably a high-priority (H or M) item 
that has not been marked done.
Implement it end-to-end following the curated page template and the 
evidence tier rules.
Run npm run build. Fix any build errors.
Summarize what you changed and what remains.
Do not take more than one item per session.
```

That is the entire prompt. The agent will handle the rest if it reads the context files carefully.

### What agents are good at

AI agents excel at the specific kinds of work this backlog needs most:

**Expanding stubs into full pages.** Given the curated page template, an agent can take a one-paragraph stub on a figure like Li Hong or Asclepius and expand it into a properly structured page with numbered sections, consensus snapshot, debates, tier table, and sources list — drawing on its training data to fill in what specialists broadly agree on. The agent should label everything by tier and flag anything it is uncertain about.

**Drafting comparative tables.** The site uses tables to structure comparisons across traditions. An agent can draft a six-column comparison table for a claim like "celestial savior motif across four traditions" far faster than a human can, and the result can be reviewed and corrected by a human before it goes into curated content.

**Finding and formatting citations.** An agent with web-search access can locate full bibliographic details for a book or article mentioned in a page's notes section. Turning "Beckwith, *Greek Buddha* (2015)" into a complete citation with publisher, ISBN, and relevant chapter is exactly the kind of task that is tedious for humans and easy for agents.

**Cross-referencing and link hygiene.** An agent can scan all Markdown files for internal links, check whether the target files exist, and report broken references — useful for backlog item I2.

**Evidence verification from R21.** Each item in the [R21 investigation notes](research-backlog.md#r21--unverified-greco-buddhist-claims-from-popular-sources) names a specific claim, the source it appears in, and the specialist corpus where it should be checked. An agent with web access can work through these systematically, returning a verdict of confirmed, unconfirmed, or refuted with the relevant primary source quotation.

### What agents are not good at

**Tier inflation.** Agents trained on popular-web text have absorbed a great deal of popularized comparative religion that asserts Tier D analogies as Tier A facts. The most important editorial task when reviewing AI-generated content is checking that the tier labels in the prose actually match the evidence, not the agent's implicit confidence. If an agent writes "Mithras was born on December 25," that is a Tier D claim at best (no ancient source attests this); the agent may not flag it correctly.

**Primary-source verification without access.** An agent without web search or database access cannot verify a claim against a specific journal article or museum catalog entry. It can paraphrase what it has seen in its training data — which is not the same as checking the primary source. Agents should be explicit when they are drawing on training data rather than a verified source, and their output should be reviewed accordingly.

**Judgment calls on contested debates.** Whether the Mitra–Maitreya etymology is a Tier B or Tier C claim depends on engagement with specific specialists (Mayrhofer, Gershevitch, Karashima). An agent cannot adjudicate that debate — it can describe it, lay out the positions, and label them — but the tier call on contested interpretive questions is a human editorial judgment.

### Running agents on the data files

The `static/sources/` directory contains CSV data files used by some pages (timelines, source tables). If you want an agent to extend or review these:

- To **show a CSV as a table on a doc page**, put the file under `static/` (for example `static/sources/foo.csv`). In the doc, add an import and the component (after frontmatter, before the body is fine):

  ```mdx
  import {CsvTable} from '@site/src/components/CsvTable';

  <CsvTable src="/sources/foo.csv" caption="Optional caption." />
  ```

  The first CSV row is used as the table header. Use a **`.mdx`** file extension for that page so the import stays in scope in dev (same pattern as [Visual timeline](visual-timeline.mdx)). See [CSV viewer test](csv-viewer-test.mdx) and [Achaemenid complete history](../bardiya/achaemenid-complete-history.mdx#view-the-timeline-table) for live examples.
- The column structure of each CSV is described in comments or in the page that embeds it.
- Additions to CSV data should carry the same source discipline as prose — every row should have a verifiable source reference.
- The `Bardiya Timeline` CSV in particular has a detailed chronological schema; additions should preserve the date-format and source-column conventions.

When asking an agent to extend a CSV, provide the file path, ask it to read the existing rows first to understand the schema, and then add rows one claim at a time with explicit sourcing.

---

## 4. Reviewing existing data

### How to prioritize a data review pass

The backlog's [§ R21](research-backlog.md#r21--unverified-greco-buddhist-claims-from-popular-sources) section is the most urgent queue for data review: it names specific claims from popular sources that have not been verified. Each item states the claim, states where it appears, and states the specialist corpus where it should be checked. A systematic pass through that list — either manually or with an AI agent that has web access — would substantially improve the site's reliability.

For broader page-level review, the [§ C4 row](research-backlog.md) names the overview pages where non-obvious claims most need citations attached. A review pass on those pages involves reading each claim and asking: does this have a source? Is the source primary or secondary? Is the tier label accurate? Pages to prioritize in that pass, in order of current citation thinness: [Gandhāra and Central Asian transmission](gandhara-central-asian-transmission.md), [Achaemenid and West Asian Judaism](achaemenid-and-west-asian-judaism.md), [Measuring influence: Mitra, Maitreya](measuring-influence-mitra-maitreya.md), [Alternative Buddha–Jesus transmission theories](alternative-buddha-jesus-transmission-theories.md), and [Paul / Mithra notes](paul-mithraism-and-historicity-notes.md).

### What to do when you find an error

If you find a claim that is wrong — misattributed, mistranslated, sourced to a discredited work, or simply invented — the correct action is:

1. Find the accurate primary source or specialist analysis.
2. Replace the incorrect claim with the accurate one, labeled with tier and source.
3. If the claim was Tier C or D masquerading as Tier A, retain a note explaining what the popular source said and why it was incorrect — this is more useful to future readers than simply deleting the wrong version.
4. If the claim is in a raw research file (`docs/research/`), mark it in the notes with a status (unverified / confirmed / refuted) rather than deleting it — the raw files are explicitly a leads collection, not curated content.

---

## 5. Coordination and scope discipline

The single most important workflow rule is: **take one item per session**. The site has almost a hundred pages and a hundred backlog items. An agent or contributor who takes a broad mandate — "improve all the figure pages" — will produce uneven work across many files, make it hard to review, and introduce inconsistencies. An agent or contributor who takes item C2 for one specific figure page, completes it end-to-end with build verification, and stops has done something reviewable and mergeable.

The second rule is: **run `npm run build` before submitting**. Docusaurus has strict link validation; a broken internal link or a missing frontmatter field will cause the build to fail. The build check is the minimum quality gate.

If you are running multiple AI agents in parallel — each working on a separate backlog item — coordinate by marking items as in-progress in the backlog file before assigning them, to avoid duplicate work.

---

## See also

- [Research backlog](research-backlog.md) — the full queue of items, with IDs, priorities, and notes
- [Curated page template](curated-page-template.md) — required page structure for overview and figure pages
- [Method: evidence, influence, and milieu](method-evidence-and-influence.md) — tier definitions and the typology vs. genealogy distinction
- [About research notes](../research/about-research-notes.md) — when raw material belongs in `docs/research/` rather than curated content
- [Further reading](further-reading.md) — key reference works that agents should know about before expanding any section
