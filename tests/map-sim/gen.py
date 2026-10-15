import json,collections
H=json.load(open('hamlets.json')); BT=json.load(open('bytown.json'))
TOWNS=['First Hearth','Canopy Rest','Reedwatch','Sunward Exchange','Stonepass Refuge']
L=[]
w=L.append
w("""# 10. The Book of the Realm: Every Person and Place

An Oblivion-style gazetteer of the realm. Every named person, band, hamlet, trade and technique in the design files has a place here. Nobody here is a quest-giver waiting for the player. Each has a life the simulation already runs, and a story the player can walk into.

**How to read it:** names in **bold** are roster people from the Living World Map. Facts marked *(sim)* happened in the 364-day test run described in [08-simulation-tests.md](08-simulation-tests.md). Everything else is story built on top of those facts.

---

## Part I: The outlaw houses

The Grey Crows, the Red Crows and the Iron Reavers are not rabble. They are **families**. The same surnames (the Leans, Halfpennies, Shortknives, Coldhearths, Crowfoots, Wildgeese and Strongbows) turn up in every camp. Brothers ride for rival captains, and cousins carry messages between bands that are supposed to be at war. That is why the bands feud without ever destroying each other *(sim: 120 feuds in a year, and most end "with no winner")*: nobody wants to kill their own blood.

Every camp has the same shape: a **captain** who calls himself a king, a **lieutenant**, a **camp cook**, **water carriers**, a **go-between** who deals with the towns, **poachers** who feed the camp, a **scout**, and **highwaymen** who do the robbing.

### The Grey Crows: three kings in one band

The Grey Crows are the largest band (38 men), split across three camps east of Reedwatch, each with its own king. This is the realm's *Game of Thrones* in miniature.

| Camp | King | Court | The king's story |
|---|---|---|---|
| 6 km east of Reedwatch | **Thomas the Lean, "king of the Marches"** | **John the Lean** (lieutenant, his brother), **Alice Stonehand** (cook), **Stephen the Lean** and **Henry Quickfoot** (water), **William Wildgoose** (go-between), **John Shortknife** and **John Redhand** (poachers), **Henry Longshanks** (scout), **William Crowfoot** and **John Shortknife** (highwaymen), **Robert Shortknife**, **Richard Coldhearth**, **Nicholas Shortknife** and **Joan Halfpenny** (rovers) | The eldest king, who holds the camp nearest Reedwatch. The Leans are the band's old blood, and Thomas wants the Crows to stay outlaws: rich, free and unhanged. |
| 14 km east of Reedwatch | **John Blackbeard, "king of the Marches"** | **Joan the Lean** (lieutenant, Thomas's niece), **Juliana the Lean** (cook), **John Stonehand** and **Emma Crowfoot** (water), **John Nettle** (go-between), **Mabel Quickfoot** and **Alice Coldhearth** (poachers), **Christina Coldhearth** and **Richard Greyhood** (scouts), **William Brokenose**, **Robert Thornback** and **John Ashwood** (highwaymen) | He also calls himself king of the Marches, which is a direct challenge to Thomas. He wants Reedwatch, a real title and a hall. Joan the Lean rides with him against her own uncle. *(sim: broken camps "join their band at 14 km east of Reedwatch", so Blackbeard's camp is where beaten Crows go, and it keeps growing.)* |
| 12 km east of Reedwatch | **Alice Thornback, "queen of the Rifts"** | **Robert of the Moor** (lieutenant), **Margaret Blackbeard** (cook, John's sister), **John Wildgoose** (water), **Stephen Shortknife** (go-between), **Isabella Ashwood** (poacher), **John Strongbow** (scout), **Ralph Coldhearth** and **Richard Halfpenny** (highwaymen) | The only queen among the outlaws, and the only one who goes *toward* the Blight. Her people pick the bones of guild parties lost at the rifts and sell what they find. She knows the rift paths better than any guild. |

**Story threads:**
* **The Crow Succession.** If any Crow king dies, by a lord's hero, the Blight or the player, the other two fight over his camp. The Leans side with whoever honours their blood.
* **Margaret Blackbeard's letters.** John Blackbeard's sister cooks in Alice Thornback's camp. She is his spy, or Alice's, or both.
* **Robert Thornback** is a highwayman in Blackbeard's camp and a folk hero to the hamlets, because he only robs carts with a lord's seal. He is a possible companion if the player saves him from a hero's raid.

### The Red Crows: the splinter

| Camp | King | Court | Story |
|---|---|---|---|
| 6 km north-east of Reedwatch | **Walter Crowfoot, "king of the Rifts"** | **Adam Wildgoose** (lieutenant), **Stephen Quickfoot** (cook), **William Greyhood** (water), **Henry Redhand** (go-between), **William of the Moor** (poacher), **John Longshanks** (scout), **Robert Halfpenny** and **Alice Crowfoot** (highwaymen), **John Coldhearth**, **Thomas Greyhood**, **Nicholas of the Moor** and **William Crowfoot** (rovers) | Walter left the Grey Crows when Thomas the Lean refused to raid lords' carts. **Henry Redhand** is the realm's busiest go-between: he takes **Sunward coin** to point the Red Crows at First Hearth's carts *(sim: the Red Crows ambush carts from Selden)*, and Sir John the Coin denies it. |

### The Iron Reavers: deserters with two masters

| Camp | King | Court | Story |
|---|---|---|---|
| 7 km north-west of Stonepass | **John Brokenose, "king of the Waste"** | **John Longshanks** (lieutenant), **Thomas Stonehand** (cook), **Robert Brokenose** and **William Halfpenny** (water), **Robert Halfpenny** (go-between), **Robert Shortknife** and **John the Lean** (poachers), **Joan the Lean** (scout), **John Blackbeard** (a highwayman who shares the Crow king's name, and the joke in every tavern), **Robert Halfpenny** and **Alice Halfpenny** (highwaymen), **Beatrice Nettle**, **William Halfpenny**, **John Halfpenny**, **Beatrice Coldhearth** and **Thomas Quickfoot** (rovers) | A former Stonepass sergeant who deserted over unpaid wages. **Robert Halfpenny** carries **First Hearth's coin** to him. He takes Sir Robert's pay to raid Stonepass, and he knows that Sir Robert's hero will break him the moment he grows too strong *(sim: First Hearth's hero breaks the Reavers 7 times)*. |
| 6 km west of Stonepass | **Thomas Coldhearth, "king of the Rifts"** | **Beatrice Ashwood** (lieutenant), **Nicholas Strongbow** (cook), **John Coldhearth** and **Alice Crowfoot** (water), **Joan of the Moor** (go-between), **Roger Crowfoot** and **Matilda the Lean** (poachers), **Thomas of the Moor** (scout), **Alice Halfpenny**, **Emma the Lean** and **Nicholas Wildgoose** (highwaymen) | He refuses First Hearth's coin and takes hamlets instead *(sim: the Reavers occupy Malstead on day 24 and Stanton on day 66)*. **Joan of the Moor** is quietly negotiating with Sir John Ironhand: pardon for land. |

**Beatrice Nettle**, a rover with the Reavers, knows the dry roads around the Blighted from her years as a guide. She is the desert-rider companion. She'll leave the Reavers for the player if the player has broken a Reaver camp without killing the rovers.

### The other bands

The Salt Jackals, Thornback Brothers, Ash Hounds, Dust Riders, Blackwater Men and Hollow Knives have **no named members on the map**. Their members are the realm's nameless. The story keeps it that way: they are the faceless outlaws of the roads, and the player only learns names by joining them (when the game names everyone the player talks to).

---

## Part II: The road and the wayside

### The tower watch: the keepers of the beacons

Six watchtowers, three wardens each. At dusk they light the beacons *(sim: day 4, six wardens light the beacon)*. None of them knows why except **Walter Underhill**, who keeps tower three with **William Robson** and **William Brown**.

| Tower | Wardens | Story |
|---|---|---|
| One | **John atte Gate**, **Isabella Johnson**, **John Hobson** | John Hobson lights the beacon every night and logs it. His logbook is the only record of which nights the beacons went dark. |
| Two | **Robert atte Lane**, **John atte Bridge**, **William Young** | This Robert atte Lane shares a name with the Red Lances' captain. Tavern talk says it's the same man, living two lives. It isn't, but the rumour gets the warden beaten. |
| Three | **Walter Underhill**, **William Robson**, **William Brown** | Walter is the last who knows the Oath (see Thread 4). When he dies on the road, William Robson inherits his duties and his silence. |
| Four | **Robert Gray**, **William White**, **Henry Black** | Closest to the Broken March. Henry Black was the first warden to see a calamity's ash-light on the horizon. |
| Five | **Alice atte Gate**, **Richard atte Well**, **Robert Good** | A desert tower. Robert Good trades water with the water-sellers to keep the tower supplied. |
| Six | **John Long**, **Emma Robson**, **John White** | John White keeps a tally of the slavers' raids he sees from the tower, and nobody reads it. |

### The hospices and the shrine

| House | Who | Story |
|---|---|---|
| Wayside hospice, west | **Ralph Wilson**, **Joan Little**, **Isabella atte Gate** | They take in the wounded who can't pay. Joan Little patches up outlaws as readily as guildsmen and asks no questions. |
| Wayside hospice, First Hearth road | **John Long**, **Beatrice atte Lane**, **Thomas Brown** | The nearest bed to Riftgate, where guild survivors come to recover *(sim: 183 guild deaths a year, and many more wounded)*. |
| Wayside hospice, Sunward road | **Agnes Good**, **John Underhill**, **Alice atte Brook** | They hold the ransom money for the slavers' captives, and keep the accounts. |
| The wayside shrine | **Mother Alice**, the anchoress | Walled into her cell for twenty years, she hears every pilgrim's confession. She knows more secrets than any spymaster, and tells none, unless the realm is ending. |

**Pilgrims to the shrine:** two bands walk the roads. One is **Alice Johnson**, **Robert Thomson**, **Emma Watson** and **Thomas Watson**, out of Reedwatch. The other is **Emma atte Lane**, **John atte Green**, **William Good** and **John Watson**, out of Sunward. They are easy prey for highwaymen and a common reason for the player to meet outlaws. Emma Watson goes to Mother Alice to confess a murder that someone else is about to hang for.

### Caravans, pedlars and heralds

| Who | Story |
|---|---|
| **The Stonepass Refuge caravan:** **John atte Green** (master), **William Underhill** and **William Dickson** (guards), **Agnes Johnson** (muleteer) | Carries ingots and steel. It is the Iron Reavers' favourite prey, and John atte Green pays John Brokenose a secret toll to pass. |
| **The Sunward Exchange caravan:** **Thomas Gray** (master), **Isabella atte Brook** and **Agnes Little** (guards), **John atte Bridge** (muleteer) | Carries jewels and coin. It also carries Dame Matilda's Blight-salt in false-bottomed barrels, and Thomas Gray doesn't know it. |
| **The Reedwatch caravan:** **Agnes atte Brook** (master), **William Dickson** and **Beatrice Watson** (guards), **Beatrice atte Wood** (muleteer) | Carries cloth and fish. Agnes atte Brook is honest and losing money every week. She'll hire the player as an escort. |
| **Pedlars** **Avice atte Wood** (First Hearth), **Margaret Gray** (Canopy Rest) and **Margaret atte Lane** (Stonepass) | They sell needles, ribbons and *news*. A pedlar is the fastest way word travels between towns, so they matter to reputation. |
| **Heralds** **William Robson** (Stonepass) and **John atte Green** (Reedwatch) | They carry the lords' proclamations: the Hearth-Moot summons, bounties and titles. Bribing a herald changes what a town hears. |
| **The water-sellers** **William Little**, **John Hobson**, **Edmund atte Bridge** and **Christina Brown** | They haul water from the last spring and pay Juliana the Warlock's toll. If the spring is freed, they are ruined or rich, depending on who freed it. |

### Free companies and free mages

* **The Grey Company:** **Margaret Young** (captain), with **Margaret Robson**, **John atte Green**, **Matilda Underhill**, **Thomas atte Lane**, **Ralph atte Bridge**, **Alice Hobson**, **William Dickson**, **William Hughson** and **Joan atte Gate**. They are the professionals. Margaret Young has never broken a contract, and she has never taken one from Sir Robert. *Why not* is her secret: she was Sir Robert's hero before Thomas Fox was.
* **The Red Lances:** **Robert atte Lane** (captain), with **Joan Dickson**, **Isabella Robson**, **Agnes Hughson**, **Robert atte Wood**, **Christina Watson**, **William atte Lane** and **Mabel Watson**. They are hungry and unpaid. Isabella Robson of the Lances is the cousin of Cairn Gate's Isabella Robson, and the two don't speak.
* **The Low-Water band:** **John Little**, **Emma Fox**, **Mabel Robson**, **Thomas Watson**, **Richard Wilson** and **Agnes atte Wood** hold the ford. This John Little is not Reedwatch's giant hero, though he's happy to let travellers think so.
* **The Company of the Lantern:** **Robert Underhill**, **John Hughson**, **John Dickson**, **Richard atte Gate** and **Isabella Good**, free mages who answer to no lord. Richard atte Gate leads them. They're the ones who beat Juliana the Warlock.
* **The warlock's household:** **Juliana the Warlock** and her apprentice **John Robson**. When Juliana is exiled, John Robson stays at the spring alone and keeps her wards up. The water-sellers don't know whether to pay him.
* **Journeyman mages on the road:** **Adam Johnson** (First Hearth inn), **Cecilia Swift** (Canopy Rest inn) and **John Wilson** (Sunward inn). Each is travelling to the tower school by Mereworth. They are the first mages a new player can hire.

### The guild parties of five

Each guild has one party that is always out. They're the player's rivals, and sometimes the player's rescuers.

| Guild | Warrior | Mage | Priest | Thief | Hunter |
|---|---|---|---|---|---|
| First Hearth (Riftgate) | **William atte Gate** | **Roger atte Gate** | **Agnes Fox** | **Walter atte Gate** | **Joan Underhill** |
| Canopy Rest (Westwatch) | **Agnes atte Lane** | **Ralph Thomson** | **John Good** | **Beatrice Long** | **Alice Underhill** |
| Reedwatch (Oxdon) | **Joan Gray** | **Walter Dickson** | **Matilda atte Gate** | **John Long** | **Alice Hughson** |
| Sunward Exchange (Blightwatch) | **John Johnson** | **Avice Hughson** | **Juliana Swift** | **Alice atte Lane** | **Agnes atte Brook** |
| Stonepass Refuge (Cairn Gate) | **Alice Good** | **John Fox** | **Ralph Johnson** | **Isabella atte Green** | **John Johnson** |

* **First Hearth's party is three atte Gate siblings** (William, Roger and Walter) and two friends. If one dies, the others leave the guild.
* **Walter Dickson and John Long of Reedwatch** die in a rift *(sim: a level-34 Reedwatch party is lost on day 136; the dead are Avice Black, Emma Webster, Walter Dickson, John Long and one more)*. Joan Gray, Matilda atte Gate and Alice Hughson weren't with them that day. Matilda had traded places with Avice Black that morning, and she won't say why.

---

## Part III: The five towns, person by person
""")
exec(open('hooks.py').read())
import hashlib
for i,t in enumerate(TOWNS):
  d=BT[str(i)]
  w(f"\n### {t}\n")
  w("| Person | Role | Their place in the story |")
  w("|---|---|---|")
  seen=set()
  for role,ppl in sorted(d.items()):
    if role=='Sorcerer': continue
    for n,_ in ppl:
      if (n,role) in seen: continue
      seen.add((n,role))
      h=P.get((t,n),"")
      if h=="" : h="(no hook)"
      w(f"| **{n}** | {role.replace('CunningFolk','Cunning folk')} | {h} |")
  sor=d.get('Sorcerer',[])
  w(f"\n**The {t} circle** ({len(sor)} sorcerers, who meet at the hold's stone circle; *sim: nine meet in conclave on day 5*):\n")
  for k,(n,_) in enumerate(sor):
    g=GIFT[(k+i*3)%len(GIFT)]; s=SIT[(k*7+i*2)%len(SIT)]
    w(f"* **{n}** {g}, {s}.")
