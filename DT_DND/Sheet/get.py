# get.py
import q
from access_data.color_reference import *
from colorist import *
from access_data.Grimoir import *


# # Core values
def Level(): return q.db.Core.L
def PB(): return q.db.Core.PB
def Race(): return q.db.Core.R.replace(" ", "")
def Subrace(): return q.db.Core.SR.replace(" ", "")
def Class(): return q.db.Core.C.replace(" ", "")
def Subclass(): return q.db.Core.SC.replace(" ", "")
def Background(): return q.db.Core.BG.replace(" ", "")

# # Core Setters


# # Core Data get
def dClass(): return q.db.Class
def dRace(): return q.db.Race
def dBackground(): return q.db.Background

# # Core Abil get
def aClass(): return q.db.Class["Abil"]
def aRace(): return q.db.Race["Abil"]

# # Core Skill get
def sClass(): return q.db.Class["Skill Select"]


# def kMilestone(): return q.db.Milestone
# def kProf(): return q.db.Prof
# def kSkill(): return q.db.Skill
# def kAC(): return q.db.AC
# def kSpeed(): return q.db.Speed
# def kVision(): return q.db.Vision
# def kInitiative(): return q.db.Initiative
def kHP(): return q.db.HP
# def q.db.Condition: return q.db.Condition
def dAtr(): return q.db.Atr
# def kSavingthrow(): return q.db.SavingThrow
# def q.db.Spell: return q.db.Spell
# def q.db.Characteristic: return q.db.Characteristic
# def q.db.Description: return q.db.Description
# def kBackpack(): return q.db.Inventory.Backpack
# def kEquip(): return q.db.Inventory.Equip



# def pProf(): return q.pc.Prof

# def pSpeed(): return q.pc.Speed
# def pVision(): return q.pc.Vision
# def pInitiative(): return q.pc.Initiative
# def pAtr(): return q.pc.Atr

def aMod(atr): return q.db.Atr[atr]["Mod"]

# def cMilestone(): return q.pc.milestone_count

# def q.pc.spell_data: return q.pc.spell_data

# def Current_Equip(slot): return kEquip()[slot]
# def Current_Backpack(): return list(q.db.Inventory.Backpack.keys())

# def dBackpack(): return q.db.Inventory.Backpack

# def bMult_Category(*categories): return q.pc.Bazaar.Mult_Category(*categories)

# def bCategory(category): return q.pc.Bazaar.Category(category)

# def bSlot(slot): return q.pc.Bazaar.Slot(slot)

# def bProf(prof): return q.pc.Bazaar.Prof(prof)

# def q.w.prop(prop): return q.pc.Bazaar.Property(prop)

# def bItem(item): return q.pc.Bazaar.Item(item)


# def bOffHand(): return q.pc.Bazaar.OffHand



def Initiative_text():
    mod = q.pc.Initiative
    return f"{'+' if mod >= 0 else '-'}{abs(mod)}"


# Spell bullshit
def cantrips_known(): return len(q.db.Spell.Book[0])




def spells_known():
    cdata = q.db.Spell.Book
    num = 0
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        num += len(cdata[i])
    return num


def spells_prepared():
    cdata = q.db.Spell.Prepared
    num = 0
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        num += len(cdata[i])
    return num


def valid_class():
    cdata = q.db.Core
    class_exception_map = {1: ["Cleric", "Warlock"], 2: ["Wizard"]}
    return cdata.L >= 3 or cdata.C in class_exception_map.get(cdata.L, [])

def valid_spellclass(): return q.db.Core.C in list_Spellcast or q.db.Core.SC in list_Spellcast

def valid_s_spellclass(cat):
    cdata = q.db.Core
    if cat == "Class":
        return cdata.C in list_Spellcast
    elif cat == "Subclass":
        return cdata.SC in list_Spellcast





def prof_color( cat, item): return c_item_true if item in q.pc.Prof[cat] else c_item_false


def condition_color( item): return c_item_true if q.db.Condition[item] else c_item_false


def skill_text( skill):
    mod = q.db.Skill[skill]["Mod"]
    return f"{'+' if mod >= 0 else '-'}{abs(mod)}"


# def dc_val( atr):
#     return 8 + kAtr()[atr]["Mod"] + vPB()




