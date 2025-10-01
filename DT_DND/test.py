from box import Box
from colorist import *
import sys
import json
from path_helper import get_path

def Load_Json(folder_path, filename):
    file_path = get_path(folder_path, f'{filename}.json')
    try:
        with open(file_path, 'r') as f: 
            return Box(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        red(f"[load_json_data] - (Can't load file path) {file_path}: {e}")
        sys.exit(1)

class PC:
    def __init__(self):
        self.Level = 3
        self.PB = 1
        self.Race = "Elf"
        self.Subrace = "High"
        self.Stats = Box({
            "Atr": Box({"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}),
            "Speed": Box({"Walk": 0, "Climb": 0, "Swim": 0, "Fly": 0, "Burrow": 0}),
            "Vision": Box({"Dark": 0, "Blind": 0, "Tremor": 0, "Tru": 0}),
            "Prof": Box({"Skill": [], "Weapon": [], "Armor": [], "Tool": [], "Lang": []}),
            "Combat": Box({"Initiative": 0, "HP": 0, "HD": 0})
        })
        self.Abil = {}
    
    def Visual(self):
        print(f"Level: {self.Level}, PB: {self.PB}")
        print(f"Race: {self.Race}, Subrace: {self.Subrace}")
        print(f"Atr: {self.Stats.Atr}")
        print(f"Speed: {self.Stats.Speed}")
        print(f"Vision: {self.Stats.Vision}")
        print(f"Prof: {self.Stats.Prof}")
        print(f"Combat: {self.Stats.Combat}")
        print(self.Abil)

class Load:
    def Weapon(self,parent):
        PROF = pc.Stats.Prof.Weapon
        if parent and parent[0] == "Simple": PROF.extend("All Simple")
        elif parent and parent[0] == "Martial": PROF.extend("All Martial")
        else: PROF.extend(parent)

    def Armor(self,parent):
        pc.Stats.Prof.Armor.extend(parent)

    def Skill(self,parent):
        pc.Stats.Prof.Skill.extend(parent)

    def Tool(self,parent):
        pc.Stats.Prof.Tool.extend(parent)

    def Lang(self,parent):
        pc.Stats.Prof.Lang.extend(parent)

    def Selection(self, feature, Name, level):
        Place = pc.Abil
        Place.setdefault(Name, {})
        Past = Place.get(Name, {}).get("Select", [])
        Total_Choices = feature.Choices
        Place[Name]["Select"] = (Past + [""] * Total_Choices)[:Total_Choices]

    def Use(self, feature, Name, level):
        Place = pc.Abil
        Place.setdefault(Name, {})
        past = Place.get(Name, {}).get("Use", [False])
        Total_Uses = feature.Use[level]
        Place[Name]["Use"] = (past + [False] * Total_Uses)[:Total_Uses]

    def Passive(self, feature, Name, level):
        Place = pc.Abil
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
        self.rData = None
        self.srData = None
        self.dFeature = []

        self._Race = None
        self._Subrace = None
        self._Level = None
        self._PB = None

    @property
    def File(self): 
        return f"dist/Race_Json/{self._Race}"

    def Refresh(self):
        self._Race = pc.Race
        self._Subrace = pc.Subrace
        self._Level = pc.Level
        self._PB = pc.PB

        if not self._Race: return

        self.rData = Load_Json(self.File, "Base")
        try: self.srData = Load_Json(self.File, self._Subrace)
        except (FileNotFoundError, json.JSONDecodeError): self.srData = Box({})

        data = self.rData.copy()
        for key, value in self.srData.items():
            if key in data and isinstance(data[key], dict) and isinstance(value, dict): data[key].update(value)
            else: data[key] = value

        self.Data = Box(data)
        self.dFeature = self.Data.Features

        self.Config_Init()
        self.Load_Features()

    def Config_Init(self):
        for key, value in self.Data.items():
            if key == "Prof":
                for prof_key, prof_value in value.items():
                    loader = getattr(self.load, prof_key, None)
                    if loader:
                        loader(prof_value)
            elif hasattr(pc.Stats, key):
                pc.Stats[key].update(value)


    def Load_Features(self):
        level = self._Level
        for fIndex in self.dFeature:
            Types = fIndex.Type
            Name = fIndex.Name.replace(" ", "_")
            for type_name in Types:
                handle = self.fHandle.get(type_name)
                if handle:
                    handle(fIndex, Name, level)

pc = PC()
pc.Visual()
print("-----------------------------")
br = bRace()
br.Refresh()
pc.Visual()
