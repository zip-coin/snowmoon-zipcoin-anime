# Builds the watch screens and the Hydrafill poster for episode 3.
# Run from episode-03/scripts:  python3 make_screens.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, cv2
U="../images/keyframes/"
REG="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"; BOLD="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
MONO="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
F=lambda s,b=False: ImageFont.truetype(BOLD if b else REG,s,index=0)
LOGO=Image.open("../../assets/logo/zipcoin_logo_transparent.png").convert("RGBA")
GREEN=(40,150,95); DG=(126,230,170)

def place(src,box,draw_fn,mask_fn,out,bg,geo=None):
    im=Image.open(U+src).convert("RGBA"); W,H=im.size
    cx,cy,w,h,ang=geo
    S=3; iw,ih=int(w*0.96),int(h*0.96)
    cv=Image.new("RGBA",(iw*S,ih*S),bg+(255,)); draw_fn(cv,ImageDraw.Draw(cv),iw*S,ih*S)
    cv=cv.resize((iw,ih),Image.LANCZOS)
    rot=cv.rotate(ang,resample=Image.BICUBIC,expand=True,fillcolor=bg+(255,))
    layer=Image.new("RGBA",(W,H),bg+(255,)); layer.paste(rot,(int(cx-rot.width/2),int(cy-rot.height/2)))
    if mask_fn=="rect":
        rm=Image.new("L",(int(w*0.97),int(h*0.97)),0); ImageDraw.Draw(rm).rounded_rectangle((0,0,rm.width-1,rm.height-1),int(min(w,h)*0.14),fill=255)
        rm=rm.rotate(ang,resample=Image.BICUBIC,expand=True)
        mk=Image.new("L",(W,H),0); mk.paste(rm,(int(cx-rm.width/2),int(cy-rm.height/2)))
        mk=mk.filter(ImageFilter.GaussianBlur(1.5))
    else:
        a=np.asarray(im.convert("RGB")).astype(int)
        m=mask_fn(a).astype(np.uint8)
        n,lab,st,_=cv2.connectedComponentsWithStats(m)
        i=1+np.argmax(st[1:,4]); m=(lab==i)
        mk=Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.5))
    im.paste(layer,(0,0),mk)
    im.convert("RGB").save("../assets/screens/"+out,quality=95)
def ct(d,W,y,t,f,fill): d.text(((W-d.textlength(t,font=f))/2,y),t,font=f,fill=fill)

# ---- Febric watch: request (and confirmed) ----
FB=(252,246,232)
def febric(confirmed):
    def fn(cv,d,W,H):
        ink=(40,36,50)
        l=LOGO.resize((150,150),Image.LANCZOS); cv.alpha_composite(l,((W-150)//2,40))
        ct(d,W,205,"Wallet 0x8f62...",ImageFont.truetype(MONO,44),ink)
        ct(d,W,265,"social recovery mode",F(44,True),GREEN)
        ct(d,W,320,"transaction request",F(44,True),GREEN)
        d.line([(80,392),(W-80,392)],fill=(210,200,185),width=4)
        ct(d,W,410,"Hydrafill",F(52),ink)
        ct(d,W,475,"5.5 zipcoins",F(76,True),ink)
        bx0,by0,bx1,by1=W//2-190,H-165,W//2+190,H-65
        if confirmed:
            d.rounded_rectangle((bx0,by0,bx1,by1),50,outline=GREEN,width=6,fill=(225,245,232))
            ct(d,W,by0+14,"Confirmed ✓",F(50,True),GREEN)
        else:
            d.rounded_rectangle((bx0,by0,bx1,by1),50,fill=GREEN)
            ct(d,W,by0+14,"Confirm",F(54,True),(255,255,255))
    return fn
fmask=lambda a: a.mean(2)>225
for c,n in ((False,"ep3_febric_request.jpg"),(True,"ep3_febric_confirmed.jpg")):
    place("kf5_febric_watch_blank.jpg",None,febric(c),fmask,n,FB,(852,445,268,315,14.39))

# ---- Gladias watch: Seila question / signatures ----
GB=(14,13,20)
def question(cv,d,W,H):
    wh=(240,238,248); soft=(170,165,190)
    l=LOGO.resize((120,120),Image.LANCZOS); cv.alpha_composite(l,(60,70))
    d.text((200,82),"Recovery check",font=F(40,True),fill=DG)
    d.text((200,132),"from Seila",font=F(36),fill=soft)
    d.line([(60,220),(W-60,220)],fill=(60,56,80),width=4)
    lines=["What was the most","unusual thing I did","on the evening the kids","came back from","Vil and Daia's?"]
    y=255
    for t in lines: ct(d,W,y,t,F(46,True),wh); y+=66
    bx0,by0,bx1,by1=W//2-200,H-150,W//2+200,H-60
    d.rounded_rectangle((bx0,by0,bx1,by1),45,outline=DG,width=5)
    ct(d,W,by0+14,"Answer",F(46,True),DG)
def sigs(cv,d,W,H):
    wh=(240,238,248); soft=(170,165,190)
    l=LOGO.resize((150,150),Image.LANCZOS); cv.alpha_composite(l,((W-150)//2,90))
    ct(d,W,255,"Hydrafill · 5.5 zc",F(46),soft)
    ct(d,W,330,"Signatures",F(56,True),wh)
    r=48; gap=40; tot=4*2*r+3*gap; sx=(W-tot)//2; cy=500
    for i in range(4):
        cx=sx+r+i*(2*r+gap)
        if i<3:
            d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=GREEN)
            d.line([(cx-20,cy),(cx-5,cy+17),(cx+22,cy-16)],fill=(255,255,255),width=9,joint="curve")
        else:
            d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=soft,width=6)
    ct(d,W,590,"3 of 4",F(64,True),DG)
    ct(d,W,680,"1 remaining",F(46),soft)
gmask=lambda a: a.mean(2)<30
place("kf6_gladias_watch_blank.jpg",None,question,"rect","ep3_gladias_question.jpg",GB,(934,512,294,354,7.77))
place("kf6_gladias_watch_blank.jpg",None,sigs,"rect","ep3_gladias_signatures.jpg",GB,(934,512,294,354,7.77))

# ---- Hydrafill poster on KF4 ----
im=Image.open(U+"kf4_febric_poster_raw.jpg").convert("RGBA"); d=ImageDraw.Draw(im)
t="Hydrafill"; f=F(24,True); w=d.textlength(t,font=f)
d.text((525-w/2,100),t,font=f,fill=(70,120,50,255))
im.convert("RGB").save("../assets/screens/ep3_kf4_poster.jpg",quality=95)
print("ok")
