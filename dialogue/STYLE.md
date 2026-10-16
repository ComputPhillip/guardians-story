# Dialogue: format and style guide

Every NPC in Guardians can talk to every other NPC about whatever they are doing. Dialogue is **ambient**: two people who share a place and an activity exchange a few lines, and the player overhears them if they're in earshot. Think of Oblivion's townsfolk chatter and Kenshi's barks, with *Game of Thrones* grit.

The action list is in [`src/actions.json`](src/actions.json): every activity on the Living World Map, every world event, and every player deed.

## Files

One JSON file per category in `dialogue/`. Each file is a list of **sets**:

```json
{
  "action": "Gossip",
  "kind": "activity",
  "who": "any two townsfolk in company",
  "exchanges": [
    {
      "id": "gossip_01",
      "when": { "state": ["Lean", "Starving"], "time": "evening", "place": "inn", "news": null, "standing": null, "hold": null },
      "lines": [
        { "speaker": "A", "text": "Grain's up again. {steward} says it's the roads." },
        { "speaker": "B", "text": "Roads. It's the Crows, and he knows it." }
      ]
    }
  ]
}
```

* `kind`: `activity` (from the daily plan), `event` (world news being discussed), or `deed` (people reacting to something the player did).
* `who`: the pair or group who speak it, for example "two farm servants", "a priest and a monk", "a guard and the player's witness".
* `exchanges`: **at least 3 per action**, 2–4 lines each. Use more exchanges for common actions.
* `when`: conditions. Leave a field `null` when it doesn't matter. At least one exchange per action must have all `null` conditions, as a fallback.
  * `state`: the town's state: `Starving`, `Lean`, `Fed` or `Thriving`.
  * `time`: `dawn`, `day`, `evening` or `night`.
  * `place`: `home`, `inn`, `market`, `temple`, `keep`, `field`, `wild`, `road`, `camp` or `workshop`.
  * `news`: an event kind from `actions.json` that the speakers have **heard**.
  * `standing`: the speakers' view of the player: `Hunted`, `Shunned`, `Distrusted`, `Neutral`, `Friend`, `Champion`, `Titled` or `Councillor`. Use this for deed reactions.
  * `hold`: one of the five holds, for local colour.
* `speaker`: `A`, `B` or `C`. For creature activities, the speakers are people who **see** the creatures.

## Placeholders

Only these. The game fills them from the simulation.

| Placeholder | Filled with |
|---|---|
| `{A}`, `{B}` | The speakers' first names |
| `{town}` | The speakers' town |
| `{lord}` | The town's lord, for example "Sir Robert" |
| `{lady}`, `{steward}` | The lady and the steward |
| `{hamlet}` | A hamlet of the town (from the event, if any) |
| `{band}` | An outlaw band (from the event, if any) |
| `{calamity}` | A calamity's generated name, for example "Zorulesh, Who Drinks the Wells" |
| `{guild}` | The town's guild tavern, for example "Riftgate" |
| `{good}` | A trade good |
| `{player}` | What the speakers call the player: a name if they know it, otherwise "that stranger" |
| `{dead}` | The name of someone who died (from the event) |

## Voice

* **Grounded and medieval, not archaic.** No "thee" or "forsooth". Plain, short, salty speech. People complain, joke, lie, flirt and grieve.
* **Lines are short:** under 20 words each, so they read as barks.
* **People only know what they've heard.** News lines need a `news` condition.
* **Every class sounds different.** Lords are measured and threatening. Clergy are pious or tired. Outlaws are coarse and loyal. Farmers are practical. Scholars are pedantic.
* **The world leaks through.** Mention the canon: the Blight, the Crows, the lords' hunts, the Half Law, the Forest Charter, the beacons, the Hearth-Moot, taxes, prices and the empty throne.
* **Hold colour:** First Hearth is proud and royal, Canopy Rest pious and woody, Reedwatch poor and wry, Sunward rich and mercantile, Stonepass clannish and hard.
* No modern idiom, no profanity stronger than "bloody", "piss" or "arse", and no slurs.

## Canon to draw on

Read `story/` for names and facts, especially:
* `02-houses-and-factions.md`: the lords, the guilds and the bands
* `03-world-threads.md`: what is happening in the world
* `10-book-of-the-realm.md`: the people, places and hamlets
* `11-hunting-lodges.md`: the lodges, the Half Law and the Forest Charter
