#!/usr/bin/env python3
"""Builds the Telar Labs studio homepage (telarlabs.net) into public/.
Run: python3 tools/build.py   (standard library only)"""
import json, os, html, re, glob
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, 'public')
CFG = json.load(open(os.path.join(ROOT, 'site.config.json')))
E = lambda s: html.escape(str(s), quote=True)
URL = CFG['site_url'].rstrip('/')
ST = CFG['studio']
MAIL = CFG['contact_email']

LOGO = ('<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#ffb547"/>'
        '<path d="M8 11h16M8 16h16M8 21h16" stroke="#1b1206" stroke-width="2.6" stroke-linecap="round"/>'
        '<path d="M12 7v18M20 7v18" stroke="#1b1206" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="3 3"/></svg>')

def page(path, title, desc, body, ads_on=True, head_extra='', og_type='website'):
    full = title if ST in title else f'{title} | {ST}'
    ads = (f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={E(CFG["adsense_client"])}" '
           'crossorigin="anonymous"></script>') if CFG.get('adsense_client') and ads_on else ''
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{E(URL + path)}">
<meta property="og:title" content="{E(full)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="{og_type}"><meta property="og:url" content="{E(URL + path)}">
<meta property="og:image" content="{E(URL)}/assets/img/clips.webp">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#16131c">
<link rel="stylesheet" href="/assets/site.css">
{ads}{head_extra}
</head>
<body>
<header class="top"><div class="wrap top-in">
  <a class="logo" href="/">{LOGO}<span>{E(ST)}</span></a>
  <nav class="nav"><a href="/#apps">Apps</a><a href="/guides/">Guides</a><a href="/about/">About</a><a href="/contact/">Contact</a></nav>
</div></header>
<main>
{body}
</main>
<footer class="foot"><div class="wrap foot-in">
  <div><a class="logo" href="/">{LOGO}<span>{E(ST)}</span></a>
  <p class="muted">Small, free tools for teachers and creators.</p></div>
  <div class="foot-cols">
    <div><h4>Apps</h4>{''.join(f'<a href="{E(a["url"])}">{E(a["name"])}</a>' for a in CFG["apps"] if a.get("url") and (not a.get("soon") or CFG.get("stories_live")))}</div>
    <div><h4>{E(ST)}</h4><a href="/guides/">Guides</a><a href="/about/">About</a><a href="/privacy/">Privacy policy</a><a href="/terms/">Terms of use</a><a href="/contact/">Contact</a></div>
  </div>
</div><div class="wrap fine">&copy; {date.today().year} {E(ST)}.</div></footer>
</body>
</html>'''
    out = os.path.join(PUB, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(PUB, path.strip('/'))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(doc)

def app_card(a):
    soon = a.get('soon') and not (a['name'] == 'Telar Stories' and CFG.get('stories_live'))   # switched on at launch
    if not soon and a.get('blurb_live'): a = {**a, 'blurb': a['blurb_live']}
    tag = 'div' if soon else 'a'
    href = '' if soon else f' href="{E(a["url"])}"'
    badge = '<span class="badge soon">Coming soon</span>' if soon else f'<span class="badge">{"New · " if a.get("soon") else ""}{E(a["for"])}</span>'
    cta = '' if soon else f'<span class="go">Open {E(a["name"])} →</span>'
    return (f'<{tag} class="app" style="--c:{a["color"]}"{href}>'
            f'<div class="shot"><img src="/assets/img/{a["img"]}" alt="{E(a["name"])} screenshot" loading="lazy" width="800" height="450"></div>'
            f'<div class="app-body">{badge}<h3>{E(a["name"])}</h3><p>{E(a["blurb"])}</p>{cta}</div></{tag}>')


GAMES = [
 ('https://quizpolice.telarlabs.net/practice/spot-the-fallacy/', 'College', 'Spot the Fallacy', 'Read short arguments and name the logical fallacy. With a guide to 12 common fallacies.'),
 ('https://drafttrail.telarlabs.net/practice/word-choice/', 'Writing', 'Word Choice Check', 'Affect or effect? Fewer or less? Practice commonly confused words for essays.'),
 ('https://quizpolice.telarlabs.net/practice/percent-sprint/', 'Math', 'Percent & Estimation Sprint', 'Percentages, discounts, tips, fractions and quick estimates in 60 seconds.'),
 ('https://quizpolice.telarlabs.net/practice/math-sprint/', 'Math', 'Math Sprint', 'Adding, subtracting, times tables and division. Beat your best score.'),
 ('https://quizpolice.telarlabs.net/practice/world-history/', 'History', 'World History Timeline', 'Which came first? Pick the year? Key events from every continent.'),
 ('https://quizpolice.telarlabs.net/practice/geography/', 'Geography', 'Geography Practice', 'Countries and capital cities from every continent, 10 questions at a time.'),
 ('https://stories.telarlabs.net/games/', 'Kids 3 to 8', 'Memory Match & Story Order', 'Gentle games with the Telar Stories characters, plus a story-order game for every story.'),
]
def games_cards():
    return ''.join(f'<a class="gcard" href="{u}"><span class="gcat">{E(c)}</span><h3>{E(t)}</h3><p>{E(d)}</p><span class="gmeta">Play free →</span></a>'
                   for u, c, t, d in GAMES if 'stories.' not in u or CFG.get('stories_live'))

def home(G=()):
    cards = ''.join(app_card(a) for a in CFG['apps'])
    body = f'''
