import base64, os, sys

OUT = sys.argv[1]
MEDIA = sys.argv[2]  # tamerardal-com/out/_next/static/media
os.makedirs(OUT, exist_ok=True)

# Palette from tamerardal-com/src/app/globals.css (dark theme for the dark cards,
# light theme values for the light logo)
BG, CARD, RULE = "#171b1d", "#1f2426", "#33393b"
TEXT, STEEL = "#e3e4de", "#9aa5a8"
BRASS, BRASS_HI = "#d4a84a", "#e3bd62"
TEAL, IRON, BAND = "#7db6ae", "#24575a", "#0f2628"
RED = "#e8756b"  # Sting Red: HIGH severity (dark theme)
L_PAPER, L_INK, L_BRASS = "#e7e8e3", "#1b2226", "#6e4f0c"

DISPLAY = "'Big Shoulders','Arial Narrow','Roboto Condensed',sans-serif"
SERIF = "'Source Serif 4','Iowan Old Style',Georgia,serif"
MONO = "'IBM Plex Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

FONT_FILES = {
    "display": ("Big Shoulders", "700 900", "55cb69ad17a100ed.p.2l41_ldkjomdb.woff2"),
    "serif": ("Source Serif 4", "200 900", "68d403cf9f2c68c5-s.p.012bmydply3go.woff2"),
    "mono": ("IBM Plex Mono", "400", "99e609270109b47d-s.p.40sczeszzbjw1.woff2"),
    "mono500": ("IBM Plex Mono", "500", "effe91970fc4db64-s.p.0oace-s_gkfks.woff2"),
}


def font_css(keys):
    out = ""
    for k in keys:
        fam, wt, fn = FONT_FILES[k]
        b64 = base64.b64encode(open(os.path.join(MEDIA, fn), "rb").read()).decode()
        out += f"@font-face{{font-family:'{fam}';font-weight:{wt};font-style:normal;src:url(data:font/woff2;base64,{b64}) format('woff2')}}\n"
    return out


def fly(body=BRASS, eye=BG, wing_op=0.3, animate=False):
    """Gadfly mark on a 120x120 grid. Head up, stinger down."""
    wl = "wing wl" if animate else ""
    wr = "wing wr" if animate else ""
    return f"""<g>
  <path class="{wl}" d="M56 58 C40 56 14 44 12 26 C30 20 52 34 56 58Z" fill="{body}" fill-opacity="{wing_op}" stroke="{body}" stroke-width="2.5" stroke-linejoin="round"/>
  <path class="{wr}" d="M64 58 C80 56 106 44 108 26 C90 20 68 34 64 58Z" fill="{body}" fill-opacity="{wing_op}" stroke="{body}" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M52 88 L68 88 L60 110Z" fill="{body}" stroke="{body}" stroke-width="2" stroke-linejoin="round"/>
  <ellipse cx="60" cy="68" rx="11" ry="22" fill="{body}"/>
  <circle cx="60" cy="41" r="10" fill="{body}"/>
  <circle cx="55.5" cy="39.5" r="3" fill="{eye}"/>
  <circle cx="64.5" cy="39.5" r="3" fill="{eye}"/>
  <path d="M50 63 Q60 67 70 63 M49.5 72 Q60 76 70.5 72 M51 81 Q60 85 69 81" fill="none" stroke="{eye}" stroke-width="2" stroke-linecap="round" stroke-opacity=".75"/>
</g>"""


FLAP_CSS = """
.wing{transform-box:fill-box}
.wl{transform-origin:100% 100%;animation:flapL .2s ease-in-out infinite alternate}
.wr{transform-origin:0% 100%;animation:flapR .2s ease-in-out infinite alternate}
@keyframes flapL{from{transform:rotate(-8deg)}to{transform:rotate(9deg)}}
@keyframes flapR{from{transform:rotate(8deg)}to{transform:rotate(-9deg)}}
"""


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)


def svg(w, h, body, title, css="", fonts=()):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t">
<title id="t">{title}</title>
<style>{font_css(fonts)}{css}</style>
{body}
</svg>
"""


# ---------- logos ----------
write("logo-icon.svg", svg(120, 120, fly(), "Gadfly"))
write("logo-mono.svg", svg(120, 120, fly(body="#000000", eye="#FFFFFF", wing_op=0.18), "Gadfly (monochrome)"))


def horizontal(text_color, body, eye):
    inner = f"""{fly(body=body, eye=eye)}
<text x="140" y="96" font-family="{DISPLAY}" font-size="88" font-weight="800" fill="{text_color}" letter-spacing="2">GADFLY</text>"""
    return svg(420, 120, inner, "Gadfly", fonts=("display",))


write("logo-horizontal.svg", horizontal(L_INK, L_BRASS, L_PAPER))
write("logo-horizontal-dark.svg", horizontal(TEXT, BRASS, BG))

# ---------- hero (animated) ----------
trail = "M742 292 C800 300 782 228 832 206 C884 184 804 120 850 64"
hero_body = f"""
<defs>
  <radialGradient id="glow" cx="22%" cy="45%" r="55%">
    <stop offset="0" stop-color="{IRON}" stop-opacity=".55"/>
    <stop offset="1" stop-color="{IRON}" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="900" height="320" rx="20" fill="{BG}"/>
