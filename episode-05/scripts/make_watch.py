from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, numpy.linalg as la, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SRC='../images/keyframes/kf3_watch_blank.jpg'
im=Image.open(SRC).convert('RGB'); W,H=im.size
Q=[(801,320),(1031,316),(1036,596),(806,600)]
BOLD='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; REG='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
F=lambda p,s: ImageFont.truetype(p,s,index=0)
CW,CH=920,1120
INK=(34,30,32); FIRE=(205,72,28)
cv=Image.new('RGBA',(CW,CH),(0,0,0,0)); d=ImageDraw.Draw(cv)
def ctr(y,t,f,fill):
    w=d.textlength(t,font=f); d.text(((CW-w)/2,y),t,font=f,fill=fill)
logo=Image.open('../../assets/logo/zipcoin_logo_transparent.png').convert('RGBA').resize((190,190),Image.LANCZOS)
cv.alpha_composite(logo,((CW-190)//2,70))
emo=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf',109)
e=Image.new('RGBA',(140,140),(0,0,0,0)); ImageDraw.Draw(e).text((0,0),'🔥',font=emo,embedded_color=True)
e=e.crop(e.getbbox()).resize((210,210),Image.LANCZOS); cv.alpha_composite(e,((CW-210)//2,300))
ctr(540,'50 zipcoins',F(BOLD,130),FIRE)
ctr(720,'have just been',F(BOLD,96),INK)
ctr(850,'burned.',F(BOLD,96),INK)
def coeffs(dst,src):
    A=[];B=[]
    for (x,y),(u,v) in zip(dst,src):
        A+=[[x,y,1,0,0,0,-u*x,-u*y],[0,0,0,x,y,1,-v*x,-v*y]];B+=[u,v]
    return la.solve(np.array(A,float),np.array(B,float))
wa=np.array(cv.transform((W,H),Image.PERSPECTIVE,coeffs(Q,[(0,0),(CW,0),(CW,CH),(0,CH)]),Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.4))).astype(float)
arr=np.array(im).astype(int); lit=(arr.min(2)>200).astype(np.uint8)*255
clip=np.array(Image.fromarray(lit).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1))).astype(float)/255
a=(wa[...,3]/255*clip)[...,None]
out=np.array(im).astype(float)*(1-a)+wa[...,:3]*a
res=Image.fromarray(out.clip(0,255).astype(np.uint8)); res.save('../assets/ep5_kf3_burned.jpg',quality=95)
