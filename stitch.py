import json,urllib.request,time,datetime as dt
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
for c,sym in [("doge","DOGEUSDT"),("sol","SOLUSDT")]:
    d=json.load(open(f"data/{c}.json"))
    if "segments" in d: continue
    first=d["points"][0][0]; out=[]; t=1500000000000
    while True:
        r=get(f"https://data-api.binance.vision/api/v3/klines?symbol={sym}&interval=1d&startTime={t}&limit=1000")
        if not r: break
        for k in r:
            day=dt.datetime.fromtimestamp(k[0]/1000,dt.UTC).strftime("%Y-%m-%d")
            if day<first: out.append([day,float(k[4])])
        t=r[-1][0]+86400000
        if day>=first: break
        time.sleep(.3)
    segs=[]
    if out: segs.append({"from":out[0][0],"to":out[-1][0],"source":"Binance","pair":sym[:-4]+"/USDT","url":"https://developers.binance.com/docs/binance-spot-api-docs/rest-api"})
    segs.append({"from":first,"to":d["points"][-1][0],"source":d["source"],"pair":d["pair"],"url":d["source_url"]})
    d["points"]=out+d["points"]; d["segments"]=segs; json.dump(d,open(f"data/{c}.json","w"),separators=(",",":"))
    print(c,segs)
for c in ["btc","eth","xrp"]:
    d=json.load(open(f"data/{c}.json"))
    d.setdefault("segments",[{"from":d["points"][0][0],"to":d["points"][-1][0],"source":d["source"],"pair":d["pair"],"url":d["source_url"]}]); json.dump(d,open(f"data/{c}.json","w"),separators=(",",":"))
