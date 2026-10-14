import json,time,urllib.request,datetime as dt,os,sys
UA={"User-Agent":"Mozilla/5.0"}
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
        except Exception as e:
            if "404" in str(e) or "400" in str(e): return None
            time.sleep(3)
D=lambda t: dt.datetime.fromtimestamp(t,dt.UTC).strftime("%Y-%m-%d")
NOW=int(time.time())
def bitstamp(p):
    out={};t=int(dt.datetime(2011,8,1).timestamp())
    while t<NOW:
        r=get(f"https://www.bitstamp.net/api/v2/ohlc/{p}/?step=86400&limit=1000&start={t}")
        if not r or "data" not in r: return out
        for x in r["data"]["ohlc"]: out[D(int(x["timestamp"]))]=float(x["close"])
        t+=1000*86400; time.sleep(.3)
    return out
def coinbase(p):
    out={};t=int(dt.datetime(2015,1,1).timestamp())
    while t<NOW:
        e=min(t+299*86400,NOW)
        r=get(f"https://api.exchange.coinbase.com/products/{p}/candles?granularity=86400&start={D(t)}T00:00:00Z&end={D(e)}T00:00:00Z")
        if r is None: return out
        for x in r: out[D(int(x[0]))]=float(x[4])
        t=e+86400; time.sleep(.25)
    return out
def binance(s):
    out={};t=1500000000000
    while True:
        r=get(f"https://data-api.binance.vision/api/v3/klines?symbol={s}&interval=1d&startTime={t}&limit=1000")
        if not r: return out
        for k in r: out[D(k[0]//1000)]=float(k[4])
        t=r[-1][0]+86400000
        if len(r)<1000: return out
def cg(i):
    r=get(f"https://api.coingecko.com/api/v3/coins/{i}/market_chart?vs_currency=usd&days=365&interval=daily")
    return {D(int(p[0]//1000)):p[1] for p in (r or {}).get("prices",[])}
SRC={"Bitstamp":"https://www.bitstamp.net/api/","Coinbase Exchange":"https://docs.cdp.coinbase.com/exchange/","Binance":"https://developers.binance.com/docs/binance-spot-api-docs/rest-api","CoinGecko":"https://docs.coingecko.com/reference/coins-id-market-chart"}
def run(key,sym,cgid,bsym=None):
    fn=f"data/{key}.json"
    if os.path.exists(fn): return
    s=sym.upper(); bsym=bsym or s
    cands=[("Bitstamp",f"{s}/USD",bitstamp(s.lower()+"usd")),("Coinbase Exchange",f"{s}/USD",coinbase(f"{s}-USD")),("Binance",f"{bsym}/USDT",binance(bsym+"USDT"))]
    cands=[c for c in cands if len(c[2])>30]
    usd=[c for c in cands if c[0]!="Binance"]; bn=[c for c in cands if c[0]=="Binance"]
    segs=[];pts=[]
    if usd:
        prim=min(usd,key=lambda c:min(c[2]))
        first=min(prim[2])
        if bn:
            pre=sorted((d,v) for d,v in bn[0][2].items() if d<first)
            if pre: segs.append(dict(source="Binance",pair=bn[0][1],frm=pre[0][0],to=pre[-1][0])); pts+=pre
        body=sorted(prim[2].items()); segs.append(dict(source=prim[0],pair=prim[1],frm=body[0][0],to=body[-1][0])); pts+=body
    elif bn:
        body=sorted(bn[0][2].items()); segs.append(dict(source="Binance",pair=bn[0][1],frm=body[0][0],to=body[-1][0])); pts+=body
    else:
        c=cg(cgid); time.sleep(8)
        if c:
            body=sorted(c.items()); segs.append(dict(source="CoinGecko",pair=f"{s}/USD",frm=body[0][0],to=body[-1][0])); pts+=body
    pts=[[d,v] for d,v in pts if v>0]
    segs=[{"from":g["frm"],"to":g["to"],"source":g["source"],"pair":g["pair"],"url":SRC[g["source"]]} for g in segs]
    json.dump({"coin":key,"pair":f"{s}/USD","fetched":"2026-10-14","segments":segs,"points":pts},open(fn,"w"),separators=(",",":"))
    print(key,len(pts),[(g["source"],g["from"]) for g in segs],flush=True)
if __name__=="__main__":
    for line in open(sys.argv[1] if len(sys.argv)>1 else "coinlist.txt"):
        k,sym,cgid,*b=line.split(); run(k,sym,cgid,b[0] if b else None)
