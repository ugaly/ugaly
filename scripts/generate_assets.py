"""Generates animated SVG assets for the ugaly profile README.
All SVGs are self-contained (no external fonts/scripts) so GitHub's camo proxy renders them."""
import math, os, sys
from xml.sax.saxutils import escape as esc

OUT = sys.argv[1]
os.makedirs(f"{OUT}/projects", exist_ok=True)

FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',monospace"
BG, SURF, LINE, TXT, MUTED = "#0d1117", "#161b22", "#30363d", "#e6edf3", "#8b949e"


def tw(s, size):  # rough text width estimate
    return len(s) * size * 0.64


def write(name, svg):
    with open(f"{OUT}/{name}", "w") as f:
        f.write(svg)


# ------------------------------------------------------------------ HERO
def hero():
    W, H = 1000, 340
    cx, cy = 790, 170
    orbit = [("Java", 70, 0, "#f89820"), ("Spring", 70, 120, "#6db33f"), ("Kafka", 70, 240, "#e6edf3"),
             ("React", 118, 30, "#61dafb"), ("Next.js", 118, 102, "#ffffff"), ("Expo", 118, 174, "#a371f7"),
             ("Redis", 118, 246, "#ff4438"), ("K8s", 118, 318, "#326ce5"),
             ("Postgres", 160, 60, "#699eca"), ("Docker", 160, 180, "#2496ed"), ("Odoo", 160, 300, "#a24689")]
    rings = "".join(
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LINE}" stroke-dasharray="2 6"/>' for r in (70, 118, 160))
    nodes = []
    for i, (label, r, start, col) in enumerate(orbit):
        dur = {70: 18, 118: 28, 160: 40}[r]
        # circle path starting at angle `start`
        a = math.radians(start)
        sx, sy = cx + r * math.cos(a), cy + r * math.sin(a)
        ex, ey = cx - r * math.cos(a), cy - r * math.sin(a)
        path = f"M{sx:.1f},{sy:.1f} A{r},{r} 0 1,1 {ex:.1f},{ey:.1f} A{r},{r} 0 1,1 {sx:.1f},{sy:.1f}"
        w = tw(label, 11) + 18
        nodes.append(f'''<g><animateMotion dur="{dur}s" repeatCount="indefinite" path="{path}"/>
      <rect x="{-w/2:.1f}" y="-11" width="{w:.1f}" height="22" rx="11" fill="{SURF}" stroke="{col}" stroke-opacity=".7"/>
      <circle cx="{-w/2+9:.1f}" cy="0" r="3" fill="{col}"/>
      <text x="{6:.1f}" y="4" text-anchor="middle" font-size="11" fill="{TXT}" font-family="{MONO}">{label}</text></g>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Joseph Mwalwama — I build the software a business runs on.">
  <defs>
    <linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#58a6ff"/><stop offset=".5" stop-color="#a371f7"/><stop offset="1" stop-color="#3fb950"/></linearGradient>
    <radialGradient id="glow" cx="{cx/W:.2f}" cy=".5" r=".45"><stop offset="0" stop-color="#1f6feb" stop-opacity=".35"/><stop offset="1" stop-color="#1f6feb" stop-opacity="0"/></radialGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#21262d" stroke-width="1"/></pattern>
    <linearGradient id="fade" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}"/></linearGradient>
    <clipPath id="clip"><rect width="{W}" height="{H}" rx="16"/></clipPath>
  </defs>
  <style>
    .in{{opacity:0;animation:up .8s cubic-bezier(.2,.7,.2,1) forwards}}
    .d1{{animation-delay:.1s}}.d2{{animation-delay:.35s}}.d3{{animation-delay:.6s}}.d4{{animation-delay:.85s}}.d5{{animation-delay:1.1s}}
    @keyframes up{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
    .pulse{{animation:p 2s ease-out infinite;transform-origin:62px 278px}}
    @keyframes p{{0%{{opacity:.8;transform:scale(1)}}100%{{opacity:0;transform:scale(3)}}}}
    .scan{{animation:s 6s linear infinite}}
    @keyframes s{{from{{transform:translateY(-40px)}}to{{transform:translateY({H}px)}}}}
    .shine{{animation:sh 5s ease-in-out infinite}}
    @keyframes sh{{0%,100%{{stop-opacity:0}}50%{{stop-opacity:.9}}}}
  </style>
  <g clip-path="url(#clip)">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <rect width="{W}" height="{H}" fill="url(#grid)"/>
    <rect width="{W}" height="{H}" fill="url(#glow)"/>
    <rect width="{W}" height="{H}" fill="url(#fade)" opacity=".6"/>
    <rect class="scan" width="{W}" height="40" fill="#58a6ff" opacity=".04"/>
    {rings}
    <circle cx="{cx}" cy="{cy}" r="26" fill="{SURF}" stroke="url(#g)" stroke-width="2"/>
    <text x="{cx}" y="{cy+6}" text-anchor="middle" font-size="17" font-weight="700" fill="{TXT}" font-family="{MONO}">JM</text>
    {"".join(nodes)}
    <g font-family="{FONT}">
      <text x="52" y="78" font-size="13" letter-spacing="3" fill="#58a6ff" font-family="{MONO}">FULL-STACK SOFTWARE ENGINEER</text>
      <text x="50" y="132" font-size="46" font-weight="800" fill="{TXT}">Joseph Mwalwama</text>
      <text x="52" y="178" font-size="25" font-weight="600" fill="url(#g)">I build the software a business runs on.</text>
      <text x="52" y="214" font-size="15" fill="{MUTED}">Backend systems · payment integrations · web &amp; mobile products</text>
      <text x="52" y="238" font-size="15" fill="{MUTED}">Dar es Salaam, Tanzania · Clockwise Technologies</text>
      <g>
        <rect x="46" y="262" width="292" height="32" rx="16" fill="#0f2a1a" stroke="#238636"/>
        <circle class="pulse" cx="62" cy="278" r="5" fill="#3fb950"/>
        <circle cx="62" cy="278" r="5" fill="#3fb950"/>
        <text x="76" y="283" font-size="13" font-weight="600" fill="#7ee787">Available for freelance &amp; contract</text>
      </g>
    </g>
    <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="none" stroke="{LINE}"/>
  </g>
</svg>'''


# ------------------------------------------------------------------ FLOW (shared)
def flow(steps, x0, y, width, accent, uid, node_h=30, fs=11):
    """Row of nodes with animated packets travelling between them."""
    n = len(steps)
    ws = [tw(s, fs) + 22 for s in steps]
    gap = (width - sum(ws)) / (n - 1)
    out, xs, x = [], [], x0
    for w in ws:
        xs.append(x); x += w + gap
    for i in range(n - 1):
        a, b = xs[i] + ws[i], xs[i + 1]
        yc = y + node_h / 2
        out.append(f'<line x1="{a:.1f}" y1="{yc}" x2="{b-4:.1f}" y2="{yc}" stroke="{accent}" stroke-opacity=".35" stroke-width="1.5" stroke-dasharray="4 4"><animate attributeName="stroke-dashoffset" from="8" to="0" dur=".6s" repeatCount="indefinite"/></line>')
        out.append(f'<path d="M{b-6:.1f},{yc-4} L{b:.1f},{yc} L{b-6:.1f},{yc+4}" fill="none" stroke="{accent}" stroke-opacity=".6" stroke-width="1.5"/>')
        out.append(f'<circle r="3.5" fill="{accent}"><animateMotion dur="2.4s" begin="{i*0.6:.1f}s" repeatCount="indefinite" path="M{a:.1f},{yc} L{b-4:.1f},{yc}" keyPoints="0;1;1" keyTimes="0;0.45;1" calcMode="linear"/><animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;.05;.4;.45;1" dur="2.4s" begin="{i*0.6:.1f}s" repeatCount="indefinite"/></circle>')
    for i, (s, w) in enumerate(zip(steps, ws)):
        out.append(f'''<g><rect x="{xs[i]:.1f}" y="{y}" width="{w:.1f}" height="{node_h}" rx="8" fill="{SURF}" stroke="{accent}" stroke-opacity=".55">
      <animate attributeName="stroke-opacity" values=".55;1;.55" dur="2.4s" begin="{i*0.6:.1f}s" repeatCount="indefinite"/></rect>
      <text x="{xs[i]+w/2:.1f}" y="{y+node_h/2+4}" text-anchor="middle" font-size="{fs}" fill="{TXT}" font-family="{MONO}">{esc(s)}</text></g>''')
    return "\n".join(out)


def pills(tags, x, y, accent):
    out = []
    for t in tags:
        w = tw(t, 11) + 18
        out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="22" rx="11" fill="{accent}" fill-opacity=".12" stroke="{accent}" stroke-opacity=".35"/>'
                   f'<text x="{x+w/2:.1f}" y="{y+15}" text-anchor="middle" font-size="11" fill="{accent}" font-family="{FONT}">{esc(t)}</text>')
        x += w + 8
    return "".join(out)


