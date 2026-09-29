"""Episode 2 end frames: air card on keyframe 1, holograms warped into keyframe 4.
Run after make_graphics.py:  python3 make_endframes.py"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np, numpy.linalg as la
KF="../images/keyframes/"; A="../assets/"
def coeffs(dst,src):
    A=[];B=[]
    for (x,y),(u,v) in zip(dst,src):
        A+=[[x,y,1,0,0,0,-u*x,-u*y],[0,0,0,x,y,1,-v*x,-v*y]];B+=[u,v]
    return la.solve(np.array(A,float),np.array(B,float))

# ---- keyframe 1 + air card ----
k1=Image.open(KF+"kf1_gladias_watch.jpg").convert("RGBA")
for v in ("906","918"):
    c=Image.open(A+f"cards/ep2_air_{v}.png").convert("RGBA"); w=330; c=c.resize((w,int(c.height*w/c.width)),Image.LANCZOS)
    e=k1.copy(); e.alpha_composite(c,(560,300)); e.convert("RGB").save(A+f"endframes/end_shot1_air_{v}.jpg",quality=95)

# ---- keyframe 4 + holograms, warped into the panel ----
k4=Image.open(KF+"kf4_hologram_blank.jpg").convert("RGBA"); W,H=k4.size
Q=[(724,142),(1181,236),(1181,640),(724,789)]
cx=sum(p[0] for p in Q)/4; cy=sum(p[1] for p in Q)/4
Qi=[(cx+(x-cx)*0.93, cy+(y-cy)*0.93) for x,y in Q]
def put(holo_file,out):
    base=k4.copy()
    # tint the glass darker so the light graphics read
    tint=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(tint).polygon(Q,fill=(28,20,44,150))
    base.alpha_composite(tint.filter(ImageFilter.GaussianBlur(2)))
    h=Image.open(holo_file).convert("RGBA"); hw,hh=h.size
    wh=h.transform((W,H),Image.PERSPECTIVE,coeffs(Qi,[(0,0),(hw,0),(hw,hh),(0,hh)]),Image.BICUBIC)
    # screen-blend the light graphics onto the panel
    b=np.asarray(base).astype(float); o=np.asarray(wh).astype(float)
    al=o[...,3:4]/255; col=o[...,:3]
    scr=255-(255-b[...,:3])*(1-col/255)
    b[...,:3]=b[...,:3]*(1-al)+scr*al
    # the whale layer is semi-opaque colour, so composite it normally too
    Image.fromarray(b.clip(0,255).astype(np.uint8)).convert("RGB").save(out,quality=95)
put(A+"holograms/ep2_holo_scheme.png",A+"endframes/end_shot4_scheme.jpg")
put(A+"holograms/ep2_holo_bluewhale.png",A+"endframes/end_shot5_bluewhale.jpg")
print("ok")
