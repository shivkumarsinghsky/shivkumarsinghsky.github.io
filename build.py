"""Builds index.html from the project list below. Run: python3 build.py"""
import datetime
import html
import json
import math

GH = "https://github.com/shivkumarsinghsky"
SITE = "https://shivkumarsinghsky.github.io/"
HANDLE = "shivkumarsinghsky"
EMAIL = "shivkumarsky01@gmail.com"
SOCIAL = [
    ("GitHub", GH,
     '<path fill="currentColor" d="M12 .5C5.65.5.5 5.65.5 12c0 5.09 3.29 9.4 7.86 10.93.58.1.79-.25.79-.56v-1.97c-3.2.7-3.87-1.37-3.87-1.37-.52-1.33-1.28-1.69-1.28-1.69-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.28 1.19-3.09-.12-.29-.52-1.46.11-3.04 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.58.23 2.75.11 3.04.74.81 1.19 1.83 1.19 3.09 0 4.42-2.69 5.39-5.26 5.68.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5Z"/>'),
    ("LinkedIn", f"https://www.linkedin.com/in/{HANDLE}/",
     '<rect x="1.5" y="1.5" width="21" height="21" rx="4" fill="currentColor"/><g fill="var(--icon-cut)"><rect x="5.5" y="9.5" width="3" height="9"/><circle cx="7" cy="6.6" r="1.8"/><path d="M10.6 9.5h2.9v1.3c.5-.9 1.6-1.5 2.9-1.5 2.4 0 3.1 1.5 3.1 3.8v5.4h-3v-4.8c0-1.1-.3-1.8-1.3-1.8-1.1 0-1.6.8-1.6 1.9v4.7h-3z"/></g>'),
    ("Instagram", f"https://www.instagram.com/{HANDLE}/",
     '<rect x="2.5" y="2.5" width="19" height="19" rx="5.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.4" cy="6.6" r="1.3" fill="currentColor"/>'),
    ("Email", f"mailto:{EMAIL}",
     '<rect x="2" y="4.5" width="20" height="15" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="m3 6.5 9 6.5 9-6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>'),
]

TITLE = "Shiv Kumar — Software Architect | Distributed Systems, EAM & Enterprise AI"
DESC = ("Shiv Kumar is a Software Architect and Senior Software Engineer in Noida, India, with 12+ years "
        "designing enterprise platforms, distributed systems, event-driven microservices, EAM/FSM and AI applications.")

