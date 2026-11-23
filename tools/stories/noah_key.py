"""Green-screen key for the Noah-with-dove sprite. Only green connected to the image border is removed,
so the green olive leaf (enclosed by its outline) stays solid."""
from PIL import Image, ImageFilter
import numpy as np
from scipy import ndimage
SRC='/mnt/user-data/attachments/c4c42cf4-7f0e-5510-8275-f3b972cef798/0fc5a2ad-image.jpg'
OUT='/home/claude/telarlabs-home/stories-site/public/assets/ch/noah-dove.webp'
a=np.asarray(Image.open(SRC).convert('RGB')).astype(float); r,g,b=a[...,0],a[...,1],a[...,2]
d=g-np.maximum(r,b)
lab,_=ndimage.label(d>25)
edge=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
bg=np.isin(lab,list(edge))
near=ndimage.binary_dilation(bg,iterations=3)        # soft edge band around the background
soft=np.clip(1-(d-25)/45,0,1)
alpha=np.where(bg,0,np.where(near,soft,1))
g2=np.where(near&(d>0),np.maximum(r,b),g)           # remove green spill on edges only
o=Image.fromarray(np.dstack([r,g2,b,alpha*255]).astype(np.uint8),'RGBA')
o=o.crop(o.getbbox()); o=o.resize((round(o.width*700/o.height),700),Image.LANCZOS)
o.save(OUT,'WEBP',quality=88,method=6); print(o.size)
