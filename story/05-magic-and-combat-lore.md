# 5. Magic and Combat Lore

**Design rule:** abilities stay *grounded and readable*: simple fire, light, steel and sigils that fit the 8-state animation rig (Light Strike, Heavy Cleave, Block/Parry, Ranged Draw, Staff Cast Pulse and so on). No spell should need more than a staff pulse and one clear VFX shape.

## Where power comes from

| Source | Who uses it | In the world |
|---|---|---|
| **Steel** (Martial) | Guardsmen, Duellists, Sellswords, Brigands | Most of the realm's power. Sword-forms were codified by the Stewards and passed down in the guilds. |
| **The Bow** (Marksmanship) | Wardens, Scouts, Hunters, Rangers | Commoners' power. Wardens once manned the Rim lookouts. |
| **Arcane** (Magic) | Scholars, Wanderers, Hermits, Court Mages | Learned, rare and slightly feared. Drawn from **leylines**, faint currents in the ground. This is why a mage's power peaks in the *Leyline Band* (6–9.5 m) and is strongest inside ground sigils. |
| **Faith** (Magic) | Clerics, Healers, Pilgrims, Anchorites | Prayer made real. All healing is Faith. Faith is weaker in raw damage (0.6x AP) but protects the whole party. |
| **Alchemy** | Arcana brewers | Draughts and elixirs (`POT-HEAL`, `POT-ELIX`, `POT-WARD`, `POT-STAM`). |
| **The Blight** | Horrors, calamities, Brother William | Stolen power. It feeds on the leylines; that is why Arcane and Blight are drawn to the same places. |

### The mages of the realm (from the map)

The map's rosters hold about **90 sorcerers**, **10 mages**, cunning folk in every hold, and an alchemist family in Stonepass. Magic is rare among the people the player meets, but not unknown:

* **Sorcerers** are commoners with a gift who keep it quiet. They gather nine at a time in **conclave at the five stone circles**, which sit on leylines.
* **Mages** are trained, mostly at **the Arcane Academy** and the town libraries. Court mages (Dame Matilda of Sunward, the steward John Dickson) serve lords.
* **Cunning folk** know hedge-magic: charms, herb-lore and the odd ward. Some are heroes, like Nicholas Swift of Stonepass.
* **Margaret the Sage** wanders the realm holding audiences with lords. She can **awaken** a sleeping gift, as she does for Robert Cordwainer in First Hearth's market. In game terms, awakening is how an NPC gains a Magic major, and the player can ask her to do it for a companion.
* **Warlocks** are mages who sell their power or take what they want. **Juliana the Warlock** holds the last spring in the Sunward desert and tolls its water. When she is beaten she is **exiled** to the warlock's refuge outside First Hearth.
* **The Company of the Lantern** are free mages who answer to no lord.

**Why magic is rare:** an Arcane aptitude good enough for Journeyman is held by about 35% of those trained, and only the top 3% reach Master. Most mages are scholars who can throw one good firebolt. A true Arcane Master is a political asset that houses fight over, which is part of why Joan Thomson matters.

## The simple spell list (story names to system abilities)

These are the names players hear in dialogue and see in the UI. Each maps to an existing ability in `stewards_combat_system.md`, so no new system work is needed.

### Arcane: fire and storm

| Story name | System ability | What it looks like |
|---|---|---|
| **Firebolt** | *Focus Bolt* (Staff L1) | A fist-sized ember thrown from the staff head |
| **Fireball** | *Arcane Detonation* (Staff L5) | A firebolt that bursts in a 2.5 m ring of flame on impact. The iconic mage spell. |
| **Ember Volley** | *Arcane Barrage* (Scholar) | Three small fire darts that seek the weakest-warded foe |
| **Pillars of Fire** | *Sovereign's Fire* (Court Mage awakening) | Three columns of fire marching in a line through the target |
| **Chain Lightning** | *Chain Lightning* (Wanderer) | A white crackle jumping between up to 4 targets, stronger over water |
| **Gust** | *Gale-Force Repulse* (Wanderer) | A blast of wind that throws attackers back and can slam them into walls |
| **Binding Sigil** | *Sigil of Binding* (Staff L15) | A glowing ring on the ground that roots anyone who steps in |
| **Ash Skin** | *Carapace of Ash* (Hermit) | Grey stone-like scales that harden over the caster when struck |

### Faith: light and wards

| Story name | System ability | What it looks like |
|---|---|---|
| **Holy Light** | *Radiant Pulse* (Staff L5, Faith) | A burst of gold light that burns horrors and undead |
| **Mend** | *Mending Grace* (Healer) | A soft glow that closes wounds and clears bleeding |
| **Hallowed Ground** | *Consecrated Ground* (Cleric) | A golden ring that heals allies and burns the Blight |
| **Ward** | *Radiant Aegis* / *Faith Ward* | A shimmer of light that blunts spells |
| **Dawnbreak** | *Dawnbreaker Pillar* (Cleric awakening) | A column of light that heals the party and blinds enemies |
| **Last Grace** | *Miracle of the Road* (Pilgrim) | Stops a killing blow and holds an ally at 25% HP |

