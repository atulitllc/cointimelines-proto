import re,glob,subprocess,concurrent.futures as cf
urls=set()
for f in glob.glob("docs/**/index.html",recursive=True):
    urls|=set(re.findall(r'href="(https?://[^"]+)"',open(f).read()))
urls={u.replace("&amp;","&") for u in urls if "fonts.g" not in u and "cointimelines.com" not in u}
def chk(u):
    ua="Atulit research pk0567480@gmail.com" if "sec.gov" in u else "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
    r=subprocess.run(["curl","-s","-o","/dev/null","-w","%{http_code}","-L","-A",ua,"--max-time","15",u],capture_output=True,text=True);return r.stdout,u
with cf.ThreadPoolExecutor(24) as ex:
    for s,u in sorted(ex.map(chk,urls)):
        if s!="200": print(s,u,flush=True)
print("total",len(urls))
