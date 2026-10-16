# 11. The Hunting Lodges

*"Take half. Leave half. The wood remembers."* (the Lodge Oath)

Every town has a hunting lodge, a sworn brotherhood of about thirty huntsmen and huntswomen, as large as an adventurers' guild. The guilds go east for glory and loot. The lodges stay home, keep the woods and feed the town. They are the oldest working institution in the realm. They are older than the guilds, outlasted the Stewards, and quietly do the job the lords have forgotten they need.

Everything marked *(sim)* happens in the Living World Map's own 364-day run.

---

## Where the lodges came from

### The King's Verderers

Before the Breaking, the woods belonged to the crown. The king's **verderers** kept them: sworn foresters who rode with the Stewards, counted the deer, hanged poachers and fed the Rim garrisons with venison. The Stewards kept the Rim. The verderers kept the Stewards fed.

They had one law, carved over every lodge door:

> **The Half Law.** Never take more than half a herd. Leave the breeding stock, and the wood will feed you again.

The map enforces it: lodge parties leave every herd and every lodge wood at half its stock *(sim: `lodge_herd_keep 0.5`)*. In the story it is the oldest law in the realm, and the only one that every lodge still keeps.

### The Breaking: the lodges choose bread

When King Aldric died and the lords tore the Stewards apart, they tried to do the same to the verderers. Each lord claimed the woods around his town as *his* forest, and the deer in it as *his* deer.

The verderers refused to become house guards. Instead, in each town, they made a deal with whoever held the keep. It is still the deal the lodges live by:

| The lodge gets | The lord gets |
|---|---|
| The right to hunt **six lodge woods** around the town *(sim: six woods per town, 2.5–6 km out)* and the far herds up to 15 km away | Meat and hides sold into the town market, never hoarded |
| Its own purse and its own law | Everything in the purse above **400 coin** goes to the town *(sim: `lodge_share_above 400`)* |
| Its hunters keep **four-fifths** of what they bring in *(sim: `lodge_pay_share 0.8`)* | The lodge's huntsmen serve the **lord's hunt** whenever he rides out |
| No tithe on the lodge itself | **The beasts of the chase (wolf, bear and red deer stag) belong to the lord** |

That last clause is the root of every lodge story.

### The Forest Charter: why the lodges don't kill wolves

Under the charter, the **wolf and the bear are the lord's beasts**. Only the lord's hunt may kill them. The lodges may not cull them, even when they come down to the folds.

The map simulates exactly this. The lodges are built to cull wolves and bears near the hamlets, but **culls are switched off**: `lodge_culls_week` is 0, and in a year the five lodges cull **nothing** *(sim)*. Meanwhile, hungry packs out of the hound runs take livestock from the folds of **Dunworth** (First Hearth, 27 nights) and **Wynstead** (Canopy Rest, 25 nights) *(sim: "the hunting ground behind them is bare")*.

So the shepherds of Dunworth watch their sheep taken night after night while thirty armed huntsmen sit in a lodge two hours' walk away, forbidden by charter to lift a bow. Most of the lodge hates it. The lords like it, because a hamlet that needs the lord's hunt needs the lord.

**This is the lodges' great political question:** break the Forest Charter and save the folds, or keep it and keep the lodge.

### The long decline

The lodges are dying slowly. Meat is cheap in a Fed town, and herbs and ore pay better. Every season, whole crews of town huntsmen put down their bows *(sim: 19 times in a year a huntsmen crew "turns to herb gatherers work" (9), "miners work" (5) or "quarrymen work" (5) "because it pays better this season")*. The old lodge-masters call it desertion. The young call it eating.

Death is the other drain. Twenty-two lodge hunters "do not come back from the week's hunting" in a year *(sim)*, and the lodges sign new members from the town to replace them, at 20 coin each.

---

## How a lodge works

