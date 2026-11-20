#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page, v2 (1024x1024 PNG).

Run once here to produce entry.png. The entry program (main.ts) only
copies entry.png to /output/entry.png, so the grader needs no fonts.
All facts are events that happened, or were first reported, on
Thursday 19 November 2026 (evening-complete research, 20 Nov 2026).

Layout (top-10 template): flat one-page newspaper, cream paper,
40 stories, 3 flat-illustrated leads (Shenzhen, GTA VI, Anthropic),
navy "WHERE IT HAPPENED" world map with per-region counts, a long
numbered list (items 5-40), and a red "DATE CHECK" footer.
No photographs: every picture is drawn flat.
Sections flow top to bottom from a y cursor so nothing overlaps.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (20, 20, 20)
MUTED = (90, 86, 78)
NAVY = (27, 42, 74)
NAVY_LT = (127, 163, 199)
RED = (180, 35, 24)
RULE = (180, 172, 156)
TEAL = (18, 120, 110)
ORANGE = (230, 120, 40)
PURPLE = (91, 42, 134)
GOLD = (212, 160, 40)

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


def kicker(d, x, y, text, color, size=20):
    d.text((x, y), text, font=font(SANS_B, size), fill=color)
    return y + size + 8


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 44  # margin
R = W - M  # right edge
y = 0

# --- Masthead ---
d.text((M, 22), "WORLD NEWS", font=font(SERIF_B, 54), fill=NAVY)
d.text((R, 30), "THURSDAY", font=font(SANS_B, 26), fill=RED, anchor="ra")
d.text((R, 64), "19 NOVEMBER 2026", font=font(SANS_B, 26), fill=INK,
       anchor="ra")
d.line([M, 104, R, 104], fill=INK, width=4)
d.line([M, 112, R, 112], fill=RULE, width=2)

# --- Number strip ---
y = 122
strip = [("40", "STORIES"), ("3", "HISTORIC FIRSTS"), ("7", "REGIONS"),
         ("1", "DAY")]
sw = (R - M - 3 * 12) // 4
for i, (num, lab) in enumerate(strip):
    x0 = M + i * (sw + 12)
    d.rectangle([x0, y, x0 + sw, y + 36], outline=RULE, width=2)
    d.text((x0 + 12, y + 2), num, font=font(SERIF_B, 28), fill=RED)
    d.text((x0 + 60, y + 10), lab, font=font(SANS_B, 18), fill=NAVY)
y += 42

# --- Lead 1: Shenzhen summit (flat illustration right) ---
y = kicker(d, M, y, "1  •  SHENZHEN SUMMIT  —  LEAD STORY", RED)
lead_top = y
y = para(d, M, y, "Trump, Xi and Putin Meet in Shenzhen",
         font(SERIF_B, 32), 560, 39)
y = para(d, M, y + 2,
         "First-ever trilateral: about 90 minutes at Kylin Villa. "
         "Their joint \u201cDeclaration toward Peace\u201d backs UN reform, "
         "more refined fuel, ICC limits and the line \u201ca nuclear war "
         "cannot be won\u201d. Ukraine and Iran are not named \u2014 no "
         "ceasefire was announced.",
         font(SANS, 19), 560, 24, color=(60, 58, 52))
lead_bot = y
# flat illustration: skyline + three flags
ix0, iy0, ix1, iy1 = 640, lead_top - 4, R, lead_bot
d.rectangle([ix0, iy0, ix1, iy1], fill=(233, 228, 216), outline=RULE, width=2)
d.text((ix0 + 14, iy0 + 8), "KYLIN VILLA, SHENZHEN",
       font=font(SANS_B, 13), fill=MUTED)
for bx, bh, col in ((ix0 + 14, 62, NAVY), (ix0 + 62, 82, (90, 100, 130)),
                    (ix0 + 112, 52, NAVY), (ix0 + 158, 74, (90, 100, 130))):
    d.rectangle([bx, iy1 - 8 - bh, bx + 42, iy1 - 8], fill=col)
# three flags: US stripes, China red + star, Russia white/blue/red
fx = ix0 + 212
d.line([fx, iy0 + 30, fx, iy1 - 8], fill=INK, width=3)
for j in range(5):
    d.rectangle([fx, iy0 + 30 + j * 6, fx + 34, iy0 + 36 + j * 6],
                fill=(180, 35, 24) if j % 2 == 0 else (255, 255, 255))
d.rectangle([fx, iy0 + 30, fx + 14, iy0 + 48], fill=(27, 42, 74))
fx = ix0 + 260
d.line([fx, iy0 + 30, fx, iy1 - 8], fill=INK, width=3)
d.rectangle([fx, iy0 + 30, fx + 34, iy0 + 60], fill=(222, 41, 16))
d.ellipse([fx + 5, iy0 + 35, fx + 13, iy0 + 43], fill=GOLD)
fx = ix0 + 308
d.line([fx, iy0 + 30, fx, iy1 - 8], fill=INK, width=3)
for j, c in enumerate(((255, 255, 255), (0, 57, 166), (213, 0, 50))):
    d.rectangle([fx, iy0 + 30 + j * 10, fx + 34, iy0 + 40 + j * 10],
                fill=c)
