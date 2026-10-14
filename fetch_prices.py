import json,time,urllib.request,datetime as dt
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
def bitstamp(pair,start):
    out={};t=start;end=int(time.time())
    while t<end:
        d=get(f"https://www.bitstamp.net/api/v2/ohlc/{pair}/?step=86400&limit=1000&start={t}")["data"]["ohlc"]
        for r in d: out[int(r["timestamp"])]=float(r["close"])
        t+=1000*86400; time.sleep(.4)
    return out
def coinbase(prod,start):
    out={};t=start;end=int(time.time())
    while t<end:
        e=min(t+299*86400,end)
        d=get(f"https://api.exchange.coinbase.com/products/{prod}/candles?granularity=86400&start={dt.datetime.utcfromtimestamp(t).isoformat()}Z&end={dt.datetime.utcfromtimestamp(e).isoformat()}Z")
        for r in d: out[int(r[0])]=float(r[4])
        t=e+86400; time.sleep(.4)
    return out
S=int(dt.datetime(2011,8,1).timestamp())
res={}
for c,pair,prod in [("btc","btcusd","BTC-USD"),("eth","ethusd","ETH-USD"),("xrp","xrpusd","XRP-USD"),("doge","dogeusd","DOGE-USD"),("sol","solusd","SOL-USD")]:
    b=bitstamp(pair,S); cb=coinbase(prod,int(dt.datetime(2015,1,1).timestamp()))
    # choose source with earliest start per coin; fill nothing across sources
    bs=min(b) if b else 9e12; cs=min(cb) if cb else 9e12
    src,data=("Bitstamp",b) if bs<=cs else ("Coinbase Exchange",cb)
    pts=[[dt.datetime.utcfromtimestamp(k).strftime("%Y-%m-%d"),v] for k,v in sorted(data.items()) if v>0]
    print(c,src,len(pts),pts[0],pts[-1],"bitstamp start",dt.datetime.utcfromtimestamp(bs).date() if b else None,"cb start",dt.datetime.utcfromtimestamp(cs).date() if cb else None)
    json.dump({"coin":c,"source":src,"source_url":"https://www.bitstamp.net/api/" if src=="Bitstamp" else "https://docs.cdp.coinbase.com/exchange/","pair":f"{c.upper()}/USD","field":"daily close (UTC)","fetched":"2026-10-14","points":pts},open(f"data/{c}.json","w"),separators=(",",":"))
