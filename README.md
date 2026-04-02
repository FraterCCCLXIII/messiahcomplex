# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

## Installation

```bash
yarn
```

## Local Development

```bash
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```bash
yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Viewing CSV data on a page

CSV files under `static/` (for example `static/sources/foo.csv`) can be shown as an HTML table in any doc page with the `CsvTable` MDX component:

```mdx
<CsvTable src="/sources/foo.csv" caption="Optional caption." />
```

The first row is treated as the header. See [`docs/overview/contributing.md`](docs/overview/contributing.md) for details and [Achaemenid complete history](docs/bardiya/achaemenid-complete-history.md#view-the-timeline-table) for a live example.

## Deployment (GitHub Actions)

This repository deploys automatically to GitHub Pages via `.github/workflows/deploy.yml` whenever code is pushed to `main`.

One-time setup in GitHub:

1. Go to **Settings > Pages**.
2. Under **Build and deployment > Source**, select **GitHub Actions**.

After that, each push to `main` builds the site and deploys the `build` output to GitHub Pages.
