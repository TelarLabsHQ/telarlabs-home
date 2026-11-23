"""Printable activity packs for the Telar Stories ready-made stories (3 pages each, A4, fits US Letter).
Page 1: colouring page. Page 2: put four scenes in order. Page 3: talk-about questions and a drawing box."""
import os, sys, random
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from lineart import lineart

SITE = '/home/claude/telarlabs-home/stories-site/public/'
CH, BG = SITE + 'assets/ch/', SITE + 'assets/bg/'
OUT = SITE + 'printables/'; os.makedirs(OUT, exist_ok=True)
F = '/usr/share/fonts/truetype/google-fonts/'
pdfmetrics.registerFont(TTFont('P', F + 'Poppins-Regular.ttf')); pdfmetrics.registerFont(TTFont('PB', F + 'Poppins-Bold.ttf'))
W, H = A4; M = 48
TMP = '/tmp/claude-print/'; os.makedirs(TMP, exist_ok=True)

PACKS = {
 'mira-and-the-rainy-day': dict(title='Mira and the Rainy Day', color='Color Mira and Mochi!',
   chars=[('mira-wave-happy', 1.0), ('mochi-sitting', .45)], box='Draw a raindrop or\na rainbow here!',
   scenes=[('reading-nook', [('mira-bored', 346, 700, 315), ('mochi-sleeping', 633, 703, 100)], 'It is raining. Mira has nothing to do.'),
           ('library', [('mira-surprised', 373, 673, 315), ('mochi-book', 653, 667, 160)], 'Bump! Mochi pushes a red book onto the floor.'),
           ('reading-nook', [('mira-reading', 400, 700, 315), ('mochi-sleeping', 633, 703, 100)], 'Mira reads the stories in the old red book.'),
           ('garden-rainbow', [('mira-jumping', 600, 687, 385), ('mochi-meow', 800, 693, 140)], 'Mira jumps for joy under a rainbow.')],
   qs=['How did Mira feel at the start of the story? How do you know?', 'What did Mochi do that changed Mira\'s day?',
       'What was inside the old red book?', 'What do YOU like to do on a rainy day?'],
   draw='Draw your own rainy-day adventure', drawsub='What would you find inside a magic book? Draw it here.', name='My story is called'),
 'the-first-christmas': dict(title='The First Christmas', color='Color Mary and baby Jesus!',
   chars=[('mary-baby', 1.0), ('donkey-standing', .55)], box='Draw the bright\nstar here!',
   scenes=[('nazareth-house', [('mary-praying', 480, 715, 360), ('gabriel-arms', 860, 715, 430)], 'The angel Gabriel visits Mary.'),
           ('road-bethlehem', [('mary-donkey', 520, 715, 400), ('joseph-standing', 860, 715, 400)], 'Mary and Joseph travel to Bethlehem.'),
           ('stable', [('baby-manger', 640, 715, 170), ('mary-kneeling', 400, 715, 330), ('joseph-standing', 900, 715, 400)], 'Baby Jesus is born in a stable.'),
           ('fields-night', [('shepherd-boy-surprised', 420, 715, 330), ('shepherd-old-looking', 700, 715, 380), ('angel-choir', 980, 520, 300)], 'Angels sing to the shepherds.')],
   qs=['Who told Mary that she would have a baby?', 'Why did Mary and Joseph stay in a stable?',
       'Who came to visit baby Jesus?', 'Why do we call Jesus God\'s greatest gift?'],
   draw='Draw the night Jesus was born', drawsub='Draw the stable, the star, the shepherds or the angels.', name='My picture is called'),
 'the-lost-sheep': dict(title='The Lost Sheep', color='Color the shepherd and the lamb!',
   chars=[('shepherd-carrying-lamb', 1.0), ('lamb-sad', .45)], box='Draw the ninety-nine\nsheep here!',
   scenes=[('pasture', [('flock', 867, 673, 200), ('shepherd-worried', 373, 680, 387)], 'One little lamb is missing!'),
           ('ravine-dusk', [('shepherd-walking', 640, 693, 347)], 'The shepherd searches the rocky hills.'),
           ('ravine-night', [('shepherd-hugging-lamb', 640, 693, 373)], '"I found you!" He holds the lamb close.'),
           ('village-night', [('shepherd-carrying-lamb', 640, 693, 387)], 'He carries the lamb home with joy.')],
   qs=['How many sheep did the shepherd have?', 'How did the shepherd feel when one lamb was lost?',
       'Why didn\'t the shepherd give up, even at night?', 'What does this story tell us about how God loves us?'],
   draw='Draw the shepherd finding the lamb', drawsub='Draw the happy moment, or the party with his friends.', name='My picture is called'),
 'the-christmas-gift': dict(title='The Christmas Gift', color='Color Lily and Mr. Ben!',
   chars=[('lily-cookies', .78), ('ben-card', 1.0)], box='Draw a Christmas\ncookie here!',
   scenes=[('toy-shop', [('lily-window', 640, 760, 430)], 'Lily sees a snow globe at the toy shop.'),
           ('snowy-street', [('lily-walking', 300, 705, 320), ('ben-sad', 1010, 700, 300)], 'Lily sees Mr. Ben, all alone.'),
           ('gift-kitchen', [('mom-rolling', 880, 760, 430), ('lily-stirring', 360, 720, 280)], 'Lily and Mom bake cookies.'),
           ('ben-living', [('ben-card', 330, 715, 400), ('lily-standing', 660, 715, 320), ('mom-singing', 1000, 760, 470)], 'Mr. Ben smiles the biggest smile.')],
   qs=['What did Lily want to buy with her coins?', 'Why was Mr. Ben sad at Christmas?',
       'What did Lily give Mr. Ben instead?', 'Who could YOU make happy with a small gift?'],
   draw='Draw a gift you could make for someone', drawsub='Who is it for? What would make them smile?', name='My gift is for'),
 'noahs-ark': dict(title="Noah's Ark", color='Color Noah and the animals!',
   chars=[('noah-welcome', 1.0), ('sheep-pair', .42)], box='Draw a rainbow\nhere!',
   scenes=[('ark-building', [('noah-family', 780, 715, 230), ('noah-hammer', 260, 715, 390)], 'Noah and his family build the ark.'),
           ('ark-hill', [('elephants', 1090, 718, 190), ('giraffes', 820, 718, 220), ('zebras', 520, 718, 170), ('lions', 220, 718, 170)], 'The animals come, two by two.'),
           ('ark-storm', [], 'It rains for forty days and forty nights.'),
           ('ark-mountain', [('noah-dove', 280, 715, 360)], 'The dove brings back an olive leaf.')],
   qs=['What did God ask Noah to build?', 'How did the animals come to the ark?',
       'What did the dove bring back to Noah?', 'What does the rainbow remind us of?'],
   draw='Draw your favorite animals going into the ark', drawsub='Remember: two by two!', name='My animals are'),
 'friends-around-the-world': dict(title='Friends Around the World', color='Color the friends!',
   chars=[('kids-wave', 1.0)], box='Draw yourself as\na new friend here!',
   scenes=[('school-gate', [('amara-shy', 640, 715, 340)], 'Amara\'s first day at a new school.'),
           ('classroom-map', [('paolo-pancit', 640, 715, 350)], 'Paolo shares pancit from the Philippines.'),
           ('classroom-map', [('rose-hands', 330, 715, 440), ('amara-jollof', 720, 715, 340)], 'Amara shares jollof rice.'),
           ('school-lunch', [('kids-lunch', 640, 720, 340)], 'Everyone shares their food at lunch.')],
   qs=['How did Amara feel on her first day? Why?', 'Which greeting did you like best: Kumusta, Cześć, Hallo or Bawo ni?',
       'What food would you bring to Share Your Home Day?', 'How can you help a new classmate feel welcome?'],
   draw='Draw something special from your family', drawsub='A food, a game, a song or a place you love. How do you say "hello" at home?', name='My name is'),
}

