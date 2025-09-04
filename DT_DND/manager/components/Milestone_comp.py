import q
from Sheet.get import *

def gen_abil(name: str):
    an, tn = name, name.replace(" ", "_")
    return an, tn 


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
    
class bMilestone():
    def __init__(self):
        self.Upd()

    def set_all(self):
        self.Atr = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.Speed = {"Walk": 0, "Climb": 0, "Swim": 0, "Fly": 0, "Burrow": 0}
        self.Vision = {"Dark": 0, "Blind": 0, "Tremor": 0, "Tru": 0}
        self.Skill = []
        self.Weapon = []
        self.Armor = []
        self.Tool = []
        self.Lang = []
        self.Initiative = 0
        self.HP = 0
        self.SavingThrow = []

    def Upd(self):
        self.Count()
        self.Clear()
        self.Create()

    def Count(self):
        num = dict_Feat_Count[q.db.Core.C][q.db.Core.L]
        if q.db.Core.SR in race_bonus_Feat_L:
            num += 1
        q.pc.milestone_count = num

    def Clear(self):
        count = q.pc.milestone_count
        cdata = q.db.Milestone
        
        for i in range(count, len(cdata["Select"])):
            cdata["Select"][i] = ""
            cdata["Feat"][i] = ""
            cdata["Asi"][i] = ["", ""]
        current_feats = set(cdata["Feat"])
        for attr in list(vars(q.pc)):
            if attr.startswith("Feat_"):
                feat = attr[5:]
                if feat not in current_feats: delattr(q.pc, attr)
        for key in list(cdata["Data"].keys()):
            if key not in cdata["Feat"]: cdata["Data"].pop(key)
        self.set_all()
    
    
    def Create(self):
        for feat in q.db.Milestone["Feat"]:
            if feat: setattr(q.pc, f"Feat_{feat.replace(' ', '')}", globals()[feat.replace(' ', '')](self))


    def select_atr(self, name):
        select = q.db.Milestone["Data"][name]["Select"][0]
        if select: self.Atr[select] += 1


class Empty():
    def __init__(self, p):
        pass
        
class Actor():
    def __init__(self, p):
        p.Atr["CHA"] += 1

class Alert():
    def __init__(self, p):
        p.Initiative += 5

class Athlete():
    def __init__(self, p):
        _ ,feat = gen_abil("Athlete") 
        Fselect_1(feat, 1)
        p.select_atr(feat)


class Charger():
    def __init__(self, p):
        pass        

class Crossbow_Expert():
    def __init__(self, p):
        pass
    
class classensive_Duelist():
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
        p.Atr["CON"] += 1

class Elemental_Adept():
    def __init__(self, p):
        _ ,feat = gen_abil("Elemental Adept") 
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
        p.Atr["STR"] += 1
        p.Armor.extend(["Heavy"])

class Heavy_Armor_Master():
    def __init__(self, p):
        p.Atr["STR"] += 1

class Inspiring_Leader():
    def __init__(self, p):
        pass
class Keen_Mind():
    def __init__(self, p):
        p.Atr["INT"] += 1

class Lightly_Armored():
    def __init__(self, p):
        _ ,feat = gen_abil("Lightly Armored") 
        p.Armor.extend(["Light"])
        Fselect_1(feat, 1)
        p.select_atr(feat)

class Lucky():
    def __init__(self, p):
        _ ,feat = gen_abil("Lucky") 
        Fuse_1(feat, 3)

class MageSlayer():
    def __init__(self, p):
        pass
class MediumArmorMaster():
    def __init__(self, p):
        pass
class Mobile():
    def __init__(self, p):
        p.Speed["Walk"] += 10

class Moderately_Armored():
    def __init__(self, p):
        _ ,feat = gen_abil("Moderately_Armored") 
        p.Armor.extend(["Medium", "Shield"])
        Fselect_1(feat, 1)
        p.select_atr(feat)

class Mounted_Combatant():
    def __init__(self, p):
        pass
class Polearm_Master():
    def __init__(self, p):
        pass
class Resilient():
    def __init__(self, p):
        _ ,feat = gen_abil("Resilient") 
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
        p.HP += q.db.Core.L * 2

class War_Caster():
    def __init__(self, p):
        pass
class Weapon_Master():
    def __init__(self, p):
        _ ,feat = gen_abil("Weapon Master") 
        Fselect_1(feat, 4)
        collection = []
        for i in q.db.Milestone["Data"][feat]["Select"]:
            if i: collection.append(i)
            p.Weapon.extend(collection)
