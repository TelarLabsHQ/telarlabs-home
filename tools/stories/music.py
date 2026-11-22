"""Background music for Telar Stories: four calm, seamless loops (gentle, happy, dreamy, adventure).
Everything is synthesized here (no samples), so the music is original and free to use.
Notes that run past the end wrap round to the start, and the reverb is circular, so each file loops without a seam."""
import numpy as np, subprocess, os, sys
SR = 44100
OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'public', 'stories-demo', 'assets', 'music')
rng = np.random.default_rng(7)
mf = lambda m: 440 * 2 ** ((m - 69) / 12)
NOTE = {n: i for i, n in enumerate(['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])}
def m(s):  # 'C4' -> midi
    return NOTE[s[:-1]] + 12 * (int(s[-1]) + 1)

class Track:
    def __init__(self, secs): self.L = int(secs * SR); self.buf = np.zeros((2, self.L), np.float32)
    def add(self, t, sig, pan=0.0, gain=1.0):
        i = int(t * SR) % self.L; n = len(sig); l, r = np.sqrt((1 - pan) / 2), np.sqrt((1 + pan) / 2)
        idx = (np.arange(n) + i) % self.L
        np.add.at(self.buf[0], idx, sig * gain * l); np.add.at(self.buf[1], idx, sig * gain * r)

def env(n, a, d=None, rel=0.02):
    t = np.arange(n) / SR; e = np.minimum(1, t / max(a, 1e-4))
    if d is not None: e *= np.exp(-t / d)
    k = int(rel * SR); e[-k:] *= np.linspace(1, 0, k)
    return e

def piano(f, dur, vel=1.0):
    n = int((dur + 1.2) * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for h, (a, dec) in enumerate([(1, 1.6), (.45, 1.0), (.22, .7), (.12, .5), (.06, .35), (.03, .25)], 1):
        fh = f * h * (1 + 0.0004 * h * h); s += a * np.sin(2 * np.pi * fh * t + rng.uniform(0, 6.28)) * np.exp(-t / (dec * (220 / f) ** .3))
    s *= env(n, .006, None, .3); s[int(dur * SR):] *= np.exp(-np.arange(n - int(dur * SR)) / SR / .25)
    return s * vel * .35

def marimba(f, vel=1.0):
    n = int(1.1 * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) * np.exp(-t / .38) + .35 * np.sin(2 * np.pi * f * 3.93 * t) * np.exp(-t / .06) + .12 * np.sin(2 * np.pi * f * 9.2 * t) * np.exp(-t / .02)
    return s * env(n, .002, None, .05) * vel * .5

def musicbox(f, vel=1.0):
    n = int(2.6 * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) * np.exp(-t / 1.1) + .3 * np.sin(2 * np.pi * f * 2 * t) * np.exp(-t / .5) + .15 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t / .12)
    return s * env(n, .002, None, .1) * vel * .32

def pluck(f, dur=0.6, vel=1.0, bright=.5):   # Karplus-Strong, a soft ukulele-like pluck
    n = int((dur + .4) * SR); p = int(SR / f); buf = np.convolve(rng.uniform(-1, 1, p + 8), np.ones(6) / 6, 'valid')[:p] * 2; out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]; buf[i % p] = .996 * ((1 - bright) * buf[i % p] + bright * .5 * (buf[i % p] + buf[(i + 1) % p]))
    return out * env(n, .002, None, .1) * vel * .4

def pad(freqs, dur, vel=1.0, bright=.25, att=1.2):
    n = int((dur + 1.5) * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for f in freqs:
        for det in (-0.004, 0, 0.005):
            ph = rng.uniform(0, 6.28); ff = f * (1 + det)
            s += np.sin(2 * np.pi * ff * t + ph) + bright * .5 * np.sin(4 * np.pi * ff * t + ph) + bright * .25 * np.sin(6 * np.pi * ff * t + ph)
    e = np.minimum(1, t / att); r = np.clip((dur + 1.5 - t) / 1.5, 0, 1); s *= e * r
    return s / (len(freqs) * 3) * vel * .5

def strings(f, dur, vel=1.0):   # short bowed note
    n = int((dur + .25) * SR); t = np.arange(n) / SR
    s = sum((1 / h) * np.sin(2 * np.pi * f * h * t * (1 + .003 * np.sin(2 * np.pi * 5.5 * t))) for h in range(1, 7))
    return s * env(n, .03, None, .2) * np.exp(-t / (dur * 2.5)) * vel * .18

def kick(vel=1.0):
    n = int(.35 * SR); t = np.arange(n) / SR; f = 50 + 70 * np.exp(-t / .03)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / .12) * vel * .7

def tom(f=90, vel=1.0):
    n = int(.6 * SR); t = np.arange(n) / SR; ff = f * (1 + .6 * np.exp(-t / .04))
    return (np.sin(2 * np.pi * np.cumsum(ff) / SR) * np.exp(-t / .25) + .05 * np.convolve(rng.uniform(-1, 1, n), np.ones(6) / 6, 'same') * np.exp(-t / .02)) * vel * .55

def shaker(vel=1.0):
    n = int(.12 * SR); t = np.arange(n) / SR; x = rng.uniform(-1, 1, n)
    x = np.convolve(x, np.ones(3) / 3, 'same') - np.convolve(x, np.ones(25) / 25, 'same')   # soft, mid-high hiss
    return x * np.minimum(1, t / .015) * np.exp(-t / .03) * vel * .05

def reverb(tr, secs=2.4, mix=.25, damp=4000):
    """circular convolution with a decaying-noise impulse response, so the loop stays seamless"""
    n = int(secs * SR); t = np.arange(n) / SR
    out = np.zeros_like(tr.buf)
    for c in range(2):
        ir = rng.normal(0, 1, n) * np.exp(-t / (secs / 5))
        ir = np.convolve(ir, np.ones(8) / 8, 'same')   # soften highs
        ir[:int(.012 * SR)] = 0; ir /= np.sqrt((ir ** 2).sum())
        L = tr.L; X = np.fft.rfft(tr.buf[c]); h = np.zeros(L); h[:min(n, L)] = ir[:L]
        wet = np.fft.irfft(X * np.fft.rfft(h), L)
        out[c] = tr.buf[c] + mix * wet * 3
    tr.buf = out

def finish(tr, name):
    b = tr.buf / (np.abs(tr.buf).max() + 1e-9) * .85
    rms = np.sqrt((b ** 2).mean()); b *= min(1.0, 0.12 / rms)   # similar loudness for every style
    b = np.clip(b, -.95, .95)
    os.makedirs(OUT, exist_ok=True)
    raw = (b.T * 32767).astype('<i2').tobytes()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', '-', '-c:a', 'aac', '-b:a', '96k',
                    os.path.join(OUT, name + '.m4a')], input=raw, check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', '-', '-c:a', 'libmp3lame', '-b:a', '128k',
                    f'/tmp/music-{name}.mp3'], input=raw, check=True)
    print(name, round(tr.L / SR, 1), 's')