<section class="hero"><div class="wrap">
  <p class="eyebrow">Free · No sign-up · Works on any device</p>
  <h1>Small, free tools for teachers and creators</h1>
  <p class="lead">{E(ST)} is an independent studio making simple web apps that work on the devices people already have: a classroom board, a quiz monitor, a writing recorder, a library of free video backgrounds, and event tickets and bookings paid directly to organizers.</p>
  <div class="cta"><a class="btn" href="#apps">See the apps</a><a class="btn ghost" href="/about/">About the studio</a></div>
</div></section>
<section class="wrap section" id="apps">
  <h2>Our apps</h2>
  <div class="apps">{cards}</div>
</section>
<section class="wrap section"><h2>Guides</h2><p class="muted">Practical help for teaching, running events and making videos.</p>
  <div class="guides">{''.join(gcard(g) for g in list(G)[:6])}</div><p style="margin-top:16px"><a class="btn ghost" href="/guides/">All guides →</a></p>
</section>
<section class="wrap section" id="practice"><h2>Free practice games</h2><p class="muted">Quick learning games for students, from early readers to college. No sign-up, and they work on any phone.</p>
  <div class="guides">{games_cards()}</div>
</section>
<section class="wrap section why">
  <div><h3>Free to use</h3><p>Every app has a free version with no account needed. The information pages show a few ads to cover hosting; the tools themselves stay clean while you teach or create.</p></div>
  <div><h3>Your data stays with you</h3><p>Boards, drafts and quiz keys are saved in your own browser. We collect as little as possible, and quiz data is deleted automatically after 30 days.</p></div>
  <div><h3>Built for real classrooms</h3><p>Big buttons, works on phones and old laptops, keeps working when the Wi-Fi drops, and available in English, Spanish and Chinese where it matters.</p></div>
</section>'''
    page('/', f'{ST} – Free Tools for Teachers and Creators',
         'Telar Labs makes free web apps for teachers and creators: PizarraPad online board, QuizPolice quiz monitor, DraftTrail writing recorder, Telar Clips free video backgrounds and Tixward event tickets and bookings.', body)

def prose(path, title, desc, inner, ads_on=True):
    if path in ('/contact/', '/privacy/', '/terms/'): ads_on = False   # no ads on short utility pages
    page(path, title, desc, f'<article class="wrap prose">{inner}</article>', ads_on=ads_on)

def pages():
    apps_li = ''.join(f'<li><b>{E(a["name"])}</b>: {E(a["blurb"])}{"" if a.get("soon") else f" <a href=\"{E(a["url"])}\">{E(a["url"].replace("https://", ""))}</a>"}</li>' for a in CFG['apps'])
    prose('/about/', 'About', f'About {ST}, an independent studio making simple, free web tools for teachers, event organizers and creators.', f'''
