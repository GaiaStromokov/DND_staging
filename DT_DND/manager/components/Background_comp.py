import q
from Sheet.get import *



    

def Fselect_1(name, num):
    prof_dict = dBackground()["Prof"]
    prof_dict[name] = (prof_dict.setdefault(name, []) + [""] * num)[:num]


class bBackground():
    def __init__(self):
        self.Skill = []
        self.Weapon = []
        self.Armor = []
        self.Tool = []
        self.Lang = []


        dBackground()["Prof"] = {}
        if q.db.Core.BG: self.cBackground = globals()[q.db.Core.BG](self)
        


class Empty():
    def __init__(self, p):
        pass
    


class Acolyte():
    def __init__(self, p):

        p.Skill = ["Insight", "Religion"]
        Fselect_1("Lang", 2)

        


class Charlatan():
    def __init__(self, p):
        p.Skill = ["Deception", "Sleight of Hand"]
        p.Tool = ["Disguise", "Forgery"]



class Criminal():
    def __init__(self, p):
        p.Skill = ["Deception", "Stealth"]
        p.Tool = ["Thief"]
        Fselect_1("Game", 1)

class Entertainer():
    def __init__(self, p):
        p.Skill = ["Acrobatics", "Performance"]
        p.Tool = ["Disguise"]
        Fselect_1("Music", 1)

class FolkHero():
    def __init__(self, p):
        p.Skill = ["Animal Handling", "Survival"]
        Fselect_1("Job", 1)

class GuildArtisan():
    def __init__(self, p):

        p.Skill = ["Insight", "Persuasion"]
        p.Tool = ["Tinker"]
        Fselect_1("Job", 1)
        Fselect_1("Lang", 1)


class Hermit():
    def __init__(self, p):
        p.Skill = ["Medicine", "Religion"]
        p.Tool = ["Herbalism Kit"]
        Fselect_1("Lang", 1)



class Noble():
    def __init__(self, p):
        p.Skill = ["History", "Persuasion"]
        Fselect_1("Lang", 1)
        Fselect_1("Game", 1)



class Outlander():
    def __init__(self, p):
        p.Skill = ["Athletics", "Survival"]
        Fselect_1("Music", 1)
        Fselect_1("Lang", 1)


class Sage():
    def __init__(self, p):
        p.Skill = ["Arcana", "History"]
        Fselect_1("Lang", 2)



class Sailor():
    def __init__(self, p):
        p.Skill = ["Athletics", "Perception"]
        p.Tool = ["Navigator"]

class Soldier():
    def __init__(self, p):
        p.Skill = ["Athletics", "Intimidation"]
        Fselect_1("Game", 1)


class Urchin():
    def __init__(self, p):
        p.Skill = ["Sleight of Hand", "Stealth"]
        p.Tool = ["Disguise", "Thief"]
