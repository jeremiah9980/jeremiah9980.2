#!/usr/bin/env python3
"""
Generator for jeremiah9980.2 site.
Produces raw HTML files with consistent nav/footer and per-page content.
Run once, then HTML files are editable directly.
"""
import os
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "Jeremiah Cargill"


def asset_prefix(depth):
    return "../" * depth if depth > 0 else "./"


def nav(depth, active_section=None):
    p = asset_prefix(depth)
    items = [
        ("", "Index"),
        ("professional/", "Professional"),
        ("professional/cargill-consulting/", "Cargill Consulting"),
        ("professional/next-gen-it/", "Next-Gen-IT"),
        ("projects/", "Projects"),
        ("professional/about/", "About"),
    ]
    links = []
    for path, label in items:
        href = p + path if path else p + "index.html"
        cls = ' class="active"' if label == active_section else ""
        links.append(f'      <li><a href="{href}"{cls}>{label}</a></li>')
    return f"""<nav class="site-nav">
  <div class="site-nav-inner">
    <a href="{p if depth > 0 else './'}" class="brand">
      Cargill<span class="amp">&amp;</span>Co
      <span class="brand-sub">Enterprise · SMB · Lab</span>
    </a>
    <button class="nav-toggle" aria-label="Toggle menu">Menu</button>
    <ul class="nav-links">
{chr(10).join(links)}
    </ul>
  </div>
</nav>"""


def footer(depth):
    p = asset_prefix(depth)
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">Cargill<span>&amp;</span>Co</div>
        <p class="footer-tag">Two practices, one architect. Enterprise-grade thinking applied across the size spectrum, plus an active project lab.</p>
      </div>
      <div class="footer-col">
        <h5>Professional</h5>
        <ul>
          <li><a href="{p}professional/cargill-consulting/">Cargill Consulting</a></li>
          <li><a href="{p}professional/next-gen-it/">Next-Gen-IT</a></li>
          <li><a href="{p}professional/about/">About</a></li>
          <li><a href="{p}professional/about/resumes/">Resumes</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Projects</h5>
        <ul>
          <li><a href="{p}projects/infrastructure/">Infrastructure</a></li>
          <li><a href="{p}projects/conflict-collection/">Conflict Collection</a></li>
          <li><a href="{p}projects/ai/">AI</a></li>
          <li><a href="{p}projects/clients/">Clients</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <ul>
          <li><a href="https://github.com/jeremiah9980">GitHub</a></li>
          <li><a href="https://www.linkedin.com/in/jeremiahcargill/">LinkedIn</a></li>
          <li><span class="muted">Austin, TX</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-meta">
      <span>© 2026 Jeremiah Cargill</span>
      <span>Built in production · Portfolio &amp; practice</span>
    </div>
  </div>
</footer>"""


def breadcrumbs(items, depth):
    """items: list of (label, href_or_None). Last one is current."""
    p = asset_prefix(depth)
    parts = []
    for i, (label, href) in enumerate(items):
        if href is None:
            parts.append(f'<span>{label}</span>')
        else:
            parts.append(f'<a href="{p + href if href else p}">{label}</a>')
        if i < len(items) - 1:
            parts.append('<span class="sep">/</span>')
    return f'<div class="container"><div class="breadcrumbs">{"".join(parts)}</div></div>'


def page(title, depth, body, active=None, description=""):
    p = asset_prefix(depth)
    desc = description or f"{title} — {SITE}, Enterprise Architect."
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · {SITE}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{p}assets/css/main.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
</head>
<body>
{nav(depth, active)}
<main>
{body}
</main>
{footer(depth)}
<script src="{p}assets/js/main.js"></script>
</body>
</html>
"""


def write(path, html):
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(html, encoding="utf-8")
    print(f"  wrote {path}")


# ============================================================================
# ROOT — two-lane entry
# ============================================================================
body = """
<section class="hero">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow eyebrow-rule">Jeremiah Cargill · Austin, TX</span>
    </div>
    <h1 class="reveal">Enterprise architecture, <em>small-business IT,</em> and an independent project lab.</h1>
    <p class="lede reveal">Two practices sharing one architect. Cargill Consulting handles enterprise — identity, infrastructure, cloud, platform engineering. Next-Gen-IT handles SMB — packaged audits, operations, and security for small firms that need real architecture instead of another help desk. Everything I build in between lives in the lab.</p>
    <div class="hero-meta reveal">
      <span>20+ years in infrastructure</span>
      <span>Okta SME</span>
      <span>VMware · UCS · NetApp · OpenShift</span>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-2">
      <a href="professional/" class="lane-card reveal">
        <span class="lane-num">01 · Professional</span>
        <h2>Hire an architect.</h2>
        <p>Two delivery postures for two buyers. Pick the practice that fits your org.</p>
        <ul>
          <li>Cargill Consulting — Enterprise</li>
          <li>Next-Gen-IT — Small Business</li>
          <li>About · Resumes · Credentials</li>
        </ul>
        <span class="card-arrow">Open practice →</span>
      </a>
      <a href="projects/" class="lane-card reveal">
        <span class="lane-num">02 · Projects</span>
        <h2>See the lab.</h2>
        <p>Infrastructure, DevOps, AI, client case studies, and an in-production platform for co-parenting conflict documentation.</p>
        <ul>
          <li>Infrastructure · DevOps · AI</li>
          <li>Conflict Collection Platform</li>
          <li>GPS · Flywheel · GameChanger</li>
          <li>Client Work</li>
        </ul>
        <span class="card-arrow">Open lab →</span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow eyebrow-rule">Why two practices</span>
        <h2>Enterprise thinking, applied at every size.</h2>
      </div>
      <div>
        <p>A Fortune 1000 insurer needs an Okta SME who can negotiate with an IAM steering committee. A five-person title company needs someone who can fix their DMARC posture before the next wire-fraud attempt lands. The technical depth is the same — the delivery model, scope, and pricing aren't. Running both as distinct practices keeps the offers honest and the buyers unconfused.</p>
        <div class="btn-cluster">
          <a class="btn" href="professional/cargill-consulting/">Cargill Consulting</a>
          <a class="btn btn-ghost" href="professional/next-gen-it/">Next-Gen-IT</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
write("index.html", page("Enterprise &amp; SMB Architecture, Project Lab", 0, body, active="Index",
                         description="Enterprise architecture (Cargill Consulting), SMB IT practice (Next-Gen-IT), and an independent project lab — by Jeremiah Cargill."))


# ============================================================================
# PROFESSIONAL router
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", None)], 1) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">01 · Professional</span>
    <h1 class="reveal">Two practices. <em>Same architect.</em></h1>
    <p class="lede reveal">Enterprise buyers get Cargill Consulting. Small-business owners get Next-Gen-IT. The technical depth is identical; the way work gets scoped, priced, and delivered isn't.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-2">
      <a href="cargill-consulting/" class="lane-card">
        <span class="lane-num">1.a · Enterprise</span>
        <h2>Cargill Consulting</h2>
        <p>For Fortune 1000, regulated industries, and large IT orgs that need a specialist architect for identity, infrastructure, cloud, or platform engineering.</p>
        <ul>
          <li>Okta &amp; Identity Architecture</li>
          <li>Enterprise Infrastructure (VMware · UCS · NetApp)</li>
          <li>Cloud &amp; DevOps</li>
          <li>Architecture assessments &amp; SME retainers</li>
        </ul>
        <span class="card-arrow">Enter practice →</span>
      </a>
      <a href="next-gen-it/" class="lane-card">
        <span class="lane-num">1.b · Small Business</span>
        <h2>Next-Gen-IT</h2>
        <p>For owner-operated firms — title companies, realty offices, small clinics. Three packaged, fixed-scope offers. No hourly mystery meat, no six-figure proposals.</p>
        <ul>
          <li>Next-Gen-Audit — fixed-scope IT &amp; security audit</li>
          <li>Next-Gen-Operations — ongoing IT on retainer</li>
          <li>Next-Gen-Security — DMARC, MFA, wire-fraud prevention</li>
        </ul>
        <span class="card-arrow">Enter practice →</span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule">1.c · About</span>
    <h2>Who you're hiring.</h2>
    <p>Twenty years across enterprise infrastructure, identity, and platform work. Current role: Senior Systems Engineer at Texas Mutual Insurance. Prior: multi-site datacenter design, healthcare clinic rollouts, manufacturing print automation, hybrid migration architectures.</p>
    <div class="btn-cluster">
      <a class="btn" href="about/">Full background</a>
      <a class="btn btn-ghost" href="about/resumes/">Three targeted resumes</a>
    </div>
  </div>
</section>
"""
write("professional/index.html", page("Professional", 1, body, active="Professional"))


