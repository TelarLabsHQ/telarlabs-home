"""Green-screen key for the Friends 'sharing food' sprite (kids-lunch). The key green is very bright,
so it is removed everywhere (also the gaps between chair legs) while darker garnish greens stay."""
from PIL import Image
import numpy as np
from scipy import ndimage
SRC='/mnt/user-data/attachments/c4c42cf4-7f0e-5510-8275-f3b972cef798/a111f586-image.png'
OUT='/home/claude/telarlabs-home/stories-site/public/assets/ch/kids-lunch.webp'
a=np.asarray(Image.open(SRC).convert('RGB')).astype(float); r,g,b=a[...,0],a[...,1],a[...,2]
d=g-np.maximum(r,b)
key=(g>160)&(d>85)                                   # the neon key colour
key=ndimage.binary_opening(key,iterations=1)
lab,n=ndimage.label(key); sizes=ndimage.sum(key,lab,range(1,n+1))
key=np.isin(lab,1+np.flatnonzero(sizes>=6))           # ignore tiny specks inside the drawing
top=np.zeros_like(key); top[:480]=True                # above the food: catch green slivers between braids
key|=top&(g>200)&(d>130)
near=ndimage.binary_dilation(key,iterations=3)
soft=np.clip(1-(d-30)/70,0,1)
alpha=np.where(key,0,np.where(near,soft,1))
g2=np.where(near&(d>0),np.maximum(r,b),g)
o=Image.fromarray(np.dstack([r,g2,b,alpha*255]).astype(np.uint8),'RGBA')
o=o.crop(o.getbbox()); o=o.resize((round(o.width*700/o.height),700),Image.LANCZOS)
o.save(OUT,'WEBP',quality=88,method=6); print(o.size)
bg=Image.new('RGBA',o.size,(255,0,255,255)); bg.alpha_composite(o); bg.convert('RGB').save('/tmp/kl_m.png')