DOMAINS = [
    {"id": "architecture", "name": "Architecture & distributed systems", "short": ["Architecture &", "distributed systems"],
     "color": "#3E63DD", "dark": "#7C9BFF",
     "line": "How large systems are shaped: patterns, events, tenancy and trade-offs.",
     "repos": [
        ("system-design-architecture", "Twelve reference system designs with capacity models, ADRs and diagrams: video, messaging, feeds, job portal, e-commerce, multi-tenant SaaS and enterprise AI.", ["system design", "capacity planning", "ADRs"]),
        ("microservices-patterns", "A catalogue of 17 microservices patterns with TypeScript implementations: saga, outbox, CQRS, event sourcing, circuit breaker, bulkhead and idempotency.", ["microservices", "saga", "CQRS"]),
        ("event-driven-platform", "Three services that talk only through RabbitMQ events, with a transactional outbox, idempotent consumers, retries and dead-letter queues.", ["RabbitMQ", "outbox", "TypeScript"]),
        ("enterprise-saas-platform", "Multi-tenant SaaS foundations: PostgreSQL row-level security, tenant-aware auth, RBAC, entitlements, audit logs and rate limits.", ["multi-tenant", "row-level security", "RBAC"]),
     ]},
    {"id": "eam", "name": "EAM & real-time systems", "short": ["EAM &", "real-time systems"],
     "color": "#0E9F8E", "dark": "#3FD1BE",
     "line": "Asset-heavy operations: work orders, maintenance and live telemetry.",
     "repos": [
        ("eam-platform-architecture", "Enterprise Asset Management reference architecture: work-order lifecycle, preventive and predictive maintenance, asset hierarchy, field service and maintenance KPIs.", ["EAM", "FSM", "domain-driven design"]),
        ("realtime-monitoring-platform", "MQTT ingestion, Redis Streams or Kafka, alerting with hysteresis, PostgreSQL time series and a live WebSocket dashboard.", ["MQTT", "Kafka", "IoT telemetry"]),
     ]},
    {"id": "ai", "name": "Generative & agentic AI", "short": ["Generative &", "agentic AI"],
     "color": "#8E4EC6", "dark": "#C08CF0",
     "line": "LLM systems that cite their sources, respect permissions and ask before acting.",
     "repos": [
        ("rag-enterprise-assistant", "Retrieval-augmented generation over company documents: hybrid vector and BM25 search, pgvector, access-controlled retrieval, citations, guardrails and evaluation.", ["RAG", "pgvector", "LLM evaluation"]),
        ("enterprise-ai-agent-platform", "LangGraph agents with authorised tool calling, RAG, memory, human-in-the-loop approvals, structured outputs and tracing.", ["LangGraph", "AI agents", "human-in-the-loop"]),
     ]},
    {"id": "system-design", "name": "Large-scale system design", "short": ["Large-scale", "system design"],
     "color": "#D9821E", "dark": "#F2AE57",
     "line": "Well-known product problems worked through end to end, with runnable prototypes.",
     "repos": [
        ("realtime-messaging-platform", "Chat at scale: WebSocket gateways, per-conversation ordering, delivery and read receipts, presence and idempotent sends.", ["WebSockets", "chat", "presence"]),
        ("video-streaming-platform", "Video sharing: resumable uploads, a transcoding pipeline, HLS adaptive streaming, CDN delivery and sharded counters.", ["video streaming", "HLS", "CDN"]),
        ("social-media-platform", "News feeds: fan-out on write, on read and hybrid, with a simulation that measures the trade-off.", ["news feed", "fan-out", "caching"]),
        ("job-portal-platform", "Job search with filters and facets, explainable candidate matching and an idempotent application workflow.", ["search", "BM25", "matching"]),
     ]},
    {"id": "tooling", "name": "Developer tooling & machine learning", "short": ["Tooling &", "machine learning"],
     "color": "#DC4A4F", "dark": "#FF8589",
     "line": "Tools that remove boilerplate, and machine learning from first principles.",
     "repos": [
        ("zynkoh-cli", "A code generator for Clean Architecture FastAPI modules: tenant-scoped repositories, CRUD with safe filtering, and end-to-end tested output.", ["code generator", "FastAPI", "clean architecture"]),
        ("learnix", "Linear regression, loss functions and gradient descent in pure Python, checked against least squares and scikit-learn.", ["machine learning", "gradient descent", "Python"]),
     ]},
]

TOOLBOX = [
    ("Architecture", ["Solution & enterprise architecture", "Microservices", "Event-driven systems", "Multi-tenant SaaS", "API design", "High availability"]),
    ("Backend", ["Node.js & TypeScript", ".NET & C#", "Python & FastAPI", "Express.js", "REST APIs"]),
    ("Frontend", ["Angular", "React", "TypeScript", "HTML5 & CSS3", "Responsive web apps"]),
    ("Data & messaging", ["PostgreSQL", "SQL Server", "MongoDB", "Redis", "Kafka", "RabbitMQ", "MQTT"]),
    ("Cloud & delivery", ["AWS", "Microsoft Azure", "Docker", "Kubernetes", "CI/CD", "Observability"]),
    ("AI", ["LLM applications", "RAG", "Agentic AI", "LangChain", "LangGraph"]),
]

e = html.escape