# ============================================================================
# 1.a CARGILL CONSULTING hub
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("Cargill Consulting", None)], 2) + """
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow eyebrow-rule reveal">1.a · Enterprise Practice</span>
        <h1 class="reveal">Architecture for orgs that <em>can't afford to guess.</em></h1>
        <p class="lede reveal">Cargill Consulting is my enterprise practice. I design identity platforms, datacenter and virtualization environments, cloud migrations, and the operational plumbing that holds them together. Twenty years of it. Hands on the keyboard.</p>
      </div>
      <div class="dossier reveal">
        <dl>
          <dt>Positioning</dt><dd>Specialist architect, not a generalist shop</dd>
          <dt>Buyers</dt><dd>Fortune 1000, regulated industries, large IT orgs</dd>
          <dt>Engagement</dt><dd>Assessment · SME retainer · fixed-scope design</dd>
          <dt>Current</dt><dd>Sr. Systems Engineer, Texas Mutual Insurance</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <span class="eyebrow eyebrow-rule">Capabilities</span>
    <h2>Four depths I sell.</h2>
    <div class="grid grid-2 mt-3">
      <a href="identity/" class="card">
        <span class="card-eyebrow">Identity</span>
        <h3>Okta &amp; Global Identity Architecture</h3>
        <p>Okta SSO, MFA, policy, lifecycle automation, workflows, federation design, Azure-integrated identity patterns.</p>
        <span class="card-arrow">Open capability</span>
      </a>
      <a href="infrastructure/" class="card">
        <span class="card-eyebrow">Infrastructure</span>
        <h3>Enterprise Infrastructure</h3>
        <p>VMware/vSphere, Cisco UCS, NetApp, multi-site datacenter design, recovery topology, operational documentation.</p>
        <span class="card-arrow">Open capability</span>
      </a>
      <a href="cloud/" class="card">
        <span class="card-eyebrow">Cloud</span>
        <h3>Cloud Platform Architecture</h3>
        <p>Migration planning, hybrid architecture, OpenShift adoption, platform strategy beyond lift-and-shift.</p>
        <span class="card-arrow">Open capability</span>
      </a>
      <a href="devops/" class="card">
        <span class="card-eyebrow">DevOps</span>
        <h3>DevOps &amp; Platform Engineering</h3>
        <p>CI/CD pipelines, Ansible &amp; Terraform, GitHub operational tooling, automation that actually survives audit.</p>
        <span class="card-arrow">Open capability</span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow eyebrow-rule">How to engage</span>
        <h2>Three ways to buy architecture work.</h2>
      </div>
      <div>
        <ol class="process">
          <li>
            <h4>Architecture assessment</h4>
            <p>Fixed-scope, 2–4 weeks, one deliverable: a written architecture report with prioritized findings and a remediation roadmap. Most common starting point.</p>
          </li>
          <li>
            <h4>SME-on-retainer</h4>
            <p>Standing hours per month — design review, escalations, working sessions with your team. I'm the Okta SME (or VMware, or UCS) sitting next to your engineers without the full-time headcount.</p>
          </li>
          <li>
            <h4>Fixed-scope design</h4>
            <p>Specific deliverable — an Okta tenant design, a UCS topology, a migration runbook. Scoped up front, priced before we start, written contract.</p>
          </li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">Case evidence</span>
    <h2>Representative environments.</h2>
    <p class="muted">Redacted case studies live in the project lab under Projects › Clients. A fuller enterprise case library is available on request during engagement conversations.</p>
    <div class="grid grid-3 mt-3">
      <div class="card">
        <span class="card-eyebrow">Insurance · Current</span>
        <h3>Texas Mutual</h3>
        <p>Senior Systems Engineer. VMware, UCS audit, NetApp, OpenShift migration planning across ~930 VMs and 56 hosts spanning production and DR.</p>
      </div>
      <div class="card">
        <span class="card-eyebrow">Healthcare · Prior</span>
        <h3>Harbor Health</h3>
        <p>Multi-clinic standardized network and endpoint topology. Repeatable blueprint across clinics, call center, HQ, and mobile units.</p>
      </div>
      <div class="card">
        <span class="card-eyebrow">Manufacturing · Prior</span>
        <h3>CMTX / EC Cross-Site</h3>
        <p>TX + CA production workflow architecture, HP Indigo integration, Onyx VPS pipeline, scripted distribution between sites.</p>
      </div>
    </div>
  </div>
</section>
"""
write("professional/cargill-consulting/index.html", page("Cargill Consulting — Enterprise Architecture", 2, body, active="Cargill Consulting"))


