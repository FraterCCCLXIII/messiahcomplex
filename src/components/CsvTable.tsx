import React, {useEffect, useState} from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';
import Papa from 'papaparse';

export type CsvTableProps = {
  /** Path under `static/`, e.g. `/sources/bardiya-timeline.csv` */
  src: string;
  /** Optional caption below the table */
  caption?: string;
};

/**
 * Fetches a CSV from `static/` and renders it as an HTML table.
 * First row is treated as the header row. Uses `useBaseUrl` so it works with `baseUrl`.
 */
export function CsvTable({src, caption}: CsvTableProps): React.ReactNode {
  const url = useBaseUrl(src);
  const [rows, setRows] = useState<string[][] | null>(null);
  const [error, setError] = useState<string | null>(null);

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
        if (parsed.errors.length > 0) {
          const first = parsed.errors[0];
          throw new Error(first.message ?? 'CSV parse error');
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

  return (
    <figure className="csv-table-figure">
      <div className="csv-table-scroll">
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
      </div>
      {caption ? <figcaption>{caption}</figcaption> : null}
    </figure>
  );
}
