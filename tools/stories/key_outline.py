"""Key out the green and peel off the white sticker outline that some image tools add."""
import sys, numpy as np
from PIL import Image
from scipy import ndimage
def key(src, out, h=700, t=30):
    a = np.asarray(Image.open(src).convert('RGB')).astype(float); r, g, b = a[..., 0], a[..., 1], a[..., 2]
    d = g - np.maximum(r, b)
    lab, _ = ndimage.label(d > t)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    sizes = ndimage.sum(np.ones_like(d), lab, range(1, lab.max() + 1))
    big = {i + 1 for i, n in enumerate(sizes) if n >= (150 if t <= 30 else 15)}             # enclosed gaps (between legs, under arms) are background too
    bg = np.isin(lab, list(edge | big))
    bg[:6, :] = bg[-6:, :] = True; bg[:, :6] = bg[:, -6:] = True     # thin frame lines some tools leave at the edge
    lum = (r + g + b) / 3; sat = np.max(a, 2) - np.min(a, 2)
    light = (lum > 185) & (sat < 70) | ((d > 8) & (lum > 120))          # cream outline, plus green-tinted fringe
    rim = ndimage.binary_dilation(bg) & ~bg
    has_outline = (rim & light).sum() > 0.6 * rim.sum()                   # only peel when the picture really has a sticker border
    for _ in range(18 if has_outline else 0):                                                   # peel outward-in, stop at the drawing's own dark line
        ring = ndimage.binary_dilation(bg) & ~bg & light
        if not ring.any(): break
        bg |= ring
    bg = ndimage.binary_dilation(bg, iterations=1)                       # take the last anti-aliased pixel too
    alpha = ndimage.gaussian_filter((~bg).astype(float), 0.7)
    alpha = np.where(bg & (alpha < .5), 0, alpha)
    near = ndimage.binary_dilation(bg, iterations=3)
    g2 = np.where((d > 0) & (near | (t <= 30)), np.maximum(r, b), g)   # with a high threshold, only despill the edge
    o = Image.fromarray(np.dstack([r, g2, b, np.clip(alpha, 0, 1) * 255]).astype(np.uint8), 'RGBA')
    o = o.crop(o.getbbox()); o = o.resize((round(o.width * h / o.height), h), Image.LANCZOS)
    o.save(out, 'WEBP', quality=88, method=6); return o
if __name__ == '__main__':
    key(sys.argv[1], sys.argv[2], t=int(sys.argv[3]) if len(sys.argv) > 3 else 30)
