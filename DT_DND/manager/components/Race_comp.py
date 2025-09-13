import q
import Sheet.get as get

def Fgen(name): q.db.Race.Abil.setdefault(name.replace(" ", "_"), {})

    
def Fuse_1(name, num):
    name = name.replace(" ", "_")
    q.db.Race.Abil.setdefault(name, {})
    past = q.db.Race.Abil.get(name, {}).get("Use", [False])
    q.db.Race.Abil[name] = {"Use": (past + [False] * num)[:num]}

def Fuse_2(index, name, num):
    index = index.replace(" ", "_")
    name = name.replace(" ", "_")
    q.db.Race.Abil[index].setdefault(name, {})
    past = q.db.Race.Abil.get(index, {}).get(name, {}).get("Use", [False])
    q.db.Race.Abil[index][name] = {"Use": (past + [False] * num)[:num]}
    
    
def fSelect_1(name, num):
    name = name.replace(" ", "_")
    q.db.Race.Abil.setdefault(name, {})
    past = q.db.Race.Abil.get(name, {}).get("Select", [])
    q.db.Race.Abil[name]["Select"] = (past + [""] * num)[:num]




class bRace:
    def __init__(self):
        if get.Race(): self.cRace = globals()[get.Race()](self)
        if get.Subrace() and get.Subrace() != "Empty":  self.cSubrace = globals()[f"{get.Race()}_{get.Subrace()}"](self)
            
    def Upd(self):
        self.cRace.Upd()
        if get.Subrace() and get.Subrace() != "Empty": self.cSubrace.Upd()

    @property
    def data(self): return q.dbm.Stats.R

    @property
    def Level(self): return q.dbm.Core.g.L


class Empty:
    def __init__(self, p):
        p.data.Speed["Walk"] = 30
    

    def Upd(self):
        pass
        
class Human:
    def __init__(self, p):

        p.data.Prof.Lang.extend(["Common"])
        p.data.Speed["Walk"] = 30

    def Upd(self):
        pass

class Human_Standard:
    def __init__(self, p):
        pass


    def Upd(self):
        pass

class Human_Variant:
    def __init__(self, p):
        pass

    def Upd(self):
        pass

class Elf:
    def __init__(self, p):

        p.data.Vision["Dark"] = 60
        p.data.Speed["Walk"] = 30
        p.data.Prof.Skill.extend(["Perception"])
        p.data.Prof.Lang.extend( ["Common", "Elvish"])


    def Upd(self):
        pass

class Elf_High:
    def __init__(self, p):
        p.data.Prof.Weapon.extend(["Longsword", "Shortsword", "Shortbow", "Longbow"])


    def Upd(self):
        fSelect_1("Cantrip", 1)

class Elf_Wood:
    def __init__(self, p):

        p.data.Speed["Walk"] = 35
        p.data.Prof.Weapon.extend(["Shortbow", "Longsword", "Shortsword", "Longbow"]) 

    def Upd(self):
        pass

class Elf_Drow:
    def __init__(self, p):
        self.p = p
        p.data.Vision["Dark"]= 120
        p.data.Prof.Weapon.extend(["Rapier", "Shortsword", "Hand Crossbow"])


    
    def Upd(self):
        level = self.p.Level
        Fgen("Drow Magic")
        if level >= 1: Fuse_2("Drow Magic", "Dancing Lights", 1)
        if level >= 3: Fuse_2("Drow Magic", "Faerie Fire", 1)


class Elf_Shadar_Kai:
    def __init__(self, p):
        pass

    def Upd(self): 
        Fuse_1("Blessing of the Raven Queen", q.dbm.Core.g.PB)

class Dwarf:
    def __init__(self, p):

        p.data.Vision["Dark"] = 60
        p.data.Speed["Walk"] = 30
        p.data.Prof.Weapon.extend(["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"])
        p.data.Prof.Lang.extend(["Common", "Dwarvish"])

    def Upd(self):
        pass

class Dwarf_Hill:
    def __init__(self, p):
        self.p = p

    def Upd(self): 
        self.p.data.Combat.HP = q.dbm.Core.g.L

class Dwarf_Mountain:
    def __init__(self, p):
        p.data.Prof.Armor.extend(["Light", "Medium"])

    def Upd(self):
        pass

class Halfling:
    def __init__(self, p):

        p.data.Speed["Walk"] = 25
        p.data.Prof.Skill.extend(["Stealth"])
        p.data.Prof.Lang.extend(["Common", "Halfling"])

    def Upd(self):
        pass

class Halfling_Lightfoot:
    def __init__(self, p):
        pass
    
    def Upd(self):
        pass

class Halfling_Stout:
    def __init__(self, p):
        pass
    
    def Upd(self):
        pass

class Gnome:
    def __init__(self, p):
        p.data.Speed["Walk"] = 25
        p.data.Vision["Dark"] = 60
        p.data.Prof.Lang.extend(["Common", "Gnomish"])

    def Upd(self):
        pass

class Gnome_Forest:
    def __init__(self, p):
        pass
    def Upd(self):
        pass

class Gnome_Rock:
    def __init__(self, p):
        p.data.Tool.extend("Tinker")

    def Upd(self):
        pass

class Dragonborn:
    def __init__(self, p):
        p.data.Speed["Walk"] = 30
        p.data.Prof.Lang.extend(["Common", "Draconic"])

    def Upd(self):
        pass

