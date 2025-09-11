import q
import Sheet.get as get
from access_data.color_reference import *
from colorist import *
from access_data.Grimoir import *

from manager.components.Background_comp import bBackground
from manager.components.Class_comp import bClass
from manager.components.Milestone_comp import bMilestone
from manager.components.Race_comp import bRace
db=q.db

def defaultStat():
    return Box({
        "Atr": Box({"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}),
        "Speed": Box({"Walk": 0, "Climb": 0, "Swim": 0, "Fly": 0, "Burrow": 0}),
        "Vision": Box({"Dark": 0, "Blind": 0, "Tremor": 0, "Tru": 0}),
        "Prof": Box({"Skill": [], "Weapon": [], "Armor": [], "Tool": [], "Lang": []}),
        "Combat": Box({"Initiative": 0, "HP": 0, "HD": 0})
    })

def defaultSpell():
    return Box({
        "Caster": "",
        "MSL": 0,
        "CA": 0,
        "SA": 0,
        "PA": 0,
        "Slots": [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        "Abil": "",
        "DC": 0,
        "Mod": 0,
        "Atk": ""
    })

class Access:
    def __init__(self, cls):
        self.cls = cls
    def __get__(self, instance, owner):
        if instance is None: return self
        if not hasattr(instance, f'_{self.cls.__name__}_instance'):
            nested_instance = self.cls()
            nested_instance.p = instance
            setattr(instance, f'_{self.cls.__name__}_instance', nested_instance)
        return getattr(instance, f'_{self.cls.__name__}_instance')

class dbm:
    def __init__(self):
        self.rRace = None
        self.rClass = None
        self.rBackground = None
        self.rMilestone = None
        self.Stats = Box({"R": defaultStat(),"C": defaultStat(),"BG": defaultStat(),"M": defaultStat()})
        self.dSpell = defaultSpell()

    @property
    def Collect_Atr(self):
        stats = [self.Stats[k] for k in ["R", "C", "BG", "M"]]
        return Box({k: sum(s["Atr"][k] for s in stats) for k in stats[0]["Atr"]})

    @property
    def Collect_Speed(self):
        stats = [self.Stats[k] for k in ["R", "C", "BG", "M"]]
        return Box({k: sum(s["Speed"][k] for s in stats) for k in stats[0]["Speed"]})

    @property
    def Collect_Vision(self):
        stats = [self.Stats[k] for k in ["R", "C", "BG", "M"]]
        return Box({k: sum(s["Vision"][k] for s in stats) for k in stats[0]["Vision"]})

    @property
    def Collect_Prof(self):
        stats = [self.Stats[k] for k in ["R", "C", "BG", "M"]]
        return Box({k: list({item for s in stats for item in s["Prof"][k]}) for k in stats[0]["Prof"]})

    @property
    def Collect_Combat(self):
        stats = [self.Stats[k] for k in ["R", "C", "BG", "M"]]
        return Box({k: sum(s["Combat"][k] for s in stats) for k in stats[0]["Combat"]})


    @property
    def Collect_Health(self):
        return q.dbm.Collect_Combat.HP
    
    @property
    def Collect_Initiative(self):
        return q.dbm.Collect_Combat.Initiative
    @property
    def Collect_All(self):
        return Box({
            "Atr": self.Collect_Atr,
            "Speed": self.Collect_Speed,
            "Vision": self.Collect_Vision,
            "Prof": self.Collect_Prof,
            "Combat": self.Collect_Combat
        })
    
    @property
    def Visual_Skill(self):
        proficient_skills = set(self.Collect_Prof["Skill"])
        return {skill: skill in proficient_skills for skill in get.list_Skill}

    @property
    def Mod_Skill(self):
        dSkill = self.Visual_Skill
        return {skill: int(self.Atr.g.Mod(get.dict_Skill[skill]["Atr"])) + (db.Core.PB if dSkill[skill] else 0) for skill in get.list_Skill}
    
    @Access
    class Manager:
        def startup(self):
            self.Init_schema()
            self.p.rRace.Upd()
            self.p.rClass.Upd()
            self.Recalculate_Stats()
            self.Upd.Spells()

        def Init_schema(self):
            self.p.Milestone_Count = 0
            self.p.rRace = bRace()
            self.p.rClass = bClass()
            self.p.rBackground = bBackground()
            self.p.rMilestone = bMilestone()
            
        def Recalculate_Stats(self):
            self.p.Atr.Collect()
            self.p.Health.Collect()
            self.p.Combat.Armor.Collect()
            
        def Update_Spells(self):
            pass
        
        @Access
        class New:
            def Level(self):
                pass
            def Race(self):
                q.dbm.Race.s.Abil.Wipe()
                q.dbm.rRace = bRace()
                q.dbm.rRace.Upd()
                q.dbm.rMilestone.Upd()
                q.dbm.Manager.Recalculate_Stats()
            def Class(self):
                q.dbm.Class.s.Abil.Wipe()
                q.dbm.Spell.Wipe()
                q.dbm.rClass = bClass()
                q.dbm.rClass.Upd()
                q.dbm.rMilestone.Upd()
                q.dbm.Manager.Recalculate_Stats()
                q.dbm.Manager.Update_Spells()
            def Background(self):
                q.dbm.Background.Wipe()
                q.dbm.Background = bBackground()
                q.dbm.Manager.Recalculate_Stats()

        @Access
        class Upd:
            def Atr(self):
                q.dbm.Atr.Collect()
                q.dbm.rMilestone.Upd()
                q.dbm.Manager.Recalculate_Stats()
                q.dbm.Manager.Update_Spells()           
            
            def Class_Select(self):
                q.dbm.rClass.Upd()
                q.dbm.rMilestone.Upd()
                q.dbm.Manager.Recalculate_Stats()     

            def Background_Prof(self):
                q.dbm.rBackground = bBackground()
                q.dbm.Manager.Recalculate_Stats()
            def Spells(self):
                if q.dbm.Spell.Validate: q.dbm.rClass.Spell_config()
            def Milestone_Feat(self):
                q.dbm.Manager.Upd.Atr()


    @Access
    class Core:
        @Access
        class g:
            def Visual(self):
                return {
                    "Level": db.Core.L,
                    "PB": db.Core.PB,
                    "Class": db.Core.C.replace("_", " "),
                    "Subclass": db.Core.SC.replace("_", " "),
                    "Race": db.Core.R.replace("_", ""),
                    "Subrace": db.Core.SR.replace("_", " "),
                    "Background": db.Core.BG.replace("_", " ")
                }
            @property
            def L(self):  return db.Core.L
            @property
            def PB(self): return db.Core.PB
            @property
            def R(self):  return db.Core.R
            @property
            def SR(self): return db.Core.SR
            @property
            def C(self):  return db.Core.C
            @property
            def SC(self): return db.Core.SC
            @property
            def BG(self): return db.Core.BG
            
        @Access
        class s: 
            def L(self, value):
                Level = value
                PB = (Level - 1) // 4 + 2
                
                db.Core.L = Level
                db.Core.PB = PB
                q.dbm.Class.Validate
                q.dbm.Manager.New.Level()
            def R(self, value): 
                db.Core.R = value.replace(" ", "_")
                db.Core.SR = ""
                q.dbm.Race.s.Abil.Wipe()
                q.dbm.Manager.New.Race()
                
            def SR(self, value): 
                db.Core.SR = value.replace(" ", "_")
                q.dbm.Race.s.Abil.Wipe()
                q.dbm.Manager.New.Race()
                
            def C(self, value): 
                db.Core.C = value.replace(" ", "_")
                db.Core.SC = ""
                q.dbm.Class.s.Abil.Wipe()
                q.dbm.Manager.New.Class()

            def SC(self, value): 
                db.Core.SC = value.replace(" ", "_")
                q.dbm.Class.s.Abil.Wipe()
                q.dbm.Manager.New.Class()

            def BG(self, value): 
                db.Core.BG = value.replace(" ", "_")
                q.dbm.Background.reset()
                q.dbm.Milestone.New.Background()
    @Access
    class Atr:
        def Collect(self):
            dAtr = q.db.Atr
            for atr in get.list_Atr:
                vBase = dAtr[atr]["Base"]
                vRace = q.dbm.Stats["R"]["Atr"][atr]
                vRasi = dAtr[atr]["Rasi"]
                vMilestone1 = dAtr[atr].get("Milestone", 0)
                vClass = q.dbm.Stats["C"]["Atr"][atr]
                vMilestone2 = q.dbm.Stats["M"]["Atr"][atr]
                fScore = vBase + vRace + vRasi + vClass + vMilestone1 + vMilestone2
                dAtr[atr]["Val"] = fScore
                dAtr[atr]["Mod"] = (fScore - 10) // 2
        @Access
        class g:
            def data(self, idx): return db.Atr[idx]
            def Rasi(self, idx): return db.Atr[idx]["Rasi"]
            def Milestone(self, idx): return db.Atr[idx]["Milestone"]
            def Val(self, idx): return db.Atr[idx]["Val"]
            def Mod(self, idx): return db.Atr[idx]["Mod"]
        
        @Access
        class s:
            @Access
            class Base:
                def Modify(self, stat, num):
                    db.Atr[stat].Base = int(num)
                    q.dbm.Atr.Collect()
    @Access
    class Class:
        def reset(self): self.p.Stats["C"] = defaultStat()

        def Validate(self):
            Level = db.Core.L
            Class = db.Core.C
            class_exception_map = {1: ["Cleric", "Warlock"], 2: ["Wizard"]}
            return Level >= 3 or Class in class_exception_map.get(Level, [])
        @Access
        class g: 
            def Visual(self):
                data = q.db.Core
                return {
                    "Level": data.L,
                    "PB": data.PB,
                    "Race": data.R.replace("_", ""),
                    "Subrace": data.SR.replace("_", ""),
                    "Class": data.C.replace("_", ""),
                    "Subclass": data.SC.replace("_", ""),
                    "Background": data.BG.replace("_", "")
                }
            def Data(self): return db.Class
            def Abil(self): db.Class["Abil"]
            def Skill_Select(self): return db.Class["Skill Select"]
            

        @Access
        class s: 
            @Access
            class Skill_Select:
                def Clear(self):
                    cdata = db.Class["Skill Select"]
                    for idx in range(len(cdata)): cdata[idx] = ""
                    q.dbm.Manager.Upd.Class_Select()
                def Modify(self, cat, data):
                    cdata = db.Class["Skill Select"]
                    cdata[cat] = data
                    q.dbm.Manager.Upd.Class_Select()
            @Access
            class Abil:
                def Use(self, key, index, data):
                    db.Class.Abil[key]["Use"][index] = data
                def Select(self, key, index, data):
                    db.Class.Abil[key]["Select"][index] = data
                    q.dbm.Manager.Upd.Class_Select()
                def Wipe(self):
                    db.Class.Abil = {}
                    
    @Access
    class Race:
        def reset(self): self.p.Stats["R"] = defaultStat()
        @Access
        class g: 
            def data(self): return db.Race
            def Abil(self): db.Race["Abil"]
        @Access
        class s: 
            @Access
            class Asi:
                def Clear(self): 
                    db.Race.Rasi = ["", ""]
                    for atr in get.list_Atr: db.Atr[atr].Rasi = 0
                    q.dbm.Race.s.Asi.Finalize()
                    q.dbm.Atr.Collect()
                    
                def Modify(self, key, data):
                    cdata = db.Race
                    cdata.Rasi[key] = data
                    q.dbm.Race.s.Asi.Finalize()
                    q.dbm.Atr.Collect()

                def Finalize(self):
                    cdata = db.Race.Rasi
                    sdata = db.Atr
                    atr_1, atr_2 = cdata[0], cdata[1]
                    for atr in get.list_Atr: 
                        if atr == atr_1: sdata[atr].Rasi = 1
                        elif atr == atr_2: sdata[atr].Rasi = 2
                        else: sdata[atr].Rasi = 0
            @Access
            class Abil:
                def Use(self, key, index, data): 
                    db.Race.Abil[key]["Use"][index] = data
                
                def Wipe(self):
                        db.Race.Abil = {}
            
            @Access
            class Spell:
                def Use(self, key, spell, data): 
                    db.Race.Abil[key][spell]["Use"] = data
                    
                def Select(self, key, data): db.Race.Abil[key]["Select"][0] = data

    @Access
    class Background:
        def Reset(self): self.p.Stats["BG"] = defaultStat()
        def Wipe(self):
            db.Background={"Prof": {}, "Equipment": {}}
        @Access
        class g: 
            def Data(self): return db.Background
        @Access
        class s: 
            @Access
            class Prof:
                def Clear(self):
                    cdata = db.Background["Prof"]
                    for key in cdata:
                        plen = len(cdata[key]["Select"])
                        cdata[key]["Select"] = [""] * plen
                    q.dbm.Manager.Upd.Background_Prof()
                def Modify(self, cat, index, data):
                    cdata = db.Background["Prof"]
                    cdata[cat]["Select"][index] = data
                    q.dbm.Manager.Upd.Background_Prof()

        
    @Access
    class Milestone:
        @property
        def Reset(self): self.p.Stats["M"] = defaultStat()

        @Access
        class Data:
            pass
        @Access
        class g: pass
        @Access
        class s: 
            @Access
            class Top:
                def Clear(self, index):
                    cdata = db.Milestone
                    prefeat = cdata["Feat"][index]
                    if prefeat and prefeat in cdata["Data"]:
                        cdata["Data"].pop(prefeat)
                    cdata["Select"][index] = ""
                    cdata["Feat"][index] = ""
                    cdata["Asi"][index] = ["", ""]
                    q.dbm.Milestone.s.Asi.Finalize()
                    q.dbm.Manager.Upd.Milestone_Feat()
                    
                def Modify(self, index, inp):
                    cdata = db.Milestone
                    cdata["Select"][index] = inp
                    cdata["Feat"][index] = ""
                    cdata["Asi"][index] = ["", ""]
                    q.dbm.Milestone.s.Asi.Finalize()
                    q.dbm.Manager.Upd.Milestone_Feat()
                    
            @Access
            class Feat:
                def Clear(self, index):
                    cdata = db.Milestone
                    prefeat = cdata["Feat"][index]
                    if prefeat and prefeat in cdata["Data"]:
                        cdata["Data"].pop(prefeat)
                    cdata["Feat"][index] = ""
                    q.dbm.Milestone.s.Asi.Finalize()
                    q.dbm.Manager.Upd.Milestone_Feat()

                def Select(self, index, feat):
                    cdata = db.Milestone
                    if feat not in cdata["Feat"]:
                        cdata["Feat"][index] = feat
                        if feat in get.list_Feat_Select:
                            cdata["Data"][feat] = {"Select": [""]}
                        elif feat == "Weapon Master":
                            cdata["Data"][feat] = {"Select": ["", "", "", ""]}
                        else:
                            cdata["Data"][feat] = {}
                            
                    
                def Modify(self, data, script, feat, index):
                    cdata = db.Milestone
                    if feat not in cdata["Data"]: return
                    if script == "Clear": data= ""
                    cdata["Data"][feat]["Select"][index] = data
                    q.dbm.Milestone.s.Asi.Finalize()
                    q.dbm.Manager.Upd.Milestone_Feat()

                def Feat_Use(self, feat, index, data):
                    cdata = db.Milestone
                    if feat in cdata["Data"]: cdata["Data"][feat]["Use"][index] = data

            @Access
            class Asi:
                def Clear(self, key, index):
                    db.Milestone["Asi"][key][index] = ""
                    q.dbm.Milestone.s.Asi.Finalize()
                    q.dbm.Manager.Upd.Milestone_Feat()
                    
                def Modify(self, key, index, data):
                    db.Milestone["Asi"][key][index] = data
                    q.dbm.Milestone.s.Asi.Finalize()
                    q.dbm.Manager.Upd.Milestone_Feat()
                def Finalize(self):
                    print("Finalizing Milestone Asi")
                    stats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
                    dAsi = db.Milestone["Asi"]
                    dAtr = db.Atr
                    for idx1,idx2 in dAsi:
                        if idx1: stats[idx1] += 1
                        if idx2: stats[idx2] += 1
                    for atr in stats:
                        dAtr[atr].Milestone = stats[atr]
                    
    @Access
    class Spell:
        @property
        def Validate(self): 
            Class = self.p.Core.g.C
            Subclass = self.p.Core.g.SC
            Map = get.list_Spellcast
            return Class in Map or Subclass in Map
        def Wipe(self): self.p.dSpell = defaultSpell()
        def _Toggle_Cantrip(self, spell, spell_list, max_known):
            current_known = get.cantrips_known()
            if spell in spell_list:       spell_list.remove(spell)
            elif current_known < max_known: spell_list.append(spell)

        def _Toggle_Spell(self, spell, spell_list, max_known):
            current_known = get.spells_known()
            if spell in spell_list:       spell_list.remove(spell)
            elif current_known < max_known: spell_list.append(spell)

        def _Toggle_Prepare(self, spell, spell_list, max_known):
            current_prep = get.spells_prepared()
            if spell in spell_list:       spell_list.remove(spell)
            elif current_prep < max_known: spell_list.append(spell)
        @Access
        class g: 
            @Access
            class Cantrip:
                def Known(self): return len(db.Spell.Book[0])
            @Access
            class Spell:
                
                def Known(self):
                    cdata = db.Spell.Book
                    num = 0
                    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        num += len(cdata[i])
                    return num

                def Prepared(self):
                    cdata = q.db.Spell.Prepared
                    num = 0
                    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        num += len(cdata[i])
                    return num


        @Access
        class s:
            def Learn(self, spell, level):
                cspell = db.Spell["Book"][level]
                sdata = q.qbm.dspell
                if level == 0: self.p._Toggle_Cantrip(spell, cspell, sdata['cantrips_available'])
                else:          self.p._Toggle_Spell(spell, cspell, sdata['spells_available'])

            def Prepare(self, spell, level):
                cspell = db.Spell["Prepared"][level]
                sdata = q.qbm.dspell
                self.p._Toggle_Prepare(spell, cspell, sdata['prepared_available'])
                
            def Cast(self, level):
                slots = db.Spell["Slot"][level]
                for i in range(len(slots)):
                    if not slots[i]:
                        slots[i] = True
                        break
    @Access
    class Health:
        def Collect(self):
            cdata = q.dbm.Collect_Health
            math = cdata + q.db.HP.Player
            q.db.HP["Sum"] = math
            q.db.HP["Current"] = math
        @Access
        class g: 
            @property
            def Visual(self):
                data = q.db.HP
                HP = f"{data["Current"]} / {data["Sum"]}"
                TEMP = f"{data["Temp"]}"
                MAX = data["Player"]
                return Box({"HP": HP, "Temp": TEMP, "Max": MAX})
        @Access
        class s: 
            def Hp(self, delta):
                hp = db.HP
                if delta < 0:
                    if hp["Temp"] > 0: hp["Temp"] -= 1
                    else: hp["Current"] -= 1
                else: hp["Current"] = min(hp["Current"] + 1, hp["Sum"])

            def Temp(self, delta):
                hp = db.HP
                if delta > 0 or hp["Temp"] > 0: hp["Temp"] += delta

            def Player(self, data):
                db.HP["Player"] = int(data)
                q.dbm.Manager.Collect_Combat
    
    @Access
    class Initiative:
        @Access
        class g:
            @property
            def Visual(self):
                print(q.dbm.Stats.M)
                data = q.dbm.Collect_Initiative
                DEX = q.dbm.Atr.g.Mod("DEX")
                math = data + DEX
                VAL =f"{'+' if math >= 0 else '-'}{abs(math)}"
                RACE = q.dbm.Stats.R.Combat.Initiative
                CLASS = q.dbm.Stats.C.Combat.Initiative
                MILESTONE = q.dbm.Stats.M.Combat.Initiative
                return Box({"Val": VAL, "Dex": DEX, "Race": RACE, "Class": CLASS, "Milestone": MILESTONE})

    @Access
    class Armor:
        @Access
        class g:
            @property
            def Visual(self):
                data = q.db.AC
                SUM = data.Sum
                BASE = data.Base
                DEX = data.Dex
                SHIELD = data.Shield
                return Box({"Sum": SUM,"Base": BASE,"Dex": DEX,"Shield": SHIELD})




    @Access
    class Combat:
        
        @Access
        class Armor:
            def Collect(self):
                dex_mod = q.dbm.Atr.g.Mod("DEX")
                base_ac = 10
                dex = dex_mod
                shield_bonus = 0

                armor = q.db.Inventory.Closet["Armor"]
                if armor:
                    item = q.w.dItem(armor)
                    prof = item.Base in self.Prof["Armor"]
                    if prof:
                        base_ac = item.AC
                        dex = min(dex_mod, item.Dex_Max)
                h2data  = q.db.Inventory.Closet["Hand_2"]
                if h2data:
                    hand_2 = get.weapon_action_handler(h2data)   
                    if hand_2.Category == "Shield":
                        shield_bonus = hand_2.AC
                q.db.AC.Base = base_ac
                q.db.AC.Dex = dex
                q.db.AC.Shield = shield_bonus
                q.db.AC.Sum = base_ac + dex + shield_bonus

        @Access
        class g: pass
        @Access
        class s: 
            @Access
            class Wizard:
                def Arcane_Ward(self, num):
                    ward_data = db.Class["Abil"]["Arcane Ward"]["HP"]
                    new_hp = ward_data["Current"] + num
                    ward_data["Current"] = max(0, min(new_hp, ward_data["Max"]))
            @Access
            class Condition:
                def Modify(self, index, data):
                    db.Condition[index] = data
    @Access
    class Rest:
        @Access
        class g: pass
        @Access
        class s:
            def Long(self):
                if get.valid_spellclass():
                    for level in range(1, 10):
                        if level in db.Spell["Slot"]:
                            db.Spell["Slot"][level] = [False] * len(db.Spell["Slot"][level])

            def Short(self):
                pass
    @Access
    class Player: pass
    @Access
    class Info:
        @Access
        class g: pass
        @Access
        class s:
            @Access
            class Char:
                def Modify(self, name, data):
                    db.Characteristic[name] = data
            
            @Access
            class Desc:
                def Modify(self, name, data):
                    db.Description[name] = data
                    
    @Access
    class Inventory:
        @Access
        class g: pass
        @Access
        class s:
            @Access
            class Backpack:
                def Add(self, cat, item):
                    backpack = db.Inventory.Backpack
                    if item in backpack.keys(): backpack[item][1] += 1
                    else:                        backpack[item] = [cat, 1]
                
                def Remove(self, item):
                    db.Inventory.Backpack.pop(item, None)
                    return 0
                
                #TODO - fix this function
                def Modify(self, item, delta): 
                    backpack = db.Inventory.Backpack
                    print(backpack)
                    if item not in backpack: backpack[item] = [None, delta]
                    else:                    backpack[item][1] += delta
                    
                    if backpack[item][1] <= 0:
                        backpack.pop(item, None)
                        
                        slot = get.item_slot(item)
                        if slot:
                            db.Inventory.Closet[slot] = ""
                        
                        return 0
                    
                    return backpack[item][1]
    @Access
    class Closet:
        @Access
        class g: pass
        @Access
        class s: 
            @Access
            class Equip:
                def Clear(self, cat):
                    db.Inventory.Closet[cat] = ""

                def Modify(self, cat, name):
                    closet = db.Inventory.Closet
                    backpack = db.Inventory.Backpack
                    item = q.w.dItem(name)
                    item_type = item.Slot

                    if item_type == "Weapon": 
                        self.Weapon(cat, name, item, closet, backpack)
                    elif item_type == "Armor": 
                        self.Armor(cat, name, item, closet)
                    elif item_type == "Shield": 
                        self.Shield(cat, name, item, closet)

                def Weapon(self, cat, name, item, closet, backpack):
                    two_handed = "Two-handed" in item.Prop
                    versatile = "Versatile" in item.Prop
                    h1 = closet["Hand_1"]
                    h2 = closet["Hand_2"]

                    def owned_count(i): 
                        return backpack[i][1] if i in backpack else 0

                    if cat == "Hand_1":
                        if two_handed:
                            closet["Hand_1"], closet["Hand_2"] = name, ""
                            return
                        if h2 == name:
                            if versatile or owned_count(name) > 1: 
                                closet["Hand_1"] = name
                        else: 
                            closet["Hand_1"] = name
                    elif cat == "Hand_2":
                        if h1 and "Two-handed" in q.w.dItem(h1).Prop: 
                            return
                        if h1 == name:
                            if versatile or owned_count(name) > 1: 
                                closet["Hand_2"] = name
                        else: 
                            closet["Hand_2"] = name

                def Armor(self, cat, name, item, closet):
                    str_mod = db.Atr["STR"]["Mod"]
                    if str_mod < item.Str_Req:  return
                    else: closet[cat] = name

                def Shield(self, cat, name, item, closet):
                    h1 = closet["Hand_1"]
                    if h1 and "Two-handed" in q.w.dItem(h1).Prop: return
                    closet["Hand_2"] = name