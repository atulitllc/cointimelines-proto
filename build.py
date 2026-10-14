"""CryptoHistoryBook static build. INDEXABLE gates robots/noindex for the whole site (stays False)."""
import json, os, re, shutil, sys, html as H, datetime as dt
sys.path.insert(0, "/workspace/atulit-petcare-proto")
import seo  # reuse Atulit beacon template
from content import COINS, EVENTS
import coins50, coins100, re as _re
BUILD_V = dt.datetime.now().strftime("%Y%m%d%H%M%S")
for _c,_m in {"btc":("bitcoin",["Layer 1","Payments"]),"eth":("ethereum",["Layer 1","Smart contracts"]),"xrp":("ripple",["Layer 1","Payments"]),"doge":("dogecoin",["Meme","Payments"]),"sol":("solana",["Layer 1","Smart contracts"])}.items():
    COINS[_c]["cgid"], COINS[_c]["cats"] = _m
    COINS[_c]["founded_label"] = {"xrp":"Jun 2012"}.get(_c)
for _k,_v in list(coins50.C.items()) + list(coins100.D.items()):
    if not os.path.exists(f"data/{_k}.json"): continue
    COINS[_k] = _v
    for _e in _v["events"]:
        _e = dict(_e, coin=_k, slug=_e["date"][:4] + "-" + _re.sub(r"[^a-z0-9]+", "-", _e["name"].lower()).strip("-")[:48])
        EVENTS.append(_e)
MKT = {x["id"]: x for f in ("data/cg_markets_2026-10-14.json","data/cg_markets_2026-10-14_p2.json") for x in json.load(open(f))}
def _num(v):
    return f"{v/1e12:.2f} trillion" if v>=1e12 else f"{v/1e9:.2f} billion" if v>=1e9 else f"{v/1e6:.1f} million" if v>=1e6 else f"{v:,.0f}"
for _k in coins100.D:
    if _k in COINS:
        m = MKT.get(COINS[_k]["cgid"]) or {}
        if m.get("circulating_supply"): COINS[_k]["facts"].append(("Circulating supply", _num(m["circulating_supply"]) + " (CoinGecko, Oct 14, 2026)"))
        if m.get("max_supply"): COINS[_k]["facts"].append(("Max supply", _num(m["max_supply"]) + " (CoinGecko)"))
        COINS[_k]["primary"].append(("CoinGecko: " + COINS[_k]["name"], "https://www.coingecko.com/en/coins/" + COINS[_k]["cgid"]))
WFIX = json.load(open("wiki_fix.json"))
def _fixsrc(lst, fallback):
    out = []
    for t, u in lst:
        if "en.wikipedia.org/wiki/" in u:
            key = u.split("/wiki/")[1].replace("_", " ")
            if key in WFIX:
                if WFIX[key] is None: continue
                u = "https://en.wikipedia.org/wiki/" + WFIX[key].replace(" ", "_"); t = "Wikipedia: " + WFIX[key]
        if (t, u) not in out: out.append((t, u))
    return out or fallback
for _k, _v in COINS.items():
    _v["primary"] = _fixsrc(_v["primary"], [])
for _e in EVENTS:
    _e["sources"] = _fixsrc(_e["sources"], COINS[_e["coin"]]["primary"][:2])
from articles import ARTICLES, GLOSSARY, COMPARES, YEAR_INTRO
from assets_src import CSS, JS
INDEXABLE = False
BRAND = "CryptoHistoryBook"; ORIGIN = "https://cryptohistorybook.com"
LIVE_HOST = "cryptohistorybook.com"; BEACON_SITE = "cryptohistorybook"
UPDATED = "Oct 14, 2026"; UPDATED_ISO = "2026-10-14"
OUT = "docs"; ICONS = "/tmp/lucide/package/icons"
KC = {"launch":"#0ea5e9","rally":"#10b981","crash":"#ef4444","upgrade":"#7c3aed","legal":"#f59e0b","fork":"#ec4899","outage":"#64748b","milestone":"#f97316"}
KI = {"launch":"rocket","rally":"trending-up","crash":"trending-down","upgrade":"layers","legal":"gavel","fork":"git-fork","outage":"power-off","milestone":"milestone"}
e = H.escape
def icon(n, cls="ic"):
    s = open(f"{ICONS}/{n}.svg").read()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S).strip()
    return re.sub(r'class="[^"]*"', f'class="{cls}" aria-hidden="true"', s, count=1).replace('width="24" height="24"', "")
def mdate(iso): d = dt.date.fromisoformat(iso); return d.strftime("%b ") + str(d.day) + d.strftime(", %Y")
# ---------- data ----------
SER = {c: json.load(open(f"data/{c}.json")) for c in COINS}
def price_on(c, day):
    for d, v in SER[c]["points"]:
        if d == day: return v
def seg_of(c, day):
    for g in SER[c]["segments"]:
        if g["from"] <= day <= g["to"]: return g
def plabel(c, day):
    g = seg_of(c, day); return f'{g["source"]} {g["pair"]} daily close, {day}'
def fmt(v): return f"${v:,.0f}" if v >= 1000 else (f"${v:,.2f}" if v >= 1 else f"${v:.4g}")

def _auto(c):
    P = SER[c]["points"]
    if not P or c in ("btc","eth","xrp","doge","sol"): return
    k = COINS[c]; first = P[0]; hi = max(P, key=lambda p: p[1]); after = [p for p in P if p[0] > hi[0]]
    g0 = seg_of(c, first[0]); gs = [(f'{g["source"]} API', g["url"]) for g in SER[c]["segments"]]
    out = [dict(coin=c, slug=first[0][:4]+"-first-close-in-our-data", date=first[0], kind="milestone", name="First daily close in our data", summary=f'Our sourced {k["sym"]} price history begins on this day.', body=[f'{k["name"]} has a daily close from {g0["source"]} ({g0["pair"]}) starting {first[0]}. Earlier trading may exist on other markets, but we only show prices we can source. Treat early closes with care: new listings often trade thinly.'], sources=gs),
           dict(coin=c, slug=hi[0][:4]+"-highest-close-in-our-data", date=hi[0], kind="rally", name="Highest close in our data", summary=f'The highest daily close for {k["sym"]} in our price history.', body=[f'This is the highest daily close for {k["name"]} in our fetched series, which runs from {first[0]} to {P[-1][0]}. Intraday highs and prices on other exchanges may have been higher.'], sources=gs)]
    if len(after) > 30:
        lo = min(after, key=lambda p: p[1])
        out.append(dict(coin=c, slug=lo[0][:4]+"-lowest-close-after-the-peak", date=lo[0], kind="crash", name="Lowest close after the peak", summary=f'The lowest {k["sym"]} close in our data after its highest close.', body=[f'After its highest close on {hi[0]}, {k["name"]} reached this lowest daily close in our series, a drop of about {round((1-lo[1]/hi[1])*100)} percent. Later prices may differ.'], sources=gs))
    for x in out:
        if not any(y["coin"] == c and y["date"] == x["date"] and y["name"] == x["name"] for y in EVENTS): EVENTS.append(x)
for _c in list(COINS): _auto(_c)
for ev in EVENTS:
    if ev["date"].startswith("auto:max:"):
        pre = ev["date"].split(":")[2]
        cand = [p for p in SER[ev["coin"]]["points"] if p[0].startswith(pre)]
        ev["date"] = max(cand, key=lambda p: p[1])[0]
    ev["price"] = None if ev.get("prices") is False else price_on(ev["coin"], ev["date"])
    ev["year"] = ev["date"][:4]
for c in COINS:
    evs = sorted([x for x in EVENTS if x["coin"] == c], key=lambda x: x["date"])
    COINS[c]["events"] = evs
    for i, x in enumerate(evs): x["prev"] = evs[i-1] if i else None; x["next"] = evs[i+1] if i+1 < len(evs) else None
