"""How-to guides for Telar Stories (stories.telarlabs.net/guides/). Public content pages with ads; the app itself has none."""
import os, html, json
# soft note for ad-blocker users when they download printables: off until AdSense ads are live ("adblock_note" in site.config.json)
ADNOTE = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'site.config.json'))).get('adblock_note')
ADNOTE_JS = '''<script>(function(){function blocked(){return !!window.tsAdBlocked}
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[download]');if(!a)return;try{if(sessionStorage.getItem('tsAdNote'))return}catch(x){}
setTimeout(function(){if(!blocked()||document.querySelector('.adnote'))return;try{sessionStorage.setItem('tsAdNote','1')}catch(x){}
var n=document.createElement('div');n.className='adnote';n.setAttribute('role','status');n.innerHTML='<span style="font-size:24px">💛</span><div><b>Your download is starting.</b><span>Telar Stories stays free thanks to ads. If you can, please allow ads on this site.</span></div><button type="button">OK</button>';
n.querySelector('button').onclick=function(){n.remove()};document.body.appendChild(n);setTimeout(function(){if(n.parentNode)n.remove()},14000)},1200)});})();</script>
<style>.adnote{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:60;display:flex;gap:12px;align-items:center;width:min(520px,calc(100vw - 24px));background:var(--bg2);color:var(--fg);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:14px;padding:12px 14px;box-shadow:0 12px 32px rgba(0,0,0,.45)}.adnote div{flex:1;font-size:14px;line-height:1.4}.adnote b{display:block;font-size:15px}.adnote span{color:var(--muted)}.adnote button{background:var(--accent);color:#1b1206;border:0;border-radius:9px;padding:8px 14px;font-weight:700;cursor:pointer}</style>''' if ADNOTE else ''
OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'stories-site', 'public', 'guides')
E = html.escape
G = [
 ('first-story-video', 'Make your first story video in five minutes', 'Use a ready-made story as it is, play it, and save the video.', '''
<p class="lead">You don't need to write or draw anything to get started. Every ready-made story already has pictures, words, gentle movements and a narrator's voice.</p>
<h2>1. Pick a story</h2>
<p>At the top of the page, under <b>Ready-made stories</b>, tap a story such as <i>Mira and the Rainy Day</i> or <i>The Lost Sheep</i>. If you've already changed the story on screen, the app asks before replacing it.</p>
<h2>2. Watch it</h2>
<p>Press <b>▶ Play</b> at the top. The story plays scene by scene, with the narrator reading the words. The strip of small pictures under the main picture shows every scene. Tap one to jump to it.</p>
<h2>3. Save the video</h2>
<p>Press <b>⬇ Make video</b>. A progress bar and a percentage show how far along it is. Keep the screen open while the video is made: if you switch apps or lock your phone, it pauses and continues when you come back.</p>
<p>When it reaches 100%, the video is <b>saved automatically</b> to your Downloads, with the story's name and the date in the file name. On phones, <b>Share or save to phone</b> sends it straight to your gallery, Messenger or another app, and <b>Save again</b> downloads another copy.</p>
<ul><li>Videos are saved as <b>MP4</b>, which plays almost everywhere, including CapCut, Messenger and TVs.</li>
<li>On a few phones the app uses a slower, steadier way to make the video. It tells you when it does; just keep the screen open a little longer.</li></ul>
<h2>4. Share it</h2>
<p>Send the video in your class or family group chat, show it on the classroom TV, or upload it to YouTube or Facebook. See <a href="../share-and-keep/">Sharing your video and keeping your work</a>.</p>
<p class="tip"><b>Tip:</b> Using a sample exactly as it is is perfectly fine. Change only what you want, like a child's name, and leave the rest.</p>
<h2>Which ready-made story to start with</h2>
<table><tr><th>Story</th><th>Good for</th></tr>
<tr><td><i>Mira and the Rainy Day</i></td><td>Young children, bedtime, and a gentle lesson about finding joy on a boring day.</td></tr>
<tr><td><i>The First Christmas</i></td><td>Sunday school, Christmas programs and family devotions.</td></tr>
<tr><td><i>The Lost Sheep</i></td><td>A short Bible parable about how much each person matters.</td></tr>
<tr><td><i>The Christmas Gift</i></td><td>Kindness and giving, for classrooms and families in December.</td></tr>
<tr><td><i>Noah's Ark</i></td><td>A favorite Bible story with animals, rain and a rainbow.</td></tr>
<tr><td><i>Friends Around the World</i></td><td>Welcoming new classmates and learning hello in other languages.</td></tr></table>
<h2>Small changes that make it yours</h2>
<ul><li><b>Change a name.</b> Swap the main character's name for your child's or your class's name. The AI voice will read it the new way.</li>
<li><b>Change the last scene.</b> Add a line for your class, like "Thank you, Grade 2, for listening!"</li>
<li><b>Record the first line yourself.</b> A parent's or teacher's real voice at the start makes children pay attention.</li>
<li><b>Pick different music.</b> Under <b>Whole story</b>, try another track; it changes the mood a lot.</li></ul>
<h2>How long does it take?</h2>
<p>Playing a ready-made story takes a minute or two. Making the video usually takes less time than the story itself on a computer, and a bit longer on an older phone. If you made changes to the words, making new AI voices takes up to a minute per scene the first time.</p>'''),
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
<p>Tap a scene in the strip, then type in <b>Words & voice</b>. Use <b>+ Scene</b> to add a scene, or <b>Duplicate</b> to copy the current one with its picture and characters. You can end the story however you like; nothing is added automatically.</p>
<h2>An example: "Leo and the Big Puddle"</h2>
<ol><li><b>Title:</b> Leo and the Big Puddle.</li>
<li>Leo loved his new red boots. He wore them every day, even when the sun was shining.</li>
<li>"I want to jump in a puddle," said Leo. But it had not rained for weeks.</li>
<li>Leo looked in the garden. No puddles. He looked by the gate. No puddles.</li>
<li>He tried to make a puddle with a cup of water. It was much too small.</li>
<li>"Be patient," said Dad. "The rain will come."</li>
<li>That night, Leo heard a sound on the window. Tap, tap, tap!</li>
<li>In the morning, the biggest puddle he had ever seen was waiting by the door.</li>
<li>SPLASH! Leo laughed and laughed.</li>
<li>Some good things are worth waiting for.</li></ol>
<p>Notice the repeated line ("No puddles"), the sound words ("Tap, tap, tap", "SPLASH!"), and the short lesson at the end.</p>
<h2>Common mistakes</h2>
<ul><li><b>Too many words in one scene.</b> If a caption fills more than three lines, split it into two scenes.</li>
<li><b>Too many characters.</b> One hero and one or two helpers are enough for a short story.</li>
<li><b>No problem to solve.</b> A story where nothing goes wrong is hard to remember. Even a small problem, like a missing toy, gives the story a shape.</li>
<li><b>A rushed ending.</b> Give the happy moment its own scene, then add one calm scene to finish.</li></ul>
<p>Next, choose pictures for each scene: <a href="../pictures-and-movement/">Choosing pictures, characters and gentle movement</a>.</p>'''),
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
<p class="tip"><b>Tip:</b> If a scene feels busy, remove a character or switch the camera to still. Simple scenes are easier for children to watch.</p>
<h2>Characters you can use in any story</h2>
<p>The <b>Characters</b> tab is grouped. Some groups belong to a ready-made story, like <i>Noah's Ark</i>, but every character can be used in your own stories too. For everyday stories, start with:</p>
<ul><li><b>Mira &amp; Mochi:</b> a little girl and her cat, in many poses.</li>
<li><b>Mei's family:</b> Mei, her mom and her dad, with poses for standing, waving, walking, hugging, reading and more.</li>
<li><b>Friends Around the World:</b> five children and their teacher, Ms. Rose, for school stories.</li></ul>
<p>Each pose is a separate picture. To show a character doing something new in the next scene, add the same character in a different pose, for example <i>Mei · walk</i> in one scene and <i>Mei · wave</i> in the next.</p>
<h2>Backgrounds for every season</h2>
<p>The <b>Background</b> tab has two groups. <b>Story places</b> are homes, schools, gardens and Bible settings. <b>From Telar Clips</b> are scenes from our free video library, good for seasons and celebrations: a snowy Christmas village, New Year fireworks, a crescent-moon town for Ramadan, temple steps with lamps for Diwali, green hills with a rainbow, an autumn park, a tropical beach and more.</p>
<p class="tip"><b>Tip:</b> A few backgrounds have water across the bottom, like the harbour and the starry lake. Use them for opening or closing scenes without characters, or for words like "The stars came out over the lake."</p>
<h2>Making characters look right together</h2>
<ul><li><b>Keep sizes believable.</b> Children should be shorter than adults. Use <b>Smaller</b> and <b>Bigger</b> until they look right standing together.</li>
<li><b>Put feet on the ground.</b> Drag characters so their feet sit on a floor, path or grass, not in the sky.</li>
<li><b>Face each other when talking.</b> Use <b>Flip</b> so two characters look at each other.</li>
<li><b>Match the light.</b> Use <i>sunset glow</i> or <i>night</i> on characters in evening scenes, so they don't look too bright.</li></ul>'''),
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
<p>Names and words from other languages are often hard for AI voices. Take Mochi, the cat in our stories: the AI voice may say "MOH-chee" or "MOH-kee", but we want "mow-chee". Open <b>Pronunciation help</b>, then write the word, an equals sign, and how it sounds:</p>
<pre>Mochi = mowchee</pre>
<p>Add more words the same way, one per line:</p>
<pre>Mochi = mowchee
lola = law-lah
Lucia = loo-see-ah</pre>
<ul><li><b>Use small letters only.</b> Capital letters make the voice spell the word out, like an acronym: "MOW-chee" would come out as "M-O-W chee".</li>
<li>Use hyphens to split syllables if it helps.</li>
<li>Tap <b>▶ Hear the words</b> to test, then <b>Save & update voices</b>.</li>
<li>Captions on the video keep your original spelling.</li></ul>
<h2>Which voice to choose</h2>
<table><tr><th>Voice</th><th>Good for</th></tr>
<tr><td>Warm storyteller (female)</td><td>Most stories, bedtime and Bible stories. The voice used in our ready-made stories.</td></tr>
<tr><td>Bright and cheerful (female)</td><td>Happy, lively stories for younger children.</td></tr>
<tr><td>Calm storyteller (male)</td><td>Gentle stories and lessons, and a change of narrator.</td></tr>
<tr><td>Deep voice (male)</td><td>Big moments, like a storm, a king or a giant.</td></tr>
<tr><td>British (female and male)</td><td>Classic fairy-tale feel, or for listeners used to British English.</td></tr></table>
<p>Use one narrator for the whole story so it feels like one person reading. Pick the speed for your listeners: <b>Slow</b> for young children and language learners, <b>Normal</b> for most stories.</p>
<h2>Mixing voices</h2>
<p>Each scene keeps its own voice, so you can mix: the AI voice reads the story and a child records the last line, or Dad records the father's words while the AI voice narrates. The scene strip shows a 🎙 on scenes that have a voice.</p>
<h2>If the AI voice is slow or won't start</h2>
<ul><li>The first time, wait for the download to finish; the progress shows in megabytes.</li>
<li>Use a strong Wi-Fi connection for the first download.</li>
<li>Close other tabs and apps on older phones.</li>
<li>If it still won't start, record your own voice for that scene, or try on a computer.</li></ul>'''),
 ('share-and-keep', 'Sharing your video and keeping your work', 'Where your video and your story are saved, how to share them, and how not to lose them.', '''
<p class="lead">Telar Stories works entirely in your browser. That keeps your stories private, but it also means a few things are worth knowing.</p>
<h2>Where your work is saved</h2>
<ul><li>Your story, pictures and voices are saved <b>in this browser on this device</b>. Close the page and come back later, and it's still there.</li>
<li>It isn't saved online, so it won't appear on your other devices by itself.</li>
<li>Clearing your browser's data, using a private window, or a phone freeing up space can remove it.</li></ul>
<h2>Save a backup</h2>
<p>Under <b>Keep your story safe</b>, tap <b>Save a backup</b>. You get one file ending in <b>telar-story-backup.json</b> with the whole story: every scene, its picture and characters, the voices, the music choice and your pronunciation list. Keep it in Google Drive, email it to yourself, or copy it to a USB stick.</p>
<p>To continue on another phone or computer, open Telar Stories there, tap <b>Open a backup</b> and choose the file. The app asks before replacing the story on screen.</p>
<ul><li>Don't open the backup file by itself; it only shows computer code. Always open it from Telar Stories.</li>
<li>If you used your own music file, choose it again after opening the backup.</li></ul>
<p class="tip"><b>Keep your finished video.</b> Once you're happy with a story, press <b>Make video</b> and download it. The video file is yours to keep, even if the browser's data is cleared.</p>
<h2>Sharing</h2>
<ul><li><b>Group chats:</b> send the downloaded video in Messenger, WhatsApp, Viber or Telegram.</li>
<li><b>Classroom or church:</b> play it on a TV or projector from a laptop or USB stick.</li>
<li><b>YouTube and Facebook:</b> upload it like any other video. Stories are 16:9, so they fit YouTube and TVs.</li>
<li><b>Editing apps:</b> open the MP4 in CapCut or a similar app to add your own music or intro.</li></ul>
<h2>Music</h2>
<p>Under <b>Whole story</b>, choose background music: <i>Gentle: Soft piano</i>, <i>Warm and happy: Picnic</i> or <i>Sunday</i>, <i>Easy and happy: Playful</i> or <i>Garden</i>, your own music file, or no music. Our music is made for Telar Stories and free to use in your videos. If you use your own music, make sure you're allowed to use it, especially on YouTube and Facebook.</p>
<h2>Respect and privacy</h2>
<ul><li>Use children's real names only when the family is happy for the video to be shared.</li>
<li>For public posts, consider using a first name only, or a made-up name.</li></ul>
<h2>Showing it to a group</h2>
<ul><li><b>On a TV or projector,</b> play the downloaded MP4 file rather than the app itself. The video plays smoothly and doesn't need the internet.</li>
<li><b>Check the sound</b> before the class or service. Narration is easier to hear through a speaker than from a laptop.</li>
<li><b>Pause and ask questions.</b> Stop after a scene and ask, "What do you think happens next?"</li></ul>
<h2>Internet and data</h2>
<p>The first visit downloads the pictures you use, and the first AI voice downloads about 90 MB. After that, much of it loads from your device. Use Wi-Fi for the first AI voice if you can. Playing and saving your video doesn't use the internet.</p>'''),
 ('bible-story-sunday-school', 'Make a Bible story video for Sunday school', 'Plan, write and narrate a short Bible story video children can follow, with tips for reading Scripture aloud.', '''
<p class="lead">A short narrated video is a gentle way to open a Sunday school lesson, a children's message or a family devotion. Telar Stories includes three ready-made Bible stories, and you can make your own.</p>
<h2>Start with a ready-made story</h2>
<p><i>The First Christmas</i>, <i>The Lost Sheep</i> and <i>Noah's Ark</i> are ready to play. Each has pictures, words and a narrator. Use one as it is, or change the words to match the Bible version your church uses.</p>
<h2>Choose a story for your own video</h2>
<p>Pick a story with a clear beginning, middle and end, and one main lesson. Stories that work well for young children:</p>
<ul><li><b>Parables:</b> the lost sheep, the lost coin, the good Samaritan, the mustard seed.</li>
<li><b>Old Testament stories:</b> creation, Noah, Joseph's coat, baby Moses, David and Goliath, Daniel and the lions, Jonah.</li>
<li><b>Jesus and children:</b> "Let the little children come to me", feeding the five thousand, calming the storm.</li></ul>
<h2>Write it in eight to ten scenes</h2>
<ol><li><b>Title</b> and where the story is found, for example "A story Jesus told. Luke 15."</li>
<li><b>Setting:</b> who is there and where.</li>
<li><b>The problem or the question.</b></li>
<li><b>What happens next,</b> two or three scenes.</li>
<li><b>The turning point:</b> God helps, Jesus speaks, someone chooses to obey.</li>
<li><b>How it ends.</b></li>
<li><b>One sentence to remember,</b> like a short verse or "God never stops looking for us."</li></ol>
<p>Use simple words, and keep each scene to one to three sentences. Short sentences are easier for children to follow when they are read aloud.</p>
<h2>Reading Scripture aloud</h2>
<ul><li><b>Bible names:</b> the AI voice reads most names well. If one sounds wrong, add it to <b>Pronunciation help</b>, for example <code>Goliath = guh-lie-uth</code>. See <a href="../voices-and-pronunciation/">Voices and pronunciation</a>.</li>
<li><b>Quoting a verse:</b> keep it short, and say where it comes from in the caption.</li>
<li><b>Your own voice:</b> many teachers record the verse themselves and let the AI voice read the story. You can mix both in one video.</li></ul>
<h2>Pictures</h2>
<p>Use the Bible settings in <b>Story places</b>: the house in Nazareth, the road to Bethlehem, the stable, fields at night, rocky hills, the pasture and the ark scenes. Characters from the ready-made Bible stories, like the shepherds, Noah's family and the animals, can be reused in new stories.</p>
<h2>Using it in class</h2>
<ul><li>Play the video at the start, then ask two or three questions: "Who was lost? Who looked for it? How did the shepherd feel?"</li>
<li>Pause before the last scene and ask the children to guess the ending.</li>
<li>Send the video to parents afterwards, so families can talk about the story at home.</li></ul>
<p class="tip"><b>Tip:</b> Keep videos between one and three minutes. Young children listen best to short stories they can watch more than once.</p>
<h2>Questions Sunday school teachers ask</h2>
<h3>Can I use the ready-made Bible stories in church?</h3><p>Yes. Play them in class, in children's church or in a service, and share them with families.</p>
<h3>Which Bible version are the stories based on?</h3><p>The ready-made stories retell the Bible in simple words for children. Check the wording against your church's Bible and change any line you like before making your video.</p>
<h3>Can children make their own Bible story?</h3><p>Yes. Older children can write a parable in their own words in six to eight scenes, choose the pictures, and record the narration together.</p>'''),
 ('bedtime-story-for-your-child', 'Make a personal bedtime story for your child', 'Turn your child into the hero of a short narrated story, with their name, their pet and a calm ending for bedtime.', '''
<p class="lead">Children love hearing stories about themselves. With Telar Stories you can make a short bedtime story where your child is the hero, read in a gentle voice, with soft music and a calm ending.</p>
<h2>Pick the ingredients</h2>
<ul><li><b>Your child's name,</b> and a friend, sibling or pet who joins the adventure.</li>
<li><b>Something your child loves:</b> rain, stars, animals, the beach, building things, helping in the kitchen.</li>
<li><b>A small worry or a wish:</b> being afraid of the dark, missing a grandparent, starting school, wanting a puppy.</li>
<li><b>A warm ending:</b> feeling safe, being proud, falling asleep.</li></ul>
<h2>A simple bedtime plan</h2>
<ol><li><b>Title:</b> "Ella and the Sleepy Stars."</li>
<li>Your child at home in the evening.</li>
<li>Something gentle happens: a star twinkles, the cat wants to play, the rain taps on the window.</li>
<li>A small adventure, two or three scenes. Keep it calm, not scary.</li>
<li>Coming home, a hug from Mom or Dad.</li>
<li>Getting cozy in bed.</li>
<li>"Good night, Ella. Sweet dreams."</li></ol>
<h2>Choosing characters</h2>
<p>Pick the character who looks most like your child, or the one they like best. <b>Mira</b> and <b>Mei</b> have many poses, and <b>Mei's family</b> includes a mom and a dad. Mochi the cat is a good pet for any story. The name in the words is what makes it your child's story; the picture doesn't have to match exactly.</p>
<h2>Making it calm</h2>
<ul><li>Choose <b>Light: night (darker)</b> on characters in evening scenes, and backgrounds like the cozy bedroom, the reading nook or the starry lake.</li>
<li>Use <b>Movement: gentle breathing</b> or <b>steady</b>, not hop.</li>
<li>Pick the <b>Slow</b> speed for the AI voice, and the <i>Gentle: Soft piano</i> music.</li>
<li>End on a still scene with very few words, so the video fades out softly.</li></ul>
<h2>Your own voice</h2>
<p>A story read by Mom, Dad, Lola or Lolo means more than any narrator. Record each scene with <b>● Record my voice</b>. Grandparents who live far away can record a story on their own phone and send the video, a lovely way to keep bedtime together.</p>
<h2>Keep it safe</h2>
<p>Save the video and also tap <b>Save a backup</b>, so you can change the story later, like adding a new pet or a new year at school. See <a href="../share-and-keep/">Sharing your video and keeping your work</a>.</p>
<p class="tip"><b>Privacy tip:</b> if you share the video outside the family, consider using a first name only.</p>
<h2>Questions parents ask</h2>
<h3>How long should a bedtime story be?</h3><p>One to three minutes is plenty. Children often ask to watch it again, which is part of the bedtime routine.</p>
<h3>Can I make a story about a hard moment, like a new sibling or moving house?</h3><p>Yes. Stories help children understand big changes. Keep the problem gentle, show the child feeling unsure, and end with comfort and love.</p>
<h3>Is it free?</h3><p>Yes. Telar Stories is free, with no sign-up, and your stories stay on your device.</p>'''),
 ('story-videos-in-the-classroom', 'Using story videos in the classroom', 'Lesson ideas for teachers: reading, values, languages and student-made stories, with simple routines that work.', '''
<p class="lead">A short story video can open a lesson, start a discussion, or become a project students make themselves. Here are ways teachers use Telar Stories in class.</p>
<h2>1. A story to start a lesson</h2>
<p>Play a one- to two-minute story at the start of a lesson to set the topic. <i>Friends Around the World</i> opens a lesson about cultures and greetings; <i>The Christmas Gift</i> opens a talk about kindness and giving.</p>
<h2>2. Listening and comprehension</h2>
<ul><li><b>Before:</b> show the title scene and ask, "What do you think this story is about?"</li>
<li><b>During:</b> pause after a key scene. "How does Amara feel now? How do you know?"</li>
<li><b>After:</b> ask students to put three scenes in order, or retell the story in their own words.</li></ul>
<h2>3. Values and social-emotional learning</h2>
<p>Make a short story about a classroom situation: sharing toys, including a new classmate, saying sorry, being patient. Children can talk about a character's choices more easily than about their own.</p>
<h2>4. Language learning</h2>
<ul><li>Write the same story in two languages, and make one video for each.</li>
<li>Use the AI voice's <b>Slow</b> speed so learners can follow every word, with the captions on screen.</li>
<li>Students record their own voice reading a scene, a good speaking practice they can listen back to.</li></ul>
<h2>5. Students make their own stories</h2>
<p>Older children can plan and make a story in groups:</p>
<ol><li><b>Plan:</b> a hero, a problem, and how it's solved, in six to eight scenes on paper.</li>
<li><b>Write:</b> one to three sentences per scene. Check spelling together.</li>
<li><b>Build:</b> choose backgrounds and characters, and place them.</li>
<li><b>Voice:</b> record the narration, taking turns reading.</li>
<li><b>Share:</b> play every group's video for the class.</li></ol>
<p>Students don't need accounts. If groups work over several days on a shared computer, use <b>Save a backup</b> at the end of each class and <b>Open a backup</b> to continue.</p>
<h2>6. A video for parents</h2>
<p>Make a short story about the week's lesson or a class event, and send it to parents. It's an easy way to show what children learned.</p>
<h2>Practical tips</h2>
<ul><li>Download the video before class and play the MP4 file, so it doesn't depend on the school's internet.</li>
<li>Keep videos short. Two short stories are better than one long one.</li>
<li>For a whiteboard to go with the lesson, try <a href="https://pizarrapad.telarlabs.net">PizarraPad</a>, our free online board.</li></ul>
<h2>Questions teachers ask</h2>
<h3>Do students need accounts or email addresses?</h3><p>No. Telar Stories works in the browser with no sign-up. Work is saved on the device, and backups can be saved as files.</p>
<h3>Does it work on school Chromebooks and tablets?</h3><p>It works in modern browsers like Chrome, Edge and Safari. The AI voice needs a one-time download of about 90 MB; on slow connections, students can record their own voices instead.</p>
<h3>Can I use the videos on our school page?</h3><p>Yes, the videos you make are yours to share. Follow your school's rules about students' names and voices.</p>'''),
 ('christmas-story-video', 'Make a Christmas story video for your family, class or church', 'Ideas and a step-by-step plan for a short narrated Christmas story, from the Nativity to a family greeting.', '''
<p class="lead">A narrated Christmas story makes a warm greeting for family far away, a children's message for a Christmas service, or a closing activity before the school break.</p>
<h2>Three kinds of Christmas story</h2>
<ul><li><b>The Nativity:</b> <i>The First Christmas</i> is ready to play, from the angel's visit to Mary to the shepherds at the stable.</li>
<li><b>A kindness story:</b> <i>The Christmas Gift</i> tells how Lily gives up a present to cheer up her lonely neighbor, Mr. Ben.</li>
<li><b>Your own family story:</b> your children, your home, and how your family celebrates.</li></ul>
<h2>A family Christmas greeting in six scenes</h2>
<ol><li><b>Title:</b> "Christmas with the Santos Family" over the snowy Christmas village or the living room with fireplace.</li>
<li>The children waiting for Christmas, counting the days.</li>
<li>Getting ready: baking, decorating, wrapping gifts. Use Mei's gift pose or Lily's baking poses.</li>
<li>Remembering the true meaning: a short line about Jesus, or about love and family.</li>
<li>A message for the people watching: "We miss you, Lola and Lolo!"</li>
<li>"Merry Christmas and a happy New Year!"</li></ol>
<h2>Backgrounds for the season</h2>
<p>Under <b>Story places</b>: the snowy street, the cozy bedroom, the toy shop, the Christmas kitchen, the front door in the snow, the living room with fireplace, and the stable with the star. Under <b>From Telar Clips</b>: the snowy Christmas village and, for New Year, the fireworks over the harbour.</p>
<h2>Narration and music</h2>
<ul><li>Let each family member record one scene with <b>● Record my voice</b>. Children love hearing themselves in the video.</li>
<li>Choose gentle music, like <i>Gentle: Soft piano</i> or <i>Warm and happy: Sunday</i>.</li>
<li>Keep it under two minutes, so people watch to the end on their phones.</li></ul>
<h2>Sharing it</h2>
<p>Send the MP4 in your family group chat, or post it on Facebook. For a church or school program, play the downloaded file on the projector. See <a href="../share-and-keep/">Sharing your video and keeping your work</a>.</p>
<p class="tip"><b>Tip:</b> Save a backup of your Christmas story. Next year, open it, change the names and the year, add the new baby or the new puppy, and make a fresh greeting in minutes.</p>
<h2>Ideas for a church Christmas program</h2>
<ul><li>Play <i>The First Christmas</i> before the children's nativity play, so the audience knows the story.</li>
<li>Have the Sunday school class record the narration, one child per scene.</li>
<li>End the program with a short video greeting from the church, with the service times in the last scene.</li></ul>'''),
]
CSS = '''<style>:root{--bg:#16131c;--bg2:#1f1b27;--fg:#f4f1f8;--muted:#a8a1b1;--line:#352f40;--accent:#ff8fa3}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
a{color:var(--accent)}.top{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--line);background:#121017;position:sticky;top:0}
.homelink{color:inherit;text-decoration:none}.top b{font-size:17px}.top b span{color:var(--accent)}.top .sp{flex:1}.btn{border:1px solid var(--line);background:#2a2533;color:var(--fg);padding:8px 14px;border-radius:10px;font-weight:700;text-decoration:none;font-size:14px}
.btn.primary{background:var(--accent);color:#2a0d14;border-color:var(--accent)}main{max-width:760px;margin:0 auto;padding:22px 16px 60px}
h1{font-size:30px;line-height:1.2;margin:8px 0 10px}h2{font-size:21px;margin:28px 0 8px}.lead{font-size:18px;color:#e9e2f0}
.crumb{font-size:14px;color:var(--muted)}.crumb a{color:var(--muted)}li{margin:4px 0}
.tip{background:var(--bg2);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:12px 14px}
pre{background:#0f0d13;border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-size:15px;overflow-x:auto}
.cards{display:grid;gap:12px;margin-top:18px}.card{display:block;background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:16px 18px;color:var(--fg);text-decoration:none}
.card:hover{border-color:var(--accent)}.card b{font-size:18px}.card span{display:block;color:var(--muted);font-size:15px;margin-top:4px}
.table,table{width:100%;border-collapse:collapse;margin:10px 0}th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}th{background:var(--bg2)}code{background:#0f0d13;padding:1px 6px;border-radius:6px}
.next{margin-top:34px;display:flex;gap:10px;flex-wrap:wrap}
.top b,.top .btn{white-space:nowrap}@media(max-width:480px){.top{gap:6px;padding:10px 12px}.top .btn{padding:7px 10px;font-size:13px}.top b{font-size:15px}}
.foot{max-width:760px;margin:0 auto;padding:20px 16px 40px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:8px 18px;font-size:14px}.foot a{color:var(--muted)}</style>'''
def page(title, desc, body, depth, path=''):
    up = '../' * depth
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)} | Telar Stories</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="https://stories.telarlabs.net/{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4326677240395780" crossorigin="anonymous" onerror="window.tsAdBlocked=1"></script>{CSS}</head><body>
<header class="top"><a href="{up}" class="homelink" title="Telar Stories home"><b>Telar <span>Stories</span></b></a><div class="sp"></div><a class="btn" href="{up}stories/">Printables</a><a class="btn" href="{up}guides/">Guides</a><a class="btn primary" href="{up}">Open the app</a></header>
<main>{body}</main>
<footer class="foot"><a href="{up}">Telar Stories</a><a href="{up}guides/">Guides</a><a href="{up}stories/">Stories &amp; printables</a><a href="{up}games/">Games for kids</a><a href="https://telarlabs.net/">Telar Labs</a><a href="https://telarlabs.net/guides/">More guides</a><a href="https://telarlabs.net/about/">About</a><a href="https://telarlabs.net/privacy/">Privacy</a><a href="https://telarlabs.net/terms/">Terms</a><a href="https://telarlabs.net/contact/">Contact</a></footer>{ADNOTE_JS}</body></html>'''
os.makedirs(OUT, exist_ok=True)
cards = ''.join(f'<a class="card" href="{s}/"><b>{E(t)}</b><span>{E(d)}</span></a>' for s, t, d, _ in G)
open(os.path.join(OUT, 'index.html'), 'w').write(page('Guides', 'How to make story videos with Telar Stories.',
    '<h1>Telar Stories guides</h1><p class="lead">Short, friendly guides for making story videos. No editing skills needed.</p>' + f'<div class="cards">{cards}</div>', 1, 'guides/'))
for i, (s, t, d, body) in enumerate(G):
    nxt = G[i + 1] if i + 1 < len(G) else None
    foot = '<div class="next">' + (f'<a class="btn" href="../{nxt[0]}/">Next: {E(nxt[1])} →</a>' if nxt else '') + '<a class="btn primary" href="../../">Open the app</a></div>'
    os.makedirs(os.path.join(OUT, s), exist_ok=True)
    open(os.path.join(OUT, s, 'index.html'), 'w').write(page(t, d, f'<p class="crumb"><a href="../">Guides</a></p><h1>{E(t)}</h1>{body}{foot}', 2, f'guides/{s}/'))
SITE = os.path.join(OUT, '..')
# ---------------------------------------------------------------- story pages with printables (content pages, with ads)
STORIES = [
 dict(slug='mira-and-the-rainy-day', id='mira', title='Mira and the Rainy Day',
  desc='A free narrated picture-book story about a rainy afternoon, a curious cat and an old red book, with a printable coloring page, sequencing sheet and discussion questions.',
  age='Ages 3 to 7', mins='About 1½ minutes', theme='Imagination, reading, finding joy on a boring day',
  summary='<p>It’s a rainy afternoon, and Mira wants to play outside. “There is nothing to do,” she sighs, while her little cat, Mochi, sleeps nearby. Then Mochi wakes up, wanders to the bookshelf and – bump! – knocks an old red book onto the floor. Inside, Mira finds stories about faraway places, brave animals and wonderful friends. By the time she looks up, the rain has stopped and a rainbow fills the sky.</p>',
  lesson='<p>Boredom is often the start of something good. The story gently shows children that books and imagination can turn an ordinary day into an adventure, and that small surprises, like a cat knocking over a book, can lead somewhere wonderful.</p>',
  before=['Look out the window together. What is the weather like today?', 'What do you do when you can’t play outside?', 'Show the title scene and ask: what do you think this story is about?'],
  after=['How did Mira feel at the start of the story? How do you know?', 'What did Mochi do that changed Mira’s day?', 'What was inside the old red book?', 'How did Mira feel at the end? Why?', 'What do YOU like to do on a rainy day?', 'If you found a magic book, what kind of stories would be inside?'],
  activities=['<b>Rainy-day book nook:</b> make a cozy reading corner with pillows and a blanket, and read a favorite book together, the way Mira did.',
   '<b>Rain sounds:</b> tap fingers on a table to make soft rain, then louder rain, then let it stop and draw a rainbow in the air.',
   '<b>Book hunt:</b> let your child pick an “old” book from the shelf, like Mochi did, and read it together.',
   '<b>Make it yours:</b> in Telar Stories, change Mira’s name to your child’s name and record the last line together, then save the video.'],
  pages=[('Color Mira and Mochi', 'A coloring page with Mira, Mochi and a box to draw a raindrop or rainbow.'),
         ('Put the story in order', 'Four pictures from the story to number 1 to 4, then retell. Answers at the bottom.'),
         ('Think, talk and draw', 'Four questions to talk about and a big box to draw a rainy-day adventure.')]),
 dict(slug='the-first-christmas', id='xmas', title='The First Christmas',
  desc='A free narrated picture-book telling of the Nativity for young children, from the angel’s visit to Mary to the shepherds at the stable, with a printable coloring page, sequencing sheet and discussion questions.',
  age='Ages 3 to 8', mins='About 2 minutes', theme='Christmas, the Nativity, God’s gift of Jesus',
  summary='<p>In the little town of Nazareth, the angel Gabriel visits a young woman named Mary. “Do not be afraid,” he says. “You will have a baby, and you will name him Jesus.” Mary and Joseph travel to Bethlehem, but the town is so crowded that the only place to stay is a stable. That night, baby Jesus is born and laid in a manger. Out in the fields, angels appear to shepherds with the good news, and the shepherds hurry to find the baby, just as the angel said.</p>',
  lesson='<p>Christmas is about a gift: God sending Jesus to the world. The story also shows trust (Mary saying yes to God), kindness (the innkeeper making room) and joy that is meant to be shared (the shepherds telling everyone).</p>',
  before=['What do you know about Christmas? Why do we celebrate it?', 'Have you ever had to wait for something special?', 'Look at the title scene. Who do you think the people are?'],
  after=['Who visited Mary, and what did he tell her?', 'Why did Mary and Joseph go to Bethlehem?', 'Where was baby Jesus born? Why there?', 'Who heard the news first, and how did they hear it?', 'Why do we call Jesus God’s greatest gift?', 'How can you share the joy of Christmas with someone this year?'],
  activities=['<b>Nativity play:</b> act out the story with family or classmates, using a doll for baby Jesus and towels for costumes.',
   '<b>Star of joy:</b> cut out a paper star and write on it one way to be kind this Christmas.',
   '<b>Count the characters:</b> list everyone in the story (Mary, Joseph, the angel, the innkeeper, the shepherds) and talk about what each one did.',
   '<b>Record it together:</b> in Telar Stories, let children take turns recording the narration, one scene each, and save the video for the Christmas program.'],
  pages=[('Color Mary and baby Jesus', 'A coloring page with Mary holding baby Jesus, the donkey, and a box to draw the star.'), ('Put the story in order', 'Four pictures from the story to number 1 to 4, then retell. Answers at the bottom.'), ('Think, talk and draw', 'Four questions and a big box to draw the night Jesus was born.')]),
 dict(slug='the-lost-sheep', id='sheep', title='The Lost Sheep',
  desc='A free narrated picture-book telling of the parable of the lost sheep from Luke 15, with a printable coloring page, sequencing sheet and discussion questions for Sunday school and home.',
  age='Ages 3 to 8', mins='About 2 minutes', theme='God’s love for each one of us, never giving up',
  summary='<p>A shepherd boy loves his sheep and counts them every evening. One night he counts ninety-seven, ninety-eight, ninety-nine… one is missing! He makes sure the others are safe, then searches the rocky hills and thorny bushes as the sun goes down. In the dark and cold he hears a tiny “baa”, and finds the little lamb, alone and afraid. He carries it home on his shoulders and calls his friends: “Be glad with me! I found my lost sheep!”</p>',
  lesson='<p>Jesus told this story to show how much God loves every single person. No one is too small to matter, and God keeps looking for us and is full of joy when we come home. Children can also learn to notice when someone is left out and go looking for them.</p>',
  before=['Have you ever lost something special? How did you feel?', 'What does a shepherd do?', 'Have you ever felt lost or left out?'],
  after=['How many sheep did the shepherd have?', 'How did the shepherd know one was missing?', 'Where did he look for the lamb?', 'How did the lamb feel when it was lost? And when it was found?', 'Why did the shepherd have a party?', 'What does this story tell us about how God loves us?'],
  activities=['<b>Hide the lamb:</b> hide a toy sheep in the room and let children search for it, then celebrate when it’s found.',
   '<b>Counting game:</b> line up 10 cotton balls, take one away, and let children find which one is missing.',
   '<b>Memory verse:</b> learn Luke 15:6, “Rejoice with me; I have found my lost sheep.”',
   '<b>Be a shepherd:</b> talk about someone who might feel left out at school or church, and one way to include them this week.'],
  pages=[('Color the shepherd and the lamb', 'A coloring page with the shepherd carrying the lamb, the little lamb, and a box to draw the ninety-nine sheep.'), ('Put the story in order', 'Four pictures from the story to number 1 to 4, then retell. Answers at the bottom.'), ('Think, talk and draw', 'Four questions and a big box to draw the shepherd finding the lamb.')]),
 dict(slug='the-christmas-gift', id='gift', title='The Christmas Gift',
  desc='A free narrated picture-book story about Lily, who gives up the gift she wanted to cheer up her lonely neighbor, with a printable coloring page, sequencing sheet and discussion questions.',
  age='Ages 4 to 9', mins='About 2 minutes', theme='Kindness, giving, thinking of others',
  summary='<p>All year, Lily has saved her coins to buy a snow globe with a tiny dancing bear. On the way home from the toy shop, she sees her old neighbor, Mr. Ben, sitting alone by his window. Mom explains that his family lives far away. Lily thinks about the snow globe, then about Mr. Ben, and has an idea. She spends her coins on flour and sprinkles, bakes cookies with Mom, and on Christmas Eve brings them to Mr. Ben with a card. He smiles the biggest smile, and they sing Christmas songs together.</p>',
  lesson='<p>The best gifts are the ones we give. Lily chooses kindness over something she wanted for herself, and discovers it makes her happier. It’s a gentle way to talk with children about noticing lonely people, and about giving time and care, not only things.</p>',
  before=['What would you like for Christmas?', 'Do you know someone who might feel lonely at Christmas?', 'What makes a gift special?'],
  after=['What was Lily saving her coins for?', 'Why was Mr. Ben alone?', 'What did Lily decide to do with her coins? Why?', 'How did Mr. Ben feel when he got the cookies?', 'How did Lily feel at the end?', 'Who could you make happy with a small gift or a visit?'],
  activities=['<b>Kindness cookies:</b> bake or decorate cookies together and give them to a neighbor, a grandparent or a school guard.',
   '<b>Card for someone lonely:</b> make a Christmas card for someone who lives alone or far from family.',
   '<b>Coin jar:</b> start a family jar for helping others, and decide together how to use it.',
   '<b>Make it yours:</b> in Telar Stories, change Lily’s name and Mr. Ben’s name to people your child knows, and record a message at the end.'],
  pages=[('Color Lily and Mr. Ben', 'A coloring page with Lily and her cookies, Mr. Ben with his card, and a box to draw a Christmas cookie.'), ('Put the story in order', 'Four pictures from the story to number 1 to 4, then retell. Answers at the bottom.'), ('Think, talk and draw', 'Four questions and a big box to draw a gift you could make for someone.')]),
 dict(slug='noahs-ark', id='noah', title='Noah’s Ark',
  desc='A free narrated picture-book telling of Noah’s Ark for young children, with the animals coming two by two, the great rain and the dove with the olive leaf, plus a printable coloring page, sequencing sheet and discussion questions.',
  age='Ages 3 to 8', mins='About 2 minutes', theme='Trusting and obeying God, God’s promise',
  summary='<p>Long ago, many people forgot to be kind and forgot about God, but Noah loved God and always tried to do what was right. God told Noah to build a very big boat called an ark. Noah and his family worked hard, day after day, and then the animals came, two by two: lions and elephants, giraffes and zebras, sheep and rabbits. The rain fell for forty days and forty nights, but inside the ark everyone was safe. At last the rain stopped, and a dove came back with an olive leaf. The land was drying!</p>',
  lesson='<p>Noah trusted God even when building a huge boat on dry land seemed strange. The story shows that God takes care of those who trust Him, and the rainbow is a sign of God’s promise.</p>',
  before=['What is your favorite animal?', 'Have you ever been caught in a big rainstorm? How did it feel?', 'What do you think an ark is?'],
  after=['Why did God choose Noah?', 'What did God ask Noah to build?', 'How did the animals come into the ark?', 'How long did it rain?', 'What did the dove bring back?', 'What does a rainbow remind us of?'],
  activities=['<b>Two by two:</b> make pairs of animal cards and play a matching game.',
   '<b>Animal parade:</b> children act like their favorite animal and march “into the ark” in pairs.',
   '<b>Rainbow promise:</b> make a paper rainbow and write a promise on each color.',
   '<b>Count the animals:</b> pause the story at the animals scene and count every pair together.'],
  pages=[('Color Noah and the animals', 'A coloring page with Noah, two sheep, and a box to draw a rainbow.'), ('Put the story in order', 'Four pictures from the story to number 1 to 4, then retell. Answers at the bottom.'), ('Think, talk and draw', 'Four questions and a big box to draw animals going into the ark.')]),
 dict(slug='friends-around-the-world', id='friends', title='Friends Around the World',
  desc='A free narrated picture-book story about Amara’s first day at a new school and a class that shares hello and food from around the world, with a printable coloring page, sequencing sheet and discussion questions.',
  age='Ages 4 to 9', mins='About 2½ minutes', theme='Welcoming others, cultures, friendship',
  summary='<p>It’s Amara’s first day at a new school. Her family has just moved from Nigeria, and she doesn’t know anyone. Her teacher, Ms. Rose, announces Share Your Home Day. The next day, Paolo says “Kumusta!” and shares pancit, Zofia says “Cześć!” and shares pierogi, Ayaan says “Assalam-o-alaikum!” and shares samosas, and Lena says “Hallo!” with a soft pretzel. Then it’s Amara’s turn: “Bawo ni!” She shares jollof rice, everyone loves it, and at lunch they share all their food. Amara laughs for the first time all week.</p>',
  lesson='<p>We come from different places, but a smile means hello everywhere. The story helps children welcome new classmates, be curious about other cultures, and see that sharing something from home can turn strangers into friends.</p>',
  before=['How do you feel on the first day at a new place?', 'How do you say “hello” in another language?', 'What food does your family make for special days?'],
  after=['Why was Amara shy at the start?', 'What is Share Your Home Day?', 'Which greetings did the children say? Can you say them?', 'What foods did they share?', 'How did Amara feel at the end? Why?', 'How can you help a new classmate feel welcome?'],
  activities=['<b>Hello wall:</b> make a poster of “hello” in all the languages your class or family knows.',
   '<b>Share Your Home Day:</b> hold your own day where each child brings a photo, a food or a song from their family.',
   '<b>Map it:</b> find Nigeria, the Philippines, Poland, Pakistan and Germany on a map or globe.',
   '<b>Welcome buddy:</b> talk about what a good welcome buddy does for a new classmate.'],
  pages=[('Color the friends', 'A coloring page with the five friends waving hello.'), ('Put the story in order', 'Four pictures from the story to number 1 to 4, then retell. Answers at the bottom.'), ('Think, talk and draw', 'Four questions and a big box to draw something special from your family.')]),
]
SP = os.path.join(SITE, 'stories'); os.makedirs(SP, exist_ok=True)
import sys as _s; _s.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from games import make_images, memory_game, order_game, games_hub, GCSS, MEMORY_TEXT
make_images()
STYLE2 = '<style>.meta{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 16px}.meta span{background:var(--bg2);border:1px solid var(--line);border-radius:999px;padding:4px 12px;font-size:14px}.pv{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:12px 0}.pv figure{margin:0}.pv img{width:100%;height:auto;border-radius:8px;border:1px solid var(--line);background:#fff}.pv figcaption{font-size:13px;color:var(--muted);margin-top:4px}.dl{background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:18px 0}.dl .btn{display:inline-block;margin-top:8px}@media(max-width:560px){.pv{grid-template-columns:1fr 1fr}}</style>'
for st in STORIES:
    sl = st['slug']; li = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    pv = ''.join(f'<figure><img src="../../printables/{sl}-p{i}.webp" width="579" height="819" alt="{E(t)} – printable page {i}" loading="lazy"><figcaption><b>{E(t)}</b><br>{E(d)}</figcaption></figure>' for i, (t, d) in enumerate(st['pages'], 1))
    body = (f'{STYLE2}<p class="crumb"><a href="../">Stories</a></p><h1>{E(st["title"])}</h1>'
      f'<div class="meta"><span>{E(st["age"])}</span><span>{E(st["mins"])}</span><span>{E(st["theme"])}</span></div>'
      f'<p class="lead">{E(st["desc"])}</p>'
      f'<p><a class="btn primary" href="../../?story={st["id"]}">▶ Open this story in Telar Stories</a></p>'
      f'<h2>The story</h2>{st["summary"]}<h2>What it teaches</h2>{st["lesson"]}'
      f'<h2 id="play">Play: put the story in order</h2>{GCSS}{order_game(sl)}'
      f'<h2>Before the story</h2>{li(st["before"])}<h2>After the story: questions to talk about</h2>{li(st["after"])}'
      f'<h2>Free printable activity pack</h2><p>Three pages to print at home, in class or at church. Black-and-white friendly, A4 and US Letter.</p><div class="pv">{pv}</div>'
      f'<div class="dl"><b>{E(st["title"])} – activity pack</b> (PDF, 3 pages)<br><a class="btn primary" href="../../printables/{sl}-activities.pdf" download>⬇ Download the printables</a></div>'
      f'<h2>Activities to try</h2>{li(st["activities"])}'
      f'<h2>Make it your own</h2><p>Open the story in Telar Stories and change anything: your child’s name, the words, the music or the voice. You can record your own voice for each scene and save the finished story as an MP4 video to share with family. See <a href="../../guides/first-story-video/">Make your first story video</a>.</p>'
      f'<p class="tip"><b>Free to use:</b> print as many copies as you need for your family, class or church. Please don’t sell them.</p>' + (f'<h2>More stories</h2><ul>' + ''.join(f'<li><a href="../{o["slug"]}/">{E(o["title"])}</a></li>' for o in STORIES if o is not st) + '</ul>'))
    os.makedirs(os.path.join(SP, sl), exist_ok=True)
    open(os.path.join(SP, sl, 'index.html'), 'w').write(page(st['title'] + ': free story and printables', st['desc'], body, 2, f'stories/{sl}/'))
cards2 = ''.join(f'<a class="card" href="{x["slug"]}/"><b>{E(x["title"])}</b><span>{E(x["desc"])}</span></a>' for x in STORIES)
open(os.path.join(SP, 'index.html'), 'w').write(page('Stories and free printables', 'Free narrated picture-book stories with printable coloring pages and activities for home, class and church.',
    '<h1>Stories and free printables</h1><p class="lead">Each story comes with questions to talk about, a free printable activity pack and a Story Order game. Open any story in Telar Stories to play it, change it or save it as a video.</p><p class="tip">🎮 Looking for games? Try <a href="../games/memory-match/">Memory Match</a> or see all <a href="../games/">games for kids</a>.</p>' + f'<div class="cards">{cards2}</div>', 1, 'stories/'))
GP = os.path.join(SITE, 'games'); os.makedirs(os.path.join(GP, 'memory-match'), exist_ok=True)
open(os.path.join(GP, 'index.html'), 'w').write(page('Games for kids', 'Free games for young children with the Telar Stories characters: Memory Match and Story Order for every story.', games_hub(), 1, 'games/'))
open(os.path.join(GP, 'memory-match', 'index.html'), 'w').write(page('Memory Match: a free memory game for kids', 'A free memory card game for children ages 3 to 8 with the Telar Stories characters. Easy, medium and hard levels, no sign-up.',
    '<p class="crumb"><a href="../">Games</a></p><h1>Memory Match</h1><p class="lead">Turn over two cards at a time and find the matching characters.</p>' + memory_game() + MEMORY_TEXT
    + '<h2>More games</h2><ul>' + ''.join(f'<li><a href="../../stories/{x["slug"]}/#play">Story Order: {E(x["title"])}</a></li>' for x in STORIES) + '</ul>', 2, 'games/memory-match/'))
open(os.path.join(SITE, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'<url><loc>https://stories.telarlabs.net/{u}</loc></url>\n' for u in ['', 'guides/'] + [f'guides/{x[0]}/' for x in G] + ['stories/'] + [f'stories/{x["slug"]}/' for x in STORIES] + ['games/', 'games/memory-match/']) + '</urlset>\n')
open(os.path.join(SITE, 'robots.txt'), 'w').write('User-agent: *\nDisallow: /cdn-cgi/\n\nUser-agent: Mediapartners-Google\nAllow: /\n\nSitemap: https://stories.telarlabs.net/sitemap.xml\n')
open(os.path.join(SITE, 'ads.txt'), 'w').write('google.com, pub-4326677240395780, DIRECT, f08c47fec0942fa0\n')
# The app needs cross-origin isolation for the AI voice; the guides must not have it, or ads can't load.
open(os.path.join(SITE, '_headers'), 'w').write('/\n  Cross-Origin-Opener-Policy: same-origin\n  Cross-Origin-Embedder-Policy: require-corp\n'
    '/index.html\n  Cross-Origin-Opener-Policy: same-origin\n  Cross-Origin-Embedder-Policy: require-corp\n'
    '/assets/*\n  Cross-Origin-Embedder-Policy: require-corp\n  Cross-Origin-Resource-Policy: same-origin\n'
    '/assets/ort-v2/*\n  Cache-Control: public, max-age=604800\n/assets/bg/*\n  Cache-Control: public, max-age=86400\n/assets/ch/*\n  Cache-Control: public, max-age=86400\n')
print('built', len(G), 'guides')

# old telar-stories.pages.dev address: send fresh visitors to stories.telarlabs.net
import sys as _sys; _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); import home_domain as _hd; _hd.inject(SITE)
