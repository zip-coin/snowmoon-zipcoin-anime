"""Build Seedance last-frame images: keyframe + payment card (and red ring for shot 7).
Run from the scripts/ folder after make_cards.py:  python3 make_endframes.py
"""
from PIL import Image
import numpy as np

KF = "../images/keyframes/"
CARDS = "../assets/cards/"
OUT = "../assets/endframes/"

A = Image.open(KF + "keyframe_A_counter.jpg").convert("RGBA")   # hand over the counter circle
B = Image.open(KF + "keyframe_B_device.jpg").convert("RGBA")    # Gladias looking at his device

def holo(card, width, alpha=0.93):
    c = Image.open(CARDS + card).convert("RGBA")
    c = c.resize((width, int(c.height * width / c.width)), Image.LANCZOS)
    a = np.asarray(c).astype(float); a[..., 3] *= alpha
    return Image.fromarray(a.astype(np.uint8))

def red_ring(img, cx=1190, cy=706, rx=332, ry=130):
    """Recolour the green counter ring to red (ellipse measured on keyframe A)."""
    a = np.asarray(img.convert("RGB")).astype(float)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    H, W = r.shape
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2)
    ann = np.clip(1 - np.abs(d - 1) / 0.22, 0, 1)
    w = ann * np.clip((g - np.maximum(r, b)) / 8, 0, 1)
    br = (r + g + b) / 3
    out = np.stack([r*(1-w) + np.clip(br*1.25, 0, 255)*w, g*(1-w) + br*0.45*w, b*(1-w) + br*0.45*w], -1)
    return Image.fromarray(out.clip(0, 255).astype(np.uint8)).convert("RGBA")

W = A.size[0]
e = red_ring(A); e.alpha_composite(holo("card_7_declined.png", 700), (W - 730, 40))
e.convert("RGB").save(OUT + "endframe_7_declined.jpg", quality=95)

e = B.copy(); e.alpha_composite(holo("card_8_loan_request.png", 640), (20, 60))
e.convert("RGB").save(OUT + "endframe_8_loan.jpg", quality=95)

e = B.copy(); e.alpha_composite(holo("card_8b_received.png", 640), (20, 120))
e.convert("RGB").save(OUT + "endframe_8b_received.jpg", quality=95)

e = A.copy(); e.alpha_composite(holo("card_9_success.png", 700), (W - 730, 10))
e.convert("RGB").save(OUT + "endframe_9_success.jpg", quality=95)
print("end frames written to", OUT)
