"""Printable activity pack for 'Mira and the Rainy Day' (3 pages, A4, works on Letter too)."""
import os, sys
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
sys.path.insert(0, os.path.dirname(__file__)); from lineart import lineart

SITE = '/home/claude/telarlabs-home/stories-site/public/'
CH, BG = SITE + 'assets/ch/', SITE + 'assets/bg/'
OUT = SITE + 'printables/'; os.makedirs(OUT, exist_ok=True)
F = '/usr/share/fonts/truetype/google-fonts/'
pdfmetrics.registerFont(TTFont('P', F + 'Poppins-Regular.ttf')); pdfmetrics.registerFont(TTFont('PB', F + 'Poppins-Bold.ttf'))
W, H = A4; M = 48   # margins keep everything inside US Letter too
TMP = '/tmp/claude-print/'; os.makedirs(TMP, exist_ok=True)

def scene(bg, chars, name):
    im = Image.open(BG + bg + '.webp').convert('RGBA').resize((1280, 720))
    for k, x, h in chars:
        c = Image.open(CH + k + '.webp').convert('RGBA'); c = c.resize((round(c.width * h / c.height), h))
        im.alpha_composite(c, (x - c.width // 2, 690 - h))
    p = TMP + name + '.jpg'; im.convert('RGB').resize((640, 360)).save(p, quality=85); return p

def footer(c):
    c.setFont('P', 9); c.setFillGray(.45)
    c.drawCentredString(W / 2, 30, 'Telar Stories · stories.telarlabs.net · Free to print for home, class and church')
    c.setFillGray(0)

c = canvas.Canvas(OUT + 'mira-and-the-rainy-day-activities.pdf', pagesize=A4)
c.setTitle('Mira and the Rainy Day – Activity pack'); c.setAuthor('Telar Labs')

# 1. colouring page
c.setFont('PB', 26); c.drawCentredString(W / 2, H - 70, 'Color Mira and Mochi!')
c.setFont('P', 12); c.drawCentredString(W / 2, H - 92, 'From the story "Mira and the Rainy Day"')
mira = TMP + 'mira-l.png'; lineart(CH + 'mira-wave-happy.webp').save(mira)
mochi = TMP + 'mochi-l.png'; lineart(CH + 'mochi-sitting.webp').save(mochi)
mi, mo = Image.open(mira), Image.open(mochi)
h1 = 520; w1 = h1 * mi.width / mi.height
h2 = 250; w2 = h2 * mo.width / mo.height
y0 = 80
c.drawImage(ImageReader(mira), M, y0 + 50, w1, h1, mask='auto')
c.drawImage(ImageReader(mochi), W - M - w2 - 10, y0 + 40, w2, h2, mask='auto')
c.setLineWidth(2); c.setDash(6, 5); c.roundRect(W - M - 150, H - 330, 150, 150, 14); c.setDash()
c.setFont('P', 11); c.drawCentredString(W - M - 75, H - 200, 'Draw a raindrop or')
c.drawCentredString(W - M - 75, H - 215, 'a rainbow here!')
c.setFont('P', 12); c.drawString(M, y0 + 10, 'My name: ____________________________')
footer(c); c.showPage()

# 2. put the story in order
c.setFont('PB', 24); c.drawCentredString(W / 2, H - 70, 'Put the story in order')
c.setFont('P', 12); c.drawCentredString(W / 2, H - 92, 'Write 1, 2, 3 and 4 in the circles to show what happened first, next and last.')
S = [  # shown out of order on purpose
 (scene('garden-rainbow', [('mira-jumping', 520, 330), ('mochi-walking', 760, 150)], 'o4'), 'Mira jumps for joy under a rainbow.'),
 (scene('reading-nook', [('mira-bored', 560, 320), ('mochi-sleeping', 820, 120)], 'o1'), 'It is raining. Mira has nothing to do.'),
 (scene('reading-nook', [('mira-reading', 600, 300), ('mochi-sitting', 860, 150)], 'o3'), 'Mira reads the stories in the old red book.'),
 (scene('library', [('mochi-book', 640, 200)], 'o2'), 'Bump! Mochi pushes a red book onto the floor.'),
]
bw = (W - 2 * M - 24) / 2; bh = bw * 9 / 16
for i, (p, cap) in enumerate(S):
    x = M + (i % 2) * (bw + 24); y = H - 140 - bh - (i // 2) * (bh + 90)
    c.drawImage(p, x, y, bw, bh); c.setLineWidth(1.5); c.rect(x, y, bw, bh)
    c.setFillGray(1); c.circle(x + 26, y + bh - 26, 18, fill=1); c.setFillGray(0); c.setLineWidth(2); c.circle(x + 26, y + bh - 26, 18)
    c.setFont('P', 11); c.drawString(x, y - 18, cap)
c.setFont('PB', 13); c.drawString(M, 190, 'Retell it!')
c.setFont('P', 12); c.drawString(M, 170, 'Use your numbers to tell the story to a friend or a grown-up.')
c.setFont('P', 9); c.setFillGray(.5); c.drawString(M, 120, 'Answers: rainy day 1 · Mochi and the book 2 · reading 3 · rainbow 4'); c.setFillGray(0)
footer(c); c.showPage()

# 3. think, talk and draw
c.setFont('PB', 24); c.drawCentredString(W / 2, H - 70, 'Think, talk and draw')
Q = ['How did Mira feel at the start of the story? How do you know?',
     'What did Mochi do that changed Mira\'s day?',
     'What was inside the old red book?',
     'What do YOU like to do on a rainy day?']
y = H - 115
c.setFont('PB', 13); c.drawString(M, y, 'Talk about it'); y -= 24
c.setFont('P', 12)
for n, q in enumerate(Q, 1):
    c.drawString(M, y, f'{n}.  {q}'); y -= 22
    c.setLineWidth(.6); c.setStrokeGray(.6); c.line(M + 20, y, W - M, y); c.setStrokeGray(0); y -= 26
y -= 6; c.setFont('PB', 13); c.drawString(M, y, 'Draw your own rainy-day adventure'); y -= 14
c.setFont('P', 11); c.drawString(M, y - 4, 'What would you find inside a magic book? Draw it here.')
c.setLineWidth(2); c.roundRect(M, 80, W - 2 * M, y - 100, 14)
c.setFont('P', 11); c.drawString(M + 12, 92, 'My story is called: ____________________________________________')
footer(c); c.showPage()
c.save()

# a preview image for the web page (page 1)
print('ok')