def same_weapon():
    cdata = q.db.Inventory.Equip
    main_hand = cdata["Hand_1"]
    off_hand = cdata["Hand_2"]
    if main_hand == off_hand: return True
    else: return False
    
def weapon_versatile():
    cdata = q.db.Inventory.Equip
    clist = q.w.prop("Versatile")
    main_hand = cdata["Hand_1"]
    off_hand = cdata["Hand_2"]

    if main_hand == off_hand:
        if main_hand in clist: return True
        else: return False
    else: return False



def get_Fighting_Style( Style):
    item_map = {
        "Archery": "You gain a +2 bonus to attack rolls you make with ranged weapons.",
        "Defense": "While you are wearing armor, you gain a +1 bonus to AC.",
        "Dueling": "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
        "Great Weapon Fighting": "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll. The weapon must have the two-handed or versatile property for you to gain this benefit.",
        "Protection": "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.",
        "Two Weapon Fighting": "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.",
        "Blind Fighting": "You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover.",
        "Interception": f"When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + {q.db.Core.PB}. You must be wielding a shield or a simple or martial weapon to use this reaction.",
        "Thrown Weapon Fighting": "You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.",
        "Unarmed Fighting": f"Your unarmed strikes can deal bludgeoning damage equal to 1d6 + {q.db.Atr["STR"]["Mod"]}. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you."
    }
    return item_map[Style]

dict_Maneuver_map = {
    "Ambush": "When you make a Stealth check or roll initiative, Use 1 SD and add too roll, Not available when incapacitated.",
    "Bait and Switch": "on turn, if withen 5 ft of a willing creature with more then 5t of movement, Use 1SD too switch places with the creature, this doesn't provoke OA, until the start of your next turn, you and the creature gains AC equal too roll.",
    "Brace": "When creature moves into melee reach, use reaction and 1 SD too make attack, add SD too damage.",
    "Commander's Strike": "Replace one attack with bonus action, ally you can see makes weapon attack and adds SD too damage.",
    "Commanding Presence": "Use 1 SD on Intimidation, Performance, or Persuasion checks, add too roll.",
    "Disarming Attack": "On hit, use 1 SD, add too damage, target makes STR save or drops item.",
    "Distracting Strike": "On hit, use 1 SD, add too damage, next ally attack has advantage.",
    "Evasive Footwork": "When moving, use 1 SD and add too AC until you stop.",
    "Feinting Attack": "Bonus action, use 1 SD too gain advantage on next attack, add SD too damage if hit.",
    "Goading Attack": "On hit, use 1 SD, add too damage, target makes WIS save or has disadvantage attacking others.",
    "Grappling Strike": "After melee hit, use 1 SD and bonus action too grapple, add SD too Athletics check.",
    "Lunging Attack": "Use 1 SD too increase melee reach by 5 ft, add too damage if hit.",
    "Maneuvering Attack": "On hit, use 1 SD, add too damage, ally moves half speed without provoking OA from target.",
    "Menacing Attack": "On hit, use 1 SD, add too damage, target makes WIS save or frightened until next turn.",
    "Parry": "When hit by melee attack, use reaction and 1 SD too reduce damage by roll + DEX mod.",
    "Precision Attack": "Use 1 SD too add too attack roll before or after rolling.",
    "Pushing Attack": "On hit, use 1 SD, add too damage, Large or smaller makes STR save or pushed 15 ft.",
    "Quick Toss": "Bonus action, use 1 SD too make thrown weapon attack, add too damage if hit.",
    "Rally": "Bonus action, use 1 SD, ally gains temp HP equal too roll + CHA mod.",
    "Riposte": "When enemy misses melee attack, use reaction and 1 SD too attack back, add too damage.",
    "Sweeping Attack": "On melee hit, use 1 SD, second creature within 5 ft takes SD damage if original roll hits.",
    "Tactical Assessment": "Use 1 SD on Investigation, History, or Insight checks, add too roll.",
    "Trip Attack": "On hit, use 1 SD, add too damage, Large or smaller makes STR save or knocked prone."
}


    