# ------------------------------------------------------------------ PROJECT CARD
def card(slug, num, title, sub, steps, tags, accent):
    W, H = 480, 250
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title)} — {esc(sub)}">
  <defs>
    <linearGradient id="t{slug}" x1="0" x2="1"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></linearGradient>
    <radialGradient id="r{slug}" cx="1" cy="0" r=".9"><stop offset="0" stop-color="{accent}" stop-opacity=".16"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
  </defs>
  <style>.ar{{animation:a 1.6s ease-in-out infinite}}@keyframes a{{50%{{transform:translateX(4px)}}}}</style>
  <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{BG}" stroke="{LINE}"/>
  <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="url(#r{slug})"/>
  <rect x="24" y="0" width="140" height="3" rx="1.5" fill="url(#t{slug})"/>
  <g font-family="{FONT}">
    <text x="24" y="40" font-size="12" fill="{accent}" font-family="{MONO}" letter-spacing="1">{esc(num)}</text>
    <text x="24" y="68" font-size="21" font-weight="700" fill="{TXT}">{esc(title)}</text>
    <text x="24" y="92" font-size="13" fill="{MUTED}">{esc(sub)}</text>
  </g>
  {flow(steps, 24, 120, W-48, accent, slug)}
  {pills(tags, 24, 184, accent)}
  <g font-family="{FONT}" font-size="12" font-weight="600" fill="{TXT}">
    <text x="{W-24}" y="232" text-anchor="end">Read case study <tspan class="ar" fill="{accent}">→</tspan></text>
  </g>