w("""
---

## Part IV: The hamlets

Every hamlet below is on the map. Its land, people and year come from the workbook and the simulation *(sim)*. Each one has its own small story.
""")
def kind(info):
  k=info.get('Kind (v58)')
  if k=='herders': return "a herders' camp in the desert"
  if k=='oasis': return "an oasis hamlet"
  c={x:info.get(x+' cells',0) or 0 for x in['Meadow','Highlands','Wetland','Woodland','Desert']}
  m=max(c,key=c.get)
  return {'Meadow':'a farming hamlet','Highlands':'a hill hamlet','Wetland':'a fen hamlet','Woodland':'a woodland hamlet','Desert':'a desert hamlet'}[m]
HOOK={'raid':"raided",'abandoned':"abandoned",'overrun':"overrun by Blight-born",'occupied':"occupied by outlaws",'slavers':"struck by slavers",'ambush':"carts ambushed",'moves':"beasts at the folds"}
by=collections.defaultdict(list)
for h,v in H.items(): by[v['hold']].append((h,v))
qi=0; used=collections.Counter()
for t in TOWNS:
  w(f"\n### {t}\n")
  w("| Hamlet | What it is | Its year *(sim)* | Story |")
  w("|---|---|---|---|")
  for h,v in sorted(by[t]):
    info=v['info']; e=v['ev']
    trade=[lab for k,lab in [('Miners','miners'),('Fishers','fishers'),('Loggers','loggers'),('Hunters','hunters')] if (info.get(k) or 0)>=5]
    sp=info.get('Smith or priest')
    desc=f"{kind(info)} of {v['people']}"+(f", known for its {', '.join(trade)}" if trade else "")+(f"; keeps a {sp}" if sp else "")
    yr=[f"{HOOK[k]} ×{e[k]}" for k in ['abandoned','overrun','occupied','slavers','raid','ambush','moves'] if e.get(k)]
    cat=next((k for k in ['abandoned','occupied','slavers','overrun','raid','ambush','moves'] if e.get(k)),None)
    if cat:
      pool=EVENT[cat]; st=pool[used[cat]%len(pool)]; used[cat]+=1
    else:
      st=QUIET[qi%len(QUIET)]; qi+=1
    w(f"| **{h}** | {desc[0].upper()+desc[1:]} | {', '.join(yr) if yr else 'quiet'} | {st} |")
