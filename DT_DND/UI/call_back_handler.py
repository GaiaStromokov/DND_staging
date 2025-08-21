from ui.upd_helper_import import *
from ui.upd_class_import import *





    
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
        # def populate_Arcane_Ward():
        #     HP = q.db.Clasq.pc.Abil["Arcane Ward"]["HP"]
        #     configure_item("Arcane_Ward_HP", label=f"{HP["Current"]} / {HP["Max"]}")

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
        self.Bazaar()
        self.Backpack()
        self.Closet()
        
    def Bazaar(self): 
        self.BAZAAR.whole()

    def Backpack(self): 
        self.BACKPACK.whole()
        
    def Backpack_mod(self): 
        self.BACKPACK.populate_backpack()

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
            "All":                      self.Populate.All,
            "Level":                    self.Populate.All,
            "Long Rest":                self.Populate.All,
            "Race":                     self.Populate.Race,
            "Class":                    self.Populate.Class,
            "Background":               self.Populate.Background,
            "Atr":                      self.Populate.Atr,
            "Spell":                    self.Populate.Spell,
            "Arcane Ward":              self.Populate.Arcane_Ward,
            "Milestone":                self.Populate.Milestone,
            "Background Prof Select":   self.Populate.Background,
            "Generic":                  self.Populate.Generic,
            "HP":                       self.Populate.HP,
            "Condition":                self.Populate.Condition,
            "Characteristic":           self.Populate.characteristics,
            "Description":              self.Populate.characteristics,
            "Bazaar Add Item":          self.Populate.Inventory,
            "Reset Backpack":           self.Populate.Inventory,
            "Mod Backpack":             self.Populate.Backpack_mod,
            "Refresh Closet":           self.Populate.Closet,
            "Mod Armor":                self.Populate.Armor
        }

    
    def populate_fields(self, source):
        self.stage_map[source]()

    def check_Class(self):
        if get.valid_class() == False: sett.Subclass("")

    def Level(self, sender, data, user_data):
        math = q.db.Core.L + user_data[0]
        if math not in [0, 21]:
            sett.Level(int(math))
            self.check_Class()
            q.pc.new_Level()
            self.populate_fields("Level")

    def Race(self, sender, data, user_data):
        old_obj = q.db.Core.R
        if old_obj != data:
            green(f"[stage_Race] - changing race to {data}")
            sett.Race(data)
            sett.Subrace("")
            q.pc.new_Race()
            self.populate_fields("Race")
        else:
            red(f"[stage_Race] - race not changed")

    def Subrace(self, sender, data, user_data):
        old_obj = q.db.Core.SR
        if old_obj != data:
            green(f"[stage_Subrace] - changing subrace to {data}")
            sett.Subrace(data)
            q.pc.new_Race()
            self.populate_fields("Race")
        else:
            red(f"[stage_Subrace] - subrace not changed")

    def Class(self, sender, data, user_data):
        old_obj = q.db.Core.C
        if old_obj != data:
            green(f"[stage_Class] - changing class to {data}")
            sett.Class(data)
            sett.Subclass("")
            q.pc.new_Class()
            self.populate_fields("Class")
        else:
            red(f"[stage_Class] - class not changed")

    def Subclass(self, sender, data, user_data):
        old_obj = q.db.Core.SC
        if old_obj != data:
            green(f"[stage_Subclass] - changing subclass to {data}")
            sett.Subclass(data)
            q.pc.new_Class()
            self.populate_fields("Class")
        else:
            red(f"[stage_Subclass] - subclass not changed")

    def Background(self, sender, data, user_data):
        old_obj = q.db.Core.BG
        if old_obj != data:
            green(f"[stage_Background] - changing background to {data}")
            sett.Background(data)
            q.pc.new_Background()
            self.populate_fields("Background")
        else:
            red(f"[stage_Background] - background not changed")

    def Atr_Base(self, sender, data, user_data):
        sett.input_base_atr("Stage_Atr_Base", data, user_data)
        q.pc.update_Atr()
        self.populate_fields("Atr")

    def Race_Asi(self, sender, data, user_data):
        sett.input_rasi("Stage_Rasi", data, user_data)
        q.pc.update_Atr()
        self.populate_fields("Atr")

    def Race_Use(self, sender, data, user_data):
        sett.use_race("Stage_Race_Use", data, user_data)

    def Race_Spell_Use(self, sender, data, user_data):
        sett.use_race_spell("stage_Race_Spell_Use", data, user_data)

    def Race_Spell_Select(self, sender, data, user_data):
        sett.select_race_spell("stage_Race_Spell_Select", data, user_data)
        self.populate_fields("Race")

    def Milestone_Level_Select(self, sender, data, user_data):
        if data == "Clear":
            sett.clear_level_select_milestone("Stage_Milestone_Level_Select_Clear", data, user_data)
        else:
            sett.select_level_milestone("Stage_Milestone_Level_Select", data, user_data)
        q.pc.update_Milestone_Feat()
        self.populate_fields("All")

    def Milestone_Feat_Select(self, sender, data, user_data):
        sett.select_feat_milestone("Stage_Milestone_Feat_Select", data, user_data)
        q.pc.update_Milestone_Feat()
        self.populate_fields("Milestone")

    def Milestone_Feat_Choice(self, sender, data, user_data):
        sett.choice_feat_milestone("Stage_Milestone_Feat_Choice", data, user_data)
        q.pc.update_Milestone_Feat()
        self.populate_fields("Milestone")

    def Milestone_Feat_Use(self, sender, data, user_data):
        sett.use_feat_milestone("Stage_Milestone_Feat_Use", data, user_data)

    def Milestone_Asi_Select(self, sender, data, user_data):
        sett.select_asi_milestone("Stage_Milestone_Asi_Select", data, user_data)
        q.pc.update_Atr()
        self.populate_fields("Atr")

    def Class_Use(self, sender, data, user_data):
        sett.use_class("Stage_Class_Use", data, user_data)

    def Class_Skill_Select(self, sender, data, user_data):
        sett.select_skill_class("Stage_Class_Skill_Select", data, user_data)
        q.pc.update_Class_Select()
        self.populate_fields("Class")

    def Class_select(self, sender, data, user_data):
        sett.select_class("Stage_Class_select", data, user_data)
        q.pc.update_Class_Select()
        self.populate_fields("Class")

    def Spell_Learn(self, sender, data, user_data):
        sett.learn_spell("stage_Spell_Learn", data, user_data)
        q.pc.update_Spell_Learn()
        self.populate_fields("Spell")

    def Spell_Prepare(self, sender, data, user_data):
        sett.prepare_spell("stage_Spell_Prepare", data, user_data)
        q.pc.update_Spell_Prepare()
        self.populate_fields("Spell")

    def Spell_Cast(self, sender, data, user_data):
        sett.cast_spell("stage_Spell_Cast", data, user_data)
        q.pc.update_Spell_Cast()
        self.populate_fields("Spell")

    def Background_Prof_Select(self, sender, data, user_data):
        sett.select_prof_background("Stage_Background_Prof_Select", data, user_data)
        q.pc.update_Background_Prof()
        self.populate_fields("Background Prof Select")

    def Long_Rest(self, sender, data, user_data):
        sett.long_rest("stage_Long_Rest", data, user_data)
        self.populate_fields("Long Rest")

    def Health_Mod(self, sender, data, user_data):
        sett.mod_health("stage_Health_Mod", data, user_data)
        self.populate_fields("HP")

    def Player_HP_Mod(self, sender, data, user_data):
        sett.mod_hp_player("stage_Player_HP_Mod", data, user_data)
        q.pc.recalculate_stats()
        self.populate_fields("HP")

    def Arcane_Ward(self, sender, data, user_data):
        sett.mod_arcane_ward("stage_Arcane_Ward", data, user_data)
        self.populate_fields("Arcane Ward")

    def Player_Prof_Select(self, sender, data, user_data):
        sett.select_prof_player("stage_Player_Prof_Select", data, user_data)
        q.pc.recalculate_stats()
        self.populate_fields("Generic")

    def Player_Condition(self, sender, data, user_data):
        sett.select_player_condition("stage_Player_Condition", data, user_data)
        self.populate_fields("Condition")

    def Characteristic_Input(self, sender, data, user_data):
        sett.input_characteristic("stage_Characteristic_Input", data, user_data)
        self.populate_fields("Characteristic")

    def Description_Input(self, sender, data, user_data):
        sett.input_description("stage_Description_Input", data, user_data)
        self.populate_fields("Description")

    def Bazaar_Add_Item(self, sender, data, user_data):
        sett.add_item_bazaar("stage_Bazaar_Add_Item", data, user_data)
        self.populate_fields("Bazaar Add Item")

    def Backpack_Mod_Item(self, sender, data, user_data):
        value = sett.mod_item_backpack(sender, data, user_data)
        if value == 0:
            self.populate_fields("Reset Backpack")
        else:
            self.populate_fields("Mod Backpack")

    def Closet_Equip(self, sender, data, user_data):
        
        cat = user_data[0]
        if len(user_data) > 1 and user_data[1] == "Clear":
            package = "Clear"
        else:
            package = data.replace(' + ', 'PPP').replace(' ', '_')

        # Delegate equip logic to system
        sett.closet_equip("stage_Closet_Equip", package, user_data)


        q.pc.sum_AC()
        self.populate_fields("Mod Armor")

        self.populate_fields("Refresh Closet")