</svg>'''


# ------------------------------------------------------------------ KEY POS FEATURE
def keypos():
    W, H, A = 1000, 280, "#f78166"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Key POS — POS and inventory platform, launching 1 December 2026">
  <defs>
    <linearGradient id="kg" x1="0" x2="1"><stop offset="0" stop-color="#f78166"/><stop offset="1" stop-color="#d29922"/></linearGradient>
    <radialGradient id="kr" cx="0" cy="0" r="1"><stop offset="0" stop-color="{A}" stop-opacity=".18"/><stop offset="1" stop-color="{A}" stop-opacity="0"/></radialGradient>
  </defs>
  <style>
    .b{{animation:bl 1.2s step-end infinite}}@keyframes bl{{50%{{opacity:.35}}}}
  </style>
  <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="{BG}" stroke="{LINE}"/>
  <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="url(#kr)"/>
  <rect x="28" y="0" width="220" height="3" rx="1.5" fill="url(#kg)"/>
  <g font-family="{FONT}">
    <rect x="28" y="26" width="190" height="24" rx="12" fill="{A}" fill-opacity=".14" stroke="{A}" stroke-opacity=".5"/>
    <circle class="b" cx="42" cy="38" r="4" fill="{A}"/>
    <text x="52" y="42" font-size="11" font-weight="700" fill="{A}" letter-spacing="1">LAUNCHING 1 DEC 2026</text>
    <text x="28" y="88" font-size="30" font-weight="800" fill="{TXT}">Key POS</text>
    <text x="170" y="88" font-size="16" fill="{MUTED}">— point of sale &amp; inventory for multi-branch businesses</text>
    <text x="28" y="116" font-size="14" fill="{MUTED}">Multilingual staff · stock transfer, tracking &amp; counting · role-based web, mobile &amp; POS terminal apps</text>
  </g>
  {flow(["Web", "Mobile", "POS terminal", "API Gateway", "Microservices", "Kafka", "PostgreSQL"], 28, 148, W-56, A, "kp", node_h=34, fs=12)}
  {pills(["Spring Boot microservices", "Next.js", "React Native / Expo", "Kafka", "Redis", "Docker"], 28, 208, A)}
  <text x="{W-28}" y="250" text-anchor="end" font-family="{FONT}" font-size="13" font-weight="600" fill="{TXT}">keypos.store  ·  Read case study <tspan fill="{A}">→</tspan></text>
</svg>'''