<rect width="900" height="320" rx="20" fill="url(#glow)"/>
<path d="{trail}" fill="none" stroke="{BRASS}" stroke-opacity=".6" stroke-width="2" stroke-dasharray="3 9" stroke-linecap="round" class="trail"/>
<g transform="translate(70 70) scale(1.4)" class="bob">{fly(animate=True)}</g>
<text x="270" y="152" font-family="{DISPLAY}" font-size="128" font-weight="900" fill="{TEXT}" letter-spacing="3">GADFLY</text>
<text x="272" y="198" font-family="{SERIF}" font-size="25" fill="{BRASS}">Sting your idea before the internet does.</text>
<text x="272" y="240" font-family="{SERIF}" font-size="17" fill="{STEEL}">Red-team a draft with parallel personas and real community</text>
<text x="272" y="264" font-family="{SERIF}" font-size="17" fill="{STEEL}">objections. Get a ranked list of fixes, not a lecture.</text>
<g>
  <animateMotion dur="9s" repeatCount="indefinite" rotate="auto" path="{trail}"/>
  <g transform="rotate(90) scale(.32) translate(-60 -60)">{fly(animate=True)}</g>
</g>
"""
hero_css = FLAP_CSS + """
.bob{animation:bob 3.2s ease-in-out infinite alternate}
@keyframes bob{from{transform:translate(70px,66px) scale(1.4)}to{transform:translate(70px,76px) scale(1.4)}}
.trail{animation:dash 1.6s linear infinite}
@keyframes dash{to{stroke-dashoffset:-24}}
@media (prefers-reduced-motion:reduce){.wl,.wr,.bob,.trail{animation:none}}
"""
write("hero.svg", svg(900, 320, hero_body, "Gadfly: sting your idea before the internet does", hero_css, ("display", "serif")))


# ---------- flow (animated) ----------
def box(x, y, w, h, label, sub, cls):
    return f"""<g class="node {cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{CARD}" stroke="{RULE}" stroke-width="1.5"/>
<text x="{x+w/2}" y="{y+h/2-3}" text-anchor="middle" font-family="{SERIF}" font-size="17" font-weight="700" fill="{TEXT}">{label}</text>
<text x="{x+w/2}" y="{y+h/2+16}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{STEEL}">{sub}</text></g>"""


personas = ["Opposing expert", "Fact-checker", "Skeptic", "Newcomer", "Seen-it-all veteran"]
chips = ""
for i, p in enumerate(personas):
    chips += f'<g class="chip" style="animation-delay:{1.6 + i*0.12:.2f}s"><rect x="352" y="{146+i*30}" width="196" height="24" rx="4" fill="{BG}" stroke="{TEAL}" stroke-opacity=".6"/><text x="450" y="{163+i*30}" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{TEXT}">{p}</text></g>'

arrows = [
    ("M135 200 L160 200", 0.2),
    ("M280 200 C300 200 310 80 340 80", 0.8),
    ("M280 200 C300 200 315 230 340 230", 0.8),
    ("M450 112 L450 134", 1.4),
    ("M560 230 L596 230", 2.6),
    ("M700 230 L736 230", 3.2),
]
arrow_svg = "".join(
    f'<path d="{d}" fill="none" stroke="{BRASS}" stroke-width="2" stroke-dasharray="5 6" stroke-linecap="round" class="flow" style="animation-delay:{dl}s"/>'
    for d, dl in arrows
)
flow_body = f"""
<rect width="900" height="360" rx="20" fill="{BG}"/>
<text x="30" y="40" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{BRASS}">HOW IT WORKS</text>
{arrow_svg}
{box(30, 170, 105, 60, "Draft", "md / paste", "n1")}
{box(160, 170, 120, 60, "Claims", "extract", "n2")}
{box(340, 48, 220, 64, "Research agent", "HN · Reddit · forums", "n3")}
<g class="node n4"><rect x="340" y="134" width="220" height="164" rx="8" fill="{CARD}" stroke="{RULE}" stroke-width="1.5"/></g>
{chips}
<text x="450" y="322" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{STEEL}">personas run in parallel</text>
{box(596, 200, 104, 60, "Merge", "dedupe + rank", "n5")}
{box(736, 200, 134, 60, "Report", "fix per objection", "n6")}
"""
flow_css = f"""
.flow{{animation:dash 1.2s linear infinite}}
@keyframes dash{{to{{stroke-dashoffset:-22}}}}
.chip{{animation:pop 6s ease-in-out infinite}}
@keyframes pop{{0%,8%{{opacity:.3}}14%,60%{{opacity:1}}80%,100%{{opacity:.3}}}}
.node rect{{animation:pulse 6s ease-in-out infinite}}
.n1 rect{{animation-delay:0s}}.n2 rect{{animation-delay:.5s}}.n3 rect{{animation-delay:1.1s}}
.n4 rect{{animation-delay:1.5s}}.n5 rect{{animation-delay:2.3s}}.n6 rect{{animation-delay:3s}}
@keyframes pulse{{0%,100%{{stroke:{RULE}}}6%,16%{{stroke:{BRASS}}}30%{{stroke:{RULE}}}}}
@media (prefers-reduced-motion:reduce){{.flow,.chip,.node rect{{animation:none}}}}
"""
write("flow.svg", svg(900, 360, flow_body, "Gadfly pipeline: draft, claims, research agent and parallel personas, merge, report", flow_css, ("serif", "mono")))


# ---------- report preview (animated) ----------
def card(y, sev, color, title, body, fix, src, delay):
    return f"""<g class="card" style="animation-delay:{delay}s">