w("""
### Hamlets with a named story

* **Malton** (Sunward): abandoned and resettled again and again *(sim: abandoned on days 70 and 75 and many times after)*. The resettlers find the last family's food stores untouched every time, so no one is eating. Somebody is clearing Malton on purpose, to buy the land cheap.
* **Malstead and Stanton** (Stonepass): taken by Thomas Coldhearth's Reavers *(sim: days 24 and 66)* and retaken by Cairn Gate's adventurers *(sim: days 32 and 75)*. One family stayed behind and fed the Reavers. Now the neighbours want them hanged.
* **Hurstead** (Stonepass): 7 people carried off by the slavers *(sim: day 21)* and ransomed home *(sim: day 49)*. One of the seven didn't come home, and was sold on.
* **Tunden and Dorton** (Stonepass): burned by the Iron Reavers on day 5 *(sim)*. Tunden lost 3,072 grain and 14 people. Its survivors joined the Reavers out of hunger.
* **Kirkden and Ulfham** (Sunward): the first hamlets overrun by Blight-born *(sim: day 21)*. Sunward's guild cleared them in six days. These are the realm's first sign that the leaks have begun.
* **Whitden** (First Hearth): the Red Crows and the Thornback Brothers both take sheep from its folds *(sim: day 1)*, so the shepherds pay both. That is the cheapest peace in the realm.
* **Radham** (First Hearth): its grain carts are shadowed by the Thornback Brothers *(sim: day 1)* and lost to them *(sim: day 50)*.
* **Selden** (Reedwatch): its carts are lost to the Red Crows *(sim: day 56)*, Henry Redhand's Sunward-paid work.
* **Cranham** (Stonepass): the slavers try it and Stonepass's guards drive them off *(sim: day 7)*. It is the only hamlet that beat them, and it trains its people now.
* **Holton** (Reedwatch): the wolf den has gone hungry and comes to its folds every night *(sim: day 16)*.

---

## Part V: Trades, titles and the hall

### Skill titles: the realm's quiet thrones

The workbook says: *the one best master of each skill in the world holds its title, and it passes on when they die or are surpassed.* There is a title for **Mining, Logging, Harvesting, Skinning, Fishing, Farming, Smelting, Woodworking, Weaving, Leatherworking, Stonecutting, Weaponsmithing, Armoring, Engineering, Jewelcrafting, Cooking and Furnishing**, and one for each school of Magic.

This is *Game of Thrones* for craftsmen. A **Master Weaponsmith** of the realm can name their price, and their rivals can arrange accidents. The player can:
* **Rise:** become the best and take the title, then defend it.
* **Kingmake:** fund a rival's tools, or poach a master *(sim: Reedwatch hires Margaret Smith, a weaponsmithing journeyman, away from First Hearth for 150 coin on day 42)*.
* **Murder:** the map supports killing makers (`kill_maker`), and the title passes on. The town remembers.

### Professions and their people

| Profession | Story place |
|---|---|
| **Tanning** | Reedwatch's stink-yards, where the Blackwater Men buy leather to smuggle |
| **Clergy** | The temples, shrine, hermitage and hospices (Part II) |
| **Adventuring** | The guilds and their parties of five |
| **Hospitality** | The inns and guild taverns. Every innkeeper hears everything. |
| **Scholarship** | Libraries, the tower school by Mereworth and the hidden library |
| **Homemaking** | Half the realm's women keep house. Households are where feuds start, and marriages end them. |
| **Haulage** | Carriers and caravans: the roads' lifeblood, and the outlaws' living |
| **Labour** | Day labourers, the first to starve and the first recruited by outlaw bands |
| **Banditry** | The outlaw houses (Part I) |

### The minors: who people are inside their trade

Every person has a minor (a subclass) for life, and each one is a kind of person the player meets.

| Minor | Where you meet them |
|---|---|
| **Warlord** | Sir John Ironhand is one; so is any lord who leads in the field. Their levy is stronger. |
| **War Chanter** | They sing the Stonepass clans into battle, and the Reavers have one too. |
| **Lawgiver** | Stewards and clerks who judge petitions at the Stewards Halls |
| **Herald** | William Robson and John atte Green, who carry the lords' words |
| **Archivist** | The librarians, who hold the realm's memory and its forgeries |
| **Invocator** | Faith casters who call on the saints in battle (the Cleric's *Dawnbreaker Pillar*) |
| **Flagellant** | Penitents who whip themselves on the pilgrim road to atone for the Breaking. Brother William recruits from them. |
| **Dervish** | Desert ascetics near Sunward who dance in the heat of the day, and fight that way |
| **Fen Walker** | Reedwatch guides who know the safe paths through the fen (the Ranger's *Fen-Strider's Grace*) |
| **Wildcrafter** and **Reagent Seeker** | Herb-gatherers who climb to the butte-top herb patches and Ashcut Gorge |
| **Potion Seller** | Market stalls of draughts, some of them the Little family's, some of them fakes |
| **Siegewright** | Engineers who build walls and towers when a town's council orders them |
| **Waller** | Builders of field walls and hamlet palisades |
| **Gem Cutter** and **Goldsmith** | Sunward's jewellers (Sunward has the only tier-5 jeweller's bench) |
| **Bladesmith**, **Mailmaker** and **Toolsmith** | The smiths; the best of them holds a skill title |
| **Furnace Keeper** and **Refiner** | Stonepass smelters, with the sky-iron secret |
| **Delver**, **Prospector**, **Quarry Hand** and **Salter** | Miners. Salters near Sunward first found the grey salt. |
| **Feller**, **Forester** and **Charcoaler** | Canopy Rest's woods. Charcoalers see everything that moves at night. |
| **Netter**, **Eeler** and **Boatman** | Reedwatch fishers. The Blackwater Men hire boatmen for the coves. |
| **Trapper**, **Huntsman** and **Fowler** | The hunting lodges and the lords' hunts |
| **Herder**, **Ploughman**, **Smallholder** and **Dairy Hand** | The hamlets (Part IV) |
| **Caravaneer**, **Factor**, **Pedlar** and **Shopkeeper** | The merchants of the roads and markets |
| **Clerk** | Stewards' clerks, who keep books that can be altered |
| **Cook** and **Baker** | Inns, keeps and the camp cooks of the outlaw houses |
| **Butcher**, **Tanner**, **Currier**, **Glover** and **Saddler** | Leather trades |
| **Weaver**, **Fuller**, **Dyer**, **Tailor** and **Loom Hand** | Cloth trades |
| **Joiner**, **Carver**, **Cabinetmaker**, **Cooper**, **Upholsterer** and **Thatcher** | Wood and furnishing trades |
| **Mason** | Builders of keeps, halls and the player's hall |
| **Fletcher**, **Bowyer** and **Glassblower** | Specialist crafts, scattered across the towns |
| **Apothecary** | Healers who sell herbs from a shop rather than the temple |

### The player's hall

The hall's parts are each a part of the player's story:
* **Storehouse:** where the player's wealth sits, and what raiders come for.
* **Barracks:** houses recruits. A **raid on the hall succeeds when its strength beats walls, towers and the garrison**, so the barracks is the player's own Stonepass Wall.
* **Alchemy lab:** brew your own elixirs and break the Little family's monopoly, which makes enemies in Stonepass.

---

## Part VI: The wild

| Beast | Where and why it matters |
|---|---|
| **Wolf** | Frontier and the Broken March. When a den goes hungry for ten days, its wolves raid the folds every night *(sim: Holton, day 16)*. |
| **Wild boar** | Root by day and fight when cornered. A lord's hunt that brings one to bay is a feast *(sim: the Canopy Rest hunt, day 3)*. |
| **Red deer and roe** | The lords' hunts' quarry. Poaching them is how the Thornback Brothers became folk heroes. |
| **Gazelle and wild goat** | Desert and hill game. Sunward's hunt loses its gazelle *(sim: day 2)*, and the court mocks the lord for a week. |
| **Wildfowl** | Fen ducks. Reedwatch's fowlers feed the town in lean weeks. |

The **hunting lodges** of each town cull these grounds and sell what they take *(sim: some hunters don't come back from the week's hunting)*.
""")
open('/home/user/guardians-story/story/10-book-of-the-realm.md','w').write("\n".join(L)+"\n")
print(len(L))
