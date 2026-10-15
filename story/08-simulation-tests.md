# 8. Story Tests on the Living World Map

**Map tested:** `Stewards_Living_World_Map.html` (current version, 15 October 2026)
**How:** headless Chromium, the map's own 364-day world run, with player deeds injected through the map's `window.__acts` hook. The scripts are in [`tests/map-sim/`](../tests/map-sim/). The map ran with **0 page errors** in all four runs.

## The four runs

| Run | What the player does |
|---|---|
| **Baseline** | Nothing: there is no player in the world |
| **Guardian** | Clears a lair every 3 days, kills outlaws every 6 days and retakes a lost hamlet every 9 days, rotating through the five towns |
| **Outlaw** | Joins the Grey Crows every week, steals 300 coin from a town every week, and burns Reedwatch's granary (day 30) and First Hearth's (day 120) |
| **Redeemed** | Lives as the Outlaw until day 90, then works off the bounty in Reedwatch every week, tries to atone on day 200, and lives as the Guardian from day 120 |

## Results

| Measure | Baseline | Guardian | Outlaw | Redeemed |
|---|---|---|---|---|
| Blight leaks | 415 | 364 | 396 | 369 |
| Hamlets overrun by Blight | 35 | 35 | 36 | 36 |
| Hamlets abandoned | 44 | 56 | 42 | 40 |
| Outlaw raids | 274 | 264 | 267 | 232 |
| Lords' heroes breaking camps | 44 | 23 | 52 | 36 |
| **Calamities risen and named** | 21 | 13 | 17 | 23 |
| Cataclysm slain | 1 (a rift, day 290) | 0 | 0 | 0 |
| Guild deaths | 183 | 183 | 198 | 189 |
| Player titles | none | **all 5 by day 42** | none | 5, by days 217–231 |
| Player standing (end) | Neutral | Councillor everywhere | Hunted everywhere | Councillor everywhere |
| Reedwatch days Lean or Starving | **0** | 0 | **332** | **332** |

## What the story learned (and changed)

| Story assumption | What the map does | Change made to the story |
|---|---|---|
| A calamity rises around day 60 and is a rare event | **The first calamity is named on day 87** (*Zorulesh, Who Drinks the Wells*), then one rises every 2–3 weeks, 21 in a year. Most rise in the **Broken March forts**. | Calamities are now a **recurring threat with names** (see the bestiary in [03-world-threads.md](03-world-threads.md)), and the first rising is set to day ~87. |
| Drakrevor is the only cataclysm | The map has **three cataclysms**. In the baseline year the one in a Blighted rift is slain on day 290, and the lords' expedition thins the Heart by 50% on day 182. | Added the **two lesser cataclysms** and the **lords' expedition** to the Demon King thread. |
| Reedwatch is poor and failing | Reedwatch is **Thriving for 306 of 364 days**. It starves only when someone burns its granary, and then it stays Lean or Starving for the rest of the year. | Reedwatch is now a hold that is *doing well, and is easy to ruin*. **Harlan's bid for Reedwatch** now needs Reedwatch Starving, which in practice means a burned granary (by the player, or by Harlan's own arsonist). |
| The Grey Crows grow past 30 and threaten Reedwatch | Every band is broken by a **lord's hero when it reaches about 30 men** (44 times in a year). Broken camps **re-form at 25 men each season**. Even with the player joining every week, the Crows peaked at 34 and then fell. | The outlaw thread is now a **cycle**: bands grow, a hero breaks them, they drift back. A band only wins if its lord's heroes are dead or busy, which is a new story lever. |
| First Hearth secretly pays the Iron Reavers | The **Iron Reavers are the most dangerous band**: they twice occupy Stonepass hamlets (days 24 and 66), and **First Hearth's hero breaks them 7 times**. | A sharper twist: Sir Robert pays the Reavers to bleed Stonepass, then sends his own hero to break them whenever they grow strong enough to be a threat to him. |
| (not in the story) | **The slavers' holds of the north** (36 men) raid hamlets, take people and sell them back for ransom. **The tower school by Mereworth** trains battle mages, healers and alchemists (116 graduates a year). **Hunting lodges** in every town. | Added to [02-houses-and-factions.md](02-houses-and-factions.md) and the life paths. |

## Design findings for the map (not story)

These are issues in the simulation itself, worth raising with the map's owner:

1. **Titles come too fast, and everywhere at once.** The Guardian was titled in all five towns on day 42 and ended at about +810 standing in every town (the Councillor tier is 200). Deeds done in one town raised standing in all five almost equally. This works against the "reputation travels by word of mouth" rule. *Suggestion:* scale cross-town standing by whether the news has reached the town, and cap it.
2. **Councillor with an unpaid bounty.** The Redeemed run ended as Councillor in every town while still owing bounties (480 coin in Reedwatch), and atonement was refused on day 200 because of that bounty. *Suggestion:* block titles and seats while a bounty stands.
3. **"Hunted" by the towns but never by the guilds.** The Outlaw reached Hunted in every town and stole 15,600 coin, but no guild contract was ever posted (`hunted player` fired 0 times). The guild hunt only checks guild standing, which theft and arson don't touch.
4. **One granary fire starves a town for the rest of the year.** After the day-30 burning, Reedwatch was Lean or Starving for 332 days. That is dramatic, and probably too permanent.
5. **The Guardian ended with more abandoned hamlets than the baseline** (56 against 44), despite retaking 40. Retaken hamlets seem to go back into the three-strikes count straight away.
6. **Text glitches in event messages:** "the **The** Broken March", "Grey Crows camp **camp**", "the **the** heart of the blight", "grows by **a** 10%", and "raises **them** to hero" for a named person.

## Running the tests again

```bash
cd tests/map-sim
NODE_PATH=$(npm root -g) node run.js /path/to/Stewards_Living_World_Map.html ""            base.json
NODE_PATH=$(npm root -g) node run.js /path/to/Stewards_Living_World_Map.html guardian.json out_guardian.json
```

A scenario file is a list of deeds such as `{"day":30,"kind":"burn","town":2}`. The deed kinds come from the map, for example `clear`, `camp`, `retake`, `coin`, `burn`, `serve`, `atone`, `give`, `buy`, `sell` and `recruit`.
