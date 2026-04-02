import type {ReactNode} from 'react';
import {useLayoutEffect, useRef, useState} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

const HOME_GALLERY: {file: string; alt: string}[] = [
  {
    file: 'archangel-michael-icon.png',
    alt: 'Eastern Orthodox icon of the Archangel Michael on a red horse with trumpet and spear.',
  },
  {
    file: 'triumphal-entry-palm-sunday-icon.png',
    alt: 'Byzantine icon of Christ’s triumphal entry into Jerusalem on a donkey.',
  },
  {
    file: 'phrygian-rider-lion-snake-relief.png',
    alt: 'Ancient stone relief of a rider in a Phrygian cap on a horse, with a lion and snake below.',
  },
  {
    file: 'kalki-avatar-white-horse.png',
    alt: 'Indian lithograph-style image of a four-armed figure on a galloping white horse.',
  },
  {
    file: 'persian-miniature-rider.png',
    alt: 'Persian miniature of a haloed rider on horseback in a stylized landscape.',
  },
  {
    file: 'ancient-greek-rider-relief.png',
    alt: 'Ancient Greek stone relief of a rider on a rearing horse with inscription below.',
  },
];

function HeroGalleryImage({file, alt}: {file: string; alt: string}) {
  const src = useBaseUrl(`/img/home/${file}`);
  return (
    <div className={styles.heroGalleryItem} role="listitem">
      <img
        src={src}
        alt={alt}
        width={360}
        height={540}
        loading="lazy"
        decoding="async"
        className={styles.heroGalleryImg}
      />
    </div>
  );
}

function HeroGallery() {
  const ref = useRef<HTMLDivElement>(null);
  const [visibleCount, setVisibleCount] = useState(HOME_GALLERY.length);

  useLayoutEffect(() => {
    const el = ref.current;
    if (!el) {
      return undefined;
    }

    function updateFitCount() {
      const cw = el.clientWidth;
      if (cw <= 0) {
        return;
      }
      const first = el.firstElementChild as HTMLElement | null;
      if (!first) {
        return;
      }
      const itemW = first.offsetWidth;
      if (itemW <= 0) {
        return;
      }
      const gapStr = getComputedStyle(el).gap;
      const gapPx = parseFloat(gapStr.split(/\s+/)[0] ?? '0');
      const gap = Number.isFinite(gapPx) ? gapPx : 0;
      const raw = Math.floor((cw + gap) / (itemW + gap));
      const n = Math.max(1, Math.min(HOME_GALLERY.length, raw));
      setVisibleCount((prev) => (prev === n ? prev : n));
    }

    updateFitCount();
    const ro = new ResizeObserver(updateFitCount);
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  const visible = HOME_GALLERY.slice(0, visibleCount);

  return (
    <div
      ref={ref}
      className={styles.heroGallery}
      role="list"
      aria-label="Art and iconography across traditions">
      {visible.map(({file, alt}) => (
        <HeroGalleryImage key={file} file={file} alt={alt} />
      ))}
    </div>
  );
}

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className={styles.heroIntro}>
          Exploring the origins of religion and the evolution of messianic archetypes—how
          savior figures, renewal myths, and mediator roles emerge, diverge, and travel across
          traditions, with careful attention to evidence and historical context.
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--primary button--lg"
            to="/docs/intro">
            Explore
          </Link>
          <Link
            className="button button--secondary button--lg"
            to="/docs/overview/contributing">
            Contribute
          </Link>
        </div>
        <HeroGallery />
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="Exploring the origins of religion and messianic archetypes—comparative research on messiah figures across traditions.">
      <HomepageHeader />
    </Layout>
  );
}