class weapon_action_sc:
    def __init__(self, item):
        item_data = q.w.Item(item)
        tier = item_data.Tier
        
        mod = self._gam(item)
        prof_bonus = q.db.Core.PB if item in q.db.Prof["Weapon"] else 0
        
        self.Name = iName(item)
        self.Range = " : ".join(f"{v} ft" for v in (item_data.get("Reach"), item_data.get("Range")) if v)
        
        self.hNum = mod + prof_bonus + tier
        self.hSign = "+" if self.hNum >= 0 else "-"
        self.hColor = c_weapon_hit(self.hNum)
        
        self.dNum = mod + tier
        self.dSign = "+" if self.dNum >= 0 else "-"
        self.dColor = c_weapon_dmg(self.dNum)
        
        self.dDice = item_data.vDamage if weapon_versatile() else item_data.Damage
        self.dType = item_data.Type
        self.Prop = item_data.Prop

    def _gam(self, item):
        str_mod = q.db.Atr["STR"]["Mod"]
        dex_mod = q.db.Atr["DEX"]["Mod"]
        if item in q.w.prop("Finesse"): return max(str_mod, dex_mod)
        if item in q.w.cat("Melee"): return str_mod
        if item in q.w.cat("Ranged"): return dex_mod
        return 0
# class s_item:
#     def __init__(self, item_name):
#         pass
#     #     item_data = items.get(item_name)
#     #     self.Name = item_name
#     #     for key, value in item_data.items():setattr(self, key, value)
#     # def __repr__(self):return f"s_item({', '.join(f'{k}={repr(v)}' for k, v in self.__dict__.items())})"
#     # def get(self, key, default=None):return getattr(self, key, default)


lnRarity = [0,1,2,3,4]

def item_rarity(tier):
    return ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"][tier]

def isName(item):
    return item.replace('_', ' ').replace('PPP1', '').replace('PPP2', '').replace('PPP3', '')

def iName(item):
    return item.replace('_', ' ').replace('PPP', ' + ')

def pName(item):
    return item.replace('_', ' ')

# def Lprof(parent, cat):
#     return False #pc[parent][cat] + kProf()[cat][parent]

# # ANCHOR - DB Getters

# def gCore(): return q.db.Core


# # ----------------
# # SECTION - SET 
# # ----------------


#-----------------------------------------------------------
#ANCHOR - BOOK
option_Race = {
    "Empty": ["Empty"],
    "Human": ["Standard", "Variant"],
    "Elf": ["High", "Drow", "Wood", "Shadar Kai"],
    "Dwarf": ["Hill", "Mountain"],
    "Halfling": ["Lightfoot", "Stout"],
    "Gnome": ["Forest", "Rock"],
    "Dragonborn": ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold","Green","Red","Silver","White"],
    "Half Orc": ["Standard"],
    "Tiefling": ["Asmodeus","Baalzebul", "Dispater", "Fierna", "Glasya", "Levistus", "Mammon", "Mephistopheles", "Zariel"],
    "Harengon": ["Standard"]
}

option_Class = {
    "Empty": ["Empty"],
    "Fighter": ["Champion", "Battle Master", "Eldrich Knight", "Samuri"],
    "Wizard": ["Abjuration", "Conjuration"] # "Enchantment", "Evocation", "Illusion", "Necromancy" 
}