| | |
|---|---|
| **Members** | 30 per lodge. The town's named huntsmen are its core crews; the rest are townsfolk signed for 20 coin. |
| **Home woods** | Six lodge woods around the town. Parties of four work them by day, keeping the Half Law. They are safe *(sim: 0.3% death risk a week)*. |
| **Far hunts** | Parties of four ride out to the far herds, up to 15 km and never into the Blighted, **but only when the town's meat is dear** *(sim: a far hunt only when the meat index ≥ 1)*. They are dangerous *(sim: up to 15% risk)*. |
| **The purse** | It lives on meat and hide sales. Hunters keep four-fifths, and anything above 400 coin goes to the town. A lodge is never rich. |
| **Food** | Lodges are self-sufficient: hunters eat what they kill before they sell any of it. |
| **The lord's hunt** | When the lord rides, the lodge's huntsmen beat the coverts. *(sim: "The lord's hunt of Canopy Rest brings a red deer hind to bay"; "The lord's hunt of Sunward Exchange loses its gazelle".)* |

---

## The five lodges

### First Hearth: the King's Lodge

*The old royal lodge, and the proudest. It still flies the crown's green banner over an empty throne.*

| | |
|---|---|
| **Woods** | Six, mostly south-west of town toward the old royal deer park, which the **Thornback Brothers** poach |
| **Crews** | **Joan atte Bridge**, **Emma atte Well**, **Isabella Gray**, **William Johnson** |
| **Best bows** | **Richard Hughson** (level 49), **Isabella Fox** (46), **Joan Wright** (46), **Agnes White** (44) |
| **Its year** *(sim)* | 290 home hunts, 22 far hunts, 2,106 coin sold, **4 dead** |

**Isabella Fox** is the cousin of Thomas Fox, Sir Robert's hero, and she wants the lodge to back Sir Robert's claim. A lodge that once served a king could serve one again. The old lodge-master would rather burn the banner.

**The Two Carters.** **John Carter** fails to come back from the week's hunting on day 154. His brother **Walter Carter** goes out to find him and doesn't come back either, on day 161 *(sim)*. The lodge says beasts. Their mother, a carter's widow in First Hearth, says the Thornback Brothers. The truth is in the royal deer park, and it's neither.

The First Hearth lodge also lost **Mabel Hobson** (day 14) and **Cecilia Brown** (day 28) early in the year *(sim)*, both on far hunts in the lean spring.

**Dunworth's wolves** are this lodge's shame. Dunworth is First Hearth's hamlet, its folds are raided 27 nights *(sim)*, and the lodge is forbidden to cull. See [Lodge stories](#lodge-stories).

### Canopy Rest: the Greenwood Lodge

*The largest family lodge. It is half Underhills, and it is the unluckiest lodge in the realm.*

| | |
|---|---|
| **Woods** | Six, east and west of town, in the realm's deepest woodland |
| **Crews** | **Joan atte Lane**, **William Underhill**, **Hugh Underhill**, **John Underhill**, **Mabel Gray**, **Nicholas Gray**, **William Brown**, **Thomas Brown**. It has more named crews than any other lodge. |
| **Best bows** | **John Little** (level 46), **Matilda Plowman** (45), **Roger Mason** (38), **Thomas Alice** (35) |
| **Its year** *(sim)* | 246 home hunts, 14 far hunts, 1,635 coin sold, **6 dead**, the most of any lodge |

The Underhills have kept Canopy Rest's woods for five generations. **William Underhill** is also a guard on the Stonepass caravan in the off-season. The family needs the coin.

**The Swift brothers.** **Robert Swift** dies on day 112. His brother **Richard Swift** takes his place in the party and dies on day 196 *(sim)*. The lodge now refuses to take the third brother. He has joined the Grey Crows' poachers out of spite, and he poaches the lodge's own woods.

The Greenwood Lodge also lost **Richard Wright** (day 84), **Margaret Smith** (day 91), **Sister Watson** (day 287) and **Geoffrey Fox** (day 343) *(sim)*. Sister Watson was a nun who left the temple for the lodge. Brother William preached at her funeral, and Sister Margaret noticed he didn't grieve.