def scene(bg, chars, name):
    im = Image.open(BG + bg + '.webp').convert('RGBA').resize((1280, 720))
    for k, x, y, h in chars:
        c = Image.open(CH + k + '.webp').convert('RGBA'); c = c.resize((round(c.width * h / c.height), h))
        im.alpha_composite(c, (x - c.width // 2, y - h))
    p = TMP + name + '.jpg'; im.convert('RGB').resize((640, 360)).save(p, quality=85); return p

def footer(c):
    c.setFont('P', 9); c.setFillGray(.45)
    c.drawCentredString(W / 2, 30, 'Telar Stories · stories.telarlabs.net · Free to print for home, class and church'); c.setFillGray(0)

def build(slug, d):
    c = canvas.Canvas(OUT + slug + '-activities.pdf', pagesize=A4)
    c.setTitle(d['title'] + ' – Activity pack'); c.setAuthor('Telar Labs')
    # 1 colouring
    c.setFont('PB', 26); c.drawCentredString(W / 2, H - 70, d['color'])
    c.setFont('P', 12); c.drawCentredString(W / 2, H - 92, f'From the story "{d["title"]}"')
    arts = []
    for k, rel in d['chars']:
        p = TMP + k + '-l.png'; lineart(CH + k + '.webp').save(p); im = Image.open(p); arts.append((p, im.width / im.height, rel))
    top = H - 120 - (190 if d['box'] else 0); bottom = 90; avail_h = top - bottom; avail_w = W - 2 * M
    gap = 16
    scale = min(avail_h, (avail_w - gap * (len(arts) - 1)) / sum(r * rel for _, r, rel in arts))
    x = M + (avail_w - sum(scale * rel * r for _, r, rel in arts) - gap * (len(arts) - 1)) / 2
    for p, r, rel in arts:
        h = scale * rel; w = h * r; c.drawImage(ImageReader(p), x, bottom + 10, w, h, mask='auto'); x += w + gap
    if d['box']:
        c.setLineWidth(2); c.setDash(6, 5); c.roundRect(W - M - 170, H - 300, 170, 160, 14); c.setDash()
        c.setFont('P', 11)
        for i, line in enumerate(d['box'].split('\n')): c.drawCentredString(W - M - 85, H - 165 - i * 15, line)
        c.setFont('PB', 13); c.drawString(M, H - 150, 'Color, then add your own')
        c.drawString(M, H - 168, 'drawing in the box!')
    c.setFont('P', 12); c.drawString(M, 70, 'My name: ____________________________')
    footer(c); c.showPage()
    # 2 order
    c.setFont('PB', 24); c.drawCentredString(W / 2, H - 70, 'Put the story in order')
    c.setFont('P', 12); c.drawCentredString(W / 2, H - 92, 'Write 1, 2, 3 and 4 in the circles to show what happened first, next and last.')
    order = list(range(4)); random.Random(slug).shuffle(order)
    if order == [0, 1, 2, 3]: order = [2, 0, 3, 1]
    bw = (W - 2 * M - 24) / 2; bh = bw * 9 / 16
    for pos, i in enumerate(order):
        bg, chars, cap = d['scenes'][i]; p = scene(bg, chars, f'{slug}-{i}')
        x = M + (pos % 2) * (bw + 24); y = H - 140 - bh - (pos // 2) * (bh + 90)
        c.drawImage(p, x, y, bw, bh); c.setLineWidth(1.5); c.rect(x, y, bw, bh)
        c.setFillGray(1); c.circle(x + 26, y + bh - 26, 18, fill=1); c.setFillGray(0); c.setLineWidth(2); c.circle(x + 26, y + bh - 26, 18)
        c.setFont('P', 11); c.drawString(x, y - 18, cap)
    c.setFont('PB', 13); c.drawString(M, 190, 'Retell it!')
    c.setFont('P', 12); c.drawString(M, 170, 'Use your numbers to tell the story to a friend or a grown-up.')
    ans = ' · '.join(f'{["top left", "top right", "bottom left", "bottom right"][pos]} {order[pos] + 1}' for pos in range(4))
    c.setFont('P', 9); c.setFillGray(.5); c.drawString(M, 120, 'Answers: ' + ans); c.setFillGray(0)
    footer(c); c.showPage()
    # 3 think, talk and draw
    c.setFont('PB', 24); c.drawCentredString(W / 2, H - 70, 'Think, talk and draw')
    y = H - 115; c.setFont('PB', 13); c.drawString(M, y, 'Talk about it'); y -= 24
    for n, q in enumerate(d['qs'], 1):
        c.setFont('P', 12); c.drawString(M, y, f'{n}.  {q}'); y -= 22
        c.setLineWidth(.6); c.setStrokeGray(.6); c.line(M + 20, y, W - M, y); c.setStrokeGray(0); y -= 26
    y -= 6; c.setFont('PB', 13); c.drawString(M, y, d['draw']); y -= 14
    c.setFont('P', 11); c.drawString(M, y - 4, d['drawsub'])
    c.setLineWidth(2); c.roundRect(M, 80, W - 2 * M, y - 100, 14)
    c.setFont('P', 11); c.drawString(M + 12, 92, d['name'] + ': ' + '_' * (62 - len(d['name'])))
    footer(c); c.showPage(); c.save()

if __name__ == '__main__':
    import subprocess
    for slug, d in PACKS.items():
        if len(sys.argv) > 1 and slug not in sys.argv[1:]: continue
        build(slug, d)
        subprocess.run(['pdftoppm', '-r', '70', '-png', OUT + slug + '-activities.pdf', TMP + 'pv'], check=True)
        for i in (1, 2, 3): Image.open(f'{TMP}pv-{i}.png').save(f'{OUT}{slug}-p{i}.webp', 'WEBP', quality=80)
        print('ok', slug)