# ============================================================================
# 1.a.1 Identity (Okta)
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("Cargill Consulting", "professional/cargill-consulting/"), ("Identity", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">Cargill Consulting · Capability</span>
    <h1 class="reveal">Identity architecture built to <em>actually ship.</em></h1>
    <p class="lede reveal">Okta SME work. Federation. Lifecycle automation. Azure-integrated identity. Policy that reflects the business, not a vendor's default template.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-3">
      <div class="card"><span class="card-eyebrow">Okta</span><h3>Design &amp; Admin</h3><p>Enterprise SSO, adaptive MFA, policy structure, application onboarding, sign-on experience, administrative governance.</p></div>
      <div class="card"><span class="card-eyebrow">Automation</span><h3>Workflows &amp; Lifecycle</h3><p>Okta Workflows, event-driven provisioning, criteria-based automations, onboarding/offboarding, role-driven access logic.</p></div>
      <div class="card"><span class="card-eyebrow">Azure</span><h3>Hybrid Identity</h3><p>Azure-connected services, directory-driven access, hybrid integration patterns between on-prem and cloud-native identity.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow eyebrow-rule">Solution areas</span>
        <h2>Federation, lifecycle, and platform-level thinking.</h2>
      </div>
      <div>
        <h3>Enterprise SSO &amp; Federation</h3>
        <ul>
          <li>SAML and OIDC application integrations</li>
          <li>Okta-driven authentication across enterprise apps</li>
          <li>Policy alignment for sign-in and access enforcement</li>
          <li>Better user experience without weakening controls</li>
        </ul>
        <h3 class="mt-3">Identity Automation &amp; Provisioning</h3>
        <ul>
          <li>Automated onboarding, change, and offboarding</li>
          <li>Role and group-driven access logic</li>
          <li>Conditional workflow automation on identity criteria</li>
          <li>Reduced manual admin, cleaner operational control</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule">Best-fit engagements</span>
    <h2>When to bring me in.</h2>
    <ul>
      <li>You're consolidating onto Okta and need a tenant design before applications start onboarding</li>
      <li>Your lifecycle automation is manual and your offboarding has gaps</li>
      <li>You've got Azure identity entangled with Okta and need a federation model that doesn't fight itself</li>
      <li>Your access review process is a spreadsheet and your auditor has noticed</li>
    </ul>
    <div class="btn-cluster">
      <a class="btn" href="../">Back to Cargill Consulting</a>
      <a class="btn btn-ghost" href="../../about/resumes/">Identity-focused resume</a>
    </div>
  </div>
</section>
"""
write("professional/cargill-consulting/identity/index.html", page("Identity &amp; Okta Architecture", 3, body, active="Cargill Consulting"))


# ============================================================================
# 1.a.2 Infrastructure
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("Cargill Consulting", "professional/cargill-consulting/"), ("Infrastructure", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">Cargill Consulting · Capability</span>
    <h1 class="reveal">Datacenter work that <em>holds under audit.</em></h1>
    <p class="lede reveal">VMware/vSphere, Cisco UCS, NetApp storage, recovery topology, operational documentation. Multi-site datacenter environments, healthcare clinic rollouts, manufacturing print automation — architected, implemented, documented.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="stats">
      <div class="stat"><span class="stat-num">930+</span><span class="stat-label">VMs across prod &amp; DR</span></div>
      <div class="stat"><span class="stat-num">56</span><span class="stat-label">ESXi hosts</span></div>
      <div class="stat"><span class="stat-num">68</span><span class="stat-label">UCS blades audited</span></div>
      <div class="stat"><span class="stat-num">20+</span><span class="stat-label">years in infrastructure</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">Patterns I repeatedly put in place</span>
    <h2>Architecture themes.</h2>
    <div class="mt-3">
      <span class="chip">Datacenter core design</span>
      <span class="chip">Site-to-site connectivity</span>
      <span class="chip">Virtualization &amp; storage</span>
      <span class="chip">Workflow automation</span>
      <span class="chip">Operational documentation</span>
      <span class="chip">Device &amp; endpoint standardization</span>
      <span class="chip">Production / OT integration</span>
      <span class="chip">Migration readiness</span>
      <span class="chip accent">Cisco UCS architecture</span>
      <span class="chip accent">Recovery topology</span>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">Representative environments</span>
    <h2>Real diagrams from real environments.</h2>
    <p class="muted">The complete infrastructure gallery — with diagrams, topology views, and case detail — lives in the project lab.</p>
    <div class="grid grid-2 mt-3">
      <a href="../../../projects/infrastructure/" class="card">
        <span class="card-eyebrow">Texas Mutual</span>
        <h3>Cisco UCS Topology</h3>
        <p>Fabric interconnects, chassis layout, blade population, ESXi host placement, enterprise storage, backup integration across production and DR.</p>
        <span class="card-arrow">Open gallery</span>
      </a>
      <a href="../../../projects/infrastructure/" class="card">
        <span class="card-eyebrow">Harbor Health</span>
        <h3>Multi-Clinic Standard</h3>
        <p>Repeatable clinic design — firewall, switching, APs, printers, iPads, phones, connected medical devices. HQ, call center, and mobile units.</p>
        <span class="card-arrow">Open gallery</span>
      </a>
      <a href="../../../projects/infrastructure/" class="card">
        <span class="card-eyebrow">CMTX / EC</span>
        <h3>TX + CA Production Workflow</h3>
        <p>Cross-site designer handoff, batch processing, HP Indigo systems, shared resources, scripted distribution between Texas and California.</p>
        <span class="card-arrow">Open gallery</span>
      </a>
      <a href="../../../projects/infrastructure/" class="card">
        <span class="card-eyebrow">Hybrid &amp; Migration</span>
        <h3>Support &amp; Cloud Gateway</h3>
        <p>On-prem to virtual to cloud gateway mapping, backup flows, migration readiness documentation.</p>
        <span class="card-arrow">Open gallery</span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule">Best-fit roles &amp; engagements</span>
    <h2>When to bring me in.</h2>
    <ul>
      <li>Your VMware estate has aged and you need a modernization plan, not a vendor pitch</li>
      <li>UCS health and lifecycle are unclear and your DR story rests on a prayer</li>
      <li>You've got multi-site operational complexity and no documented standard</li>
      <li>You need an OpenShift migration plan that survives a 24–36 month horizon</li>
    </ul>
    <div class="btn-cluster">
      <a class="btn" href="../">Back to Cargill Consulting</a>
      <a class="btn btn-ghost" href="../../about/resumes/">Infrastructure-focused resume</a>
    </div>
  </div>
</section>
"""
write("professional/cargill-consulting/infrastructure/index.html", page("Enterprise Infrastructure", 3, body, active="Cargill Consulting"))


# ============================================================================
# 1.a.3 Cloud
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("Cargill Consulting", "professional/cargill-consulting/"), ("Cloud", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">Cargill Consulting · Capability</span>
    <h1 class="reveal">Cloud architecture <em>past the lift-and-shift.</em></h1>
    <p class="lede reveal">Most enterprise cloud migrations stall because the target architecture was never designed — the workload just moved. I build migration plans that respect the operational model, the regulatory posture, and the platform engineering maturity of the team that has to run it.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-3">
      <div class="card">
        <span class="card-eyebrow">Strategy</span>
        <h3>Migration Planning</h3>
        <p>Wave planning, dependency mapping, landing-zone design, cutover choreography, rollback posture. What to move, when, and what stays.</p>
      </div>
      <div class="card">
        <span class="card-eyebrow">Hybrid</span>
        <h3>Hybrid Architecture</h3>
        <p>Identity bridges, network connectivity, data gravity analysis, cost-model honesty. Hybrid is a destination for some workloads, not just a waypoint.</p>
      </div>
      <div class="card">
        <span class="card-eyebrow">Platform</span>
        <h3>OpenShift &amp; Container Platform</h3>
        <p>OpenShift adoption roadmap, SNO POC design, operator strategy, GitOps posture, workload modernization beyond pure lift.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule">Recent work</span>
    <h2>OpenShift migration, 24–36 month horizon.</h2>
    <p>A recent engagement produced: RVTools-based infrastructure analysis across production and DR vCenters, a Jira-import CSV for modernization backlog, a POC runbook targeting a specific WebSphere cluster for Single Node OpenShift, and an OpenShift working session with Red Hat engineering. The plan accounts for expiring SSL certs, multipath storage anomalies, dead boot LUNs, and UCS node health — because cloud migration planning that ignores the source state is fiction.</p>
    <div class="btn-cluster">
      <a class="btn" href="../">Back to Cargill Consulting</a>
      <a class="btn btn-ghost" href="../../../projects/devops-cloud/">See the DevOps &amp; Cloud lab</a>
    </div>
  </div>
</section>
"""
write("professional/cargill-consulting/cloud/index.html", page("Cloud Platform Architecture", 3, body, active="Cargill Consulting"))


# ============================================================================
# 1.a.4 DevOps
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("Cargill Consulting", "professional/cargill-consulting/"), ("DevOps", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">Cargill Consulting · Capability</span>
    <h1 class="reveal">Automation that <em>survives audit.</em></h1>
    <p class="lede reveal">Pipelines, infrastructure as code, and platform tooling designed for the team that has to maintain them on day 400, not just day 40.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-3">
      <div class="card"><span class="card-eyebrow">CI/CD</span><h3>Pipeline Design</h3><p>Delivery pipelines with clear gates, approvals, and rollback. Not clever — supportable.</p></div>
      <div class="card"><span class="card-eyebrow">IaC</span><h3>Terraform &amp; Ansible</h3><p>Infrastructure as code with module structure, state discipline, and environment promotion that actually works.</p></div>
      <div class="card"><span class="card-eyebrow">Tooling</span><h3>Operational Utilities</h3><p>Internal tools — repo inventory, scoring, compliance reporting — that give the platform team visibility without a vendor contract.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule">Representative artifact</span>
    <h2>GitHub Repo Utility Inventory.</h2>
    <p>A React-based inventory and scoring tool for enterprise repo hygiene: tags, scoring criteria, CSV export. Built to give platform leads a current view of what's alive, what's rotting, and what's worth the migration effort. Lives under the project lab; adapts to most mid-size enterprise repo estates.</p>
    <div class="btn-cluster">
      <a class="btn" href="../../../projects/devops-cloud/">Open the DevOps lab</a>
      <a class="btn btn-ghost" href="../">Back to Cargill Consulting</a>
    </div>
  </div>
</section>
"""
write("professional/cargill-consulting/devops/index.html", page("DevOps &amp; Platform Engineering", 3, body, active="Cargill Consulting"))


# ============================================================================
# 1.b NEXT-GEN-IT hub
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("Next-Gen-IT", None)], 2) + """
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow eyebrow-rule reveal">1.b · Small-Business Practice</span>
        <h1 class="reveal">Real architecture for small firms — <em>not another help desk.</em></h1>
        <p class="lede reveal">Next-Gen-IT is my SMB practice. Three packaged offers, fixed scope, real deliverables. Built for owner-operated firms — title companies, realty offices, small clinics — that need an architect, not a break-fix vendor.</p>
      </div>
      <div class="dossier reveal">
        <dl>
          <dt>Who it's for</dt><dd>Owner-operated firms, ~5–50 seats</dd>
          <dt>Industries</dt><dd>Title · Realty · Clinics · Professional services</dd>
          <dt>Model</dt><dd>Packaged offers, not hourly mystery meat</dd>
          <dt>Proof</dt><dd>TeleoTitle · Abode Labs</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <span class="eyebrow eyebrow-rule">Three packaged offers</span>
    <h2>Pick the one you need.</h2>
    <div class="grid grid-3 mt-3">
      <a href="audit/" class="offer">
        <span class="card-eyebrow">1.b.1</span>
        <h3>Next-Gen-Audit</h3>
        <p>One-time, fixed-scope IT &amp; security audit. One PDF, one remediation runbook. You know exactly what you have and exactly what to fix.</p>
        <span class="price">Fixed scope · 2 weeks · Deliverable-based</span>
        <span class="card-arrow">See the offer</span>
      </a>
      <a href="operations/" class="offer">
        <span class="card-eyebrow">1.b.2</span>
        <h3>Next-Gen-Operations</h3>
        <p>Ongoing IT operations — endpoint hygiene, backup verification, monitoring, patch discipline, basic network. Retainer-based, outcome-defined.</p>
        <span class="price">Monthly retainer · Outcome SLA</span>
        <span class="card-arrow">See the offer</span>
      </a>
      <a href="security/" class="offer">
        <span class="card-eyebrow">1.b.3</span>
        <h3>Next-Gen-Security</h3>
        <p>DMARC enforcement, wire-fraud prevention, MFA rollout, phishing simulation, incident playbook. Packaged by firm type.</p>
        <span class="price">Fixed scope · 3–4 weeks</span>
        <span class="card-arrow">See the offer</span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow eyebrow-rule">Why this practice exists</span>
        <h2>Title companies, realtors, and small clinics are wire-fraud targets.</h2>
      </div>
      <div>
        <p>The small firms I work with are high-value targets — title companies move hundreds of thousands in wires, realty offices handle earnest money, clinics sit on HIPAA data. The IT vendors serving them are usually break-fix shops that haven't heard the words DMARC, DKIM, or SPF, let alone enforced them.</p>
        <p>Next-Gen-IT is what happens when an enterprise architect packages the right 10% of enterprise security and operations posture into fixed-scope offers that a five-person firm can actually buy.</p>
        <div class="btn-cluster">
          <a class="btn" href="../../projects/clients/teleotitle/">TeleoTitle case</a>
          <a class="btn btn-ghost" href="../../projects/clients/abode-labs/">Abode Labs case</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
write("professional/next-gen-it/index.html", page("Next-Gen-IT — SMB Practice", 2, body, active="Next-Gen-IT"))


# ============================================================================
# 1.b.1 Next-Gen-Audit
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("Next-Gen-IT", "professional/next-gen-it/"), ("Next-Gen-Audit", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">1.b.1 · Packaged Offer</span>
    <h1 class="reveal">Next-Gen-Audit.</h1>
    <p class="lede reveal">Fixed-scope IT &amp; security audit. Two weeks. Two deliverables — a clean findings PDF and a copy-pasteable remediation runbook. You leave knowing exactly what you have and exactly what to fix first.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="offer">
      <dl>
        <dt>Who it's for</dt><dd>Owner-operators, office managers, or IT leads at 5–50 seat firms who want a clear picture before they make the next spend.</dd>
        <dt>Timeline</dt><dd>2 weeks start to finish. One kickoff call, one closeout call.</dd>
        <dt>Deliverables</dt><dd><strong>1.</strong> Findings PDF with prioritized issues, evidence, and business-risk framing. <strong>2.</strong> Remediation runbook with concrete steps, copy-pasteable commands, and a risk-ordered sequence.</dd>
        <dt>What's included</dt><dd>Email authentication (SPF/DKIM/DMARC) posture · endpoint inventory &amp; patch state · backup verification · MFA coverage · admin account hygiene · cloud app inventory · wire-fraud exposure surface (title/realty only) · network baseline · external attack-surface sweep.</dd>
        <dt>What's NOT included</dt><dd>Remediation execution · ongoing monitoring · compliance attestation · penetration testing. Those are separate engagements.</dd>
      </dl>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">How it runs</span>
    <h2>Two weeks, four milestones.</h2>
    <ol class="process">
      <li>
        <h4>Kickoff &amp; evidence collection</h4>
        <p>One 45-minute call. Account access provisioning with proper controls. Inventory questionnaire. Day 1–3.</p>
      </li>
      <li>
        <h4>Assessment sweep</h4>
        <p>Email authentication scan, endpoint inventory pull, backup validation, MFA coverage review, admin audit, cloud inventory, external attack surface sweep. Day 4–9.</p>
      </li>
      <li>
        <h4>Write-up &amp; prioritization</h4>
        <p>Findings compiled into the PDF. Remediation runbook written with explicit DNS records, command snippets, and vendor-specific steps. Day 10–12.</p>
      </li>
      <li>
        <h4>Closeout</h4>
        <p>One-hour review call. Questions answered, trade-offs explained. Runbook handed off. Day 13–14.</p>
      </li>
    </ol>
  </div>
</section>

<section>
  <div class="container">
    <div class="callout">
      <div class="callout-label">Proof of concept</div>
      <p>The DNS and email-authentication runbook I built for <a href="../../../projects/clients/abode-labs/">Abode Labs</a> and <a href="../../../projects/clients/teleotitle/">TeleoTitle</a> is the prototype deliverable for this offer — DMARC enforcement, wire-fraud risk framing, and concrete DNS remediation with copy-pasteable syntax.</p>
    </div>
  </div>
</section>

<section>
  <div class="container narrow tc">
    <h2>Ready to know what you actually have?</h2>
    <div class="btn-cluster" style="justify-content:center">
      <a class="btn" href="mailto:jeremiah@cargillco.example">Start an audit</a>
      <a class="btn btn-ghost" href="../">Back to Next-Gen-IT</a>
    </div>
    <p class="muted mt-2"><span class="mono">Contact email is a placeholder — update before publishing.</span></p>
  </div>
</section>
"""
write("professional/next-gen-it/audit/index.html", page("Next-Gen-Audit — IT &amp; Security Audit", 3, body, active="Next-Gen-IT"))


