"""Build the zipcoin payment card PNGs (transparent) from the flat logo.
Run from the scripts/ folder:  python3 make_cards.py   (needs Pillow + numpy)
Font: Noto Sans CJK (any clean sans works; change REG/BOLD paths)."""
import os
OUT = "../assets/cards/"
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps
import numpy as np

SRC = "../assets/logo/zipcoin_logo_flat.jpg"
REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
def F(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size, index=0)

# ---- logo: crop coin, circular mask ----
im = Image.open(SRC).convert("RGB")
a = np.asarray(im).astype(int)
mask = (a.min(axis=2) < 235)
ys, xs = np.where(mask)
x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
r = max(x1 - x0, y1 - y0) / 2 + 2
coin = im.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r))).convert("RGBA")
S = coin.size[0]
m = Image.new("L", (S * 4, S * 4), 0)
ImageDraw.Draw(m).ellipse((0, 0, S * 4 - 1, S * 4 - 1), fill=255)
m = m.resize((S, S), Image.LANCZOS)
coin.putalpha(m)
coin = coin.resize((800, 800), Image.LANCZOS)
coin.save("../assets/logo/zipcoin_logo_transparent.png")

def grey(img):
    g = ImageOps.grayscale(img.convert("RGB"))
    g = g.point(lambda v: int(v * 0.6 + 40))
    out = Image.merge("RGBA", (g, g, g, img.split()[3]))
    return out
coin_grey = grey(coin)
coin_grey.save("../assets/logo/zipcoin_logo_greyed.png")

PURPLE = (36, 24, 54, 235)
GREEN = (126, 230, 170)
RED = (240, 96, 96)
WHITE = (245, 245, 250)
SOFT = (200, 195, 215)

def card(w, h, border, pad=90):
    W, H = w + pad * 2, h + pad * 2
    base = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # glow
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).rounded_rectangle((pad, pad, pad + w, pad + h), 48, outline=border + (200,), width=18)
    glow = glow.filter(ImageFilter.GaussianBlur(28))
    base.alpha_composite(glow)
    body = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(body)
    d.rounded_rectangle((pad, pad, pad + w, pad + h), 44, fill=PURPLE, outline=border + (255,), width=5)
    base.alpha_composite(body)
    return base, ImageDraw.Draw(base), pad

def paste_logo(img, logo, x, y, size):
    l = logo.resize((size, size), Image.LANCZOS)
    img.alpha_composite(l, (x, y))

def tick(d, x, y, s, col):
    d.line([(x, y + s * 0.55), (x + s * 0.38, y + s * 0.9), (x + s, y + s * 0.1)], fill=col, width=int(s * 0.16), joint="curve")

def cross(d, x, y, s, col):
    w = int(s * 0.16)
    d.line([(x, y), (x + s, y + s)], fill=col, width=w)
    d.line([(x + s, y), (x, y + s)], fill=col, width=w)

# 1 declined
img, d, p = card(1200, 420, RED)
paste_logo(img, coin_grey, p + 60, p + 70, 280)
d.text((p + 390, p + 95), "Payment declined.", font=F(78, True), fill=WHITE)
d.text((p + 390, p + 210), "Not enough funds.", font=F(58), fill=RED + (255,))
img.save(OUT + "card_7_declined.png")

# 2 loan request
img, d, p = card(1300, 860, GREEN)
paste_logo(img, coin, p + 60, p + 60, 170)
d.text((p + 260, p + 70), "Reputation-backed", font=F(58, True), fill=WHITE)
d.text((p + 260, p + 140), "loan request", font=F(58, True), fill=WHITE)
y = p + 280
d.line([(p + 60, y - 20), (p + 1240, y - 20)], fill=(90, 80, 115), width=3)
rows = [("Work history:", "teaching assistant."),
        ("", "Positive review from the professor and 5 students."),
        ("Nullifier:", "0x18f4...60c5"),
        ("Requested loan:", "2773 zipcoins")]
for k, v in rows:
    if k:
        d.text((p + 60, y), k, font=F(44), fill=SOFT)
        d.text((p + 60 + d.textlength(k + "  ", font=F(44)), y), v, font=F(44, True), fill=WHITE)
    else:
        d.text((p + 60, y), v, font=F(40), fill=WHITE)
    y += 95
# button
bx0, by0, bx1, by1 = p + 440, y + 40, p + 860, y + 150
d.rounded_rectangle((bx0, by0, bx1, by1), 55, fill=GREEN + (255,))
tw = d.textlength("Submit", font=F(54, True))
d.text(((bx0 + bx1) / 2 - tw / 2, by0 + 18), "Submit", font=F(54, True), fill=(30, 40, 35))
img.save(OUT + "card_8_loan_request.png")

# 3 received
img, d, p = card(900, 360, GREEN)
paste_logo(img, coin, p + 60, p + 50, 260)
d.text((p + 370, p + 70), "+2773 zc", font=F(96, True), fill=GREEN + (255,))
d.text((p + 375, p + 210), "Loan received", font=F(50), fill=WHITE)
img.save(OUT + "card_8b_received.png")

# 4 success
img, d, p = card(1340, 700, GREEN)
paste_logo(img, coin, p + 60, p + 60, 200)
tick(d, p + 1180, p + 100, 100, GREEN + (255,))
d.text((p + 300, p + 100), "Payment succeeded.", font=F(72, True), fill=WHITE)
y = p + 330
d.line([(p + 60, y - 30), (p + 1280, y - 30)], fill=(90, 80, 115), width=3)
for k, v, b in [("Base", "10.5 zc", False), ("Tax", "1.1 zc", False), ("Total", "11.6 zc", True)]:
    f = F(56, b)
    d.text((p + 80, y), k, font=f, fill=WHITE if b else SOFT)
    tw = d.textlength(v, font=f)
    d.text((p + 1260 - tw, y), v, font=f, fill=GREEN + (255,) if b else WHITE)
    y += 100
img.save(OUT + "card_9_success.png")

print("cards written to", OUT)