list_Race = list(option_Race.keys())
list_Class = list(option_Class.keys())
list_Background = ["Empty", "Charlatan","Criminal","Entertainer","Folk Hero","Guild Artisan","Hermit","Noble","Outlander","Sage","Sailor","Soldier","Urchin"]
list_Spellcast = ["Wizard", "Eldrich Knight"]
list_Feat = ["Empty", "Actor", "Alert", "Athlete", "Charger", "Crossbow Expert", "Defensive Duelist", "Dual Wielder", "Dungeon Delver", "Durable", "Elemental Adept", "Grappler", "Great Weapon Master", "Healer", "Heavily Armored", "Heavy Armor Master", "Inspiring Leader", "Keen Mind", "Lightly Armored", "Lucky", "Mage Slayer", "Martial Adept", "Medium Armor Master", "Mobile", "Moderately Armored", "Mounted Combatant", "Polearm Master", "Resilient", "Savage Attacker", "Sentinel", "Sharpshooter", "Shield Master", "Skulker", "Tavern Brawler", "Tough", "War Caster", "Weapon Master"]
list_Feat_Select = ["Moderately Armored","Lightly Armored","Elemental Adept","Athlete"]
list_Prof = ["Armor","Weapon","Tool","Lang"]
list_Level = list(range(1, 21))
list_Base_Atr = list(range(1, 19))
list_Atr = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
list_Description = ["Gender", "Almnt", "Faith", "Size", "Age", "Hair", "Skin", "Eyes", "Height", "Weight"]
list_Ideals = ["Traits", "Ideals", "Bonds", "Flaws"]
list_Condition = ["Blinded", "Charmed", "Deafened", "Frightened", "Grappled", "Incapacitated", "Invisible", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious", "Exhaustion"]
list_Spell_Desc = ["Level", "Casting Time", "Duration", "School", "Ritual", "Range", "Components", "Desc", "At Higher Levels"]
list_Coins = ["CP", "SP", "GP", "PP"]
# #-------
# ## LINK - #! Spells
# #-------

def spell_not_cantrip(spell_name):
    return Grimoir[spell_name]["Level"] != 0


def List_Spells(Class, level):
    return [spell for spell, v in Grimoir.items() if v['Level'] == level and Class in v['List']]


# #-------
# ## LINK - #! Class based shit
# #-------



spell_default = {
    "Slot": [[],[],[],[],[],[],[],[],[],[]],
    "Book": [[],[],[],[],[],[],[],[],[],[]],
    "Prepared": [[],[],[],[],[],[],[],[],[],[]]
}


spell_data_default = {
    "Caster": "",
    "max_spell_level": 0,
    "cantrips_available": 0,
    "spells_available": 0,
    "slots": [[],[],[],[],[],[],[],[],[],[]],
    "abil": "",
    "dc": 0,
    "mod": 0,
    "atk": "",
    "prepared_available": 0
    
}

dict_Feat_Count = {
    'Fighter': [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7],
    'Rogue': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6],
    'Wizard': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Ranger': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Paladin': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]
}



dict_Skill = {
        "Acrobatics": {"Atr": "DEX", "Desc": "Balance, flips, and avoiding being knocked down."},
        "Animal Handling": {"Atr": "WIS", "Desc": "Control and calm animals or read their behavior."},
        "Arcana": {"Atr": "INT", "Desc": "Knowledge of magic, spells, and magical traditions."},
        "Athletics": {"Atr": "STR", "Desc": "Climbing, jumping, swimming, and grappling."},
        "Deception": {"Atr": "CHA", "Desc": "Lying, bluffing, and misleading others."},
        "History": {"Atr": "INT", "Desc": "Recall historical facts, people, and events."},
        "Insight": {"Atr": "WIS", "Desc": "Detecting lies, motives, and emotions."},
        "Intimidation": {"Atr": "CHA", "Desc": "Threatening or coercing others into compliance."},
        "Investigation": {"Atr": "INT", "Desc": "Finding hidden clues or analyzing scenes."},
        "Medicine": {"Atr": "WIS", "Desc": "Stabilize the dying and diagnose illnesses."},
        "Nature": {"Atr": "INT", "Desc": "Knowledge of plants, animals, and the environment."},
        "Perception": {"Atr": "WIS", "Desc": "Noticing hidden things or sudden changes."},
        "Performance": {"Atr": "CHA", "Desc": "Acting, singing, dancing, and entertaining."},
        "Persuasion": {"Atr": "CHA", "Desc": "Convincing others with logic or charm."},
        "Religion": {"Atr": "INT", "Desc": "Understanding deities, rites, and dogma."},
        "Sleight of Hand": {"Atr": "DEX", "Desc": "Pickpocketing or manipulating objects subtly."},
        "Stealth": {"Atr": "DEX", "Desc": "Sneaking, hiding, and moving silently."},
        "Survival": {"Atr": "WIS", "Desc": "Tracking, finding food, and navigating the wild."}
    }

#ANCHOR - Speed Dict


list_spell_header = ["Cantrip", "Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9"]