# ============================================================================
# 1.b.2 Next-Gen-Operations
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("Next-Gen-IT", "professional/next-gen-it/"), ("Next-Gen-Operations", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">1.b.2 · Packaged Offer</span>
    <h1 class="reveal">Next-Gen-Operations.</h1>
    <p class="lede reveal">Ongoing IT operations on a retainer, with outcomes written into the agreement. Endpoint hygiene, backup verification, monitoring, patch discipline, basic network — done on a schedule, reported monthly, with someone on the hook.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="offer">
      <dl>
        <dt>Who it's for</dt><dd>Small firms whose current IT is a mix of one employee's nephew, a break-fix vendor, and wishful thinking.</dd>
        <dt>Model</dt><dd>Monthly retainer. Outcome-defined SLAs — not "hours used."</dd>
        <dt>Cadence</dt><dd>Weekly check (automated health), monthly report (human review), quarterly strategy call.</dd>
        <dt>Scope in</dt><dd>Endpoint patch &amp; hygiene · backup verification with restore test · monitoring &amp; alerting · DNS &amp; email auth drift · admin account review · user lifecycle · basic network care · tickets on defined SLA.</dd>
        <dt>Scope out</dt><dd>Net-new architecture projects · application development · compliance audit prep · incident response beyond standard tier. Those get scoped separately.</dd>
      </dl>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">What "outcome SLA" actually means</span>
    <h2>Commitments, not hours.</h2>
    <div class="grid grid-3 mt-3">
      <div class="card"><span class="card-eyebrow">Patching</span><h3>95%+ endpoint patch compliance, 30-day window.</h3><p>Not "we'll try to patch." Reported monthly with evidence.</p></div>
      <div class="card"><span class="card-eyebrow">Backups</span><h3>Verified restore test, quarterly.</h3><p>A backup that hasn't been restored is a theory.</p></div>
      <div class="card"><span class="card-eyebrow">Email auth</span><h3>DMARC reject maintained.</h3><p>Drift detected within 48 hours, reported within 72.</p></div>
      <div class="card"><span class="card-eyebrow">Monitoring</span><h3>Alerts acknowledged in 1 business hour.</h3><p>Triaged and escalated on defined paths.</p></div>
      <div class="card"><span class="card-eyebrow">Admin accounts</span><h3>Monthly review of privileged access.</h3><p>Departures actioned within 24 hours of notification.</p></div>
      <div class="card"><span class="card-eyebrow">Reporting</span><h3>One-page monthly report.</h3><p>Plain English. What's green, what's yellow, what needs a decision.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container narrow tc">
    <h2>Operations you can actually point to.</h2>
    <div class="btn-cluster" style="justify-content:center">
      <a class="btn" href="mailto:jeremiah@cargillco.example">Discuss retainer</a>
      <a class="btn btn-ghost" href="../">Back to Next-Gen-IT</a>
    </div>
  </div>
</section>
"""
write("professional/next-gen-it/operations/index.html", page("Next-Gen-Operations — SMB IT on Retainer", 3, body, active="Next-Gen-IT"))


# ============================================================================
# 1.b.3 Next-Gen-Security
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("Next-Gen-IT", "professional/next-gen-it/"), ("Next-Gen-Security", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">1.b.3 · Packaged Offer</span>
    <h1 class="reveal">Next-Gen-Security.</h1>
    <p class="lede reveal">The wire-fraud and email-impersonation posture your firm needs before the next attempt lands. DMARC enforcement, MFA rollout, phishing simulation, incident playbook — packaged by firm type, priced before we start.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-2">
      <div class="offer">
        <h3>Title-company package</h3>
        <p>Purpose-built for the wire-fraud threat model that title firms live under every day.</p>
        <dl>
          <dt>DNS posture</dt><dd>SPF · DKIM · DMARC enforcement across all sending domains, including look-alikes</dd>
          <dt>Wire protocol</dt><dd>Out-of-band wire verification process + signed staff playbook</dd>
          <dt>MFA</dt><dd>Phishing-resistant MFA on email &amp; escrow systems</dd>
          <dt>Training</dt><dd>Quarterly phishing sim with tracked improvement</dd>
          <dt>Incident runbook</dt><dd>Written, rehearsed, and actually findable at 3am</dd>
        </dl>
      </div>
      <div class="offer">
        <h3>Realty &amp; professional-services package</h3>
        <p>Earnest-money fraud, client-data exposure, and impersonation risk tuned to realty and services firms.</p>
        <dl>
          <dt>DNS posture</dt><dd>SPF · DKIM · DMARC enforcement + monitoring</dd>
          <dt>Account security</dt><dd>MFA baseline, password manager rollout, admin hardening</dd>
          <dt>Client data</dt><dd>Secure document exchange process, mobile device posture</dd>
          <dt>Training</dt><dd>Role-appropriate phishing simulation</dd>
          <dt>Incident runbook</dt><dd>Simple decision tree for the "I clicked it" moment</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="callout">
      <div class="callout-label">Why this is a real offer and not an upsell</div>
      <p>The industry's open secret is that title companies and realty firms are disproportionately targeted for wire fraud precisely because their IT vendors don't enforce the basics. The DMARC runbook I wrote for TeleoTitle — a real deliverable, not a sales deck — is the working spec for this offer. If your firm handles client money or confidential transactions, the question isn't whether you're a target, it's whether you're a <em>hardened</em> target.</p>
    </div>
  </div>
</section>

<section>
  <div class="container narrow tc">
    <h2>Close the wire-fraud window.</h2>
    <div class="btn-cluster" style="justify-content:center">
      <a class="btn" href="mailto:jeremiah@cargillco.example">Start the engagement</a>
      <a class="btn btn-ghost" href="../../../projects/clients/teleotitle/">Read the TeleoTitle case</a>
    </div>
  </div>
</section>
"""
write("professional/next-gen-it/security/index.html", page("Next-Gen-Security — DMARC, MFA, Wire-Fraud Prevention", 3, body, active="Next-Gen-IT"))


# ============================================================================
# 1.c ABOUT hub
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("About", None)], 2) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">1.c · About</span>
    <h1 class="reveal">Who you're <em>actually hiring.</em></h1>
    <p class="lede reveal">One architect, two practices, twenty-plus years. Below, the pieces of the story that matter depending on which door you came in.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-3">
      <a href="resumes/" class="card">
        <span class="card-eyebrow">1.c.1</span>
        <h3>Resumes</h3>
        <p>Three targeted resume versions — Enterprise Infrastructure, Okta Identity, Cloud/DevOps. Each opens clean for print or send.</p>
        <span class="card-arrow">Open resume center</span>
      </a>
      <a href="cargill-consulting/" class="card">
        <span class="card-eyebrow">1.c.2</span>
        <h3>Why Cargill Consulting</h3>
        <p>The enterprise practice origin story — what the work looks like, how engagements are shaped, what you get that you don't get from a bodyshop.</p>
        <span class="card-arrow">Read the story</span>
      </a>
      <a href="next-gen-it/" class="card">
        <span class="card-eyebrow">1.c.3</span>
        <h3>Why Next-Gen-IT</h3>
        <p>The SMB practice origin story — why small firms need real architecture, the moment that crystallized the practice, what's different.</p>
        <span class="card-arrow">Read the story</span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule">The short version</span>
    <h2>Jeremiah Cargill, in 120 words.</h2>
    <p>Senior infrastructure engineer and enterprise architect based in the Austin / Central Texas area. Twenty-plus years across VMware, Cisco UCS, NetApp storage, Kubernetes, and network forensics. Current role: Senior Systems Engineer at Texas Mutual Insurance — VMware platform support, UCS and datacenter analysis, OpenShift migration planning.</p>
    <p>Okta SME. Strong in identity architecture, federation, lifecycle automation, and Azure-integrated identity patterns. Independent: run Cargill Consulting (enterprise) and Next-Gen-IT (SMB) as two parallel practices. Active project lab including infrastructure tooling, AI integrations, and a neutral-analysis platform for co-parenting and legal conflict documentation.</p>
    <div class="btn-cluster">
      <a class="btn" href="resumes/">Targeted resumes</a>
      <a class="btn btn-ghost" href="https://github.com/jeremiah9980">GitHub</a>
    </div>
  </div>
</section>
"""
write("professional/about/index.html", page("About Jeremiah Cargill", 2, body, active="About"))


# ============================================================================
# 1.c.1 Resumes
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("About", "professional/about/"), ("Resumes", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">Resume Center</span>
    <h1 class="reveal">Three versions. <em>Pick the conversation.</em></h1>
    <p class="lede reveal">Each version is a standalone resume built for a different opportunity profile. Clean to print, easy to send to recruiters, honest about positioning.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-3">
      <div class="offer">
        <span class="card-eyebrow">Version 1</span>
        <h3>Enterprise Infrastructure Architect</h3>
        <p>Best for infrastructure leadership, enterprise systems, virtualization, networking, datacenter operations, and architecture-heavy systems roles.</p>
        <ul>
          <li>Strong infrastructure and networking depth</li>
          <li>Enterprise systems architecture framing</li>
          <li>Virtualization, DR, and operational leadership</li>
        </ul>
        <div class="btn-cluster">
          <a class="btn" href="https://jeremiah9980.github.io/jeremiah9980/resumes/enterprise-infrastructure-architect.html">Open clean version</a>
        </div>
      </div>
      <div class="offer">
        <span class="card-eyebrow">Version 2</span>
        <h3>Global Identity Architect / Okta SME</h3>
        <p>Best for identity architecture, Okta, Azure identity, SSO, MFA, lifecycle automation, federation, and enterprise access management roles.</p>
        <ul>
          <li>Okta-centered positioning</li>
          <li>Workflow and automation language</li>
          <li>Azure identity alignment</li>
        </ul>
        <div class="btn-cluster">
          <a class="btn" href="https://jeremiah9980.github.io/jeremiah9980/resumes/okta-global-identity-architect.html">Open clean version</a>
        </div>
      </div>
      <div class="offer">
        <span class="card-eyebrow">Version 3</span>
        <h3>Cloud Platform &amp; DevOps Architect</h3>
        <p>Best for platform engineering, cloud infrastructure, automation, DevOps, Terraform, CI/CD, and modern enterprise delivery roles.</p>
        <ul>
          <li>Cloud and automation emphasis</li>
          <li>Terraform and platform language</li>
          <li>Modern engineering profile</li>
        </ul>
        <div class="btn-cluster">
          <a class="btn" href="https://jeremiah9980.github.io/jeremiah9980/resumes/cloud-platform-devops-architect.html">Open clean version</a>
        </div>
      </div>
    </div>
    <div class="scaffold mt-4">
      <div class="scaffold-label">Migration note</div>
      <p>These currently link to the existing v1 site. When you port the three resume HTMLs into <code>/professional/about/resumes/</code> as individual files, update the links above.</p>
    </div>
  </div>
</section>
"""
write("professional/about/resumes/index.html", page("Resume Center", 3, body, active="About"))


