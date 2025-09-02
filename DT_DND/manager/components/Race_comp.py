import q
import Sheet.get as get

import json

def Fgen(name): q.db.Race.Abil.setdefault(name, {})

    
def Fuse_1(name, num):
    q.db.Race.Abil.setdefault(name, {})
    past = q.db.Race.Abil.get(name, {}).get("Use", [False])
    q.db.Race.Abil[name] = {"Use": (past + [False] * num)[:num]}

def Fuse_2(index, name, num):
    q.db.Race.Abil[index].setdefault(name, {})
    past = q.db.Race.Abil.get(index, {}).get(name, {}).get("Use", [False])
    q.db.Race.Abil[index][name] = {"Use": (past + [False] * num)[:num]}
    
    
def fSelect_1(name, num):
    q.db.Race.Abil.setdefault(name, {})
    past = q.db.Race.Abil.get(name, {}).get("Select", [])
    q.db.Race.Abil[name]["Select"] = (past + [""] * num)[:num]




class bRace:
    def __init__(self):
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
        if get.Race(): self.cRace = globals()[get.Race()](self)
            
        if get.Subrace() and get.Subrace() != "Empty":  self.cSubrace = globals()[f"{get.Race()}_{get.Subrace()}"](self)
            
    def Upd(self):
        self.cRace.Upd()
        if get.Subrace() and get.Subrace() != "Empty": self.cSubrace.Upd()

    def __repr__(self):
        def serialize(obj):
            if hasattr(obj, "__dict__"):
                return {k: serialize(v) for k, v in obj.__dict__.items() if k not in ("cRace", "cSubrace")}
            elif isinstance(obj, dict):
                return {k: serialize(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [serialize(v) for v in obj]
            else:
                return obj
        data = serialize(self)
        if hasattr(self, "cRace"): data["cRace"] = serialize(self.cRace)
        if hasattr(self, "cSubrace"): data["cSubrace"] = serialize(self.cSubrace)
        return json.dumps(data, indent=4)


class Empty:
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 30
    

    def Upd(self):
        pass
        
class Human:
    def __init__(self, p):
        self.p = p
        self.p.Lang.extend(["Common"])
        self.p.Speed["Walk"] = 30

    def Upd(self):
        pass

class Human_Standard:
    def __init__(self, p):
        self.p = p


    def Upd(self):
        pass

class Human_Variant:
    def __init__(self, p):
        self.p = p

    def Upd(self):
        pass

class Elf:
    def __init__(self, p):
        self.p = p
        self.p.Vision["Dark"] = 60
        self.p.Speed["Walk"] = 30
        self.p.Skill.extend(["Perception"])
        self.p.Lang.extend( ["Common", "Elvish"])


    def Upd(self):
        pass

class Elf_High:
    def __init__(self, p):
        self.p = p
        self.p.Weapon.extend(["Longsword", "Shortsword", "Shortbow", "Longbow"])


    def Upd(self):
        fSelect_1("Cantrip", 1)

class Elf_Wood:
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 35
        self.p.Weapon.extend(["Shortbow", "Longsword", "Shortsword", "Longbow"]) 

    def Upd(self):
        pass

class Elf_Drow:
    def __init__(self, p):
        self.p = p
        self.p.Vision["Dark"] = 120
        self.p.Weapon.extend(["Rapier", "Shortsword", "Hand Crossbow"])


    
    def Upd(self):
        level = q.db.Core.L
        Fgen("Drow_Magic")
        if level >= 1: Fuse_2("Drow_Magic", "Dancing Lights", 1)
        if level >= 3: Fuse_2("Drow_Magic", "Faerie Fire", 1)


class Elf_Shadar_Kai:
    def __init__(self, p):
        self.p = p


    
    def Upd(self): 
        Fuse_1("Blessing_of_the_Raven_Queen", q.db.Core.PB)

class Dwarf:
    def __init__(self, p):
        self.p = p
        self.p.Vision["Dark"] = 60
        self.p.Speed["Walk"] = 30
        self.p.Weapon.extend(["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"])
        self.p.Lang.extend(["Common", "Dwarvish"])



    
    def Upd(self):
        pass

class Dwarf_Hill:
    def __init__(self, p):
        self.p = p


    
    def Upd(self): 
        self.p.HP = q.db.Core.L

class Dwarf_Mountain:
    def __init__(self, p):
        self.p = p
        self.p.Armor.extend(["Light", "Medium"])


    
    def Upd(self):
        pass

class Halfling:
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 25
        self.p.Skill.extend(["Stealth"])
        self.p.Lang.extend(["Common", "Halfling"])


    
    def Upd(self):
        pass

class Halfling_Lightfoot:
    def __init__(self, p):
        self.p = p
        

    
    def Upd(self):
        pass

class Halfling_Stout:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        pass

class Gnome:
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 25
        self.p.Vision["Dark"] = 60
        self.p.Lang.extend(["Common", "Gnomish"])


    
    def Upd(self):
        pass

class Gnome_Forest:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        pass

class Gnome_Rock:
    def __init__(self, p):
        self.p = p
        self.p.Tool.extend("Tinker")


    
    def Upd(self):
        pass

class Dragonborn:
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 30
        self.p.Lang.extend(["Common", "Draconic"])


    
    def Upd(self):
        pass

class Dragonborn_Black:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fuse_1("Breath_Weapon", 1)

class Dragonborn_Blue:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fuse_1("Breath_Weapon", 1)

class Dragonborn_Brass:
    def __init__(self, p):
        self.p = p
        Fuse_1("Breath_Weapon", 1)

class Dragonborn_Bronze:
    def __init__(self, p):
        self.p = p

    def Upd(self):
        Fuse_1("Breath_Weapon", 1)

class Dragonborn_Copper:
    def __init__(self, p):
        self.p = p

    def Upd(self):
        Fuse_1("Breath_Weapon", 1)

class Dragonborn_Gold:
    def __init__(self, p):
        self.p = p
        
        Fuse_1("Breath_Weapon", 1)

class Dragonborn_Green:
    def __init__(self, p):
        self.p = p

    def Upd(self):
        Fuse_1("Breath_Weapon", 1)

class Dragonborn_Red:
    def __init__(self, p):
        self.p = p

    def Upd(self):
        Fuse_1("Breath_Weapon", 1)

class Dragonborn_Silver:
    def __init__(self, p):
        self.p = p

    def Upd(self):
        Fuse_1("Breath_Weapon", 1)

class Dragonborn_White:
    def __init__(self, p):
        self.p = p

    def Upd(self):
        Fuse_1("Breath_Weapon", 1)

class Half_Orc:
    def __init__(self, p):
        self.p = p
        self.p.Vision["Dark"] = 60
        self.p.Speed["Walk"] = 30
        self.p.Skill.extend(["Intimidation"])
        self.p.Lang.extend(["Common", "Orc"])
        




    
    def Upd(self):
        Fgen("Relentless_Endurance")
        Fuse_1("Relentless_Endurance", 1)
        Fgen("Savage_Attacks")

class HalfOrc_Standard:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        pass

class Tiefling:
    def __init__(self, p):
        self.p = p
        self.p.Vision["Dark"] = 60
        self.p.Speed["Walk"] = 30
        self.p.Lang.extend(["Common", "Infernal"]) 



    
    def Upd(self):
        pass

class Tiefling_Asmodeus:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fgen("Infernal_Legacy")
        level = q.db.Core.L
        if level >= 1: Fuse_2("Infernal_Legacy", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Infernal_Legacy", "Hellish Rebuke", 1)
        if level >= 5: Fuse_2("Infernal_Legacy", "Darkness", 1)

class Tiefling_Baalzebul:
    def __init__(self, p):
        self.p = p



    
    def Upd(self):
        Fgen("Legacy_of_Maladomini")
        level = q.db.Core.L
        if level >= 1: Fuse_2("Legacy_of_Maladomini", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Legacy_of_Maladomini", "Ray of Sickness", 1)
        if level >= 5: Fuse_2("Legacy_of_Maladomini", "Crown of Madness", 1)

class Tiefling_Dispater:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fgen("Legacy_of_Dis")
        level = q.db.Core.L
        if level >= 1: Fuse_2("Legacy_of_Dis", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Legacy_of_Dis", "Disguise Self", 1)
        if level >= 5: Fuse_2("Legacy_of_Dis", "Detect Thoughts", 1)

class Tiefling_Fierna:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fgen("Legacy_of_Minauros")
        level = q.db.Core.L
        if level >= 1: Fuse_2("Legacy_of_Minauros", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy_of_Minauros", "Tensers Floating Disk", 1)
        if level >= 5: Fuse_2("Legacy_of_Minauros", "Arcane Lock", 1)

class Tiefling_Glasya:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fgen("Legacy_of_Cania")
        level = q.db.Core.L
        if level >= 1: Fuse_2("Legacy_of_Cania", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy_of_Cania", "Burning Hands", 1)
        if level >= 5: Fuse_2("Legacy_of_Cania", "Flame Blade", 1)

class Tiefling_Levistus:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fgen("Legacy_of_Stygia")
        level = q.db.Core.L
        if level >= 1: Fuse_2("Legacy_of_Stygia", "Ray of Frost", 1)
        if level >= 3: Fuse_2("Legacy_of_Stygia", "Armor of Agathys", 1)
        if level >= 5: Fuse_2("Legacy_of_Stygia", "Darkness", 1)

class Tiefling_Mammon:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fgen("Legacy_of_Minauros")
        level = q.db.Core.L
        if level >= 1: Fuse_2("Legacy_of_Minauros", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy_of_Minauros", "Tensers Floating Disk", 1)
        if level >= 5: Fuse_2("Legacy_of_Minauros", "Arcane Lock", 1)

class Tiefling_Mephistopheles:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fgen("Legacy_of_Cania")
        level = q.db.Core.L
        if level >= 1: Fuse_2("Legacy_of_Cania", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy_of_Cania", "Burning Hands", 1)
        if level >= 5: Fuse_2("Legacy_of_Cania", "Flame Blade", 1)

class Tiefling_Zariel:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        Fgen("Legacy_of_Avernus")
        level = q.db.Core.L
        if level >= 1: Fuse_2("Legacy_of_Avernus", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Legacy_of_Avernus", "Searing Smite", 1)
        if level >= 5: Fuse_2("Legacy_of_Avernus", "Branding Smite", 1)
            
class Harengon:
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 30
        self.p.Skill.extend(["Perception"])
        self.p.Lang.extend(["Common"])




    
    def Upd(self):
        Fgen("Rabbit_Hop")
        Fuse_1("Rabbit_Hop", q.db.Core.PB)
        self.p.Initiative = q.db.Core.PB

class Harengon_Standard:
    def __init__(self, p):
        self.p = p


    
    def Upd(self):
        pass