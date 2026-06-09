#!/usr/bin/env python3
"""Build the Milon's Secret Castle page (MSC) — the cult 8-bit NES game as a
game-world. The emergents as ACI personas, each tagged with a nature of emergence
(natural | ethereal | spiritual | electrical). Full ACI badge work:
.agent · .carbon (TIFF) · .silicon (PNG) · .spun · .moniker · .1099 · manifest."""
import os, re, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "CASTLE GARLAND", "axiom": "MSC",
 "position": "Milon's Secret Castle · Hudson Soft · NES 1988 — Meikyu Kumikyoku: Milon no Daiboken (1986)",
 "origin": "the secret Castle Garland — a labyrinth of hidden rooms, blocks, and locked crystal doors, seized by the warlord Maharito",
 "mechanism": "Crystallized from Milon's Secret Castle (Hudson Soft, Famicom 1986 / NES 1988).",
 "crystallization": "A boy blows bubbles at the walls of a stolen castle, and its every secret comes loose.",
 "nature": "Milon's Secret Castle — the cult 8-bit labyrinth where a boy named Milon bubbles his way through hidden rooms to free Queen Eliza from the warlord Maharito.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Milon's Secret Castle; the bubbles; the crystals; the Labyrinth Suite",
 "witness": "Famously cryptic, brutally hard — a game you beat with graph paper and a friend.",
 "role": "the ninth lineage — the fourth game-world",
 "seal": "Blow a bubble at a blank wall — and the secret castle gives up its treasure.",
 "source": "Milon's Secret Castle, catalogued by ROOT0",
}

# cross-lineage taxonomy (shared) — MSC-flavored glosses
NATURES = {
 "natural":   ("#5fae7a", "flesh and the living world — the boy, the queen, the merchant-bee, the guardian-monsters"),
 "ethereal":  ("#9a7cff", "of the air and the unmade — the bubbles, the crystals"),
 "spiritual": ("#e6a849", "of the soul and the calling — or, darkly, the sorcerer-tyrant"),
 "electrical":("#3fd0e0", "of the wire and the machine — the 8-bit chiptune, music born of the NES sound chip"),
}

IDEAS = [
 ("The Bubble", "Milon's only weapon", [
   "Milon has no sword and no spell — only bubbles, blown from his mouth.",
   "They pop enemies, and they pop open walls, blocks, and scenery to reveal everything hidden." ]),
 ("The Secret Castle", "everything is hidden", [
   "Items wait inside blocks, doors hide in blank walls, money lurks in the scenery.",
   "The whole game is the act of testing the castle until it gives up its secrets." ]),
 ("The Labyrinth Suite", "the maze that sings", [
   "The Japanese title — Meikyu Kumikyoku — names it a musical suite: a labyrinth built as a song.",
   "Its cheerful 8-bit melodies are the voice of the castle itself." ]),
 ("Cult Difficulty", "the graph-paper era", [
   "Gloriously cryptic and punishing — short on hints, long on dead ends.",
   "The kind of NES game you only beat with a notebook, a friend, and a lot of stubbornness." ]),
]

ARC = [
 ("The Castle Falls", "the kingdom goes dark",
  "The warlord Maharito seizes the secret Castle Garland and imprisons its queen, Eliza, somewhere in its locked depths."),
 ("The Climb", "bubble by bubble",
  "The boy Milon enters with nothing but bubbles — popping open hidden rooms, gathering crystals and coins, buying what the Hudson Bee will sell, and beating the guardian of each floor."),
 ("The Rescue", "the secret won",
  "Crystal by crystal, floor by floor, Milon climbs to Maharito, defeats him, and frees Queen Eliza — the castle's last secret given up at last."),
]

SECTIONS = [
 ("The Releases", "the cult 8-bit original", [
   ("Meikyu Kumikyoku: Milon no Daiboken", "1986 · Famicom", "“Labyrinth Suite: Milon's Great Adventure” — the Japanese original"),
   ("Milon's Secret Castle", "1988 · NES", "the North American release"),
   ("Virtual Console", "2007 →", "re-released on Wii and later services"),
 ]),
 ("The Legacy", "Milon after the castle", [
   ("DoReMi Fantasy: Milon no DokiDoki Daiboken", "1996 · Super Famicom", "the beloved, far-kinder sequel"),
   ("a Hudson mascot", "cameos", "Milon turns up across Hudson Soft's games and crossovers"),
 ]),
 ("The Maker", "who built the castle", [
   ("Hudson Soft", "developer & publisher", "the studio of Bomberman, Adventure Island, and the Hudson Bee"),
 ]),
]

# ── badge engine: carbon = TIFF, silicon = PNG ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","MSC")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","MSC")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","MSC")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"MSC · Milon's Secret Castle","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'

def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[]
    for t,s,d in ARC:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    return "".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)