### Steel: sword, axe, spear, hammer, shield

| Story name | System ability | What it looks like |
|---|---|---|
| **Slash** | *Quick Slash* (Sword L1) | A fast one-handed cut |
| **Hamstring** | *Tendon Cut* (Sword L5) | A low cut to the leg that makes the target bleed and slows it |
| **Flurry** | *Flurry of Steel* (Sword L30) | A quick double strike |
| **Steward's Riposte** | Same (Sword L50) | The old Steward counter: parry, then an unblockable cut. The player learns it at Master. |
| **Cleave** | *Reaping Arc* (Axe L15) | A wide swing through a group |
| **Execute** | *Executioner's Guillotine* (Axe L50) | An overhead chop that finishes a wounded enemy |
| **Skewer** | *Impaling Lunge* (Spear L5) | A spear thrust that pierces a line of enemies |
| **Ground Slam** | *Earthshaker Slam* (Hammer L15) | A hammer hits the ground and shakes everyone nearby |
| **Shield Bash** | Same (Shield L8) | Interrupts a big swing and knocks the enemy back |
| **Shield Wall** | *Lock Shields* (Shield L35) | Two shield-bearers lock together into a wall |

### Bow

| Story name | System ability |
|---|---|
| **Aimed Shot** | *Measured Shot* |
| **Piercing Arrow** | *Bodkin Piercer* |
| **Arrow Rain** | *Suppressing Volley* / *Iron Rain Barrage* |
| **Pinning Shot** | Same |

## How the systems become story

* **No dodge roll.** Stewards' training says *"A Steward does not leap. A Steward steps."* Footwork, flanking and spacing are taught as the old Steward discipline, and John Thomson teaches them as tutorials in Act I.
* **Auto-triggered abilities.** In-world, these are *drilled forms*: trained fighters act on instinct. The player commands where to stand; the body knows what to do.
* **Sweet-spot rings.** Every weapon school teaches its "measure", the distance at which the weapon sings.
* **Flank arcs.** The duellist's proverb: *"A shield only guards one way."*
* **Wall-pins.** These are Stonepass hammer-lore, "Give them to the stone."
* **Permadeath and wounds.** Death is permanent, but a beaten survivor is wounded and must rest. The healers' trade (and Sister Margaret's arc) revolve around this.
* **Master true damage (15%).** Folk say that a master's blade "cuts what armour can't keep out". In the story, this is the visible proof of mastery.
* **Talents.** The realm's word for them is "birth-gifts". *Arcane spark* children are sought by houses, *Blight-hardened* people are rumoured to have Blight in their blood, and *Born survivors* are said to be "refused by the grave".

## The Blight in combat

* Horrors and calamities telegraph their attacks with **red ground shapes** that warn where they'll hit. In the fiction, the Blight is *visible*: grey-red cracks spread across the ground before it erupts.
* *Blight-hardened* fighters and Faith wards resist it.
* The Hermit's **Blight-Eater Rune** is "old Steward craft". It works because it starves the Blight of leyline power.

## Every technique, by who teaches it

Every auto-triggered ability in `stewards_combat_system.md` has a teacher and a reputation in the world. The **story name** is what people call it in the taverns.

### Steel

| Ability | Story name | Who teaches it, and its reputation |
|---|---|---|
| Heavy Hack | **Woodsman's Cut** | Every axe-fighter's first lesson. Canopy Rest fellers swear it's how they learned. |
| Sundering Chop | **Mail-Breaker** | Stonepass axemen. It splits mail rings, and smiths hate it. |
| Bearded Hook | **The Hook** | A Reaver trick: drag a fleeing man back by the shoulder. John Brokenose is the master of it. |
| Long Thrust | **The Long Reach** | Reedwatch spearmen, who learned it holding the fords. John Little is said to reach "a man and a half". |
| Brace for Charge | **Set the Spear** | Garrison drill against boar and horse alike. |
| Shaft Sweep | **Clear the Shaft** | The spearman's answer to a man who gets too close. |
| Heart-Skewer | **The Heart-Thrust** | Master spear-work. Folk say only three living people can do it cleanly. |
| Crushing Swing | **The Maul** | Stonepass hammer drill. Sir John Ironhand earned his name with it. |
| Bell-Ringer | **Ring the Bell** | "Give them to the stone": the hammer blow that slams a man into a wall. |
| Plate-Cracker | **Cracking the Shell** | What a hammer does to a knight. Lords dislike how cheap it makes their armour. |
| Cataclysmic Anvil | **The Anvil** | Named for the butte. The finishing blow of a hammer master. |
| Passive Guard | **The Guard** | The first thing a shield-bearer learns: face the danger. |
| Deflect Barrage | **Catch the Arrows** | Escort guards on the caravan roads, who stand between archers and the carts. |
| Pommel Strike | **The Pommel** | A duellist's insult: stopping a mage's spell with the hilt. Thomas Fox's favourite. |

