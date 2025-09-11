import q
from Sheet.get import *

def tgen(name: str):
    tn = name.replace(" ", "_")
    return tn 


dict_Feat_Count = {
    'Empty': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Fighter': [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7],
    'Rogue': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6],
    'Wizard': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Ranger': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Paladin': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]
}
race_bonus_Feat_L = ["Variant"]


def Fselect_1(name, num):
    past = q.db.Milestone["Data"].get(name, {}).get("Select", [])
    q.db.Milestone["Data"][name]["Select"] = (past + [""] * num)[:num]

def Fuse_1(name, num):
    past = q.db.Milestone["Data"].get(name, {}).get("Use", [])
    q.db.Milestone["Data"][name]["Use"] = (past + [False] * num)[:num]

def Add_Stat(name, val):
    q.dbm.Stats.M.Atr[name] += val

def Add_Init(val):
    q.dbm.Stats.M.Combat.Initiative += val

def Add_Weapon(items):
    q.dbm.Stats.M.Prof.Weapon.extend(items)
def Add_Armor(items):
    q.dbm.Stats.M.Prof.Armor.extend(items)

def Add_HP(val):
    q.dbm.Stats.M.Combat.HP += val

def Add_Speed(cat, val):
    q.dbm.Stats.M.Speed[cat] += val

def Select_Atr(name):
    select = q.db.Milestone["Data"][name]["Select"][0]
    if select: q.dbm.Stats.Atr[select] += 1
    
class bMilestone():
    def __init__(self):
        self.Upd()


    def Upd(self):
        self.Count()
        self.Clear()
        self.Create()

    def Count(self):
        num = dict_Feat_Count[q.dbm.Core.g.C][q.dbm.Core.g.L]
        if q.dbm.Core.g.SR in race_bonus_Feat_L:
            num += 1
        q.dbm.milestone_count = num

    def Clear(self):
        count = q.dbm.milestone_count
        cdata = q.db.Milestone
        parent = q.dbm.Milestone.Data

        for i in range(count, len(cdata["Select"])):
            cdata["Select"][i] = ""
            cdata["Feat"][i] = ""
            cdata["Asi"][i] = ["", ""]
        current_feats = set(cdata["Feat"])
        for attr in list(vars(parent)):
            if attr.startswith("Feat_"):
                feat = attr[5:]
                if feat not in current_feats:
                    delattr(parent, attr)
        for key in list(cdata["Data"].keys()):
            if key not in current_feats:
                cdata["Data"].pop(key)
        q.dbm.Milestone.Reset

    
        
    def Create(self):
        for feat in q.db.Milestone["Feat"]:
            if feat:
                name = feat.replace(' ', '_')
                setattr(q.dbm.Milestone.Data, f"Feat_{name}", globals()[name](self))






class Empty():
    def __init__(self, p):
        pass
        
class Actor():
    def __init__(self, p):
        Add_Stat("CHA", 1)

class Alert():
    def __init__(self, p):
        Add_Init(5)

class Athlete():
    def __init__(self, p):
        feat = tgen("Athlete") 
        Fselect_1(feat, 1)
        Select_Atr(feat)


class Charger():
    def __init__(self, p):
        pass        

class Crossbow_Expert():
    def __init__(self, p):
        pass
    
class Defensive_Duelist():
    def __init__(self, p):
        pass
class Dual_Wielder():
    def __init__(self, p):
        pass
    
class Dungeon_Delver():
    def __init__(self, p):
        pass
    
class Durable():
    def __init__(self, p):
        Add_Stat("CON", 1)

class Elemental_Adept():
    def __init__(self, p):
        feat = tgen("Elemental Adept") 
        Fselect_1(feat, 1)

class Grappler():
    def __init__(self, p):
        pass
class Great_Weapon_Master():
    def __init__(self, p):
        pass
class Healer():
    def __init__(self, p):
        pass
class HeavilyArmored():
    def __init__(self, p):
        Add_Stat("STR", 1)
        Add_Armor(["Heavy"])

class Heavy_Armor_Master():
    def __init__(self, p):
        Add_Stat("STR", 1)

class Inspiring_Leader():
    def __init__(self, p):
        pass
class Keen_Mind():
    def __init__(self, p):
        Add_Stat("STR", 1)

class Lightly_Armored():
    def __init__(self, p):
        feat = tgen("Lightly Armored") 
        Add_Armor(["Light"])
        Fselect_1(feat, 1)
        Select_Atr(feat)

class Lucky():
    def __init__(self, p):
        feat = tgen("Lucky") 
        Fuse_1(feat, 3)

class MageSlayer():
    def __init__(self, p):
        pass
class MediumArmorMaster():
    def __init__(self, p):
        pass
class Mobile():
    def __init__(self, p):
        Add_Speed("Walk", 10)

class Moderately_Armored():
    def __init__(self, p):
        feat = tgen("Moderately_Armored") 
        Add_Armor(["Medium", "Shield"])
        Fselect_1(feat, 1)
        Select_Atr(feat)

class Mounted_Combatant():
    def __init__(self, p):
        pass
class Polearm_Master():
    def __init__(self, p):
        pass
class Resilient():
    def __init__(self, p):
        feat = tgen("Resilient") 
        Fselect_1(feat, 1)

class Savage_Attacker():
    def __init__(self, p):
        pass
class Sentinel():
    def __init__(self, p):
        pass
class Sharpshooter():
    def __init__(self, p):
        pass
class Shield_Master():
    def __init__(self, p):
        pass
class Skulker():
    def __init__(self, p):
        pass
class Tavern_Brawler():
    def __init__(self, p):
        pass
class Tough():
    def __init__(self, p):
        Add_HP(q.dbm.Core.g.L * 2)


class War_Caster():
    def __init__(self, p):
        pass
class Weapon_Master():
    def __init__(self, p):
        feat = tgen("Weapon Master") 
        Fselect_1(feat, 4)
        collection = []
        for i in q.db.Milestone["Data"][feat]["Select"]:
            if i: collection.append(i)
        Add_Weapon(collection)
