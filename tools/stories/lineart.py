"""Turn a colour character sprite into clean black line art for colouring pages."""
import numpy as np, sys
from PIL import Image, ImageFilter
from scipy import ndimage
def lineart(src, h=1400):
    im = Image.open(src).convert('RGBA'); im = im.resize((round(im.width*h/im.height), h), Image.LANCZOS)
    a = np.asarray(im).astype(float); alpha = a[..., 3] / 255
    sil = alpha > .5
    g = (0.3*a[...,0] + 0.59*a[...,1] + 0.11*a[...,2]) * alpha + 255*(1-alpha)
    # difference of Gaussians picks up the drawn outlines and big colour edges, not soft shading
    g1 = ndimage.gaussian_filter(g, 1.0); g2 = ndimage.gaussian_filter(g, 2.2)
    dog = g1 - 0.985*g2
    lines = dog < -4.5
    dark = g < 60
    lab_d, nd = ndimage.label(dark); sz_d = ndimage.sum(dark, lab_d, range(1, nd + 1))
    small = np.isin(lab_d, 1 + np.flatnonzero(sz_d < 0.0009 * dark.size))   # pupils, nostrils, buttons: keep solid
    lines |= small | (dark & ~small & ~ndimage.binary_erosion(dark, iterations=2))   # big dark areas (hair): outline only
    # irises: closed shapes that were dark in the picture are filled solid (in the upper part, where faces are,
    # so dark clothing patterns stay open for colouring)
    ys = np.where(sil.any(1))[0]; ytop = int(ys[0] + 0.5 * (ys[-1] - ys[0])) if len(ys) else g.shape[0]
    closed = ndimage.binary_closing(lines, iterations=3)
    holes, nh = ndimage.label(~closed)
    for k, sl in enumerate(ndimage.find_objects(holes), 1):
        if sl[0].stop > ytop: continue
        m = holes[sl] == k; area = m.sum(); hh, ww = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        mean = g[sl][m].mean(); shine = (m & (g[sl] > 235)).sum()   # eyes have a white highlight; skin and cloth don't
        if 0.00003 * g.size < area < 0.006 * g.size and 0.5 < hh / max(ww, 1) < 2.2 and (mean < 100 or (mean < 175 and shine > 4)):
            lines[sl] |= m
    # eyes: keep the iris solid and the white highlight white, so they look like the colour picture
    lines &= ~(g > 235)
    edge = sil ^ ndimage.binary_erosion(sil, iterations=3)
    lines |= edge                                         # a firm outer outline
    lab, n = ndimage.label(lines); sz = ndimage.sum(lines, lab, range(1, n+1))
    lines = np.isin(lab, 1 + np.flatnonzero(sz >= 25))   # drop specks
    out = np.where(lines, 0, 255).astype(np.uint8)
    o = Image.fromarray(out, 'L').filter(ImageFilter.GaussianBlur(.6)).point(lambda v: 0 if v < 150 else 255)
    return o
if __name__ == '__main__':
    lineart(sys.argv[1]).save(sys.argv[2])
