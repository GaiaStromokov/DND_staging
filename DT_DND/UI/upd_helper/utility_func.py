from dearpygui.dearpygui import *
import q
from colorist import *
from access_data.color_reference import *
import Sheet.get as get


def tgen(name: str):
    n = name.replace("_", " ")
    t = name.replace(" ", "_")
    return n, t


def gen_abil(name: str):
    an = name
    tn = name.replace(" ", "_")
    return an, tn 

def item_delete(tag):
    if does_item_exist(tag): delete_item(item=tag, children_only=False)

def item_clear(tag):
    if does_item_exist(tag): delete_item(item=tag, children_only=True)
    



def item_detail_handler(item):
    data = q.w.dItem(item)

    item_type = data.Slot
    if item_type == "Weapon":
        if "Shield" in data.Cat:
            item_type = "Shield"

    detail_functions = {
        "Weapon": item_detail_weapon,
        "Shield": item_detail_shield,
        "Armor": item_detail_armor,
    }

    if func := detail_functions.get(item_type):
        func(data)


def item_detail_weapon(data):
    with group(horizontal=True):
        if data.get("Reach"):
            add_text("Reach", color=c_h1)
            add_text(data.Reach, color=c_text)
        if data.get("Range"):
            add_text("Range", color=c_h1)
            add_text(data.Range, color=c_text)
        add_text("Damage", color=c_h1)
        add_text(data.Damage, color=c_h5)
        add_text(data.Type, color=c_damagetype[f"{data.Type}"])

    with group(horizontal=True):
        add_text("Prop", color=c_h1)
        for prop in data.Prop:
            add_text(f"{prop}", color=c_text)
        add_text("Rarity", color=c_h1)
        add_text(get.item_rarity(data.Tier), color=c_rarity[f"{get.item_rarity(data.Tier)}"])
        add_text("Weight", color=c_h1)
        add_text(data.Weight, color=c_text)
        add_text("Cost", color=c_h1)
        add_text(data.Cost, color=c_h9)

def item_detail_shield(data):
    with group(horizontal=True):
        add_text("AC", color=c_h1)
        add_text(data.AC, color=c_text)
        add_text("Rarity", color=c_h1)
        add_text(get.item_rarity(data.Tier), color=c_rarity[f"{get.item_rarity(data.Tier)}"])
        add_text("Weight", color=c_h1)
        add_text(data.Weight, color=c_text)
        add_text("Cost", color=c_h1)
        add_text(data.Cost, color=c_h9)

def item_detail_armor(data):
    pass

def spell_detail(spell):
    try: data = get.Grimoir[spell]
    except (KeyError, AttributeError, TypeError): return  
    with group(horizontal=True):
        add_text("Level", color=c_h1)
        if data["Level"] == 0: add_text("Cantrip", color=c_text)
        else: add_text(data["Level"], color=c_text)
        add_text("School", color=c_h1)
        add_text(data["School"], color=f"{c_spell_school[data['School']]}")
    with group(horizontal=True):
        add_text("Range", color=c_h1)
        add_text(data["Range"], color=c_text)
        add_text("Components", color=c_h1)
        add_text(data["Components"], color=c_text)
    with group(horizontal=True):
        add_text("Casting Time", color=c_h1)
        add_text(data["Casting Time"], color=c_text)
        add_text("Duration", color=c_h1)
        add_text(data["Duration"], color=c_text)
    with group(horizontal=True):
        if data["Ritual"]:
            add_text("Ritual", color=c_h1)
            add_text(data["Ritual"], color=c_text)
        if data["Concentration"]:
            add_text("Concentration", color=c_h1)
            add_text(data["Concentration"], color=c_text)
    with group(horizontal=False):
        add_text("Description", color=c_h1)
        add_text(data["Desc"], color=c_text, wrap=420)
