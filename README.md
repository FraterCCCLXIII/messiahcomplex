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

## Deployment (GitHub Actions)

This repository deploys automatically to GitHub Pages via `.github/workflows/deploy.yml` whenever code is pushed to `main`.

One-time setup in GitHub:

1. Go to **Settings > Pages**.
2. Under **Build and deployment > Source**, select **GitHub Actions**.

After that, each push to `main` builds the site and deploys the `build` output to GitHub Pages.