# #SECTION - Prof Tool
dict_Tool = {
    "Alchemist": "Job", "Brewer": "Job", "Calligrapher": "Job", "Carpenter": "Job", "Cartographer": "Job", "Cobbler": "Job", "Cook": "Job", "Glassblower": "Job", "Jeweler": "Job", "Leatherworker": "Job", "Mason": "Job", "Painter": "Job", "Potter": "Job", "Smith": "Job", "Tinker": "Job", "Weaver": "Job", "Thief": "Job", "Woodworker": "Job", "Navigator": "Job", "Disguise": "Job", "Forgery": "Job",
    "Dice": "Game", "Dragonchess": "Game", "Cards": "Game", "Three-Dragon Ante": "Game",
    "Bagpipes": "Music", "Drum": "Music", "Dulcimer": "Music", "Flute": "Music", "Lute": "Music", "Lyre": "Music", "Horn": "Music", "Pan Flute": "Music", "Shawm": "Music", "Viol": "Music"
}

dict_Lang = {
    "Common": {},
    "Dwarvish": {},
    "Elvish": {},
    "Giant": {},
    "Gnomish": {},
    "Goblin": {},
    "Halfling": {},
    "Orc": {},
    "Abyssal": {},
    "Celestial": {},
    "Draconic": {},
    "Deep Speech": {},
    "Infernal": {},
    "Primordial": {},
    "Sylvan": {},
    "Undercommon": {}
}



# #!SECTION Data List
# Armor_L = ["Light","Medium","Heavy","Shield"]

list_Job = [k for k, v in dict_Tool.items() if v == "Job"]
list_Game = [k for k, v in dict_Tool.items() if v == "Game"]
list_Music = [k for k, v in dict_Tool.items() if v == "Music"]
list_Lang = list(dict_Lang.keys())
list_Skill = list(dict_Skill.keys())


list_Vision = ["Dark", "Blind","Tremor","Tru"]
list_Speed = ["Walk","Climb","Swim","Fly", "Burrow"]

dict_Class_Skills = {
    "Empty": [],
    "Fighter": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
    "Wizard":  ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
    }

dict_Background_Skills = {
    "Empty": {},
    "Acolyte": {"Lang": list_Lang},
    "Charlatan": {},
    "Criminal": {"Game": list_Game},
    "Entertainer": {"Music": list_Music},
    "FolkHero": {"Job":list_Job},
    "GuildArtisan": {"Job": list_Job, "Lang": list_Lang},
    "Hermit": {"Lang": list_Lang},
    "Noble": {"Game": list_Game, "Lang": list_Lang},
    "Outlander": {"Music": list_Music, "Lang": list_Lang},
    "Sage": {"Lang": list_Lang},
    "Sailor": {},
    "Soldier": {"Game": list_Game},
    "Urchin": {},
}

dict_Feat_Lists = {
    "Athlete": ["STR", "DEX"],
    "Lightly Armored": ["STR","DEX"],
    "Moderately Armored": ["STR", "DEX"],
    "Elemental Adept": ["Acid", "Cold", "Fire", "Lightning", "Thunder"],
    "Resiliant": list_Atr,
    "Weapon Master": [], #s_cat("Simple"),
}
    
list_High_Elf_Cantrip = [spell for spell, v in Grimoir.items() if v['Level'] == 0 and 'Wizard' in v['List']]

list_Fighting_Styles = ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two Weapon Fighting", "Blind Fighting", "Interception", "Thrown Weapon Fighting", "Unarmed Fighting"]
list_Maneuvers = ["Ambush", "Bait and Switch", "Brace", "Commander's Strike", "Commanding Presence", "Disarming Attack", "Distracting Strike", "Evasive Footwork", "Feinting Attack", "Goading Attack", "Grappling Strike", "Lunging Attack", "Maneuvering Attack", "Menacing Attack", "Parry", "Precision Attack", "Pushing Attack", "Quick Toss", "Rally", "Riposte", "Sweeping Attack", "Tactical Assessment", "Trip Attack"],
list_Student_of_War_Profs = list_Job
list_Fighter_Samuri_Bonus_Proficiency = ["History", "Insight", "Performance","Persuasion"]
list_weapon_attributes = ["Name", "Range", "Hit", "Damage", "Type", "Notes"]
list_equip_type = ["Weapon", "Armor","Wand", "Staff", "Rod", "Potion", "Scroll", "Ring", "Wonderous", "Other"]
Fighter_Second_Wind_Use = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Fighter_Action_Surge_Use = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2]
Fighter_Indomitable_Use = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2]

