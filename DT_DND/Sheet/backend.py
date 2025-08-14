# backend.py
import q
from DT_DND.Sheet.get_set_import import s, g
from colorist import *


    
def stage_Level(sender, data, user_data, pop_fields):
    math = q.db.Core.L + user_data[0]
    if math not in [0,21]:
        s.Level(int(math))
        check_Class()
        q.pc.new_Level()
        pop_fields("Level")
    else:
        pass

    


def stage_Race(sender, data, user_data, pop_fields):
    old_obj = q.db.Core.R
    if old_obj != data:
        green(f"[stage_Race] - changing race to {data}")
        s.Race(data)
        s.Subrace("")
        q.pc.new_Race()
        pop_fields("Race")
    else: red(f"[stage_Race] - race not changed")

def stage_Subrace(sender, data, user_data, pop_fields):
    old_obj = q.db.Core.SR
    if old_obj != data:
        green (f"[stage_Subrace] - changing subrace to {data}")
        s.Subrace(data)
        q.pc.new_Race()
        pop_fields("Race")
    else: red(f"[stage_Subrace] - subrace not changed")

def stage_Class(sender, data, user_data, pop_fields):
    old_obj = q.db.Core.C
    if old_obj != data:
        green(f"[stage_Class] - changing class to {data}")
        s.Class(data)
        s.Subclass("")
        q.pc.new_Class()
        pop_fields("Class")
    else: red(f"[stage_Class] - class not changed")


def check_Class():
    if g.valid_class() == False: s.Subclass("")

def stage_Subclass(sender, data, user_data, pop_fields):
    old_obj = q.db.Core.SC
    if old_obj != data:
        green(f"[stage_Subclass] - changing subclass to {data}")
        s.Subclass(data)
        q.pc.new_Class()
        pop_fields("Class")
    else: red(f"[stage_Subclass] - subclass not changed")


def stage_Background(sender, data, user_data, pop_fields):
    old_obj = q.db.Core.BG
    if old_obj != data:
        green(f"[stage_Background] - changing background to {data}")
        s.Background(data)
        q.pc.new_Background()
        pop_fields("Background")
    else: red(f"[stage_Background] - background not changed")


def stage_Background_Prof_Select(sender, data, user_data, pop_fields):
    s.select_prof_background("Stage_Background_Prof_Select", data, user_data)
    q.pc.update_Background_Prof()
    pop_fields("Background Prof Select")


def stage_Atr_Base(sender, data, user_data, pop_fields):
    s.input_base_atr("Stage_Atr_Base", data, user_data)
    q.pc.update_Atr()
    pop_fields("Atr")

def stage_Race_Asi(sender, data, user_data, pop_fields):
    s.input_rasi("Stage_Rasi",data,user_data)
    q.pc.update_Atr()
    pop_fields("Atr")

def stage_Race_Use(sender, data, user_data, pop_fields):
    s.use_race("Stage_Race_Use",data,user_data)




def stage_Milestone_Level_Select(sender, data, user_data, pop_fields):
    if data == "Clear":
        s.clear_level_select_milestone("Stage_Milestone_Level_Select_Clear", data, user_data)
    else:
        s.select_level_milestone("Stage_Milestone_Level_Select", data, user_data)
    q.pc.update_Milestone_Feat()
    pop_fields("All")

def stage_Milestone_Feat_Select(sender, data, user_data, pop_fields):
    s.select_feat_milestone("Stage_Milestone_Feat_Select", data, user_data)
    q.pc.update_Milestone_Feat()
    pop_fields("Milestone")


def stage_Milestone_Feat_Choice(sender, data, user_data, pop_fields):
    s.choice_feat_milestone("Stage_Milestone_Feat_Choice", data, user_data)
    q.pc.update_Milestone_Feat()
    pop_fields("Milestone")
    
def stage_Milestone_Feat_Use(sender, data, user_data, pop_fields):
    s.use_feat_milestone("Stage_Milestone_Feat_Use", data, user_data)
    