def chords_of(names): return [[m(x) for x in c.split()] for c in names]

def gentle():
    bpm = 72; beat = 60 / bpm; bar = 4 * beat
    ch = chords_of(['C3 E3 G3 C4', 'A2 E3 A3 C4', 'F2 C3 F3 A3', 'G2 D3 G3 B3', 'C3 E3 G3 C4', 'A2 E3 A3 C4', 'D3 F3 A3 C4', 'G2 D3 G3 B3'])
    mel = ['E5 4', 'D5 2', 'C5 2', 'C5 4', 'E5 2', 'G5 2', 'A5 4', 'G5 2', 'F5 2', 'D5 6', '- 2',
           'E5 2', 'G5 2', 'E5 2', 'C5 2', 'A4 4', 'C5 4', 'D5 3', 'E5 1', 'F5 4', 'D5 6', '- 2']
    tr = Track(len(ch) * 2 * bar)
    for k in range(len(ch) * 2):
        c = ch[k % len(ch)]; t0 = k * bar
        tr.add(t0, pad([mf(x) for x in c[1:]], bar, .55, .1), 0, 1)
        for i, x in enumerate([c[0], c[1], c[2], c[3], c[2], c[1], c[2], c[3]]):
            tr.add(t0 + i * beat / 2, piano(mf(x + 12 if i in (3, 7) else x), beat, .5 + .1 * (i % 2 == 0)), -.2 + .05 * i, 1)
    t = 0; mel = mel * 2
    for ev in mel:
        n, d = ev.split(); d = float(d) * beat / 2
        if n != '-': tr.add(t, piano(mf(m(n)), d, .75), .15)
        t += d
    reverb(tr, 2.6, .3); finish(tr, 'gentle')

