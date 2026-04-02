import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * Sidebar mirrors the seven research zones described in docs/intro.md:
 *
 *  Start here                    — method, archetypes, axial age, syncretism methodology
 *  Achaemenid & Hellenistic      — Zone 2 (most evidence-dense): Persian empire → Hellenistic Judaism
 *  The Mithra thread             — cross-cutting dossier: Indo-Iranian contract-god → Roman → Buddhist
 *  Gandhāra & Central Asia       — Zone 3: east-facing corridor, Saka, Kushan, Pure Land
 *  Mediterranean mysteries       — Zone 4: mystery ecology, Mithraism, solar syncretism, Paul
 *  Sasanian & Late Antique world — Zone 5.5: Zoroastrianism codified, Neoplatonism, Nestorian Silk Road
 *  PIE & deep grammar            — Zone 5: reconstructed IE narrative, ANE traces, Ugaritic
 *  Figures                       — by tradition, roughly chronological
 *  Reference                     — maps, timelines, tools, backlog
 */
const sidebars: SidebarsConfig = {
  researchSidebar: [
    'intro',

    // ── START HERE ──────────────────────────────────────────────────────────
    {
      type: 'category',
      label: 'Start here',
      collapsed: false,
      items: [
        'overview/messianic-archetypes',
        'overview/method-evidence-and-influence',
        'overview/exploring-transmission-and-deep-patterns',
        'overview/eurasian-mediator-figures-assessment',
        'overview/mythic-biography-patterns-prophet-and-buddha-analogy',
        'overview/axial-age-framework',
        'overview/syncretism-methodology',
        'overview/interpretatio-and-divine-translatability',
        'overview/soteriological-convergence-of-empire',
        'overview/synthesis-at-nodes',
        'overview/canon-as-imperial-artifact',
        'overview/skepticism-mysticism-negative-grammar',
      ],
    },

    // ── BRONZE AGE FOUNDATIONS ───────────────────────────────────────────────
    // Pre-Persian substrate: Mesopotamia, Egypt, and the Indus Valley as
    // participants in the Bronze Age world system. The layers that made the
    // Achaemenid synthesis possible.
    {
      type: 'category',
      label: 'Bronze Age foundations',
      link: {type: 'doc', id: 'overview/mesopotamian-religion-and-jewish-exile'},
      collapsed: true,
      items: [
        'overview/indus-valley-bronze-age-matrix',
        'overview/babylonian-astral-religion',
        'overview/egyptian-solar-theology-and-wisdom',
      ],
    },

    // ── ZONE 2: ACHAEMENID & HELLENISTIC CONTACT ────────────────────────────
    // Most evidence-dense zone: Persian empire → Hellenistic synthesis → Second Temple Judaism.
    // Covers 550–30 BCE; category header links to the Achaemenid hub page.
    {
      type: 'category',
      label: 'Achaemenid & Hellenistic contact',
      link: {type: 'doc', id: 'overview/achaemenid-and-west-asian-judaism'},
      collapsed: false,
      items: [
        'overview/zoroastrian-primary-texts',
        'overview/saoshyant-influence-hypotheses',
        'overview/achaemenid-axial-age-synthesis',
        'overview/persian-loanwords-in-biblical-tradition',
        'overview/persian-rulers-in-biblical-texts',
        'overview/eschatological-vocabulary-timeline',
        'overview/daniel-and-iranian-eschatology',
        'overview/enoch-son-of-man',
        'overview/dead-sea-scrolls-dualism-and-iranian-parallels',
        'overview/jewish-angelology-and-yazata-parallels',
        'overview/angelomorphic-christology-michael-mithra',
        'overview/evidence-leads-persian-milieu-and-mitra-cluster',
        'overview/gnosticism-and-mandaeanism',
        // ── Hellenistic expansion (330–30 BCE) ──
        'overview/alexandria-synthesis-hub',
        'overview/hellenistic-period-transmission',
        'overview/apocalyptic-genre-and-social-origins',
        'overview/septuagint-transmission-mechanism',
        'overview/sophia-wisdom-tradition',
        'overview/sibylline-oracles',
        'overview/shia-imamology-zoroastrian-parallels',
      ],
    },

    // ── THE MITHRA THREAD ────────────────────────────────────────────────────
    // Cross-cutting dossier: Indo-Iranian *mitra-* → Zoroastrian Mithra →
    // Roman Mithras → Manichaean Mihr → Maitreya / Pure Land.
    // Category header links to the cluster hub.
    {
      type: 'category',
      label: 'The Mithra thread',
      link: {type: 'doc', id: 'mithras'},
      collapsed: true,
      items: [
        'overview/indo-iranian-mitra-contract',
        'overview/mithra-roman-manichaean',
        'overview/manichaean-mihr-soteriology',
        'overview/amitabha-maitreya-gandhara-transmission',
        'overview/solar-saviors-mithra-maitreya',
        'overview/divine-contract-mithra-maitreya-amidah',
      ],
    },

    // ── ZONE 3: GANDHĀRA & CENTRAL ASIA ─────────────────────────────────────
    // East-facing corridor: Parthian bridge → Gandhāra → Saka / Kushan →
    // Pure Land phonology → alternative transmission theories.
    {
      type: 'category',
      label: 'Gandhāra & Central Asia',
      link: {type: 'doc', id: 'overview/gandhara-central-asian-transmission'},
      collapsed: true,
      items: [
        'overview/greco-buddhism',
        'overview/parthian-arsacid-corridor',
        'overview/saka-scythian-hypotheses',
        'overview/measuring-influence-mitra-maitreya',
        'overview/alternative-buddha-jesus-transmission-theories',
        'overview/greek-vocabulary-translation-lens',
        'overview/barbarian-inaugurator-pattern',
        'overview/cultural-transmission-theory',
      ],
    },

    // ── ZONE 4: MEDITERRANEAN MYSTERIES ─────────────────────────────────────
    // Mystery ecology, solar syncretism, civic soter language, and the
    // Pauline mission cities. Category header links to the atlas.
    {
      type: 'category',
      label: 'Mediterranean mysteries',
      link: {type: 'doc', id: 'overview/hero-cult-and-mystery-cult-atlas'},
      collapsed: true,
      items: [
        'overview/helios-apollo-sol-syncretism',
        'overview/solar-deities-eurasian-synthesis',
        'overview/attis-and-cybele',
        'overview/isis-osiris-serapis',
        'overview/demeter-eleusis-mysteries',
        'overview/greek-wandering-gods-initiation',
        'overview/tomb-veneration-relic-cults',
        'overview/hermes-mediator-and-initiation',
        'overview/philippi-via-egnatia-religious-milieu',
        'overview/messiah-language-greek-civic-context',
        'overview/emperor-cult-and-civic-soter',
        'overview/paul-mithraism-and-historicity-notes',
        'overview/paul-celestial-christology',
        'overview/paul-iranian-mediator',
        'overview/stoicism-and-synthesis',
        'overview/hermeticism-corpus-hermeticum',
        'overview/logos-doctrine-neoplatonic-christology',
        'overview/mediterranean-mystery-sources-appendix',
        'overview/mediterranean-figure-glossary',
        'overview/baptism-initiation-ritual-bridge',
      ],
    },

    // ── ZONE 5.5: SASANIAN & LATE ANTIQUE WORLD ──────────────────────────────
    // 224–651 CE: Zoroastrianism institutionalized, Manichaeism, Babylonian Talmud,
    // Neoplatonism, Nestorian Silk Road mission.
    {
      type: 'category',
      label: 'Sasanian & Late Antique world',
      link: {type: 'doc', id: 'overview/sasanian-empire-transmission'},
      collapsed: true,
      items: [
        'overview/zurvanism',
        'overview/manichaeism-synthesis',
        'overview/merkabah-mysticism',
        'overview/therapeutae',
        'overview/neoplatonism-and-theurgy',
        'overview/nestorian-christianity-silk-road',
      ],
    },

    // ── ZONE 5: PIE & DEEP GRAMMAR ───────────────────────────────────────────
    // Most hypothesis-heavy layer: PIE reconstructions, ANE traces in the
    // Bible, Paleo-Balkan horseman cult. Category header links to the new
    // overview page written for this zone.
    {
      type: 'category',
      label: 'PIE & deep grammar',
      link: {type: 'doc', id: 'overview/pie-ane-deep-grammar'},
      collapsed: true,
      items: [
        // ── PIE origins and the Indian branch ────────────────────────────
        'overview/pie-origins-yamnaya-expansion',
        'overview/vedic-religion-indo-aryan-migration',
        'overview/sramana-revolution-axial-india',
        // ── PIE myth and narrative grammar ───────────────────────────────
        'overview/pie-twin-and-brother-archetypes',
        'overview/pie-mediator-slot-origins',
        'overview/primordial-cosmic-man',
        'overview/pie-cosmic-combat-myth',
        'overview/pie-and-ane-traces-in-biblical-tradition',
        'overview/pie-motifs-atu-thompson-and-hero-traditions',
        'overview/thracian-horseman-paleo-balkan',
        'overview/ugaritic-baal-cycle',
      ],
    },

    // ── FIGURES ──────────────────────────────────────────────────────────────
    // Organized by tradition, roughly chronological from deepest antiquity.
    // Category header links to the figures hub page.
    {
      type: 'category',
      label: 'Figures',
      link: {type: 'doc', id: 'figures/index'},
      collapsed: false,
      items: [
        {
          type: 'category',
          label: 'Ancient Near East',
          collapsed: true,
          items: [
            'figures/babylonian-marduk',
            'figures/mesopotamian-gilgamesh',
            'figures/mesopotamian-dumuzi-tammuz',
            'figures/canaanite-baal',
            'figures/phoenician-adonis',
          ],
        },
        {
          type: 'category',
          label: 'Egyptian',
          collapsed: true,
          items: [
            'figures/egyptian-aten-ra-amun',
            'figures/egyptian-osiris',
          ],
        },
        {
          type: 'category',
          label: 'Iranian & Zoroastrian',
          collapsed: true,
          items: [
            'figures/zoroaster-zarathustra',
            'figures/cyrus-the-great',
            'figures/zoroastrian-saoshyant',
            'figures/roman-mithraism',
            'figures/bardaisan-of-edessa',
          ],
        },
        {
          type: 'category',
          label: 'Jewish traditions',
          collapsed: true,
          items: [
            'figures/judaism-mashiach',
            'figures/elijah-enoch',
          ],
        },
        {
          type: 'category',
          label: 'Greco-Roman',
          collapsed: true,
          items: [
            'figures/greco-roman-dionysus',
            'figures/greco-roman-asclepius',
            'figures/greco-roman-heracles',
            'figures/greco-roman-orpheus',
            'figures/greek-prometheus',
          ],
        },
        {
          type: 'category',
          label: 'Asian traditions',
          collapsed: true,
          items: [
            'figures/vedic-purusha',
            'figures/hindu-shiva-sadashiva',
            'figures/buddhism-maitreya',
            'figures/buddhist-vairocana',
            'figures/hinduism-kalki',
            'figures/taoism-li-hong',
          ],
        },
        {
          type: 'category',
          label: 'Christian & Islamic',
          collapsed: true,
          items: [
            'figures/christianity-parousia',
            'figures/islam-mahdi',
          ],
        },
        {
          type: 'category',
          label: 'Northern European',
          collapsed: true,
          items: [
            'figures/norse-baldr',
            'figures/arthurian-king-arthur',
          ],
        },
        {
          type: 'category',
          label: 'Mesoamerican',
          collapsed: true,
          items: [
            'figures/mesoamerican-quetzalcoatl',
          ],
        },
      ],
    },

    // ── THE BARDIYA HYPOTHESIS ───────────────────────────────────────────────
    // Minority speculative hypothesis: Gaumata Bardiya (522 BCE) as historical
    // template for the Buddha and Christ. All claims labeled by tier.
    // Category header links to the hypothesis overview.
    {
      type: 'category',
      label: 'The Bardiya Hypothesis',
      link: {type: 'doc', id: 'bardiya/index'},
      collapsed: true,
      items: [
        // Overview & method
        'bardiya/introduction',
        'bardiya/key-figures',
        'bardiya/historical-context',
        'bardiya/achaemenid-complete-history',
        'bardiya/methodology',
        // Evidence
        {
          type: 'category',
          label: 'Evidence',
          collapsed: false,
          items: [
            'bardiya/evidence-primary-sources',
            'bardiya/evidence-linguistics',
            'bardiya/evidence-archaeology',
          ],
        },
        // Historicity
        {
          type: 'category',
          label: 'Historicity questions',
          collapsed: false,
          items: [
            'bardiya/buddha-historicity',
            'bardiya/jesus-historicity',
          ],
        },
        // Parallels
        {
          type: 'category',
          label: 'Comparative parallels',
          collapsed: false,
          items: [
            'bardiya/buddhist-parallels',
            'bardiya/christian-parallels',
            'bardiya/mythic-patterns',
          ],
        },
        // Religious contexts
        {
          type: 'category',
          label: 'Religious contexts',
          collapsed: true,
          items: [
            'bardiya/religions-zoroastrianism',
            'bardiya/religions-buddhism',
            'bardiya/religions-judaism',
            'bardiya/religions-christianity',
            'bardiya/religions-greco-roman',
          ],
        },
        // Appendices
        {
          type: 'category',
          label: 'Appendices',
          collapsed: true,
          items: [
            'bardiya/bibliography',
            'bardiya/glossary',
          ],
        },
      ],
    },

    // ── CONTRIBUTE ────────────────────────────────────────────────────────────
    // How to add evidence, expand pages, and run AI agents against the backlog.
    {
      type: 'category',
      label: 'Contribute',
      collapsed: false,
      items: [
        'overview/contributing',
        'overview/research-backlog',
      ],
    },

    // ── REFERENCE ────────────────────────────────────────────────────────────
    {
      type: 'category',
      label: 'Reference',
      collapsed: true,
      items: [
        'overview/chronological-map',
        'overview/visual-timeline',
        'overview/further-reading',
        'overview/curated-page-template',
        'research/about-research-notes',
        'research/oxford-handbook-eschatology-notes',
        'research/thesis-assessment-notes-2026',
        'research/iranian-origins-sakyas',
      ],
    },
  ],
};

export default sidebars;
