# set.py
import q
from access_data.color_reference import *
from colorist import *

from access_data.Grimoir import *
from Sheet.get import *


class sett:
    def __init__(self):
        pass
    def Core_Level(self, value):
        q.db.Core.L = max(1, min(value, 20))
        q.db.Core.PB = (q.db.Core.L - 1) // 4 + 2
    def Core_Race(self, value): q.db.Core.R = value.replace(" ", "_")
    def Core_Subrace(self, value): q.db.Core.SR = value.replace(" ", "_")
    def Core_Class(self, value): q.db.Core.C = value.replace(" ", "_")
    def Core_Subclass(self, value): q.db.Core.SC = value.replace(" ", "_")
    def Core_Background(self, value): q.db.Core.BG = value.replace(" ", "_")
    #---
    def Atr_Modify(self, key, data):
        q.db.Atr[key].Base = int(data)
    #---
    def Race_Asi_Clear(self): q.db.Race.Rasi = ["", ""]
    def Race_Asi_Modify(self, key, data):
        cdata = q.db.Race
        cdata.Rasi[key] = data
    def Race_Abil_Use(self, key, index, data): 
        q.db.Race.Abil[key]["Use"][index] = data
    def Race_Spell_Use(self, key, spell, data): 
        print(key, spell, data)
        q.db.Race.Abil[key][spell]["Use"] = data
    def Race_Spell_Select(self, key, data): q.db.Race.Abil[key]["Select"][0] = data
    #---
    def Class_Skill_Select_Clear(self):
        cdata = q.db.Class["Skill Select"]
        for idx in range(len(cdata)): cdata[idx] = ""
    def Class_Skill_Select_Modify(self, cat, data):
        cdata = q.db.Class["Skill Select"]
        cdata[cat] = data
    def Class_Abil_Use(self, key, index, data):
        q.db.Class.Abil[key]["Use"][index] = data
    def Class_Abil_Select(self, key, index, data):
        q.db.Class.Abil[key]["Select"][index] = data
    #---
    def Background_Prof_Clear(self):
        cdata = q.db.Background["Prof"]
        for key in cdata:
            plen = len(cdata[key]["Select"])
            cdata[key]["Select"] = [""] * plen
    def Background_Prof_Modify(self, cat, index, data):
        cdata = q.db.Background["Prof"]
        cdata[cat]["Select"][index] = data
    #---
    def Milestone_Top_Clear(self, index):
        cdata = q.db.Milestone
        prefeat = cdata["Feat"][index]
        if prefeat and prefeat in cdata["Data"]:
            cdata["Data"].pop(prefeat)
        cdata["Select"][index] = ""
        cdata["Feat"][index] = ""
        cdata["Asi"][index] = ["", ""]
    def Milestone_Top_Modify(self, index, data):
        cdata = q.db.Milestone
        cdata["Select"][index] = data
        cdata["Feat"][index] = ""
        cdata["Asi"][index] = ["", ""]

    def Milestone_Feat_Clear(self, index):
        cdata = q.db.Milestone
        prefeat = cdata["Feat"][index]
        if prefeat and prefeat in cdata["Data"]:
            cdata["Data"].pop(prefeat)
        cdata["Feat"][index] = ""
    def Milestone_Feat_Modify(self, index, data):
        cdata = q.db.Milestone
        if data not in cdata["Feat"]:
            cdata["Feat"][index] = data
            if data in list_Feat_Select:
                cdata["Data"][data] = {"Select": [""]}
            elif data == "Weapon Master":
                cdata["Data"][data] = {"Select": ["", "", "", ""]}
            else:
                cdata["Data"][data] = {}
    def Milestone_Feat_Select(self, feat, index, data):
        cdata = q.db.Milestone
        if feat in cdata["Data"]: cdata["Data"][feat]["Select"][index] = data
    def Milestone_Feat_Use(self, feat, index, data):
        cdata = q.db.Milestone
        if feat in cdata["Data"]: cdata["Data"][feat]["Use"][index] = data

    def Milestone_Asi_Clear(self, key, index):
        q.db.Milestone["Asi"][key][index] = ""
    def Milestone_Asi_Modify(self, key, index, data):
        q.db.Milestone["Asi"][key][index] = data
    #---
    def Proficiency_Player_Modify(self):
        pass
    #---
    def _Toggle_Cantrip(self, spell, spell_list, max_known):
        current_known = cantrips_known()
        if spell in spell_list:       spell_list.remove(spell)
        elif current_known < max_known: spell_list.append(spell)

    def _Toggle_Spell(self, spell, spell_list, max_known):
        current_known = spells_known()
        if spell in spell_list:       spell_list.remove(spell)
        elif current_known < max_known: spell_list.append(spell)

    def _Toggle_Prepare(self, spell, spell_list, max_known):
        current_prep = spells_prepared()
        if spell in spell_list:       spell_list.remove(spell)
        elif current_prep < max_known: spell_list.append(spell)

    def Spell_Learn(self, spell, level):
        cspell = q.db.Spell["Book"][level]
        sdata = q.pc.Class.spell_data
        if level == 0: self._Toggle_Cantrip(spell, cspell, sdata['cantrips_available'])
        else:          self._Toggle_Spell(spell, cspell, sdata['spells_available'])

    def Spell_Prepare(self, spell, level):
        cspell = q.db.Spell["Prepared"][level]
        sdata = q.pc.Class.spell_data
        self._Toggle_Prepare(spell, cspell, sdata['prepared_available'])
        
    def Spell_Cast(self, level):
        slots = q.db.Spell["Slot"][level]
        for i in range(len(slots)):
            if not slots[i]:
                slots[i] = True
                break
    #---
    def Rest_Long(self):
        if valid_spellclass():
            for level in range(1, 10):
                if level in q.db.Spell["Slot"]:
                    q.db.Spell["Slot"][level] = [False] * len(q.db.Spell["Slot"][level])

    def Rest_Short(self):
        pass
    #---
    def Combat_Health_Hp(self, delta):
        hp = kHP()
        if delta < 0:
            if hp["Temp"] > 0: hp["Temp"] -= 1
            else: hp["Current"] -= 1
        else: hp["Current"] = min(hp["Current"] + 1, hp["Sum"])

    def Combat_Health_Temp(self, delta):
        hp = kHP()
        if delta > 0 or hp["Temp"] > 0: hp["Temp"] += delta

    def Combat_Health_Player(self, data):
        kHP()["Player"] = int(data)

    def Combat_Wizard_Arcane_Ward(self, num):
        ward_data = aClass()["Arcane Ward"]["HP"]
        new_hp = ward_data["Current"] + num
        ward_data["Current"] = max(0, min(new_hp, ward_data["Max"]))

    def Combat_Condition_Modify(self, index, data):
        q.db.Condition[index] = data
    #---
    def Info_Char_Modify(self, name, data):
        q.db.Characteristic[name] = data

    def Info_Desc_Modify(self, name, data):
        q.db.Description[name] = data
    #---
    def Inventory_Backpack_Add(self, cat, item):
        backpack = q.db.Inventory.Backpack
        if item in backpack.keys(): backpack[item][1] += 1
        else:                        backpack[item] = [cat, 1]

    def Inventory_Item_Clear(self, item):
        q.db.Inventory.Backpack.pop(item, None)
        return 0

    def Inventory_Item_Modify(self, item, delta):
        backpack = q.db.Inventory.Backpack
        print(backpack)
        if item not in backpack: backpack[item] = [None, delta]
        else:                    backpack[item][1] += delta
        
        if backpack[item][1] <= 0:
            backpack.pop(item, None)
            
            slot = item_slot(item)
            if slot:
                q.db.Inventory.Closet[slot] = ""
            
            return 0
        
        return backpack[item][1]
    #---
    def Closet_Equip_Clear(self, cat):
        q.db.Inventory.Closet[cat] = ""

    def Closet_Equip_Modify(self, cat, name):
        closet = q.db.Inventory.Closet
        backpack = q.db.Inventory.Backpack
        item = q.w.dItem(name)
        item_type = item.Slot

        if item_type == "Weapon": 
            self.eWeapon(cat, name, item, closet, backpack)
        elif item_type == "Armor": 
            self.eArmor(cat, name, item, closet)
        elif item_type == "Shield": 
            self.eShield(cat, name, item, closet)

    def eWeapon(self, cat, name, item, closet, backpack):
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

    def eArmor(self, cat, name, item, closet):
        str_mod = q.db.Atr["STR"]["Mod"]
        if str_mod < item.Str_Req:  return
        else: closet[cat] = name

    def eShield(self, cat, name, item, closet):
        h1 = closet["Hand_1"]
        if h1 and "Two-handed" in q.w.dItem(h1).Prop: return
        closet["Hand_2"] = name
    #---