# Agent instructions (Messiah-Complex)

This repository is a **Docusaurus 3** site (`messiah-docs`). Agents editing content should follow this file so work stays **consistent**, **navigable**, and **honest about evidence**.

## Read first

| Doc | Purpose |
| --- | --- |
| [`docs/overview/method-evidence-and-influence.md`](docs/overview/method-evidence-and-influence.md) | **Typology vs genealogy**, **tiers of claim**, fragmentary evidence, assisted collation |
| [`docs/research/about-research-notes.md`](docs/research/about-research-notes.md) | **Curated vs raw** research material |
| [`docs/overview/research-backlog.md`](docs/overview/research-backlog.md) | **Queued topics** (tables + **§ Detailed checklists**); pick one ID or one checklist line per pass |
| [`docs/overview/curated-page-template.md`](docs/overview/curated-page-template.md) | **Standard sections** for new/expanded pages (Context, consensus, tiers, Sources & dating) |

## Page structure (curated docs)

New or heavily expanded **overview** and **figure** pages should follow **[Curated page template](docs/overview/curated-page-template.md)**: **Context** (audience, question, scope), **Consensus snapshot**, **Debates / tiers**, **See also**, **Sources & dating**. Put **shared milieu** on hub pages and **link** instead of duplicating long blocks.

## Editorial stance

- **Separate** motif similarity from historical genealogy. Label **hypothesis** and **minority** views explicitly; do not state speculative chains as fact.
- **Curated** pages live under `docs/overview/` and `docs/figures/`. They should match the site’s tone: precise, tier-aware, minimal decorative bolding (do **not** bold every word).
- **Raw** compilations live under `docs/research/`. Treat claims there as **leads**, not verified conclusions.

## When adding or changing docs

1. **New doc** → register in [`sidebars.ts`](sidebars.ts) under the right category (Overview, Mithra & transmission, Figures, etc.).
2. **Cross-link** from relevant hubs: [`docs/mithras.md`](docs/mithras.md), topic siblings, and [`docs/overview/further-reading.md`](docs/overview/further-reading.md) when appropriate.
3. **Frontmatter**: include `title`, and usually `description` for SEO/sidebar tooltips.
4. **References**: prefer primary witnesses, peer-reviewed books/articles, and standard reference works (e.g. Encyclopaedia Iranica). Flag blogs and forums as orientation-only when used.

## Verification

- After substantive Markdown or config changes, run **`npm run build`** and fix broken links or build errors.
- **Node**: `>=20` (see `package.json`).

## Self-guided workflow (recommended)

1. Open [`docs/overview/research-backlog.md`](docs/overview/research-backlog.md) (or user-specified queue).
2. Take **one** item (or one clearly scoped batch); implement it end-to-end.
3. Update backlog / “See also” / hub links as needed.
4. Run `npm run build`; resolve failures.
5. Summarize what changed and what remains—then stop unless the user asks to continue.

## Avoid

- Drive-by refactors of unrelated files or large formatting-only churn.
- Presenting **Tier C** speculation as consensus.
- Duplicating the same content across many pages without linking to a single canonical overview.
- Adding long URL dumps or unvetted claims without tier labeling.

## Tech reference

- **Dev server**: `npm start`
- **Production build**: `npm run build`
- **Docs root**: `docs/` (plugin `path: 'docs'` in Docusaurus config)
