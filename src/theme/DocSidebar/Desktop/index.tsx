import React, {useState} from 'react';
import OriginalDocSidebarDesktop from '@theme-original/DocSidebar/Desktop';

type Props = React.ComponentProps<typeof OriginalDocSidebarDesktop>;

export default function DocSidebarDesktopWrapper(props: Props): JSX.Element {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <div className={`sidebar-drawer${collapsed ? ' sidebar-drawer--collapsed' : ''}`}>
      <div className="sidebar-top-toggle">
        <button
          className="sidebar-panel-btn"
          onClick={() => setCollapsed(c => !c)}
          aria-label={collapsed ? 'Show sidebar' : 'Hide sidebar'}
          title={collapsed ? 'Show sidebar' : 'Hide sidebar'}
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
            <path d="M9 3v18" />
          </svg>
        </button>
      </div>

      <div className="sidebar-drawer__content">
        <OriginalDocSidebarDesktop {...props} />
      </div>
    </div>
  );
}
