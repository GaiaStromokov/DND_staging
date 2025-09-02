from ui.upd_helper_import import *
from ui.upd_class_import import *
sett = sett()



class backend_populate:
    def __init__(self):
        self.ACTION = upd_actions()
        self.BACKGROUND = upd_background()
        self.BACKPACK = upd_backpack()
        self.BAZAAR = upd_bazaar()
        self.CLASS = upd_class()
        self.CLOSET = upd_closet()
        self.MILESTONE = upd_milestone()
        self.RACE = upd_race()
        self.SHEET = upd_sheet()
        self.SPELL = upd_spell()

    def Startup(self):
        self.Static()
        self.Dynamic()
        self.BAZAAR.whole()
    
    def All(self):
        self.Static()
        self.Dynamic()
    
    def Dynamic(self):
        self.RACE.whole()
        self.CLASS.whole()
        self.BACKGROUND.whole()
        self.MILESTONE.whole()
        self.Inventory()

    def Race(self): 
        self.Generic()
        self.RACE.whole()
        self.MILESTONE.whole()

    def Class(self):
        self.Generic()
        self.CLASS.whole()
        self.SPELL.whole()

    def Background(self): 
        self.Generic()
        self.BACKGROUND.whole()

    def Atr(self):
        self.Generic()
        self.ACTION.weapon()
        self.RACE.whole()
        self.CLASS.whole()
        self.MILESTONE.whole()
        self.SPELL.whole()

    def Spell(self): 
        self.SPELL.whole()

    def Arcane_Ward(self):
        pass

    def Milestone(self): 
        self.Atr()
    
    def Generic(self):
        self.SHEET.core()
        self.SHEET.skills()
        self.SHEET.health()
        self.SHEET.initiative()
        self.SHEET.vision()
        self.SHEET.speed()
        self.SHEET.prof()
        self.SHEET.attributes()
        self.SHEET.ac()
        self.SHEET.character()
        
    def Static(self):
        self.Generic()

    def HP(self): 
        self.SHEET.health()
        
    def Condition(self):
        self.SHEET.conditions()
        
    def characteristics(self): 
        self.SHEET.character()

    def Inventory(self): 
        self.Backpack()
        self.Closet()
        self.ACTION.whole()
        
    def Backpack(self): 
        self.BACKPACK.whole()
        
    def Inventory_Modify(self): 
        self.BACKPACK.whole()
        self.ACTION.whole()
        self.CLOSET.whole()
        self.SHEET.ac()
        
    def Closet(self): 
        self.ACTION.whole()
        self.CLOSET.whole()
        self.Armor()

    def Armor(self): 
        self.SHEET.ac()
        
