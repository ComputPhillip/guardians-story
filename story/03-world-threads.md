# 3. World Threads: Stories That Happen Without You

Guardians has **no main story**. Like Kenshi, the player is one person in a world that is already moving. The "story" is three things:

1. **World threads.** These are storylines the world runs by itself on clocks and conditions. They advance, resolve or collapse whether or not the player is involved.
2. **Life paths.** These are the roles and attitudes the player grows into, and how the world reacts to them (see [07-life-paths.md](07-life-paths.md)).
3. **Emergent moments.** These come from the simulation itself: a raid, a death, a rumour reaching the wrong town.

The player can join a thread, profit from it, oppose it, or never hear of it. A player who spends a hundred days hauling ore between Stonepass and Reedwatch should still see the world change around them: a lord dies, a hamlet burns, a calamity is named.

## How a thread works

Each thread is a chain of **beats**. A beat fires when its **condition** is true: a day count, a faction's strength, a town's state, a person alive or dead, or something the player did. Each beat has a **default outcome** that happens if no one intervenes. **Word of mouth** carries every beat, so the player learns of it only when someone who knows tells them.

```
Beat: "Sir Thomas of Reedwatch is murdered"
  Condition: day >= 40 AND Hearth-Moot held AND Sir Thomas alive AND Hollow Knives exist
  Default:   Sir Thomas dies; Dame Alice rules Reedwatch; each house blames another
  Player can change it: warn him (needs standing with Reedwatch), kill the Knives' contract-holder, be his bodyguard
  News starts at: the keep of First Hearth
```

The day numbers below are suggested defaults on the map's 91-day run, and later days continue on a longer run. Every name and number comes from the canon files.

---

## Thread 1: The Waking of the Demon King
*The world's slow clock. It always runs.*

| Beat | Condition (default timing) | Default outcome | How players can push on it |
|---|---|---|---|
| Blight leaks | Any Blighted lair left alone for 3 weeks | A pack overruns the nearest hamlet | Guild parties and players who clear lairs hold it back |
| Magic wakes | Rolling | Common folk are **awakened** (Margaret the Sage, Robert Cordwainer) | Learn why: the leylines are stirring |
| Rifts surge | Day 30+, more as leaks pile up | Dormant rifts turn **surging** | Seal or clear them |
| **Calamities rise** | First around **day 87** (tested), then one every 2–3 weeks, mostly in the Broken March forts | A new calamity rises and **is named**, for example *Zorulesh, Who Drinks the Wells*. Rumours of its name spread. | Kill it, and that one never returns. Another will rise somewhere else. |
| The lords' expedition | Day ~182 (tested) | The lords pool their heroes and march on the Heart, thinning it by half; on day ~273 they march on a calamity lair | Join it, fund it (as a Councillor) or sabotage it |
| A lesser cataclysm falls | Day ~290 (tested) | The cataclysm of a Blighted rift is slain, and nothing of its tier rises there again | Be the one who kills it |
| The beacons go dark | After a calamity rises | The Blight snuffs out watchtower beacons near the March | Relight them (see *Beacon Night*) |
| **Drakrevor wakes** | When the **Waking** meter fills (it fills with leaks, surging rifts and unlit Rim Fires, and drains when lairs are cleared) | The horde marches. Hamlets near the March fall first, then a town. | The Rim Fires (Thread 4) slow it; reaching the Heart (L90) ends it |

The Waking meter is the closest thing the game has to a "main quest". It is never forced on the player; the world just gets worse if no one deals with it.

## Thread 2: The Empty Throne
*The politics of the five holds.*

| Beat | Condition | Default outcome | Player hooks |
|---|---|---|---|
| Sir Robert's claim | Day ~10 | Sir Robert of First Hearth sends sealed letters to the other lords announcing his claim at the Hearth-Moot | Carry, read, lose or sell the letters |
| The Reaver deal | Ongoing | First Hearth secretly pays the **Iron Reavers** to bleed Stonepass. The Reavers occupy Stonepass hamlets (tested: days 24 and 66), and whenever they near 30 men, **Sir Robert's own hero breaks them** (7 times a year), so he stays their master. | Expose it to Sir John Ironhand (war) or blackmail Sir Robert |
| **The Hearth-Moot** | Day ~40 | All five lords meet in First Hearth | Attend as a guard, a hero, a servant or an assassin |
| **Murder at the Moot** | At the Moot, if the Hollow Knives' contract stands | **Sir Thomas of Reedwatch** is killed. Each house blames another. | Prevent it, fake it or carry it out |
| The holds arm | After the murder | Garrisons stop escorting carts, prices rise and hamlets go hungry | Sellswords (Grey Company, Red Lances) are in demand |
| **The Grey Wedding** | Day ~60, if Canopy Rest and Stonepass both still stand | Aelis of Canopy Rest weds Gerrit Ironhand in **Ashcut Gorge**. Brother Tamsin breaks Blight-salt at the feast, Horrors come out of the walls and the Reavers strike. Gerrit dies; Aelis may live. | Be a guest, a guard or a Reaver. Expose Tamsin first, and the wedding is just a wedding. |
| **Siege of the Stonepass Wall** | After the Grey Wedding, if Sir Robert lives | First Hearth marches on Stonepass | Fight for either side, or hold the passes for neither |
| The crown | Any lord holds 3 holds' support | A king is crowned, and **Leadership** exists again | The player can be that king (see the *Lord* path) |

If no one takes the throne, the throne stays empty, and that is also a valid world state.

