# 12. Dialogue: How NPCs Talk to Each Other

Every NPC can talk to every other NPC about **everything they can do, everything that can happen, and everything the player can do**. The dialogue data is in [`dialogue/`](../dialogue/), and its format and voice are in [`dialogue/STYLE.md`](../dialogue/STYLE.md).

## What is covered

| Kind | Source | Count | File |
|---|---|---|---|
| **Activities** | Every activity verb in the Living World Map's daily plans: sleeping, meals, chores, worship, company, every trade, every guard and outlaw task, the lord's hunt, alarms, and creatures seen by people | 323 | `home-and-rest.json`, `worship-and-company.json`, `market-and-road.json`, `work-1.json`, `work-2.json`, `work-3.json` |
| **World events** | Every kind of news the simulation writes: raids, leaks, calamities rising, deaths, promotions, shortages, hero raids, camp moves and more | 48 | `events.json` |
| **Player deeds** | Every deed the map lets the player do, from giving grain to burning a granary or dealing with slavers | 40 | `player-deeds.json` |

## When two NPCs talk

The map already puts people in the same place doing the same thing: a shared table, a workplace, a market stall, a pew, an inn bench, a camp fire. The dialogue system runs on top of that.

1. **Trigger.** Two or more named people share a place (the map's `locs`) and the player is within **earshot**, about 12 m, or one room indoors. Only bodies near the player exist, as on the map, so dialogue only ever plays where someone can hear it.
2. **Pick a topic.** In order of priority:
   1. **A player deed they've heard about** (`deed`). People talk about the player most when the player is standing right there.
   2. **Fresh news they've heard** (`event`). Word of mouth decides who knows what: a person only knows news the map's Word tab has carried to them.
   3. **What they're doing** (`activity`). This is the shared verb, for example both on `Harrow`, or one on `Serve` and one on `Drink`.
3. **Pick an exchange.** From the chosen set, keep exchanges whose `when` conditions all match, then prefer the one with the **most** matching non-null conditions. The town's state, the time of day, the place, the hold, the speakers' standing toward the player and the news they know are all read from the simulation. If nothing matches, the all-null fallback plays.
4. **Fill and play.** Placeholders are filled from the simulation: `{lord}` from the keep household, `{band}` and `{hamlet}` from the event, `{calamity}` from the generated name, `{player}` from whether these two have met the player. Speaker A is the one who started the activity first, or at random.

## Rules that keep it believable

* **No repeats.** The same exchange doesn't play twice for the same pair within a week, or twice anywhere in earshot within a day.
* **Cooldown.** A pair talks at most once per 30 in-game minutes, and a crowd (8+ people, the map's "shared beats") plays one exchange at a time.
* **Silence is allowed.** Only about 1 in 3 eligible meetings produces dialogue. People mostly just work.
* **Heard, not known.** News lines need the `news` condition, so an NPC can only discuss what the word-of-mouth system has actually told them. A rumour can arrive late, or wrong: the event and deed files include exaggerated versions on purpose.
* **Overheard dialogue spreads news.** When the player overhears an exchange with a `news` condition, the player hears that news too, the same as being told at a table.
* **Class voice.** A lord, a farm servant, an outlaw and a monk never sound alike. See STYLE.md.
* **Sleep and night.** Sleepers neither tell nor hear news (as on the map), but bedfellows murmur, and campmates on watch talk low.

## Creatures

Animals and Blight creatures don't speak. Their activity verbs (Browse, Graze, Root, Prowl, Swarm, Dominate, Ravage and so on) have dialogue spoken by the **people who see them**: shepherds, wardens, hunters, scouts and outlaws on watch. Blight lines are short and dread-filled, and can name the calamity.

## Testing

`dialogue/validate.py` checks that every action, event and deed in `dialogue/src/actions.json` has a set, that each set has enough exchanges and a fallback, that only the allowed placeholders are used, and that exchange ids are unique.