<rect x="28" y="{y}" width="844" height="96" rx="6" fill="{CARD}" stroke="{RULE}"/>
<rect x="28" y="{y}" width="6" height="96" fill="{color}"/>
<rect x="52" y="{y+14}" width="52" height="20" rx="3" fill="{color}"/>
<text x="78" y="{y+28}" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="500" fill="{BG}">{sev}</text>
<text x="118" y="{y+29}" font-family="{SERIF}" font-size="17" font-weight="700" fill="{TEXT}">{title}</text>
<text x="850" y="{y+29}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{STEEL}">{src}</text>
<text x="52" y="{y+56}" font-family="{SERIF}" font-size="14.5" fill="{STEEL}">{body}</text>
<text x="52" y="{y+80}" font-family="{SERIF}" font-size="14.5" fill="{TEXT}"><tspan font-family="{MONO}" font-size="11" font-weight="500" fill="{BRASS}" letter-spacing="1">FIX  </tspan>{fix}</text>
</g>"""


report_body = f"""
<rect width="900" height="420" rx="20" fill="{BG}"/>
<circle cx="34" cy="30" r="6" fill="{RULE}"/><circle cx="54" cy="30" r="6" fill="{RULE}"/><circle cx="74" cy="30" r="6" fill="{RULE}"/>
<text x="100" y="35" font-family="{MONO}" font-size="13" fill="{STEEL}">gadfly report · quit-todo-apps.md</text>
<text x="872" y="35" text-anchor="end" font-family="{MONO}" font-size="12" fill="{BRASS}">3 objections · example output</text>
{card(58, "HIGH", RED, "&#8220;Doubled&#8230; measured how?&#8221;",
      "The post claims 2x productivity but gives no metric or baseline. It reads as a feeling.",
      "Add one number: tasks shipped per week, before vs. after.", "research + persona", 0)}
{card(166, "MED", BRASS_HI, "&#8220;That&#8217;s a sample of one.&#8221;",
      "Two weeks, one person, one job. Readers will say it won&#8217;t work for them.",
      "Say it&#8217;s your experience, and name who it may not suit.", "persona", 1.1)}
{card(274, "LOW", TEAL, "&#8220;So you just swapped apps for sticky notes?&#8221;",
      "The post never says what replaced the to-do app, so the claim feels incomplete.",
      "Describe your replacement system in two sentences.", "persona", 2.2)}
<text x="450" y="402" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{STEEL}">ranked by severity · each objection ships with a fix · evidence tagged real vs. simulated</text>
"""
report_css = """
.card{animation:reveal 9s ease-in-out infinite;opacity:0}
@keyframes reveal{0%{opacity:0;transform:translateY(10px)}8%,86%{opacity:1;transform:none}95%,100%{opacity:0;transform:translateY(-4px)}}
@media (prefers-reduced-motion:reduce){.card{animation:none;opacity:1}}
"""
write("report-preview.svg", svg(900, 420, report_body, "Example Gadfly report with three ranked objections and fixes", report_css, ("serif", "mono", "mono500")))

# ---------- social preview (static; rasterised with Chrome) ----------
social = f"""
<defs><radialGradient id="g" cx="28%" cy="50%" r="60%"><stop offset="0" stop-color="{IRON}" stop-opacity=".6"/><stop offset="1" stop-color="{IRON}" stop-opacity="0"/></radialGradient></defs>
<rect width="1280" height="640" fill="{BG}"/><rect width="1280" height="640" fill="url(#g)"/>
<g transform="translate(110 150) scale(3.2)">{fly()}</g>
<text x="540" y="330" font-family="{DISPLAY}" font-size="210" font-weight="900" fill="{TEXT}" letter-spacing="4">GADFLY</text>
<text x="546" y="398" font-family="{SERIF}" font-size="34" fill="{BRASS}">Sting your idea before the internet does.</text>
<text x="546" y="456" font-family="{SERIF}" font-size="22" fill="{STEEL}">Pre-publish red-team for posts and technical ideas.</text>
"""
write("social-preview.svg", svg(1280, 640, social, "Gadfly", fonts=("display", "serif")))
print("ok")