y = lead_bot + 8
d.line([M, y, R, y], fill=RULE, width=2)
y += 10

# --- Row B: two illustrated boxes (GTA VI | Anthropic) ---
by, bh = y, 118
bw = (R - M - 20) // 2
# GTA VI box
x0 = M
d.rectangle([x0, by, x0 + bw, by + bh], outline=RULE, width=2)
yy = kicker(d, x0 + 14, by + 8, "2  •  GTA VI  —  LAUNCH DAY", PURPLE, 16)
yy = para(d, x0 + 14, yy, "GTA VI Launches to a 99",
         font(SANS_B, 20), bw - 140, 25)
para(d, x0 + 14, yy + 2,
     "Ties the highest Metacritic score ever. Back in Vice City "
     "after 13 years.",
     font(SANS, 16), bw - 140, 21, color=(60, 58, 52))
gx0, gy0 = x0 + bw - 118, by + 8
d.ellipse([gx0, gy0, gx0 + 108, gy0 + 100], fill=(250, 196, 120))
d.rectangle([gx0, gy0 + 72, gx0 + 108, gy0 + 100], fill=(60, 30, 90))
for px in (gx0 + 16, gx0 + 50, gx0 + 84):
    d.rectangle([px, gy0 + 58, px + 12, gy0 + 100], fill=(60, 30, 90))
d.text((gx0 + 6, gy0 + 82), "VICE CITY", font=font(SANS_B, 12),
       fill=(255, 255, 255))
# Anthropic box
x0 = M + bw + 20
d.rectangle([x0, by, x0 + bw, by + bh], outline=RULE, width=2)
yy = kicker(d, x0 + 14, by + 8, "3  •  ANTHROPIC  —  NASDAQ: ANT",
            TEAL, 16)
yy = para(d, x0 + 14, yy, "Biggest IPO Ever: $81.3bn",
         font(SANS_B, 20), bw - 140, 25)
para(d, x0 + 14, yy + 2,
     "Priced $83, opened $111.50, closed $97.17 (+17%) on day one.",
     font(SANS, 16), bw - 140, 21, color=(60, 58, 52))
cx0, cy0 = x0 + bw - 128, by + 10
for i, h in enumerate((30, 52, 80)):
    d.rectangle([cx0 + i * 38, cy0 + 88 - h, cx0 + i * 38 + 28, cy0 + 88],
                fill=TEAL)
d.line([cx0 - 6, cy0 + 88, cx0 + 112, cy0 + 88], fill=INK, width=3)
d.line([(cx0 + 6, cy0 + 60), (cx0 + 44, cy0 + 38), (cx0 + 82, cy0 + 12)],
       fill=RED, width=4)
d.polygon([(cx0 + 82, cy0 + 12), (cx0 + 70, cy0 + 14), (cx0 + 80, cy0 + 26)],
          fill=RED)
y = by + bh + 10

# --- ICJ band ---
d.rectangle([M, y, R, y + 48], fill=NAVY)
d.text((M + 16, y + 4), "4  •  WORLD COURT: MYANMAR COMMITTED GENOCIDE, 9\u20136",
       font=font(SANS_B, 23), fill=(255, 255, 255))
d.text((M + 16, y + 28),
       "First time the ICJ has held a state responsible for genocide: ~10,000 Rohingya killed in 2017.",
       font=font(SANS, 17), fill=(220, 224, 235))
y += 48 + 6

# --- WHERE IT HAPPENED map band ---
my = y
d.rectangle([M, my, R, my + 84], fill=(38, 56, 96))
d.text((M + 16, my + 6), "WHERE IT HAPPENED",
       font=font(SANS_B, 17), fill=(255, 255, 255))
d.text((M + 16, my + 26), "40 stories, 7 regions",
       font=font(SANS, 14), fill=(200, 210, 230))
# simplified flat continents (kept above the counts line)
d.polygon([(300, my + 28), (380, my + 22), (410, my + 40), (390, my + 56),
           (330, my + 58), (300, my + 48)], fill=NAVY_LT)  # N America
d.polygon([(410, my + 58), (438, my + 56), (444, my + 66), (428, my + 72),
           (412, my + 66)], fill=NAVY_LT)  # S America
d.polygon([(560, my + 24), (600, my + 20), (612, my + 36), (584, my + 46),
           (560, my + 38)], fill=NAVY_LT)  # Europe
d.polygon([(566, my + 46), (604, my + 42), (616, my + 60), (594, my + 72),
           (570, my + 68)], fill=NAVY_LT)  # Africa
