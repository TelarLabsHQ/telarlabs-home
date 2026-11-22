"""Short how-to guides inside the Telar Stories prototype (/stories-demo/guides/). Hidden from search until launch."""
import os, html
OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'public', 'stories-demo', 'guides')
E = html.escape
G = [
 ('first-story-video', 'Make your first story video in five minutes', 'Use a ready-made story as it is, play it, and save the video.', '''
<p class="lead">You don't need to write or draw anything to get started. Every ready-made story already has pictures, words, gentle movements and a narrator's voice.</p>
<h2>1. Pick a story</h2>
<p>At the top of the page, under <b>Ready-made stories</b>, tap a story such as <i>Mira and the Rainy Day</i> or <i>The Lost Sheep</i>. If you've already changed the story on screen, the app asks before replacing it.</p>
<h2>2. Watch it</h2>
<p>Press <b>▶ Play</b> at the top. The story plays scene by scene, with the narrator reading the words. The strip of small pictures under the main picture shows every scene. Tap one to jump to it.</p>
<h2>3. Save the video</h2>
<p>Press <b>⬇ Make video</b>. Keep the page open while the video is made; it can take up to as long as the story itself. When it's ready, tap <b>Download video</b>.</p>
<ul><li>On most phones and computers the video is saved as <b>MP4</b>, which plays almost everywhere, including CapCut, Messenger and TVs.</li>
<li>Some browsers save <b>WebM</b> instead. It plays in Chrome and on YouTube; for CapCut on some phones, convert it to MP4 first.</li></ul>
<h2>4. Share it</h2>
<p>Send the video in your class or family group chat, show it on the classroom TV, or upload it to YouTube or Facebook. See <a href="../share-and-keep/">Sharing your video and keeping your work</a>.</p>
<p class="tip"><b>Tip:</b> Using a sample exactly as it is is perfectly fine. Change only what you want, like a child's name, and leave the rest.</p>'''),
 ('write-a-story', 'Write a short story in ten scenes', 'A simple plan for a story children can follow, with tips for words that sound good read aloud.', '''
<p class="lead">Most good picture-book stories follow the same shape: someone wants something, something gets in the way, and it works out in the end. Ten scenes of one to three sentences each make a story of about one and a half minutes.</p>
<h2>A ten-scene plan</h2>
<ol><li><b>Title.</b> The name of the story, over a picture of the main character.</li>
<li><b>Meet the hero.</b> Who they are and where they are.</li>
<li><b>What they want.</b> A wish, a worry or a question.</li>
<li><b>The problem.</b> Something gets in the way.</li>
<li><b>A first try.</b> It doesn't quite work.</li>
<li><b>A helper or an idea.</b> A friend, a parent, a teacher or a surprise.</li>
<li><b>Trying again.</b> This time with help.</li>
<li><b>The big moment.</b> The problem is solved.</li>
<li><b>How everyone feels.</b> Happy, proud, thankful.</li>
<li><b>The lesson or a warm goodbye.</b> One simple sentence to remember.</li></ol>
<h2>Words that read aloud well</h2>
<ul><li><b>Keep sentences short.</b> One idea per sentence. Aim for 15 to 40 words in each scene.</li>
<li><b>Use names often.</b> "Mira looked outside" is easier for young listeners than "She looked outside".</li>
<li><b>Add sounds and feelings.</b> "Bump!", "Splash!", "Mira sighed." Listeners love them.</li>
<li><b>Repeat a line.</b> A phrase that comes back, like "But the rain would not stop," helps children follow along.</li>
<li><b>End with something to remember.</b> A kind lesson, a Bible verse or a simple "Good night".</li></ul>
<h2>Putting it in the app</h2>
<p>Tap a scene in the strip, then type in <b>Words & voice</b>. Use <b>+ Scene</b> to add a scene, or <b>Duplicate</b> to copy the current one with its picture and characters. You can end the story however you like; nothing is added automatically.</p>'''),
 ('pictures-and-movement', 'Choosing pictures, characters and gentle movement', 'Set each scene with a background, characters, poses, light and a slow camera.', '''
<p class="lead">Telar Stories is designed to look like a picture book that talks: calm pictures, small movements and nothing flashy. A few simple choices make each scene clear and easy to watch.</p>
<h2>Backgrounds</h2>
<p>Open the <b>Background</b> tab and tap a place for the scene. Keep the same background for scenes that happen in the same place; change it when the story moves somewhere new. It helps young viewers follow the story.</p>
<h2>Characters and poses</h2>
<p>In the <b>Characters</b> tab, tap a pose to add it. Then tap the character in the picture to:</p>
<ul><li><b>Move</b> it by dragging.</li><li><b>Flip</b> it to face the other way, for example toward another character.</li>
<li>Make it <b>Smaller</b> or <b>Bigger</b>, or <b>Bring to front</b>.</li><li><b>Remove</b> it from the scene.</li></ul>
<p>Two or three characters per scene is plenty. Put the character who is speaking a little bigger or nearer the middle.</p>
<h2>Movement and light</h2>
<ul><li><b>Movement:</b> <i>gentle breathing</i> for calm scenes, <i>hop</i> for happy moments, <i>walk across</i> when someone arrives or leaves, and <i>steady</i> for no motion at all.</li>
<li><b>Light:</b> <i>day</i>, <i>sunset</i> or <i>night</i>, to match the background.</li>
<li><b>Camera:</b> a <i>slow zoom in</i> draws attention to a moment, a <i>slow zoom out</i> works well at the end, and <i>still</i> keeps everything calm.</li></ul>
<p class="tip"><b>Tip:</b> If a scene feels busy, remove a character or switch the camera to still. Simple scenes are easier for children to watch.</p>'''),
 ('voices-and-pronunciation', 'Voices: the AI storyteller, your own voice, and saying names right', 'Choose a narrator, record yourself, and fix words the AI voice says wrong.', '''
<p class="lead">Every scene can have a voice. You can use a free AI storyteller voice, record your own, or mix both in one story.</p>
<h2>The AI storyteller voice</h2>
<p>In <b>Words & voice</b>, choose a voice such as <i>Warm storyteller (female)</i> or <i>Calm storyteller (male)</i>, and a speed: Slow, Normal or Faster. Then tap <b>Make AI voice for this scene</b>, or <b>For all scenes</b>.</p>
<ul><li>The AI voice runs inside your browser, so your words aren't sent anywhere.</li>
<li>The first time, your device downloads the voice, about 90 MB. Use Wi-Fi if you can. After that it's much faster.</li>
<li>Keep the page open until the voices are ready.</li></ul>
<h2>Recording your own voice</h2>
<p>Tap <b>● Record my voice</b>, read the scene's words, then tap Stop. Use <b>▶ Listen</b> to check it. With a recording, the scene lasts as long as your voice plus a short pause.</p>
<ul><li>Record in a quiet room, with the phone about a hand's width from your mouth.</li>
<li>Read a little slower than you normally speak, and smile; listeners can hear it.</li>
<li>Children, parents and grandparents can record their own lines for a family story.</li></ul>
<h2>When the AI says a word wrong</h2>
<p>Names and words from other languages are often hard for AI voices. Take Mochi, the puppy in our stories: the AI voice may say "MOH-chee" or "MOH-kee", but we want "mow-chee". Open <b>Pronunciation help</b>, then write the word, an equals sign, and how it sounds:</p>
<pre>Mochi = mowchee</pre>
<p>Add more words the same way, one per line:</p>
<pre>Mochi = mowchee
lola = law-lah
Lucia = loo-see-ah</pre>
<ul><li><b>Use small letters only.</b> Capital letters make the voice spell the word out, like an acronym: "MOW-chee" would come out as "M-O-W chee".</li>
<li>Use hyphens to split syllables if it helps.</li>
<li>Tap <b>▶ Hear the words</b> to test, then <b>Save & update voices</b>.</li>
<li>Captions on the video keep your original spelling.</li></ul>'''),
 ('share-and-keep', 'Sharing your video and keeping your work', 'Where your video and your story are saved, how to share them, and how not to lose them.', '''
<p class="lead">Telar Stories works entirely in your browser. That keeps your stories private, but it also means a few things are worth knowing.</p>
<h2>Where your work is saved</h2>
<ul><li>Your story, pictures and voices are saved <b>in this browser on this device</b>. Close the page and come back later, and it's still there.</li>
<li>It isn't saved online, so it won't appear on your other devices.</li>
<li>Clearing your browser's data, using a private window, or a phone freeing up space can remove it.</li></ul>
<p class="tip"><b>Keep your finished video.</b> Once you're happy with a story, press <b>Make video</b> and download it. The video file is yours to keep, even if the browser's data is cleared.</p>
<h2>Sharing</h2>
<ul><li><b>Group chats:</b> send the downloaded video in Messenger, WhatsApp, Viber or Telegram.</li>
<li><b>Classroom or church:</b> play it on a TV or projector from a laptop or USB stick.</li>
<li><b>YouTube and Facebook:</b> upload it like any other video. Stories are 16:9, so they fit YouTube and TVs.</li>
<li><b>Editing apps:</b> open the MP4 in CapCut or a similar app to add your own music or intro.</li></ul>
<h2>Music</h2>
<p>Under <b>Whole story</b>, choose background music: Gentle, Happy, Adventure, Dreamy, your own music file, or none. If you use your own music, make sure you're allowed to use it, especially on YouTube and Facebook.</p>
<h2>Respect and privacy</h2>
<ul><li>Use children's real names only when the family is happy for the video to be shared.</li>
<li>For public posts, consider using a first name only, or a made-up name.</li></ul>'''),
]
CSS = '''<style>:root{--bg:#16131c;--bg2:#1f1b27;--fg:#f4f1f8;--muted:#a8a1b1;--line:#352f40;--accent:#ff8fa3}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
a{color:var(--accent)}.top{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--line);background:#121017;position:sticky;top:0}
.top b{font-size:17px}.top b span{color:var(--accent)}.top .sp{flex:1}.btn{border:1px solid var(--line);background:#2a2533;color:var(--fg);padding:8px 14px;border-radius:10px;font-weight:700;text-decoration:none;font-size:14px}
.btn.primary{background:var(--accent);color:#2a0d14;border-color:var(--accent)}main{max-width:760px;margin:0 auto;padding:22px 16px 60px}
h1{font-size:30px;line-height:1.2;margin:8px 0 10px}h2{font-size:21px;margin:28px 0 8px}.lead{font-size:18px;color:#e9e2f0}
.crumb{font-size:14px;color:var(--muted)}.crumb a{color:var(--muted)}li{margin:4px 0}
.tip{background:var(--bg2);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:12px 14px}
pre{background:#0f0d13;border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-size:15px;overflow-x:auto}
.cards{display:grid;gap:12px;margin-top:18px}.card{display:block;background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:16px 18px;color:var(--fg);text-decoration:none}
.card:hover{border-color:var(--accent)}.card b{font-size:18px}.card span{display:block;color:var(--muted);font-size:15px;margin-top:4px}
.next{margin-top:34px;display:flex;gap:10px;flex-wrap:wrap}</style>'''
def page(title, desc, body, depth):
    up = '../' * depth
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>{E(title)} – Telar Stories</title><meta name="description" content="{E(desc)}">{CSS}</head><body>
<header class="top"><b>Telar <span>Stories</span></b><div class="sp"></div><a class="btn" href="{up}guides/">Guides</a><a class="btn primary" href="{up}">Open the app</a></header>
<main>{body}</main></body></html>'''
os.makedirs(OUT, exist_ok=True)
cards = ''.join(f'<a class="card" href="{s}/"><b>{E(t)}</b><span>{E(d)}</span></a>' for s, t, d, _ in G)
open(os.path.join(OUT, 'index.html'), 'w').write(page('Guides', 'How to make story videos with Telar Stories.',
    '<h1>Telar Stories guides</h1><p class="lead">Short, friendly guides for making story videos. No editing skills needed.</p>' + f'<div class="cards">{cards}</div>', 1))
for i, (s, t, d, body) in enumerate(G):
    nxt = G[i + 1] if i + 1 < len(G) else None
    foot = '<div class="next">' + (f'<a class="btn" href="../{nxt[0]}/">Next: {E(nxt[1])} →</a>' if nxt else '') + '<a class="btn primary" href="../../">Open the app</a></div>'
    os.makedirs(os.path.join(OUT, s), exist_ok=True)
    open(os.path.join(OUT, s, 'index.html'), 'w').write(page(t, d, f'<p class="crumb"><a href="../">Guides</a></p><h1>{E(t)}</h1>{body}{foot}', 2))
print('built', len(G), 'guides')
