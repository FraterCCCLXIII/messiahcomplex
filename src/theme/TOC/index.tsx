import React, {useCallback, useEffect, useState} from 'react';
import OriginalTOC from '@theme-original/TOC';

type Props = React.ComponentProps<typeof OriginalTOC>;

export default function TOCWrapper(props: Props): JSX.Element {
  const [collapsed, setCollapsed] = useState(false);
  const [closing, setClosing] = useState(false);
  const [opening, setOpening] = useState(false);

  const toggle = useCallback(() => {
    if (collapsed) {
      setCollapsed(false);
      setOpening(true);
      return;
    }
    if (closing || opening) {
      return;
    }
    setClosing(true);
  }, [collapsed, closing, opening]);

  useEffect(() => {
    if (!opening) {
      return;
    }
    const id = requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        setOpening(false);
      });
    });
    return () => cancelAnimationFrame(id);
  }, [opening]);

  /* With prefers-reduced-motion, CSS disables transitions — no transitionend on close */
  useEffect(() => {
    if (!closing) {
      return;
    }
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (!mq.matches) {
      return;
    }
    const t = window.setTimeout(() => {
      setClosing(false);
      setCollapsed(true);
    }, 0);
    return () => window.clearTimeout(t);
  }, [closing]);

  const handleContentTransitionEnd = useCallback((e: React.TransitionEvent<HTMLDivElement>) => {
    if (e.target !== e.currentTarget) {
      return;
    }
    if (e.propertyName !== 'transform') {
      return;
    }
    if (!closing) {
      return;
    }
    setClosing(false);
    setCollapsed(true);
  }, [closing]);

  const drawerClass = [
    'toc-drawer',
    collapsed && 'toc-drawer--collapsed',
    closing && 'toc-drawer--closing',
    opening && 'toc-drawer--opening',
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <div className={drawerClass}>
      <div className="toc-top-toggle">
        <button
          type="button"
          className="sidebar-panel-btn"
          onClick={toggle}
          aria-label={collapsed ? 'Show table of contents' : 'Hide table of contents'}
          title={collapsed ? 'Show table of contents' : 'Hide table of contents'}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden="true"
          >
            <rect width="18" height="18" x="3" y="3" rx="2" />
            <path d="M15 3v18" />
          </svg>
        </button>
      </div>

      <div
        className="toc-drawer__content"
        onTransitionEnd={handleContentTransitionEnd}
        aria-hidden={collapsed}
      >
        <OriginalTOC {...props} />
      </div>
    </div>
  );
}