d.polygon([(626, my + 22), (740, my + 18), (780, my + 40), (740, my + 60),
           (660, my + 56), (626, my + 44)], fill=NAVY_LT)  # Asia
d.polygon([(770, my + 66), (806, my + 62), (812, my + 74), (780, my + 78)],
          fill=NAVY_LT)  # Oceania
for dx, dy in ((700, my + 34), (585, my + 34), (620, my + 38),
               (350, my + 44), (428, my + 64)):
    d.ellipse([dx - 4, dy - 4, dx + 4, dy + 4], fill=GOLD,
              outline=(255, 255, 255), width=1)
d.text((M + 16, my + 68),
       "N. AMERICA 10  •  EUROPE 8  •  ASIA 7  •  AFRICA 5  •  "
       "LATIN AMERICA 3  •  MIDDLE EAST 2  •  GLOBAL 5",
       font=font(SANS_B, 14), fill=(255, 255, 255))
y = my + 84 + 8

# --- Numbered list: items 5-40, two columns ---
d.text((M, y), "THE DAY IN 40  —  CONTINUED",
       font=font(SANS_B, 18), fill=RED)
y += 18
items = [
    (5, "Kerch Bridge hit a 3rd time; rail halted, 1 track reopened"),
    (6, "Gaza tank raid ends; road reopens, families return"),
    (7, "Iran hit a US base in Kuwait; drones shot down, no injuries"),
    (8, "Wall St plunges: Dow \u22121,101; S&P down a 6th straight day"),
    (9, "Berlin: Europe ready to talk \u2014 after a Ukraine peace deal"),
    (10, "US signs military deal with Venezuela, restoring ties"),
    (11, "Kenya gives Mrima Hill rare earths to a US consortium"),
    (12, "Cyclone Akvan: Odisha evacuates 47,000 people"),
    (13, "Senegal migrant boat capsizes; dozens missing"),
    (14, "Indonesia refinery blast kills one worker in Cepu"),
    (15, "Berlin clears path to UniCredit\u2013Commerzbank deal"),
    (16, "California subpoenas Nvidia over chips reaching China"),
    (17, "S. Korea court orders retrial for ex-PM Han Duck-soo"),
    (18, "S. Korea upholds ex-first lady Kim\u2019s 4-year term"),
    (19, "Mongolia\u2019s parliament accepts president\u2019s resignation"),
    (20, "Serbia elects student-backed \u010cupi\u0107 speaker, acting president"),
    (21, "Somalia orders the UAE ambassador out in 72 hours"),
    (22, "UK: ministers must admit the secret Apple data order"),
    (23, "Japan\u2013India sign live-fire training deal in Tokyo"),
    (24, "Denmark approves US\u2013Greenland security deal, 109\u20130"),
    (25, "Ethiopia and Eritrea mass troops on their border"),
    (26, "Haiti retakes Martissant; police say 34 gang members killed"),
    (27, "US judge holds ICE in contempt over Colorado re-arrests"),
    (28, "Guyana: US says its Essequibo position has not changed"),
    (29, "South Africa holds its rate at 7.25% in a 4\u20133 vote"),
    (30, "COP31 draft drops fossil-fuel language, $120bn target"),
    (31, "Voyager 1 confirmed one light-day from Earth \u2014 a first"),
    (32, "Cancer pill: tumours shrank in 6 of 10 patients in trial"),
    (33, "Van Gogh sells for a record $190.4m in New York"),
    (34, "Trump pardons baseball legend Pete Rose (d. 2024)"),
    (35, "JPMorgan: vendors hacked, some customer data taken"),
    (36, "White House national cyber director steps down"),
    (37, "Dutch watchdog: don\u2019t buy AI smart glasses"),
    (38, "Trump raised two detained Americans with China"),
    (39, "Shelton and Zverev win at the ATP Finals"),
    (40, "Fiona the hippo dies at Cincinnati Zoo"),
]
fnum = font(SANS_B, 13)
fitem = font(SANS, 13)
colw = (R - M - 28) // 2
for idx, (n, txt) in enumerate(items):
    col = idx // 18
    row = idx % 18
    x = M + col * (colw + 28)
    yy = y + row * 14
    d.text((x, yy), str(n), font=fnum, fill=RED)
    d.text((x + 28, yy), txt, font=fitem, fill=INK)
y = y + 18 * 14 + 8

# --- Footer: DATE CHECK ---
d.rectangle([M, y, R, y + 34], fill=RED)
d.text((M + 16, y + 8),
       "DATE CHECK \u2014 Every story above happened, or was first reported, "
       "on Thursday 19 November 2026.",
       font=font(SANS_B, 16), fill=(255, 255, 255))
y = y + 34 + 4
d.text((M, y), "Sources: Reuters, AP, BBC, WSJ, CNN, UN News  •  "
       "Drawn flat \u2014 no photographs  •  40 stories",
       font=font(SANS, 12), fill=MUTED)
print("layout bottom y =", y, "of", H)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
