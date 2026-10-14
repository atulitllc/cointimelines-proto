
(function(){
var d=document,R=d.documentElement.getAttribute('data-root')||'./';
var mb=d.querySelector('.menu-btn');if(mb)mb.onclick=function(){d.querySelector('nav.main').classList.toggle('open')};
var io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');if(e.target.dataset.count)count(e.target);io.unobserve(e.target)}})},{threshold:.12}):null;
d.querySelectorAll('.reveal,[data-count]').forEach(function(el){io?io.observe(el):el.classList.add('in')});
function count(el){var n=+el.dataset.count,t0=performance.now();(function f(t){var k=Math.min(1,(t-t0)/1400);el.textContent=Math.round(n*(1-Math.pow(1-k,3))).toLocaleString();if(k<1)requestAnimationFrame(f)})(t0)}
// newsletter
d.querySelectorAll('form.nl').forEach(function(f){f.onsubmit=function(e){e.preventDefault();var v=f.email.value.trim(),m=f.querySelector('.msg')||f.parentNode.querySelector('.msg');if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)){m.textContent='Please enter a valid email address.';return}
try{var l=JSON.parse(localStorage.getItem('ct-newsletter')||'[]');if(l.indexOf(v)<0)l.push(v);localStorage.setItem('ct-newsletter',JSON.stringify(l))}catch(x){}
m.textContent='Saved on this device only. Nothing is sent yet; the newsletter has not launched.';f.reset()}});
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
