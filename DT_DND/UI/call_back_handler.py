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
        self.BAZAAR.Whole()
    
    def All(self):
        self.Static()
        self.Dynamic()
    
    def Dynamic(self):
        self.RACE.Whole()
        self.CLASS.Whole()
        self.BACKGROUND.Whole()
        self.MILESTONE.Whole()
        self.Inventory()

    def Race(self): 
        self.Generic()
        self.RACE.Whole()
        self.MILESTONE.Whole()

    def Class(self):
        self.Generic()
        self.CLASS.Whole()
        self.SPELL.Whole()

    def Background(self): 
        self.Generic()
        self.BACKGROUND.Whole()

    def Atr(self):
        self.Generic()
        self.ACTION.weapon()
        self.RACE.Whole()
        self.CLASS.Whole()
        self.MILESTONE.Whole()
        self.SPELL.Whole()

    def Spell(self): 
        self.SPELL.Whole()

    def Arcane_Ward(self):
        pass

    def Milestone(self): 
        self.Atr()
    
    def Generic(self):
        self.SHEET.Core()
        self.SHEET.Skills()
        self.SHEET.Health()
        self.SHEET.Initiative()
        self.SHEET.Vision()
        self.SHEET.Speed()
        self.SHEET.Prof()
        self.SHEET.Attributes()
        self.SHEET.AC()
        self.SHEET.Char()
        
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
        self.ACTION.Whole()
        
    def Backpack(self): 
        self.BACKPACK.Whole()
        
    def Inventory_Modify(self): 
        self.BACKPACK.Whole()
        self.ACTION.Whole()
        self.CLOSET.Whole()
        self.SHEET.ac()
        
    def Closet(self): 
        self.ACTION.Whole()
        self.CLOSET.Whole()
        self.Armor()

    def Armor(self): 
        self.SHEET.AC()
        
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
        check = q.dbm.Class.g.Validate()
        if check == False: 
            sett.Core_Subclass("")

    def Core_Level(self, sender, inp, user_data):
        level = q.dbm.Core.g.L
        addition = user_data[0]
        math = max(1, min(int(level + addition), 20))
        q.dbm.Core.s.L(math)
        self.populate_fields("All")

    def Core_Race(self, sender, inp, user_data):
        old_obj = q.dbm.Core.g.R
        if old_obj != inp:
            green(f"[stage_Race] - changing race to {inp}")
            q.dbm.Core.s.R(inp)
            self.populate_fields("Race")
        else: 
            red(f"[stage_Race] - race not changed")

    def Core_Subrace(self, sender, inp, user_data):
        old_obj = q.dbm.Core.g.SR
        if old_obj != inp:
            green(f"[stage_Subrace] - changing subrace to {inp}")
            q.dbm.Core.s.SR(inp)
            self.populate_fields("Race")
        else:
            red(f"[stage_Subrace] - subrace not changed")

    def Core_Class(self, sender, inp, user_data):
        old_obj = q.dbm.Core.g.C
        if old_obj != inp:
            green(f"[stage_Class] - changing class to {inp}")
            q.dbm.Core.s.C(inp)
            self.populate_fields("Class")
        else: 
            red(f"[stage_Class] - class not changed")

    def Core_Subclass(self, sender, inp, user_data):
        old_obj = q.dbm.Core.g.SC
        if old_obj != inp:
            green(f"[stage_Subclass] - changing subclass to {inp}")
            q.dbm.Core.s.SC(inp)
            self.populate_fields("Class")
        else: 
            red(f"[stage_Subclass] - subclass not changed")

    def Core_Background(self, sender, inp, user_data):
        old_obj = q.dbm.Core.g.BG
        if old_obj != inp:
            green(f"[stage_Background] - changing background to {inp}")
            q.dbm.Core.s.BG(inp)
            self.populate_fields("Background")
        else: 
            red(f"[stage_Background] - background not changed")

    def Atr_Base_Modify(self, sender, inp, user_data):
        stat = user_data[0]
        q.dbm.Atr.s.Base.Modify(stat, inp)
        self.populate_fields("Atr")

    def Race_Asi_Modify(self, sender, inp, user_data):
        print(f"Race Asi Modify: {inp}, {user_data}")
        key = user_data[0]
        if key == "Clear": q.dbm.Race.s.Asi.Clear()
        else: q.dbm.Race.s.Asi.Modify(key, inp)
        self.populate_fields("Atr")

    def Race_Abil_Use(self, sender, inp, user_data):
        key, index = user_data
        q.dbm.Race.s.Abil.Use(key, index, inp)

    def Race_Spell_Use(self, sender, inp, user_data):
        key, spell = user_data
        q.dbm.Race.s.Spell.Use(key, spell, inp)

    def Race_Spell_Select(self, sender, inp, user_data):
        key = user_data[0]
        q.dbm.Race.s.Spell.Select(key, inp)
        self.populate_fields("Race")

    def Milestone_Top_Select(self, sender, inp, user_data):
        print(sender, inp, user_data)
        index = user_data[0]
        if inp == "Clear": q.dbm.Milestone.s.Top.Clear(index)
        else: q.dbm.Milestone.s.Top.Modify(index, inp)
        self.populate_fields("All")

    def Milestone_Feat_Select(self, sender, inp, user_data):
        index = user_data[0]
        feat = inp
        if inp == "Clear": q.dbm.Milestone.s.Feat.Clear(index)
        else: q.dbm.Milestone.s.Feat.Select(index, feat)
        self.populate_fields("Milestone")
        
        
    def Milestone_Feat_Modify(self, sender, inp, user_data):
        script, feat, index = user_data
        q.dbm.Milestone.s.Feat.Modify(inp, script, feat, index)
        self.populate_fields("Milestone")



    def Milestone_Feat_Use(self, sender, inp, user_data):
        feat, index = user_data
        q.dbm.Milestone.s.Feat.Use(feat, index, inp)

    def Milestone_Asi_Select(self, sender, inp, user_data):
        key, index = user_data
        if inp == "Clear": q.dbm.Milestone.s.Asi.Clear(key, index) 
        else: q.dbm.Milestone.s.Asi.Modify(key, index, inp) 
        self.populate_fields("Atr")

    def Class_Use(self, sender, inp, user_data):
        key, index = user_data
        q.dbm.Class.s.Abil.Use(key, index, inp) 


    def Class_Skill_Select(self, sender, inp, user_data):
        script = user_data[0]
        if script == "Clear": q.dbm.Class.s.Skill_Select.Clear()
        else: q.dbm.Class.s.Skill_Select.Modify(script, inp)
        self.populate_fields("Class")


    def Class_Abil_Select(self, sender, inp, user_data):
        key, index = user_data
        q.dbm.Class.s.Abil.Select(key, index, inp)
        self.populate_fields("Class")

    def Spell_Learn(self, sender, inp, user_data):
        spell, level = user_data
        q.dbm.Spell.s.Learn(spell, level)
        self.populate_fields("Spell")

    def Spell_Prepare(self, sender, inp, user_data):
        spell, level = user_data
        q.dbm.Spell.s.Prepare(spell, level)
        self.populate_fields("Spell")

    def Spell_Cast(self, sender, inp, user_data):
        level = user_data[0]
        q.dbm.Spell.s.Cast(level)
        self.populate_fields("Spell")

    def Background_Prof_Select(self, sender, inp, user_data):
        cat, index = user_data
        if inp == "Clear": q.dbm.Background.s.Prof.Clear()
        else: q.dbm.Background.s.Prof.Select(cat, index, inp)
        self.populate_fields("Background Prof Select")

    def Long_Rest(self, sender, inp, user_data):
        q.dbm.Rest.s.Long()
        self.populate_fields("Long Rest")

    def Player_Health_Mod(self, sender, inp, user_data):
        place, delta = user_data
        if place == "Temp":q.dbm.Health.s.Temp(delta)
        else: q.dbm.Health.s.Hp(delta)
        self.populate_fields("HP")

    def Player_Health_Set(self, sender, inp, user_data):
        delta = inp
        q.dbm.Health.s.Player(delta)
        self.populate_fields("HP")

    def Class_Wizard_Abjuration_Arcane_Ward(self, sender, inp, user_data):
        num = user_data[0]
        q.dbm.Class.s.Wizard.Arcane_Ward(num)
        self.populate_fields("Arcane Ward")

    def Player_Prof_Select(self, sender, inp, user_data):
        sett.Proficiency_Player_Modify() 
        q.pc.recalculate_stats()
        self.populate_fields("Generic")

    def Player_Condition_Modify(self, sender, inp, user_data):
        index = user_data[0]
        q.dbm.Class.s.Condition.Modify(inp)
        self.populate_fields("Condition")

    def Info_Char_Input(self, sender, inp, user_data):
        name = user_data[0]
        q.dbm.Info.s.Char.Modify(name, inp)
        self.populate_fields("Characteristic")

    def Info_Desc_Input(self, sender, inp, user_data):
        name = user_data[0]
        q.dbm.Info.s.Desc.Modify(name, inp)
        sett.Info_Desc_Modify(name, inp)
        self.populate_fields("Description")

    def Inventory_Bazaar_Item_Add(self, sender, inp, user_data):
        cat, item = user_data
        q.dbm.Inventory.s.Backpack.Add(cat, item)
        sett.Inventory_Backpack_Add(cat, item)
        self.populate_fields("Bazaar Add Item")

    def Inventory_Backpack_Item_Modify(self, sender, inp, user_data):
        item, delta = user_data
        if delta == "Clear": value = q.dbm.Inventory.s.Backpack.Clear(item)
        else:  value = q.dbm.Inventory.s.Backpack.Modify(item, delta)
        print(f"Value: {value}")
        if value == 0: self.populate_fields("Backpack Delete Item")
        else:  self.populate_fields("Backpack Modify Item")

    def Closet_Item_Equip(self, sender, inp, user_data):
        cat = user_data[0]
        delta = user_data[1]
        
        if delta == "Clear": q.dbm.Closet.s.Equip.Clear(cat)
        elif delta == "Modify":
            package = inp.replace(' + ', 'PPP').replace(' ', '_')
            q.dbm.Closet.s.Equip.Modify(cat, package)
        else: red("error")

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
            "HP": self.Stage.Player_Health_Mod,
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
    
    def Start(self): 
        self.Populate.Startup()
