from PIL import Image, ImageDraw
def mk(n):
    S=n*4; im=Image.new("RGBA",(S,S)); px=im.load()
    a,b,c=(124,58,237),(236,72,153),(249,115,22)
    for y in range(S):
        for x in range(S):
            t=(x+y)/(2*S); u=t/0.55 if t<.55 else (t-.55)/.45
            p,q=(a,b) if t<.55 else (b,c); px[x,y]=tuple(int(p[i]+(q[i]-p[i])*u) for i in range(3))+(255,)
    m=Image.new("L",(S,S)); ImageDraw.Draw(m).rounded_rectangle([0,0,S-1,S-1],radius=int(S*.28),fill=255); im.putalpha(m)
    d=ImageDraw.Draw(im); k=S/64
    pts=[(14,42),(24,34),(31,38),(41,24),(50,19)]; d.line([(x*k,y*k) for x,y in pts],fill="white",width=int(4.5*k),joint="curve")
    for x,y,r in [(24,34,3.6),(41,24,3.6)]: d.ellipse([(x-r)*k,(y-r)*k,(x+r)*k,(y+r)*k],fill="white")
    d.ellipse([(50-5)*k,(19-5)*k,(55)*k,(24)*k],fill=(253,230,138),outline="white",width=int(2*k))
    return im.resize((n,n),Image.LANCZOS)
mk(180).save("docs/apple-touch-icon.png"); mk(64).save("docs/favicon.ico",sizes=[(16,16),(32,32),(48,48)])