### Bow

| Ability | Story name | Who teaches it |
|---|---|---|
| Deadeye Double-Tap | **Two from the Ridge** | Tower wardens, who shoot from the beacon platforms |
| Momentum Shot | **Running Shot** | Dust Riders and scouts who shoot from the move |
| Jaw Snare | **The Jaw Trap** | Poachers like John Shortknife and the hunting lodges. Lords' hunts outlaw it. |
| Trophy Popper | **Taking the Trophy** | Hunters' Lodge custom: the killing shot on a snared beast |
| Heartseeker Snipe | **The Heartseeker** | Legendary long shot. Agnes atte Green claims it; nobody has seen it. |
| Bramble Shot | **Bramble Arrows** | Canopy Rest rangers, who shoot thorn-coated shafts into the road |
| Houndmaster's Whistle | **The Whistle** | Westwatch's hound-masters, whose dogs come running out of nowhere |
| Watchman's Flare | **Beacon Arrow** | Tower wardens: a burning arrow that lights the field. It's what Walter Underhill fired the night he died. |
| Point-Blank Repel | **Push-Off** | Wardens' close-quarters shot |
| Iron Rain Barrage | **Iron Rain** | Garrison volleys from the walls during a siege |
| Evasive Sidestep | **The Scout's Step** | Desert scouts, who step aside rather than leap |
| Windrunner's Rhythm | **The Wind's Rhythm** | A scout's trance, whispered about around Dust Rider fires |

### Arcane

| Ability | Story name | Who teaches it |
|---|---|---|
| Mind-Snap Counter | **Snapping the Thread** | The tower school's first defensive lesson: break another mage's spell |
| Cataclysmic Collapse | **The Gathering Dark** | A forbidden pull-and-burst. The tower school bans it, and Juliana the Warlock teaches it. |
| Tempest Conduit | **The Storm Ring** | Wanderers of the fens, where the leylines run through water |
| Petrifying Gaze | **Stone-Eye** | Hermit lore. Old women in the hills say a hermit's look can stop your heart. |
| Imperial Decree | **The Court Voice** | Court mages: Dame Matilda's command spell that sharpens a lord's men |
| Soul Tether | **The Tether** | Court mages' cruellest spell: link two enemies, and what hurts one hurts the other |
| Harmonic Overcharge | **The Leyline Beam** | Master Arcane. Only possible inside a stone circle's reach, folk say. |

### Faith

| Ability | Story name | Who teaches it |
|---|---|---|
| Sacred Blessing | **The Blessing of the Blade** | Temple priests who bless weapons before a fight |
| Triage Surge | **The Quick Mercy** | Infirmarians like Sister Agnes of Reedwatch, who heal in the time it takes to kneel |
| Sanctuary of Renewal | **Sanctuary** | The hospitallers of the wayside hospices |
| Wayfarer's Second Wind | **Second Wind** | Pilgrims' prayer for the road |
| Warding Vigil | **The Vigil** | Anchorites. Mother Alice has kept one vigil for twenty years. |
| Chains of Penance | **Penance Chains** | Flagellant-trained anchorites, who bind a charging enemy |
| Keep's Unbroken Dome | **The Keep's Dome** | The old Steward ward that held the Rim. Now known only to the shrine. |

### Class and minor techniques

| Ability | Story name | Who uses it |
|---|---|---|
| Taunting Shout | **The Challenge** | Guardsmen and lords' heroes: "Face *me*!" |
| Brace the Line | **Hold the Line** | Garrison sergeants' shield-drill |
| Bastion Standard | **Raise the Standard** | A lord's banner planted in battle. Each hold's standard is a sacred object. |
| Riposte Stance | **The Duellist's Stance** | Duellists; Margaret Young taught Thomas Fox |
| Disarming Slash | **The Disarm** | Duellists' humiliation of a lesser blade |
| Grand Duel | **The Ring** | A formal duel circle: lords' heroes settle disputes this way |
| Mercenary War Cry | **The Company Cry** | Each free company has its own (the Grey Company's is silence) |
| Blood Money Cleave | **Blood Money** | Sellswords who fight harder when hurt, for the bonus pay |
| Unstoppable Rampage | **Red Rage** | Iron Reaver berserkers |
| Hamstring Ambush | **The Hamstring** | Highwaymen's trick, the Halfpenny family's speciality |
| Dirty Sand / Caltrops | **Sand and Spikes** | Highwaymen and toll bandits at the ford |
| Cutthroat Execute | **The Cutthroat** | Hollow Knives, the assassins |
| Fen-Strider's Grace | **The Fen-Walk** | Fen Walkers of Reedwatch |
