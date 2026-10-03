# Optional: camera-move clips from the keyframes (no AI video). shot6 = Lectoby listening, used for the last line.
import numpy as np, subprocess, math
from PIL import Image

KF={1:'../images/keyframes/kf1_knock_wide.jpg',2:'../images/keyframes/kf2_seila_door.jpg',3:'../images/keyframes/kf3_watch_blank.jpg',4:'../images/keyframes/kf4_mov.jpg',5:'../images/keyframes/kf5_lectoby.jpg','3b':'../assets/ep5_kf3_burned.jpg'}
OW,OH,FPS=1920,1080,30
def load(k): return Image.open(KF[k]).convert('RGB').resize((OW,OH),Image.LANCZOS)
ease=lambda t: t*t*(3-2*t)
def frame(img,z,cx,cy,dx=0,dy=0):
    w,h=OW/z,OH/z; x0=cx*OW-w/2+dx; y0=cy*OH-h/2+dy
    x0=min(max(x0,0),OW-w); y0=min(max(y0,0),OH-h)
    return img.transform((OW,OH),Image.EXTENT,(x0,y0,x0+w,y0+h),Image.BICUBIC)
def shake(t,hits,amp=6,dur=0.18):
    dx=dy=0
    for h in hits:
        if h<=t<h+dur:
            p=(t-h)/dur; a=amp*(1-p)
            dx+=a*math.sin(p*40); dy+=a*0.6*math.cos(p*37)
    return dx,dy
def write(name,secs,fn):
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{OW}x{OH}','-r',str(FPS),'-i','-',
        '-c:v','libx264','-pix_fmt','yuv420p','-crf','18',name],stdin=subprocess.PIPE)
    n=int(secs*FPS)
    for i in range(n):
        p.stdin.write(np.asarray(fn(i/FPS,i/(n-1))).tobytes())
    p.stdin.close(); p.wait(); print('ok',name)
k1=load(1); write('shot1_knock_wide.mp4',5,lambda t,u: frame(k1,1+0.10*ease(u),0.70,0.48,*shake(t,[1.2,1.55,3.2,3.55],5)))
k2=load(2); write('shot2_knock_again.mp4',4,lambda t,u: frame(k2,1.02+0.08*ease(u),0.45,0.42,*shake(t,[0.9,1.25],5)))
k3=load(3); k3b=load('3b')
def s3(t,u):
    a=min(max((t-1.0)/0.5,0),1)
    img=Image.blend(k3,k3b,a)
    dx,dy=shake(t,[0.85,1.05],7,0.15)
    return frame(img,1.0+0.12*ease(u),0.51,0.45,dx,dy)
write('shot3_watch_burned.mp4',4.5,s3)
k4=load(4); write('shot4_mov.mp4',4,lambda t,u: frame(k4,1.0+0.18*ease(u),0.5,0.30))
write('shot5_seila_talking.mp4',8,lambda t,u: frame(k2,1.05+0.05*u,0.40+0.03*u,0.42))
k5=load(5); write('shot6_lectoby_talking.mp4',8,lambda t,u: frame(k5,1.05+0.06*u,0.55-0.03*u,0.45))
