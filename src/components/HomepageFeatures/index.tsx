import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Aggregate',
    description: (
      <>
        Collect sources and scholarly notes on messiah figures from Zoroastrian,
        Abrahamic, Indic, Taoist, Norse, and Arthurian traditions—without
        flattening their differences.
      </>
    ),
  },
  {
    title: 'Map archetypes',
    description: (
      <>
        Trace recurring motifs—future savior, cosmic renewal, judgment, golden
        age—and how they evolve or diverge in each lineage.
      </>
    ),
  },
  {
    title: 'Compare with care',
    description: (
      <>
        Use the chronological map and further reading to test influence and
        parallel claims against primary texts and specialist literature.
      </>
    ),
  },
];

function Feature({
  title,
  description,
  index,
}: FeatureItem & {index: number}) {
  return (
    <div className={clsx('col col--4')}>
      <div className={styles.featureBlock}>
        <span className={styles.featureIndex} aria-hidden>
          {String(index + 1).padStart(2, '0')}
        </span>
        <Heading as="h3" className={styles.featureTitle}>
          {title}
        </Heading>
        <p className={styles.featureText}>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={props.title} {...props} index={idx} />
          ))}
        </div>
      </div>
    </section>
  );
}
