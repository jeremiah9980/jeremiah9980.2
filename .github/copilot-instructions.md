# Copilot Instructions — jeremiah9980.2

## Repository overview

This is a static HTML portfolio and practice site for Jeremiah Cargill, served via GitHub Pages at `https://jeremiah9980.github.io/jeremiah9980.2/`.

**Stack:** Plain HTML, CSS custom properties, minimal vanilla JS. No build step, no framework, no bundler.

## Information architecture

```text
/                              [home — two-lane router with hero]
├── professional/
│   ├── cargill-consulting/    [Enterprise practice — services + engagements]
│   ├── next-gen-it/           [SMB practice — audit deliverable examples]
│   └── about/                 [About hub — resumes, practice origin stories]
└── projects/
    ├── conflict-collection/   [FLAGSHIP — multi-model neutral analysis platform]
    ├── clients/               [Client work hub — case studies]
    ├── infrastructure/
    ├── ai/
    └── devops-cloud/
```

## Design system

- Dark coral on deep navy palette; design tokens live in `assets/css/main.css` at the top
- Typography: IBM Plex Sans / Plex Mono, Fraunces variable serif for display headings
- Shared components: `.hero`, `.lane-card`, `.split`, `.btn`, `.eyebrow`, `.report-*` (for deliverable reports)
- When adding a new page, copy structure from a sibling page to preserve visual rhythm

## Linked product: Next-Gen-IT portal

The `next-gen-it/` section of this site showcases the **Next-Gen-IT** product — a domain health audit platform for small businesses and realty teams. The live portal lives in the separate repository `jeremiah9980/Next-Gen-IT`, under `portal/`.

Key portal files (`jeremiah9980/Next-Gen-IT/portal/`):

- `index.html` — authenticated portal dashboard
- `login.html` — SHA-256 password gate (client-side, sessionStorage)
- `auth.js` — auth guard; auto-redirects unauthenticated visitors to login
- `report.html` — individual domain audit report view
- `runbook.html` — client-facing remediation runbook view

The portal is a GitHub Pages static frontend backed by a FastAPI backend. It performs domain audits covering DNS, email authentication (SPF/DKIM/DMARC), website health, and SEO signals.

## Editing conventions

- Never add a build step or framework
- Keep all JS in vanilla ES6+; use `assets/js/main.js` for site-wide utilities
- CSS tokens first — if a colour or spacing value is used more than once, add it as a custom property
- `.report-*` classes are reserved for client deliverable report pages; reuse them for new report examples
- When linking between pages, use relative paths