<h1>About {E(ST)}</h1>
<p class="lead">{E(ST)} is a small, independent studio that builds simple web tools for teachers, students, event organizers and content creators. Most of what we make is free, works on any phone or laptop, and opens without an account.</p>
<h2>Why we build these tools</h2>
<p>Our apps start from everyday problems we keep hearing about from schools, churches, clubs and small teams:</p>
<ul>
<li><b>Classrooms</b> often have a projector or TV but no interactive board, and the internet isn't always reliable. Online quizzes are easy to cheat on, and AI has made it harder to know how an essay was written.</li>
<li><b>Small organizers</b> running reunions, fun runs, fitness classes or church concerts end up juggling group chats, spreadsheets and payment screenshots, while big ticketing platforms take a cut of every ticket.</li>
<li><b>Creators and volunteers</b> who make greeting, school and church videos keep needing the same backgrounds, overlays and holiday clips, in the right sizes for each platform.</li>
</ul>
<p>Good tools exist for all of this, but many need sign-ups, subscriptions, fast internet or a big budget. We try to make tools that just open and work.</p>
<h2>What we make</h2>
<ul>{apps_li}</ul>
<h2>What we promise</h2>
<ul>
<li><b>Free to start, no sign-up.</b> Teachers and students don't need accounts. Organizers get a private link instead of a password.</li>
<li><b>Your data stays small and short-lived.</b> PizarraPad saves boards in your own browser. DraftTrail recordings stay on the student's device until they hand in the file. QuizPolice deletes quiz data 30 days after a quiz is created. Tixward removes payment screenshots 30 days after an event and the rest of the event data after 90 days.</li>
<li><b>Money goes where it should.</b> On Tixward, buyers pay organizers directly. We never take a percentage of ticket sales.</li>
<li><b>No ads inside the tools.</b> Students taking a quiz, teachers at the board and buyers paying for tickets never see ads. Some information pages and guides may show a few ads to help pay for hosting.</li>
<li><b>Built for ordinary devices.</b> We test on phones as well as laptops, and on slow connections. Where we can, tools keep working offline.</li>
<li><b>Honest about limits.</b> No monitor catches every kind of cheating, and no recorder can prove who wrote something. We say so in our apps and guides.</li>
</ul>
<h2>How we're funded</h2>
<p>We keep the core tools free. Hosting and development are paid for by a small number of ads on information pages and by Tixward's one-time fee for larger events (events with up to 300 paid tickets are free, and free tickets are always free). Telar Clips are free to download and use.</p>
<h2>How we make things</h2>
<ul>
<li>Every app is designed, built and tested by the {E(ST)} team, then improved based on feedback from the people using it.</li>
<li>We use AI assistance in parts of our design, illustration and writing work. Everything is reviewed by the team before it's published.</li>
<li>Our motion graphics are original: generated in code or illustrated for {E(ST)}, never copied from other libraries.</li>
<li>Screenshots in our guides use sample data with made-up names, never real users' information.</li>
</ul>
<h2>Our guides</h2>
<p>Alongside the apps, we publish <a href="/guides/">practical guides</a> for teachers, event organizers and creators: how to reduce cheating in online quizzes, teach with a projector, sell tickets when buyers pay you directly, plan a reunion, or size a video for each platform. Each guide comes from the problems people bring to us while using our tools.</p>
<ul><li>Guides are written and reviewed by the {E(ST)} team, and dated so you know how current they are.</li>
<li>We test the steps ourselves, and we're open about the limits of every tool, including our own.</li>
<li>When a guide mentions one of our apps, we say so plainly. The advice works with other tools too.</li>
<li>When a setting or price changes, we update the guide. If you spot something out of date, please tell us.</li></ul>
<h2>Get in touch</h2>
<p>Ideas, feedback, corrections or partnership questions: <a href="mailto:{E(MAIL)}">{E(MAIL)}</a>. We usually reply within two to three working days.</p>''')
    prose('/contact/', 'Contact', f'Contact {ST}.', f'''