def evpath(x): return f'{COINS[x["coin"]]["slug"]}/events/{x["slug"]}/'
EVBY = {evpath(x): x for x in EVENTS}
# ---------- svg art ----------
LOGO = '''<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7c3aed"/><stop offset=".55" stop-color="#ec4899"/><stop offset="1" stop-color="#f97316"/></linearGradient></defs><rect width="64" height="64" rx="18" fill="url(#lg)"/><path d="M10 17c7-3 15-3 22 1 7-4 15-4 22-1v32c-7-3-15-3-22 1-7-4-15-4-22-1z" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="3" stroke-linejoin="round"/><path d="M32 18v32" stroke="#fff" stroke-opacity=".5" stroke-width="3"/><path d="M14 42 L24 34 L31 38 L41 24 L50 19" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="24" cy="34" r="3.6" fill="#fff"/><circle cx="41" cy="24" r="3.6" fill="#fff"/><circle cx="50" cy="19" r="4.6" fill="#fde68a" stroke="#fff" stroke-width="2"/></svg>'''
def coinlogo(c, cls="logo"):
    if os.path.exists(f'logos/{COINS[c]["cgid"]}.png'):
        return f'<img class="{cls}" src="__R__img/coins/{COINS[c]["cgid"]}.png" alt="{e(COINS[c]["name"])} logo" width="44" height="44" loading="lazy" decoding="async">'
    k = COINS[c]; col = k["color"]
    inner = {
     "btc": '<text x="32" y="44" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="34" fill="#fff" transform="rotate(14 32 32)">&#8383;</text>',
     "eth": '<path d="M32 10 18 33l14 8 14-8z" fill="#fff"/><path d="M32 10v31l14-8z" fill="#fff" opacity=".6"/><path d="M18 36l14 18 14-18-14 8z" fill="#fff"/><path d="M32 44v10l14-18z" fill="#fff" opacity=".6"/>',
     "xrp": '<path d="M17 18h6l9 9 9-9h6L32 33zM17 46h6l9-9 9 9h6L32 31z" fill="#fff"/>',
     "doge": '<text x="33" y="44" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="800" font-size="32" fill="#fff">&#272;</text>',
     "sol": '<defs><linearGradient id="sg" x1="0" x2="1"><stop offset="0" stop-color="#14F195"/><stop offset="1" stop-color="#9945FF"/></linearGradient></defs><path d="M22 20h26l-6 6H16zM16 29h26l6 6H22zM22 38h26l-6 6H16z" fill="url(#sg)"/>'}[c]
    bg = "#111" if c == "sol" else col
    return f'<svg class="{cls}" viewBox="0 0 64 64" role="img" aria-label="{k["name"]} logo"><circle cx="32" cy="32" r="30" fill="{bg}"/>{inner}</svg>'
def hero_art(c=None):
    col = COINS[c]["color"] if c else "#fde68a"
    return f'''<svg class="art" viewBox="0 0 520 320" aria-hidden="true"><g fill="none" stroke="#fff" stroke-linecap="round"><path d="M10 280 C80 250 110 270 160 210 S240 220 280 150 S360 160 400 90 S470 70 510 30" stroke-width="6" stroke-opacity=".9" class="draw" style="--len:800"/><path d="M10 300 C90 290 150 300 220 260 S330 250 380 200 S470 180 510 140" stroke-width="3" stroke-opacity=".4"/></g><g fill="#fff"><circle cx="160" cy="210" r="9"/><circle cx="280" cy="150" r="9"/><circle cx="400" cy="90" r="9"/><circle cx="510" cy="30" r="13" fill="{col}" stroke="#fff" stroke-width="4"/></g><g fill="#fff" fill-opacity=".18"><rect x="60" y="40" width="110" height="70" rx="16"/><rect x="200" y="20" width="80" height="50" rx="14"/><circle cx="330" cy="260" r="40"/></g></svg>'''
def diagram(kind):
    blk = lambda x, y, c, t, s="": f'<g transform="translate({x},{y})"><rect width="130" height="90" rx="16" fill="{c}"/><text x="65" y="36" text-anchor="middle" fill="#fff" font-weight="700" font-size="16">{t}</text><text x="65" y="60" text-anchor="middle" fill="#fff" font-size="12" opacity=".9">{s}</text></g>'
    arrow = lambda x1, y1, x2, y2: f'<path d="M{x1} {y1}L{x2} {y2}" stroke="#a78bfa" stroke-width="4" marker-end="url(#ah)"/>'
    defs = '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5 0 10z" fill="#a78bfa"/></marker></defs>'
    t = 'font-family="Inter,sans-serif"'
    if kind == "chain":
        b = "".join(blk(20+i*175, 40, c, f"Block {n}", s) for i,(n,c,s) in enumerate([(101,"#7c3aed","prev hash: 9f3a"),(102,"#ec4899","prev hash: 41bc"),(103,"#f97316","prev hash: c7e2"),(104,"#10b981","new block")]))
        a = "".join(arrow(152+i*175, 85, 192+i*175, 85) for i in range(3))
        cap = '<text x="360" y="175" text-anchor="middle" fill="currentColor" font-size="14">Each block stores a fingerprint (hash) of the one before it</text>'
        return f'<svg viewBox="0 0 720 190" {t}>{defs}{b}{a}{cap}</svg>'
    if kind == "ledger":
        nodes = [(360,40),(150,110),(570,110),(220,230),(500,230)]
        ln = "".join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#c4b5fd" stroke-width="3"/>' for i,a in enumerate(nodes) for b in nodes[i+1:])
        cs = ["#7c3aed","#ec4899","#f97316","#0ea5e9","#10b981"]
        nd = "".join(f'<g><circle cx="{x}" cy="{y}" r="34" fill="{cs[i]}"/><rect x="{x-16}" y="{y-14}" width="32" height="28" rx="5" fill="#fff" opacity=".9"/><path d="M{x-10} {y-5}h20M{x-10} {y+2}h20M{x-10} {y+9}h12" stroke="{cs[i]}" stroke-width="3"/></g>' for i,(x,y) in enumerate(nodes))
        return f'<svg viewBox="0 0 720 290" {t}>{ln}{nd}<text x="360" y="285" text-anchor="middle" fill="currentColor" font-size="14">Thousands of computers keep the same copy of the ledger</text></svg>'
    if kind == "wallet":
        return f'''<svg viewBox="0 0 720 230" {t}>{defs}<g transform="translate(30,40)"><rect width="200" height="130" rx="22" fill="#7c3aed"/><circle cx="160" cy="65" r="18" fill="#fde68a"/><text x="30" y="60" fill="#fff" font-weight="700" font-size="18">Wallet</text><text x="30" y="88" fill="#fff" font-size="13">holds private key</text></g>{arrow(240,105,320,105)}<g transform="translate(330,50)"><rect width="150" height="110" rx="18" fill="#ec4899"/><text x="75" y="50" text-anchor="middle" fill="#fff" font-weight="700" font-size="16">Signs</text><text x="75" y="74" text-anchor="middle" fill="#fff" font-size="13">a transaction</text></g>{arrow(490,105,560,105)}<g transform="translate(570,50)"><rect width="130" height="110" rx="18" fill="#f97316"/><text x="65" y="50" text-anchor="middle" fill="#fff" font-weight="700" font-size="16">Blockchain</text><text x="65" y="74" text-anchor="middle" fill="#fff" font-size="13">records it</text></g><text x="360" y="215" text-anchor="middle" fill="currentColor" font-size="14">Coins live on the chain. Your wallet holds the key that moves them.</text></svg>'''
    if kind in ("fork", "segwit", "merge"):
        if kind == "fork":
            body = blk(20,90,"#7c3aed","Shared","history")+arrow(152,135,210,75)+arrow(152,135,210,195)+blk(220,20,"#F7931A","Bitcoin","keeps 1 MB base")+blk(220,150,"#10b981","Bitcoin Cash","8 MB blocks")+blk(400,20,"#F7931A","BTC","continues")+blk(400,150,"#10b981","BCH","continues")+arrow(352,65,392,65)+arrow(352,195,392,195)
            cap = "Aug 1, 2017: one chain becomes two at block 478,558"
        elif kind == "segwit":
            body = '<g transform="translate(40,30)"><rect width="300" height="160" rx="18" fill="#F7931A"/><text x="150" y="40" text-anchor="middle" fill="#fff" font-weight="700" font-size="17">Before: one transaction</text><rect x="20" y="60" width="260" height="38" rx="8" fill="#fff" opacity=".9"/><text x="150" y="85" text-anchor="middle" font-size="13" fill="#7c2d12">inputs, outputs, signatures</text></g>' + arrow(350,110,400,110) + '<g transform="translate(410,30)"><rect width="290" height="160" rx="18" fill="#7c3aed"/><text x="145" y="40" text-anchor="middle" fill="#fff" font-weight="700" font-size="17">After SegWit</text><rect x="20" y="60" width="250" height="34" rx="8" fill="#fff" opacity=".9"/><text x="145" y="82" text-anchor="middle" font-size="13" fill="#4c1d95">inputs, outputs</text><rect x="20" y="104" width="250" height="34" rx="8" fill="#fde68a"/><text x="145" y="126" text-anchor="middle" font-size="13" fill="#78350f">witness (signatures) set apart</text></g>'
            cap = "SegWit moves signatures into a separate witness section"
        else:
            body = blk(20,20,"#64748b","Proof of work","mining chain")+blk(20,150,"#7c3aed","Beacon Chain","proof of stake")+arrow(152,65,250,120)+arrow(152,195,250,140)+'<g transform="translate(260,80)"><rect width="180" height="90" rx="16" fill="url(#mg)"/><text x="90" y="40" text-anchor="middle" fill="#fff" font-weight="800" font-size="18">The Merge</text><text x="90" y="64" text-anchor="middle" fill="#fff" font-size="12">Sep 15, 2022</text></g><defs><linearGradient id="mg"><stop offset="0" stop-color="#627EEA"/><stop offset="1" stop-color="#ec4899"/></linearGradient></defs>'+arrow(445,125,510,125)+blk(520,80,"#10b981","Ethereum","staking only")
            cap = "Mining ends: one chain, secured by stake"
        return f'<svg viewBox="0 0 720 260" {t}>{defs}{body}<text x="360" y="252" text-anchor="middle" fill="currentColor" font-size="14">{cap}</text></svg>'
    if kind == "gavel":
        steps = [("Dec 2020","SEC sues","#ef4444"),("Jul 2023","Split ruling","#10b981"),("Aug 2024","$125M penalty","#f59e0b"),("Aug 2025","Appeals dropped","#7c3aed")]
        g = "".join(f'<g transform="translate({20+i*175},40)"><rect width="155" height="110" rx="18" fill="{c}"/><text x="78" y="45" text-anchor="middle" fill="#fff" font-weight="800" font-size="17">{a}</text><text x="78" y="72" text-anchor="middle" fill="#fff" font-size="14">{b}</text></g>' for i,(a,b,c) in enumerate(steps))
        return f'<svg viewBox="0 0 720 190" {t}>{g}<text x="360" y="182" text-anchor="middle" fill="currentColor" font-size="14">SEC v. Ripple Labs, Southern District of New York, 1:20-cv-10832</text></svg>'
    if kind == "megaphone":
        return f'''<svg viewBox="0 0 720 220" {t}>{defs}<g transform="translate(40,40)"><rect width="170" height="120" rx="22" fill="#C2A633"/><text x="85" y="55" text-anchor="middle" fill="#fff" font-weight="800" font-size="20">Post or event</text><text x="85" y="82" text-anchor="middle" fill="#fff" font-size="13">tweet, TV, meme</text></g>{arrow(220,100,280,100)}<g transform="translate(290,40)"><rect width="170" height="120" rx="22" fill="#ec4899"/><text x="85" y="55" text-anchor="middle" fill="#fff" font-weight="800" font-size="20">Attention</text><text x="85" y="82" text-anchor="middle" fill="#fff" font-size="13">new buyers rush in</text></g>{arrow(470,100,530,100)}<g transform="translate(540,40)"><rect width="150" height="120" rx="22" fill="#10b981"/><text x="75" y="55" text-anchor="middle" fill="#fff" font-weight="800" font-size="20">Spike</text><text x="75" y="82" text-anchor="middle" fill="#fff" font-size="13">then often a fade</text></g><text x="360" y="205" text-anchor="middle" fill="currentColor" font-size="14">DOGE's code barely changes, so attention drives most moves</text></svg>'''
    return ""
