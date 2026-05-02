# jeremiah9980.2

Second-generation portfolio and practice site for Jeremiah Cargill.

**Live:** <https://jeremiah9980.github.io/jeremiah9980.2/>
**V1 archive:** <https://jeremiah9980.github.io/jeremiah9980/>

## What this is

A static HTML site organized around two top-level lanes:

- **Professional** — two parallel practices: Cargill Consulting for enterprise work, Next-Gen-IT for small-business audits and security. About hub with resumes and practice origin stories.
- **Projects** — independent lab featuring the Conflict Collection flagship product, redacted client case studies, and infrastructure work.

No build step. No framework. Just HTML, CSS, a tiny JS file, and GitHub Pages.

## Design

Dark coral UI on deep navy. IBM Plex Sans / Plex Mono with Fraunces variable serif for display. Glass panels, gradient top borders on lane-cards. All design tokens are CSS custom properties at the top of `assets/css/main.css` — adjust palette in one place, propagates everywhere.

## Information architecture

```text
/                                                [home — two-lane router with hero]
├── professional/
│   ├── index.html                                [Professional router]
│   ├── cargill-consulting/
│   │   └── index.html                            [Enterprise practice — 6 services + 6 packaged engagements]
│   ├── next-gen-it/
│   │   ├── index.html                            [SMB practice — example-deliverable framing]
│   │   ├── starsky-owen-audit-report.html        [Example: realty audit with workflow diagram]
│   │   └── shonna-king-domain-health-audit.html  [Example: domain/email-auth health report]
│   └── about/
│       ├── index.html                            [About hub — 3 cards + bio split]
│       ├── resumes/                              [Three targeted resume versions]
│       ├── cargill-consulting/                   [Practice origin: enterprise narrative]
│       └── next-gen-it/                          [Practice origin: SMB narrative]
└── projects/
    ├── index.html                                [Lab router — flagship-led, 3 cards]
    ├── conflict-collection/                      [FLAGSHIP — multi-model neutral analysis platform]
    ├── clients/
    │   ├── index.html                            [Client work hub — 4 cases]
    │   ├── teleotitle/                           [Title company — DMARC + wire-fraud hardening]
    │   ├── abode-labs/                           [Brand domain — DNS + email auth]
    │   ├── starsky-owen/                         [Realty data tooling]
    │   └── cosmicgen/                            [Engagement in scoping]
    ├── infrastructure/                           [VMware/UCS/NetApp/OpenShift work]
    ├── ai/                                       [AI integration work]
    └── devops-cloud/                             [DevOps and cloud work]
```

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000/
```

## Deploying to GitHub Pages

1. Push to the `main` branch of the `jeremiah9980.2` repo
2. Repo settings → Pages → Source: `main` / root
3. Live at `https://jeremiah9980.github.io/jeremiah9980.2/`

GitHub Pages serves the raw HTML directly. No `.nojekyll` file required since there's nothing Jekyll would mangle, but if Pages ever trips on a leading-underscore filename, drop an empty `.nojekyll` at the root.

## Asset locations

- `assets/css/main.css` — full stylesheet, design tokens at top
- `assets/js/main.js` — mobile nav toggle (only)
- `assets/img/hero.png` — homepage hero
- `assets/img/starsky-workflow.png` — referenced from the Starsky Owen example report

## Editing notes

Pages share repeated nav, footer, and component markup (`.hero`, `.lane-card`, `.split`, `.btn`, `.eyebrow`). When editing a single page, the safe move is to copy the structure from a sibling page rather than reinvent it — that preserves the shared visual rhythm.

The two example deliverable reports under `/professional/next-gen-it/` use additional `.report-*` classes (defined in `main.css`) for their report-shell layout. Reuse those for any new client-deliverable examples.

## License

All content © Jeremiah Cargill. Code structure available for personal reference.