# ============================================================================
# 1.c.2 About → Cargill Consulting narrative
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("About", "professional/about/"), ("Cargill Consulting", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">1.c.2 · Practice Origin</span>
    <h1 class="reveal">Why Cargill Consulting exists.</h1>
    <p class="lede reveal">The enterprise practice is the formal home for the work I've been doing for two decades — identity, infrastructure, cloud, platform engineering — delivered as an independent specialist rather than as a cog in a bodyshop.</p>
  </div>
</section>

<section class="tight">
  <div class="container narrow">
    <h2>The shape of the practice.</h2>
    <p>Enterprise IT orgs increasingly want specialist depth without the full-time headcount. A Fortune 1000 insurer doesn't need a "DevOps team" — it needs an Okta SME for six months, an infrastructure architect to chair a UCS modernization, a cloud platform specialist to write the OpenShift landing zone. Cargill Consulting is packaged to drop into exactly those spots.</p>

    <h2 class="mt-4">What you get that you don't get from a bodyshop.</h2>
    <ul>
      <li><strong>One architect, not a rotating bench.</strong> You talk to me for the whole engagement.</li>
      <li><strong>Hands on the keyboard.</strong> I write the runbook. I run the RVTools pull. I build the Terraform module. Architecture without execution is a slide deck.</li>
      <li><strong>Documentation as a first-class deliverable.</strong> Most architecture work dies because the knowledge leaves with the consultant. The written artifacts are the point.</li>
      <li><strong>Honest scope.</strong> If your problem is smaller than you think, the engagement is smaller. If it's bigger, I'll tell you up front.</li>
    </ul>

    <h2 class="mt-4">Engagement shapes.</h2>
    <ol class="process">
      <li><h4>Architecture assessment</h4><p>Two to four weeks. Fixed fee. One deliverable: a written architecture report with prioritized findings and a remediation roadmap.</p></li>
      <li><h4>SME-on-retainer</h4><p>Standing hours per month. Design review, escalations, working sessions with your team. I sit next to your engineers without the headcount.</p></li>
      <li><h4>Fixed-scope design</h4><p>A specific deliverable — Okta tenant design, UCS topology, migration runbook. Scoped up front, priced before we start.</p></li>
    </ol>

    <div class="btn-cluster mt-4">
      <a class="btn" href="../../cargill-consulting/">Open the practice</a>
      <a class="btn btn-ghost" href="../resumes/">Resume versions</a>
    </div>
  </div>
</section>
"""
write("professional/about/cargill-consulting/index.html", page("About Cargill Consulting", 3, body, active="About"))


# ============================================================================
# 1.c.3 About → Next-Gen-IT narrative
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Professional", "professional/"), ("About", "professional/about/"), ("Next-Gen-IT", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">1.c.3 · Practice Origin</span>
    <h1 class="reveal">Why Next-Gen-IT exists.</h1>
    <p class="lede reveal">A title-company contact sent me his firm's DMARC posture and his email authentication setup. It was wide open. That was the moment the SMB practice went from "someone should do this" to "I'm going to do this."</p>
  </div>
</section>

<section class="tight">
  <div class="container narrow">
    <h2>The gap.</h2>
    <p>Small firms handling real money — title companies, realty offices, small clinics, professional services — are disproportionately targeted for wire fraud and email impersonation. The IT vendors serving them are mostly break-fix shops. They fix printers. They set up new laptops. They don't enforce DMARC. They've never written an incident runbook.</p>
    <p>The result is that a five-person title firm moving half a million in wires a week has the same security posture as someone's cousin's LLC — because that's who set it up.</p>

    <h2 class="mt-4">The thesis.</h2>
    <p>Enterprise security posture isn't magic. The right 10% of it — email authentication, MFA, backup verification, admin hygiene, incident playbook — is exactly what a small firm needs. The problem isn't knowledge, it's packaging. Small firms can't buy a $200K security assessment. They need the right outcomes in a shape they can actually afford.</p>
    <p>Next-Gen-IT packages the right 10% into three fixed-scope offers. You know what you're buying, what you're getting, and when you're done.</p>

    <h2 class="mt-4">The proof.</h2>
    <p>The DNS and email-authentication runbook I built for TeleoTitle and Abode Labs — DMARC enforcement, wire-fraud risk framing, concrete DNS remediation with copy-pasteable syntax — is the working prototype for the Next-Gen-Audit and Next-Gen-Security offers. Not a pitch deck. A real deliverable, built for a real firm, now packaged for repeat delivery.</p>

    <div class="btn-cluster mt-4">
      <a class="btn" href="../../next-gen-it/">Open the practice</a>
      <a class="btn btn-ghost" href="../../../projects/clients/teleotitle/">TeleoTitle case</a>
    </div>
  </div>
</section>
"""
write("professional/about/next-gen-it/index.html", page("About Next-Gen-IT", 3, body, active="About"))


# ============================================================================
# 2. PROJECTS router
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", None)], 1) + """
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow eyebrow-rule reveal">02 · Project Lab</span>
        <h1 class="reveal">Independent work, <em>built in production.</em></h1>
        <p class="lede reveal">Some of these are client deliverables. Some are pure lab. One is a platform I'm building out into its own product. All of them ship code, not just ideas.</p>
      </div>
      <div class="dossier reveal">
        <dl>
          <dt>Stance</dt><dd>Executable artifacts over advisory output</dd>
          <dt>Scope</dt><dd>Infrastructure · DevOps · AI · Legal-tech · GPS</dd>
          <dt>Public repo</dt><dd><a href="https://github.com/jeremiah9980">github.com/jeremiah9980</a></dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-3">
      <a href="infrastructure/" class="card">
        <span class="card-eyebrow">2.a</span>
        <h3>Infrastructure</h3>
        <p>VMware, UCS, NetApp, OpenShift migration work. RVTools reports, Jira-import CSVs, POC runbooks, health analyses.</p>
        <span class="card-arrow">Open</span>
      </a>
      <a href="devops-cloud/" class="card">
        <span class="card-eyebrow">2.b</span>
        <h3>DevOps / Cloud</h3>
        <p>CI/CD pipelines, Ansible &amp; Terraform, GitHub Repo Utility Inventory (React), platform tooling.</p>
        <span class="card-arrow">Open</span>
      </a>
      <a href="ai/" class="card">
        <span class="card-eyebrow">2.c</span>
        <h3>AI</h3>
        <p>AI platform assistant, Claude API integrations into productivity tooling, agent patterns, skill-creator workflow.</p>
        <span class="card-arrow">Open</span>
      </a>
      <a href="gamechanger/" class="card">
        <span class="card-eyebrow">2.d</span>
        <h3>Video / GameChanger</h3>
        <p>OBS/streaming workflow tooling and the GameChanger video project. Early stage.</p>
        <span class="card-arrow">Open</span>
      </a>
      <a href="conflict-collection/" class="card">
        <span class="card-eyebrow">2.e · Flagship</span>
        <h3>Conflict Collection Platform</h3>
        <p>Multi-channel conflict ingestion, neutral multi-model analysis, timeline builder, court-ready exhibit builder. For co-parents, attorneys, mediators.</p>
        <span class="card-arrow">Open</span>
      </a>
      <a href="gps/" class="card">
        <span class="card-eyebrow">2.f</span>
        <h3>GPS</h3>
        <p>Timeline builder and live tracker. Standalone — and a potential evidence source for Conflict Collection.</p>
        <span class="card-arrow">Open</span>
      </a>
      <a href="flywheel/" class="card">
        <span class="card-eyebrow">2.g</span>
        <h3>Flywheel</h3>
        <p>Business-operations / automation flywheel project. Scoping in progress.</p>
        <span class="card-arrow">Open</span>
      </a>
      <a href="clients/" class="card">
        <span class="card-eyebrow">2.h · Case studies</span>
        <h3>Clients</h3>
        <p>Redacted client case studies — CosmicGen, TeleoTitle, Abode Labs, Starsky Owen Realty.</p>
        <span class="card-arrow">Open</span>
      </a>
    </div>
  </div>
</section>
"""
write("projects/index.html", page("Project Lab", 1, body, active="Projects"))


# ============================================================================
# 2.a Infrastructure project
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("Infrastructure", None)], 2) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.a · Lab</span>
    <h1 class="reveal">Infrastructure work — <em>the real ones.</em></h1>
    <p class="lede reveal">Diagrams, topology views, migration artifacts, and audit outputs from actual environments. Some are client deliverables (redacted where necessary); some are lab work that later became reusable templates.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="stats">
      <div class="stat"><span class="stat-num">838</span><span class="stat-label">VMs · AUS prod cluster</span></div>
      <div class="stat"><span class="stat-num">92</span><span class="stat-label">VMs · DR cluster</span></div>
      <div class="stat"><span class="stat-num">68</span><span class="stat-label">UCS blades audited</span></div>
      <div class="stat"><span class="stat-num">36mo</span><span class="stat-label">OpenShift horizon</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">Active / Recent</span>
    <h2>OpenShift migration program.</h2>
    <p>Production and DR vCenter analysis (RVTools), UCS health audit across 68 blades, Jira-import CSV for modernization backlog, POC runbook targeting the C2-WebSphere-Cluster for Single Node OpenShift, OpenShift working session with Red Hat engineering. Findings surfaced expiring SSL certificates, multipath storage failures, dead boot LUNs, and a critically unhealthy UCS node — all of which shaped the migration wave plan.</p>

    <div class="grid grid-2 mt-3">
      <div class="card"><span class="card-eyebrow">Artifact</span><h3>Infrastructure health reports</h3><p>RVTools-derived reports covering both vCenter environments, host-level drill, storage paths, certificate expiries, boot-LUN status.</p></div>
      <div class="card"><span class="card-eyebrow">Artifact</span><h3>Jira-import CSV</h3><p>Structured backlog for the modernization program — every finding becomes a ticket with priority, workstream, and owner hints.</p></div>
      <div class="card"><span class="card-eyebrow">Artifact</span><h3>POC runbook (SNO)</h3><p>Single Node OpenShift POC on the C2-WebSphere-Cluster target — prerequisites, sequence, rollback posture.</p></div>
      <div class="card"><span class="card-eyebrow">Artifact</span><h3>Migration wave plan</h3><p>24–36 month horizon, workload-class banding, dependency sequencing.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">Prior environments</span>
    <h2>Representative work, documented.</h2>
    <div class="grid grid-2 mt-3">
      <div class="card"><span class="card-eyebrow">Datacenter / Virtualization</span><h3>TX Datacenter &amp; Virtual Environment</h3><p>Core-stack, managed router, firewall, VoIP, HP Indigo systems, virtual infra — documented in a single reference.</p></div>
      <div class="card"><span class="card-eyebrow">Multi-Site Enterprise</span><h3>TX / CA / LAX Site Architecture</h3><p>Regional sites, datacenters, branch presence, cross-site workflow dependencies.</p></div>
      <div class="card"><span class="card-eyebrow">Healthcare</span><h3>Harbor Health Multi-Clinic Footprint</h3><p>Standardized site topology — clinics, call center, HQ, mobile units.</p></div>
      <div class="card"><span class="card-eyebrow">Hybrid / Migration</span><h3>Support &amp; Migration Reference</h3><p>On-prem to virtual to cloud gateway, backup flows, migration-readiness mapping.</p></div>
      <div class="card"><span class="card-eyebrow">Workflow Automation</span><h3>MFA Print &amp; Onyx VPS Pipeline</h3><p>Downloaders, RIP stations, forwarding, packing slips, Zund cut-queue integration.</p></div>
      <div class="card"><span class="card-eyebrow">Physical Security</span><h3>Facility Access Control</h3><p>Entry points, control-board hubs, readers, locking mechanisms for secure ops handoff.</p></div>
    </div>
    <div class="scaffold mt-4">
      <div class="scaffold-label">Asset migration</div>
      <p>Copy infrastructure diagrams from the existing site's <code>/assets/infra/</code> folder into <code>/assets/images/infra/</code> in this repo, then replace placeholders with <code>&lt;img&gt;</code> tags. All diagrams are preserved in the v1 repo under <code>jeremiah9980.github.io/jeremiah9980/assets/infra/</code>.</p>
    </div>
  </div>
</section>
"""
write("projects/infrastructure/index.html", page("Infrastructure Projects", 2, body, active="Projects"))


# ============================================================================
# 2.b DevOps / Cloud project
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("DevOps / Cloud", None)], 2) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.b · Lab</span>
    <h1 class="reveal">DevOps and cloud — <em>what's been shipped.</em></h1>
    <p class="lede reveal">Pipelines, IaC, and platform utilities. The artifacts that started as one-off problem solvers and turned into reusable patterns.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-2">
      <div class="card">
        <span class="card-eyebrow">React · In production</span>
        <h3>GitHub Repo Utility Inventory</h3>
        <p>Enterprise repo hygiene tool — scoring, tagging, CSV export. Built to give platform leads a current view of what's alive, what's rotting, what's worth migration effort. React artifact with filtering and export.</p>
      </div>
      <div class="card">
        <span class="card-eyebrow">Skill-creator · Work in progress</span>
        <h3>Document Refinement Skill</h3>
        <p>An authoring skill for systematic document refinement, initiated via <code>/skill-creator</code>. Unfinished — parked pending completion of two prior skills it depends on.</p>
      </div>
      <div class="card">
        <span class="card-eyebrow">Ansible &amp; Terraform</span>
        <h3>Enterprise IaC patterns</h3>
        <p>Module structure, state discipline, environment promotion, secrets handling. The boring patterns that make the difference between IaC that survives and IaC that gets abandoned after one team rotation.</p>
      </div>
      <div class="card">
        <span class="card-eyebrow">CI/CD</span>
        <h3>Delivery pipelines</h3>
        <p>Gates, approvals, rollback posture, deployment observability. Pipelines audited for who can push what and prove it.</p>
      </div>
    </div>
    <div class="scaffold mt-4">
      <div class="scaffold-label">Scaffold</div>
      <p>Expand each card into a full sub-page with: problem statement, approach, code snippets (or link to repo), outcome, and a "what I'd change next time" section. Priority order: Repo Utility Inventory first (it has the most material), IaC patterns second, CI/CD third.</p>
    </div>
  </div>