class backend_input:
    def __init__(self, stage):
        self.Stage = stage
        self.input_map = {
            "Level Input":              self.Stage.Level,
            "Core Race":                self.Stage.Race,
            "Core Subrace":             self.Stage.Subrace,
            "Core Class":               self.Stage.Class,
            "Core Subclass":            self.Stage.Subclass,
            "Core Background":          self.Stage.Background,
            "Base Atr":                 self.Stage.Atr_Base,
            "Race Asi":                 self.Stage.Race_Asi,
            "Race Use":                 self.Stage.Race_Use,
            "Race Spell Use":           self.Stage.Race_Spell_Use,
            "Race Spell Select":        self.Stage.Race_Spell_Select,
            "Milestone Level Select":   self.Stage.Milestone_Level_Select,
            "Milestone Feat Select":    self.Stage.Milestone_Feat_Select,
            "Milestone Feat Choice":    self.Stage.Milestone_Feat_Choice,
            "Milestone Feat Use":       self.Stage.Milestone_Feat_Use,
            "Milestone Asi Select":     self.Stage.Milestone_Asi_Select,
            "Class Use":                self.Stage.Class_Use,
            "Class Skill Select":       self.Stage.Class_Skill_Select,
            "Class Select":             self.Stage.Class_select,
            "Spell Learn":              self.Stage.Spell_Learn,
            "Spell Prepare":            self.Stage.Spell_Prepare,
            "Spell Cast":               self.Stage.Spell_Cast,
            "Background Prof Select":   self.Stage.Background_Prof_Select,
            "Long Rest":                self.Stage.Long_Rest,
            "HP":                       self.Stage.Health_Mod,
            "Player HP Mod":            self.Stage.Player_HP_Mod,
            "Arcane Ward":              self.Stage.Arcane_Ward,
            "Player Prof Input":        self.Stage.Player_Prof_Select,
            "Condition":                self.Stage.Player_Condition,
            "Characteristic":           self.Stage.Characteristic_Input,
            "Description":              self.Stage.Description_Input,
            "Bazaar Add Item":          self.Stage.Bazaar_Add_Item,
            "Backpack Mod Item":        self.Stage.Backpack_Mod_Item,
            "Closet Equip":             self.Stage.Closet_Equip,
            "Closet Clear":             self.Stage.Closet_Equip
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

    def get_callback_handler(self):
        return self.Input.callback
    
    def Start(self):
        self.Populate.All()