# Builds the message card for KF4 (episode 4). Run from episode-04/scripts:  python3 make_card.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, numpy.linalg as la, cv2, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SRC='../images/keyframes/kf4_card_blank.jpg'
im=Image.open(SRC).convert('RGB'); W,H=im.size
Q=np.array([(407,48),(1399,49),(1345,503),(461,515.5)],float)
c=Q.mean(0); QI=c+(Q-c)*np.array([0.88,0.84])
REG='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'; BOLD='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
F=lambda p,s: ImageFont.truetype(p,s,index=0)
CW,CH=2400,1100
INK=(52,38,32); SOFT=(110,88,76); FIRE=(196,72,30)
cv=Image.new('RGBA',(CW,CH),(0,0,0,0)); d=ImageDraw.Draw(cv)
def ctr(y,t,f,fill):
    w=d.textlength(t,font=f); d.text(((CW-w)/2,y),t,font=f,fill=fill); return w
logo=Image.open('../../assets/logo/zipcoin_logo_transparent.png').convert('RGBA')
L=logo.resize((190,190),Image.LANCZOS)
f1=F(BOLD,120); t1='Beautiful Plants food court'; tw=d.textlength(t1,font=f1)
x0=(CW-(190+40+tw))/2; cv.alpha_composite(L,(int(x0),10)); d.text((x0+230,20),t1,font=f1,fill=INK)
ctr(225,'2415 Len Su street, Sadzu Du',F(REG,92),SOFT)
ctr(355,'sa dzu du de   len su 2415 de   bun kai mo fan',ImageFont.truetype(MONO,64),SOFT)
d.line((200,480,CW-200,480),fill=(140,115,100,200),width=6)
# fire emoji + big line
emo=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf',109)
e=Image.new('RGBA',(140,140),(0,0,0,0)); ImageDraw.Draw(e).text((0,0),'🔥',font=emo,embedded_color=True)
e=e.crop(e.getbbox()).resize((170,170),Image.LANCZOS)
fb=F(BOLD,170); t2='400 zipcoins burned'; w2=d.textlength(t2,font=fb)
x2=(CW-(170+40+w2))/2; cv.alpha_composite(e,(int(x2),565)); d.text((x2+210,525),t2,font=fb,fill=FIRE)
ctr(790,'to send this message',F(BOLD,110),INK)
def coeffs(dst,src):
    A=[];B=[]
    for (x,y),(u,v) in zip(dst,src):
        A+=[[x,y,1,0,0,0,-u*x,-u*y],[0,0,0,x,y,1,-v*x,-v*y]];B+=[u,v]
    return la.solve(np.array(A,float),np.array(B,float))
def warp(img,q,cw,ch): return np.array(img.transform((W,H),Image.PERSPECTIVE,coeffs([tuple(p) for p in q],[(0,0),(cw,0),(cw,ch),(0,ch)]),Image.BICUBIC)).astype(float)
wa=warp(cv,QI,CW,CH)
base=np.array(im).astype(float)
pm=Image.new('L',(W,H),0); ImageDraw.Draw(pm).polygon([tuple(p) for p in c+(Q-c)*0.97],fill=255)
pm=np.array(pm.filter(ImageFilter.GaussianBlur(6))).astype(float)[...,None]/255
frost=np.array(Image.fromarray(base.astype(np.uint8)).filter(ImageFilter.GaussianBlur(4))).astype(float)*0.4+np.array([240,228,210])*0.6
base=base*(1-pm*0.6)+frost*(pm*0.6)
al=wa[...,3]/255
glow=np.array(Image.fromarray((al*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(4))).astype(float)[...,None]/255
base=base+(255-base)*glow*0.35
a=(al*0.93)[...,None]; out=base*(1-a)+wa[...,:3]*a
# watch screen: logo only
arr=np.array(im).astype(int); m=(arr.min(2)>225).astype(np.uint8); sub=np.zeros_like(m); sub[560:800,740:1000]=m[560:800,740:1000]
n,l,s,_=cv2.connectedComponentsWithStats(sub); i=1+np.argmax(s[1:,4]); x,y,w,h,_=s[i]
ws=Image.new('RGBA',(w*4,h*4),(0,0,0,0)); lg=logo.resize((int(w*4*0.62),int(w*4*0.62)),Image.LANCZOS)
ws.alpha_composite(lg,((w*4-lg.width)//2,(h*4-lg.height)//2-20))
ws=ws.resize((w,h),Image.LANCZOS); lay=Image.new('RGBA',(W,H),(0,0,0,0)); lay.paste(ws,(x,y))
la_=np.array(lay).astype(float); mk=np.array(Image.fromarray((l==i).astype(np.uint8)*255).filter(ImageFilter.MinFilter(5))).astype(float)/255
a2=(la_[...,3]/255*mk)[...,None]; out=out*(1-a2)+la_[...,:3]*a2
res=Image.fromarray(out.clip(0,255).astype(np.uint8)); res.save('../assets/ep4_kf4_message.jpg',quality=95)