<h1>Contact us</h1>
<p class="lead">Questions, feedback, bug reports or ideas for a new tool? We'd love to hear from you.</p>
<p>Email: <a href="mailto:{E(MAIL)}">{E(MAIL)}</a></p>
<p>We usually reply within two to three working days. If you're reporting a problem, please include the app name, the page link and what device you were using.</p>''')
    prose('/privacy/', 'Privacy Policy', f'Privacy policy for {ST} websites.', f'''
<h1>Privacy policy</h1>
<p class="lead">This policy covers telarlabs.net. Each of our apps also has its own privacy page with details for that app.</p>
<h2>What we collect</h2>
<p>This site doesn't have accounts or forms, and we don't ask for personal information. If you email us, we use your address only to reply.</p>
<h2>Advertising</h2>
<p>We may use Google AdSense on our information pages. Google and its partners use cookies to show ads based on your visits to this and other websites. You can turn off personalized ads in <a href="https://adssettings.google.com" rel="noopener">Google Ads Settings</a>, and learn more at <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">How Google uses information from sites that use its services</a>. Visitors in the European Economic Area, the UK and Switzerland are shown a consent message before personalized ads are used.</p>
<h2>Analytics</h2><p>We use Cloudflare Web Analytics to count page visits. It does not use cookies and does not track you across websites.</p>
<h2>Hosting</h2>
<p>Our sites are hosted on Cloudflare, which may record basic technical information such as IP address and browser type to keep the service secure.</p>
<h2>Children</h2>
<p>Our tools are used in schools. We don't knowingly collect personal information from children, and our classroom apps are designed to work without student accounts.</p>
<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:{E(MAIL)}">{E(MAIL)}</a></p>
<p class="muted">Last updated {E(CFG["updated"])}.</p>''')
    prose('/terms/', 'Terms of Use', f'Terms of use for the {ST} website.', f'''
<h1>Terms of use</h1>
<p class="lead">These terms cover telarlabs.net, including our guides. Each of our apps has its own terms page with details for that app.</p>
<h2>Using this site</h2>
<p>You're welcome to read, share and link to our pages and guides. Please don't copy whole guides onto other websites; a short quote with a link back is fine.</p>
<h2>Our guides</h2>
<p>Our guides are general information, written in good faith and checked when published. Tools, settings, prices and rules change, so check the details that matter for your situation, especially for money, safety, permissions and school or local policies. The guides are not legal, financial or professional advice.</p>
<h2>Our apps</h2>
<p>Each app (Telar Clips, PizarraPad, QuizPolice, DraftTrail and Tixward) has its own terms and privacy page, linked from that app's footer. Those terms apply when you use the app.</p>
<h2>Links to other sites</h2>
<p>We sometimes link to other websites and services. We don't control them and aren't responsible for their content or practices.</p>
<h2>No warranty</h2>
<p>This site is provided as is. We work to keep it accurate and available, but we can't promise it will always be error-free or online.</p>
<h2>Changes</h2>
<p>We may update these terms. The date below shows the latest version.</p>
<h2>Contact</h2>
<p>Questions: <a href="mailto:{E(MAIL)}">{E(MAIL)}</a></p>
<p class="muted">Last updated November 22, 2026.</p>''')
    page('/404.html', 'Page not found', 'This page does not exist.',
         '<section class="wrap prose"><h1>Page not found</h1><p class="lead">That page doesn\'t exist.</p><p><a class="btn" href="/">Go to the homepage</a> <a class="btn ghost" href="/guides/">Read our guides</a></p></section>', ads_on=False)

GDIR = os.path.join(ROOT, 'guides')
CATS = [('Teaching', 'For teachers', 'Quizzes, writing, whiteboards and classroom tech that works.'),
        ('Events', 'For organizers', 'Tickets, payments, check-in and planning for small events.'),
        ('Creating', 'For creators', 'Video sizes, backgrounds and recap videos for schools, churches and small teams.')]
APPS = {a['name']: a for a in CFG['apps']}
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def load_guides():
    out = []
    for f in sorted(glob.glob(os.path.join(GDIR, '*.html'))):
        head, body = open(f).read().split('\n---\n', 1)
        g = dict(l.split(': ', 1) for l in head.strip().splitlines())
        g['slug'] = os.path.basename(f)[:-5]
        g['body'] = body.strip()
        g.setdefault('date', CFG.get('guides_published', '2026-11-20'))
        g.setdefault('updated', g['date'])
        g['words'] = len(re.sub(r'<[^>]+>', ' ', body).split())
        g['mins'] = max(1, round(g['words'] / 220))
        out.append(g)
    order = CFG.get('guides_order', [])
    out.sort(key=lambda g: (order.index(g['slug']) if g['slug'] in order else 99, g['title']))
    return out

def nice_date(d):
    y, m, dd = map(int, d.split('-'))
    return f'{MONTHS[m - 1]} {dd}, {y}'

def gcard(g):
    t = g['short'][0].upper() + g['short'][1:]
    return (f'<a class="gcard" href="/guides/{g["slug"]}/"><span class="gcat">{E(g["cat"])}</span>'
            f'<h3>{E(t)}</h3><p>{E(g["desc"])}</p><span class="gmeta">{g["mins"]} min read</span></a>')