**Wynstead's wolves:** Canopy Rest's hamlet Wynstead loses livestock 25 nights *(sim)*. Sir John Greybeard is too pious to break his own charter, and too frightened to ride out himself.

### Reedwatch: the Fen Lodge

*The poorest lodge and the steadiest. Fowlers and eelers as much as huntsmen.*

| | |
|---|---|
| **Woods** | Six, mostly east of town, the side that faces the Grey Crows' camps |
| **Crews** | **Avice Watson**, **Robert Wilson**, **William Black**, **John Swift** |
| **Best bows** | **Alice Baker** (level 48), **John Underhill** (46), **John Good** (45), **Ralph Johnson** (39) |
| **Its year** *(sim)* | 300 home hunts, only 12 far hunts, 1,818 coin sold, **2 dead**, the fewest of any lodge |

Its woods lie between Reedwatch and the Grey Crows, so the lodge has made its own peace: Thomas the Lean's poachers hunt the far side of the stream, and the lodge hunts this side. Nobody crosses. **Alice Baker** negotiated it, and Sir Thomas pretends not to know. If John Blackbeard ever takes Thomas the Lean's camp, the peace is over.

**John Underhill** (of the Canopy Rest Underhills, married into Reedwatch) dies on day 126 *(sim)*. His Canopy Rest cousins blame the Fen Lodge for sending him somewhere they'd never go.

**Henry Hostler**, son of the innkeeper, dies on day 273 *(sim)*. He was the lodge's tavern-mouth: every rumour from the inn reached the lodge through him. Now it doesn't.

### Sunward Exchange: the Desert Lodge

*The hardest-worked lodge. Desert meat is always dear, so this lodge is always out on the far hunt.*

| | |
|---|---|
| **Woods** | Six, south and west of town, scrub and oasis groves, with gazelle and wild goat rather than deer |
| **Crews** | **William atte Lane**, **Isabella Watson**, **Henry Black**, **John Robson** |
| **Best bows** | **John Swift** (level 49), **John Thomson** (40), **Alice Black** (38), **Joan Hobson** (37) |
| **Its year** *(sim)* | 271 home hunts and **41 far hunts**, nearly twice as many as any other lodge, 1,632 coin sold, **6 dead** |

The far hunts follow the price of meat *(sim)*, and in the desert meat is always dear. So the Desert Lodge rides out to the far herds week after week, close to the Blighted's edge, and pays for it. It lost **Alice Good** (day 7), **Emma Brown** (day 126), **William Long** (day 238), **Agnes Good** (day 273), **John Gray** (day 280) and **William Little** (day 357) *(sim)*.

**Henry Black** of the lodge crews is also a warden at tower four, the tower nearest the Broken March. He was the first to see a calamity's ash-light. He told the lodge before he told the lord.

**The lodge's grievance:** Sir John the Coin buys its meat at the market price and sells it on to the oasis hamlets at double. The lodge's hunters are dying to make the Coin richer, and they know it.

**William Little**, the last to die that year, was a cousin of Stonepass's Little family of alchemists. The Littles want to know what he was hunting so far out, and who was buying it.

### Stonepass Refuge: the Highland Lodge

*The only lodge that never goes far. The best-paid lodge in the realm, and the most closed.*

| | |
|---|---|
| **Woods** | Six around the highland town, with hill red deer and wild goat |
| **Crews** | **Thomas Good**, **Agnes atte Brook**, **Robert atte Lane**, **Beatrice atte Lane** |
| **Best bows** | **Ralph Gray** (level 49), **Beatrice Gray** (47), **Avice Baker** (41), **Mabel Carter** (41) |
| **Its year** *(sim)* | 312 home hunts, the most of any lodge; **no far hunts at all**; 2,301 coin sold, the most; **4 dead** |

Stonepass meat never gets dear enough for the far hunt *(sim)*, so the Highland Lodge works its home woods and nothing else. It is the richest lodge and the most insular. Hunters marry within it, and **the Grays** (Ralph and Beatrice) lead it like a clan.

