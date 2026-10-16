# 13. The Crimson Desert Port

*Every skill, power and system in Crimson Desert (Pearl Abyss, 2026, including the 2.0 Enhanced Edition), carried into Guardians with a grounded name.*

Crimson Desert is a single-hero action game with a fantasy bracelet that grants flight, time-slowing and elemental powers. Guardians is a squad simulation with no dodge roll, auto-triggered techniques, point-and-click footwork, and low magic that always has a source (steel, faith, arcane study, alchemy or the Blight). So this is a **translation**, not a copy. Every Crimson Desert skill gets one of four verdicts:

| Verdict | Meaning |
|---|---|
| **Existing** | Guardians already has it, under the name in [05-magic-and-combat-lore.md](05-magic-and-combat-lore.md) |
| **New** | Added to Guardians as written, with a grounded name, a teacher and a source |
| **Grounded** | The effect is kept but the fiction is changed to fit the world (a glider becomes a rope and grapnel; a time-slow becomes a stance) |
| **Replaced** | The effect breaks canon (gunpowder, true flight, illusions) and is swapped for the nearest thing the world allows |

All new techniques follow the combat system's rules: they **auto-trigger** on spatial and tactical conditions, they fit the **8-state animation rig**, and the player's skill is **where they stand**.

---

## Part I: Systems

### The three dials

| Crimson Desert | Guardians | Notes |
|---|---|---|
| **Health** | **Blood** | Hit points. Raised at the infirmary and by hard living; the dial the healers care about. |
| **Stamina** | **Wind** | Spent on sprinting, climbing, techniques and holding a stance. "Out of wind" is a medieval phrase. Draughts (`POT-STAM`) restore it. |
| **Spirit** | **Resolve** | Spent on Faith and Arcane casting and on the Measure stance (below). Regained by standing in the Measure, by prayer, and by elixirs. |

Crimson Desert shares Kliff's dial upgrades with Damiane and Oongka. Guardians shares them across the player's **squad**: the hall's barracks, forge and lab raise the whole company's Blood, Wind and Resolve.

### Skill points: Abyss Artifacts become Cores

Crimson Desert pays for every skill with Abyss Artifacts, earned from a kill gauge, bosses, puzzles and vendors. The workbook already gives every Blight creature a **core** drop ("loot value and cores per kill" on the Enemy Types sheet). So:

* **Cores** are the skill currency. They are the hard, grey stones found inside Blight-born, and the realm's trainers want them because the tower school by Mereworth pays for them.
* A technique is **bought from a teacher** for cores: a guild veteran, a lodge hunter, a sergeant, an outlaw captain, a monk. Nobody learns from a menu; they learn from a person, and the person remembers who they taught.
* Cores also come from **calamity kills** (a great many), from the **lords' expedition**, and, for the wealthy, from Sunward's **Blight-salt dealers**, which is how Dame Matilda's trade touches the player.

### Respec: Faded Artifacts become Unlearning

A Faded Abyss Artifact resets the tree. In Guardians the player can **unlearn** a technique by a season at the tower school or a penance at the temple, getting the cores back less a tithe. The dialogue system treats it as news: *"Heard the captain's gone back to school."*

### Watch and Learn becomes Learning by Eye

Crimson Desert lets you learn a skill by watching an enemy or NPC perform it a few times. This is the best fit of anything in the port, because the map already runs every person's day: sergeants drill, heroes spar, outlaws raid, lodge hunters shoot.

* **Learning by Eye.** Watch a technique performed three to five times in earshot and it is learned free, no cores. The map's **word-of-mouth** rule applies: you must have been there.
* Every technique below lists its **teacher**, and that is who you watch.
* The dialogue data's `activity` sets (Drill, Training, Archery, Duel, Raid, Patrol) are where this happens.

### No passive healing

Crimson Desert has no passive health regeneration; you eat. Guardians already works this way: wounds rest at hospices and infirmaries, draughts heal in the fight, and the lodges and kitchens feed the squad. Cooking and alchemy are the healing systems.

### The camp becomes the Hall

Greymane Camp, Crimson Desert's crafting and upgrade hub, is the player's **Hall** (storehouse, barracks, forge, alchemy lab), already in the workbook.

---

## Part II: Stances and the Measure

