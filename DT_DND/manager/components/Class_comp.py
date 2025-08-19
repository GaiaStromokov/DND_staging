import q
import Sheet.get as g
from colorist import *


def Fgen(name): q.db.Class.Abil.setdefault(name, {})
    
    
def Fuse_1(name, num):
    cdata = q.db.Class.Abil
    cdata.setdefault(name, {})
    past = cdata.get(name, {}).get("Use", [False])
    cdata[name]["Use"] = (past + [False] * num)[:num]

def Fselect_1(name, num):
    cdata = q.db.Class.Abil
    cdata.setdefault(name, {})
    past = cdata.get(name, {}).get("Select", [])
    cdata[name]["Select"] = (past + [""] * num)[:num]

def remove_ability(name): q.db.Class.Abil.pop(name, None)




class bClass():
    def __init__(self):
        
        self.Atr = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.Skill = []
        self.Weapon = []
        self.Armor = []
        self.Tool = []
        self.Lang = []
        self.Initiative = 0
        self.HP = 0
        self.HD = 0
        
        self.spell_data = {
            "Caster": "",
            "max_spell_level": 0,
            "cantrips_available": 0,
            "spells_available": 0,
            "slots": [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
            "abil": "",
            "dc": 0,
            "mod": 0,
            "atk": "",
            "prepared_available": 0,
            
        }
        
        if q.db.Core.C: self.cClass = globals()[q.db.Core.C](self)
        if q.db.Core.SC: self.cSubclass = globals()[f"{q.db.Core.C}_{q.db.Core.SC}"](self)


        
        
    def pre_Upd(self):
        self.cClass.pre_Upd()
        if q.db.Core.SC: self.cSubclass.pre_Upd()
        
        
    def Upd(self):
        self.cClass.Upd()
        if q.db.Core.SC: self.cSubclass.Upd()
    
    def Spell_config(self):      
        if q.db.Core.SC in g.list_Spellcast: self.cSubclass.Spell_config()
        elif q.db.Core.C in g.list_Spellcast: self.cClass.Spell_config()
        

    def __repr__(self):
        return str(self.__dict__)



    
    
class Empty():
    def __init__(self, p): pass
    def pre_Upd(self): pass
    def Upd(self): pass
    
class Fighter():
    def __init__(self, p):
        self.p = p
        p.HD = 10
        p.Armor.extend(q.w.search(Tier = 0, Slot="Armor"))
        p.Armor.extend(q.w.search(Tier = 0, Slot="Shield"))
        p.Weapon.extend(q.w.search(Tier = 0, Slot="Weapon"))
        
    def pre_Upd(self):
        skill_list = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
        past = q.db.Class["Skill Select"]
        q.db.Class["Skill Select"] = ([s for s in past if s in skill_list and s != ""] + ["", ""])[:2]



    def Upd(self):
        level = q.db.Core.L
        if level >= 1:
            Fselect_1("Fighting Style", 1)
            Fuse_1("Second Wind", g.Fighter_Second_Wind_Use[level])
        else:
            remove_ability("Fighting Style")
            remove_ability("Second Wind")
        if level >= 2: Fuse_1("Action Surge", g.Fighter_Action_Surge_Use[level])
        else: remove_ability("Action Surge")
        if level >= 5: Fgen("Extra Attack")
        else: remove_ability("Extra Attack")
        if level >= 9: Fuse_1("Indomitable", g.Fighter_Indomitable_Use[level])
        else: remove_ability("Indomitable")
        


class Fighter_Champion():
    def __init__(self, p):
        pass
    def pre_Upd(self):
        pass
    def Upd(self):
        level = q.db.Core.L
        if level >= 3: Fgen("Improved Critical")
        else: remove_ability("Improved Critical")
        if level >= 7: Fgen("Remarkable Athlete")
        else: remove_ability("Remarkable Athlete")
        if level >= 10: Fselect_1("Fighting Style", 2)
        if level >= 15:
            remove_ability("Improved Critical")
            Fgen("Superior Critical")
        else: remove_ability("Superior Critical")
        if level >= 18: Fgen("Survivor")
        else: remove_ability("Survivor")

class Fighter_BattleMaster():
    def __init__(self, p):
        pass
    def pre_Upd(self):
        if q.db.Core.L >= 3:
            Fselect_1("Student of War", 1)
            selected_tool = q.db.Class.Abil["Student of War"].get("Select", [""])[0]
            if selected_tool and selected_tool not in q.db.Prof["Class"]["Tool"]:
                self.Tool = [selected_tool]
        else:
            remove_ability("Student of War")
    def Upd(self):
        level = q.db.Core.L
        if level >= 3:
            Fuse_1("Combat Superiority", g.Fighter_Combat_Superiority_Use[level])
            Fselect_1("Combat Superiority", g.Fighter_Combat_Superiority_Select[level])
            
            Fgen("Relentless")
        else:
            remove_ability("Combat Superiority")
            remove_ability("Relentless")

class Fighter_EldrichKnight():
    def __init__(self, p):
        self.p = p
    def pre_Upd(self):
        pass
    def Upd(self):
        level = q.db.Core.L
        if level >= 3: Fgen("Weapon Bond")
        else: remove_ability("Weapon Bond")
        if level >= 7: Fgen("War Magic")
        else: remove_ability("War Magic")
        if level >= 10: Fgen("Eldrich Strike")
        else: remove_ability("Eldrich Strike")
        if level >= 15: Fgen("Arcane Charge")
        else: remove_ability("Arcane Charge")
        if level >= 18:
            remove_ability("War Magic")
            Fgen("Improved War Magic")
        else: remove_ability("Improved War Magic")
        
    def Spell_config(self):
        cspell=self.p.spell_data
        level = q.db.Core.L
        pb = q.db.Core.PB
        Class = "Eldrich Knight"
        abil = g.casting_abil[Class]
        
        cspell["Caster"] = g.casting_class[Class]
        cspell["max_spell_level"] = g.max_spell_Level[Class][level]
        cspell["cantrips_available"] = g.cantrips_available[Class][level]
        cspell["spells_available"] = g.spells_available[Class][level]
        cspell["abil"] = abil
        cspell["slots"] = g.spell_slots[Class][level]
        cspell["mod"] = q.db.Atr[abil]["Mod"]
        mod = cspell["mod"]
        cspell["atk"] = f"{'+' if (pb + mod) >= 0 else ''}{pb + mod}"

        cspell["dc"] = 8 + pb + mod
        cspell["prepared_available"] = mod + q.db.Core.L
        
        past = q.db.Spell["Slot"]
        for index,val in enumerate(cspell["slots"]):
            q.db.Spell.Slot[index] = (past[index] + [False] * val)[:val]

class Fighter_Samuri():
    def __init__(self, p):
        pass
    def pre_Upd(self):
        if q.db.Core.L >= 3:
            Fselect_1("Bonus Proficiency", 1)
            select = q.db.Class.Abil["Bonus Proficiency"].get("Select", [""])[0]
            if select and select not in q.db.Skill["Class"]:
                self.Skill = [select]
        else:
            remove_ability("Bonus Proficiency")
    def Upd(self):
        level = q.db.Core.L
        if level >= 3: Fuse_1("Fighting Spirit", 3)
        else: remove_ability("Fighting Spirit")
        if level >= 7: Fgen("Elegant Courtier")
        else: remove_ability("Elegant Courtier")
        if level >= 10: Fgen("Tireless Spirit")
        else: remove_ability("Tireless Spirit")
        if level >= 15: Fgen("Rapid Strike")
        else: remove_ability("Rapid Strike")
        if level >= 18: Fuse_1("Strength before Death", 1)
        else: remove_ability("Strength before Death")



class Wizard():
    def __init__(self, p):
        self.p = p
        self.p.HD = 6
        self.p.Weapon.extend(["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"])

    def pre_Upd(self):
        skill_list = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
        past = q.db.Class["Skill Select"]
        q.db.Class["Skill Select"] = ([s for s in past if s in skill_list and s != ""] + ["", ""])[:2]


        
    def Spell_config(self):
        cspell = self.p.spell_data
        level = q.db.Core.L
        pb = q.db.Core.PB
        Class = "Wizard"
        abil = g.casting_abil[Class]
        
        cspell["Caster"] = g.casting_class[Class]
        cspell["max_spell_level"] = g.max_spell_Level[Class][level]
        cspell["cantrips_available"] = g.cantrips_available[Class][level]
        cspell["spells_available"]= level * 2
        cspell["slots"] = g.spell_slots[Class][level] 
        cspell["abil"] = abil
        cspell["mod"] = q.db.Atr[abil]["Mod"]
        mod = cspell["mod"]
        cspell["atk"] = f"{'+' if (pb + mod) >= 0 else ''}{pb + mod}"

        cspell["dc"] = 8 + pb + mod
        cspell["prepared_available"] = mod + level
        
        past = q.db.Spell["Slot"]
        for index,val in enumerate(cspell["slots"]): q.db.Spell.Slot[index] = (past[index] + [False] * val)[:val]
    def Upd(self):
        level = q.db.Core.L
        if level >=1:
            Fgen("Spellcasting")
            Fuse_1("Arcane Recovery", 1)
        else:
            remove_ability("Spellcasting")
            remove_ability("Arcane Recovery")
        if level >=18:
            Fuse_1("Spell Mastery", 2)
            Fselect_1("Spell Mastery", 2)
        else:
            remove_ability("Spell Mastery")
        if level >=20:
            Fuse_1("Signature Spells", 2)
            Fselect_1("Signature Spells", 2)
        else:
            remove_ability("Signature Spells")


class Wizard_Abjuration():
    def __init__(self, p):
        pass
    def pre_Upd(self):
        pass
    def Spell_config(self):
        pass
    def Upd(self):
        level = q.db.Core.L
        if level >= 2:
            Fgen("Abjuration Savant")
            
            ab_ward = Fgen("Arcane Ward")
            ward_max_hp = level + q.db.Atr["INT"]["Mod"]
            ward_current_hp = ab_ward.get("HP", {}).get("Current", ward_max_hp)
            ab_ward["HP"] = {"Max": ward_max_hp, "Current": ward_current_hp}
            Fuse_1("Arcane Ward", 1)
        else:
            remove_ability("Abjuration Savant")
            remove_ability("Arcane Ward")
        if level >= 6: Fgen("Projected Ward")
        else: remove_ability("Projected Ward")
        if level >= 10: Fgen("Improved Abjuration")
        else: remove_ability("Improved Abjuration")
        if level >= 14: Fgen("Spell Resistance")
        else: remove_ability("Spell Resistance")

class Wizard_Conjuration():
    def __init__(self, p):
        pass
    def pre_Upd(self):
        pass
    def Spell_config(self):
        pass
    def Upd(self):
        level = q.db.Core.L
        if level >= 2:
            Fgen("Conjuration Savant")
            Fgen("Minor Conjuration")
            
        else:
            remove_ability("Conjuration Savant")
            remove_ability("Minor Conjuration")
        if level >= 6: Fuse_1("Benign Transportation", 1)
        
        else: remove_ability("Benign Transportation")
        
        if level >= 10: Fgen("Focused Conjuration")
        
        else: remove_ability("Focused Conjuration")
            
        if level >= 14: Fgen("Durable Summons")
        
        else: remove_ability("Durable Summons")