def diagram() -> str:
    cx, cy, r = 300, 250, 175
    nodes, edges = [], []
    for i, d in enumerate(DOMAINS):
        angle = math.radians(-90 + i * 72)
        x, y = cx + r * math.cos(angle), cy + r * math.sin(angle)
        n = len(d["repos"])
        edges.append(
            f'<line class="edge" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" '
            f'style="--c:{d["dark"]};--d:{i * 120}ms"/>')
        label = "".join(
            f'<tspan x="{x:.1f}" dy="{0 if j == 0 else 17}">{e(t)}</tspan>' for j, t in enumerate(d["short"]))
        nodes.append(
            f'<a class="node" href="#{d["id"]}" style="--c:{d["dark"]}" '
            f'aria-label="{e(d["name"])}: {n} projects">'
            f'<rect x="{x - 78:.1f}" y="{y - 34:.1f}" width="156" height="68" rx="12"/>'
            f'<text class="node-label" x="{x:.1f}" y="{y - 8:.1f}">{label}</text>'
            f'<text class="node-count" x="{x:.1f}" y="{y + 24:.1f}">{n} projects</text></a>')
    hub = (f'<g class="hub"><circle cx="{cx}" cy="{cy}" r="58"/>'
           f'<text x="{cx}" y="{cy - 4}">Shiv</text><text x="{cx}" y="{cy + 18}">Kumar</text></g>')
    return (f'<svg class="system" viewBox="30 30 540 410" role="img" '
            f'aria-labelledby="sys-title"><title id="sys-title">Shiv Kumar\'s work, drawn as a system: '
            f'five practice areas connected to one hub</title>{"".join(edges)}{hub}{"".join(nodes)}</svg>')


def area_list() -> str:
    return "".join(
        f'<li><a href="#{d["id"]}" style="--c:{d["dark"]}">{e(d["name"])}<span>{len(d["repos"])} projects</span></a></li>'
        for d in DOMAINS)


def social_links() -> str:
    return "".join(
        f'<li><a href="{url}" rel="me noopener" aria-label="{label}: {EMAIL if label == "Email" else HANDLE}" title="{EMAIL if label == "Email" else label}">'
        f'<svg viewBox="0 0 24 24" aria-hidden="true">{icon}</svg></a></li>'
        for label, url, icon in SOCIAL)


def footer_links() -> str:
    return "".join(
        f'<li><a href="{url}" rel="me noopener">{EMAIL if label == "Email" else label}</a></li>'
        for label, url, _ in SOCIAL)


def projects() -> str:
    out = []
    for d in DOMAINS:
        rows = []
        for name, desc, tags in d["repos"]:
            tag_html = "".join(f"<li>{e(t)}</li>" for t in tags)
            rows.append(f'''<li class="project">
            <h4><a href="{GH}/{name}">{e(name)}</a></h4>
            <p>{e(desc)}</p>
            <ul class="tags">{tag_html}</ul>
          </li>''')
        out.append(f'''<section class="domain" id="{d["id"]}" style="--c:{d["color"]};--c-dark:{d["dark"]}" aria-labelledby="{d["id"]}-title">
        <header class="domain-head">
          <h3 id="{d["id"]}-title">{e(d["name"])}</h3>
          <p>{e(d["line"])}</p>
        </header>
        <ul class="project-list">
          {"".join(rows)}
        </ul>
      </section>''')
    return "\n      ".join(out)


def toolbox() -> str:
    cols = []
    for title, items in TOOLBOX:
        li = "".join(f"<li>{e(x)}</li>" for x in items)
        cols.append(f'<div class="tool-col"><h3>{e(title)}</h3><ul>{li}</ul></div>')
    return "".join(cols)


person = {
    "@context": "https://schema.org", "@type": "Person", "name": "Shiv Kumar", "url": SITE,
    "image": "https://github.com/shivkumarsinghsky.png", "jobTitle": "Software Architect", "description": DESC,
    "worksFor": {"@type": "Organization", "name": "Agelix Consulting Pvt Ltd"},
    "address": {"@type": "PostalAddress", "addressLocality": "Noida", "addressRegion": "Uttar Pradesh", "addressCountry": "IN"},
    "email": f"mailto:{EMAIL}",
    "sameAs": [url for label, url, _ in SOCIAL if label != "Email"],
    "knowsAbout": ["Software Architecture", "System Design", "Distributed Systems", "Microservices",
                   "Event-Driven Architecture", "Multi-Tenant SaaS", "Enterprise Asset Management",
                   "Field Service Management", "Real-Time Monitoring", "Retrieval-Augmented Generation",
                   "Agentic AI", "LangGraph", "Python", "TypeScript", "Node.js", ".NET", "Angular", "React", "PostgreSQL",
                   "Kafka", "RabbitMQ", "Redis", "Docker", "Kubernetes", "AWS", "Azure"],
}
website = {"@context": "https://schema.org", "@type": "WebSite", "name": "Shiv Kumar", "url": SITE}
total = sum(len(d["repos"]) for d in DOMAINS)