</section>
"""
write("projects/devops-cloud/index.html", page("DevOps / Cloud Projects", 2, body, active="Projects"))


# ============================================================================
# 2.c AI project
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("AI", None)], 2) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.c · Lab</span>
    <h1 class="reveal">AI work, <em>integrated where it matters.</em></h1>
    <p class="lede reveal">Not demos for their own sake. AI work where the integration saves a human actual time or produces something a human couldn't produce in the same budget.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-2">
      <div class="card">
        <span class="card-eyebrow">Live demo</span>
        <h3>AI Platform Assistant</h3>
        <p>A running demo of an agent-style assistant for platform engineering workflows — runbook lookup, ticket triage, decision support. Built on the Anthropic API.</p>
        <div class="btn-cluster">
          <a class="btn btn-ghost" href="https://jeremiah9980.github.io/jeremiah9980/projects/ai-platform-assistant-live-demo.html">Open v1 demo</a>
        </div>
      </div>
      <div class="card">
        <span class="card-eyebrow">Multi-model pattern</span>
        <h3>Neutral analysis via consensus</h3>
        <p>The pattern underpinning the Conflict Collection platform: send the same event through multiple AI platforms (Claude, GPT, Gemini) and surface where they agree and diverge. "Neutral" is an emergent property, not a model setting.</p>
      </div>
      <div class="card">
        <span class="card-eyebrow">Productivity integration</span>
        <h3>Claude API into internal tooling</h3>
        <p>Integrating Claude into document refinement, technical review, and reporting workflows. The real value is in the boring integration points, not the flashy ones.</p>
      </div>
      <div class="card">
        <span class="card-eyebrow">Skill authoring</span>
        <h3>Custom skills &amp; agent patterns</h3>
        <p>Exploration of reusable skill authoring (via <code>/skill-creator</code>) and agent-composition patterns for domain-specific tooling.</p>
      </div>
    </div>
  </div>
</section>
"""
write("projects/ai/index.html", page("AI Projects", 2, body, active="Projects"))


# ============================================================================
# 2.d GameChanger (scaffold — needs user brief)
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("Video / GameChanger", None)], 2) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.d · Lab · Scaffold</span>
    <h1 class="reveal">Video Project / GameChanger.</h1>
    <p class="lede reveal">Video-production workflow tooling and the GameChanger project. Adjacent to the OBS/streaming workflows already in active use.</p>
  </div>
</section>

<section class="tight">
  <div class="container narrow">
    <div class="scaffold">
      <div class="scaffold-label">Needs brief</div>
      <p>This page is scaffolded but not populated. To fill it in, answer:</p>
      <ol>
        <li><strong>What is GameChanger?</strong> One-sentence definition.</li>
        <li><strong>What problem does it solve?</strong> Who feels the pain today?</li>
        <li><strong>Stage?</strong> Concept · prototype · live · productized.</li>
        <li><strong>Assets?</strong> Demo video, screenshots, repo link, deck.</li>
        <li><strong>Relationship to OBS/streaming?</strong> Is this the same project, a related project, or separate?</li>
      </ol>
      <p>Reply with the brief and this page becomes a proper project page on the next pass.</p>
    </div>

    <h2 class="mt-4">Related active work</h2>
    <p>OBS/streaming workflow tooling and home-network monitoring are ongoing. If GameChanger sits inside that thread, it'll thread in here; if it's a separate product, it gets its own page under this node.</p>
  </div>
