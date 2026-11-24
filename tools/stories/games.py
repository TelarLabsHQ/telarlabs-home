"""Games for Telar Stories (content pages, so they can carry ads away from the game):
- Memory Match (/games/memory-match/): flip cards to find pairs of Telar Stories characters.
- Story Order (on each story page): tap the four scenes in the order they happened.
Images are made from the app's own backgrounds and characters."""
import os, json
from PIL import Image
from make_packs import PACKS

SITE = '/home/claude/telarlabs-home/stories-site/public/'
CH, BG = SITE + 'assets/ch/', SITE + 'assets/bg/'
GD = SITE + 'games/img/'; os.makedirs(GD, exist_ok=True)

CARDS = [('mira-wave-happy', 'Mira'), ('mochi-sitting', 'Mochi'), ('mei-wave', 'Mei'), ('leo-wave', 'Leo'),
         ('grandma-wave', 'Grandma'), ('biscuit-sitting', 'Biscuit'), ('pip-singing', 'Pip'), ('teacher-clapping', 'Mr. Tan'),
         ('lily-gift', 'Lily'), ('noah-welcome', 'Noah'), ('shepherd-boy-lamb', 'Shepherd boy'), ('donkey-standing', 'Donkey')]

def make_images():
    for k, _ in CARDS:
        c = Image.open(CH + k + '.webp').convert('RGBA'); c.thumbnail((250, 250), Image.LANCZOS)
        im = Image.new('RGBA', (280, 280), (0, 0, 0, 0)); im.alpha_composite(c, ((280 - c.width) // 2, 275 - c.height))
        im.save(GD + 'card-' + k + '.webp', quality=82)
    for slug, d in PACKS.items():
        for i, (bg, chars, cap) in enumerate(d['scenes'], 1):
            im = Image.open(BG + bg + '.webp').convert('RGBA').resize((1280, 720))
            for k, x, y, h in chars:
                c = Image.open(CH + k + '.webp').convert('RGBA'); c = c.resize((round(c.width * h / c.height), h))
                im.alpha_composite(c, (x - c.width // 2, y - h))
            im.convert('RGB').resize((640, 360), Image.LANCZOS).save(GD + f'order-{slug}-{i}.webp', quality=78)

GCSS = '''<style>
.gbox [hidden]{display:none!important}
.gbox{background:var(--bg2);border:1px solid var(--line);border-radius:18px;padding:16px;margin:16px 0 48px}
.gbox h2{margin:0 0 4px}.gsub{color:var(--muted);margin:0 0 12px}
.gbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:12px}
.gbar button,.gbtn{font:inherit;font-weight:800;border-radius:999px;border:2px solid var(--line);background:#2a2533;color:var(--fg);padding:9px 16px;cursor:pointer;touch-action:manipulation}
.gbar button.on,.gbtn.pri{background:var(--accent);border-color:var(--accent);color:#2a0d14}
.gbar .sp{flex:1}.gstat{font-weight:700;color:var(--muted)}
.mm{display:grid;gap:8px;perspective:900px}
.mc{position:relative;aspect-ratio:3/4;border:0;padding:0;background:none;cursor:pointer;touch-action:manipulation}
.mc .in{position:absolute;inset:0;transition:transform .35s;transform-style:preserve-3d}
.mc.up .in,.mc.got .in{transform:rotateY(180deg)}
.mc .f,.mc .b{position:absolute;inset:0;border-radius:12px;backface-visibility:hidden;-webkit-backface-visibility:hidden;display:flex;flex-direction:column;align-items:center;justify-content:center}
.mc .b{background:radial-gradient(circle at 30% 25%,#ffb3c1,#ff8fa3 45%,#d9667c);border:3px solid #ffe1e7;color:#fff;font-size:30px}
.mc .f{transform:rotateY(180deg);background:#fff7ec;border:3px solid #ffd7a8}
.mc .f img{width:88%;height:auto;flex:1;object-fit:contain;min-height:0}.mc .f span{font-weight:800;color:#5a3b2a;font-size:13px;padding-bottom:4px}
.mc.got .f{border-color:#7ed39b;background:#effbf2}
.mwin,.owin{text-align:center;padding:10px 0}.mwin b,.owin b{display:block;font-size:30px;color:var(--accent)}
.oprompt{font-size:22px;font-weight:800;text-align:center;margin:4px 0 10px;min-height:34px}
.oslots{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:12px}
.oslot{aspect-ratio:16/9;border:2px dashed var(--line);border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:800;color:var(--muted);font-size:20px;overflow:hidden;position:relative}
.oslot img{width:100%;height:100%;object-fit:cover}.oslot i{position:absolute;top:3px;left:3px;background:var(--accent);color:#2a0d14;border-radius:999px;width:24px;height:24px;font-style:normal;font-size:14px;display:flex;align-items:center;justify-content:center}
.ocards{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ocards button{border:3px solid transparent;border-radius:12px;padding:0;background:none;cursor:pointer;overflow:hidden;line-height:0;touch-action:manipulation}
.ocards button img{width:100%;height:auto}.ocards button.gone{visibility:hidden}
.ocards button.no{animation:wig .4s;border-color:#ff6b6b}@keyframes wig{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.ocaps{list-style:none;padding:0;margin:10px 0;text-align:left}.ocaps li{padding:6px 0;border-bottom:1px solid var(--line)}
.snd{font-size:20px;padding:6px 10px!important}
</style>'''

SOUND = '''const S={on:true};try{S.on=localStorage.getItem('ts-snd')!=='0'}catch(e){}
let AC=null;function tone(f,d,t){if(!S.on)return;try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();const o=AC.createOscillator(),g=AC.createGain();o.type=t||'sine';o.frequency.value=f;g.gain.setValueAtTime(.0001,AC.currentTime);g.gain.exponentialRampToValueAtTime(.18,AC.currentTime+.02);g.gain.exponentialRampToValueAtTime(.0001,AC.currentTime+d);o.connect(g);g.connect(AC.destination);o.start();o.stop(AC.currentTime+d+.05)}catch(e){}}
const yay=()=>{tone(523,.15);setTimeout(()=>tone(659,.15),110);setTimeout(()=>tone(784,.25),220)},ding=()=>tone(880,.18),boop=()=>tone(220,.2,'triangle');
function sndBtn(b){const f=()=>b.textContent=S.on?'🔊':'🔇';f();b.onclick=()=>{S.on=!S.on;try{localStorage.setItem('ts-snd',S.on?'1':'0')}catch(e){}f()}}'''

def memory_game(up='../../'):
    cards = json.dumps([[f'{up}games/img/card-{k}.webp', n] for k, n in CARDS])
    return GCSS + f'''<div class="gbox" id="mg">
<div class="gbar" id="mgLv"><button data-n="6" class="on">Easy</button><button data-n="8">Medium</button><button data-n="12">Hard</button><span class="sp"></span><span class="gstat">Moves: <b id="mgMoves">0</b></span><button class="snd" id="mgSnd" aria-label="Sound on or off"></button></div>
<div class="mm" id="mgGrid"></div>
<div class="mwin" id="mgWin" hidden><b>🎉 You found them all!</b><p id="mgMsg"></p><button class="gbtn pri" id="mgAgain">Play again</button></div>
</div>
<script>(()=>{{const C={cards};{SOUND}
const $=i=>document.getElementById(i),sh=a=>{{a=a.slice();for(let i=a.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}}return a}};
let n=6,open=[],moves=0,got=0,lock=false;sndBtn($('mgSnd'));
document.querySelectorAll('#mgLv button[data-n]').forEach(b=>b.onclick=()=>{{n=+b.dataset.n;document.querySelectorAll('#mgLv button[data-n]').forEach(x=>x.classList.toggle('on',x===b));deal()}});
function deal(){{open=[];moves=0;got=0;lock=false;$('mgMoves').textContent=0;$('mgWin').hidden=true;const g=$('mgGrid');g.innerHTML='';
 const cols=n===12&&innerWidth>620?6:4;g.style.gridTemplateColumns='repeat('+cols+',1fr)';g.style.maxWidth=(cols*110)+'px';g.style.margin='0 auto';
 sh(sh(C).slice(0,n).flatMap(c=>[c,c])).forEach(c=>{{const b=document.createElement('button');b.className='mc';b.dataset.k=c[1];b.setAttribute('aria-label','Card');
  b.innerHTML='<div class="in"><div class="b">★</div><div class="f"><img src="'+c[0]+'" alt=""><span>'+c[1]+'</span></div></div>';b.onclick=()=>flip(b);g.appendChild(b)}})}}
function flip(b){{if(lock||b.classList.contains('up')||b.classList.contains('got'))return;b.classList.add('up');b.setAttribute('aria-label',b.dataset.k);open.push(b);tone(660,.08);
 if(open.length<2)return;moves++;$('mgMoves').textContent=moves;const[a,c]=open;open=[];
 if(a.dataset.k===c.dataset.k){{setTimeout(()=>{{a.classList.add('got');c.classList.add('got');ding()}},250);got++;if(got===n)setTimeout(win,700)}}
 else{{lock=true;setTimeout(()=>{{a.classList.remove('up');c.classList.remove('up');a.setAttribute('aria-label','Card');c.setAttribute('aria-label','Card');lock=false}},950)}}}}
function win(){{yay();const k='ts-mm-'+n;let best=0;try{{best=+localStorage.getItem(k)||0}}catch(e){{}}
 const stars=moves<=n*1.5?'⭐⭐⭐':moves<=n*2.2?'⭐⭐':'⭐';
 $('mgMsg').textContent=stars+' '+moves+' moves'+(!best||moves<best?' · New best!':' · Best: '+best+' moves');if(!best||moves<best)try{{localStorage.setItem(k,moves)}}catch(e){{}}
 $('mgWin').hidden=false;$('mgWin').scrollIntoView({{block:'nearest',behavior:'smooth'}})}}
$('mgAgain').onclick=deal;deal()}})();</script>'''

def order_game(slug, up='../../'):
    sc = json.dumps([[f'{up}games/img/order-{slug}-{i}.webp', cap] for i, (_, _, cap) in enumerate(PACKS[slug]['scenes'], 1)], ensure_ascii=False)
    return f'''<div class="gbox" id="og">
<div class="gbar"><span class="gstat">Tap the pictures in the order they happened.</span><span class="sp"></span><button class="snd" id="ogSnd" aria-label="Sound on or off"></button></div>
<div class="oprompt" id="ogP"></div>
<div class="oslots" id="ogSlots"></div>
<div class="ocards" id="ogCards"></div>
<div class="owin" id="ogWin" hidden><b>🎉 You did it!</b><p>Now tell the story in your own words, one picture at a time.</p><ol class="ocaps" id="ogCaps"></ol><button class="gbtn pri" id="ogAgain">Play again</button></div>
</div>
<script>(()=>{{const SC={sc};{SOUND}
const $=i=>document.getElementById(i),sh=a=>{{a=a.slice();for(let i=a.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}}return a}};
const P=['What happened first?','What happened next?','And then?','What happened last?'];let step=0;sndBtn($('ogSnd'));
function deal(){{step=0;$('ogWin').hidden=true;$('ogCards').hidden=false;$('ogP').textContent=P[0];
 $('ogSlots').innerHTML=SC.map((_,i)=>'<div class="oslot">'+(i+1)+'</div>').join('');$('ogCards').innerHTML='';
 let idx=sh([0,1,2,3]);if(idx.join()==='0,1,2,3')idx=[2,0,3,1];
 idx.forEach(i=>{{const b=document.createElement('button');b.innerHTML='<img src="'+SC[i][0]+'" alt="'+SC[i][1].replace(/"/g,'&quot;')+'" width="640" height="360">';b.onclick=()=>tap(b,i);$('ogCards').appendChild(b)}})}}
function tap(b,i){{if(b.classList.contains('gone'))return;
 if(i!==step){{b.classList.remove('no');void b.offsetWidth;b.classList.add('no');boop();$('ogP').textContent='Not yet! Try another picture.';setTimeout(()=>{{if(step<4)$('ogP').textContent=P[step]}},1200);return}}
 b.classList.add('gone');const s=$('ogSlots').children[step];s.innerHTML='<img src="'+SC[i][0]+'" alt=""><i>'+(step+1)+'</i>';ding();step++;
 if(step<4){{$('ogP').textContent=P[step];return}}
 $('ogP').textContent='';$('ogCards').hidden=true;$('ogCaps').innerHTML=SC.map(x=>'<li>'+x[1]+'</li>').join('');$('ogWin').hidden=false;setTimeout(yay,200)}}
$('ogAgain').onclick=deal;deal()}})();</script>'''

MEMORY_TEXT = '''<h2>How to play</h2>
<ol><li>Choose <b>Easy</b> (6 pairs), <b>Medium</b> (8 pairs) or <b>Hard</b> (12 pairs).</li>
<li>Tap a card to turn it over, then tap another one.</li>
<li>If the two cards show the same character, they stay open. If not, they turn back over. Try to remember where each one was!</li>
<li>Find all the pairs in as few moves as you can.</li></ol>
<p>The 🔊 button turns the sounds on or off.</p>

<h2>Meet the characters</h2>
<p>Every card is a character from Telar Stories: Mira and her cat Mochi, Mei, Leo and Grandma, Biscuit the dog and Pip the bird, Mr. Tan the teacher, Lily from <a href="../../stories/the-christmas-gift/">The Christmas Gift</a>, Noah from <a href="../../stories/noahs-ark/">Noah’s Ark</a>, the shepherd boy from <a href="../../stories/the-first-christmas/">The First Christmas</a> and Mary’s donkey. Children who know the stories love finding their favorites.</p>

<h2>What memory games help with</h2>
<ul><li><b>Working memory:</b> holding where each card was while looking for its pair.</li>
<li><b>Focus and patience:</b> slowing down and remembering instead of tapping at random.</li>
<li><b>Language:</b> say each character’s name out loud when the card turns over. Younger children can practice naming, older ones can read the name under the picture.</li>
<li><b>Taking turns:</b> play together, one card pair each, and count who finds more.</li></ul>

<h2>Tips for parents and teachers</h2>
<ul><li>Start with <b>Easy</b> for ages 3 to 5, and move up when your child finishes with three stars.</li>
<li>Talk about the characters: “Where did we see Mochi? What did Lily give Mr. Ben?”</li>
<li>After a round, open a story with the same characters in Telar Stories and make a short video together.</li>
<li>On a classroom screen, let children come up one at a time to choose two cards.</li></ul>
<p>The game is free, needs no sign-up and works on phones, tablets and computers. Nothing is saved except the best score on this device.</p>'''

ORDER_TEXT = '''<p>Each story has its own Story Order game. Children see four pictures from the story, mixed up, and tap them in the order they happened. When they finish, the pictures line up with a short sentence for each one, ready for retelling.</p>
<h2>Why sequencing matters</h2>
<p>Putting events in order is one of the first reading comprehension skills. It helps children understand that stories have a beginning, a middle and an end, and gives them words like <i>first</i>, <i>next</i>, <i>then</i> and <i>last</i>. Retelling a story in order is also great speaking practice.</p>'''

def games_hub(up='../'):
    tiles = ''.join(f'<a class="card" href="{up}stories/{s}/#play"><b>Story Order: {E(PACKS[s]["title"])}</b><span>Put four pictures from the story in order.</span></a>' for s in PACKS)
    return (f'<h1>Games for kids</h1><p class="lead">Free, gentle games with the Telar Stories characters. No sign-up, no downloads, made for ages 3 to 8.</p>'
            f'<div class="cards"><a class="card" href="memory-match/"><b>Memory Match</b><span>Flip the cards and find the pairs: Mira, Mochi, Mei, Leo, Biscuit, Pip and friends.</span></a>{tiles}</div>'
            f'<h2>Story Order</h2>{ORDER_TEXT}'
            '<h2>Playing together</h2><p>These games are made to be played with a grown-up nearby. Talk about the pictures, ask questions and celebrate together. For more ideas, each story page has questions to talk about and a free printable activity pack.</p>')

def E(s): import html; return html.escape(str(s), quote=True)