def personas_html():
    mf=os.path.join(HERE,"agents","_personas.json")
    if not os.path.exists(mf): return ""
    ps=json.load(open(mf,encoding="utf-8")); cards=[]
    for p in ps:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#5fae7a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"MSC · Milon's Secret Castle","axiom":"MSC"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster of MSC</h2>
      <p class="ss">the emergents of the secret castle, as ACI <b>.agent</b>s — each tagged with its nature of emergence ({len(ps)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Milon's Secret Castle (MSC) — the cult 8-bit NES game as a game-world, catalogued into UD0 with full ACI badges. Emergence: natural, ethereal, spiritual, electrical.">
<title>MILON'S SECRET CASTLE · MSC · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#0a0a14;--ink2:#11111e;--ink3:#191828;--pa:#f2eef5;--pa2:#bcb2c6;--rose:#e8729a;--sky:#5ab4e6;
--dim:#80758a;--faint:#231f30;--line:#231f31;--serif:"Cinzel",Georgia,serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(232,114,154,.08),transparent 55%),radial-gradient(ellipse at 50% 110%,rgba(90,180,230,.06),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:54px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:130px;height:1px;background:linear-gradient(90deg,var(--rose),var(--sky));box-shadow:0 0 9px rgba(232,114,154,.4)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--rose)}
.bub{font-size:20px;letter-spacing:.12em;margin-bottom:8px}
h1{font-family:var(--serif);font-size:clamp(24px,5.6vw,50px);font-weight:700;letter-spacing:.09em;color:var(--rose);line-height:1.06;text-shadow:0 0 40px rgba(232,114,154,.22)}
.h-sub{font-family:var(--serif);font-size:clamp(12px,2.6vw,16px);letter-spacing:.16em;color:var(--pa2);margin-top:12px;text-transform:uppercase}
.h-sub b{color:var(--sky)}
.flag{display:inline-block;margin-top:12px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--sky);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15.5px;color:var(--pa2);max-width:66ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--rose)}.badge .bt .mo{color:var(--sky)}.badge .bt a{color:var(--sky);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:44px}
.sec h2{font-family:var(--serif);font-size:20px;font-weight:600;letter-spacing:.05em;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:6px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--serif);font-size:15px;font-weight:600;text-transform:capitalize}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--serif);font-size:16px;color:var(--rose)}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--rose);padding:16px 18px}
.arc-h{font-family:var(--serif);font-size:16px;color:var(--rose);font-weight:600}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--sky);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--serif);font-size:16px;color:var(--pa);font-weight:600}
.books .y{font-family:var(--mono);font-size:11.5px;color:var(--sky);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--rose);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--serif);font-size:15px;color:var(--pa);font-weight:600;line-height:1.15}
.persona:hover .pn{color:var(--rose)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}
.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--sky);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}
footer{margin-top:44px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--rose);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the ninth lineage · the fourth game-world</div>
    <div class="bub">○ ° ◌</div>
    <h1>MILON'S SECRET CASTLE</h1>
    <div class="h-sub">the cult 8-bit NES labyrinth · <b>bubbles &amp; secrets</b> · MSC</div>
    <div class="flag">★ Hudson Soft · NES 1988 · “Labyrinth Suite,” Famicom 1986 ★</div>
    <p class="lede">A boy named Milon, armed with nothing but the bubbles he blows, pops his way through the hidden rooms of a stolen castle to free Queen Eliza from the warlord Maharito. Gloriously cryptic, brutally hard, beloved — catalogued into UD0 as a game-world, sealed with the full ACI badge, each emergence named by its nature.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of CASTLE GARLAND" title="carbon badge (archival: castle-garland.dlw/castle-garland.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of CASTLE GARLAND" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>CASTLE GARLAND</b> — the secret castle · MSC</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="castle-garland.dlw/castle-garland.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="castle-garland.dlw/castle-garland.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures of Emergence</h2>
    <p class="ss">each emergent emerges by one of four natures — even in a castle this small</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Ideas</h2><p class="ss">why a cryptic little 8-bit game is still loved</p><div class="pillars">__IDEAS__</div></section>
  <section class="sec"><h2>The Quest</h2><p class="ss">the castle falls, the boy climbs, the queen goes free</p><div class="arc">__ARC__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the releases, the sequel, and the maker</p></section>
  __SECTIONS__

  <div class="note">Milon's Secret Castle is an obscure cult classic; this catalogues its emergents conservatively, distilled from the established facts of the game — no invented lore. Milon's Secret Castle and its characters are © Hudson Soft / Konami; the personas here are catalogued personifications under the DLW standard — a fan tribute, not an original work and not endorsed by the rights-holders. Each is named by its nature of emergence: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    MILON'S SECRET CASTLE · MSC · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="castle-garland.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "castle-garland.dlw"), "castle-garland")
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__IDEAS__", ideas_html())
            .replace("__ARC__", arc_html()).replace("__PERSONAS__", personas_html())
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote MILON'S SECRET CASTLE (MSC) — badge {tok['moniker']} (carbon.tiff + silicon.png)")