class backend_stage:
    def __init__(self, populate):
        self.Populate = populate
        self.stage_map = {
            "All": self.Populate.All,
            "Level": self.Populate.All,
            "Long Rest": self.Populate.All,
            "Race": self.Populate.Race,
            "Class": self.Populate.Class,
            "Background": self.Populate.Background,
            "Atr": self.Populate.Atr,
            "Spell": self.Populate.Spell,
            "Arcane Ward": self.Populate.Arcane_Ward,
            "Milestone": self.Populate.Milestone,
            "Background Prof Select": self.Populate.Background,
            "Generic": self.Populate.Generic,
            "HP": self.Populate.HP,
            "Condition": self.Populate.Condition,
            "Characteristic": self.Populate.characteristics,
            "Description": self.Populate.characteristics,
            "Bazaar Add Item": self.Populate.Inventory,
            
            "Backpack Delete Item": self.Populate.Inventory_Modify,
            "Backpack Modify Item": self.Populate.Inventory_Modify,
            "Refresh Closet": self.Populate.Inventory_Modify,
            "Mod Armor": self.Populate.Armor
        }
    def populate_fields(self, source):
        self.stage_map[source]()
        
    def check_Class(self): 
        if get.valid_class() == False: 
            sett.Core_Subclass("")

    def Core_Level(self, sender, data, user_data):
        math = int(q.db.Core.L + user_data[0])
        if math not in [0, 21]:
            sett.Core_Level(math)
            self.check_Class()
            q.pc.new_Level()
            self.populate_fields("All")

    def Core_Race(self, sender, data, user_data):
        old_obj = q.db.Core.R
        if old_obj != data:
            green(f"[stage_Race] - changing race to {data}")
            sett.Core_Race(data)
            sett.Core_Subrace("")
            q.pc.new_Race()
            self.populate_fields("Race")
        else: 
            red(f"[stage_Race] - race not changed")

    def Core_Subrace(self, sender, data, user_data):
        old_obj = q.db.Core.SR
        if old_obj != data:
            green(f"[stage_Subrace] - changing subrace to {data}")
            sett.Core_Subrace(data)
            q.pc.new_Race()
            self.populate_fields("Race")
        else:
            red(f"[stage_Subrace] - subrace not changed")

    def Core_Class(self, sender, data, user_data):
        old_obj = q.db.Core.C
        if old_obj != data:
            green(f"[stage_Class] - changing class to {data}")
            sett.Core_Class(data)
            sett.Core_Subclass("")
            q.pc.new_Class()
            self.populate_fields("Class")
        else: 
            red(f"[stage_Class] - class not changed")

    def Core_Subclass(self, sender, data, user_data):
        old_obj = q.db.Core.SC
        if old_obj != data:
            green(f"[stage_Subclass] - changing subclass to {data}")
            sett.Core_Subclass(data)
            q.pc.new_Class()
            self.populate_fields("Class")
        else: 
            red(f"[stage_Subclass] - subclass not changed")

    def Core_Background(self, sender, data, user_data):
        old_obj = q.db.Core.BG
        if old_obj != data:
            green(f"[stage_Background] - changing background to {data}")
            sett.Core_Background(data)
            q.pc.new_Background()
            self.populate_fields("Background")
        else: 
            red(f"[stage_Background] - background not changed")

    def Atr_Base_Modify(self, sender, data, user_data):
        key = user_data[0]
        sett.Atr_Modify(key, data)
        q.pc.update_Atr()
        self.populate_fields("Atr")

    def Race_Asi_Modify(self, sender, data, user_data):
        print(f"Race Asi Modify: {data}, {user_data}")
        key = user_data[0]
        if key == "Clear":  sett.Race_Asi_Clear()
        else:  sett.Race_Asi_Modify(key, data)
        q.pc.update_Atr()
        self.populate_fields("Atr")

    def Race_Abil_Use(self, sender, data, user_data):
        key, index = user_data
        sett.Race_Abil_Use(key, index, data)

    def Race_Spell_Use(self, sender, data, user_data):
        key, spell = user_data
        sett.Race_Spell_Use(key, spell, data)

    def Race_Spell_Select(self, sender, data, user_data):
        key = user_data[0]
        sett.Race_Spell_Select(key, data)
        self.populate_fields("Race")

    def Milestone_Top_Select(self, sender, data, user_data):
        index = user_data[0]
        if data == "Clear": sett.Milestone_Top_Clear(index)
        else: sett.Milestone_Top_Modify(index, data)
        q.pc.update_Milestone_Feat()
        self.populate_fields("All")

    def Milestone_Feat_Select(self, sender, data, user_data):
        index = user_data[0]
        feat = data
        if data == "Clear": sett.Milestone_Feat_Clear(index)
        else: sett.Milestone_Feat_Select(index, feat)
        q.pc.update_Milestone_Feat()
        self.populate_fields("Milestone")
        
        
    def Milestone_Feat_Modify(self, sender, data, user_data):
        script, feat, index = user_data
        sett.Milestone_Feat_Modify(data, script, feat, index)
        q.pc.update_Milestone_Feat()
        self.populate_fields("Milestone")



    def Milestone_Feat_Use(self, sender, data, user_data):
        feat, index = user_data
        sett.Milestone_Feat_Use(feat, index, data)

    def Milestone_Asi_Select(self, sender, data, user_data):
        key, index = user_data
        if data == "Clear": sett.Milestone_Asi_Clear(key, index)
        else: sett.Milestone_Asi_Modify(key, index, data)
        q.pc.update_Atr()
        self.populate_fields("Atr")

    def Class_Use(self, sender, data, user_data):
        key, index = user_data
        sett.Class_Abil_Use(key, index, data)

    def Class_Skill_Select(self, sender, data, user_data):
        
        script = user_data[0]
        if script == "Clear": sett.Class_Skill_Select_Clear()
        else: sett.Class_Skill_Select_Modify(script, data)
        q.pc.update_Class_Select()
        self.populate_fields("Class")

    def Class_Abil_Select(self, sender, data, user_data):
        key, index = user_data
        sett.Class_Abil_Select(key, index, data)
        q.pc.update_Class_Select()
        self.populate_fields("Class")

    def Spell_Learn(self, sender, data, user_data):
        spell, level = user_data
        sett.Spell_Learn(spell, level)
        q.pc.update_Spell_Learn()
        self.populate_fields("Spell")

    def Spell_Prepare(self, sender, data, user_data):
        spell, level = user_data
        sett.Spell_Prepare(spell, level)
        q.pc.update_Spell_Prepare()
        self.populate_fields("Spell")

    def Spell_Cast(self, sender, data, user_data):
        level = user_data[0]
        sett.Spell_Cast(level)
        q.pc.update_Spell_Cast()
        self.populate_fields("Spell")

    def Background_Prof_Select(self, sender, data, user_data):
        if data == "Clear": 
            sett.Background_Prof_Clear()
        else:
            cat, index = user_data
            sett.Background_Prof_Modify(cat, index, data)
        q.pc.update_Background_Prof()
        self.populate_fields("Background Prof Select")

    def Long_Rest(self, sender, data, user_data):
        sett.Rest_Long_Rest()
        self.populate_fields("Long Rest")

    def Player_Health_Mod(self, sender, data, user_data):
        place, delta = user_data
        if place == "Temp": 
            sett.Combat_Health_Temp(delta)
        else: 
            sett.Combat_Health_Hp(delta)
        self.populate_fields("HP")

    def Player_Health_Set(self, sender, data, user_data):
        sett.Combat_Health_Player(data)
        q.pc.recalculate_stats()
        self.populate_fields("HP")

    def Class_Wizard_Abjuration_Arcane_Ward(self, sender, data, user_data):
        num = user_data[0]
        sett.Combat_Wizard_Arcane_Ward(num)
        self.populate_fields("Arcane Ward")

    def Player_Prof_Select(self, sender, data, user_data):
        sett.Proficiency_Player_Modify() 
        q.pc.recalculate_stats()
        self.populate_fields("Generic")

    def Player_Condition_Modify(self, sender, data, user_data):
        index = user_data[0]
        sett.Combat_Condition_Modify(index, data)
        self.populate_fields("Condition")

    def Info_Char_Input(self, sender, data, user_data):
        name = user_data[0]
        sett.Info_Char_Modify(name, data)
        self.populate_fields("Characteristic")

    def Info_Desc_Input(self, sender, data, user_data):
        name = user_data[0]
        sett.Info_Desc_Modify(name, data)
        self.populate_fields("Description")

    def Inventory_Bazaar_Item_Add(self, sender, data, user_data):
        cat, item = user_data
        sett.Inventory_Backpack_Add(cat, item)
        self.populate_fields("Bazaar Add Item")

    def Inventory_Backpack_Item_Modify(self, sender, data, user_data):
        item, delta = user_data
        if delta == "Clear": 
            value = sett.Inventory_Item_Clear(item)
        else: 
            value = sett.Inventory_Item_Modify(item, delta)
        print(f"Value: {value}")
        if value == 0: 
            self.populate_fields("Backpack Delete Item")
        else: 
            self.populate_fields("Backpack Modify Item")

    def Closet_Item_Equip(self, sender, data, user_data):
        cat = user_data[0]
        delta = user_data[1]
        
        if delta == "Clear":
            sett.Closet_Equip_Clear(cat)
        elif delta == "Modify":
            package = data.replace(' + ', 'PPP').replace(' ', '_')
            sett.Closet_Equip_Modify(cat, package)
        else:
            red("error")

        if cat == "Armor":
            q.pc.sum_AC()
            self.populate_fields("Mod Armor")
        self.populate_fields("Refresh Closet")

