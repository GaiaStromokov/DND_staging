# set.py
import q
from access_data.color_reference import *
from colorist import *

from access_data.Grimoir import *
from Sheet.get import *



def Level(value):
    q.db.Core.L = max(1, min(value, 20))
    q.db.Core.PB = (q.db.Core.L - 1) // 4 + 2

def Class(value): q.db.Core.C = value
def Subclass(value): q.db.Core.SC = value
def Race(value): q.db.Core.R = value
def Subrace(value): q.db.Core.SR = value
def Background(value): q.db.Core.BG = value


def input_rasi(sender, data, user_data):
    cdata = q.db.Race
    key = user_data[0]
    if key == "Clear": cdata.Rasi = ["", ""]
    else: cdata.Rasi[key] = data


def use_race(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    q.db.Race.Abil[key]["Use"][index] = data


def use_race_spell(sender, data, user_data):
    key = user_data[0]
    spell = user_data[1]
    q.db.Race.Abil[key][spell]["Use"] = data


def select_race_spell(sender, data, user_data):
    key = user_data[0]
    q.db.Race.Abil[key]["Select"][0] = data


def input_base_atr(sender, data, user_data):
    key = user_data[0]
    q.db.Atr[key].Base = int(data)


def select_prof_background(sender, data, user_data):
    cdata = q.db.Background["Prof"]
    cat = user_data[0]
    index = user_data[1]
    
    if data != "Clear":
        cdata[cat]["Select"][index] = data
    else:
        for key in cdata:
            plen = len(cdata[key]["Select"])
            cdata[key]["Select"] = [""] * plen


def select_prof_player(sender, data, user_data):
    pass
    # idx = user_data[0]
    # cat = idx
    # if idx in ["Artisan", "Gaming", "Musical"]:
    #     cat = "Tool"

    # item = user_data[1]
    # prof_list = q.db.Prof[cat]["Player"]
    


def clear_level_select_milestone(sender, data, user_data):
    cdata = q.db.Milestone
    index = user_data[0]
    if cdata["Feat"][index]:
        prefeat = cdata["Feat"][index]
        for key in list(cdata["Data"].keys()):
            if prefeat == key:
                cdata["Data"].pop(key)
                        
    cdata["Select"][index] = ""
    cdata["Feat"][index] = ""
    cdata["Asi"][index] = ["", ""]


def select_level_milestone(sender, data, user_data):
    cdata = q.db.Milestone
    index = user_data[0]
    cdata["Select"][index] = data
    
    cdata["Feat"][index] = ""
    cdata["Asi"][index] = ["", ""]


def select_feat_milestone(sender, data, user_data):
    cdata = q.db.Milestone
    index = user_data[0]
    if data not in cdata["Feat"]:
        cdata["Feat"][index] = data
    
        if data in list_Feat_Select:
            cdata["Data"][data] = {"Select": [""]}
        elif data == "Weapon Master":
            cdata["Data"][data] = {"Select": ["", "", "", ""]}
        else: 
            cdata["Data"][data] = {}


def choice_feat_milestone(sender, data, user_data):
    cdata = q.db.Milestone
    feat = user_data[0]
    index = user_data[1]
    if data == "Clear":
        output = ""
    else:
        output = data
    
    if feat in list(cdata["Data"].keys()):
        cdata["Data"][feat]["Select"][index] = output


def use_feat_milestone(sender, data, user_data):
    cdata = q.db.Milestone
    feat = user_data[0]
    index = user_data[1]
    
    if feat in list(cdata["Data"].keys()):
        cdata["Data"][feat]["Use"][index] = data


def select_asi_milestone(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    q.db.Milestone["Asi"][key][index] = data


def use_class(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    q.db.Class.Abil[key]["Use"][index] = data


def select_skill_class(sender, data, user_data):
    cdata = q.db.Class["Skill Select"]
    cat = user_data[0]
    if cat != "Clear":
        cdata[cat] = data
    else: 
        for idx, val in enumerate(cdata):
            cdata[idx] = ""


def select_class(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    q.db.Class.Abil[key]["Select"][index] = data


def learn_spell(sender, data, user_data):
    spell = user_data[0]
    level = user_data[1]
    cspell = q.db.Spell["Book"]
    sdata = q.pc.Class.spell_data
    if level == 0:
        max_known = sdata['cantrips_available']
        current_known = cantrips_known()
        if spell not in cspell[level]:  # add spell
            if current_known < max_known:
                cspell[level].append(spell)
        elif spell in cspell[level]:   # remove spell
            cspell[level].remove(spell)
    else:
        max_known = sdata['spells_available']
        current_known = spells_known()
        if spell not in cspell[level]:  # add spell
            if current_known < max_known:
                cspell[level].append(spell)
        elif spell in cspell[level]:   # remove spell
            cspell[level].remove(spell)


def prepare_spell(sender, data, user_data):
    spell = user_data[0]
    level = user_data[1]
    
    cspell = q.db.Spell["Prepared"]
    sdata = q.pc.Class.spell_data

    max_prep = sdata['prepared_available']
    current_prep = spells_prepared()

    if spell not in cspell[level]:  # add spell
        if current_prep < max_prep:
            cspell[level].append(spell)
    elif spell in cspell[level]:   # remove spell
        cspell[level].remove(spell)


def cast_spell(sender, data, user_data):
    level = user_data[0]
    slots = q.db.Spell["Slot"][level]
    for i in range(len(slots)):
        if not slots[i]:
            slots[i] = True
            break


def long_rest(sender, data, user_data):
    if valid_spellclass():
        for level in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            q.db.Spell["Slot"][level] = [False] * len(q.db.Spell["Slot"][level])


def mod_health(sender, data, user_data):
    place, delta = user_data
    hp = kHP()
    
    if place == "Temp":
        if delta > 0 or hp["Temp"] > 0:
            hp["Temp"] += delta
            
    elif place == "HP":
        if delta < 0:
            if hp["Temp"] >= 1 and hp["Temp"] > 0:
                hp["Temp"] -= 1
            else:
                hp["Current"] -= 1
        else:
            hp["Current"] = min(hp["Current"] + 1, hp["Sum"])


def mod_hp_player(sender, data, user_data):
    kHP()["Player"] = int(data)


def mod_arcane_ward(sender, data, user_data):
    num = user_data[0]
    max_hp = aClass()["Arcane Ward"]["HP"]["Max"]
    current_hp = aClass()["Arcane Ward"]["HP"]["Current"]
    new_hp = current_hp + num
    new_hp = max(0, min(new_hp, max_hp))
    aClass()["Arcane Ward"]["HP"]["Current"] = new_hp


def select_player_condition(sender, data, user_data):
    index = user_data[0]
    q.db.Condition[index] = data


def input_characteristic(sender, data, user_data):
    name = user_data[0]
    q.db.Characteristic[name] = data


def input_description(sender, data, user_data):
    name = user_data[0]
    q.db.Description[name] = data


def add_item_bazaar(sender, data, user_data):
    backpack = q.db.Inventory.Backpack
    cat = user_data[0]
    item = user_data[1]
    if item in backpack.keys():
        backpack[item][1] += 1
    else:
        backpack[item] = [cat, 1]


def mod_item_backpack(sender, data, user_data):
    item = user_data[0]
    delta = user_data[1]
    backpack = q.db.Inventory.Backpack
    if delta == "Clear":
        backpack.pop(item, None)
        return 0
    if item not in backpack: backpack[item] = [None, delta]
    else: backpack[item][1] += delta
    if backpack[item][1] <= 0:
        backpack.pop(item, None)
        return 0
    return backpack[item][1]


def Equip_Equip(sender, data, user_data):
    cat = user_data[0]
    equips = q.db.Inventory.Equip
    backpack = q.db.Inventory.Backpack
    two_handed_weapons = q.w.prop("Two-handed")

    if data == "Clear":
        equips[cat] = ""
        return

    if data in q.w.slot("Weapon"):
        Equip_1 = equips.get("Hand_1")
        Equip_2 = equips.get("Hand_2")

        def is_versatile(item):
            return item in q.w.prop("Versatile")

        if cat == "Hand_1":
            if data in two_handed_weapons:
                equips[cat] = data
                equips["Hand_2"] = ""
                return
            if data == Equip_2 and not is_versatile(data):
                owned = backpack[data][1]
                if owned <= 1:
                    return
        elif cat == "Hand_2":
            if Equip_1 in two_handed_weapons:
                return
            if data == Equip_1 and not is_versatile(data):
                owned = backpack[data][1]
                if owned <= 1:
                    return

        equips[cat] = data
        return

    equips[cat] = data
