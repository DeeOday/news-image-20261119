#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page (1024x1024 PNG).

Run once here to produce entry.png. The entry program (main.ts) only
copies entry.png to /output/entry.png, so the grader needs no fonts.
All facts are the events reported on Thursday 19 November 2026.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (20, 20, 20)
MUTED = (90, 86, 78)
NAVY = (27, 42, 74)
RED = (180, 35, 24)
RULE = (180, 172, 156)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, text, f, max_w, leading, color=INK):
    for line in wrap(d, text, f, max_w):
        d.text((x, y), line, font=f, fill=color)
        y += leading
    return y


def kicker(d, x, y, text, color):
    f = font(SANS_B, 21)
    d.text((x, y), text, font=f, fill=color)
    return y + 30


def icon_bridge(d, cx, cy, s, color):
    d.arc([cx - s, cy - s // 2, cx + s, cy + s], 0, 180, fill=color, width=5)
    d.line([cx - s, cy + s // 2, cx + s, cy + s // 2], fill=color, width=5)
    for dx in (-s // 2, 0, s // 2):
        d.line([cx + dx, cy - s // 4, cx + dx, cy + s // 2], fill=color, width=4)


def icon_cross(d, cx, cy, s, color):
    d.line([cx - s, cy, cx + s, cy], fill=color, width=5)
    d.line([cx - s // 2, cy - s, cx + s // 2, cy - s], fill=color, width=5)
    d.polygon([(cx + s // 4, cy - s), (cx + s, cy - s // 4),
               (cx + s // 4, cy + s // 2)], fill=color)
    d.line([cx - s // 2, cy + s // 2, cx - s // 2, cy - s // 2],
           fill=color, width=5)


def icon_scales(d, cx, cy, s, color):
    d.line([cx, cy - s, cx, cy + s], fill=color, width=5)
    d.line([cx - s, cy - s // 2, cx + s, cy - s // 2], fill=color, width=5)
    d.arc([cx - s, cy - s // 2, cx - s // 3, cy + s // 3], 180, 360,
          fill=color, width=4)
    d.arc([cx + s // 3, cy - s // 2, cx + s, cy + s // 3], 180, 360,
          fill=color, width=4)
    d.line([cx - s // 4, cy + s, cx + s // 4, cy + s], fill=color, width=5)


def icon_chart(d, cx, cy, s, color):
    d.line([cx - s, cy + s, cx + s, cy + s], fill=color, width=5)
    for i, h in enumerate((s // 3, s // 2, s)):
        x0 = cx - s + 6 + i * (2 * s // 3)
        d.rectangle([x0, cy + s - h, x0 + 14, cy + s], fill=color)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 44  # margin

# --- Masthead ---
d.text((M, 34), "WORLD NEWS", font=font(SERIF_B, 60), fill=NAVY)
d.text((W - M, 44), "THURSDAY", font=font(SANS_B, 30), fill=RED, anchor="ra")
d.text((W - M, 82), "19 NOVEMBER 2026", font=font(SANS_B, 30), fill=INK, anchor="ra")
d.line([M, 128, W - M, 128], fill=INK, width=4)
d.line([M, 136, W - M, 136], fill=RULE, width=2)

# --- Lead story ---
y = 158
y = kicker(d, M, y, "SHENZHEN SUMMIT  •  LEAD STORY", RED)
y = para(d, M, y, "Trump, Xi and Putin Meet in Shenzhen Today",
         font(SERIF_B, 40), W - 2 * M, 48)
y = para(d, M, y + 6,
         "The three leaders hold their first trilateral talks, with the "
         "wars in Ukraine and Iran, trade, AI and nuclear arms on the agenda.",
         font(SANS, 24), W - 2 * M, 32, color=(60, 58, 52))
d.line([M, y + 14, W - M, y + 14], fill=RULE, width=2)

# --- 2x2 grid ---
cells = [
    ("UKRAINE", NAVY, "Kerch Bridge Hit a Third Time",
     "Ukraine strikes the bridge again overnight, hitting "
     "its rail section. Traffic is halted.", icon_bridge),
    ("GAZA", (150, 60, 20), "Israeli Tanks Cross Gaza's Yellow Line",
     "First ground advance past the line since the October 2025 "
     "ceasefire. Hamas calls it a breach.", icon_cross),
    ("WORLD COURT", (30, 91, 62), "Rohingya Genocide Verdict Today",
     "The ICJ in The Hague delivers its judgment on whether "
     "Myanmar's 2017 crackdown was genocide.", icon_scales),
    ("BUSINESS", (91, 42, 134), "Anthropic Lists on Nasdaq Today",
     "The Claude maker debuts as ANT after pricing its IPO "
     "at $83 a share, above its $70\u201378 range.", icon_chart),
]
gx, gy = M, y + 34
cw, ch = (W - 2 * M - 28) // 2, 218
for i, (kick, col, head, body, icon) in enumerate(cells):
    cx = gx + (i % 2) * (cw + 28)
    cy = gy + (i // 2) * (ch + 18)
    d.rectangle([cx, cy, cx + cw, cy + ch], outline=RULE, width=2)
    ix = cx + cw - 52
    icon(d, ix, cy + 46, 26, col)
    yy = kicker(d, cx + 18, cy + 14, kick, col)
    yy = para(d, cx + 18, yy, head, font(SANS_B, 29), cw - 110, 36)
    para(d, cx + 18, yy + 4, body, font(SANS, 21), cw - 36, 28, color=(60, 58, 52))

# --- Bottom strip: GTA VI + Gulf ---
by = gy + 2 * ch + 18 + 18
d.rectangle([M, by, W - M, by + 96], fill=NAVY)
d.text((M + 20, by + 12), "GTA VI LAUNCHES TODAY",
       font=font(SANS_B, 26), fill=(255, 255, 255))
d.text((M + 20, by + 48),
       "Back in Vice City after 13 years; reviewers give it 99 on Metacritic.",
       font=font(SANS, 23), fill=(220, 224, 235))
d.text((M + 20, by + 74),
       "ALSO: Iran hits a US base in Kuwait — first attack there since September.",
       font=font(SANS_B, 20), fill=(150, 190, 255))

# --- Footer ---
d.line([M, H - 44, W - M, H - 44], fill=RULE, width=2)
d.text((M, H - 34), "Thursday, 19 November 2026  •  World news in one image",
       font=font(SANS, 19), fill=MUTED)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