class backend_input:
    def __init__(self, stage):
        self.Stage = stage
        self.input_map = {
            "Level Input": self.Stage.Core_Level,
            "Core Race": self.Stage.Core_Race,
            "Core Subrace": self.Stage.Core_Subrace,
            "Core Class": self.Stage.Core_Class,
            "Core Subclass": self.Stage.Core_Subclass,
            "Core Background": self.Stage.Core_Background,
            "Base Atr": self.Stage.Atr_Base_Modify,
            "Race Asi": self.Stage.Race_Asi_Modify,
            "Race Use": self.Stage.Race_Abil_Use,
            "Race Spell Use": self.Stage.Race_Spell_Use,
            "Race Spell Select": self.Stage.Race_Spell_Select,
            "Milestone Top Select": self.Stage.Milestone_Top_Select,
            "Milestone Feat Select": self.Stage.Milestone_Feat_Select,
            "Milestone Feat Modify": self.Stage.Milestone_Feat_Modify,
            "Milestone Feat Use": self.Stage.Milestone_Feat_Use,
            "Milestone Asi Select": self.Stage.Milestone_Asi_Select,
            "Class Use": self.Stage.Class_Use,
            "Class Skill Select": self.Stage.Class_Skill_Select,
            "Class Abil Select": self.Stage.Class_Abil_Select,
            "Spell Learn": self.Stage.Spell_Learn,
            "Spell Prepare": self.Stage.Spell_Prepare,
            "Spell Cast": self.Stage.Spell_Cast,
            "Background Prof Select": self.Stage.Background_Prof_Select,
            "Long Rest": self.Stage.Long_Rest,
            "Player Health Mod": self.Stage.Player_Health_Mod,
            "Player Health Set": self.Stage.Player_Health_Set,
            "Arcane Ward": self.Stage.Class_Wizard_Abjuration_Arcane_Ward,
            "Player Prof Input": self.Stage.Player_Prof_Select,
            "Condition": self.Stage.Player_Condition_Modify,
            "Characteristic": self.Stage.Info_Char_Input,
            "Description": self.Stage.Info_Desc_Input,
            "Bazaar Add Item": self.Stage.Inventory_Bazaar_Item_Add,
            "Backpack Mod Item": self.Stage.Inventory_Backpack_Item_Modify,
            "Closet Equip": self.Stage.Closet_Item_Equip,
            "Closet Clear": self.Stage.Closet_Item_Equip
        }

    def callback(self, sender, data, user_data):
        key = user_data[0]
        params = user_data[1:]
        action_method = self.input_map[key]
        print(f"{key} updating {action_method.__name__}, data={data}, user_data={params}")
        action_method(sender, data, params)

class backend_manager:
    def __init__(self):
        self.Populate = backend_populate()
        self.Stage = backend_stage(self.Populate)
        self.Input = backend_input(self.Stage)

    def get_callback_handler(self): return self.Input.callback
    
    def Start(self): self.Populate.Startup()