Crimson Desert's **Focus** slows time, restores Spirit, and powers Focused Insight (auto-parry), Focused Repulsion (shove), Focused Shot (mark and volley) and Focused Palm. Time does not slow in Guardians. Instead Focus becomes a fifth stance beside Hold, Protect, Skirmish and Passive:

| Crimson Desert | Guardians | What it does |
|---|---|---|
| **Focus** | **Measure** (`M`) | The fighter stops attacking and takes the measure of the foe. Parry and block windows double, Resolve regenerates, and the next technique is empowered. Taught by every duellist: *"Take their measure before you take their head."* |
| **Focused Insight** | **Reading the Swing** | In Measure, the fighter turns to face each incoming attack and counters it automatically. |
| **Focused Repulsion** | **Clearing the Press** | In Measure, a shove that pushes everyone within 2 m back (can Wall-Pin). |
| **Serenity** (2.0) | **Steady Breath** | More Resolve regained while in Measure. Taught by the anchorites. |
| **Focused Shot** | **Marking Shots** | An archer in Measure marks up to four targets, then looses at all of them. |
| **Focused Palm** | **Measured Blow** | See the Leyline Palm family below. |

---

## Part III: Kliff's kit

### Armed combat (sword and shield)

Kliff's sword is a one-handed arming sword with a shield, which is the Guardsman's kit. Teachers: sergeants at drill, the lord's heroes, Thomas Fox.

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Armed Combat (base) | **Steel** (the Martial major) | Existing | Levels 1–100 |
| Forward Slash | **Slash** (*Quick Slash*) | Existing | |
| Forward Slash: Sure Hit | **True Cut** | New | The slash tracks a sidestepping foe; cannot miss inside the sweet-spot |
| Turning Slash | **Wheel Cut** | New | A spinning overhead that sends the foe flying 2 m; triggers on a staggered target |
| Turning Slash: Rend Armor | **Rending Cut** | New | Wheel Cut that ignores stagger immunity and shreds 15% armour |
| Stab (charged, bleed) | **Thrust** | New | Charged thrust; bleed; longer charge in Measure |
| Swift Stab | **Quick Thrust** | New | Learned by eye from the fen outlaw called the Reed Devil in Crimson Desert; here from **Agnes atte Green** |
| Aerial Stab | **Falling Thrust** | Grounded | Thrust delivered when dropping from a vault, wall or cart (see Vault) |
| Spinning Slash | **Whirl-Cut** | New | Short leap and spin; hold for consecutive spins (**Whirl-Cut Proficiency**) |
| Shield Bash | **Shield Bash** | Existing | |
| Blinding Flash | **Sun on Steel** | Grounded | Tilt a polished blade or shield into the sun to blind foes in a cone. Day only. The map knows the time of day, so this is a real condition. |
| Blinding Flash Finisher | **Blind Rush** | New | A flurry on a blinded foe |
| Counter | **The Riposte** (*Steward's Riposte*) | Existing | Attack as the foe swings to interrupt |
| Parry | **The Parry** | Existing | Melee parry chance, frontal arc only |
| Dodge / Evasive Roll | **The Steward's Step** | Grounded | No roll. A sidestep that triggers when a telegraph lands, Light and Medium armour only (*Evasive Sidestep* / *Scout's Step*). *"A Steward does not leap. A Steward steps."* |
| Backstep | **Giving Ground** | New | A measured step back out of a dead-zone |
| Keen Senses | **Quick Eye** | New | The passive that unlocks the Step, the Parry and the Riposte at levels 2, 3 and 4 |
| Enraged Parry (2.0) | **Spiteful Parry** | New | A parry at Quick Eye 4 that returns the blow's stagger to the attacker |
| Finishing Rush (2.0) | **Closing Rush** | New | At Steel level 60, a dash-and-cut on a foe under 20% Blood |

### Marksmanship (bow)

Teachers: tower wardens, lodge hunters, the archer at the Lioncrest contest in Crimson Desert becomes the **archery butts** behind every guild tavern.

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Marksmanship (base) | **The Bow** (the Marksmanship major) | Existing | |
| Charged Shot | **Full Draw** | New | Hold for a heavier arrow: +50% damage, +15% armour pen |
| Multishot | **Fan Shot** | New | A spread of five arrows in a 30° fan, best inside 5 m |
| Evasive Shot | **Running Shot** (*Momentum Shot*) | Existing | Shoot while kiting |
| Evasive Shot: Proficiency | **Light Feet** | New | Faster Running Shot |
| Evasive Shot: Expertise | **Two on the Step** | New | Running Shot looses two arrows |
| Explosive Evasive Shot | **Push-Off** (*Point-Blank Repel*) | Replaced | No arrow launches you skyward; the Warden's close shot knocks the foe back instead |
| Focused Shot | **Marking Shots** | Grounded | See the Measure |