# ------------------------------------------------------------------ ARCHITECTURE
def arch():
    W, H = 1000, 380
    B, G, P, O, Y = "#58a6ff", "#3fb950", "#a371f7", "#f78166", "#d29922"

    def box(x, y, w, h, label, sub, col, i=0):
        return f'''<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{SURF}" stroke="{col}" stroke-opacity=".6">
      <animate attributeName="stroke-opacity" values=".5;1;.5" dur="3s" begin="{i*.4:.1f}s" repeatCount="indefinite"/></rect>
      <text x="{x+w/2}" y="{y+h/2-(3 if sub else -4)}" text-anchor="middle" font-size="13" font-weight="700" fill="{TXT}" font-family="{FONT}">{label}</text>
      {f'<text x="{x+w/2}" y="{y+h/2+14}" text-anchor="middle" font-size="10.5" fill="{MUTED}" font-family="{MONO}">{sub}</text>' if sub else ''}</g>'''

    def wire(d, col, dur=2.2, begin=0):
        return (f'<path d="{d}" fill="none" stroke="{col}" stroke-opacity=".3" stroke-width="1.5" stroke-dasharray="4 4"/>'
                f'<circle r="3.5" fill="{col}"><animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" path="{d}"/></circle>')

    clients = [("Web", "Next.js", 60), ("Mobile", "Expo", 150), ("POS / 3rd party", "REST · GraphQL", 240)]
    svcs = [("Auth", "Spring Security · JWT", 40), ("Orders", "Spring Boot", 118), ("Payments", "Selcom · CRDB", 196), ("Inventory", "Spring Boot", 274)]
    s = []
    for i, (l, sub, y) in enumerate(clients):
        s.append(wire(f"M180,{y+25} C225,{y+25} 225,175 270,175", B, 2.2, i * .5))
        s.append(box(30, y, 150, 50, l, sub, B, i))
    s.append(box(270, 135, 180, 80, "API Gateway", "auth · rate-limit", G, 3))
    for i, (l, sub, y) in enumerate(svcs):
        s.append(wire(f"M450,175 C495,175 490,{y+27} 540,{y+27}", G, 2.2, .3 + i * .45))
        s.append(wire(f"M720,{y+27} C760,{y+27} 755,{120 if i<2 else 260} 790,{120 if i<2 else 260}", P if i < 2 else O, 2.6, .8 + i * .4))
        s.append(box(540, y, 180, 54, l, sub, P, i + 4))
    s.append(box(790, 80, 180, 80, "Kafka / RabbitMQ", "events · outbox", Y, 8))
    s.append(box(790, 220, 180, 80, "PostgreSQL · Redis", "db-per-service", O, 9))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="How I build: clients to API gateway to Spring Boot microservices, events and data">
  <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="{BG}" stroke="{LINE}"/>
  <text x="30" y="34" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{MUTED}">HOW I BUILD — A TYPICAL PRODUCTION SYSTEM</text>
  {"".join(s)}
  <g font-family="{FONT}" font-size="11.5" fill="{MUTED}">
    <text x="30" y="358">Docker · Kubernetes · Nginx · Cloudflare · GitHub Actions CI/CD · health probes · tracing &amp; structured logs</text>
  </g>
</svg>'''


write("hero.svg", hero())
write("keypos.svg", keypos())
write("architecture.svg", arch())
PROJECTS = [
    ("payment-integrations", "01 · INTEGRATIONS", "Payment & Billing", "Business systems wired to banks & gateways",
     ["ERP / Odoo", "Billing API", "CRDB · Selcom", "Callback"], ["Spring Boot", "Webhooks", "Odoo"], "#3fb950"),
    ("e-valuation-board", "02 · GOVTECH", "E-Valuation Board", "Registration & verification of valuers in TZ",
     ["Applicant", "Web portal", "REST API", "Verified"], ["Spring Boot", "REST", "React"], "#58a6ff"),
    ("silent-ocean", "03 · SALES & ANALYTICS", "Silent Ocean", "Sales team app & KPI dashboards",
     ["Field sales", "App", "Analytics", "KPI history"], ["React", "Dashboards", "Spring Boot"], "#a371f7"),
    ("lepont", "04 · FINTECH", "Lepont", "Microfinance — loans, repayments, reporting",
     ["Apply", "Approve", "Disburse", "Repay"], ["Laravel API", "React", "MySQL"], "#d29922"),
    ("jza-tracking", "05 · LOGISTICS", "JZA Tracking", "Fleet locations & running costs",
     ["GPS device", "Ingest", "Live map", "Costs"], ["Java", "Maps", "React"], "#39c5cf"),
    ("atomcards", "06 · PRODUCT", "AtomCards", "NFC card that opens a digital profile",
     ["Tap NFC", "Profile", "Save contact"], ["React", "Vite", "NFC"], "#db61a2"),
]
for p in PROJECTS:
    write(f"projects/{p[0]}.svg", card(*p))
print("ok")