## Thread 3: The Salt Road
*Who is feeding the Blight?*

| Beat | Condition | Default outcome |
|---|---|---|
| Blight-salt appears | Day ~15 | Sunward alchemists start buying grey "salt" reagents. Prices for elixirs fall. |
| The trail | Ongoing | Salt moves from Salt Jackals caches on **Saltcrown Mesa** through **Dame Matilda**'s buyers to **Brother Tamsin** in Canopy Rest |
| Tamsin's rite | At the Grey Wedding, or day ~75 if there is no wedding | Tamsin opens a jar at a crowd, and a Blight bloom follows |
| Tamsin flees | After the rite | He goes into the Heart and speeds up the Waking meter |

Anyone who follows the salt can stop this thread: a trader who notices odd prices, an outlaw who robs a Jackal cache, or a healer working with Sister Hesk.

## Thread 4: The Stewards' Oath
*A thread that only starts if someone goes looking. It never starts on its own.*

| Beat | Trigger | Outcome |
|---|---|---|
| Rook's last words | The player finds **Ser Aldwin Rook** dying on the Riftgate road. This is an encounter that can happen on any early road trip, not a required opening. | The player gets Rook's Blade and the words "Light the fires." |
| The incomplete Oath | Gain standing with Canopy Rest, or break into its Stewards Hall | It points to **the hidden library** |
| The hidden library | Find it | The truth: the Rim Fires plus the beacon line keep the Demon King asleep |
| Sworn Stewards | Swear in three people (companions, NPCs or the player) | A new order is founded, and lords react to it (see the *Steward* path) |
| **The Rim Fires** | Three sworn Stewards light the three Blight Rim lookouts at once | The Waking meter falls sharply. The fires must be relit every season. |

## Thread 5: Outlaw Country
*The bands run on the faction rules: feud, absorb, raid, move.*

| Beat | Condition | Default outcome |
|---|---|---|
| The ford | Days 1–5 | The **Low-Water band** tolls the ford, Brother Roger pleads for help, and the **Grey Company** storms it on day 5 |
| The Red Lances | Days 1–2, unhired | Robert atte Lane's men go unpaid and start squeezing Sunward farmsteads, turning outlaw |
| The outlaw cycle | Any band nears 30 men | **A lord's hero breaks it** (44 times a year in the test), and broken camps **drift back to 25 men each season**. Bands never win on their own. | Kill a lord's heroes, keep them busy elsewhere, or become a hero yourself |
| **Harlan takes Reedwatch** | Reedwatch is **Starving**, and its heroes are dead or away | **Harlan Grey** holds Reedwatch and calls himself its lord. Reedwatch is Thriving most of the year (tested), so Harlan needs an arsonist: **one granary fire leaves it Lean or Starving for months**. |
| The slavers | Ongoing, near Stonepass | **The slavers' holds of the north** raid hamlets and sell the taken back for ransom. Stonepass pays. | Free the captives, pay the ransom, or trade with the slavers (the town shuns you if you do) |
| Bands feud | Overlapping reaches | The winner absorbs the loser's men |

## Thread 6: The Last Spring and the Mages
| Beat | Condition | Default outcome |
|---|---|---|
| The water toll | Day 1 | **Juliana the Warlock** tolls the last spring, and Sunward's water costs rise |
| The duel | Day 5 | **The Company of the Lantern** beats her, and she is exiled to the warlock's refuge near First Hearth |
| Margaret's tour | Days 2, 4, 6 | **Margaret the Sage** sees the lords of Canopy Rest, First Hearth and Stonepass |
| The conclave | Day 5 | Nine sorcerers meet at each of the five stone circles |
| A council of mages | Day ~50, if Margaret lives | The mages declare themselves a power. Lords demand their mages swear to them or leave. |

---

## Named calamities (from the map's generator)

The map gives each calamity a generated name and epithet. These are the ones that rose in the year-long test, and the story treats them as **legends that grow with every telling**:

| Epithet | Example names | Lore |
|---|---|---|
| *Who Drinks the Wells* | Zorulesh, Vhaeshnyr, Raxeshsha, Vhavhaul | Sours wells for miles, the classic Blight sign |
| *the Ember Crown* | Vhathemor, Vorvhavha, Ithdraith | Burns in ash-light; the closest thing to a fire-demon |
| *the Glass Serpent* | Golmordra, Golthemor | Leaves the ground glassy behind it |
| *the Hollow* | Ulkalvor, Ulraxul, Kalkalzor | A husk that wears the dead |
| *the Ashen Tide* | Eshkreith, Krevhamor | Moves with a fog of grey ash |
| *the Thirsting* | Kremorith, Ululthe | Drains the living |
| *the Salt Wyrm* | Thezorvor | Comes out of the Blight-salt flats, linked to the Salt Road |
| *of the Red Sand* | Nyrthemor, Nyreshul | Rises near the desert edge of Sunward |
| *the Unburied* | Vhavormor, Vorgolmor | Barrow-dead raised by the Blight |

## World endings (states, not cutscenes)

There is no final cutscene. A playthrough ends when the player dies (death is permanent) or chooses to retire. Then the game writes an **epilogue** from the world state:

* **The Demon King:** asleep, waking, awake, or slain.
* **The throne:** empty, held by a lord, held by the player, or held by an outlaw.
* **Each hold:** Thriving or Starving, and who rules it.
* **The Stewards:** forgotten, or refounded and by whom.
* **The player:** what they were known as, and in which towns (from word of mouth).
