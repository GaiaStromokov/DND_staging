
from manager.components.Background_comp import bBackground
from manager.components.Class_comp import bClass
from manager.components.Milestone_comp import bMilestone
from manager.components.Race_comp import bRace
from manager.components.Equipment_comp import Bazaar
import q
import Sheet.get as g
from colorist import *

class Character():
    def __init__(self):
        pass
    def start_configuration(self):
        self.init_schema()
        self.Class.pre_Upd()
        self.Race.Upd()
        self.Class.Upd()
        self.recalculate_stats()
        self.update_spells()

    def new_Level(self):
        self.Race.Upd()
        self.Class.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()
        self.update_spells()

    def init_schema(self):
        self.Race = bRace()
        self.Class = bClass()
        self.Background = bBackground()
        self.Milestone = bMilestone()
        
        
    @property
    def Atr(self):
        cdata = q.db.Atr
        Class = self.Class.Atr
        Milestone = self.Milestone.Atr
        return {"STR":cdata["STR"]["Base"]+cdata["STR"]["Rasi"]+Class["STR"]+Milestone["STR"],"DEX":cdata["DEX"]["Base"]+cdata["DEX"]["Rasi"]+Class["DEX"]+Milestone["DEX"],"CON":cdata["CON"]["Base"]+cdata["CON"]["Rasi"]+Class["CON"]+Milestone["CON"],"INT":cdata["INT"]["Base"]+cdata["INT"]["Rasi"]+Class["INT"]+Milestone["INT"],"WIS":cdata["WIS"]["Base"]+cdata["WIS"]["Rasi"]+Class["WIS"]+Milestone["WIS"],"CHA":cdata["CHA"]["Base"]+cdata["CHA"]["Rasi"]+Class["CHA"]+Milestone["STR"]}

    @property
    def Prof(self):
        k_prof = q.db.Prof
        Race = self.Race
        Class = self.Class
        Background = self.Background
        Milestone = self.Milestone
        return {"Weapon":Race.Weapon+k_prof["Weapon"]["Race"]+Class.Weapon+k_prof["Weapon"]["Class"]+Background.Weapon+k_prof["Weapon"]["Background"]+Milestone.Weapon+k_prof["Weapon"]["Feat"]+k_prof["Weapon"]["Player"],"Armor":Race.Armor+k_prof["Armor"]["Race"]+Class.Armor+k_prof["Armor"]["Class"]+Background.Armor+k_prof["Armor"]["Background"]+Milestone.Armor+k_prof["Armor"]["Feat"]+k_prof["Armor"]["Player"],"Tool":Race.Tool+k_prof["Tool"]["Race"]+Class.Tool+k_prof["Tool"]["Class"]+Background.Tool+k_prof["Tool"]["Background"]+Milestone.Tool+k_prof["Tool"]["Feat"]+k_prof["Tool"]["Player"],"Lang":Race.Lang+k_prof["Lang"]["Race"]+Class.Lang+k_prof["Lang"]["Class"]+Background.Lang+k_prof["Lang"]["Background"]+Milestone.Lang+k_prof["Lang"]["Feat"]+k_prof["Lang"]["Player"]}



    @property
    def Skill(self):
        proficient_skills = set(self.Race.Skill) | set(self.Class.Skill+[skill for skill in g.sClass() if skill]) | set(self.Background.Skill) | set(self.Milestone.Skill)
        return {skill: skill in proficient_skills for skill in g.list_Skill}
    
    @property
    def Speed(self):
        Race = self.Race
        Milestone = self.Milestone
        return {speed: Race.Speed[speed] + Milestone.Speed[speed] for speed in g.list_Speed}

    @property
    def Vision(self):
        Race = self.Race
        Milestone = self.Milestone
        return {vision: Race.Vision[vision] + Milestone.Vision[vision] for vision in g.list_Vision}

    @property
    def Initiative(self):
        return q.db.Atr["DEX"]["Mod"] + self.Race.Initiative + self.Class.Initiative + self.Milestone.Initiative

    @property
    def HP(self):
        return q.db.HP["Player"] + self.Race.HP + self.Class.HP


    def new_Race(self):
        self.wipe_data("Race Abil")
        self.Race = bRace()
        self.Race.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()

    def new_Class(self):
        self.wipe_data("Class Abil")
        self.wipe_data("Class Spell")
        self.Class = bClass()
        self.Class.pre_Upd()
        self.Class.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()
        self.update_spells()
    
    def new_Background(self):
        self.wipe_data("Background Data")
        self.Background = bBackground()
        self.recalculate_stats()
        

    def update_Atr(self):
        self.wipe_data("Atr")
        self.Milestone.Upd()
        self.recalculate_stats()
        self.update_spells()

    def update_Class_Select(self):
        self.Class.pre_Upd()
        self.Class.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()

    def update_Spell_Learn(self): pass

    def update_Spell_Prepare(self): pass

    def update_Spell_Cast(self): pass

    def update_Background_Prof(self):
        self.Background = bBackground()
        self.recalculate_stats()
        

    def update_Milestone_Feat(self):
        self.update_Atr()
        

    def update_spells(self):
        if g.valid_spellclass(): self.Class.Spell_config()


    def wipe_data(self, source):
        if source == "Race Abil": q.db.Race.Abil={}
        if source == "Class Abil": q.db.Class.Abil={}
        if source == "Class Spell": q.db.Spell=g.spell_default
        if source == "Background Data": q.db.Background={"Prof": {}, "Equipment": {}}

    def recalculate_stats(self):
        self.pull_atr_data()
        self.sum_Skill()
        self.sum_Speed()
        self.sum_Vision()
        self.sum_Initiative()
        self.sum_HP()
        self.sum_AC()

    def pull_atr_data(self):
        cdata = q.db.Race.Rasi
        for atr in g.list_Atr:
            q.db.Atr[atr]["Rasi"] = 0
            for i, rasi_list in enumerate(cdata):
                if atr in rasi_list:
                    q.db.Atr[atr]["Rasi"] = i + 1
                    break
        
        for atr in g.list_Atr:
            val = self.Atr[atr]
            mod = (val- 10) // 2
            q.db.Atr[atr]["Val"] = val
            q.db.Atr[atr]["Mod"] = mod

    @property
    def Prof(self):
        K_weapon = q.db.Prof["Weapon"]
        k_armor = q.db.Prof["Armor"]
        k_tool = q.db.Prof["Tool"]
        k_lang = q.db.Prof["Lang"]

        return {
            "Weapon": list(set(self.Race.Weapon + K_weapon["Race"] + self.Class.Weapon + K_weapon["Class"] + self.Background.Weapon + K_weapon["Background"] + self.Milestone.Weapon + K_weapon["Feat"] + K_weapon["Player"])),
            "Armor": list(set(self.Race.Armor + k_armor["Race"] + self.Class.Armor + k_armor["Class"] + self.Background.Armor + k_armor["Background"] + self.Milestone.Armor + k_armor["Feat"] + k_armor["Player"])),
            "Tool": list(set(self.Race.Tool + k_tool["Race"] + self.Class.Tool + k_tool["Class"] + self.Background.Tool + k_tool["Background"] + self.Milestone.Tool + k_tool["Feat"] + k_tool["Player"])),
            "Lang": list(set(self.Race.Lang + k_lang["Race"] + self.Class.Lang + k_lang["Class"] + self.Background.Lang + k_lang["Background"] + self.Milestone.Lang + k_lang["Feat"] + k_lang["Player"])),
        }



    def sum_Skill(self):
        Skill = self.Skill
        for skill in g.list_Skill:
            q.db.Skill[skill]["Mod"] = q.db.Atr[g.dict_Skill[skill]["Atr"]]["Mod"]
            if Skill[skill]: q.db.Skill[skill]["Mod"] += q.db.Core.PB


    
    def sum_Speed(self):pass
    def sum_Vision(self): pass
    def sum_Initiative(self): pass


    def sum_HP(self):
        sum = self.HP
        q.db.HP["Sum"] = sum
        q.db.HP["Current"] = sum
    
    
    def sum_AC(self):
        dex_mod = q.db.Atr["DEX"]["Mod"]

        base_ac = 10
        dex = dex_mod

        armor = q.db.Inventory.Closet["Armor"]
        if armor:
            item = q.w.Item(armor)
            prof = item.Name in self.Prof["Armor"]
            if prof:
                base_ac = item.AC
                dex = min(dex_mod, item.Dex_Max)

        q.db.AC.Base = base_ac
        q.db.AC.Dex = dex
        q.db.AC.Sum = base_ac + dex

        



def init_pc():
    if q.db is None:
        red("[init_pc] ERROR : Not loaded")
        return
    q.pc = Character()
    q.w = Bazaar()
    green("[init_pc] - player now exists")