# ---------- page shell ----------
PAGES = {}; REPORT = []
SEARCH = []
NAV = [("coins/","coins","Coins"),("guides/","book-open","Guides"),("compare/","git-compare","Compare"),("glossary/","scroll-text","Glossary")]
def nfa(): return f'<div class="nfa">{icon("shield-alert")}<span><b>Not financial advice.</b> This is history and education only. We make no buy or sell recommendations and no price predictions.</span></div>'
def sources_box(srcs, extra_price=None):
    li = "".join(f'<li><a href="{e(u)}" rel="nofollow noopener" target="_blank">{e(t)}</a></li>' for t, u in srcs)
    if extra_price: li += "".join(f'<li>Price data: {e(p)}</li>' for p in extra_price)
    return f'<section class="sources reveal"><h2>{icon("link")}Sources</h2><ul>{li}</ul><p class="chk">Facts written in our own words. Last checked {UPDATED}.</p></section>'
def ld_article(path, title, desc):
    return {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"author":{"@type":"Organization","name":f"{BRAND} editorial team"},"publisher":{"@type":"Organization","name":BRAND},"datePublished":UPDATED_ISO,"dateModified":UPDATED_ISO,"mainEntityOfPage":ORIGIN+"/"+path}
def ld_crumbs(crumbs):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":ORIGIN+"/"+p} for i,(n,p) in enumerate(crumbs)]}
def page(path, title, desc, body, crumbs, srcs, ld=(), kind="page", primary_count=None, show_nfa=False):
    if kind!="year" and path: SEARCH.append({"t":title.split(" | ")[0],"u":path,"k":kind})
    if len(title) > 60:
        for _c in COINS.values():
            if _c["name"] in title and len(_c["name"])>14: title = title.replace(_c["name"], _c["sym"])
    if len(title) > 60: title = title.replace(" & Timeline","").replace(": Key Events",": Events")
    assert len(title) <= 60, (len(title), title)
    assert len(desc) <= 155, (len(desc), desc)
    R = "../" * path.count("/") or "./"
    crumbs = [("Home","")] + crumbs
    cr = " / ".join(f'<a href="{R}{p}">{e(n)}</a>' for n,p in crumbs[:-1]) + f' / <span>{e(crumbs[-1][0])}</span>' if len(crumbs) > 1 else ""
    lds = [ld_article(path, title, desc), ld_crumbs(crumbs)] + list(ld)
    text = re.sub(r"<[^>]+>", " ", re.sub(r"<(script|svg|style)[\s\S]*?</\1>", " ", body))
    words = len(text.split())
    prim = primary_count if primary_count is not None else sum(1 for t,u in srcs if "wikipedia.org" not in u)
    dated = bool(re.search(r"\b(19|20)\d\d\b", text))
    gate = words >= 300 and prim >= 2 and dated
    REPORT.append(dict(path="/"+path, words=words, primary_citations=prim, dated_facts=dated, passes_thin_gate=gate, indexable=INDEXABLE and gate))
    robots = "index,follow" if (INDEXABLE and gate) else "noindex,nofollow"
    navh = "".join(f'<a href="{R}{p}">{icon(i)}{n}</a>' for p,i,n in NAV)
    upd = f'<p class="upd">{icon("calendar")}Updated <time datetime="{UPDATED_ISO}">{UPDATED}</time></p>'
    html = f'''<!doctype html><html lang="en" data-root="{R}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="robots" content="{robots}"><meta name="googlebot" content="{robots}">
<meta name="ct-thin-gate" content="{'pass' if gate else 'thin'}"><link rel="canonical" href="{ORIGIN}/{path}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="article"><meta name="theme-color" content="#7c3aed">
<link rel="icon" href="{R}favicon.svg" type="image/svg+xml"><link rel="icon" href="{R}favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="{R}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;700;800&display=swap" rel="stylesheet">
<script>(function(){{try{{var s=localStorage.getItem('ct-theme'),h=new Date().getHours();document.documentElement.setAttribute('data-theme',s||((h>=19||h<7)?'dark':'light'))}}catch(e){{}}}})()</script>
<link rel="stylesheet" href="{R}assets/site.css?v={BUILD_V}">
{"".join('<script type="application/ld+json">'+json.dumps(x)+'</script>' for x in lds)}
</head><body>
<header class="top"><div class="wrap"><a class="brand" href="{R}">{LOGO}<span>Crypto<b>HistoryBook</b></span></a>
<nav class="main" aria-label="Main">{navh}</nav>
<form class="hsearch" role="search" action="{R}coins/" autocomplete="off"><label class="sr" for="q" hidden>Search</label>{icon("search")}<input id="q" type="search" name="q" placeholder="Search coins, events, guides" aria-label="Search the site" aria-autocomplete="list" aria-expanded="false"><ul class="sugg" role="listbox" hidden></ul></form>
<button class="thm menu-btn" type="button" aria-label="Menu">{icon("menu")}</button>
<button class="thm" type="button" aria-label="Switch light or dark mode" onclick="var d=document.documentElement,t=d.getAttribute('data-theme')=='dark'?'light':'dark';d.setAttribute('data-theme',t);try{{localStorage.setItem('ct-theme',t)}}catch(e){{}}">{icon("moon","ic i-moon")}{icon("sun","ic i-sun")}</button></div></header>
<main class="wrap">{('<nav class="crumb" aria-label="Breadcrumb">'+cr+'</nav>') if cr else ''}
{nfa() if show_nfa else ''}{body}
{upd}{sources_box(srcs) if srcs else ''}
<div class="ad-slot" data-ad-slot="{kind}-bottom" hidden aria-hidden="true"></div>
<aside class="affiliate" data-affiliate="exchanges" hidden><p class="small">Disclosure: links in this box are affiliate links; we may earn a commission.</p><!-- exchange links go here with rel="sponsored nofollow" --></aside>
</main>
<footer><div class="wrap"><div class="cols"><div><a class="brand" href="{R}">{LOGO}<span>Crypto<b>HistoryBook</b></span></a><p><b>Not financial advice.</b> CryptoHistoryBook is a history and education site. Nothing here is a recommendation to buy, sell or hold any asset, and we make no price predictions. Prices are historical daily closes from the named exchange and date shown.</p><p>Last checked {UPDATED}.</p></div>
<div><h4>Coins</h4>{"".join(f'<a href="{R}{k["slug"]}/">{k["name"]}</a>' for k in COINS.values())}</div>
<div><h4>Learn</h4><a href="{R}guides/">Guides</a><a href="{R}compare/">Comparisons</a><a href="{R}glossary/">Glossary</a><a href="{R}sources/">Data sources</a></div>
<div><h4>About</h4><a href="{R}about/">About</a><a href="{R}privacy/">Privacy</a><a href="{R}#newsletter">Newsletter</a></div></div>
<p class="small">Icons by Lucide (ISC license). Coin marks are simplified drawings of trademarks of their respective projects.</p></div></footer>
<script>window.CHB_V="{BUILD_V}"</script><script src="{R}assets/site.js?v={BUILD_V}" defer></script>
</body></html>'''
    html = html.replace("__R__", R)
    assert "\u2014" not in html and "\u2013" not in html, path
    PAGES[path] = html