class Dragonborn_Black:
    def __init__(self, p):
        pass
    
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Blue:
    def __init__(self, p):
        pass
    
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Brass:
    def __init__(self, p):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Bronze:
    def __init__(self, p):
        pass
    
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Copper:
    def __init__(self, p):
        pass
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Gold:
    def __init__(self, p):
        pass

    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Green:
    def __init__(self, p):
        pass
    
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Red:
    def __init__(self, p):
        pass
    
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Silver:
    def __init__(self, p):
        pass
    
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_White:
    def __init__(self, p):
        pass
    
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Half_Orc:
    def __init__(self, p):

        p.data.Vision["Dark"] = 60
        p.data.Speed["Walk"] = 30
        p.data.Prof.Skill.extend(["Intimidation"])
        p.data.Prof.Lang.extend(["Common", "Orc"])
        




    
    def Upd(self):
        Fgen("Relentless Endurance")
        Fuse_1("Relentless Endurance", 1)
        Fgen("Savage Attacks")

class HalfOrc_Standard:
    def __init__(self, p):
        pass
    
    def Upd(self):
        pass

class Tiefling:
    def __init__(self, p):
        p.data.Vision["Dark"] = 60
        p.data.Speed["Walk"] = 30
        p.data.Prof.Lang.extend(["Common", "Infernal"]) 

    def Upd(self):
        pass

class Tiefling_Asmodeus:
    def __init__(self, p):
        self.p = p
    
    def Upd(self):
        Fgen("Infernal Legacy")
        level = self.p.Level
        if level >= 1: Fuse_2("Infernal Legacy", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Infernal Legacy", "Hellish Rebuke", 1)
        if level >= 5: Fuse_2("Infernal Legacy", "Darkness", 1)

class Tiefling_Baalzebul:
    def __init__(self, p):
        self.p = p
    
    def Upd(self):
        Fgen("Legacy of Maladomini")
        level = self.p.Level
        if level >= 1: Fuse_2("Legacy of Maladomini", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Legacy of Maladomini", "Ray of Sickness", 1)
        if level >= 5: Fuse_2("Legacy of Maladomini", "Crown of Madness", 1)

class Tiefling_Dispater:
    def __init__(self, p):
        self.p = p
    
    def Upd(self):
        Fgen("Legacy of Dis")
        level = self.p.Level
        if level >= 1: Fuse_2("Legacy of Dis", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Legacy of Dis", "Disguise Self", 1)
        if level >= 5: Fuse_2("Legacy of Dis", "Detect Thoughts", 1)

class Tiefling_Fierna:
    def __init__(self, p):
        self.p = p
    
    def Upd(self):
        Fgen("Legacy of Phlegethos")
        level = self.p.Level
        if level >= 1: Fuse_2("Legacy of Phlegethos", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy of Phlegethos", "Tensers Floating Disk", 1)
        if level >= 5: Fuse_2("Legacy of Phlegethos", "Arcane Lock", 1)

class Tiefling_Glasya:
    def __init__(self, p):
        self.p = p
    
    def Upd(self):
        Fgen("Legacy of Malbolge")
        level = self.p.Level
        if level >= 1: Fuse_2("Legacy of Malbolge", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy of Malbolge", "Burning Hands", 1)
        if level >= 5: Fuse_2("Legacy of Malbolge", "Flame Blade", 1)

class Tiefling_Levistus:
    def __init__(self, p):
        self.p = p
    
    def Upd(self):
        Fgen("Legacy_of_Stygia")
        level = self.p.Level
        if level >= 1: Fuse_2("Legacy_of_Stygia", "Ray of Frost", 1)
        if level >= 3: Fuse_2("Legacy_of_Stygia", "Armor of Agathys", 1)
        if level >= 5: Fuse_2("Legacy_of_Stygia", "Darkness", 1)

class Tiefling_Mammon:
    def __init__(self, p):
        self.p = p
    
    def Upd(self):
        Fgen("Legacy of Minauros")
        level = self.p.Level
        if level >= 1: Fuse_2("Legacy of Minauros", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy of Minauros", "Tensers Floating Disk", 1)
        if level >= 5: Fuse_2("Legacy of Minauros", "Arcane Lock", 1)

class Tiefling_Mephistopheles:
    def __init__(self, p):
        self.p = p
    def Upd(self):
        Fgen("Legacy of Cania")
        level = self.p.Level
        if level >= 1: Fuse_2("Legacy of Cania", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy of Cania", "Burning Hands", 1)
        if level >= 5: Fuse_2("Legacy of Cania", "Flame Blade", 1)

class Tiefling_Zariel:
    def __init__(self, p):
        self.p = p
    def Upd(self):
        Fgen("Legacy of Avernus")
        level = self.p.Level
        if level >= 1: Fuse_2("Legacy of Avernus", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Legacy of Avernus", "Searing Smite", 1)
        if level >= 5: Fuse_2("Legacy of Avernus", "Branding Smite", 1)
            
class Harengon:
    def __init__(self, p):
        self.p = p
        p.data.Speed["Walk"] = 30
        p.data.Prof.Skill.extend(["Perception"])
        p.data.Prof.Lang.extend(["Common"])

    def Upd(self):
        Fgen("Rabbit Hop")
        Fuse_1("Rabbit Hop", q.db.Core.PB)
        self.p.data.Combat.Initiative = q.db.Core.PB

class Harengon_Standard:
    def __init__(self, p):
        pass
    def Upd(self):
        pass