### Unarmed combat

Fists are the brawler's art: inns, fairs, lodges and outlaw camps. Teachers: **Robert Thornback**, lodge hunters, the Red Lances.

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Unarmed Combat (base) | **Fists** | New | A Martial sub-skill; cadence 1.6/s, 60% AD, usable when disarmed or in a tavern brawl (no permadeath in a fist-fight) |
| Pump Kick | **The Boot** | New | Front kick, heavy stagger, breaks guard |
| Dropkick | **Two Boots** | New | Leaping two-footed kick; knocks down; Wall-Pins |
| Vault | **Vault** | New | Leap over a low wall, cart, or crouching foe; also the traversal move (see Part V) |
| Flying Kick / Flying Punch | **Leaping Kick** | New | From a vault, two kicks on landing |
| Iron Fists | **Iron Knuckles** | New | Passive: +25% unarmed damage; lodge hunters' and quarrymen's hands |
| Roundhouse Kick | **Wheel Kick** | New | Spinning kick hitting everyone in a 180° arc |
| Tiger's Fury | **Red Fists** | New | Brigand awakening: a flurry of blows that ignores block from the flank |
| Meteor Kick | **Dropping Kick** | Grounded | A diving kick from a vault, wall, roof or saddle; the higher the drop, the harder the hit |

### Wrestling (grappling)

Medieval wrestling was a real sport, and the map already has arm-wrestling at the inn. Teachers: **John Little** of Reedwatch, the Iron Reavers, the Stonepass clans.

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Grappling (base) | **Wrestling** | New | Throws ignore armour and open a follow-up window; a throw into a wall is a Wall-Pin |
| Throw | **The Throw** | New | Hip throw; default |
| Clothesline | **Bar-Arm** | New | Running strike that stuns; chains into Flattening |
| Lariat | **Flattening** | New | Slam the foe into the ground; shockwave staggers foes within 2 m |
| Body Slam | **Dropping Weight** | New | From a vault, land on the foe |
| Giant Swing | **The Swing** | New | Grab mid-kick and hurl; costs Wind per second; throws a foe into others or over a cliff edge |
| Suplex | **Backbreaker** | New | From behind, drive the foe into the ground |
| Chokeslam | **Throat-and-Floor** | New | Lift by the throat and slam; a Brigand's favourite |
| Hammer Throw | **The Hurl** | New | Spin and throw a light foe 4 m |

### The Leyline Palm (Force Palm)