page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(TITLE)}</title>
  <meta name="description" content="{e(DESC)}">
  <meta name="author" content="Shiv Kumar">
  <meta name="keywords" content="Shiv Kumar, Shiv Kumar Software Architect, shivkumarsinghsky, software architect Noida, system design, distributed systems, microservices, event-driven architecture, EAM, enterprise asset management, multi-tenant SaaS, RAG, agentic AI, Angular, React">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#0E1A2B">
  <link rel="canonical" href="{SITE}">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{e(TITLE)}">
  <meta property="og:description" content="{e(DESC)}">
  <meta property="og:url" content="{SITE}">
  <meta property="og:image" content="https://github.com/shivkumarsinghsky.png">
  <meta property="profile:first_name" content="Shiv">
  <meta property="profile:last_name" content="Kumar">
  <meta property="profile:username" content="shivkumarsinghsky">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{e(TITLE)}">
  <meta name="twitter:description" content="{e(DESC)}">
  <meta name="google-site-verification" content="begIPexJ4iL4L013LY68inSfXbKtdqc1ZE48pyYNEzM">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230E1A2B'/%3E%3Ctext x='16' y='22' font-family='Arial' font-weight='700' font-size='15' fill='%23fff' text-anchor='middle'%3ESK%3C/text%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>
  <script type="application/ld+json">{json.dumps(website)}</script>
  <style>
    :root {{
      --ink: #0E1A2B; --ink-2: #16263D; --ink-line: #2A3D5A; --on-ink: #EEF2F8; --on-ink-muted: #A9B6C9;
      --paper: #F5F7FA; --surface: #FFFFFF; --text: #142033; --muted: #556275; --rule: #DDE3EB;
      --display: "Archivo", "Arial Narrow", Arial, sans-serif;
      --body: "IBM Plex Sans", -apple-system, "Segoe UI", Roboto, sans-serif;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{ --paper: #0B1524; --surface: #111F33; --text: #E6ECF4; --muted: #9AA8BC; --rule: #233650; }}
      .domain {{ --c: var(--c-dark) !important; }}
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{ margin: 0; background: var(--paper); color: var(--text); font: 17px/1.6 var(--body); }}
    a {{ color: inherit; }}
    a:focus-visible {{ outline: 3px solid #F2AE57; outline-offset: 3px; border-radius: 4px; }}
    .wrap {{ max-width: 1120px; margin: 0 auto; padding-left: 24px; padding-right: 24px; }}

    /* Hero */
    .hero {{ background: var(--ink); color: var(--on-ink); overflow: hidden; }}
    .hero-grid {{ display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr); gap: 32px;
      align-items: center; padding-top: 72px; padding-bottom: 64px; }}
    .identity {{ display: flex; align-items: center; gap: 14px; margin-bottom: 28px; }}
    .identity img {{ width: 56px; height: 56px; border-radius: 50%; border: 2px solid var(--ink-line); background: var(--ink-2); }}
    .identity p {{ margin: 0; color: var(--on-ink-muted); font-size: 0.95rem; line-height: 1.4; }}
    h1 {{ font-family: var(--display); font-weight: 800; font-size: clamp(2.8rem, 7vw, 5rem);
      line-height: 0.95; letter-spacing: -0.02em; margin: 0 0 18px; }}
    .role {{ font-family: var(--display); font-stretch: 100%; font-weight: 500; font-size: clamp(1.15rem, 2.2vw, 1.45rem);
      color: var(--on-ink); margin: 0 0 20px; }}
    .lead {{ color: var(--on-ink-muted); max-width: 34em; margin: 0 0 32px; font-size: 1.05rem; }}
    .actions {{ display: flex; flex-wrap: wrap; gap: 12px; }}
    .btn {{ display: inline-flex; align-items: center; gap: 10px; padding: 12px 20px; border-radius: 10px;
      font-weight: 600; text-decoration: none; font-size: 0.98rem; }}
    .btn-primary {{ background: var(--on-ink); color: var(--ink); }}
    .btn-primary:hover {{ background: #FFFFFF; }}
    .btn-ghost {{ border: 1px solid var(--ink-line); color: var(--on-ink); }}
    .btn-ghost:hover {{ border-color: var(--on-ink-muted); }}
    .btn svg {{ width: 18px; height: 18px; }}
    .social {{ display: flex; align-items: center; gap: 14px; margin-top: 28px; color: var(--on-ink-muted); font-size: 0.95rem; }}
    .social ul {{ display: flex; gap: 8px; list-style: none; margin: 0; padding: 0; }}
    .social a {{ --icon-cut: var(--ink); display: grid; place-items: center; width: 40px; height: 40px; border-radius: 10px;
      color: var(--on-ink); border: 1px solid var(--ink-line); }}
    .social a:hover {{ border-color: var(--on-ink-muted); background: var(--ink-2); --icon-cut: var(--ink-2); }}
    .social svg {{ width: 20px; height: 20px; }}
    .footer-links {{ display: flex; flex-wrap: wrap; gap: 18px; list-style: none; margin: 0; padding: 0; }}

    /* System diagram */
    .system {{ width: 100%; height: auto; max-width: 580px; justify-self: end; }}
    .area-list {{ display: none; }}
    .edge {{ stroke: var(--c); stroke-width: 2; stroke-dasharray: 6 6; opacity: 0.85;
      animation: draw 900ms ease-out var(--d) both; }}
    @keyframes draw {{ from {{ stroke-dashoffset: 180; opacity: 0; }} to {{ stroke-dashoffset: 0; opacity: 0.85; }} }}
    .hub circle {{ fill: var(--on-ink); }}
    .hub text {{ fill: var(--ink); font-family: var(--display); font-stretch: 112%; font-weight: 800; font-size: 19px; text-anchor: middle; }}
    .node rect {{ fill: var(--ink-2); stroke: var(--c); stroke-width: 2; transition: fill 160ms ease; }}
    .node text {{ text-anchor: middle; }}
    .node-label {{ fill: var(--on-ink); font-family: var(--body); font-weight: 600; font-size: 14px; }}
    .node-count {{ fill: var(--c); font-family: var(--body); font-weight: 500; font-size: 12.5px; }}
    .node:hover rect, .node:focus-visible rect {{ fill: #1E3250; }}
    .node:focus-visible {{ outline: none; }}
    .node:focus-visible rect {{ stroke-width: 3.5; }}

    /* Sections */
    main section.block {{ padding: 72px 0 8px; }}
    h2 {{ font-family: var(--display); font-stretch: 112%; font-weight: 750; font-size: clamp(1.7rem, 3.4vw, 2.3rem);
      letter-spacing: -0.01em; line-height: 1.1; margin: 0 0 12px; }}
    .section-intro {{ color: var(--muted); max-width: 40em; margin: 0 0 40px; }}

    .domain {{ display: grid; grid-template-columns: 300px minmax(0, 1fr); gap: 40px; padding: 36px 0;
      border-top: 1px solid var(--rule); scroll-margin-top: 24px; }}
    .domain-head {{ border-left: 4px solid var(--c); padding-left: 18px; align-self: start; position: sticky; top: 24px; }}
    .domain-head h3 {{ font-family: var(--display); font-stretch: 105%; font-weight: 700; font-size: 1.25rem; line-height: 1.25; margin: 0 0 8px; }}
    .domain-head p {{ margin: 0; color: var(--muted); font-size: 0.97rem; }}
    .project-list {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 28px 36px; }}
    .project h4 {{ font-family: var(--display); font-stretch: 100%; font-weight: 650; font-size: 1.08rem; margin: 0 0 6px; word-break: break-word; }}
    .project h4 a {{ text-decoration: none; background-image: linear-gradient(var(--c), var(--c));
      background-size: 100% 2px; background-position: 0 100%; background-repeat: no-repeat; padding-bottom: 2px; }}
    .project h4 a:hover {{ color: var(--c); }}
    .project p {{ margin: 0 0 12px; color: var(--muted); font-size: 0.96rem; line-height: 1.55; }}
    .tags {{ list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 6px; }}
    .tags li {{ font-size: 0.8rem; font-weight: 500; padding: 2px 10px; border-radius: 999px;
      color: var(--c); background: color-mix(in srgb, var(--c) 12%, transparent); }}

    .toolbox {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 28px; padding: 8px 0 24px; }}
    .tool-col h3 {{ font-family: var(--display); font-stretch: 105%; font-weight: 700; font-size: 1.02rem; margin: 0 0 10px;
      padding-bottom: 10px; border-bottom: 2px solid var(--text); }}
    .tool-col ul {{ list-style: none; margin: 0; padding: 0; }}
    .tool-col li {{ padding: 5px 0; color: var(--muted); font-size: 0.95rem; border-bottom: 1px solid var(--rule); }}

    footer {{ margin-top: 72px; background: var(--ink); color: var(--on-ink-muted); }}
    .footer-row {{ display: flex; justify-content: space-between; flex-wrap: wrap; gap: 16px; padding: 32px 0; font-size: 0.95rem; }}
    .footer-row strong {{ color: var(--on-ink); font-family: var(--display); font-stretch: 112%; }}
    footer a {{ color: var(--on-ink); }}

    @media (max-width: 900px) {{
      .hero-grid {{ grid-template-columns: 1fr; padding-top: 48px; padding-bottom: 40px; }}
      .system {{ justify-self: center; }}
      .domain {{ grid-template-columns: 1fr; gap: 20px; }}
      .domain-head {{ position: static; }}
      .toolbox {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
    }}
    @media (max-width: 600px) {{
      .wrap {{ padding-left: 16px; padding-right: 16px; }}
      .project-list {{ grid-template-columns: 1fr; }}
      .toolbox {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      .system {{ display: none; }}
      .area-list {{ display: grid; gap: 8px; list-style: none; margin: 0; padding: 0; }}
      .area-list a {{ display: flex; justify-content: space-between; gap: 12px; padding: 12px 14px; border-radius: 10px;
        background: var(--ink-2); border-left: 4px solid var(--c); text-decoration: none; font-weight: 600; font-size: 0.95rem; }}
      .area-list span {{ color: var(--c); font-weight: 500; white-space: nowrap; }}
    }}
    @media (prefers-reduced-motion: reduce) {{
      html {{ scroll-behavior: auto; }}
      .edge {{ animation: none; }}
    }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="wrap hero-grid">
      <div>
        <div class="identity">
          <img src="https://github.com/shivkumarsinghsky.png?size=112" alt="" width="56" height="56">
          <p>Noida, Uttar Pradesh, India<br>Agelix Consulting Pvt Ltd</p>
        </div>
        <h1>Shiv Kumar</h1>
        <p class="role">Software Architect and Senior Software Engineer</p>
        <p class="lead">For more than 12 years I have designed and built enterprise platforms, distributed
          systems and real-time solutions: microservices and event-driven systems, multi-tenant SaaS,
          Enterprise Asset Management and field service platforms, and AI applications built on
          retrieval and agents.</p>
        <div class="actions">
          <a class="btn btn-primary" href="{GH}" rel="me"><svg viewBox="0 0 16 16" aria-hidden="true" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>GitHub profile</a>
          <a class="btn btn-ghost" href="#work">See the {total} projects</a>
        </div>
        <div class="social">
          <span>@{HANDLE} on</span>
          <ul aria-label="Social profiles">{social_links()}</ul>
        </div>
      </div>
      {diagram()}
      <ul class="area-list" aria-label="Practice areas">{area_list()}</ul>
    </div>
  </header>

  <main>
    <section class="block" id="work" aria-labelledby="work-title">
      <div class="wrap">
        <h2 id="work-title">Architecture portfolio</h2>
        <p class="section-intro">Open-source reference architectures and implementations. Each repository
          has design documents, architecture decision records, diagrams, tests, Docker and CI.</p>
      {projects()}
      </div>
    </section>

    <section class="block" id="toolbox" aria-labelledby="toolbox-title">
      <div class="wrap">
        <h2 id="toolbox-title">Toolbox</h2>
        <p class="section-intro">The technologies I design with and build on.</p>
        <div class="toolbox">{toolbox()}</div>
      </div>
    </section>
  </main>

  <footer>
    <div class="wrap footer-row">
      <span><strong>Shiv Kumar</strong>, Software Architect</span>
      <ul class="footer-links" aria-label="Social profiles">{footer_links()}</ul>
      <span>© {datetime.date.today().year}</span>
    </div>
  </footer>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as fh:
    fh.write(page)
print(f"index.html written ({len(page)} bytes, {total} projects)")
