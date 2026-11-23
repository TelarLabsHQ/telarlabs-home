"""Turn a colour character sprite into clean black line art for colouring pages."""
import numpy as np, sys
from PIL import Image, ImageFilter
from scipy import ndimage
def lineart(src, h=1400):
    im = Image.open(src).convert('RGBA'); im = im.resize((round(im.width*h/im.height), h), Image.LANCZOS)
    a = np.asarray(im).astype(float); alpha = a[..., 3] / 255
    g = (0.3*a[...,0] + 0.59*a[...,1] + 0.11*a[...,2]) * alpha + 255*(1-alpha)
    # difference of Gaussians picks up the drawn outlines and big colour edges, not soft shading
    g1 = ndimage.gaussian_filter(g, 1.0); g2 = ndimage.gaussian_filter(g, 2.2)
    dog = g1 - 0.985*g2
    lines = dog < -4.5
    dark = g < 60; lines |= dark & ~ndimage.binary_erosion(dark, iterations=2)   # outline dark areas instead of filling them
    sil = alpha > .5; edge = sil ^ ndimage.binary_erosion(sil, iterations=3)
    lines |= edge                                         # a firm outer outline
    lines = ndimage.binary_opening(lines, iterations=0) if False else lines
    lab, n = ndimage.label(lines); sz = ndimage.sum(lines, lab, range(1, n+1))
    lines = np.isin(lab, 1 + np.flatnonzero(sz >= 25))   # drop specks
    out = np.where(lines, 0, 255).astype(np.uint8)
    o = Image.fromarray(out, 'L').filter(ImageFilter.GaussianBlur(.6)).point(lambda v: 0 if v < 150 else 255)
    return o
if __name__ == '__main__':
    lineart(sys.argv[1]).save(sys.argv[2])