Fighter_Combat_Superiority_Use = [0,0,0,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,6]
Fighter_Combat_Superiority_Select = [0,0,0,3,3,3,3,5,5,5,7,7,7,7,7,9,9,9,9,9,9]



max_spell_Level = {
    "Wizard": [0,1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,9], 
    "Eldrich Knight": [0,0,0,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4]
}
cantrips_available = {
    "Wizard": [0,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5],
    "Eldrich Knight": [0,0,0,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3]
}

spells_available = {
    "Wizard": [],
    "Eldrich Knight": [0,0,0,3,4,4,4,5,6,6,7,8,8,9,10,10,11,11,11,12,13]
}

casting_abil = {
    "Wizard": "INT",
    "Eldrich Knight": "INT"
}

casting_class = {
    "Wizard": "Wizard",
    "Eldrich Knight": "Wizard"
}
spell_slots = {
    "Wizard": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],[0, 3, 0, 0, 0, 0, 0, 0, 0, 0],[0, 4, 2, 0, 0, 0, 0, 0, 0, 0],[0, 4, 3, 0, 0, 0, 0, 0, 0, 0],[0, 4, 3, 2, 0, 0, 0, 0, 0, 0],[0, 4, 3, 3, 0, 0, 0, 0, 0, 0],[0, 4, 3, 3, 1, 0, 0, 0, 0, 0],[0, 4, 3, 3, 2, 0, 0, 0, 0, 0],[0, 4, 3, 3, 3, 1, 0, 0, 0, 0],[0, 4, 3, 3, 3, 2, 0, 0, 0, 0],[0, 4, 3, 3, 3, 2, 1, 0, 0, 0],[0, 4, 3, 3, 3, 2, 1, 0, 0, 0],[0, 4, 3, 3, 3, 2, 1, 1, 0, 0],[0, 4, 3, 3, 3, 2, 1, 1, 0, 0],[0, 4, 3, 3, 3, 2, 1, 1, 1, 0],[0, 4, 3, 3, 3, 2, 1, 1, 1, 0],[0, 4, 3, 3, 3, 2, 1, 1, 1, 1],[0, 4, 3, 3, 3, 3, 1, 1, 1, 1],[0, 4, 3, 3, 3, 3, 2, 1, 1, 1],[0, 4, 3, 3, 3, 3, 2, 2, 1, 1]],
    "Eldrich Knight": [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,2,0,0,0],[0,3,0,0,0],[0,3,0,0,0],[0,3,0,0,0],[0,4,2,0,0],[0,4,2,0,0],[0,4,2,0,0],[0,4,3,0,0],[0,4,3,0,0],[0,4,3,0,0],[0,4,3,2,0],[0,4,3,2,0],[0,4,3,2,0],[0,4,3,3,0],[0,4,3,3,0],[0,4,3,3,0],[0,4,3,3,1],[0,4,3,3,1]]
}


inventory_equip_L = ["Face","Throat","Body","Hands","Waist","Feet","Armor","Hand_1","Hand_2","Ring_1","Ring_2"]



dict_weapon_prop = {
    "Ammunition": {"SC": "AMM", "Desc": "Requires ammo. One ammo used per attack. Half recoverable after battle."},
    "Finesse": {"SC": "FIN", "Desc": "Use either Strength or Dexterity modifier for attack and damage."},
    "Heavy": {"SC": "HVY", "Desc": "Small creatures have disadvantage due to weapon size."},
    "Light": {"SC": "LGT", "Desc": "Small and easy to handle."},
    "Loading": {"SC": "LDG", "Desc": "Can only fire one shot per action or reaction."},
    "Range": {"SC": "RNG", "Desc": "Has normal and long range. Attacks beyond normal range have disadvantage."},
    "Reach": {"SC": "REH", "Desc": "Extends melee attack range by 5 feet."},
    "Thrown": {"SC": "TRN", "Desc": "Can be thrown. Uses melee attack modifier."},
    "Two-handed": {"SC": "THD", "Desc": "Requires two hands to use."},
    "Versatile": {"SC": "VSL", "Desc": "Can be used one or two handed. Damage increases when used with two hands."}
    }

dict_weapon_dtype_description = {
    "Piercing": "Puncturing and penetrating.",
    "Slashing": "Cutting and severing.",
    "Bludgeoning": "Blunt impact and concussive force."
}


