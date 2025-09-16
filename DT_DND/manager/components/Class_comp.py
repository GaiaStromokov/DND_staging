import q
import Sheet.get as g
from box import Box
from colorist import *
db = q.db


def Fgen(name): db.Class.Abil.setdefault(name.replace(" ", "_"), {})
def Fuse_1(name, num):
    name = name.replace(" ", "_")
    cdata = db.Class.Abil
    cdata.setdefault(name, {})
    past = cdata.get(name, {}).get("Use", [False])
    cdata[name]["Use"] = (past + [False] * num)[:num]

def Fselect_1(name, num):
    name = name.replace(" ", "_")
    cdata = db.Class.Abil
    cdata.setdefault(name, {})
    past = cdata.get(name, {}).get("Select", [])
    cdata[name]["Select"] = (past + [""] * num)[:num]

def remove_ability(name): db.Class.Abil.pop(name.replace(" ", "_"), None)

def Spell_Setter(Caster):
    cSpell = g.Spell_Class_Data(Caster)
    q.dbm.dSpell = Box({
        "Caster": cSpell.CList,
        "MSL": cSpell.MSL,
        "CA": cSpell.CA,
        "SA": cSpell.SA,
        "PA": cSpell.PA,
        "Slots": cSpell.Slot,
        "Abil": cSpell.CAbil,
        "DC": cSpell.DC,
        "Mod": cSpell.Mod,
        "Atk": cSpell.ATK
    })
    past = db.Spell["Slot"]
    for index,val in enumerate(cSpell.Slot): db.Spell.Slot[index] = (past[index] + [False] * val)[:val]
    


class bClass():
    def __init__(self):
        Class = q.dbm.Core.g.C
        Subclass  = q.dbm.Core.g.SC
        if Class: self.cClass = globals()[Class]()
        if Subclass: self.cSubclass = globals()[f"{Class}_{Subclass}"]()

    def pre_Upd(self):
        self.cClass.pre_Upd()
        if q.dbm.Core.g.SC: self.cSubclass.pre_Upd()
        
        
    def Upd(self):
        self.cClass.Upd()
        if q.dbm.Core.g.SC: self.cSubclass.Upd()
    
    def Spell_config(self): 
        Class = q.dbm.Core.g.C
        Subclass  = q.dbm.Core.g.SC     
        print(Class)
        print(Subclass)
        if Subclass in g.list_Spellcast: Spell_Setter(Subclass)
        elif Class in g.list_Spellcast: Spell_Setter(Class)
        

    def __repr__(self):
        return str(self.__dict__)



    
    
class Empty:
    def __init__(self): pass
    def pre_Upd(self): pass
    def Upd(self): pass
    
class Fighter:
    def __init__(self):
        cdata = q.dbm.Stats.C
        cdata.Combat.HD = 10
        cdata.Prof.Armor.extend(q.w.search(Tier = 0, Slot="Armor"))
        cdata.Prof.Armor.extend(q.w.search(Tier = 0, Slot="Shield"))
        cdata.Prof.Weapon.extend(q.w.search(Tier = 0, Slot="Weapon"))

    def Upd(self):
        level = q.dbm.Core.g.L
        skill_list = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
        past = db.Class["Skill Select"]
        db.Class["Skill Select"] = ([s for s in past if s in skill_list and s != ""] + ["", ""])[:2]


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
        


class Fighter_Champion:
    def Upd(self):
        level = q.dbm.Core.g.L
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

class Fighter_Battle_Master:
    def Upd(self):
        level = db.Core.L
        if level >= 3:
            Fuse_1("Combat Superiority", g.Fighter_Combat_Superiority_Use[level])
            Fselect_1("Combat Superiority", g.Fighter_Combat_Superiority_Select[level])

            Fselect_1("Student of War", 1)
            selected_tool = db.Class.Abil["Student of War"].get("Select", [""])[0]
            if selected_tool and selected_tool not in db.Prof["Class"]["Tool"]: q.dbm.Stats.C.Prof.Tool.extend(selected_tool)

            Fgen("Relentless")
        else:
            remove_ability("Student of War")
            remove_ability("Combat Superiority")
            remove_ability("Relentless")

class Fighter_Eldrich_Knight:
    def Upd(self):
        level = q.dbm.Core.g.L
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
        

class Fighter_Samuri:
    def Upd(self):
        level = q.dbm.Core.g.L
        if level >= 3: 
            Fuse_1("Fighting Spirit", 3)
            Fselect_1("Bonus Proficiency", 1)
            select = db.Class.Abil["Bonus Proficiency"].get("Select", [""])[0]
            if select and select not in db.Skill["Class"]: q.dbm.Stats.C.Prof.Skill.extend(select)
        else: 
            remove_ability("Fighting Spirit")
            remove_ability("Bonus Proficiency")
        if level >= 7: Fgen("Elegant Courtier")
        else: remove_ability("Elegant Courtier")
        if level >= 10: Fgen("Tireless Spirit")
        else: remove_ability("Tireless Spirit")
        if level >= 15: Fgen("Rapid Strike")
        else: remove_ability("Rapid Strike")
        if level >= 18: Fuse_1("Strength before Death", 1)
        else: remove_ability("Strength before Death")



class Wizard:
    def __init__(self):
        cdata = q.dbm.Stats.C
        cdata.Combat.HD = 6
        cdata.Prof.Weapon.extend(["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"])


    def Upd(self):
        level = q.dbm.Core.g.L
        
        skill_list = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
        past = db.Class["Skill Select"]
        db.Class["Skill Select"] = ([s for s in past if s in skill_list and s != ""] + ["", ""])[:2]

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
    def Upd(self):
        level = q.dbm.Core.g.L
        if level >= 2:
            Fgen("Abjuration Savant")
            
            ab_ward = Fgen("Arcane Ward")
            ward_max_hp = level + db.Atr["INT"]["Mod"]
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
    def Upd(self):
        level = q.dbm.Core.g.L
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

