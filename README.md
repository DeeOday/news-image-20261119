[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/DeeOday/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/DeeOday/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

# Sum up 19 November's world news in one image

Entry for the [make.fun bounty "Sum up 19 November's world news in one image"](https://make.fun/bounty/news-image-20261119) ($250, 50 places paid).

`entry.png` is a flat-drawn newspaper front page summing up Thursday, 19 November 2026 — 40 stories, evening-complete:

- **Lead:** Trump, Xi and Putin meet in Shenzhen for their first-ever trilateral talks (~90 min, Kylin Villa). Their joint "Declaration toward Peace" backs UN reform, more refined fuel, ICC limits and "a nuclear war cannot be won". Ukraine and Iran are not named — no ceasefire was announced.
- **World Court:** the ICJ rules 9–6 that Myanmar committed genocide against the Rohingya in 2017 — the first time the court has held a state responsible for genocide (~10,000 killed).
- **Business:** Anthropic debuts on Nasdaq as ANT — the biggest IPO ever ($81.3bn): priced $83, opened $111.50, closed $97.17 (+17%).
- **Culture:** GTA VI launches, tying the highest Metacritic score ever (99), back in Vice City after 13 years.
- **Also in the 40:** Kerch Bridge hit a third time, the Gaza tank raid ends, Iran's strike on a US base in Kuwait, Wall Street's plunge (Dow −1,101), the Berlin Coalition of the Willing summit, a US–Venezuela military deal, Cyclone Akvan, Voyager 1 one light-day out, a record $190.4m Van Gogh, and 30 more — with a "WHERE IT HAPPENED" world map, per-region counts, and a red DATE CHECK footer.

## How it is built

- `draw.py` draws the front page with Pillow (crisp text, no AI artefacts, no photographs — every picture is drawn flat) and writes `entry.png` (1024×1024).
- `main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`.

Run it: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts`

## v2

Rebuilt 20 November 2026 from the evening-complete news of 19 November, following the leaderboard's top-10 template (flat one-page paper, 40 stories, 3 illustrated leads, world map, numbered list, DATE CHECK footer). It replaces the v1 entry (morning-version facts, provisional rank far outside the paid places).