def stage_Milestone_Asi_Select(sender, data, user_data, pop_fields):
    s.select_asi_milestone("Stage_Milestone_Asi_Select", data, user_data)
    q.pc.update_Atr()
    pop_fields("Atr")



def stage_Race_Spell_Use(sender, data, user_data, pop_fields):
    s.use_race_spell("stage_Race_Spell_Use", data, user_data)

def stage_Race_Spell_Select(sender, data, user_data, pop_fields):
    s.select_race_spell("stage_Race_Spell_Select", data, user_data)
    pop_fields("Race")

def stage_Class_Use(sender, data, user_data, pop_fields):
    s.use_class("Stage_Class_Use", data, user_data)


def stage_Class_Skill_Select(sender, data, user_data, pop_fields):
    s.select_skill_class("Stage_Class_Skill_Select", data, user_data)
    q.pc.update_Class_Select()
    pop_fields("Class")

def stage_Class_select(sender, data, user_data, pop_fields):
    s.select_class("Stage_Class_select", data, user_data)
    q.pc.update_Class_Select()
    pop_fields("Class")






def stage_Spell_Learn(sender, data, user_data, pop_fields):
    s.learn_spell("stage_Spell_Learn", data, user_data)
    q.pc.update_Spell_Learn()
    pop_fields("Spell")
    
    
def stage_Spell_Prepare(sender, data, user_data, pop_fields):
    s.prepare_spell("stage_Spell_Prepare", data, user_data)
    q.pc.update_Spell_Prepare()
    pop_fields("Spell")

def stage_Spell_Cast(sender, data, user_data, pop_fields):
    s.cast_spell("stage_Spell_Cast", data, user_data)
    q.pc.update_Spell_Cast()
    pop_fields("Spell")


def stage_Long_Rest(sender, data, user_data, pop_fields):
    s.long_rest("stage_Long_Rest", data, user_data)
    pop_fields("Long Rest")

def stage_Health_Mod(sender, data, user_data, pop_fields):
    s.mod_health("stage_Health_Mod", data, user_data)
    pop_fields("HP")

def stage_Player_HP_Mod(sender, data, user_data, pop_fields):
    s.mod_hp_player("stage_Player_HP_Mod", data, user_data)
    q.pc.recalculate_stats()
    pop_fields("HP")

def stage_Arcane_Ward(sender, data, user_data, pop_fields):
    s.mod_arcane_ward("stage_Arcane_Ward", data, user_data)
    pop_fields("Arcane Ward")
    
    
    
def stage_Player_Prof_Select(sender, data, user_data, pop_fields):
    s.select_prof_player("stage_Player_Prof_Select", data, user_data)
    q.pc.recalculate_stats()
    pop_fields("Generic")

def stage_Player_Condition(sender, data, user_data, pop_fields):
    s.select_player_condition("stage_Player_Condition", data, user_data)
    pop_fields("Condition")

def stage_Characteristic_Input(sender, data, user_data, pop_fields):
    s.input_characteristic("stage_Characteristic_Input", data, user_data)
    pop_fields("Characteristic")

def stage_Description_Input(sender, data, user_data, pop_fields):
    s.input_description("stage_Description_Input", data, user_data)
    pop_fields("Description")



def stage_Bazaar_Add_Item(sender, data, user_data, pop_fields):
    s.add_item_bazaar("stage_Bazaar_Add_Item", data, user_data)

    pop_fields("Bazaar Add Item")

def stage_Backpack_Mod_Item(sender, data, user_data, pop_fields):
    value = s.mod_item_backpack(sender, data, user_data)
    if value == 0: pop_fields("Reset Backpack")
    else: pop_fields("Mod Backpack")


def stage_Equip_Equip(sender, data, user_data, pop_fields):
    cat = user_data[0]
    if len(user_data) > 1:
        if user_data[1] == "Clear":
            package = "Clear"
    else:
        package =  data.replace(' + ', 'PPP').replace(' ', '_')
    
    s.Equip_Equip("stage_Equip_Equip", package, user_data)
    
    if cat == "Weapon": pass
    if cat == "Armor": 
        q.pc.sum_AC()
        pop_fields("Mod Armor")

    
    pop_fields("Mod Equip")
