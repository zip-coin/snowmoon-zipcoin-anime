"""Episode 2 graphics: watch air cards + QF scheme / Bluewhale holograms.
Run from episode-02/scripts:  python3 make_graphics.py  (needs Pillow + numpy)"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
REG="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"; BOLD="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
F=lambda s,b=False: ImageFont.truetype(BOLD if b else REG,s,index=0)
LOGO=Image.open("../../assets/logo/zipcoin_logo_transparent.png").convert("RGBA")
PURPLE=(36,24,54,235); GREEN=(126,230,170); WHITE=(245,245,250); SOFT=(200,195,215); AMBER=(245,190,90)

def card(w,h,border,pad=80):
    W,H=w+pad*2,h+pad*2; base=Image.new("RGBA",(W,H),(0,0,0,0))
    g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).rounded_rectangle((pad,pad,pad+w,pad+h),44,outline=border+(200,),width=16)
    base.alpha_composite(g.filter(ImageFilter.GaussianBlur(24)))
    b=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(b).rounded_rectangle((pad,pad,pad+w,pad+h),40,fill=PURPLE,outline=border+(255,),width=5)
    base.alpha_composite(b); return base,ImageDraw.Draw(base),pad

# ---- watch air readings (book layout: Air | CO2 | PM2.5) ----
for co2,name in ((906,"ep2_air_906.png"),(918,"ep2_air_918.png")):
    img,d,p=card(700,420,AMBER)
    d.text((p+60,p+45),"Air",font=F(60,True),fill=WHITE)
    d.line([(p+60,p+140),(p+640,p+140)],fill=(90,80,115),width=3)
    for i,(k,v) in enumerate((("CO2",str(co2)),("PM2.5","4.4"))):
        y=p+170+i*110; f=F(64,i==0)
        d.text((p+60,y),k,font=F(56),fill=SOFT)
        tw=d.textlength(v,font=f); d.text((p+640-tw,y),v,font=f,fill=AMBER+(255,) if i==0 else WHITE)
    img.save("../assets/cards/"+name)

# ---- hologram explainer (light lines on transparent, use Screen blend) ----
HC=(225,238,255)
def holo_canvas(W,H):
    return Image.new("RGBA",(W,H),(0,0,0,0))
def glowify(img):
    a=img.split()[3]; g=Image.new("RGBA",img.size,HC+(0,)); g.putalpha(a.filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.8)))
    out=Image.new("RGBA",img.size,(0,0,0,0)); out.alpha_composite(g); out.alpha_composite(img); return out
def rrect(d,box,r,w=5,fill=None): d.rounded_rectangle(box,r,outline=HC+(255,),width=w,fill=fill)
def arrow(d,x0,y,x1):
    d.line([(x0,y),(x1,y)],fill=HC+(255,),width=6); d.polygon([(x1,y),(x1-26,y-16),(x1-26,y+16)],fill=HC+(255,))
def ctext(d,x,y,t,f,fill=HC+(255,)): d.text((x-d.textlength(t,font=f)/2,y),t,font=f,fill=fill)
def logo_light(size):
    l=LOGO.resize((size,size),Image.LANCZOS); a=np.asarray(l).astype(float)
    lum=(a[...,0]*.3+a[...,1]*.59+a[...,2]*.11)/255
    e=np.asarray(Image.fromarray((lum*255).astype(np.uint8)).filter(ImageFilter.FIND_EDGES).filter(ImageFilter.MaxFilter(3))).astype(float)/255
    al=np.clip(0.18+1.7*e,0,1)*a[...,3]
    o=np.dstack([np.full(lum.shape,c) for c in HC]+[al]).astype(np.uint8); return Image.fromarray(o,"RGBA")
def device(d,x,y):
    rrect(d,(x,y,x+120,y+200),20); d.line([(x+40,y+180),(x+80,y+180)],fill=HC+(255,),width=5)
    d.polygon([(x+60,y+120),(x+35,y+85),(x+50,y+85),(x+50,y+50),(x+70,y+50),(x+70,y+85),(x+85,y+85)],fill=HC+(255,))

W,H=1800,1000
h=holo_canvas(W,H); d=ImageDraw.Draw(h)
rrect(d,(20,20,W-20,H-20),40,w=4)
ctext(d,W/2,50,"QUADRATIC FUNDING ROUND",F(58,True))
# step 1
device(d,120,260); ctext(d,180,480,"download",F(38)); ctext(d,180,525,"the program",F(38))
arrow(d,280,360,470)
# step 2 donate
h.alpha_composite(logo_light(170),(500,240)); ctext(d,585,430,"donate",F(40)); ctext(d,585,475,"10 zc",F(72,True))
arrow(d,700,360,890)
# project box
rrect(d,(910,200,1330,560),30); ctext(d,1120,225,"polarization",F(36)); ctext(d,1120,265,"research",F(36))
ctext(d,1120,310,"(\"not a very good one\")",F(28))
h.alpha_composite(logo_light(110),(1065,360)); ctext(d,1120,480,"100 zc",F(56,True))
ctext(d,1120,570,"incl. bounded matching",F(30))
# reward back: the PROGRAM pays you (source hidden until the reveal)
d.line([(180,600),(180,760)],fill=HC+(255,),width=6); d.line([(180,760),(585,760)],fill=HC+(255,),width=6)
d.line([(585,760),(585,600)],fill=HC+(255,),width=6); d.polygon([(585,590),(569,616),(601,616)],fill=HC+(255,))
ctext(d,900,735,"the program pays you back",F(40))
ctext(d,900,785,"20 zc",F(72,True))
ctext(d,W/2,900,"lots of people participated",F(40))
glowify(h).save("../assets/holograms/ep2_holo_scheme.png")

# whale reveal version: dim scheme + whale behind
h2=holo_canvas(W,H); d2=ImageDraw.Draw(h2)
wh=Image.new("RGBA",(W,H),(0,0,0,0)); dw=ImageDraw.Draw(wh)
BLUE=(120,170,255)
dw.ellipse((200,300,1150,740),fill=BLUE+(120,))
dw.polygon([(1050,440),(1400,500),(1400,560),(1050,640)],fill=BLUE+(120,))
dw.polygon([(1380,530),(1620,400),(1560,530),(1620,660)],fill=BLUE+(120,))
dw.polygon([(620,650),(760,820),(820,660)],fill=BLUE+(120,))
dw.ellipse((360,450,400,490),fill=(20,30,60,200))
dw.arc((240,480,560,640),20,80,fill=(20,30,60,200),width=6)
for dx in (-40,0,40): dw.line([(470,300),(470+dx*2,190)],fill=BLUE+(170,),width=10)
wh=wh.filter(ImageFilter.GaussianBlur(3))
sch=Image.open("../assets/holograms/ep2_holo_scheme.png"); sa=np.asarray(sch).astype(float); sa[...,3]*=0.45; sch=Image.fromarray(sa.astype(np.uint8))
h2.alpha_composite(wh); h2.alpha_composite(sch)
d2=ImageDraw.Draw(h2)
d2.rounded_rectangle((520,40,1280,150),30,fill=(20,30,60,210),outline=BLUE+(255,),width=5)
ctext(d2,W/2,55,"all their doing: Bluewhale",F(56,True),fill=(200,225,255,255))
h2.save("../assets/holograms/ep2_holo_bluewhale.png")

print("graphics written")