def guides():
    G = load_guides()
    for g in G:
        app = APPS.get(g.get('app', ''))
        appbox = ''
        if app and not app.get('soon'):
            appbox = (f'<aside class="appbox" style="--c:{app["color"]}"><div><b>{E(app["name"])}</b> · {E(app["for"])}<p>{E(app["blurb"])}</p></div>'
                      f'<a class="btn" href="{E(app["url"])}">Open {E(app["name"])}</a></aside>')
        rel = [x for x in G if x['cat'] == g['cat'] and x['slug'] != g['slug']][:3]
        url = f'{URL}/guides/{g["slug"]}/'
        ld = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'Article', 'headline': g['title'], 'description': g['desc'], 'datePublished': g['date'], 'dateModified': g['updated'],
             'author': {'@type': 'Organization', 'name': ST, 'url': URL + '/'},
             'publisher': {'@type': 'Organization', 'name': ST, 'url': URL + '/', 'logo': {'@type': 'ImageObject', 'url': URL + '/favicon.svg'}},
             'mainEntityOfPage': url, 'wordCount': g['words'], **({'image': [URL + m.group(1)]} if (m := re.search(r'src="(/guides/img/[^"]+)"', g['body'])) else {})},
            {'@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Guides', 'item': URL + '/guides/'},
                {'@type': 'ListItem', 'position': 2, 'name': g['short'], 'item': url}]}]}
        head = '\n<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace('</', '<\\/') + '</script>'
        upd = f' · Updated {nice_date(g["updated"])}' if g['updated'] != g['date'] else ''
        cat = g['cat']
        body = (f'<article class="wrap prose guide">\n'
                f'<nav class="crumbs"><a href="/guides/">Guides</a> › <a href="/guides/#{cat.lower()}">{E(cat)}</a></nav>\n'
                f'<h1>{E(g["title"])}</h1>\n'
                f'<p class="byline">By the {E(ST)} team · {nice_date(g["date"])}{upd} · {g["mins"]} min read</p>\n'
                f'{g["body"]}\n{appbox}\n'
                f'<p class="note">Spotted a mistake or have a tip to add? Email <a href="mailto:{E(MAIL)}">{E(MAIL)}</a>. We update our guides when tools and settings change.</p>\n'
                f'</article>\n'
                f'<section class="wrap section"><h2>More {E(cat.lower())} guides</h2><div class="guides">{"".join(gcard(x) for x in rel)}</div></section>')
        page(f'/guides/{g["slug"]}/', g['title'], g['desc'], body, head_extra=head, og_type='article')
    secs = ''
    for c, lab, d in CATS:
        items = [g for g in G if g['cat'] == c]
        if items:
            secs += (f'<section class="wrap section" id="{c.lower()}"><h2>{E(lab)}</h2><p class="muted">{E(d)}</p>'
                     f'<div class="guides">{"".join(gcard(g) for g in items)}</div></section>')
    page('/guides/', 'Guides for Teachers, Organizers and Creators',
         'Practical, free guides from Telar Labs: reducing cheating in online quizzes, teaching with a projector, selling event tickets, planning reunions and making videos.',
         '<section class="hero"><div class="wrap"><p class="eyebrow">Guides</p><h1>Practical guides for teachers, organizers and creators</h1>'
         f'<p class="lead">Step-by-step help for the everyday problems our apps were built for, written and reviewed by the {E(ST)} team. Useful whether or not you use our tools.</p></div></section>' + secs)
    return G

def extras(GUIDES=()):
    open(os.path.join(PUB, 'favicon.svg'), 'w').write(LOGO.replace('class="logo-mark" ', 'xmlns="http://www.w3.org/2000/svg" '))
    urls = ['/', '/guides/', '/about/', '/contact/', '/privacy/', '/terms/'] + [f'/guides/{g["slug"]}/' for g in GUIDES]
    open(os.path.join(PUB, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'<url><loc>{URL}{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    open(os.path.join(PUB, 'robots.txt'), 'w').write(f'User-agent: *\nDisallow: /cdn-cgi/\n\nUser-agent: Mediapartners-Google\nAllow: /\n\nSitemap: {URL}/sitemap.xml\n')
    if CFG.get('adsense_client'):
        pub = CFG['adsense_client'].replace('ca-', '')
        open(os.path.join(PUB, 'ads.txt'), 'w').write(f'google.com, {pub}, DIRECT, f08c47fec0942fa0\n')
    open(os.path.join(PUB, '_headers'), 'w').write('/assets/*\n  Cache-Control: public, max-age=86400\n')
    # Telar Stories moved to its own subdomain
    open(os.path.join(PUB, '_redirects'), 'w').write('/stories-demo https://stories.telarlabs.net/ 301\n/stories-demo/* https://stories.telarlabs.net/:splat 301\n')

if __name__ == '__main__':
    G = guides(); home(G); pages(); extras(G)
    print('Built Telar Labs home')
