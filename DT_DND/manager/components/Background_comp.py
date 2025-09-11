import q
from Sheet.get import *



    

def Fselect_1(name, num):
    prof_dict = dBackground()["Prof"]
    prof_dict[name] = (prof_dict.setdefault(name, []) + [""] * num)[:num]


class bBackground():
    def __init__(self):
        dBackground()["Prof"] = {}
        if q.db.Core.BG: self.cBackground = globals()[q.db.Core.BG](self)
    @property
    def data(self):
        return q.dbm.Stats.BG


class Empty():
    def __init__(self, p):
        pass
    


class Acolyte():
    def __init__(self, p):

        p.data.Skill.extend(["Insight", "Religion"])
        Fselect_1("Lang", 2)

        


class Charlatan():
    def __init__(self, p):
        p.data.Skill.extend(["Deception", "Sleight of Hand"])
        p.data.Tool.extend(["Disguise", "Forgery"])



class Criminal():
    def __init__(self, p):
        p.data.Skill.extend(["Deception", "Stealth"])
        p.data.Tool.extend(["Thief"])
        Fselect_1("Game", 1)

class Entertainer():
    def __init__(self, p):
        p.data.Skill.extend(["Acrobatics", "Performance"])
        p.data.Tool.extend(["Disguise"])
        Fselect_1("Music", 1)

class FolkHero():
    def __init__(self, p):
        p.data.Skill.extend(["Animal Handling", "Survival"])
        Fselect_1("Job", 1)

class GuildArtisan():
    def __init__(self, p):

        p.data.Skill.extend(["Insight", "Persuasion"])
        p.data.Tool.extend(["Tinker"])
        Fselect_1("Job", 1)
        Fselect_1("Lang", 1)


class Hermit():
    def __init__(self, p):
        p.data.Skill.extend(["Medicine", "Religion"])
        p.data.Tool.extend(["Herbalism Kit"])
        Fselect_1("Lang", 1)



class Noble():
    def __init__(self, p):
        p.data.Skill.extend(["History", "Persuasion"])
        Fselect_1("Lang", 1)
        Fselect_1("Game", 1)



class Outlander():
    def __init__(self, p):
        p.data.Skill.extend(["Athletics", "Survival"])
        Fselect_1("Music", 1)
        Fselect_1("Lang", 1)


class Sage():
    def __init__(self, p):
        p.data.Skill.extend(["Arcana", "History"])
        Fselect_1("Lang", 2)



class Sailor():
    def __init__(self, p):
        p.data.Skill.extend(["Athletics", "Perception"])
        p.data.Tool.extend(["Navigator"])

class Soldier():
    def __init__(self, p):
        p.data.Skill.extend(["Athletics", "Intimidation"])
        Fselect_1("Game", 1)


class Urchin():
    def __init__(self, p):
        p.data.Skill.extend(["Sleight of Hand", "Stealth"])
        p.data.Tool.extend(["Disguise", "Thief"])