# Newsletter provider. Keep enabled False until the Kit account and form exist.
NEWSLETTER = {"enabled": False, "provider": "kit", "form_id": ""}
def newsletter():
    nl = NEWSLETTER
    live = nl["enabled"] and nl["form_id"].strip().isdigit()
    head = f'''<section class="news reveal" id="newsletter"><h2 style="margin-top:0;color:#fff">{icon("mail")} The CryptoHistoryBook Letter</h2><p>One short email when we add a new timeline or explainer. No hype, no tips.</p>'''
    if not live:
        return head + f'''<form class="nl" novalidate><label class="sr" for="nl-email" hidden>Email</label><input id="nl-email" name="email" type="email" placeholder="you@example.com" autocomplete="email" required><button class="btn w" type="submit">{icon("sparkles")}Join the list</button><div class="msg" role="status" style="width:100%"></div></form><p class="small" style="color:rgba(255,255,255,.85)">Your email is saved only in this browser for now. Nothing is sent anywhere yet.</p></section>'''
    act = f"https://app.kit.com/forms/{nl['form_id'].strip()}/subscriptions"
    return head + f'''<iframe name="nl-frame" title="Newsletter signup" hidden style="display:none"></iframe><form class="nl" data-live="1" action="{act}" method="post" target="nl-frame" novalidate><label class="sr" for="nl-email" hidden>Email</label><input id="nl-email" name="email_address" type="email" placeholder="you@example.com" autocomplete="email" required><button class="btn w" type="submit">{icon("sparkles")}Join the list</button><label class="small" style="width:100%;display:flex;gap:8px;align-items:flex-start;color:rgba(255,255,255,.92)"><input type="checkbox" name="consent" value="yes" required style="margin-top:3px"> <span>I agree to receive The CryptoHistoryBook Letter from Atulit LLC by email. Unsubscribe anytime with one click. See our <a href="__R__privacy/" style="color:#fff">privacy policy</a>.</span></label><div class="msg" role="status" style="width:100%"></div></form><p class="small" style="color:rgba(255,255,255,.85)">You will get a confirmation email first. Your address is stored with our email provider, Kit, and is never sold.</p></section>'''
def ev_js(c, evs, focus=None, R=""):
    out = []
    for x in evs:
        out.append(dict(name=x["name"], date=x["date"], dlabel=mdate(x["date"]), kind=x["kind"], price=x["price"], psrc=plabel(c, x["date"]) if x["price"] else "", summary=x["summary"], url=R+evpath(x), focus=x is focus))
    return e(json.dumps(out))
def chartbox(c, evs, R, mini=False, frm="", to="", focus=None, log=None):
    k = COINS[c]; d = SER[c]
    log = (not mini) if log is None else log
    segs = "; ".join(f'{g["source"]} {g["pair"]} daily closes {g["from"]} to {g["to"]}' for g in d["segments"])
    ctr = "" if mini else '<span class="seg">' + "".join(f'<button type="button" data-range="{r}" class="{"on" if r=="all" else ""}">{l}</button>' for r,l in [("all","All"),("5","5Y"),("1","1Y")]) + '</span>'
    return f'''<div class="chartbox reveal"><div class="chartbar"><b style="font-family:Space Grotesk">{icon("chart-spline")} {k["name"]} price, USD</b><span style="flex:1"></span>{ctr}<span class="seg"><button type="button" data-log class="{"on" if log else ""}">Log scale: {"on" if log else "off"}</button></span></div>
<div class="chart{" mini" if mini else ""}" data-coin="{c}" data-color="{k["color"]}" data-color2="{k["color2"]}" data-log="{1 if log else 0}" data-from="{frm}" data-to="{to}" data-events="{ev_js(c, evs, focus, R)}" role="img" aria-label="{k["name"]} daily closing price chart with event markers"></div>
<div class="legend">{"".join(f'<span><i style="background:{v}"></i>{n}</span>' for n,v in KC.items())}</div>
<p class="src">{icon("info")}<span>Source: {e(segs)}. Fetched {UPDATED} from free public APIs. Click a dot for the event and its price on that day.</span></p></div>'''
def tl_ol(evs, R, cls="tl"):
    li = []
    for x in evs:
        p = f' <span class="small">{fmt(x["price"])} ({e(plabel(x["coin"], x["date"]))})</span>' if x["price"] else ""
        li.append(f'<li class="reveal"><span class="dot" style="background:{KC[x["kind"]]}">{icon(KI[x["kind"]])}</span><a class="ev" href="{R}{evpath(x)}"><span class="d">{mdate(x["date"])}</span><span class="kind" style="background:{KC[x["kind"]]}">{x["kind"]}</span><br><b>{e(x["name"])}</b>{p}<br><span class="small">{e(x["summary"])}</span></a></li>')
    return f'<ol class="{cls}">{"".join(li)}</ol>'