It still lost **Roger Brewster** (day 126), **Joan Butcher** (day 140), **Margaret Thomson** (day 224) and **Thomas Hughson** (day 301) *(sim)* without ever leaving its own woods. Hunters don't die in safe woods four times in a year. The Iron Reavers' poachers, **Robert Shortknife** and **John the Lean**, work the same hills.

**Agnes atte Brook** of the lodge crews is also master of the Reedwatch caravan, and the Highland Lodge sells its hides through her.

---

## Lodge stories

### Dunworth's Wolves (First Hearth)
The hound run's pack takes livestock from Dunworth's folds 27 nights a year *(sim)*. Under the Forest Charter only Sir Robert's hunt may kill them, and Sir Robert is busy with the crown. The shepherds come to the King's Lodge, and the lodge says no.
* **Break the charter:** join the lodge, lead a cull, and save Dunworth. The lodge is outlawed by Sir Robert, and the lodge-master hangs for it unless the player stops it.
* **Petition the lord:** take Dunworth's case to Sir Robert's keep. Dame Alice will arrange a hunt in return for a favour.
* **Go round the law:** hire the Grey Company, or do it yourself. The charter binds the lodge, not you.

### Wynstead's Wolves (Canopy Rest)
The same problem in Canopy Rest *(sim: 25 nights)*. Sir John Greybeard is pious and won't break his own law. Dame Agnes might. Wynstead's shepherds have begun leaving lambs out as offerings at the stone circle, which Brother William encourages.

### The Half Law
Somebody is hunting a lodge wood bare, taking more than half. Is it a poacher band, a lodge member selling to Sir John the Coin, or a hungry hamlet? Breaking the Half Law is the one crime every lodge agrees on, and the punishment is the old verderers' punishment: the offender's bow hand.

### The Two Carters (First Hearth)
John Carter fails to return on day 154, and his brother Walter on day 161 *(sim)*. Follow their trail into the old royal deer park.

### The Swift Brothers (Canopy Rest)
Robert dies on day 112 and Richard on day 196 *(sim)*. The third Swift brother is now a Grey Crow poacher, and he wants the lodge to suffer.

### The Desert Lodge's Strike (Sunward)
After the sixth death of the year, the Desert Lodge refuses to ride the far hunt until Sir John the Coin pays a fair price. Sunward's meat runs short, prices climb, and the player can break the strike, back it, or bring meat in and profit.

### The King's Banner (First Hearth)
Isabella Fox wants the King's Lodge to declare for Sir Robert. If the lodge backs a claimant, the other four lodges must choose. The lodges become one more piece in the Game of Holds.

### The Lord's Hunt
The lords' hunts are where politics happens *(sim: a lord's hunt rides out most days)*, and the lodge's huntsmen beat the coverts for them. A lodge hunter hears everything said in the saddle, and a lodge hunter can arrange an accident.

---

## The lodges and the player

These are the map's own deeds *(sim: `join_lodge`, `lodge_sell`, `hire_hunter`)*:

| Deed | Cost | What it means in the story |
|---|---|---|
| **Join a lodge** | **25 coin** in dues | You swear the Half Law and the Forest Charter. Lodge members trust you; lords' foresters watch you. |
| **Sell hides to the lodge** | The lodge takes a **15% cut** | Better than a market stall, and it raises your standing in the town. |
| **Hire a hunter** | **40 coin**, half that for members | Take the lodge's best free bow with you. The lodge loses a hunter, and remembers. |

**The Hunter life path:** join a lodge, rise to lodge-master, and then decide what the lodges are for: the lords' foresters, the hamlets' protectors, or a sixth power in the realm, thirty bows in every town.

## Notes for the map

* **Lodge culls are switched off** (`lodge_culls_week = 0`). The story makes that the Forest Charter, but if it isn't deliberate, it is why Dunworth and Wynstead lose their folds all year.
* One generated lodge hunter is named **"Sister Watson"**, a religious title used as a first name. The story gives her a past to fit, but the name generator may need a guard.
* A Canopy Rest lodge member is named **"Thomas Alice"**, which looks like a first name used as a surname.
