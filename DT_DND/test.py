from box import Box
from colorist import *
import sys
import json
from path_helper import get_path



def dTemplate():
    Data = Box({
        "Atr": Box({"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}),
        "Speed": Box({"Walk": 0, "Climb": 0, "Swim": 0, "Fly": 0, "Burrow": 0}),
        "Vision": Box({"Dark": 0, "Blind": 0, "Tremor": 0, "Tru": 0}),
        "Prof": Box({"Skill": [], "Weapon": [], "Armor": [], "Tool": [], "Lang": []}),
        "Combat": Box({"Initiative": 0, "HP": 0, "HD": 0}),
        "Features": []   
    })
    return Data

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
        self.Subrace = "Shadar Kai"
        self.Data = dTemplate()
        self.Abil = {}
    
    def Visual(self):
        print(f"Level: {self.Level}, PB: {self.PB}")
        print(f"Race: {self.Race}, Subrace: {self.Subrace}")
        print(f"Atr: {self.Data.Atr}")
        print(f"Speed: {self.Data.Speed}")
        print(f"Vision: {self.Data.Vision}")
        print(f"Prof: {self.Data.Prof}")
        print(f"Combat: {self.Data.Combat}")
        print("Features:")
        for feature in self.Data.Features:
            print(f"  - {feature}")
        for abil in self.Abil.keys():
            print(f"  -{abil} -{self.Abil[abil]}")

class Load:
    def Weapon(self,parent):
        PROF = pc.Data.Prof.Weapon
        if parent and parent[0] == "Simple": PROF.append("All Simple")
        elif parent and parent[0] == "Martial": PROF.append("All Martial")
        else: PROF.extend(parent)

    def Spell(self, feature, Name, level, pb):
        Place = pc.Abil
        Place.setdefault(Name, {})
        
        if hasattr(feature, 'Given'):
            for req_level, spell in feature.Given.items():
                if level >= int(req_level):
                    if spell not in Place[Name]:
                        Place[Name][spell] = [False]


    def Selection(self, feature, Name, level, pb):
            Place = pc.Abil
            Place.setdefault(Name, {})
            Past = Place.get(Name, {}).get("Select", [])
            Total_Choices = feature.Choices
            Place[Name]["Select"] = (Past + [""] * Total_Choices)[:Total_Choices]
            
            if hasattr(feature, 'Desc'): Place[Name]["Desc"] = feature.Desc
            if hasattr(feature, 'Multi_Desc'): Place[Name]["Multi_Desc"] = feature.Multi_Desc
    
    def Dragon(self, feature, Name, level, pb):
        pass
        


    def Use(self, feature, Name, level, pb):
        Place = pc.Abil
        Place.setdefault(Name, {})
        past = Place.get(Name, {}).get("Use", [False])
        
        if hasattr(feature, 'Use'):
            if isinstance(feature.Use, list): Total_Uses = feature.Use[level]
            elif feature.Use == "PB": Total_Uses = pb
            else: Total_Uses = int(feature.Use)
            Place[Name]["Use"] = (past + [False] * Total_Uses)[:Total_Uses]
        
        if hasattr(feature, 'Desc'): Place[Name]["Desc"] = feature.Desc
        if hasattr(feature, 'lDesc'): Place[Name]["Desc"] = feature.lDesc[str(max(int(k) for k in feature.lDesc if int(k) <= level))]


    def Passive(self, feature, Name, level, pb):
        Place = pc.Abil
        Place.setdefault(Name, {})
        if hasattr(feature, 'Amount'):
            Place[Name]["Amount"] = feature.Amount[level]
        if hasattr(feature, 'Desc'):
            Place[Name]["Desc"] = list(feature.Desc)

class bRace:
    def __init__(self):
        self.load = Load()
        self.fHandle = {
            "Selection": self.load.Selection,
            "Use": self.load.Use,
            "Passive": self.load.Passive,
            "Spell": self.load.Spell
        }

        self._Race = None
        self._Subrace = None
        self._Level = None
        self._PB = None

    @property
    def File(self): 
        return f"dist/Race_Json/{self._Race}"

    def apply_merge(self, source):
            for idx in ["Speed", "Vision"]:
                for key, value in source[idx].items():
                    pc.Data[idx][key] += value

            for key, value in source["Prof"].items():
                if key == "Weapon": self.load.Weapon(value)
                else: pc.Data.Prof[key].extend(value)
                
            pc.Data.Features.extend(source.Features)
        
    def Refresh(self):
        self._Race = pc.Race
        self._Subrace = pc.Subrace.replace(" ", "_")
        self._Level = pc.Level
        self._PB = pc.PB

        if not self._Race: return

        rData = Load_Json(self.File, "Base")

        if self._Subrace not in ["", "Empty"]: srData = Load_Json(self.File, self._Subrace)
        else: srData = dTemplate()
            
        self.apply_merge(rData)
        self.apply_merge(srData)

        self.Load_Features()

    def Load_Features(self):
            for fIndex in pc.Data.Features:
                if self._Level >= fIndex.Level:
                    Types = fIndex.Type
                    Name = fIndex.Name.replace(" ", "_")
                    for type_name in Types:
                        handle = self.fHandle.get(type_name)
                        if handle:
                            handle(fIndex, Name, self._Level, self._PB)

pc = PC()
pc.Visual()
print("-----------------------------")
br = bRace()
br.Refresh()
pc.Visual()