def itemlist(name, items):
    return {"@context":"https://schema.org","@type":"ItemList","name":name,"itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"url":ORIGIN+"/"+p} for i,(n,p) in enumerate(items)]}
def faq_html(faq):
    return '<section class="faq"><h2>Questions</h2>' + "".join(f'<details open><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in faq) + '</section>'
def faq_ld(faq): return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
def linkify(R, paths):
    out = []
    for p in paths:
        t = EVBY[p]["name"] + " (" + mdate(EVBY[p]["date"]) + ")" if p in EVBY else TITLES.get(p, p)
        out.append(f'<a class="card" href="{R}{p}" style="padding:14px 18px">{icon("arrow-right")} {e(t)}</a>')
    return '<div class="grid g2">' + "".join(out) + '</div>'
TITLES = {}
for k in COINS.values(): TITLES[k["slug"]+"/"] = k["name"]+" hub"; TITLES[k["slug"]+"/history/"] = k["name"]+" timeline"
for a in ARTICLES: TITLES[a["path"]] = a["h1"]
for g in GLOSSARY: TITLES["glossary/"+g[0]+"/"] = "Glossary: "+g[1]
for cp in COMPARES: TITLES["compare/"+cp["slug"]+"/"] = cp["title"].split(":")[0]
def trim_title(*opts):
    for t in opts:
        if len(t) <= 60: return t
    return opts[-1][:60]
# ---------- coin pages ----------
for c, k in COINS.items():
    s = k["slug"]; evs = k["events"]; years = sorted({x["year"] for x in evs})
    last = SER[c]["points"][-1]
    # hub
    R = "../"
    facts = "".join(f'<div class="fact"><span>{e(a)}</span><b>{e(b)}</b></div>' for a,b in k["facts"])
    yl = "".join(f'<a href="{R}{s}/history/{y}/">{y}</a>' for y in years)
    rel_cmp = [cp for cp in COMPARES if c in (cp["a"], cp["b"])]
    body = f'''<section class="hero" style="background:linear-gradient(135deg,{k["color"]},{k["color2"]})"><span class="blob" style="width:260px;height:260px;background:#fff;left:-60px;top:-60px"></span>{hero_art(c)}<div class="inner"><span class="chip">{coinlogo(c,"ic")} {k["sym"]}</span><h1>{k["name"]}: history, founders and key events</h1><p class="lede">From {k.get("founded_label") or mdate(k["founded"])} to today, every major rally, crash and upgrade, each with a dated, sourced price.</p><a class="btn w" href="{R}{s}/history/">{icon("history")}Open the interactive timeline</a></div></section>
<div class="stats"><div class="stat reveal" style="background:{k["color"]}"><b data-count="{len(evs)}">{len(evs)}</b><span>dated events</span></div><div class="stat reveal" style="background:#7c3aed"><b data-count="{len(years)}">{len(years)}</b><span>years covered</span></div><div class="stat reveal" style="background:#ec4899"><b data-count="{len(SER[c]["points"])}">{len(SER[c]["points"])}</b><span>daily closes charted</span></div><div class="stat reveal" style="background:#0ea5e9"><b data-count="{sum(len(x["sources"]) for x in evs)}">{sum(len(x["sources"]) for x in evs)}</b><span>source links</span></div></div>
<p class="small">Latest close in our data: <b>{fmt(last[1])}</b> ({e(plabel(c,last[0]))}).</p>
<div class="facts">{facts}</div>
<section class="prose reveal"><h2>Origin story</h2>{"".join(f"<p>{e(p)}</p>" for p in k["origin"])}<p><b>Founders:</b> {e(k["founders"])}.</p></section>
{chartbox(c, evs, R)}
<h2>Browse by year</h2><div class="yearlist">{yl}</div>
<h2>Key events</h2>{tl_ol(evs, R)}
{('<h2>Compare</h2>'+linkify(R, ["compare/"+cp["slug"]+"/" for cp in rel_cmp])) if rel_cmp else ''}'''
    srcs = k["primary"] + ([] if "wiki" in k else [("Wikipedia: "+k["name"], f"https://en.wikipedia.org/wiki/{ {'xrp':'Ripple_Labs','sol':'Solana_(blockchain_platform)'}.get(c,k['name'])}")])
    page(f"{s}/", trim_title(f"{k['name']} History: Founders, Key Events & Prices", f"{k['name']} History and Key Events"), f"{k['name']} history from launch to today: origin story, founders, and every major event with a sourced daily close price.", body, [(k["name"], f"{s}/")], srcs, kind="hub", show_nfa=True)
    # timeline
    R = "../../"
    body = f'''<section class="hero" style="background:linear-gradient(135deg,{k["color"]},{k["color2"]})">{hero_art(c)}<div class="inner"><span class="chip">{icon("history")} Interactive timeline</span><h1>{k["name"]} timeline</h1><p class="lede">{len(evs)} dated events on a price chart. Toggle log scale, change the range and click any dot.</p></div></section>
{chartbox(c, evs, R)}
<h2>All events, in order</h2>{tl_ol(evs, R)}
<h2>Years</h2><div class="yearlist">{"".join(f'<a href="{R}{s}/history/{y}/">{y}</a>' for y in years)}</div>
<p><a href="{R}{s}/">{icon("arrow-left")} Back to the {k["name"]} hub</a></p>'''
    page(f"{s}/history/", trim_title(f"{k['name']} Timeline: Every Key Event With Prices", f"{k['name']} Timeline: Key Events"), f"Interactive {k['name']} timeline: {len(evs)} key events from {evs[0]['year']} to {evs[-1]['year']}, each with a sourced daily close where data exists.", body, [(k["name"], f"{s}/"),("Timeline", f"{s}/history/")], k["primary"], ld=[itemlist(f"{k['name']} timeline", [(x["name"], evpath(x)) for x in evs]), itemlist(f"{k['name']} years", [(y, f"{s}/history/{y}/") for y in years])], kind="timeline", show_nfa=True)
    # years
    for y in years:
        R = "../../../"; ye = [x for x in evs if x["year"] == y]
        pts = [p for p in SER[c]["points"] if p[0].startswith(y)]
        stats = ""
        if pts:
            hi = max(pts, key=lambda p:p[1]); lo = min(pts, key=lambda p:p[1])
            stats = f'<div class="facts"><div class="fact"><span>First close of {y}</span><b>{fmt(pts[0][1])}</b><span class="small">{e(plabel(c,pts[0][0]))}</span></div><div class="fact"><span>Highest close</span><b>{fmt(hi[1])}</b><span class="small">{e(plabel(c,hi[0]))}</span></div><div class="fact"><span>Lowest close</span><b>{fmt(lo[1])}</b><span class="small">{e(plabel(c,lo[0]))}</span></div><div class="fact"><span>Last close of {y}</span><b>{fmt(pts[-1][1])}</b><span class="small">{e(plabel(c,pts[-1][0]))}</span></div></div>'
        intro = YEAR_INTRO.get((c,y), f"Here is what happened to {k['name']} in {y}, in date order, with the daily close from our price data where it covers the date.")
        detail = "".join(f'<h3><a href="{R}{evpath(x)}">{e(x["name"])}</a> <span class="small">{mdate(x["date"])}</span></h3>' + "".join(f"<p>{e(p)}</p>" for p in x["body"][:1]) for x in ye)
        body = f'''<section class="hero" style="background:linear-gradient(135deg,{k["color"]},{k["color2"]});padding:40px">{hero_art(c)}<div class="inner"><span class="chip">{coinlogo(c,"ic")} {y}</span><h1>{k["name"]} in {y}</h1><p class="lede">{len(ye)} key event{"s" if len(ye)>1 else ""} this year.</p></div></section>
<section class="prose"><p>{e(intro)}</p></section>{stats}
{chartbox(c, ye, R, mini=True, frm=y+"-01-01", to=y+"-12-31", log=False) if len(pts)>20 else '<p class="small">Our price data does not cover this year, so no chart or prices are shown.</p>'}
<h2>Events in {y}</h2>{tl_ol(ye, R)}
<section class="prose">{detail}</section>
<p><a href="{R}{s}/">{icon("arrow-left")} {k["name"]} hub</a> &middot; <a href="{R}{s}/history/">Full timeline</a></p>'''
        srcs = []; [srcs.append(z) for x in ye for z in x["sources"] if z not in srcs]
        page(f"{s}/history/{y}/", f"{k['name']} in {y}: Key Events & Timeline", f"What happened to {k['name']} in {y}: {', '.join(x['name'] for x in ye)}"[:150].rstrip(", ")+".", body, [(k["name"], f"{s}/"),("Timeline", f"{s}/history/"),(y, f"{s}/history/{y}/")], srcs, ld=[itemlist(f"{k['name']} in {y}", [(x["name"], evpath(x)) for x in ye])], kind="year", show_nfa=True)
    # events
    for x in evs:
        R = "../../../"; p = evpath(x)
        pc = f'<div class="pricecard reveal" style="background:linear-gradient(135deg,{k["color"]},{k["color2"]})">{icon("chart-line")}<div><span class="small">{k["sym"]} close on {mdate(x["date"])}</span><br><b>{fmt(x["price"])}</b><br><span class="small">Source: {e(plabel(c,x["date"]))}</span></div></div>' if x["price"] else f'<div class="nfa">{icon("info")}<span>No price shown: our sourced price data for {k["name"]} does not cover {mdate(x["date"])}.</span></div>'
        d0 = dt.date.fromisoformat(x["date"]); frm = (d0 - dt.timedelta(days=180)).isoformat(); to = (d0 + dt.timedelta(days=180)).isoformat()
        has = x["price"] is not None
        pn = '<div class="pn">' + (f'<a class="card" href="{R}{evpath(x["prev"])}"><span class="small">{icon("chevron-left")} Previous</span><br><b>{e(x["prev"]["name"])}</b></a>' if x["prev"] else "<span></span>") + (f'<a class="card r" href="{R}{evpath(x["next"])}"><span class="small">Next {icon("chevron-right")}</span><br><b>{e(x["next"]["name"])}</b></a>' if x["next"] else "<span></span>") + '</div>'
        extra = [a["path"] for a in ARTICLES if p in a.get("related", [])] + ["compare/"+cp["slug"]+"/" for cp in COMPARES if p in cp["events"]] + ["glossary/"+g[0]+"/" for g in GLOSSARY if p in g[3]]
        body = f'''<section class="hero" style="background:linear-gradient(135deg,{KC[x["kind"]]},{k["color"]})">{hero_art(c)}<div class="inner"><span class="chip">{icon(KI[x["kind"]])} {x["kind"].title()} &middot; {mdate(x["date"])}</span><h1>{e(x["name"])}</h1><p class="lede">{e(x["summary"])}</p></div></section>
{pc}<section class="prose reveal">{"".join(f"<p>{e(q)}</p>" for q in x["body"])}</section>
{chartbox(c, evs, R, mini=True, frm=frm, to=to, focus=x, log=False) if has else ''}
{('<h2>Related</h2>'+linkify(R, extra)) if extra else ''}
<p>{icon("calendar")} Part of <a href="{R}{s}/history/{x["year"]}/">{k["name"]} in {x["year"]}</a> &middot; <a href="{R}{s}/history/">full {k["name"]} timeline</a> &middot; <a href="{R}{s}/">{k["name"]} hub</a></p>{pn}'''
        dl = mdate(x["date"])
        title = x.get("title") or trim_title(f'{x["name"]} ({dl}): What Happened to {k["name"]}', f'{x["name"]} ({dl}): {k["name"]}', f'{x["name"]} ({dl})')
        desc = x["summary"] + (f' {k["sym"]} closed at {fmt(x["price"])} that day ({seg_of(c,x["date"])["source"]}).' if x["price"] else "")
        if len(desc) > 155: desc = x["summary"]
        evld = {"@context":"https://schema.org","@type":"Event","name":x["name"],"startDate":x["date"],"description":x["summary"],"eventStatus":"https://schema.org/EventScheduled","eventAttendanceMode":"https://schema.org/OnlineEventAttendanceMode","location":{"@type":"VirtualLocation","url":ORIGIN+"/"+p}}
        page(p, title, desc, body, [(k["name"], f"{s}/"),(x["year"], f"{s}/history/{x['year']}/"),(x["name"], p)], x["sources"], ld=[evld], kind="event", show_nfa=True)
# ---------- articles ----------
for a in ARTICLES:
    p = a["path"]; R = "../" * p.count("/")
    secs = "".join(f'<h2>{e(h)}</h2>' + "".join(f"<p>{e(q)}</p>" for q in ps) for h, ps in a["sections"])
    extra = ""
    if a.get("muskline"):
        mev = [x for x in COINS["doge"]["events"] if "musk" in (x["name"]+x["summary"]+" ".join(x["body"])).lower()]
        extra = chartbox("doge", mev, R, log=True) + "<h2>The timeline</h2>" + tl_ol(mev, R)
    if a.get("outages"):
        oev = [x for x in COINS["sol"]["events"] if x["kind"] == "outage"]
        extra = chartbox("sol", oev, R, log=False) + "<h2>Major outages</h2>" + tl_ol(oev, R)
    col = {"guide":"#0ea5e9","explainer":"#ec4899","upgrade":"#F7931A","question":"#627EEA"}[a["section"]]
    body = f'''<section class="hero" style="background:linear-gradient(135deg,{col},#7c3aed)">{hero_art()}<div class="inner"><span class="chip">{icon(a.get("icon","book-open"))} {a["section"].title()}</span><h1>{e(a["h1"])}</h1><p class="lede">{e(a["desc"])}</p></div></section>
{('<div class="diagram reveal">'+diagram(a["diagram"])+'</div>') if a.get("diagram") else ''}<section class="prose">{secs}</section>{extra}
{faq_html(a["faq"]) if a.get("faq") else ''}<h2>Related</h2>{linkify(R, a["related"])}'''
    sec_name = {"guide":("Guides","guides/"),"explainer":("Guides","guides/"),"upgrade":("Guides","guides/"),"question":("Guides","guides/")}[a["section"]]
    page(p, a["title"], a["desc"], body, [sec_name, (a["h1"], p)], a["sources"], ld=[faq_ld(a["faq"])] if a.get("faq") else [], kind=a["section"], show_nfa=a["section"]!="guide")
# glossary
for slug, term, short, paras, rel, srcs in GLOSSARY:
    p = f"glossary/{slug}/"; R = "../../"
    body = f'''<section class="hero" style="padding:38px"><div class="inner"><span class="chip">{icon("scroll-text")} Glossary</span><h1>{e(term)}</h1><p class="lede">{e(short)}</p></div></section><section class="prose">{"".join(f"<p>{e(q)}</p>" for q in paras)}</section><h2>See it in the timelines</h2>{linkify(R, rel)}'''
    page(p, f"What Is {term}? Crypto Glossary"[:60] if len(f"What Is {term}? Crypto Glossary")<=60 else f"{term}: Crypto Glossary", short[:155], body, [("Glossary","glossary/"),(term,p)], srcs, kind="glossary")
# compare
for cp in COMPARES:
    p = f"compare/{cp['slug']}/"; R = "../../"; A, B = COINS[cp["a"]], COINS[cp["b"]]
    rows = "".join(f"<tr><th>{e(r[0])}</th><td>{e(r[1])}</td><td>{e(r[2])}</td></tr>" for r in cp["rows"])
    la, lb = SER[cp["a"]]["points"][-1], SER[cp["b"]]["points"][-1]
    body = f'''<section class="hero" style="background:linear-gradient(135deg,{A["color"]},{B["color"]})"><div class="inner"><span class="chip">{icon("git-compare")} Comparison</span><div class="vs">{coinlogo(cp["a"])}<b>vs</b>{coinlogo(cp["b"])}</div><h1 style="text-align:center;margin:auto">{A["name"]} vs {B["name"]}{" for "+cp["use"] if cp["use"] not in ("Store of Value","Everyday Use") else ""}</h1></div></section>
<table class="cmp reveal"><thead><tr><th style="background:#334155">Feature</th><th style="background:{A["color"]}">{A["name"]}</th><th style="background:{B["color"]}">{B["name"]}</th></tr></thead><tbody>{rows}<tr><th>Latest close in our data</th><td>{fmt(la[1])}<br><span class="small">{e(plabel(cp["a"],la[0]))}</span></td><td>{fmt(lb[1])}<br><span class="small">{e(plabel(cp["b"],lb[0]))}</span></td></tr></tbody></table>
<section class="prose"><h2>The trade-offs</h2>{"".join(f"<p>{e(q)}</p>" for q in cp["text"])}<p>Neither column is a recommendation. Each network makes different choices, and the history pages show how those choices played out.</p></section>
<div class="grid g2">{chartbox(cp["a"], A["events"], R, mini=True)}{chartbox(cp["b"], B["events"], R, mini=True)}</div>
<h2>Related events and hubs</h2>{linkify(R, cp["events"] + [A["slug"]+"/", B["slug"]+"/"])}'''
    t = cp["title"] if "for" not in cp["slug"] else trim_title(f'{A["name"]} vs {B["name"]} for {cp["use"]}: Fees, Speed, Trade-offs', cp["title"])
    page(p, t, cp["desc"], body, [("Compare","compare/"),(f'{A["name"]} vs {B["name"]}', p)], cp["sources"], kind="compare", show_nfa=True)

def rank(c): return (MKT.get(COINS[c]["cgid"]) or {}).get("market_cap_rank") or 999
ORDER = sorted(COINS, key=rank)
CATS = []
for _c in ORDER:
    for _t in COINS[_c]["cats"]:
        if _t not in CATS: CATS.append(_t)
def coin_index(R, limit=None):
    chips = '<button type="button" class="cchip on" data-cat="">All</button>' + "".join(f'<button type="button" class="cchip" data-cat="{e(t)}">{e(t)}</button>' for t in CATS)
    items = []
    for c in ORDER:
        k = COINS[c]; last = SER[c]["points"][-1]
        items.append(f'<a class="card cgi reveal" href="{R}{k["slug"]}/" data-name="{e((k["name"]+" "+k["sym"]).lower())}" data-cats="{e("|".join(k["cats"]))}"><span class="bar" style="background:linear-gradient(90deg,{k["color"]},{k["color2"]})"></span><div class="top">{coinlogo(c)}<div><b>{e(k["name"])}</b><br><span class="small">#{rank(c)} &middot; {k["sym"]}</span></div></div><div class="tags">{"".join(f'<span class="chip k">{e(t)}</span>' for t in k["cats"])}</div><span class="small">{len(k["events"])} events &middot; last close {fmt(last[1])} ({e(plabel(c,last[0]))})</span></a>')
    return f'''<div class="cfilter"><label class="search">{icon("search")}<input id="coin-q" type="search" placeholder="Search {len(ORDER)} coins by name or ticker" aria-label="Search coins"></label><div class="chips">{chips}</div></div><div class="grid g4 cgrid">{"".join(items)}</div><p class="small cnone" hidden>No coins match that search.</p><p class="small">{icon("info")} Ranking: top coins by market cap from the <a href="https://docs.coingecko.com/reference/coins-markets" rel="nofollow">CoinGecko /coins/markets</a> public API, fetched {UPDATED}, excluding stablecoins, wrapped or staked tokens, tokenized funds and coins we could not source well. Ranks show CoinGecko's position.</p>'''
# ---------- index pages ----------
def cardlist(R, items, colors=("#7c3aed","#ec4899","#f97316","#0ea5e9","#10b981")):
    return '<div class="grid g3">' + "".join(f'<a class="card reveal" href="{R}{p}"><span class="ibox" style="background:{colors[i%len(colors)]}">{icon(ic)}</span><h3>{e(t)}</h3><p class="small">{e(d)}</p></a>' for i,(p,ic,t,d) in enumerate(items)) + '</div>'
R = "../"
gl = [(a["path"], a.get("icon","book-open"), a["h1"], a["desc"]) for a in ARTICLES]
page("coins/", f"All Coins: {len(ORDER)} Crypto Timelines and Histories", f"Browse {len(ORDER)} crypto histories: hubs, timelines and dated, sourced events for the top coins by market cap as of {UPDATED}.",
     nfa()+f'<section class="hero"><div class="inner"><span class="chip">{icon("coins")} {len(ORDER)} coins</span><h1>Every coin, every timeline</h1><p class="lede">The top coins by market cap, each with an origin story, a clickable price chart and sourced events.</p></div>{hero_art()}</section>' + coin_index("../"), [("Coins","coins/")], [("CoinGecko /coins/markets API","https://docs.coingecko.com/reference/coins-markets")], ld=[itemlist("Coins", [(COINS[c]["name"], COINS[c]["slug"]+"/") for c in ORDER])], kind="index")
page("guides/", "Crypto Guides and Explainers for Beginners", "Plain English crypto guides: what crypto is, wallets, how blockchains work, hard forks, SegWit, the Merge, XRP vs SEC and why DOGE pumps.",
     f'<section class="hero"><div class="inner"><span class="chip">{icon("book-open")} Learn</span><h1>Guides and explainers</h1><p class="lede">Start with the basics, then dig into the big stories.</p></div>{hero_art()}</section>{cardlist(R, gl)}', [("Guides","guides/")], [W for W in [("ethereum.org: learn","https://ethereum.org/en/learn/"),("bitcoin.org: getting started","https://bitcoin.org/en/getting-started")]], ld=[itemlist("Guides", [(a["h1"],a["path"]) for a in ARTICLES])], kind="index")
page("glossary/", "Crypto Glossary: Halving, Forks, Staking", "Short definitions of crypto terms like halving, hard fork, soft fork, proof of work and proof of stake, linked to real events.",
     f'<section class="hero"><div class="inner"><span class="chip">{icon("scroll-text")} Glossary</span><h1>Crypto glossary</h1><p class="lede">Every term links to the moments in history where it mattered.</p></div></section>{cardlist(R, [("glossary/"+g[0]+"/","scroll-text",g[1],g[2]) for g in GLOSSARY])}', [("Glossary","glossary/")], [("ethereum.org glossary","https://ethereum.org/en/glossary/"),("bitcoin.org vocabulary","https://bitcoin.org/en/vocabulary")], ld=[itemlist("Glossary", [(g[1],"glossary/"+g[0]+"/") for g in GLOSSARY])], kind="index")
page("compare/", "Coin vs Coin Comparisons: Fees, Speed, Supply", "Side by side comparisons of Bitcoin, Ethereum, XRP, Dogecoin and Solana: consensus, supply, speed and fees, with links to the history.",
     nfa()+f'<section class="hero"><div class="inner"><span class="chip">{icon("git-compare")} Compare</span><h1>Coin vs coin</h1><p class="lede">Facts side by side. No winners picked.</p></div></section><div class="grid g2">' + "".join(f'<a class="card reveal" href="{R}compare/{cp["slug"]}/"><div class="vs">{coinlogo(cp["a"])}<b>vs</b>{coinlogo(cp["b"])}</div><h3 style="text-align:center">{e(TITLES["compare/"+cp["slug"]+"/"])}</h3><p class="small" style="text-align:center">{e(cp["desc"])}</p></a>' for cp in COMPARES) + '</div>', [("Compare","compare/")], [], ld=[itemlist("Comparisons", [(TITLES["compare/"+cp["slug"]+"/"],"compare/"+cp["slug"]+"/") for cp in COMPARES])], kind="index")
srcs_rows = "".join(f'<tr><th>{COINS[c]["name"]}</th><td>' + "<br>".join(f'{e(g["source"])} {e(g["pair"])}, {g["from"]} to {g["to"]} (<a href="{e(g["url"])}" rel="nofollow">API docs</a>)' for g in SER[c]["segments"]) + f'</td><td>{len(SER[c]["points"])}</td></tr>' for c in COINS)
page("sources/", "Data Sources and Methods", "Where CryptoHistoryBook gets its prices: free public daily close data from Bitstamp, Coinbase Exchange and Binance, fetched Oct 14, 2026.",
     f'<h1>Data sources and methods</h1><section class="prose"><p>Every price on this site is a daily close (UTC) taken from a free, public exchange API at build time on {UPDATED}. We use one exchange per day, preferring the earliest continuous USD market for each coin, and fill earlier days from Binance USDT pairs only where no USD series was available. Each price shows the exchange, pair and date it came from. When our data does not cover a date, we show no price rather than an estimate.</p><p>Event facts are written in our own words and link to primary sources such as whitepapers, BIPs and EIPs, SEC filings, court dockets, official project blogs and block explorers, plus Wikipedia for background.</p></section><table class="cmp"><thead><tr><th style="background:#334155">Coin</th><th style="background:#7c3aed">Series</th><th style="background:#ec4899">Days</th></tr></thead><tbody>{srcs_rows}</tbody></table>', [("Data sources","sources/")], [("Bitstamp API","https://www.bitstamp.net/api/"),("Coinbase Exchange API","https://docs.cdp.coinbase.com/exchange/"),("Binance Spot API","https://developers.binance.com/docs/binance-spot-api-docs/rest-api")], kind="page")
page("about/", "About CryptoHistoryBook", "CryptoHistoryBook explains crypto history with dated, sourced events and charts. It is education only and not financial advice.",
     f'<h1>About CryptoHistoryBook</h1><section class="prose"><p>CryptoHistoryBook turns the history of major cryptocurrencies into timelines you can click through. Each event is dated, written in our own words and linked to its sources. Each price is a historical daily close from a named exchange.</p><p>We do not give investment advice, rate coins or predict prices. We do not accept payment to cover a project.</p></section>', [("About","about/")], [], kind="page")
NL_PRIV = ("If you join The CryptoHistoryBook Letter, your email address and consent are stored with our email provider, Kit (kit.com), used only to send the letter, and never sold. Every email has a one click unsubscribe link." if NEWSLETTER["enabled"] and NEWSLETTER["form_id"].strip().isdigit() else "If you join the newsletter, your email is stored only in your browser\'s local storage. Nothing is sent to us yet.")
page("privacy/", "Privacy Policy", "CryptoHistoryBook uses first party page view analytics and stores newsletter signups only in your browser. No ads or third party trackers.",
     f'<h1>Privacy policy</h1><section class="prose"><p>Last updated {UPDATED}.</p><p>We use first party, cookie based page view analytics: two cookies, atulit_vid (a random visitor id) and atulit_sid (a random visit id that resets after 30 minutes of inactivity), record which pages are viewed. The data goes only to our own analytics server. There are no ads and no third party trackers.</p><p>{NL_PRIV} Your theme choice is also saved in local storage.</p></section>', [("Privacy","privacy/")], [], kind="page")
# home
R = "./"
cc = "".join(f'''<a class="card coincard reveal" href="{k["slug"]}/"><span class="bar" style="background:linear-gradient(90deg,{k["color"]},{k["color2"]})"></span><div class="top">{coinlogo(c)}<div><h3 style="margin:0">{k["name"]}</h3><span class="small">{k["sym"]} &middot; {len(k["events"])} events</span></div></div><svg class="spark" viewBox="0 0 200 56" preserveAspectRatio="none" data-coin="{c}" data-color="{k["color"]}"></svg><span class="px">{fmt(SER[c]["points"][-1][1])}</span><br><span class="small">{e(plabel(c,SER[c]["points"][-1][0]))}</span></a>''' for c,k in COINS.items())
feat = [("guides/xrp-vs-sec-explained/","scale","XRP vs SEC, explained","The five year case in four steps."),("guides/why-doge-pumps/","rocket","Why DOGE pumps","Memes, Musk and momentum."),("how-did-the-merge-affect-ethereum/","merge","How the Merge affected Ethereum","Energy, supply and what did not change."),("bitcoin/events/2024-spot-etf-approval/","landmark","Spot bitcoin ETFs","The Jan 10, 2024 approval."),("solana/outage-history/","power-off","Solana outage history","Every major halt, 2021 to 2024."),("dogecoin/elon-musk-tweet-timeline/","message-circle","Musk and Dogecoin","The tweet timeline with prices.")]
basics = [("guides/what-is-crypto/","sparkles","What is crypto?","The two minute version."),("guides/crypto-wallets/","wallet","Wallets, explained","Keys, custody and safety."),("guides/how-blockchains-work/","blocks","How blockchains work","Blocks, hashes and consensus.")]
nev = len(EVENTS); npts = sum(len(SER[c]["points"]) for c in COINS); nsrc = len({u for x in EVENTS for t,u in x["sources"]})
body = f'''<section class="hero" style="padding:70px 48px"><span class="blob" style="width:300px;height:300px;background:#fde68a;right:10%;top:-80px"></span><span class="blob" style="width:240px;height:240px;background:#38bdf8;left:-60px;bottom:-60px;animation-delay:-4s"></span>{hero_art()}<div class="inner"><span class="chip">{icon("history")} Crypto history, made clickable</span><h1>Every big crypto moment, on one timeline.</h1><p class="lede">Rallies, crashes, forks and court fights for the top 100 coins, from Bitcoin to the newest chains. Each one dated, sourced and pinned to the real price that day.</p><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn w" href="bitcoin/history/">{icon("chart-spline")}Explore the Bitcoin timeline</a><a class="btn o" href="guides/what-is-crypto/" style="color:#fff">{icon("book-open")}New to crypto?</a></div></div></section>
<div class="stats"><div class="stat reveal" style="background:#7c3aed"><b data-count="{nev}">{nev}</b><span>dated events</span></div><div class="stat reveal" style="background:#ec4899"><b data-count="{npts}">{npts}</b><span>daily closes charted</span></div><div class="stat reveal" style="background:#f97316"><b data-count="{nsrc}">{nsrc}</b><span>sources cited</span></div><div class="stat reveal" style="background:#0ea5e9"><b data-count="5">5</b><span>coin timelines</span></div></div>
<h2>Pick a coin</h2><div class="grid g5">{cc}</div>
<h2>All {len(ORDER)} coins</h2>{coin_index("./")}
{chartbox("btc", COINS["btc"]["events"], R)}
<h2>Big stories, explained</h2>{cardlist(R, feat)}
<h2>Start with the basics</h2>{cardlist(R, basics, ("#0ea5e9","#10b981","#7c3aed"))}
<h2>Compare coins</h2><div class="grid g2">{"".join(f'<a class="card reveal" href="compare/{cp["slug"]}/" style="display:flex;align-items:center;gap:14px">{coinlogo(cp["a"])}{coinlogo(cp["b"])}<b>{e(TITLES["compare/"+cp["slug"]+"/"])}</b></a>' for cp in COMPARES)}</div>
{newsletter()}'''
page("", "CryptoHistoryBook: Crypto History, Timelines and Guides", "Interactive timelines of the top 100 crypto coins: dated events, sourced historical prices and plain English guides.", body, [], [("Bitcoin whitepaper","https://bitcoin.org/bitcoin.pdf"),("Ethereum upgrade history","https://ethereum.org/en/history/"),("SEC v. Ripple docket","https://www.courtlistener.com/docket/19857399/securities-and-exchange-commission-v-ripple-labs-inc/")], ld=[itemlist("Coin timelines", [(k["name"]+" timeline", k["slug"]+"/history/") for k in COINS.values()])], kind="home", show_nfa=True)
# ---------- write ----------
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT+"/assets"); shutil.copytree("data", OUT+"/data"); os.makedirs(OUT+"/img/coins")
for _k in COINS:
    _f = f"logos/{COINS[_k]['cgid']}.png"
    if os.path.exists(_f): shutil.copy(_f, OUT+"/img/coins/")
open(OUT+"/assets/site.css","w").write(CSS); open(OUT+"/assets/site.js","w").write(JS)
seo.BEACON_SITE, seo.BEACON_DOMAIN = BEACON_SITE, LIVE_HOST
for p, h in PAGES.items():
    os.makedirs(os.path.join(OUT, p), exist_ok=True)
    open(os.path.join(OUT, p, "index.html"), "w").write(seo.add_beacon(h))
_seen=set(); _idx=[]
for _k,_c in COINS.items():
    _idx.append({"t":_c["name"],"s":_c["sym"],"u":_c["slug"]+"/","k":"coin"}); _seen.add(_c["slug"]+"/")
for _x in SEARCH:
    if _x["u"] not in _seen: _seen.add(_x["u"]); _idx.append(_x)
json.dump(_idx, open(OUT+"/search.json","w"), separators=(",",":"))
nf = PAGES["about/"].replace("<h1>About CryptoHistoryBook</h1>", "<h1>Page not found</h1><p><a href='/'>Go to the home page</a></p>",1)
open(OUT+"/404.html","w").write(seo.add_beacon(nf.replace('data-root="../"','data-root="/"').replace('href="../','href="/').replace('src="../','src="/')))
open(OUT+"/robots.txt","w").write("User-agent: *\nDisallow: /\n")
open(OUT+"/favicon.svg","w").write(LOGO.replace(' aria-hidden="true"',''))
open(OUT+"/logo.svg","w").write(LOGO.replace(' aria-hidden="true"',''))
open(OUT+"/.nojekyll","w").write("")
json.dump(REPORT, open(OUT+"/../build-report.json","w"), indent=1)
open(OUT+"/CNAME","w").write("cryptohistorybook.com\n")
import subprocess; subprocess.run(["python3","icons.py"])
print("pages", len(PAGES), "thin-gate pass", sum(r["passes_thin_gate"] for r in REPORT))
