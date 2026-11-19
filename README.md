[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/DeeOday/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/DeeOday/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

# Sum up 19 November's world news in one image

Entry for the [make.fun bounty "Sum up 19 November's world news in one image"](https://make.fun/bounty/news-image-20261119) ($250, 50 places paid).

`entry.png` is a newspaper front page summing up Thursday, 19 November 2026:

- **Lead:** Trump, Xi and Putin meet in Shenzhen for their first trilateral talks, with the Ukraine and Iran wars on the agenda
- **Ukraine:** Kerch Bridge hit again overnight, a third attack in a week, hitting its rail section; traffic halted
- **Gaza:** Israeli tanks cross the Yellow Line, the first ground advance since the October 2025 ceasefire; Hamas calls it a breach
- **World Court:** the ICJ rules today on whether Myanmar's 2017 crackdown on the Rohingya was genocide
- **Business:** Anthropic shares debut on Nasdaq as ANT after pricing its IPO at $83 a share, above its $70–$78 range
- **Also:** GTA VI launches today, back in Vice City after 13 years (Metacritic 99); Iran hits a US base in Kuwait, its first attack there since September

## How it is built

- `draw.py` draws the front page with Pillow (crisp text, no AI artefacts) and writes `entry.png` (1024×1024).
- `main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`.

Run it: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts`
