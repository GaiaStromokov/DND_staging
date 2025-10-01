
import os
from path_helper import get_path
from box import Box

base_path = get_path("dist", "Class_Json")
dir_Class = Box()

for folder in os.listdir(base_path):
    dir_Class[folder] = [f.replace('.json', '') for f in os.listdir(os.path.join(base_path, folder)) if f != "Base.json"]

list_Class = list(dir_Class.keys())

print(dir_Class)
print(list_Class)


Class_List = ["Fighter", "Wizard"]


option_Race = {
    "Empty": ["Empty"],
    "Human": ["Standard", "Variant"],
    "Elf": ["High", "Drow", "Wood", "Shadar Kai"],
    "Dwarf": ["Hill", "Mountain"],
    "Halfling": ["Lightfoot", "Stout"],
    "Gnome": ["Forest", "Rock"],
    "Dragonborn": ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold","Green","Red","Silver","White"],
    "Half Orc": ["Standard"],
    "Tiefling": ["Asmodeus","Baalzebul", "Dispater", "Fierna", "Glasya", "Levistus", "Mammon", "Mephistopheles", "Zariel"],
    "Harengon": ["Standard"]
}

