import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Messiah Complex',
  tagline: 'Research on messiah figures and messianic archetypes',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // GitHub Pages (project site): https://<org>.github.io/<repo>/
  url: 'https://fraterccclxiii.github.io',
  baseUrl: '/messiahcomplex/',

  // Used for "Edit this page" and similar GitHub links
  organizationName: 'FraterCCCLXIII',
  projectName: 'messiahcomplex',

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  // Register as a plugin (not only `themes`): the package exposes `getThemePath()` for
  // `@theme/SearchPage` / `@theme/SearchBar`. Some setups fail to resolve `@theme/SearchPage`
  // when it is only listed under `themes` with certain cache / dev-server states.
  plugins: [
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        language: ['en'],
        highlightSearchTermsOnTargetPage: true,
        explicitSearchResultPath: true,
        searchBarPosition: 'right',
      },
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Messiah Complex',
      logo: {
        alt: 'Messiah Complex',
        src: 'img/logo.svg',
        srcDark: 'img/logo-dark.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'researchSidebar',
          position: 'left',
          label: 'Research',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Research',
          items: [
            {
              label: 'Introduction',
              to: '/docs/intro',
            },
            {
              label: 'Chronological map',
              to: '/docs/overview/chronological-map',
            },
            {
              label: 'Visual timeline',
              to: '/docs/overview/visual-timeline',
            },
            {
              label: 'Mithra cluster',
              to: '/docs/mithras',
            },
            {
              label: 'PIE twin archetypes',
              to: '/docs/overview/pie-twin-and-brother-archetypes',
            },
            {
              label: 'Greek initiation cults',
              to: '/docs/overview/greek-wandering-gods-initiation',
            },
          ],
        },
        {
          title: 'Site',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
          ],
        },
      ],
      copyright: `Messiah Complex · ${new Date().getFullYear()}`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
