import React, {useCallback, useEffect, useId, useRef, useState} from 'react';
import {createPortal} from 'react-dom';
import useBaseUrl from '@docusaurus/useBaseUrl';
import Papa from 'papaparse';

import styles from './CsvTable.module.css';

export type CsvTableProps = {
  /** Path under `static/`, e.g. `/sources/bardiya-timeline.csv` */
  src: string;
  /** Optional caption below the table */
  caption?: string;
};

function DataTable({
  headers,
  body,
}: {
  headers: string[];
  body: string[][];
}): React.ReactNode {
  return (
    <table className="table table-striped table-bordered">
      <thead>
        <tr>
          {headers.map((h, i) => (
            <th key={i} scope="col">
              {h}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {body.map((row, ri) => (
          <tr key={ri}>
            {headers.map((_, ci) => (
              <td key={ci}>{row[ci] ?? ''}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

/**
 * Fetches a CSV from `static/` and renders it as an HTML table.
 * First row is treated as the header row. Uses `useBaseUrl` so it works with `baseUrl`.
 */
export function CsvTable({src, caption}: CsvTableProps): React.ReactNode {
  const url = useBaseUrl(src);
  const titleId = useId();
  const closeBtnRef = useRef<HTMLButtonElement>(null);
  const [rows, setRows] = useState<string[][] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [expanded, setExpanded] = useState(false);

  const closeExpanded = useCallback(() => setExpanded(false), []);

  useEffect(() => {
    if (!expanded) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') closeExpanded();
    };
    document.addEventListener('keydown', onKey);
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    closeBtnRef.current?.focus();
    return () => {
      document.removeEventListener('keydown', onKey);
      document.body.style.overflow = prevOverflow;
    };
  }, [expanded, closeExpanded]);

  useEffect(() => {
    let cancelled = false;
    fetch(url)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`${res.status} ${res.statusText}`);
        }
        return res.text();
      })
      .then((text) => {
        if (cancelled) return;
        const parsed = Papa.parse<string[]>(text, {
          header: false,
          skipEmptyLines: 'greedy',
        });
        const fatal = parsed.errors.filter((e) => e.type !== 'Quotes');
        if (fatal.length > 0) {
          throw new Error(fatal[0].message ?? 'CSV parse error');
        }
        const data = parsed.data as string[][];
        const nonEmpty = data.filter((row) =>
          row.some((cell) => cell.trim() !== ''),
        );
        setRows(nonEmpty.length > 0 ? nonEmpty : data);
      })
      .catch((e: unknown) => {
        if (!cancelled) {
          setError(e instanceof Error ? e.message : String(e));
        }
      });
    return () => {
      cancelled = true;
    };
  }, [url]);

  if (error) {
    return (
      <p className="text--danger" role="alert">
        Could not load CSV: {error}
      </p>
    );
  }

  if (!rows?.length) {
    return <p className="text--secondary">Loading table…</p>;
  }

  const headers = rows[0];
  const body = rows.slice(1);

  const overlay =
    expanded && typeof document !== 'undefined'
      ? createPortal(
          <div
            className={`${styles.overlay} csv-table-overlay`}
            role="dialog"
            aria-modal="true"
            aria-labelledby={titleId}>
            <div className={styles.overlayHeader}>
              <span id={titleId} className={styles.overlayTitle}>
                Table view
              </span>
              <button
                ref={closeBtnRef}
                type="button"
                className="button button--primary button--sm"
                onClick={closeExpanded}>
                Close
              </button>
            </div>
            <div className={`${styles.overlayScroll} csv-table-overlay-scroll`}>
              <DataTable headers={headers} body={body} />
            </div>
          </div>,
          document.body,
        )
      : null;

  return (
    <>
      {overlay}
      <div className={styles.root}>
        <div className={styles.toolbar}>
          <button
            type="button"
            className="button button--secondary button--sm"
            onClick={() => setExpanded(true)}
            aria-expanded={expanded}
            title="Expand table to fill the browser window">
            Expand
          </button>
        </div>
        <figure className={`csv-table-figure ${styles.figure}`}>
          <div className={styles.scroll}>
            <DataTable headers={headers} body={body} />
          </div>
          {caption ? <figcaption>{caption}</figcaption> : null}
        </figure>
      </div>
    </>
  );
}
