import q
import Sheet.get as g
from colorist import *
from box import Box
db = q.db


def defaultStat():
    return Box({
        "Atr": Box({"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}),
        "Speed": Box({"Walk": 0, "Climb": 0, "Swim": 0, "Fly": 0, "Burrow": 0}),
        "Vision": Box({"Dark": 0, "Blind": 0, "Tremor": 0, "Tru": 0}),
        "Prof": Box({"Skill": [], "Weapon": [], "Armor": [], "Tool": [], "Lang": []}),
        "Combat": Box({"Initiative": 0, "HP": 0, "HD": 0})
    })


class Load:
    def Weapon(self,parent):
        PROF = q.dbm.Stats.C.Prof.Weapon
        if parent[0] == "Simple": PROF.extend(q.w.search(Tier = 0, Slot="Weapon", Cat="Simple"))
        if parent[0] == "Martial": PROF.extend(q.w.search(Tier = 0, Slot="Weapon", Cat="Martial"))
        else: PROF.extend(parent)

    def Armor(self,parent):
        q.dbm.Stats.C.Prof.Armor.extend(parent)

    def Selection(self, feature, Name, level):
        Place = q.dbm.Class.g.Abil
        Place.setdefault(Name, {})
        Past = Place.get(Name, {}).get("Select", [])
        Total_Choices = feature.Choices
        Place[Name]["Select"] = (Past + [""] * Total_Choices)[:Total_Choices]

    def Use(self, feature, Name, level):
        Place = q.dbm.Class.g.Abil
        Place.setdefault(Name, {})
        past = Place.get(Name, {}).get("Use", [False])
        Total_Uses = feature.Use[level]
        Place[Name]["Use"] = (past + [False] * Total_Uses)[:Total_Uses]

    def Passive(self, feature, Name, level):
        Place = q.dbm.Class.g.Abil
        Place.setdefault(Name, {})
        
        if hasattr(feature, 'Amount'):
            Place[Name]["Amount"] = feature.Amount[level]

    def Familiar(self, feature, Name, level):
            Place = q.dbm.Class.g.Abil
            Place.setdefault(Name, {})
            
            if hasattr(feature, 'HP'):
                max_hp = 0
                for component in feature.HP:
                    if component == "Level": max_hp += level
                    elif component == "INT": max_hp += q.dbm.Atr.g.Mod("INT")
                
                current_hp = Place[Name].get("HP", {}).get("Current", max_hp)
                Place[Name]["HP"] = {"Max": max_hp, "Current": current_hp}

class bClass:
    def __init__(self):
        self.load = Load()
        self.fHandle = {
            "Selection": self.load.Selection,
            "Use": self.load.Use,
            "Passive": self.load.Passive,
            "Familiar": self.load.Familiar
        }
        self.Data = None
        
        self._Class = None
        self._Subclass = None
        self._Level = None
        self._PB = None

    def Refresh(self):
        self._Class = q.dbm.Core.g.C
        self._Subclass = q.dbm.Core.g.SC
        self._Level = q.dbm.Core.g.L
        self._PB = q.dbm.Core.g.PB
        
        if not self._Class:
            return
        
        data = q.Load_Json(f"dist/Class_Json/{self._Class}", "Base")
        
        if self._Subclass and self._Subclass != "Empty":
            Subclass_data = q.Load_Json(f"dist/Class_Json/{self._Class}", f'{self._Subclass}')
            
            if "Features" in Subclass_data:
                data.setdefault("Features", []).extend(Subclass_data["Features"])
            if "Caster" in Subclass_data:
                data["Caster"] = Subclass_data["Caster"]
        
        self.Data = Box(data)
        features_list = list(self.Data.Features)
        features_list.sort(key=lambda x: x.Level)
        self.dFeature = features_list
        
        place_data = {
            "HD": self.Data.HD,
            "Prof": self.Data.Prof,
            "Prof_Keys": self.Data.Prof.keys(),
            "Skill_List": self.Data.Skills.Options,
            "Skill_Num": self.Data.Skills.Choices,
            "Skill_Past": q.dbm.Class.g.Skill_Select
        }
        if hasattr(self.Data, "Casting"):
            place_data['DS'] = self.Data.Casting
            place_data["Slot_Past"] = q.dbm.Spell.g.Slots
        self.Place = Box(place_data)
        
        self.Config_Init()
        self.Upd()




    def Config_Init(self):
        if "Weapon" in self.Place.Prof_Keys: self.load.Weapon(self.Place.Prof.Weapon)
        if "Armor" in self.Place.Prof_Keys: self.load.Armor(self.Place.Prof.Armor)

    def Upd(self):
        q.dbm.Class.Skill_Select = ([s for s in self.Place.Skill_Past if s in self.Place.Skill_List and s != ""] + ["", ""])[:self.Place.Skill_Num]
        all_features = list(self.Data.Features)
        all_features.sort(key=lambda x: x.Level)
        self.Load_Features()

    def Load_Features(self):     
        level = self._Level
        df = self.dFeature   
        for fIndex in df:
            Types = fIndex.Type
            Name = fIndex.Name.replace(" ", "_")
            if level >= fIndex.Level:
                if hasattr(fIndex, 'Replaces'): self.Delete_Feature(fIndex.Replaces.replace(" ", "_"))
                for type_name in Types: 
                    handle = self.fHandle.get(type_name)
                    if handle: handle(fIndex, Name, level)

    def Delete_Feature(self, Name):
        q.dbm.Class.g.Abil.pop(Name, None)

    def Spell_config(self): 
        if not hasattr(self.Data, "Casting"):
            return

        DS = self.Data.Casting
        level = self._Level
        pb = self._PB

        CAbil = DS.Spell_Abil
        Slot = DS.Slot[self._Level]
        Mod = q.dbm.Atr.g.Mod(CAbil)
        DC  = 8 + pb + Mod
        ATK = f"{'+' if (pb + Mod) >= 0 else ''}{self._PB + Mod}"
        PA = Mod + level
        
        q.dbm.dSpell = Box({
            "Caster": DS.Spell_List,
            "MSL": DS.Max_Spell_Level[level],
            "CA": DS.Cantrips_Available[level],
            "SA": DS.Spells_Available[level],
            "PA": PA,
            "Slot": Slot,
            "Abil": CAbil,
            "DC": DC,
            "Mod": Mod,
            "Atk": ATK
        })
        
        past = self.Place.Slot_Past
        for index, val in enumerate(Slot):
            old_slots = past[index] if index < len(past) else []
            used_slots = [slot for slot in old_slots[:val] if slot]
            past[index] = used_slots + [False] * (val - len(used_slots))