</section>
"""
write("projects/gamechanger/index.html", page("Video Project / GameChanger", 2, body, active="Projects"))


# ============================================================================
# 2.e CONFLICT COLLECTION — flagship, detailed
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("Conflict Collection", None)], 2) + """
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow eyebrow-rule reveal">2.e · Flagship Project</span>
        <h1 class="reveal">Conflict Collection &amp; <em>Neutral Analysis Platform.</em></h1>
        <p class="lede reveal">Ingest text threads, emails, screenshots, and notes. Normalize into conflict events. Run each event through multiple AI models. Surface the consensus and the disagreement. Build court-ready exhibits with a documented provenance chain. Targeted at co-parents, family-law attorneys, and mediators.</p>
      </div>
      <div class="dossier reveal">
        <dl>
          <dt>Stage</dt><dd>In development</dd>
          <dt>Users</dt><dd>Co-parents · Attorneys · Mediators</dd>
          <dt>Differentiator</dt><dd>Multi-model consensus = neutral</dd>
          <dt>Output</dt><dd>Timeline · Dashboard · Exhibit packet</dd>
          <dt>Eventual home</dt><dd>Dedicated subdomain / product</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="callout">
      <div class="callout-label">Why this exists</div>
      <p>Conflict documentation in family-law contexts is fragmented across text threads, email, screenshots, voicemail transcripts, calendar entries, and people's memories. Legal exhibit work requires clean timelines, neutral framing, and verifiable provenance. Doing that manually is expensive — and lawyers bill for it. Doing it with a single AI model invites accusations of bias. Doing it with <em>multiple</em> models and surfacing their agreement gives the neutrality a structural basis rather than a vendor claim.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">Workflow</span>
    <h2>Six stages, one through-line.</h2>
    <ol class="process">
      <li>
        <h4>Ingest</h4>
        <p>Accept iMessage/SMS exports, Gmail thread exports, screenshot OCR, manual notes, calendar entries, voicemail transcripts. Each source gets tagged with its provenance — where it came from, when it was collected, whether it's verifiable against the original.</p>
      </li>
      <li>
        <h4>Normalize into conflict events</h4>
        <p>Every piece of ingested content becomes one or more event records: timestamp, parties, channel, content, attachments, tags. This is the canonical object the rest of the system operates on.</p>
      </li>
      <li>
        <h4>Multi-model neutral analysis</h4>
        <p>Each event is run through multiple AI platforms (Claude, GPT, Gemini). Outputs are structured and compared. Where models agree on a characterization — tone, behavior pattern, escalation marker — that's surfaced as consensus. Where they diverge, the divergence itself is shown. Neutral is emergent from the consensus, not asserted by the system.</p>
      </li>
      <li>
        <h4>Dashboard</h4>
        <p>Timeline view, party/relationship view, pattern detection — escalation, stonewalling, frequency shifts, response-time drift. The dashboard is built for a human reviewer (user or attorney) to scan quickly and drill down selectively.</p>
      </li>
      <li>
        <h4>Exhibit builder</h4>
        <p>Export court-ready exhibit packets — numbered, timestamped, redacted where needed, with a documented provenance chain for every item. This is the piece attorneys care about most: exhibits that don't get challenged on foundation.</p>
      </li>
      <li>
        <h4>Case continuity</h4>
        <p>Ongoing ingestion as the conflict continues, with pattern drift reporting over time and re-export of updated exhibit packets.</p>
      </li>
    </ol>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">Data model</span>
    <h2>The conflict event record.</h2>
    <p>Everything the system does operates on a normalized event. Rough shape:</p>
    <pre><code>ConflictEvent {
  id: uuid
  timestamp: iso8601
  parties: [PartyRef]
  channel: enum { sms, imessage, email, screenshot, note, voicemail, calendar }
  source: SourceRef { raw_filename, ingest_timestamp, provenance_chain[] }
  content: {
    raw_text: string
    attachments: [AttachmentRef]
  }
  tags: [string]
  analyses: [
    { model: enum, prompt_version: string, output: structured_json, timestamp: iso8601 }
  ]
  consensus: ConsensusSummary | null
  exhibit_refs: [ExhibitId]
}</code></pre>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow eyebrow-rule">Target users</span>
        <h2>Who's actually using this.</h2>
      </div>
      <div>
        <h3>Co-parents</h3>
        <p>Documenting an ongoing conflict for their own sanity and for future legal readiness. The timeline view and exhibit packets are the primary value.</p>
        <h3 class="mt-3">Family-law attorneys</h3>
        <p>Receiving a clean, neutral-framed conflict record from their client instead of a chaotic drop of screenshots. Court-ready exhibits straight out of the platform.</p>
        <h3 class="mt-3">Mediators</h3>
        <p>Understanding conflict patterns before the session — escalation markers, stonewalling frequency, response-time drift. Structural context without the advocate framing.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <span class="eyebrow eyebrow-rule">Status</span>
    <h2>Where the platform is today.</h2>
    <div class="grid grid-3">
      <div class="card"><span class="card-eyebrow">Done</span><h3>Ingest prototype</h3><p>Working prototype for iMessage/SMS and Gmail thread ingestion with provenance capture. Proven against a real case corpus.</p></div>
      <div class="card"><span class="card-eyebrow">Done</span><h3>Multi-model consensus prototype</h3><p>Claude + additional model runs against normalized events. Structured output comparison working.</p></div>
      <div class="card"><span class="card-eyebrow">In progress</span><h3>Dashboard &amp; exhibit builder</h3><p>Web UI for timeline, dashboard, exhibit packet export. Design and data-layer scoping.</p></div>
      <div class="card"><span class="card-eyebrow">Next</span><h3>Attorney pilot</h3><p>Identify 1–3 family-law attorneys willing to run a live case through the platform. Priority: Austin/Central Texas.</p></div>
      <div class="card"><span class="card-eyebrow">Eventually</span><h3>Productization</h3><p>Own subdomain, SaaS pricing, HIPAA-adjacent data handling posture, expanded channel support.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container narrow tc">
    <h2>Interested in the attorney pilot?</h2>
    <p>If you practice family law in Central Texas and would consider running one case through the platform as a pilot, I'd like to hear from you.</p>
    <div class="btn-cluster" style="justify-content:center">
      <a class="btn" href="mailto:jeremiah@cargillco.example">Contact about pilot</a>
      <a class="btn btn-ghost" href="../">Back to projects</a>
    </div>
  </div>
</section>
"""
write("projects/conflict-collection/index.html", page("Conflict Collection &amp; Neutral Analysis Platform", 2, body, active="Projects",
                                                    description="A platform for ingesting, normalizing, and neutrally analyzing conflict documentation across multiple AI models. For co-parents, family-law attorneys, and mediators."))


# ============================================================================
# 2.f GPS hub
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("GPS", None)], 2) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.f · Lab</span>
    <h1 class="reveal">GPS — <em>timeline and live tracker.</em></h1>
    <p class="lede reveal">Two complementary location tools. Timeline Builder reconstructs location history into a reviewable record; Live Tracker surfaces real-time position. Both are useful on their own and both can feed the Conflict Collection platform as evidence sources.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-2">
      <a href="timeline/" class="card">
        <span class="card-eyebrow">2.f.1</span>
        <h3>Timeline Builder</h3>
        <p>Reconstruct location history from multiple sources into a single reviewable timeline. Useful as a standalone record and as an evidence source for conflict documentation.</p>
        <span class="card-arrow">Open</span>
      </a>
      <a href="live/" class="card">
        <span class="card-eyebrow">2.f.2</span>
        <h3>Live Tracker</h3>
        <p>Real-time location view for personal, family, or fleet use. Designed to be simple, private, and honest about battery and signal realities.</p>
        <span class="card-arrow">Open</span>
      </a>
    </div>
  </div>
</section>
"""
write("projects/gps/index.html", page("GPS Projects", 2, body, active="Projects"))


# ============================================================================
# 2.f.1 Timeline Builder
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("GPS", "projects/gps/"), ("Timeline Builder", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.f.1 · Lab</span>
    <h1 class="reveal">GPS Timeline Builder.</h1>
    <p class="lede reveal">Take multiple location-history sources and build one coherent, reviewable timeline. Export a clean record for personal use, or feed events into the Conflict Collection platform as a corroborating evidence layer.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-2">
      <div class="card"><span class="card-eyebrow">Sources</span><h3>What it ingests</h3><p>Google Timeline exports, Apple Significant Locations, third-party tracker logs, manual check-ins. Each gets tagged with source provenance.</p></div>
      <div class="card"><span class="card-eyebrow">Normalization</span><h3>One record shape</h3><p>Every source becomes a time-stamped point with lat/lon, accuracy, source label, and provenance hash. The rest of the system operates on that shape.</p></div>
      <div class="card"><span class="card-eyebrow">Review UI</span><h3>Scannable timeline</h3><p>Linear time view with map, day summaries, stop detection, and anomaly highlighting.</p></div>
      <div class="card"><span class="card-eyebrow">Interop</span><h3>Feeds Conflict Collection</h3><p>Timeline events can be attached to conflict event records as corroborating evidence with full provenance.</p></div>
    </div>
    <div class="scaffold mt-4">
      <div class="scaffold-label">Scoping note</div>
      <p>Timeline Builder and the Conflict Collection timeline view likely share a React/visualization component. Worth building once and exposing from both. Flag for implementation.</p>
    </div>
  </div>
</section>
"""
write("projects/gps/timeline/index.html", page("GPS Timeline Builder", 3, body, active="Projects"))


# ============================================================================
# 2.f.2 Live Tracker
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("GPS", "projects/gps/"), ("Live Tracker", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.f.2 · Lab</span>
    <h1 class="reveal">GPS Live Tracker.</h1>
    <p class="lede reveal">Real-time location view. Built to be simple and private — the features most consumer trackers skip because they get in the way of the ad business model.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-2">
      <div class="card"><span class="card-eyebrow">Design principle</span><h3>Private by default</h3><p>No ad backend, no data resale, explicit sharing model. Users know where their data is.</p></div>
      <div class="card"><span class="card-eyebrow">Design principle</span><h3>Honest about physics</h3><p>Battery cost, signal dropouts, and location accuracy are surfaced rather than hidden. The UI reflects the reality of the underlying sensors.</p></div>
      <div class="card"><span class="card-eyebrow">Use cases</span><h3>Family · Fleet · Personal security</h3><p>Same core tech, three packaging modes. Family and personal-security modes prioritize simplicity; fleet mode prioritizes history and reporting.</p></div>
      <div class="card"><span class="card-eyebrow">Interop</span><h3>Writes to Timeline Builder</h3><p>Live Tracker's history stream is a first-class ingest source for Timeline Builder.</p></div>
    </div>
    <div class="scaffold mt-4">
      <div class="scaffold-label">Status</div>
      <p>Stage, platform (iOS / Android / web), and deployment model (self-hosted vs. SaaS) still to be decided. Fill in when the decision is made.</p>
    </div>
  </div>
</section>
"""
write("projects/gps/live/index.html", page("GPS Live Tracker", 3, body, active="Projects"))


# ============================================================================
# 2.g Flywheel (scaffold)
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("Flywheel", None)], 2) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.g · Lab · Scaffold</span>
    <h1 class="reveal">Flywheel.</h1>
    <p class="lede reveal">Project placeholder. Scoping in progress.</p>
  </div>
</section>

<section class="tight">
  <div class="container narrow">
    <div class="scaffold">
      <div class="scaffold-label">Needs brief</div>
      <p>No prior context for Flywheel. A one-paragraph brief collapses this into a real page. Questions:</p>
      <ol>
        <li><strong>What is Flywheel?</strong> Is this a business-operations flywheel concept, a content engine, an automation framework, or a productized methodology?</li>
        <li><strong>What problem does it solve, and for whom?</strong></li>
        <li><strong>Stage?</strong> Idea · prototype · live.</li>
        <li><strong>Does it intersect with any of the other projects</strong> (Conflict Collection, GPS, Clients)?</li>
        <li><strong>Assets?</strong> Doc, repo, screenshots.</li>
      </ol>
    </div>
  </div>
