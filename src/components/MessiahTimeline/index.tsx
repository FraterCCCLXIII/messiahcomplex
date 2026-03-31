import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

type TimelineEntry = {
  sortKey: number;
  range: string;
  title: string;
  tradition: string;
  blurb: string;
  to?: string;
};

const ENTRIES: TimelineEntry[] = [
  {
    sortKey: -975,
    range: '1000–600 BCE',
    title: 'Saoshyant language in the Gathas',
    tradition: 'Zoroastrian',
    blurb:
      'Earliest Avestan uses of saoshyant- language; seeds of future “benefactor / restorer” imagery.',
    to: '/docs/figures/zoroastrian-saoshyant',
  },
  {
    sortKey: -700,
    range: '8th–6th cent. BCE',
    title: 'Hebrew prophetic Mashiach',
    tradition: 'Judaism',
    blurb:
      'Future Davidic king / ideal ruler motifs in Isaiah, Jeremiah, and related prophetic literature.',
    to: '/docs/figures/judaism-mashiach',
  },
  {
    sortKey: -500,
    range: '6th–4th cent. BCE',
    title: 'Achaemenid rule & Jewish–Persian contact',
    tradition: 'West Asia',
    blurb:
      'Imperial Aramaic chancellery, Elephantine and Yehud; contexts often discussed for Iranian–Jewish exchanges.',
    to: '/docs/overview/achaemenid-and-west-asian-judaism',
  },
  {
    sortKey: -400,
    range: '500–300 BCE',
    title: 'Younger Avesta: named future Saoshyant',
    tradition: 'Zoroastrian',
    blurb:
      'Younger Avestan elaboration tied to renovation, judgment, and Frashokereti trajectories.',
    to: '/docs/figures/zoroastrian-saoshyant',
  },
  {
    sortKey: -250,
    range: '3rd cent. BCE',
    title: 'Metteyya / Maitreya in the Pāli canon',
    tradition: 'Buddhism',
    blurb:
      'DN 26 (*Cakkavatti-Sīhanāda*): the future Buddha of loving-kindness / Metteyya.',
    to: '/docs/figures/buddhism-maitreya',
  },
  {
    sortKey: -200,
    range: '400 BCE – 200 CE',
    title: 'Kalkī in the Mahābhārata epic core',
    tradition: 'Hindu / Vaishnava',
    blurb:
      'Future avatāra who ends Kali Yuga; elaborated in later Purāṇas.',
    to: '/docs/figures/hinduism-kalki',
  },
  {
    sortKey: -230,
    range: '3rd cent. BCE – 3rd cent. CE',
    title: 'Palaeo-Balkan Thracian Heros (rider hunt)',
    tradition: 'Thrace / Danube',
    blurb:
      'Votive reliefs of hunter-horseman Heros; later syncretism; σωτήρ / epekoos epithets; twin-rider goddess schemes—see PIE depth docs.',
    to: '/docs/overview/thracian-horseman-paleo-balkan',
  },
  {
    sortKey: -50,
    range: '67 BCE – 1st cent. CE',
    title: 'Roman Mithraism (tauroctony cult)',
    tradition: 'Mystery cult',
    blurb:
      'Iranian-flavored soteriology in the Mediterranean; present-tense initiation more than future eschatology.',
    to: '/docs/figures/roman-mithraism',
  },
  {
    sortKey: 75,
    range: '50–100 CE',
    title: 'Christian Messiah & Parousia',
    tradition: 'Christianity',
    blurb:
      'New Testament complex: first coming, resurrection hope, and expected return in power.',
    to: '/docs/figures/christianity-parousia',
  },
  {
    sortKey: 150,
    range: '1st–3rd cent. CE',
    title: 'Gandhara–Kushan Buddhist corridor',
    tradition: 'Central Asia',
    blurb:
      'Layered Greek, Saka, Kushan, and Parthian histories; major node for Mahayana imagery moving east.',
    to: '/docs/overview/gandhara-central-asian-transmission',
  },
  {
    sortKey: 367,
    range: '364–370 CE',
    title: 'Li Hong in Shangqing revelations',
    tradition: 'Taoism',
    blurb:
      '*Zhen’gao* revelations: sage-king messianism and cosmic renewal in Daoist eschatology.',
    to: '/docs/figures/taoism-li-hong',
  },
  {
    sortKey: 800,
    range: '7th–9th cent. CE',
    title: 'Mahdī in hadith corpora',
    tradition: 'Islam',
    blurb:
      'Future guided chief; justice before Judgment; often paired with returning Jesus in Sunni narratives.',
    to: '/docs/figures/islam-mahdi',
  },
  {
    sortKey: 950,
    range: '~10th cent. CE (poem; 13th cent. mss)',
    title: 'Baldr after Ragnarök',
    tradition: 'Norse',
    blurb:
      '*Völuspá* vision of renewal: Baldr and Höðr reconciled in a green worlds-age.',
    to: '/docs/figures/norse-baldr',
  },
  {
    sortKey: 1125,
    range: '1125 CE onward',
    title: 'Arthur: “Once and Future King”',
    tradition: 'Arthurian',
    blurb:
      'Medieval chronicles (Malmesbury, Geoffrey, Layamon) crystallize return-from-Avalon prophecy.',
    to: '/docs/figures/arthurian-king-arthur',
  },
]
  .slice()
  .sort((a, b) => a.sortKey - b.sortKey);

export default function MessiahTimeline(): ReactNode {
  return (
    <div className={styles.root}>
      <p className={styles.lead}>
        The timeline runs from earliest attestations toward medieval afterlives. Dates are
        approximate; each card links to a deeper article.
      </p>
      <div className={styles.band}>
        <strong>Overlap, not a single line.</strong> Entries sit in parallel worlds—Iranian, Levantine,
        Indic, steppe, and medieval European—connected by history where sources show contact.
      </div>
      <ol className={styles.track} aria-label="Messiah figures timeline">
        {ENTRIES.map((e, i) => {
          const side = i % 2 === 0 ? styles.itemRight : styles.itemLeft;
          return (
            <li key={`${e.sortKey}-${e.title}`} className={`${styles.item} ${side}`}>
              <div className={styles.dotCol} aria-hidden="true">
                <span className={styles.dot} />
              </div>
              <div className={styles.cardCol}>
                <article className={styles.card}>
                  <div className={styles.range}>{e.range}</div>
                  <h3 className={styles.title}>{e.title}</h3>
                  <span className={styles.tag}>{e.tradition}</span>
                  <p className={styles.blurb}>{e.blurb}</p>
                  {e.to ? (
                    <Link className={styles.link} to={e.to}>
                      Open article →
                    </Link>
                  ) : null}
                </article>
              </div>
            </li>
          );
        })}
      </ol>
    </div>
  );
}
