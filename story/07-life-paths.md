# 7. Life Paths: Who the Player Becomes

The player starts as **nobody**, like a Kenshi drifter. They choose a hamlet of birth (which sets their home hold), a combat major, and a birth-gift (talent). There is no chosen-one prophecy; the Warden's Blade is just an encounter some players will have.

The player's story is made up of **what they do, who they are known as, and how they behave**.

## Standing and reputation

* **Standing, per hold and per faction.** Standing is earned and lost through deeds. **Titled (standing 100)** with a hold grants land and a **Hall**.
* **Reputation spreads by word of mouth.** A deed is known only where someone has carried the news. A player can be a hero in Reedwatch and unknown, or wanted, in Sunward.
* **Attitude** is tracked from the player's choices, not picked from a menu:

| Attitude | Built by | How the world reacts |
|---|---|---|
| **Merciful** | Sparing the beaten, paying ransoms, healing | Outlaws surrender more often, and peasants trust you |
| **Ruthless** | Executions, burning, extortion | Lords hire you for dirty work, and hamlets bar their doors |
| **Greedy** | Price-gouging, selling out allies | Merchants and Sir John the Coin court you, and companions drift away |
| **Honourable** | Keeping contracts and oaths | Unlocks the Steward path, and Sir Thomas and Isabella Robson respect you |
| **Pious** | Temple service, cleansing barrows | Faith companions join, and Brother William tries to recruit you |
| **Curious** | Ruins, libraries, stone circles | Margaret the Sage notices you, and the hidden library opens up |

## The paths

The paths are not classes; a player can walk several at once or switch between them. Each path has its own **personal threads**, which open as the player goes deeper.

### The Trader
*Haul goods, play the markets, build a company of carts.*
* Uses the economy, routes, buy orders and caravans.
* **Threads:** notice cheap Blight-salt (the Salt Road), get squeezed by Sunward tolls, run grain to a Starving town during a war and decide your price.
* **Peak:** a trading house with a stall in every market, and coin enough to buy a lord's loyalty.

### The Adventurer
*Join a guild and clear lairs for loot.*
* Uses guild contracts, parties of five, lair tiers and the Hunters' Lodge, Academy and Temple expeditions.
* **Threads:** the Deserted Farm, the Barrow, the Academy's Relic, Blight leaks. Adventurers feel the Waking first.
* **Peak:** guildmaster of a tavern, or the party that reaches the Heart.

### The Hero
*Serve a lord as one of their three champions.*
* Get there by standing with a hold and a reputation for breaking camps. A hero's place opens when one dies.
* **Threads:** break the Grey Crows, guard the Hearth-Moot, duel Thomas Fox, choose a side in the Siege of the Stonepass Wall.
* **Peak:** Titled, with a Hall and a seat at the lords' table.

### The Sellsword
*Fight for whoever pays.*
* Join or found a free company like the Grey Company or the Red Lances, or hire one.
* **Threads:** the ford, the Red Lances' hire, war contracts once the holds arm.
* **Peak:** a company so large that lords have to bid for it.

### The Outlaw
*Take what the roads carry.*
* Join a band, or found one. Feuds absorb rivals; camps move after defeats.
* **Threads:** John Blackbeard's bid for Reedwatch, the Salt Jackals' caches, Hollow Knives contracts (including the murder at the Moot).
* **Peak:** hold a hamlet, then a town, and become **an outlaw lord** that the other lords must recognise or crush.

### The Mage
*Awaken, study and gather power.*
* Be born with *Arcane spark* or be **awakened** by Margaret the Sage. Study at a library or the Academy, or learn as a warlock.
* **Threads:** the stone-circle conclaves, the Last Spring (Lantern or warlock), the council of mages.
* **Peak:** a seat on the mage council, a court mage's post, or a warlock's spring of your own.

### The Healer or Pilgrim
*Serve the Temple: mend the wounded and cleanse the dead.*
* Wounded fighters rest rather than die, and healers decide how fast they recover.
* **Threads:** Sister Margaret and the missing salt (exposing Brother William), the Heart-Born child, cleansing barrows.

### The Steward
*Refound the old order.*
* This opens only through the Stewards' Oath thread: honourable standing, the hidden library, three sworn Stewards.
* The Stewards answer to no lord, so every lord treats them as a threat or a tool.
* **Peak:** **Lord-Steward**, keeper of the Rim Fires, with the throne left empty by choice.

### The Lord
*Rule.*
* Get there by being Titled with a hold, holding a town by force (outlaw lord), marrying in, or **taking the crown** with three holds' support.
* Rulers set taxes and station tiers, hire sellswords and order heroes out, just as the map's lords do.
* **Threads:** every Empty Throne beat now involves the player, and the other lords plot against them.

### The Slaver (the dark path)
*Sell people to the holds of the north.*
* The map supports it with slaver trade and selling captives. Towns **shun** a slaver: caravans keep away for weeks.
* **Peak:** rich, feared and alone. Every Steward and hero is a threat.

## Tested balance notes

Running the life paths on the map ([08-simulation-tests.md](08-simulation-tests.md)) showed that a dedicated guardian is **titled in all five towns in about six weeks**, and an outlaw can starve a town for months with one fire. Until the map is retuned, the story treats titles as an early-middle milestone, not an endgame.

## Companions are people, not plot devices

Every companion in [04-characters.md](04-characters.md) is a roster person with a home, a routine and their own goals. They can be recruited, can leave if the player's attitude disgusts them, and **die permanently**. Their personal arcs advance only if they are alive and travelling with the player. Otherwise the world thread carries on without them. For example, if Agnes atte Green was never recruited, she still tries to avenge her grandfather on her own, and may die trying.
