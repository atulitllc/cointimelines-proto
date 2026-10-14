CSS = r"""
:root{--bg:#fff;--fg:#0b0b1a;--mut:#5b5f77;--bd:#e8e8f2;--card:#fff;--soft:#f6f5ff;--acc:#7c3aed;--acc2:#f97316;--ok:#10b981;--bad:#ef4444;--grad:linear-gradient(135deg,#7c3aed 0%,#ec4899 50%,#f97316 100%);--shadow:0 10px 30px -12px rgba(76,29,149,.25)}
[data-theme=dark]{--bg:#0a0a14;--fg:#f4f3ff;--mut:#a3a3c2;--bd:#25253a;--card:#12121f;--soft:#171729;--shadow:0 10px 30px -12px rgba(0,0,0,.6)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;-webkit-font-smoothing:antialiased}
h1,h2,h3,.brand{font-family:"Space Grotesk",Inter,sans-serif;letter-spacing:-.02em;line-height:1.15}
h1{font-size:clamp(2rem,5vw,3.4rem);margin:.2em 0 .3em}h2{font-size:clamp(1.4rem,3vw,2rem);margin:1.6em 0 .5em}h3{font-size:1.15rem;margin:.2em 0 .4em}
a{color:var(--acc)}[data-theme=dark] a{color:#c4b5fd}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}.narrow{max-width:780px}
.ic{width:1.1em;height:1.1em;vertical-align:-.18em;flex:none}
header.top{position:sticky;top:0;z-index:50;background:color-mix(in srgb,var(--bg) 86%,transparent);backdrop-filter:saturate(1.6) blur(12px);border-bottom:1px solid var(--bd)}
header.top .wrap{display:flex;align-items:center;gap:18px;height:64px}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:1.25rem;color:var(--fg);text-decoration:none}
.brand svg{width:34px;height:34px}.brand b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
nav.main{display:flex;gap:4px;margin-left:auto;align-items:center}
nav.main a{color:var(--fg);text-decoration:none;font-weight:600;font-size:.94rem;padding:8px 12px;border-radius:10px;display:flex;align-items:center;gap:6px}
nav.main a:hover{background:var(--soft)}
.thm{display:grid;place-items:center;width:38px;height:38px;border-radius:12px;border:1px solid var(--bd);background:var(--card);color:var(--fg);cursor:pointer}
.thm .i-sun{display:none}[data-theme=dark] .thm .i-sun{display:block}[data-theme=dark] .thm .i-moon{display:none}
.menu-btn{display:none}
@media(max-width:860px){nav.main{display:none;position:absolute;top:64px;left:0;right:0;flex-direction:column;align-items:stretch;background:var(--bg);border-bottom:1px solid var(--bd);padding:10px}nav.main.open{display:flex}.menu-btn{display:grid;margin-left:auto}.thm{margin-left:0}}
.nfa{display:flex;gap:10px;align-items:center;background:linear-gradient(90deg,rgba(124,58,237,.08),rgba(249,115,22,.08));border:1px solid var(--bd);border-radius:14px;padding:10px 14px;font-size:.9rem;color:var(--mut);margin:18px 0}
.nfa .ic{color:var(--acc2)}
.hero{position:relative;overflow:hidden;border-radius:28px;margin:22px 0;padding:56px 44px;color:#fff;background:var(--grad);box-shadow:var(--shadow)}
.hero h1{color:#fff;max-width:760px}.hero p.lede{font-size:1.2rem;max-width:640px;opacity:.95}
.hero .blob{position:absolute;border-radius:50%;filter:blur(40px);opacity:.5;animation:float 12s ease-in-out infinite}
@keyframes float{0%,100%{transform:translate(0,0)}50%{transform:translate(30px,-20px)}}
.hero .art{position:absolute;right:-20px;bottom:-10px;width:min(520px,55%);opacity:.95;pointer-events:none}
.hero .inner{position:relative;z-index:2}
@media(max-width:760px){.hero{padding:34px 22px;border-radius:22px}.hero .art{opacity:.25;width:90%}}
.chip{display:inline-flex;align-items:center;gap:6px;padding:5px 12px;border-radius:999px;font-weight:600;font-size:.82rem;background:rgba(255,255,255,.2);color:#fff;border:1px solid rgba(255,255,255,.35)}
.chip.k{background:var(--soft);color:var(--fg);border-color:var(--bd)}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:14px;font-weight:700;text-decoration:none;border:0;cursor:pointer;font-size:1rem}
.btn.w{background:#fff;color:#1e1b4b}.btn.g{background:var(--grad);color:#fff}.btn.o{background:transparent;color:inherit;border:1.5px solid currentColor}
.grid{display:grid;gap:18px}.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}.g5{grid-template-columns:repeat(5,1fr)}
@media(max-width:960px){.g5{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(2,1fr)}}
@media(max-width:620px){.g2,.g3,.g5{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--bd);border-radius:20px;padding:22px;box-shadow:var(--shadow);position:relative;overflow:hidden;text-decoration:none;color:var(--fg);display:block;transition:transform .25s,box-shadow .25s}
a.card:hover{transform:translateY(-4px);box-shadow:0 18px 40px -16px rgba(124,58,237,.45)}
.card .bar{position:absolute;left:0;top:0;right:0;height:5px}
svg.logo{width:44px;height:44px;flex:none}
.coincard .top{display:flex;align-items:center;gap:12px}.coincard .logo{width:44px;height:44px}
.coincard .spark{width:100%;height:56px;margin-top:10px}
.coincard .px{font-family:"Space Grotesk";font-weight:700;font-size:1.3rem}
.small{font-size:.82rem;color:var(--mut)}
.ibox{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;color:#fff;margin-bottom:12px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:26px 0}
@media(max-width:700px){.stats{grid-template-columns:repeat(2,1fr)}}
.stat{border-radius:20px;padding:20px;color:#fff}.stat b{display:block;font:700 2.2rem "Space Grotesk"}.stat span{opacity:.9;font-weight:600;font-size:.9rem}
.reveal{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease}.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}.hero .blob{animation:none}}
.chartbox{background:var(--card);border:1px solid var(--bd);border-radius:24px;padding:18px;box-shadow:var(--shadow);margin:22px 0}
.chartbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:10px}
.seg{display:inline-flex;background:var(--soft);border-radius:12px;padding:3px;border:1px solid var(--bd)}
.seg button{border:0;background:transparent;color:var(--fg);font-weight:600;padding:6px 12px;border-radius:9px;cursor:pointer;font-size:.86rem}
.seg button.on{background:var(--card);box-shadow:0 2px 8px rgba(0,0,0,.12);color:var(--acc)}
.chart{position:relative;width:100%;height:420px}.chart.mini{height:260px}
@media(max-width:620px){.chart{height:320px}.chart.mini{height:220px}}
.chart svg{width:100%;height:100%;display:block;overflow:visible}
.chart .line{fill:none;stroke-width:2.4;stroke-linejoin:round}
.chart .grid line{stroke:var(--bd)}.chart .grid text{fill:var(--mut);font-size:11px}
.chart .mk{cursor:pointer;transition:r .15s}.chart .mk:hover{r:9}
.tip{position:absolute;pointer-events:none;background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:8px 12px;font-size:.82rem;box-shadow:var(--shadow);white-space:nowrap;opacity:0;transition:opacity .15s;z-index:5}
.pop{position:absolute;z-index:6;width:min(320px,90%);background:var(--card);border:1px solid var(--bd);border-radius:18px;padding:16px;box-shadow:0 20px 50px -10px rgba(0,0,0,.35);display:none}
.pop.show{display:block;animation:popin .25s ease}@keyframes popin{from{opacity:0;transform:scale(.95)}}
.pop .x{position:absolute;right:10px;top:8px;border:0;background:none;color:var(--mut);font-size:1.3rem;cursor:pointer}
.legend{display:flex;flex-wrap:wrap;gap:10px;font-size:.8rem;color:var(--mut);margin-top:8px}.legend i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px;vertical-align:-1px}
.src{font-size:.8rem;color:var(--mut);margin-top:10px;display:flex;gap:6px;align-items:flex-start}
ol.tl{list-style:none;padding:0;margin:20px 0;position:relative}
ol.tl:before{content:"";position:absolute;left:19px;top:6px;bottom:6px;width:3px;border-radius:3px;background:var(--grad)}
ol.tl li{position:relative;padding:0 0 18px 56px}
ol.tl .dot{position:absolute;left:6px;top:4px;width:30px;height:30px;border-radius:50%;display:grid;place-items:center;color:#fff;box-shadow:0 0 0 4px var(--bg)}
ol.tl .dot .ic{width:15px;height:15px}
ol.tl a.ev{display:block;text-decoration:none;color:var(--fg);background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:12px 16px;transition:transform .2s,border-color .2s}
ol.tl a.ev:hover{transform:translateX(4px);border-color:var(--acc)}
ol.tl .d{font-size:.8rem;color:var(--mut);font-weight:600}.ol .p{font-weight:700}
.kind{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;padding:2px 8px;border-radius:6px;color:#fff;margin-left:6px}
.pricecard{border-radius:20px;padding:20px;color:#fff;margin:20px 0;display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.pricecard b{font:700 2rem "Space Grotesk"}.pricecard .small{color:rgba(255,255,255,.9)}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:18px 0}
.fact{background:var(--soft);border:1px solid var(--bd);border-radius:16px;padding:14px}.fact span{font-size:.78rem;color:var(--mut);font-weight:600;text-transform:uppercase;letter-spacing:.05em}.fact b{display:block;font-family:"Space Grotesk";font-size:1.05rem}
.sources{background:var(--soft);border:1px solid var(--bd);border-radius:20px;padding:18px 22px;margin:34px 0}
.sources h2{margin-top:0;font-size:1.2rem;display:flex;gap:8px;align-items:center}.sources li{margin:4px 0}
.sources .chk{font-size:.85rem;color:var(--mut)}
.pn{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:26px 0}.pn a{padding:14px 18px}.pn .r{text-align:right}
.crumb{font-size:.85rem;color:var(--mut);margin-top:18px}.crumb a{color:var(--mut)}
.upd{font-size:.85rem;color:var(--mut);display:flex;gap:6px;align-items:center}
table.cmp{width:100%;border-collapse:separate;border-spacing:0;border:1px solid var(--bd);border-radius:18px;overflow:hidden;margin:20px 0}
table.cmp th,table.cmp td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--bd);vertical-align:top}
table.cmp thead th{color:#fff;font-family:"Space Grotesk"}table.cmp tbody th{background:var(--soft);width:24%;font-weight:600}
@media(max-width:620px){table.cmp{font-size:.88rem}table.cmp th,table.cmp td{padding:9px}}
.vs{display:flex;align-items:center;gap:16px;justify-content:center;margin:12px 0}.vs svg.logo{width:64px;height:64px}.vs b{font:800 1.6rem "Space Grotesk"}
.diagram{background:var(--card);border:1px solid var(--bd);border-radius:24px;padding:20px;margin:22px 0;box-shadow:var(--shadow)}.diagram svg{width:100%;height:auto;display:block}
.faq details{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:12px 16px;margin:10px 0}.faq summary{font-weight:700;cursor:pointer}
.news{border-radius:26px;padding:34px;margin:40px 0;color:#fff;background:linear-gradient(135deg,#0ea5e9,#7c3aed 60%,#ec4899)}
.news form{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px}.news input{flex:1;min-width:220px;padding:13px 16px;border-radius:14px;border:0;font-size:1rem}
.news .msg{margin-top:10px;font-weight:600;min-height:1.4em}
footer{border-top:1px solid var(--bd);margin-top:50px;padding:34px 0;color:var(--mut);font-size:.9rem}
footer .cols{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:20px}footer a{color:var(--mut);text-decoration:none;display:block;margin:3px 0}footer a:hover{color:var(--acc)}
footer h4{color:var(--fg);margin:0 0 8px;font-family:"Space Grotesk"}
@media(max-width:760px){footer .cols{grid-template-columns:1fr 1fr}}
.prose p{font-size:1.06rem}.prose{max-width:760px}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}
.yearlist{display:flex;flex-wrap:wrap;gap:8px}.yearlist a{padding:8px 14px;border-radius:12px;background:var(--soft);border:1px solid var(--bd);text-decoration:none;color:var(--fg);font-weight:700;font-family:"Space Grotesk"}
.yearlist a:hover{background:var(--grad);color:#fff}
[hidden]{display:none!important}
.g4{grid-template-columns:repeat(4,1fr)}@media(max-width:1100px){.g4{grid-template-columns:repeat(3,1fr)}}@media(max-width:760px){.g4{grid-template-columns:repeat(2,1fr)}}@media(max-width:480px){.g4{grid-template-columns:1fr}}
.cgi{padding:16px}.cgi .top{display:flex;gap:12px;align-items:center}.cgi .tags{margin:10px 0 6px}.cgi .chip.k{font-size:.72rem;padding:3px 8px}
img.logo{width:44px;height:44px;border-radius:50%;flex:none;object-fit:contain}img.ic{width:1.3em;height:1.3em;border-radius:50%}.vs img.logo{width:64px;height:64px}.coincard img.logo{width:44px;height:44px}
.hsearch{position:relative;display:flex;align-items:center;gap:6px;background:var(--card);border:1.5px solid var(--bd);border-radius:12px;padding:6px 10px;margin-left:auto;width:240px}.hsearch input{border:0;background:transparent;color:var(--fg);font-size:.92rem;flex:1;min-width:0;outline:none}.hsearch .ic{width:16px;height:16px;opacity:.7}.sugg{position:absolute;top:calc(100% + 6px);left:0;right:0;min-width:300px;list-style:none;margin:0;padding:6px;background:var(--card);border:1.5px solid var(--bd);border-radius:14px;box-shadow:0 18px 40px rgba(0,0,0,.18);z-index:60;max-height:380px;overflow:auto}.sugg li a{display:flex;justify-content:space-between;gap:10px;padding:8px 10px;border-radius:9px;color:var(--fg);text-decoration:none;font-size:.92rem}.sugg li a small{opacity:.6;white-space:nowrap}.sugg li.on a,.sugg li a:hover{background:var(--bd)}@media(max-width:860px){.top .wrap{flex-wrap:wrap;height:auto!important;min-height:64px;row-gap:0;padding-top:8px}.hsearch{order:9;width:100%;flex-basis:100%;margin:0 0 10px}}.cfilter{display:flex;flex-direction:column;gap:12px;margin:14px 0 18px}.search{display:flex;align-items:center;gap:10px;background:var(--card);border:1.5px solid var(--bd);border-radius:16px;padding:10px 14px;max-width:520px}.search input{border:0;background:transparent;color:var(--fg);font-size:1rem;flex:1;outline:none}
.chips{display:flex;flex-wrap:wrap;gap:8px}.cchip{border:1.5px solid var(--bd);background:var(--card);color:var(--fg);border-radius:999px;padding:6px 14px;font-weight:600;cursor:pointer;font-size:.86rem}.cchip.on{background:var(--grad);color:#fff;border-color:transparent}
.draw{stroke-dasharray:var(--len);stroke-dashoffset:var(--len);animation:draw 2.4s ease forwards}@keyframes draw{to{stroke-dashoffset:0}}
"""
JS = r"""
(function(){
var d=document,R=d.documentElement.getAttribute('data-root')||'./';
var mb=d.querySelector('.menu-btn');if(mb)mb.onclick=function(){d.querySelector('nav.main').classList.toggle('open')};
var io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');if(e.target.dataset.count)count(e.target);io.unobserve(e.target)}})},{threshold:.12}):null;
d.querySelectorAll('.reveal,[data-count]').forEach(function(el){io?io.observe(el):el.classList.add('in')});
function count(el){var n=+el.dataset.count,t0=performance.now();(function f(t){var k=Math.min(1,(t-t0)/1400);el.textContent=Math.round(n*(1-Math.pow(1-k,3))).toLocaleString();if(k<1)requestAnimationFrame(f)})(t0)}
// site search
(function(){var R=document.documentElement.getAttribute('data-root')||document.body.getAttribute('data-root')||'./';var IDX=null,L=null;
var K={coin:'Coin',event:'Event',guide:'Guide',compare:'Compare',glossary:'Glossary',explainer:'Explainer',hub:'Coin',timeline:'Timeline'};
function load(){if(IDX)return Promise.resolve(IDX);if(!L)L=fetch(R+'search.json?v='+(window.CHB_V||'')).then(function(r){return r.json()}).then(function(d){IDX=d;return d});return L}
function find(q){q=q.toLowerCase().trim();if(!q||!IDX)return[];var t=q.split(/\s+/),out=[];IDX.forEach(function(x){var n=x.t.toLowerCase(),s=(x.s||'').toLowerCase(),sc=0;
if(s&&s===q)sc=100;else if(n===q)sc=90;else if(n.indexOf(q)===0)sc=70;else if(s&&s.indexOf(q)===0)sc=60;else if(t.every(function(w){return n.indexOf(w)>=0}))sc=40;else return;
if(x.k==='coin')sc+=10;out.push([sc,x])});out.sort(function(a,b){return b[0]-a[0]||a[1].t.length-b[1].t.length});return out.slice(0,8).map(function(a){return a[1]})}
document.querySelectorAll('form.hsearch').forEach(function(f){var i=f.querySelector('input'),u=f.querySelector('.sugg'),res=[],sel=-1;
function close(){u.hidden=true;i.setAttribute('aria-expanded','false')}
function esc(s){return s.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function draw(){res=find(i.value);if(!res.length){u.innerHTML=i.value.trim()?'<li><a href="'+R+'coins/"><span>No matches. Browse all coins</span></a></li>':'';u.hidden=!i.value.trim();return}
u.innerHTML=res.map(function(x,n){return '<li role="option"'+(n===sel?' class="on" aria-selected="true"':'')+'><a href="'+R+x.u+'"><span>'+esc(x.t)+(x.s?' <small>'+esc(x.s)+'</small>':'')+'</span><small>'+(K[x.k]||'Page')+'</small></a></li>'}).join('');u.hidden=false;i.setAttribute('aria-expanded','true')}
i.addEventListener('focus',load);i.addEventListener('input',function(){sel=-1;load().then(draw)});
i.addEventListener('keydown',function(e){if(e.key==='ArrowDown'||e.key==='ArrowUp'){if(!res.length)return;e.preventDefault();sel=(sel+(e.key==='ArrowDown'?1:-1)+res.length)%res.length;draw()}else if(e.key==='Escape')close()});
f.addEventListener('submit',function(e){e.preventDefault();load().then(function(){var r=find(i.value),p=sel>=0?res[sel]:r[0];location.href=p?R+p.u:R+'coins/'})});
document.addEventListener('click',function(e){if(!f.contains(e.target))close()})})})();
// newsletter
d.querySelectorAll('form.nl').forEach(function(f){f.onsubmit=function(e){e.preventDefault();var v=f.email.value.trim(),m=f.querySelector('.msg')||f.parentNode.querySelector('.msg');if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)){m.textContent='Please enter a valid email address.';return}
try{var l=JSON.parse(localStorage.getItem('ct-newsletter')||'[]');if(l.indexOf(v)<0)l.push(v);localStorage.setItem('ct-newsletter',JSON.stringify(l))}catch(x){}
m.textContent='Saved on this device only. Nothing is sent yet; the newsletter has not launched.';f.reset()}});
// coin filter
var q=d.getElementById('coin-q'),cat='';function flt(){var t=(q&&q.value||'').toLowerCase().trim(),n=0;d.querySelectorAll('.cgi').forEach(function(x){var ok=(!t||x.dataset.name.indexOf(t)>=0)&&(!cat||x.dataset.cats.split('|').indexOf(cat)>=0);x.hidden=!ok;if(ok){n++;x.classList.add('in')}});var z=d.querySelector('.cnone');if(z)z.hidden=n>0}
if(q)q.oninput=flt;d.querySelectorAll('.cchip').forEach(function(b){b.onclick=function(){d.querySelectorAll('.cchip').forEach(function(x){x.classList.remove('on')});b.classList.add('on');cat=b.dataset.cat;flt()}});
// charts
var KC={launch:'#0ea5e9',rally:'#10b981',crash:'#ef4444',upgrade:'#7c3aed',legal:'#f59e0b',fork:'#ec4899',outage:'#64748b',milestone:'#f97316'};
var cache={};function load(c){return cache[c]||(cache[c]=fetch(R+'data/'+c+'.json').then(function(r){return r.json()}))}
function fmt(v){return v>=1000?'$'+Math.round(v).toLocaleString():v>=1?'$'+v.toFixed(2):'$'+v.toPrecision(3)}
function srcOf(data,day){var s=data.segments.filter(function(g){return day>=g.from&&day<=g.to})[0];return s?s.source+' '+s.pair+' daily close':''}
d.querySelectorAll('.chart').forEach(function(box){
 var coin=box.dataset.coin,col=box.dataset.color,col2=box.dataset.color2||col,evs=JSON.parse(box.dataset.events||'[]');
 var parent=box.closest('.chartbox');var logBtn=parent.querySelector('[data-log]'),rng=parent.querySelectorAll('[data-range]');
 var state={log:box.dataset.log==='1',from:box.dataset.from||'',to:box.dataset.to||''};
 load(coin).then(function(data){
  function draw(anim){
   var P=data.points.filter(function(p){return(!state.from||p[0]>=state.from)&&(!state.to||p[0]<=state.to)});if(P.length<2)return;
   var W=box.clientWidth,H=box.clientHeight,ml=58,mr=14,mt=14,mb=28,iw=W-ml-mr,ih=H-mt-mb;
   var t0=Date.parse(P[0][0]),t1=Date.parse(P[P.length-1][0]);var vs=P.map(function(p){return p[1]}),lo=Math.min.apply(0,vs),hi=Math.max.apply(0,vs);
   var L=state.log,f=L?Math.log10:function(v){return v},a=f(lo),b=f(hi);if(!L){a=0}var pad=(b-a)*.06;b+=pad;if(L)a-=pad;
   function X(day){return ml+(Date.parse(day)-t0)/(t1-t0)*iw}function Y(v){return mt+ih-(f(Math.max(v,1e-9))-a)/(b-a)*ih}
   var step=Math.max(1,Math.floor(P.length/1400)),pts=[];for(var i=0;i<P.length;i+=step)pts.push(P[i]);pts.push(P[P.length-1]);
   var path=pts.map(function(p,i){return(i?'L':'M')+X(p[0]).toFixed(1)+' '+Y(p[1]).toFixed(1)}).join('');
   var g='';var ticks=[];if(L){for(var e=Math.floor(a);e<=Math.ceil(b);e++)[1,2,5].forEach(function(m){var v=m*Math.pow(10,e);if(f(v)>=a&&f(v)<=b)ticks.push(v)});if(ticks.length>8)ticks=ticks.filter(function(v){return String(v).replace(/0|\./g,'').charAt(0)==='1'})}else{var r=hi/5,mag=Math.pow(10,Math.floor(Math.log10(r))),st=Math.ceil(r/mag)*mag;for(var v=0;v<=hi*1.05;v+=st)ticks.push(v)}
   ticks.forEach(function(v){var y=Y(v);g+='<line x1="'+ml+'" x2="'+(W-mr)+'" y1="'+y+'" y2="'+y+'"/><text x="'+(ml-8)+'" y="'+(y+4)+'" text-anchor="end">'+fmt(v||0).replace('$0.00','$0')+'</text>'});
   var y0=new Date(t0).getUTCFullYear(),y1=new Date(t1).getUTCFullYear(),ys=Math.max(1,Math.ceil((y1-y0+1)/(W<600?5:10)));
   if(y1>y0){for(var y=y0+1;y<=y1;y+=ys){var x=X(y+'-01-01');g+='<line x1="'+x+'" x2="'+x+'" y1="'+mt+'" y2="'+(mt+ih)+'" stroke-dasharray="2 4"/><text x="'+x+'" y="'+(H-8)+'" text-anchor="middle">'+y+'</text>'}}else{for(var m=0;m<12;m+=2){var dd=y0+'-'+('0'+(m+1)).slice(-2)+'-01';if(dd>=P[0][0]){var x2=X(dd);g+='<text x="'+x2+'" y="'+(H-8)+'" text-anchor="middle">'+['Jan','Mar','May','Jul','Sep','Nov'][m/2]+'</text>'}}}
   var id='g'+Math.random().toString(36).slice(2);
   var mk=evs.filter(function(e){return e.price!=null&&e.date>=P[0][0]&&e.date<=P[P.length-1][0]}).map(function(e,i){return'<circle class="mk" data-i="'+evs.indexOf(e)+'" cx="'+X(e.date)+'" cy="'+Y(e.price)+'" r="'+(e.focus?9:6)+'" fill="'+KC[e.kind]+'" stroke="#fff" stroke-width="2.5" style="opacity:0;animation:popin .4s '+(anim?1.6+i*.05:0)+'s forwards"/>'}).join('');
   box.innerHTML='<svg viewBox="0 0 '+W+' '+H+'"><defs><linearGradient id="'+id+'" x1="0" x2="1"><stop offset="0" stop-color="'+col+'"/><stop offset="1" stop-color="'+col2+'"/></linearGradient><linearGradient id="'+id+'f" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="'+col+'" stop-opacity=".28"/><stop offset="1" stop-color="'+col+'" stop-opacity="0"/></linearGradient></defs><g class="grid">'+g+'</g><path d="'+path+'L'+X(P[P.length-1][0])+' '+(mt+ih)+'L'+ml+' '+(mt+ih)+'Z" fill="url(#'+id+'f)" style="opacity:0;animation:popin 1s '+(anim?1.2:0)+'s forwards;transform:none"/><path class="line" d="'+path+'" stroke="url(#'+id+')"/><line class="cx" y1="'+mt+'" y2="'+(mt+ih)+'" stroke="var(--mut)" stroke-dasharray="3 3" style="display:none"/>'+mk+'</svg><div class="tip"></div><div class="pop"></div>';
   var ln=box.querySelector('.line');if(anim&&ln.getTotalLength){var len=ln.getTotalLength();ln.style.setProperty('--len',len);ln.classList.add('draw')}
   var tip=box.querySelector('.tip'),cx=box.querySelector('.cx'),svg=box.querySelector('svg'),pop=box.querySelector('.pop');
   svg.onmousemove=function(ev){var r=svg.getBoundingClientRect(),x=ev.clientX-r.left;if(x<ml||x>W-mr){tip.style.opacity=0;cx.style.display='none';return}
    var t=t0+(x-ml)/iw*(t1-t0),lo2=0,hi2=P.length-1;while(hi2-lo2>1){var mid=(lo2+hi2)>>1;Date.parse(P[mid][0])<t?lo2=mid:hi2=mid}var p=P[hi2];
    cx.setAttribute('x1',X(p[0]));cx.setAttribute('x2',X(p[0]));cx.style.display='';tip.innerHTML='<b>'+fmt(p[1])+'</b> on '+p[0]+'<br><span class="small">'+srcOf(data,p[0])+'</span>';tip.style.opacity=1;tip.style.left=Math.min(W-220,X(p[0])+12)+'px';tip.style.top=(Y(p[1])-50<0?Y(p[1])+12:Y(p[1])-56)+'px'};
   svg.onmouseleave=function(){tip.style.opacity=0;cx.style.display='none'};
   box.querySelectorAll('.mk').forEach(function(c){c.onclick=function(ev){ev.stopPropagation();var e=evs[+c.dataset.i];
    pop.innerHTML='<button class="x" aria-label="Close">&times;</button><span class="kind" style="background:'+KC[e.kind]+';margin:0">'+e.kind+'</span><h3 style="margin-top:8px">'+e.name+'</h3><div class="small">'+e.dlabel+'</div><p style="margin:8px 0"><b style="font-size:1.3rem">'+fmt(e.price)+'</b><br><span class="small">'+e.psrc+'</span></p><p style="margin:6px 0;font-size:.92rem">'+e.summary+'</p>'+(e.url?'<a href="'+e.url+'">Read the full story &rarr;</a>':'');
    pop.classList.add('show');var px=+c.getAttribute('cx');pop.style.left=Math.max(4,Math.min(W-pop.offsetWidth-4,px-pop.offsetWidth/2))+'px';pop.style.top=Math.max(4,+c.getAttribute('cy')-pop.offsetHeight-14)+'px';pop.querySelector('.x').onclick=function(){pop.classList.remove('show')}}});
  }
  var drawn=false;function first(){if(!drawn){drawn=true;draw(true)}}
  if(io){var o=new IntersectionObserver(function(es){if(es[0].isIntersecting){first();o.disconnect()}},{threshold:.2});o.observe(box)}else first();
  if(logBtn)logBtn.onclick=function(){state.log=!state.log;logBtn.classList.toggle('on',state.log);logBtn.textContent=state.log?'Log scale: on':'Log scale: off';draw(false)};
  rng.forEach(function(bt){bt.onclick=function(){rng.forEach(function(x){x.classList.remove('on')});bt.classList.add('on');var y=bt.dataset.range,last=data.points[data.points.length-1][0];state.to='';state.from=y==='all'?'':(+last.slice(0,4)-(+y))+last.slice(4);draw(false)}});
  var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(function(){if(drawn)draw(false)},150)});
 });
});
d.querySelectorAll('svg.spark').forEach(function(s){load(s.dataset.coin).then(function(data){var P=data.points.slice(-365),vs=P.map(function(p){return p[1]}),lo=Math.min.apply(0,vs),hi=Math.max.apply(0,vs);
 var path=P.map(function(p,i){return(i?'L':'M')+(i/(P.length-1)*200).toFixed(1)+' '+(52-(p[1]-lo)/(hi-lo||1)*48).toFixed(1)}).join('');
 s.innerHTML='<path d="'+path+'" fill="none" stroke="'+s.dataset.color+'" stroke-width="2.2" class="sl"/>';var l=s.querySelector('.sl'),n=l.getTotalLength();l.style.setProperty('--len',n);l.classList.add('draw')})});
})();
"""