</section>
"""
write("projects/flywheel/index.html", page("Flywheel", 2, body, active="Projects"))


# ============================================================================
# 2.h CLIENTS hub
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("Clients", None)], 2) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.h · Case studies</span>
    <h1 class="reveal">Client work, <em>documented and redacted.</em></h1>
    <p class="lede reveal">Four active or recent client engagements. Same case-study template across all of them — engagement, problem, what I built, outcome, artifacts.</p>
  </div>
</section>

<section class="tight">
  <div class="container">
    <div class="grid grid-2">
      <a href="cosmicgen/" class="card">
        <span class="card-eyebrow">2.h.1</span>
        <h3>CosmicGen</h3>
        <p>Client engagement — scoping in progress. See page for brief status.</p>
        <span class="card-arrow">Open case</span>
      </a>
      <a href="teleotitle/" class="card">
        <span class="card-eyebrow">2.h.2 · Title company</span>
        <h3>TeleoTitle</h3>
        <p>DNS &amp; email-authentication hardening, wire-fraud risk reduction, DMARC enforcement. Flagship case for Next-Gen-Security.</p>
        <span class="card-arrow">Open case</span>
      </a>
      <a href="abode-labs/" class="card">
        <span class="card-eyebrow">2.h.3</span>
        <h3>Abode Labs</h3>
        <p>DNS and email authentication, DMARC posture, coordinated with Don. Paired case for Next-Gen-Audit.</p>
        <span class="card-arrow">Open case</span>
      </a>
      <a href="starsky-owen/" class="card">
        <span class="card-eyebrow">2.h.4 · Realty</span>
        <h3>Starsky Owen Realty</h3>
        <p>Real-estate transaction tracker and CSV importer dashboard. Public-records sourcing strategy across Homes.com, Williamson County Clerk, ACTRIS-adjacent feeds.</p>
        <span class="card-arrow">Open case</span>
      </a>
    </div>
  </div>
</section>
"""
write("projects/clients/index.html", page("Client Work", 2, body, active="Projects"))


# ============================================================================
# 2.h.1 CosmicGen (scaffold)
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("Clients", "projects/clients/"), ("CosmicGen", None)], 3) + """
<section class="hero">
  <div class="container narrow">
    <span class="eyebrow eyebrow-rule reveal">2.h.1 · Client · Scaffold</span>
    <h1 class="reveal">CosmicGen.</h1>
  </div>
</section>
<section class="tight">
  <div class="container narrow">
    <div class="scaffold">
      <div class="scaffold-label">Needs brief</div>
      <p>No prior context available for CosmicGen. To turn this into a real case study, provide:</p>
      <ol>
        <li>Industry and size of the client</li>
        <li>What the engagement was (audit, build, advisory, ongoing operations)</li>
        <li>Problem statement in one paragraph</li>
        <li>What I built / delivered</li>
        <li>Outcome (measurable if possible)</li>
        <li>Any artifacts that can be linked (redacted where needed)</li>
      </ol>
    </div>
  </div>
</section>
"""
write("projects/clients/cosmicgen/index.html", page("CosmicGen — Client", 3, body, active="Projects"))


# ============================================================================
# 2.h.2 TeleoTitle — detailed
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("Clients", "projects/clients/"), ("TeleoTitle", None)], 3) + """
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow eyebrow-rule reveal">2.h.2 · Client Case</span>
        <h1 class="reveal">TeleoTitle — <em>wire-fraud window, closed.</em></h1>
        <p class="lede reveal">Title company with a wide-open email-authentication posture on <code>teleotitle.com</code>. Engagement produced a DNS runbook, DMARC enforcement plan, and wire-fraud-specific playbook. Flagship case for the Next-Gen-Security packaged offer.</p>
      </div>
      <div class="dossier reveal">
        <dl>
          <dt>Industry</dt><dd>Title insurance</dd>
          <dt>Contact</dt><dd>Don</dd>
          <dt>Engagement</dt><dd>Fixed-scope security &amp; DNS hardening</dd>
          <dt>Deliverable</dt><dd>DNS runbook + remediation plan</dd>
          <dt>Maps to</dt><dd>Next-Gen-Security · Next-Gen-Audit</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <span class="eyebrow eyebrow-rule">Problem</span>
    <h2>A title company is a wire-fraud target by default.</h2>
    <p>Title firms move large wires routinely. If the sending domain's email authentication is weak — no SPF, permissive DMARC, DKIM missing — impersonation and wire-redirect attacks become trivially easy. On arrival, <code>teleotitle.com</code>'s posture had gaps typical of a small firm whose IT vendor had never been asked to think about email authentication.</p>

    <h2 class="mt-4">What I built</h2>
    <ul>
      <li>Current-state assessment of <code>teleotitle.com</code> DNS, including SPF, DKIM, DMARC, and look-alike domain exposure</li>
      <li>Copy-pasteable remediation runbook with exact DNS records to publish</li>
      <li>DMARC enforcement plan with a phased posture — <code>p=none</code> with reporting, then <code>p=quarantine</code>, then <code>p=reject</code></li>
      <li>Wire-verification protocol (out-of-band callback, signed staff playbook)</li>
      <li>Incident playbook for the "suspected fraud in progress" moment</li>
    </ul>

    <h2 class="mt-4">Outcome</h2>
    <p>Email authentication posture moved from permissive to enforced. Wire verification became a process rather than a courtesy. The runbook is now living documentation — when DNS drift happens, it's detectable; when staff turn over, the process doesn't leave with them.</p>

    <div class="callout mt-4">
      <div class="callout-label">Cross-link</div>
      <p>This case is the working prototype for <a href="../../../professional/next-gen-it/security/">Next-Gen-Security</a>. Firms with a similar posture should look at that offer first.</p>
    </div>
  </div>
</section>
"""
write("projects/clients/teleotitle/index.html", page("TeleoTitle — Client Case", 3, body, active="Projects"))


# ============================================================================
# 2.h.3 Abode Labs
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("Clients", "projects/clients/"), ("Abode Labs", None)], 3) + """
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow eyebrow-rule reveal">2.h.3 · Client Case</span>
        <h1 class="reveal">Abode Labs — <em>DNS &amp; email authentication.</em></h1>
        <p class="lede reveal">Email authentication hardening and DMARC posture for <code>abodelabs.ai</code>, coordinated with Don. Paired case with TeleoTitle and flagship material for the Next-Gen-Audit offer.</p>
      </div>
      <div class="dossier reveal">
        <dl>
          <dt>Contact</dt><dd>Don</dd>
          <dt>Domain</dt><dd><code>abodelabs.ai</code></dd>
          <dt>Engagement</dt><dd>Fixed-scope DNS hardening</dd>
          <dt>Deliverable</dt><dd>Runbook with DMARC enforcement plan</dd>
          <dt>Maps to</dt><dd>Next-Gen-Audit</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <span class="eyebrow eyebrow-rule">What I built</span>
    <h2>The same rigor, a different threat model.</h2>
    <p>Where TeleoTitle's work was wire-fraud framed, Abode Labs's was brand-protection and impersonation framed. Same underlying discipline — SPF, DKIM, DMARC — delivered in the same runbook shape. The value of doing two at once was in productizing the deliverable: the second one took a fraction of the effort and produced a cleaner artifact.</p>
    <ul>
      <li>DNS assessment and gap inventory</li>
      <li>SPF / DKIM publication</li>
      <li>DMARC phased enforcement</li>
      <li>Monitoring hooks for drift detection</li>
      <li>Human-readable remediation runbook</li>
    </ul>

    <div class="callout mt-4">
      <div class="callout-label">Cross-link</div>
      <p>This case and TeleoTitle together are the proof material for the <a href="../../../professional/next-gen-it/audit/">Next-Gen-Audit</a> offer.</p>
    </div>
  </div>
</section>
"""
write("projects/clients/abode-labs/index.html", page("Abode Labs — Client Case", 3, body, active="Projects"))


# ============================================================================
# 2.h.4 Starsky Owen Realty
# ============================================================================
body = """
""" + breadcrumbs([("Home", ""), ("Projects", "projects/"), ("Clients", "projects/clients/"), ("Starsky Owen Realty", None)], 3) + """
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow eyebrow-rule reveal">2.h.4 · Client Case</span>
        <h1 class="reveal">Starsky Owen Realty — <em>transaction tracker &amp; data dashboard.</em></h1>
        <p class="lede reveal">Built a real-estate transaction tracker and CSV-importer dashboard for the Starsky Owen team covering the Round Rock / Georgetown, TX corridor. Sourcing strategy pulls from Homes.com, Williamson County Clerk deed records, and ACTRIS-adjacent public feeds.</p>
      </div>
      <div class="dossier reveal">
        <dl>
          <dt>Market</dt><dd>Round Rock · Georgetown, TX</dd>
          <dt>Engagement</dt><dd>Custom tool build + data strategy</dd>
          <dt>Deliverables</dt><dd>Dashboard · CSV importer · sourcing playbook</dd>
          <dt>Sources</dt><dd>Homes.com · Williamson County Clerk · ACTRIS-adjacent</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="container">
    <span class="eyebrow eyebrow-rule">What I built</span>
    <h2>A tracker that respects where the data actually comes from.</h2>
    <p>Most realty tools ingest one feed and call it a day. Real comp work in a Central Texas corridor requires triangulating across multiple public and semi-public sources, each with different access models, different refresh cadences, and different reliability profiles. The build covered:</p>
    <ul>
      <li>Transaction tracker with filtering, segmentation, and export</li>
      <li>CSV importer that handles the messy reality of public deed exports</li>
      <li>Data-sourcing playbook documenting where each feed lives, its access model, and its known limitations</li>
      <li>Williamson County Clerk deed integration for post-close verification</li>
      <li>ACTRIS-adjacent sourcing pattern for listing-side context</li>
    </ul>

    <h2 class="mt-4">Outcome</h2>
    <p>The Starsky Owen team has a single dashboard instead of three browser tabs and a spreadsheet. New transactions get captured on a cadence rather than retroactively. The sourcing playbook is living documentation — if a feed changes terms or format, the team knows what to swap in.</p>
  </div>
</section>
"""
write("projects/clients/starsky-owen/index.html", page("Starsky Owen Realty — Client Case", 3, body, active="Projects"))


print("\n=== All pages written ===")