def happy():
    bpm = 112; beat = 60 / bpm; bar = 4 * beat
    ch = chords_of(['G3 B3 D4', 'D3 F#3 A3', 'E3 G3 B3', 'C3 E3 G3'])
    mel = ['B4 1', 'D5 1', 'G5 2', 'F#5 1', 'E5 1', 'D5 2', 'A4 1', 'B4 1', 'C5 1', 'D5 1', 'E5 2', 'D5 2',
           'B4 1', 'G4 1', 'B4 1', 'D5 1', 'E5 2', 'G5 2', 'E5 1', 'D5 1', 'C5 1', 'B4 1', 'A4 2', '- 2',
           'B4 1', 'D5 1', 'G5 2', 'A5 1', 'G5 1', 'F#5 2', 'E5 1', 'F#5 1', 'G5 1', 'E5 1', 'D5 2', 'B4 2',
           'C5 1', 'E5 1', 'D5 1', 'C5 1', 'B4 2', 'A4 2', 'G4 4', '- 4']
    bars = 16; tr = Track(bars * bar)
    for k in range(bars):
        c = ch[k % 4]; t0 = k * bar
        for i in range(8):   # ukulele strum pattern
            if i in (0, 2, 3, 5, 6):
                for j, x in enumerate(c): tr.add(t0 + i * beat / 2 + j * .012, pluck(mf(x + 12), beat * .45, .5 if i % 2 else .7), .25)
        for i, b in enumerate([0, 2]): tr.add(t0 + b * beat, pluck(mf(c[0] - 12), beat * 1.6, .9, .3), -.1)
        for i in range(4): tr.add(t0 + i * beat, kick(.5 if i % 2 else .7), 0)
        for i in range(8): tr.add(t0 + i * beat / 2 + (.02 if i % 2 else 0), shaker(.9 if i % 2 else .6), .35)
    t = 0
    for ev in mel * 2:
        n, d = ev.split(); d = float(d) * beat / 2
        if n != '-': tr.add(t, marimba(mf(m(n)), .9), -.2)
        t += d
    reverb(tr, 1.6, .18); finish(tr, 'happy')

def dreamy():
    bpm = 60; beat = 60 / bpm; bar = 4 * beat
    ch = chords_of(['F2 A3 C4 E4', 'D2 A3 C4 F4', 'A#1 A#3 D4 F4', 'C2 G3 C4 E4'])
    mel = ['C6 2', 'A5 2', 'G5 2', 'F5 2', 'A5 4', '- 4', 'D6 2', 'C6 2', 'A5 2', 'F5 2', 'G5 6', '- 2',
           'F5 2', 'A5 2', 'C6 2', 'D6 2', 'C6 4', 'A5 4', 'G5 2', 'A5 2', 'F5 4', '- 8']
    bars = 8; tr = Track(bars * bar)
    for k in range(bars):
        c = ch[k % 4]; t0 = k * bar
        tr.add(t0, pad([mf(x) for x in c[1:]], bar, .8, .05, 2.0), 0)
        tr.add(t0, pad([mf(c[0])], bar, .5, .0, 1.0), 0)
        for i, x in enumerate([c[1], c[2], c[3], c[2]]): tr.add(t0 + i * beat + beat / 2, musicbox(mf(x + 12), .35), .4 - .2 * i)
    t = 0
    for ev in mel:
        n, d = ev.split(); d = float(d) * beat / 2
        if n != '-': tr.add(t, musicbox(mf(m(n)), .8), -.1)
        t += d
    reverb(tr, 4.0, .45); finish(tr, 'dreamy')

def adventure():
    bpm = 100; beat = 60 / bpm; bar = 4 * beat
    ch = chords_of(['D3 F3 A3', 'A#2 D3 F3', 'F2 A2 C3', 'C3 E3 G3'])
    mel = ['A4 3', 'D5 1', 'F5 2', 'E5 2', 'D5 3', 'A#4 1', 'D5 4', 'C5 3', 'F5 1', 'A5 2', 'G5 2', 'E5 6', '- 2',
           'A4 3', 'D5 1', 'F5 2', 'G5 2', 'A5 3', 'A#5 1', 'A5 4', 'G5 2', 'F5 2', 'E5 2', 'C5 2', 'D5 6', '- 2']
    bars = 16; tr = Track(bars * bar)
    for k in range(bars):
        c = ch[k % 4]; t0 = k * bar
        for i in range(8):   # galloping string ostinato
            x = c[[0, 0, 1, 0, 2, 0, 1, 0][i]]
            tr.add(t0 + i * beat / 2, strings(mf(x + 12), beat * .35, .9 if i % 2 == 0 else .6), -.3)
        tr.add(t0, pad([mf(x) for x in c], bar, .45, .45, .4), .2)
        tr.add(t0, strings(mf(c[0] - 12), bar * .9, 1.2), 0)
        for b, (f, v) in enumerate([(70, .9), (None, 0), (95, .5), (80, .6)]):
            if f: tr.add(t0 + b * beat, tom(f, v), -.1 + .1 * b)
        if k % 2 == 1: tr.add(t0 + 3.5 * beat, tom(110, .45), .2)
    t = 0
    if True:
        for rep in range(2):
            for ev in mel:
                n, d = ev.split(); d = float(d) * beat / 2
                if n != '-' and rep == 1 or (n != '-' and t >= 0 and rep == 0 and False): pass
                if n != '-': tr.add(t, strings(mf(m(n)), d * .9, 1.6) + .0, .1)
                t += d
    reverb(tr, 2.2, .25); finish(tr, 'adventure')

if __name__ == '__main__':
    for f in (sys.argv[1:] or ['gentle', 'happy', 'dreamy', 'adventure']): globals()[f]()
