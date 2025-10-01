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

class bRace:
    def __init__(self):
        self.load = Load()
        self.fHandle = {
            "Selection": self.load.Selection,
            "Use": self.load.Use,
            "Passive": self.load.Passive,
        }
        self.Data = None
        
        self._Race = None
        self._Subrace = None
        self._Level = None
        self._PB = None
    @property
    def File(self):
        return f"dist/Race_Json/{self._Race}"
        
    def Refresh(self):
        self._Race = q.dbm.Core.g.R
        self._Subrace = q.dbm.Core.g.SR
        self._Level = q.dbm.Core.g.L
        self._PB = q.dbm.Core.g.PB

        if not self._Race:
            return

        data = q.Load_Json(self.File, "Base")

        if self._Subrace and self._Subrace != "Empty":
            Subrace_data = q.Load_Json(self.File, f'{self._Subrace}')

            data["Speed"].update(Subrace_data["Speed"])
            data["Vision"].update(Subrace_data["Vision"])
            for k, v in Subrace_data["Prof"].items():
                data["Prof"][k].extend(v)

            if "Combat" in Subrace_data:
                data.setdefault("Combat", {}).update(Subrace_data["Combat"])

            if "Features" in Subrace_data:
                data.setdefault("Features", []).extend(Subrace_data["Features"])

        self.Data = Box(data)
        self.dFeature = self.Data.Features

        place_data = {
            "HD": self.Data.Combat.HD,
            "Prof": self.Data.Prof,
            "Prof_Keys": self.Data.Prof.keys(),
        }
        self.Place = Box(place_data)

        self.Config_Init()
        self.Upd()


    def Config_Init(self):
        if "Weapon" in self.Place.Prof_Keys: self.load.Weapon(self.Place.Prof.Weapon)
        if "Armor" in self.Place.Prof_Keys: self.load.Armor(self.Place.Prof.Armor)
        if "Skill" in self.Place.Prof_Keys: q.dbm.Stats.C.Prof.Skill.extend(self.Place.Prof.Skill)
        if "Tool" in self.Place.Prof_Keys: q.dbm.Stats.C.Prof.Tool.extend(self.Place.Prof.Tool)
        if "Lang" in self.Place.Prof_Keys: q.dbm.Stats.C.Prof.Lang.extend(self.Place.Prof.Lang)


    def Upd(self):
        self.Load_Features()

    def Load_Features(self):
        for fIndex in self.dFeature:
            Types = fIndex.Type
            Name = fIndex.Name.replace(" ", "_")
            for type_name in Types:
                handle = self.fHandle.get(type_name)
                if handle:
                    handle(fIndex, Name, self._Level)