Force Palm is Kliff's one true "power": energy gathered in the palm and released as a strike that lowers defence. In Guardians the **tower school by Mereworth** teaches battle mages a palm strike that carries a charge drawn from the leylines. Low magic, visible as a brief glow, never a beam. Teachers: the school's masters, the Company of the Lantern, Margaret the Sage.

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Force Palm | **Leyline Palm** | Grounded | Unarmed strike, 100% AP magic damage, –15% target defence for 4 s. Needs an Arcane aptitude or an awakening. |
| Force Palm Pulse | **Quick Palm** | Grounded | A faster palm between weapon hits; 20 Resolve |
| Focused Palm | **Measured Blow** | Grounded | From the Measure stance; pierces 40% of resistance; breaks warded doors and walls (the hidden library's seal) |
| Light Falling Palm | **Falling Palm** | Grounded | Downward palm while swinging; staggers |
| Aerial Force Palm | **Dropping Palm** | Grounded | From a vault or height |
| Diving Force Palm / Descending (2.0) | **Driving Palm** | Grounded | Dropping Palm that follows through into the ground; small shockwave |
| Flowing Force Palm (2.0) | **Threefold Palm** | Grounded | Three palms in sequence |
| Ascending Force Palm (2.0) | **Rising Palm** | Grounded | Uppercut palm that lifts a light foe |
| Force Current | **Through the Line** | Grounded | Send the charge down the grapnel line (Part V) into a hooked foe at range |

### Nature's skills

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Nature's Snare (wind wall vs projectiles) | **Wind-Wall** | Grounded | Wanderer: a gust that turns arrows aside for 2 s; or, for the faithful, **Ward** |
| Nature's Grasp (lift objects) | **Heave** | Grounded | Lift and throw crates, barrels, stones and carts; a strength feat, no magic; a thrown barrel Wall-Pins |
| Nature's Echo (phantom copy of your strikes) | **The Feint** | Replaced | No illusions. A Duellist's feint that makes the foe strike where you were, opening the flank. |
| Double Jump | **Vault** | Grounded | See above; an extra leap off a wall or a foe |
| Water Stride (2.0) | **Fen-Walk** (*Fen-Strider's Grace*) | Existing | Running the drowned Steward causeways under the reeds |

---

## Part IV: The Axiom Bracelet

Kliff's bracelet grants a spectral claw, a glider, four elements and the power to imbue weapons. None of that is grounded. Each power becomes a tool, a craft or a simple spell with a source.

### Axiom Force becomes the Grapnel

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Axiom Force (spectral claw) | **The Grapnel** | Grounded | An iron hook on a line, a smith's item (`TOOL-GRAPNEL-T1..T5`). Hook objects, levers, gates and foes. The Reavers use them on carts. |
| Axiom Force: Winch | **Haul In** | Grounded | Yank a hooked foe to you and slam them (the axe's *Bearded Hook* is the one-handed cousin) |
| Axiom Force: Ambush | **Line-Pull** | Grounded | Pull *yourself* to a hooked foe, wall or beam |
| Axiom Force (arcane version) | **The Gathering Dark** (*Cataclysmic Collapse*) | Existing | The Scholar's pull, for those with the gift |

### Flight becomes the Warden's Line

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Flight (glider) | **The Warden's Line** | Grounded | Rope and grapnel descent of any cliff face, the way the tower wardens come down from the beacons. The map's cliffs, mesas and buttes (the Stonepass Wall, Grey Butte, Saltcrown Mesa) become climbable and descendable, costing Wind. Caches and herb patches on the tops are the reward, as on the map. |
| Swift Flight / Enhanced Flight (2.0) | **Fast Rope** | Grounded | Faster descent, less Wind |
| Aerial Roll | **Breakfall** | Grounded | Land from a drop without a wound |

### The four elements

| Crimson Desert | Guardians | Verdict | Source |
|---|---|---|---|
| Flame Strike (fire in a radius around you) | **Hearth-Ring** | New | Arcane, Scholar. A ring of fire at the caster's feet; burns for 3 s. |
| Frost Mantle (immune while draining Spirit) | **Rime Mantle** | New | Arcane, Hermit. A rime shell that absorbs all damage while it drains Resolve fast. Learned at the stone circle in winter. |
| Lightning Surge | **Chain Lightning** | Existing | Wanderer |
| Storm Veil (fog, enemies lose you) | **Fen Mist** | New | Arcane, Wanderer. A fog that breaks line of sight for 5 s; strongest over water. |

### Imbue Element becomes Edge-Oils

Crimson Desert lets you imbue Turning Slash, Charged Shot, Force Palm and Meteor Kick with an element. In Guardians elements on a blade come from **alchemy**, which the workbook already has, and which the Little family of Stonepass dominates.

| Oil | Effect | Brewer | Note |
|---|---|---|---|
| **Fire-oil** | Burning, 3 s | Any alchemist | Coats Wheel Cut, Full Draw, Leyline Palm, Dropping Kick |
| **Rime-salt** | Slow, then a brief freeze on the third hit | Stonepass alchemists | Needs sky-iron filings |
| **Storm-salt** | A shock that stops the foe for 2 s | The tower school | Rare |
| **Grey Salt** | Blight rot: damage over time that spreads to nearby foes, and taints the user's Blood | Brother William's suppliers | **Forbidden.** Using it is a `ruthless` deed, and the Salt Road thread notices. |

A coating lasts one fight. **Imbue Element levels 1–4** become the four oils, each learned from its brewer.

---

## Part V: Traversal

| Crimson Desert | Guardians | Verdict | Notes |
|---|---|---|---|
| Climbing (any cliff, stamina-limited) | **Climbing** | Grounded | Any cliff face, costing Wind; the map's switchbacks are the free route |
| Sprinting | **Sprint** | Existing | Wind |
| Swimming | **Swimming** | New | Fords and the sea-cliff coves; armour weight drowns |
| Double Jump | **Vault** | Grounded | |
| Water Stride | **Fen-Walk** | Existing | |

---

## Part VI: Damiane's kit (rapier and pistol)

Damiane fights with a rapier and a flintlock. Guardians has no gunpowder, so her kit becomes the **Duellist with a bow at the hip**, or a Scout. Her pistol skills go to the Bow.

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Rapier (Armed Combat) | **The Duellist's sword** | Existing | |
| Piercing Light (charged gap-closer) | **The Lunge** | New | Close 3 m and thrust |
| Piercing Light: Uppercut | **Rising Cut** | New | Lunge into a lifting cut |
| Piercing Light: Skewer | **Deep Thrust** | New | Charged thrust, heavy single-target damage (the spear's *Skewer* is the reach version) |
| Piercing Light: Rend Armor | **Rending Cut** | New | Shared with Kliff's |
| Sword Flurry (dodge and strike) | **Step-and-Cut** | New | A Steward's Step that ends in a cut |
| Shield Toss | **Javelin Cast** | Replaced | Shields are not thrown. Spearmen carry two javelins (`SPEAR` sub-item) to cast at 8 m. |
| Spinning Scissors Throw | **Scissor Throw** | New | Wrestling: a leg-scissor trip from a run |
| Scissor Kick | **Scissor Kick** | New | Fists |
| Tornado Kick | **Whirling Kick** | New | Fists; learned by eye from a martial artist in Crimson Desert, here from the **Dervishes** of Sunward |
| Quick Swap | **Second Weapon** | New | Switch sword and bow mid-fight without losing cadence; a Scout's trick |
| Evasive Shot (pistol) | **Running Shot** | Existing | Bow |
| Focused Shot (pistol) | **Marking Shots** | Grounded | Bow, in the Measure |
| Blinding Flash | **Sun on Steel** | Grounded | |
| Evasive Roll | **The Steward's Step** | Grounded | |
| Fists tree (patch 1.07) | **Fists** | New | Shared |

---

## Part VII: Oongka's kit (great axe and arm cannon)

Oongka is the tank: a great axe, sometimes a shield, and in some builds an arm cannon. The axe is the Sellsword's and the Hammer Breaker's ground; the cannon is replaced.

| Crimson Desert | Guardians | Verdict | How it works here |
|---|---|---|---|
| Leaping Smash | **Ground Slam** (*Earthshaker Slam*) and **The Anvil** | Existing | Hammer |
| Charge (shield rush while guarding) | **Shield Rush** | New | Shield: run 5 m behind the shield, knocking foes aside; Wall-Pins |
| Rampage | **The Reaping** (*Reaping Arc*) and **Red Rage** | Existing | Axe |
| Lariat follow-up | **Bar-Arm and Flatten** | New | Wrestling chain |
| Grappling / Giant Swing | **Wrestling / The Swing** | New | Shared |
| Scatter Shot (arm cannon) | **Sand and Spikes** (*Caltrops*) | Replaced | No gunpowder |
| Explosive Strike (arm cannon) | **Fire-Flask** | Replaced | A thrown flask of fire-oil; alchemy, the Littles again |

---

## Part VIII: Horses

Crimson Desert's horses level by trust and learn skills. The map's `mount` deed buys a horse or cart; this makes the horse a character.

| Crimson Desert | Guardians | Verdict | Notes |
|---|---|---|---|
| Horse Taming | **Horse-Breaking** | New | A Hunter/Scout life skill; wild horses in the Heartlands deer parks |
| Trust levels | **Trust** | New | Raised by riding and feeding; a horse that trusts you comes when whistled (*The Whistle*) |
| Dash (Lv 2) | **Burst** | New | Short speed burst |
| Drift (Lv 3) | **Wheel About** | New | Racing turn at speed |
| Back Kick (Lv 3) | **Kick Out** | New | The horse kicks a foe behind; knockdown |
| Sprint (Lv 4) | **Full Gallop** | New | Top speed, drains the horse's Wind |
| Lateral Movement | **Side-Pass** | New | Sidestep in the saddle (the horse's Steward's Step) |
| Swimming I–III | **Ford I–III** | New | Rivers and coves |
| Quick Start / Instant Acceleration | **Off the Mark** / **Spur** | New | |
| Double Jump / High Jump | **Hedge-Leap** | New | Over hedges, walls and fallen trees |
| Mounted archery | **Horse-Bow** | New | Scout: Running Shot from the saddle |
| Breeds (Brianto, Elantrima, Priden) | **Heartlands cob, Highland pony, Sunward courser** | New | One per region, from the map's herds |
| Horse racing | **Market-day races** | New | On each town's market day |

---

## Part IX: Life skills

Crimson Desert's eleven life skills map straight onto the workbook's professions, and its "learn by observing an NPC" rule is Learning by Eye.

| Crimson Desert | Guardians (workbook skill) | Minor who teaches it |
|---|---|---|
| Fishing | **Fishing** | Netter, Eeler, Boatman |
| Hunting | **Skinning** and the **hunting lodges** | Huntsman, Trapper, Fowler |
| Mining | **Mining** | Delver, Prospector, Quarry Hand, Salter |
| Logging | **Logging** | Feller, Forester, Charcoaler |
| Gathering | **Harvesting** | Wildcrafter, Reagent Seeker |
| Cooking | **Cooking** | Cook, Baker |
| Alchemy | **Alchemy** (Arcana) | Apothecary, Potion Seller, the Littles |
| Horse taming | **Horse-Breaking** (new) | Ostler, Scout |
| Farming | **Farming** | Ploughman, Smallholder |
| Ranching | **Farming** (Herder) | Herder, Dairy Hand |
| Smithing | **Weaponsmithing** and **Armoring** | Bladesmith, Mailmaker, Toolsmith |

Crimson Desert's side games become the map's own pastimes: card games and dice are **Dice at the Fire** (already an activity), horse racing is the **market-day race**, arm wrestling is **Arm-Wrestling at the inn** (the Wrestling skill's friendly form), and target shooting is **the Butts** behind the guild tavern.

---

## Part X: What was rejected, and why

| Crimson Desert | Why it can't come as-is | What replaced it |
|---|---|---|
| True flight / glider | No high fantasy (canon rule 2) | The Warden's Line |
| Time-slowing Focus | Breaks the real-time squad simulation | The Measure stance |
| Phantom illusions (Nature's Echo) | No illusions in a low-magic world | The Feint |
| Gunpowder (pistol, arm cannon) | The workbook's materials are medieval | Bow, javelins, fire-flasks |
| Dodge roll | Design pillar: no roll, footwork only | The Steward's Step |
| Spectral claw | | The Grapnel |
| Elemental bracelet | Every power needs a source | Edge-oils from alchemy |

---

## Part XI: What this adds to the game

New systems the port introduces, for the design files:

1. **The Measure stance** (`M`), with Reading the Swing, Clearing the Press and Steady Breath.
2. **Fists** and **Wrestling** as Martial sub-skills, with 18 techniques.
3. **The Leyline Palm** family (9 techniques) for Arcane-gifted fighters.
4. **The Grapnel** tool tier (`TOOL-GRAPNEL-T1..T5`) and three techniques.
5. **Climbing, the Warden's Line, Breakfall and Swimming** as traversal.
6. **Edge-oils** (4 alchemy recipes) and the Grey Salt deed.
7. **Horses** with Trust and 11 skills, three breeds, and Horse-Breaking.
8. **Cores** as a skill currency and **Learning by Eye** as free training.
9. **Javelins** for spearmen; **Fire-Flasks** for alchemists.
10. 14 new sword and bow techniques for existing weapons.

Every new technique needs a row in the Combat sheet of the workbook (trigger, cooldown, scaling) before it exists in the game; this file gives it a name, a teacher and a place.

---

## Sources

The skill lists were gathered from community databases and guides in October 2026. They disagree on tree placement, level caps and some inputs, so the Crimson Desert column records what the sources agree on, not in-game text.

* [Steam: List of All Skills in Crimson Desert (2026)](https://steamcommunity.com/sharedfiles/filedetails/?id=3693402643)
* [crimsondb.gg: Kliff skill tree](https://crimsondb.gg/skill-tree/kliff), [Damiane](https://crimsondb.gg/skill-tree/damiane), [Oongka](https://crimsondb.gg/skill-tree/oongka)
* [crimsondesert.gg: skill trees](https://crimsondesert.gg/skill-tree)
* [Fextralife: Skills](https://crimsondesertgame.wiki.fextralife.com/Skills), [Kliff Skills](https://crimsondesertgame.wiki.fextralife.com/Kliff_Skills), [Grappling](https://crimsondesertgame.wiki.fextralife.com/Grappling), [Unarmed Combat](https://crimsondesertgame.wiki.fextralife.com/Unarmed_Combat), [Giant Swing](https://crimsondesertgame.wiki.fextralife.com/Giant_Swing), [Mounts](https://crimsondesertgame.wiki.fextralife.com/Mounts)
* [Game8: Kliff Skills](https://game8.co/games/Crimson-Desert/archives/586736), [Marksmanship](https://game8.co/games/Crimson-Desert/archives/587363), [Axiom Force](https://game8.co/games/Crimson-Desert/archives/587317)
* [Sportskeeda: Kliff skill tree](https://www.sportskeeda.com/esports/crimson-desert-kliff-skill-tree), [2.0 secret skills](https://www.sportskeeda.com/esports/all-new-kliff-secret-skills-cd-2-0-unlock), [Damiane build](https://www.sportskeeda.com/esports/damiane-build-crimson-desert-best-weapons-armor-skills-gameplay-tips), [Life skills](https://www.sportskeeda.com/esports/crimson-desert-life-skills)
* [VULKK: New skills in 2.0](https://vulkk.com/2026/08/26/all-new-skills-for-kliff-in-crimson-desert-2-0/), [Elemental attacks](https://vulkk.com/2026/04/16/how-to-unlock-all-4-elemental-attacks-in-crimson-desert/), [Observe skill locations](https://vulkk.com/2026/04/10/all-observe-skill-locations-in-crimson-desert/)
* [games.gg: Kliff skills](https://games.gg/crimson-desert/guides/crimson-desert-kliff-skills-and-how-to-play/), [Skills guide](https://games.gg/crimson-desert/guides/crimson-desert-skills-guide/), [Horse taming](https://games.gg/crimson-desert/guides/crimson-desert-horse-taming-guide/)
* [thegameswiki: Skills](https://thegameswiki.com/crimson-desert/wiki/skills), [Life Skills](https://thegameswiki.com/crimson-desert/wiki/life-skills), [Elemental Skills](https://thegameswiki.com/crimson-desert/wiki/elemental-skills), [Horse Guide](https://thegameswiki.com/crimson-desert/wiki/horse-guide), [Damiane Skills](https://thegameswiki.com/crimson-desert/wiki/damiane-skills), [Oongka Skills](https://thegameswiki.com/crimson-desert/wiki/oongka-skills)
* [PC Gamer: learn skills by watching](https://www.pcgamer.com/games/action/crimson-desert-observe-this-skill-in-action-to-learn-it/), [horse taming](https://www.pcgamer.com/games/action/crimson-desert-tame-horse-skills-level/)
* [DualShockers: All abilities explained](https://www.dualshockers.com/crimson-desert-all-abilities-explained/)
* [GameRant: Imbue Elements](https://gamerant.com/crimson-desert-imbue-elements-elemental-attacks/), [Horse guide](https://gamerant.com/crimson-desert-how-heal-tame-horse-buy-sell-switch-feed-level-manage-equipment/)
* [PowerPyx: Elemental skills](https://www.powerpyx.com/crimson-desert-how-to-unlock-all-elemental-skills-frost-flame-wind-lightning/)
* [ConsolePulse: Watch and Learn locations](https://consolepulse.com/multiplatform/crimson-desert/guides/all-watch-and-learn-free-skill-locations-crimson-desert), [Respec and artifacts](https://consolepulse.com/multiplatform/crimson-desert/guides/crimson-desert-respec-abyss-artifact-farming-guide), [Health, Stamina, Spirit](https://consolepulse.com/multiplatform/crimson-desert/guides/crimson-desert-health-stamina-spirit-progression-guide)
* [Greymane Codex: horse skills](https://crimsondesert.co/guides/horse-skills-breeds-legendary-stats)
* [Method: Crafting and gathering](https://www.method.gg/crimson-desert/crafting-in-crimson-desert-unravelling-the-systems-of-pywel)
* [GameSpot: playable characters](https://www.gamespot.com/gallery/crimson-desert-playable-characters-damiane-oongka-kliff/2900-7600/)
* [dropreference: skill tree explained](https://dropreference.com/en/blog/guide/crimson-desert-guide-tree-skills-branches-blue-green-red-2026)
