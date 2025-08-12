#ui_upd.py
from dearpygui.dearpygui import *
import q
from Sheet.getset import g

from access_data.color_reference import *
import math as math
from Sheet.sizing import *
from colorist import *

#ANCHOR - size
class size:
    w_max = 1350
    h_max = 880

    w_block = w_max - 595
    h_block = h_max - 114

    h_header_1 = 20
    w_header_2 = 188
    w_header_3 = 116

    gwrap = 640

    w_s_btn = 20
    w_m_btn = 46
    w_l_btn = 90

    w_armor_class = 62
    h_armor_class = 58

    w_attributes = 132
    h_attributes = 174

    w_buffer_1 = 132
    h_buffer_1 = 17

    w_buffer_2 = 210
    h_buffer_2 = 13

    w_character = 210
    h_character = 82

    w_conditions = 132
    h_conditions = 42

    w_core = 210
    h_core = 174

    w_health = 210
    h_health = 82

    w_initiative = 62
    h_initiative = 58

    w_inventory = 552
    h_inventory = 340

    w_item = 117

    w_proficiencies = 210
    h_proficiencies = 82

    w_rest = 132
    h_rest = 80

    w_skill = 194
    h_skill = 449

    w_speed = 62
    h_speed = 58

    w_vision = 62
    h_vision = 58

    w_wallet = 412
    h_wallet = 35

#ANCHOR -  tag
class tag:
    class Base:
        prefix = None

        @classmethod
        def build(cls, items=None, suffix=None):
            if cls.prefix is None: raise NotImplementedError("Subclasses must define prefix")
            if suffix is None: raise ValueError("Suffix must be provided")
            items_str = "_".join(items) if isinstance(items, (list, tuple)) else str(items) if items else ""
            return f"{cls.prefix}_{items_str}_{suffix}" if items_str else f"{cls.prefix}_{suffix}"

        
        @classmethod
        def select(cls, *items): return cls.build(items if items else None, "select")
        @classmethod
        def val(cls, *items): return cls.build(items if items else None, "val")
        @classmethod
        def label(cls, *items): return cls.build(items if items else None, "label")
        @classmethod
        def button(cls, *items): return cls.build(items if items else None, "button")
        @classmethod
        def source(cls, *items): return cls.build(items if items else None, "source")
        @classmethod
        def toggle(cls, *items): return cls.build(items if items else None, "toggle")
        @classmethod
        def max(cls, *items): return cls.build(items if items else None, "max")
        @classmethod
        def input(cls, *items): return cls.build(items if items else None, "input")
        @classmethod
        def text(cls, *items): return cls.build(items if items else None, "text")
        @classmethod
        def mod(cls, *items): return cls.build(items if items else None, "mod")
        @classmethod
        def sum(cls, *items): return cls.build(items if items else None, "sum")
        @classmethod
        def sub(cls, *items): return cls.build(items if items else None, "sub")
        @classmethod
        def main(cls, *items): return cls.build(items if items else None, "main")
        @classmethod
        def window(cls, *items): return cls.build(items if items else None, "window")
        @classmethod
        def tabbar(cls, *items): return cls.build(items if items else None, "tabbar")
        @classmethod
        def tab(cls, *items): return cls.build(items if items else None, "tab")
        @classmethod
        def known(cls, *items): return cls.build(items if items else None, "known")
        @classmethod
        def available(cls, *items): return cls.build(items if items else None, "available")
        @classmethod
        def current(cls, *items): return cls.build(items if items else None, "current")
        @classmethod
        def tooltip(cls, *items): return cls.build(items if items else None, "tooltip")
        @classmethod
        def popup(cls, *items): return cls.build(items if items else None, "popup")
        @classmethod
        def header(cls, *items): return cls.build(items if items else None, "header")

        @classmethod
        def wlevel(cls, level): 
            if cls.prefix is None: raise NotImplementedError("Subclasses must define prefix")
            return f"{cls.prefix}_Level_{level}_window"


        @classmethod
        def cell(cls, item1, item2):
            if cls.prefix is None:
                raise NotImplementedError("Subclasses must define prefix")
            return f"{cls.prefix}_{item1}_{item2}_cell"

        @classmethod
        def element(cls, *, item=None, suffix=None):
            if cls.prefix is None:
                raise NotImplementedError("Subclasses must define prefix")
            if suffix is None:
                raise ValueError("Suffix must be provided")
            return f"{cls.prefix}_{item}_{suffix}" if item else f"{cls.prefix}_{suffix}"

        @classmethod
        def multi(cls, *parents, suffix):
            if cls.prefix is None:
                raise NotImplementedError("Subclasses must define prefix")
            return f"{cls.prefix}_{'_'.join(parents)}_{suffix}"

        @classmethod
        def gen(cls, parents, items, suffix):
            parts = []
            if parents: parts.extend(parents)
            if items: parts.extend(items)
            return "_".join(parts) + f"_{suffix}"

        @classmethod
        def bazaar(cls, equip_type, rank):
            return f"bazaar_{equip_type}_{rank}"



        @classmethod
        def equip(cls, item):
            item = item.lower()
            return f"{item}_equip"

    @staticmethod
    def icon(item):
        item = item.lower()
        return f"{item}_icon"

    @staticmethod
    def img(item):
        item = item.lower()
        return f"{item}_img"
    class core(Base):      prefix = "core"
    class health(Base):    prefix = "health"
    class prof(Base):      prefix = "proficiencies"
    class char(Base):      prefix = "character"
    class pdesc(Base):     prefix = "pdescription"
    class buffer1(Base):   prefix = "buffer1"
    class buffer2(Base):   prefix = "buffer2"
    class atr(Base):       prefix = "attributes"
    class init(Base):      prefix = "initiative"
    class ac(Base):        prefix = "armor_class"
    class vision(Base):    prefix = "vision"
    class speed(Base):     prefix = "speed"
    class cond(Base):      prefix = "condition"
    class rest(Base):      prefix = "rest"
    class skill(Base):     prefix = "skills"
    class inve(Base):      prefix = "inventory"
    class block(Base):     prefix = "block"
    class wallet(Base):    prefix = "wallet"
    class rfeature(Base):  prefix = "block_feature_race"
    class cfeature(Base):  prefix = "block_feature_class"
    class mfeature(Base):  prefix = "block_feature_milestone"
    class bfeature(Base):  prefix = "block_feature_background"
    class wactions(Base):  prefix = "block_actions_weapon"
    class spell(Base):     prefix = "block_spells"
    class scast(Base):     prefix = "block_spells_cast"
    class slearn(Base):    prefix = "block_spells_learn"
    class sprepare(Base):  prefix = "block_spells_prepare"


#ANCHOR - Backend Import
from Sheet.backend import (
    stage_Level, 
    
    stage_Race, stage_Subrace, 
    stage_Race_Asi, stage_Race_Use,
    stage_Race_Spell_Use, stage_Race_Spell_Select,
    
    stage_Class, stage_Subclass,
    stage_Class_Use, stage_Class_Skill_Select,
    stage_Class_select,
    
    stage_Background, 
    stage_Background_Prof_Select,
    
    stage_Milestone_Level_Select, 
    stage_Milestone_Feat_Select, stage_Milestone_Feat_Choice, stage_Milestone_Feat_Use,
    stage_Milestone_Asi_Select,
    
    stage_Atr_Base,

    stage_Spell_Learn,
    stage_Spell_Prepare, stage_Spell_Cast, 
    
    stage_Long_Rest, stage_Health_Mod, stage_Player_HP_Mod,
    
    stage_Arcane_Ward,
    
    stage_Player_Prof_Select, stage_Player_Condition,
    
    stage_Characteristic_Input, stage_Description_Input,
    
    
    stage_Bazaar_Add_Item, stage_Backpack_Mod_Item,
    
    stage_Equip_Equip
)


        
#ANCHOR - Call Back Handler
def cbh(sender, data, user_data):
    func_dict = {
        "Level Input":                  stage_Level,
        "Core Race":                    stage_Race,
        "Core Subrace":                 stage_Subrace,
        "Core Class":                   stage_Class,
        "Core Subclass":                stage_Subclass,
        "Core Background":              stage_Background,

        "Base Atr":                     stage_Atr_Base,

        "Race Asi":                     stage_Race_Asi,
        "Race Use":                     stage_Race_Use,
        "Race Spell Use":               stage_Race_Spell_Use,
        "Race Spell Select":            stage_Race_Spell_Select,

        
        "Milestone Level Select":       stage_Milestone_Level_Select,
        "Milestone Feat Select":        stage_Milestone_Feat_Select,
        "Milestone Feat Choice":        stage_Milestone_Feat_Choice,
        "Milestone Feat Use":           stage_Milestone_Feat_Use,
        "Milestone Asi Select":         stage_Milestone_Asi_Select,


        "Class Use":                    stage_Class_Use,
        "Class Skill Select":           stage_Class_Skill_Select,
        "Class Select":                 stage_Class_select,
        
        "Spell Learn":                  stage_Spell_Learn,
        "Spell Prepare":                stage_Spell_Prepare,
        "Spell Cast":                   stage_Spell_Cast,
        
        "Background Prof Select":       stage_Background_Prof_Select,
        
        "Long Rest":                    stage_Long_Rest,

        
        "HP":                           stage_Health_Mod,
        "Player HP Mod":                stage_Player_HP_Mod,
        
        "Arcane Ward":                  stage_Arcane_Ward,
        
        "Player Prof Input":            stage_Player_Prof_Select,
        
        "Condition":                    stage_Player_Condition,
        
        "Characteristic":               stage_Characteristic_Input,
        "Description":                  stage_Description_Input,
        
        "Bazaar Add Item":              stage_Bazaar_Add_Item,
        "Backpack Mod Item":            stage_Backpack_Mod_Item,
        
        "Equip Equip":                  stage_Equip_Equip,
        "Clear Equip":                  stage_Equip_Equip
    }
    key = user_data[0]
    user_data=user_data[1:]
    print(f"{key} updating {func_dict[key].__name__}, data={data}, user_data={user_data}")
    func_dict[key](sender, data, user_data, populate_Fields)
    
    

def item_delete(tag):
    if does_item_exist(tag): delete_item(item=tag, children_only=False)

def item_clear(tag):
    if does_item_exist(tag): delete_item(item=tag, children_only=True)




def create_attribute_row(stat: str):
    label_width=40
    value_width=30

    tSum = tag.atr.sum(stat)
    tMod = tag.atr.mod(stat)
    tCombo = tag.atr.select(stat)

    with group(horizontal=True):
        add_button(label=stat, enabled=False, width=label_width)
        add_button(label="", enabled=False, width=value_width, tag=tSum)
        add_button(label="", enabled=False, width=value_width, tag=tMod)

    with popup(tSum, mousebutton=mvMouseButton_Left):
        with group(horizontal=True):
            add_button(label="Base", enabled=False, width=label_width)
            add_combo(items=g.list_Base_Atr, default_value="", width=value_width, no_arrow_button=True, user_data=["Base Atr", stat], callback=cbh, tag=tCombo)

    with tooltip(tSum):
        for source in ["Base", "Race", "Feat"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=label_width)
                tSource = tag.atr.source(stat, source.lower())
                add_button(label="", enabled=False, width=25, tag=tSource)



def create_skill_row(skill: str):
    label_width = 113
    mod_width = 30

    tLabel = tag.skill.label(skill)
    tBool = tag.skill.toggle(skill)
    tMod = tag.skill.mod(skill)
    
    
    with group(horizontal=True): 
        add_button(label=skill, enabled=False, width=label_width, tag=tLabel)
        add_checkbox(default_value=False, enabled=False, user_data=[], callback=cbh, tag=tBool)
        add_button(label="", enabled=False, width=mod_width, tag=tMod)
    with tooltip(tLabel):
        add_text(g.dict_Skill[skill]["Desc"])
        
    with tooltip(tBool):
        for source in ["Player", "Race", "Class", "BG", "Feat"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=50)
                
                tSource = tag.skill.source(source)
                add_checkbox(default_value=False, enabled=False, user_data=[], callback=cbh, tag=tSource)


def create_pdescription():
    tLabel = tag.pdesc.label()
    with popup(tLabel, mousebutton=mvMouseButton_Left):
        for item in g.list_Description: 
            tInput = tag.pdesc.input(item)
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=size.w_l_btn)
                add_input_text(default_value="", on_enter=True, width = 70, user_data=["Description", item], callback=cbh, tag=tInput)
    with tooltip(tLabel):
        for item in g.list_Description: 
            tText = tag.pdesc.text(item)
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=size.w_l_btn)
                add_text("", color=c_h2, wrap=400, tag=tText)




def create_ideals(name: str):
    name = name.lower()
    
    tLabel = tag.char.label(name)
    tInput = tag.char.input(name)
    tText = tag.char.text(name)
    print(tLabel, tInput, tText)
    with popup(tLabel, mousebutton=mvMouseButton_Left): add_input_text(default_value="", on_enter=True, user_data=["Characteristic", name], callback=cbh, tag=tInput)
    with tooltip(tLabel): add_text("", tag=tText, wrap=400)


def create_proficiency_addons(tLabel: str, proficiency_map: dict):
    with popup(tLabel, mousebutton=mvMouseButton_Left):
        with group(horizontal=True):
            for category, items in proficiency_map.items():
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    add_text(category)
                    add_separator()
                    for item in items:
                        tSelectable = tag.prof.multi(category, item, suffix="toggle")
                        add_selectable(label=g.pName(item), default_value=False, user_data=["Player Prof Input", category, item], callback=cbh, tag=tSelectable)

    with tooltip(tLabel):
        with group(horizontal=True):
            for category, items in proficiency_map.items():
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    add_text(category)
                    add_separator()
                    for item in items:
                        tText = tag.prof.multi(category, item, suffix="text")
                        add_text(g.pName(item), color=(0, 0, 0), tag=tText)


def init_window_Skeleton():
    with window(no_title_bar=True, no_close=True, autosize=True, tag="window_main"):
        with group(horizontal=True):
            with group(horizontal=False):
                with group(horizontal=True):
                    with group(horizontal=False):
                        add_child_window(tag=tag.core.window(), width=size.w_core, height=size.h_core, border=True, no_scrollbar=True)
                        add_child_window(tag=tag.health.window(), width=size.w_health, height=size.h_health, border=True)
                        add_child_window(tag=tag.prof.window(), width=size.w_proficiencies, height=size.h_proficiencies, border=True)
                        add_child_window(tag=tag.char.window(), width=size.w_character, height=size.h_character, border=True)
                        add_child_window(tag=tag.buffer1.window(), width=size.w_buffer_2, height=size.h_buffer_2, border=True, no_scrollbar=True)
                    with group(horizontal=False):
                        add_child_window(tag=tag.atr.window(), width=size.w_attributes, height=size.h_attributes, border=True)
                        with group(horizontal=True):
                            add_child_window(tag=tag.init.window(), width=size.w_initiative, height=size.h_initiative, border=True)
                            add_child_window(tag=tag.ac.window(), width=size.w_armor_class, height=size.h_armor_class, border=True)
                        with group(horizontal=True):
                            add_child_window(tag=tag.vision.window(), width=size.w_vision, height=size.h_vision, border=True)
                            add_child_window(tag=tag.speed.window(), width=size.w_speed, height=size.h_speed, border=True)
                        add_child_window(tag=tag.cond.window(), width=size.w_conditions, height=size.h_conditions, border=True)
                        add_child_window(tag=tag.rest.window(), width=size.w_rest, height=size.h_rest, border=True)
                        add_child_window(tag=tag.buffer2.window(), width=size.w_buffer_1, height=size.h_buffer_1, border=True, no_scrollbar=True)
                    with group(horizontal=False):
                        add_child_window(tag=tag.skill.window(), width=size.w_skill, height=size.h_skill, border=True, no_scrollbar=True)
                with group(horizontal=False):
                    add_child_window(tag=tag.inve.window(), width=size.w_inventory, height=size.h_inventory + 12, border=True, no_scrollbar=True)
            with group(horizontal=False):
                add_child_window(tag=tag.block.window(), width=size.w_block, height=size.h_block, border=True, no_scrollbar=True)
                add_child_window(tag=tag.wallet.window(), width=size.w_wallet, height=size.h_wallet, border=True, no_scrollbar=True)

def init_window_wallet():
    with group(parent=tag.wallet.window()):
        with group(horizontal=True):
            for i in g.list_Coins:
                with group(horizontal=True):
                    add_button(label=i)
                    add_text("0", color=c_h9, tag=tag.wallet.val(i))


def init_window_core():
    w_max=size.w_core-16
    h_max=size.h_core-16
    with group(parent=tag.core.window()):
        add_button(label="Character info", enabled=False, width=w_max, height = size.h_header_1)
        with group(horizontal=True):
            add_button(label="Level", enabled=False, width=50)
            add_button(label="<", user_data=["Level Input", -1], callback=cbh)
            add_button(label="", width=25, tag=tag.core.val("level"))
            add_button(label=">", user_data=["Level Input", 1], callback=cbh)
            add_button(label="", enabled=False, width=55, tag=tag.core.val("pb"))
            with group(horizontal=True):
                add_button(label="Race", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Race"], callback = cbh, tag=tag.core.select("race"))
            with group(horizontal=True):
                add_button(label="Subrace", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Subrace"], callback = cbh, tag=tag.core.select("subrace"))
            with group(horizontal=True):
                add_button(label="Class", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Class"], callback = cbh, tag=tag.core.select("class"))        
            with group(horizontal=True):
                add_button(label="Subclass", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Subclass"], callback = cbh, tag=tag.core.select("subclass"))        
            with group(horizontal=True):
                add_button(label="Background", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Background"], callback = cbh, tag=tag.core.select("background"))


                
def init_window_attributes():
    with group(parent=tag.atr.window()):
        w_max=size.w_attributes-16
        add_button(label="Attributes", enabled=False, width=w_max, height=size.h_header_1)
        for stat in g.list_Atr:
            create_attribute_row(stat)



def init_window_health():
    with group(parent=tag.health.window()):
        w_max=size.w_health-16
        h_max=size.h_health-15
        add_button(label="Health", enabled=False, width=w_max, height=size.h_header_1)
        with group(horizontal=False):
            with group(horizontal=True):
                add_button(label="+", width=size.w_s_btn, user_data=["HP","HP", 1], callback=cbh)
                add_button(label="CUR / MAX", enabled=False, width=w_max-108, tag="health_label")
                add_button(label="TEMP", enabled=False, width=w_max-150)
                add_button(label="+", width=size.w_s_btn, user_data=["HP","Temp", 1], callback=cbh)
            with group(horizontal=True):
                add_button(label="-", width=size.w_s_btn, user_data=["HP","HP", -1], callback=cbh)
                add_button(label="", enabled=False, width=w_max-108, tag=tag.health.val("hp"))
                add_button(label="", enabled=False, width=w_max-150, tag=tag.health.val("temp"))
                add_button(label="-", width=size.w_s_btn, user_data=["HP","Temp", -1], callback=cbh)
    
    with popup("health_label", mousebutton=mvMouseButton_Left):
        add_button(label="Max", width=size.w_l_btn)
        add_input_int(default_value=0, width=90, user_data=["Player HP Mod"], callback=cbh, tag=tag.health.max("hp"))
        

def init_window_skills():
    w_max=size.w_skill-16
    h_max=size.w_skill-15
    with group(parent=tag.skill.window()):
        add_button(label="Skills", enabled=False, width=w_max, height=size.h_header_1)
        for skill in g.list_Skill:
            create_skill_row(skill)


def init_window_initiatives():
    with group(parent=tag.init.window()):
        add_button(label="Init", enabled=False, width=size.w_m_btn, tag=tag.init.label())
        add_button(label="", enabled=False, width=size.w_m_btn, tag=tag.init.val())
    with tooltip(tag.init.label()):
        for source in ["Dex", "Race", "Class"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=40)
                add_button(label="", enabled=False, width=25, tag=tag.init.source(source))

def init_window_armor():
    with group(parent=tag.ac.window()):
        add_button(label="AC", enabled=False, width=size.w_m_btn, tag=tag.ac.label())
        add_button(label="", enabled=False, width=size.w_m_btn, tag=tag.ac.val())

        with tooltip(tag.ac.label()):
            with group(horizontal=True):
                add_button(label="Base", enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=tag.ac.source("base"))
            with group(horizontal=True):
                add_button(label="Dex", enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=tag.ac.source("dex"))



def init_window_vision():
    with group(parent=tag.vision.window()):
        add_button(label="Vision", enabled=False, width=size.w_m_btn, tag = tag.vision.label())
        add_button(label="", enabled=False, width=size.w_m_btn, tag=tag.vision.val())
    with tooltip(tag.vision.label()):
        for i in g.list_Vision:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=tag.vision.source(i))

def init_window_speed():
    with group(parent=tag.speed.window()):
        add_button(label="Speed", enabled=False, width=size.w_m_btn, tag = tag.speed.label())
        add_button(label="", enabled=False, width=size.w_m_btn, tag=tag.speed.val())
    with tooltip(tag.speed.label()):
        for i in g.list_Speed:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=tag.speed.source(i))



def init_window_conditions():
    with group(parent=tag.cond.window()):
        add_button(label="Conditions", enabled=False, width=size.w_header_2, height=26, tag=tag.cond.label())
    with popup(tag.cond.label(), mousebutton=mvMouseButton_Left):
        with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
            for i in g.list_Condition:
                add_selectable(label=i, default_value=False, user_data=["Condition", i], callback=cbh, tag=tag.cond.toggle(i))
    with tooltip(tag.cond.label()):
        with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
            for i in g.list_Condition:
                add_text(i, color=(0, 0, 0), tag=tag.cond.text(i))


def init_window_rest():
    with group(parent=tag.rest.window()):
        add_button(label="Short Rest", width=size.w_header_2, height=30, user_data=["Short Rest"], callback=cbh, tag=tag.rest.button("short"))
        add_button(label="Long Rest", width=size.w_header_2, height=30, user_data=["Long Rest"], callback=cbh, tag=tag.rest.button("long"))


def init_window_buffer():
    pass


def init_window_proficienices():
    w_max=size.w_proficiencies-16
    h_max=size.w_proficiencies-15
    btn_w = w_max-101
    with group(parent=tag.prof.window()):
        add_button(label="Proficiencies", enabled=False, width=w_max, height=size.h_header_1)
        with group(horizontal=True):
            add_button(label="Weapons", width=btn_w, tag=tag.prof.label("weapon"))
            add_button(label="Armor", width=btn_w, tag=tag.prof.label("armor"))
        with group(horizontal=True):
            add_button(label="Tools", width=btn_w, tag=tag.prof.label("tool"))
            add_button(label="Languages", width=btn_w, tag=tag.prof.label("lang"))

    # Create popups using the helper
    create_proficiency_addons(tag.prof.label("weapon"), {k: set(q.w.prof("Weapon")) & set(q.w.cat(k)) for k in ["Simple", "Martial"]})
    create_proficiency_addons(tag.prof.label("armor"), {"Armor": q.w.prof("Armor")})
    create_proficiency_addons(tag.prof.label("tool"), {"Artisan": g.list_Job, "Gaming": g.list_Game, "Musical": g.list_Music})
    create_proficiency_addons(tag.prof.label("lang"), {"Languages": g.list_Lang})

def init_window_characteristics():
    w_max=size.w_character-16
    h_max=size.h_character-15
    btn_w = w_max-101
    with group(parent=tag.char.window()):
        add_button(label="Characteristics", enabled=False, width=w_max, height=size.h_header_1, tag=tag.pdesc.label())
        with group(horizontal=True):
            add_button(label="Traits", width=btn_w, tag=tag.char.label("traits"))
            add_button(label="Ideals", width=btn_w, tag=tag.char.label("ideals"))
        with group(horizontal=True):
            add_button(label="Bonds", width=btn_w, tag=tag.char.label("bonds"))
            add_button(label="Flaws", width=btn_w, tag=tag.char.label("flaws"))
    for i in g.list_Ideals: create_ideals(i)
    create_pdescription()






def init_window_block():
    w1 = size.w_block - 16
    w2 = w1 - 16
    h1 = size.H_block - 40
    h2 = h1 - 15
    with group(parent=tag.block.window()):
        with tab_bar(tag=tag.block.tabbar()):
            with tab(label="Features/Traits"):
                with child_window(width=w1, height=h1, border=True):
                    add_separator(label="Race")
                    with child_window(auto_resize_y=True, width=w2, border=True, tag = tag.rfeature.sub()):
                        with group(horizontal=True):
                            add_text("Ability Score Increase: +1/+2", color=c_h1)
                            add_combo(items=g.list_Atr, default_value="",  width=50, no_arrow_button=True, user_data=["Race Asi", 0], callback=cbh, tag=tag.rfeature.select("asi_0"))
                            add_combo(items=g.list_Atr, default_value="",  width=50, no_arrow_button=True, user_data=["Race Asi", 1], callback=cbh, tag=tag.rfeature.select("asi_1"))
                            add_button(label="Clear", enabled=True, width=50, user_data=["Race Asi","Clear"], callback=cbh, tag=tag.rfeature.button("asi_clear"))
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=tag.rfeature.main())
                    add_separator(label="Class")
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=tag.cfeature.sub())
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=tag.cfeature.main())
                    add_separator(label="Feat")
                    with child_window(auto_resize_y=True, width=w2, border=False):
                        with collapsing_header(label="Milestones"):
                            add_child_window(auto_resize_y=True, width=w2, border=True, tag=tag.mfeature.sub())
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=tag.mfeature.main())
                    add_separator(label="Background")
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=tag.bfeature.sub())
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=tag.bfeature.main())
            with tab(label="Actions"):
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    with child_window(auto_resize_y=True, width=w2, border=True):
                        add_separator(label="Weapons")
                        add_child_window(auto_resize_y=True, width=w2, border=True, tag=tag.wactions.window())


def init_window_block_actions_weapons():
    with group(parent=tag.wactions.window()):
        with table(header_row=True, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, resizable=True,borders_outerV=True):
            add_table_column(label="Weapon", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Range", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Hit", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Damage", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Type", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Notes", width_stretch=True, init_width_or_weight=0)
            
            for i in range(2):
                with table_row():
                    for j in g.list_weapon_attributes:
                        add_table_cell(tag=tag.wactions.cell(j,i))


def init_window_inventory():
    h=size.h_inventory
    with group(parent=tag.inve.window()):
        with tab_bar():
            with tab(label="Equip"):
                add_child_window(height=h-28, border=True, no_scrollbar=True, tag=tag.inve.window("equip"))
            with tab(label="Backpack"):
                add_child_window(height=h-80, border=True, no_scrollbar=True, tag=tag.inve.window("backpack"))
                add_child_window(height=h-294, border=True, tag=tag.inve.window("backpack_totals"))
            with tab(label="Bazaar"):
                add_child_window(height=h-26, border=True, no_scrollbar=True,  tag=tag.inve.window("bazaar"))


def init_window_inventory_bazaar():
    with group(parent=tag.inve.window("bazaar")):
        with tab_bar():
            for equipment_type in g.list_equip_type:
                with tab(label=equipment_type):
                    with tab_bar():
                        for rarity in range(5):
                            rank = g.item_rarity(rarity)
                            with tab(label=rank):
                                add_child_window(height=size.h_inventory - 85, border=True, no_scrollbar=True, tag=tag.bazaar(equipment_type, rank))
def load_icons():
    figure_w, figure_h, figure_channel, figure_data = load_image("image/Figure_Icon.png")
    armor_w, armor_h, armor_channel, armor_data = load_image("image/Armor_Icon.png")
    arms_w, arms_h, arms_channel, arms_data = load_image("image/Arms_Icon.png")
    body_w, body_h, body_channel, body_data = load_image("image/Body_Icon.png")
    face_w, face_h, face_channel, face_data = load_image("image/Face_Icon.png")
    hands_w, hands_h, hands_channel, hands_data = load_image("image/Hands_Icon.png")
    head_w, head_h, head_channel, head_data = load_image("image/Head_Icon.png")
    mainhand_w, mainhand_h, mainhand_channel, mainhand_data = load_image("image/MainHand_Icon.png")
    offhand_w, offhand_h, offhand_channel, offhand_data = load_image("image/OffHand_Icon.png")
    ring_w, ring_h, ring_channel, ring_data = load_image("image/Ring_Icon.png")
    shoulders_w, shoulders_h, shoulders_channel, shoulders_data = load_image("image/Shoulders_Icon.png")
    throat_w, throat_h, throat_channel, throat_data = load_image("image/Throat_Icon.png")
    waist_w, waist_h, waist_channel, waist_data = load_image("image/Waist_Icon.png")
    feet_w, feet_h, feet_channel, feet_data = load_image("image/Feet_Icon.png")

    with texture_registry(show=False):
        add_static_texture(width=figure_w, height=figure_h, default_value=figure_data, tag=tag.icon("figure"))
        add_static_texture(width=armor_w, height=armor_h, default_value=armor_data, tag=tag.icon("armor"))
        add_static_texture(width=arms_w, height=arms_h, default_value=arms_data, tag=tag.icon("arms"))
        add_static_texture(width=body_w, height=body_h, default_value=body_data, tag=tag.icon("body"))
        add_static_texture(width=face_w, height=face_h, default_value=face_data, tag=tag.icon("face"))
        add_static_texture(width=hands_w, height=hands_h, default_value=hands_data, tag=tag.icon("hands"))
        add_static_texture(width=head_w, height=head_h, default_value=head_data, tag=tag.icon("head"))
        add_static_texture(width=mainhand_w, height=mainhand_h, default_value=mainhand_data, tag=tag.icon("hand_1"))
        add_static_texture(width=offhand_w, height=offhand_h, default_value=offhand_data, tag=tag.icon("hand_2"))
        add_static_texture(width=ring_w, height=ring_h, default_value=ring_data, tag=tag.icon("ring"))
        add_static_texture(width=shoulders_w, height=shoulders_h, default_value=shoulders_data, tag=tag.icon("shoulders"))
        add_static_texture(width=throat_w, height=throat_h, default_value=throat_data, tag=tag.icon("throat"))
        add_static_texture(width=waist_w, height=waist_h, default_value=waist_data, tag=tag.icon("waist"))
        add_static_texture(width=feet_w, height=feet_h, default_value=feet_data, tag=tag.icon("feet"))
        
def init_window_inventory_equip():
    wbtn = 98
    # (left_side, right_side)
    equipment_pairs = [
        ("Face", "Head"),
        ("Throat", "Shoulders"),
        ("Body", "Armor"),
        ("Hands", "Arms"),
        ("Waist", "Ring_1"),
        ("Feet", "Ring_2"),
        ("Hand_1", "Hand_2"),
    ]
    
    with group(parent="inventory_equip"):
        with group(horizontal=False):
            with group(horizontal=True):
                # Left side
                with group(horizontal=False):
                    for left_slot, right_slot in equipment_pairs:
                        with group(horizontal=True):
                            add_image_button(tag.icon(left_slot), callback=cbh, user_data=["Clear Equip", left_slot, "Clear"], tag=tag.img(left_slot))
                            with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                                add_combo(width=wbtn, no_arrow_button=True, user_data=["Equip Equip", left_slot], callback=cbh, tag=tag.equip(left_slot))
                # Center
                add_image(tag.icon("figure"))
                # Right side
                with group(horizontal=False):
                    for left_slot, right_slot in equipment_pairs:
                        with group(horizontal=True):
                            with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                                add_combo(width=wbtn, no_arrow_button=True, user_data=["Equip Equip", right_slot], callback=cbh, tag=tag.equip(right_slot))
                            add_image_button(tag.icon(right_slot), callback=cbh, user_data=["Clear Equip", right_slot, "Clear"], tag=tag.img(right_slot))


#ANCHOR - Initiative the UI
def init_ui():
    load_icons()
    init_window_Skeleton()
    init_window_core()
    init_window_health()
    init_window_proficienices()
    init_window_characteristics()
    init_window_buffer()
    init_window_attributes()
    init_window_armor()
    init_window_vision()
    init_window_speed()
    init_window_conditions()
    init_window_rest()
    init_window_skills()
    init_window_block()
    init_window_block_actions_weapons()
    init_window_inventory()
    init_window_inventory_bazaar()
    init_window_inventory_equip()
    init_window_wallet()



# #ANCHOR - Populate Start
def populate_Start(): populate_Fields("All")

# #ANCHOR - Populate Fields Handler
def populate_Fields(source):
    field_map = {
        "All": populate_All,
        "Level": populate_All,
        "Long Rest": populate_All,
        
        "Race": populate_Race,
        "Class": populate_Class,
        "Background": populate_Background,
        "Atr": populate_Atr,
        
        "Spell": populate_Spell,
        
        "Arcane Ward": populate_Arcane_Ward,
        
        "Milestone": populate_Milestone,
        
        "Background Prof Select": populate_Background,
        
        "Generic": populate_generic,
        
        "HP": populate_HP,
        
        "Condition": populate_Condition,
        
        "Characteristic": populate_characteristics,
        "Description": populate_characteristics,
        
        "Bazaar Add Item": populate_Inventory,
        
        "Reset Backpack": populate_Inventory,
        
        "Mod Backpack": populate_Backpack,
        
        "Mod Equip": populate_Equip,

        
        "Mod Armor": populate_Armor
        
    }
    field_map[source]()

def populate_All():
    fields_static()
    fields_dynamic()

def populate_Race():
    populate_generic()
    ui_upd_fRace()
    ui_upd_fMilestone()
    
def populate_Class():
    populate_generic()
    ui_upd_fClass()
    ui_upd_spells()


def populate_Background():
    populate_generic()
    ui_upd_fBackground()



def populate_Atr():
    ui_upd_attributes()
    ui_upd_skills()
    ui_upd_initiative()
    ui_upd_block_actions()
    ui_upd_fRace()
    ui_upd_fClass()
    ui_upd_fMilestone()
    ui_upd_spells()

def populate_Spell():
    ui_upd_spells_learn()
    ui_upd_spells_prepare()
    ui_upd_spells_cast()
    
    
    ui_upd_fClass()

def populate_generic():
    ui_upd_core()
    ui_upd_skills()
    ui_upd_health()
    ui_upd_initiative()
    ui_upd_vision()
    ui_upd_speed()
    ui_upd_proficiencies()

def populate_HP():
    ui_upd_health()
    
def populate_Arcane_Ward():
    HP = q.db.Clasq.pc.Abil["Arcane Ward"]["HP"]
    configure_item("Arcane_Ward_HP", label=f"{HP["Current"]} / {HP["Max"]}")

def populate_Milestone():
    populate_Atr()

def populate_Condition():
    ui_upd_conditions()

def fields_static():
    ui_upd_core()
    ui_upd_attributes()
    ui_upd_skills()
    ui_upd_health()
    ui_upd_armor_class()
    ui_upd_initiative()
    ui_upd_vision()
    ui_upd_speed()
    ui_upd_conditions()
    ui_upd_proficiencies()
    ui_upd_character()
    ui_upd_INVE_Bazaar()

def fields_dynamic():
    ui_upd_block()
    ui_upd_INVE()

def populate_characteristics():
    ui_upd_character()

def populate_Inventory():
    ui_upd_INVE()

def populate_Backpack():
    ensure_Backpack()

def populate_Equip():
    ui_upd_block_actions()
    ui_upd_INVE_Equip()
    


def populate_Armor():
    ui_upd_armor_class()

# # #--------------------------------------------------------------------


# #ANCHOR - Static Functions

def ui_upd_core():
    core = q.db.Core
    configure_item(tag.core.val("level"), label=core.L)
    configure_item(tag.core.val("pb"), label = f"PB: +{core.PB}")
    configure_item(tag.core.select("Race"), items=g.list_Race, default_value=core.R)
    configure_item(tag.core.select("Subrace"), items=g.option_Race[core.R], default_value=core.SR)
    configure_item(tag.core.select("Class"), items=g.list_Class, default_value=core.C)
    configure_item(tag.core.select("Subclass"), items=g.option_Class[core.C] if g.valid_class() else [], default_value=core.SC)
    configure_item(tag.core.select("Background"), items=g.list_Background, default_value=g.Background())



def ui_upd_attributes():
    data=q.db.Atr
    for atr in g.list_Atr:
        cdata=data[atr]
        configure_item(tag.atr.sum(atr), label = cdata.Val)
        configure_item(tag.atr.mod(atr), label = cdata.Mod)
        configure_item(tag.atr.select(atr), default_value = cdata.Base)
        configure_item(tag.atr.source("Base"), label = cdata.Base)
        configure_item(tag.atr.source("Race"), label = cdata.Rasi)
        configure_item(tag.atr.source("feat"), label = cdata.Milestone)



def ui_upd_skills():
    for skill in g.list_Skill:
        cdata=q.pc.Skill[skill]
        
        configure_item(tag.skill.toggle(skill), default_value=cdata)
        configure_item(tag.skill.mod(skill), label=g.skill_text(skill))
        # configure_item(f"skill_Player_{skill}", default_value=skill in cdata["Player"])
        # configure_item(f"skill_Race_{skill}", default_value=skill in cdata["Race"])
        # configure_item(f"skill_Class_{skill}", default_value=skill in cdata["Class"])
        # configure_item(f"skill_BG_{skill}", default_value=skill in cdata["Background"])
        # configure_item(f"skill_Feat_{skill}", default_value=skill in cdata["Feat"])
        






def ui_upd_health():
    hp = q.db.HP
    configure_item(tag.health.val("hp"), label = f"{hp["Current"]} / {hp["Sum"]}")
    configure_item(tag.health.val("temp"), label = hp["Temp"])
    set_value(tag.health.max("hp"), hp["Player"])
    

    
def ui_upd_initiative():
    configure_item(tag.init.val(), label = g.Initiative_text())
    configure_item(tag.init.source("dex"), label = q.db.Atr["DEX"]["Mod"])
    configure_item(tag.init.source("race"), label = q.db.Initiative["Race"])
    configure_item(tag.init.source("class"), label = q.db.Initiative["Class"])
    
def ui_upd_vision():
    cdata=q.pc.Vision
    configure_item(tag.vision.val(),label = cdata["Dark"])
    for i in g.list_Vision:configure_item(tag.vision.source(i),label = cdata[i])

def ui_upd_speed():
    cdata=q.pc.Speed
    configure_item(tag.speed.val(),label = cdata["Walk"])
    for i in g.list_Speed: configure_item(tag.speed.source(i),label = cdata[i])

def ui_upd_armor_class():
    ac=q.db.AC
    configure_item(tag.ac.val(), label = ac.Sum)
    configure_item(tag.ac.source("base"), label = ac.Base)
    configure_item(tag.ac.source("dex"), label = ac.Dex)


def ui_upd_conditions():
    for i in g.list_Condition:
        configure_item(tag.cond.toggle(i),default_value = q.db.Condition[i])
        configure_item(tag.cond.text(i), color = g.condition_color(i))

def ui_upd_character():
    cdata=q.db.Characteristic
    for i in g.list_Ideals:
        configure_item(tag.char.input(i), default_value=cdata[i])
        configure_item(tag.char.test(i), default_value=cdata[i])
    
    cdata=q.db.Description
    for i in g.list_Description:
        configure_item(tag.pdesc.input(i), default_value=cdata[i])
        configure_item(tag.pdesc.test(i), default_value=cdata[i])


def ui_upd_proficiencies():
    cdata = q.pc.Prof
    for i in set(q.w.prof("Weapon")) & set(q.w.cat("Simple")):
        configure_item(tag.prof.multi("Simple", i, suffix="toggle"), default_value=i in cdata["Weapon"])
        configure_item(tag.prof.multi("Simple", i, suffix="text"), color=g.prof_color("Weapon", i))

    for i in set(q.w.prof("Weapon")) & set(q.w.cat("Martial")):
        configure_item(tag.prof.multi("Martial", i, suffix="toggle"), default_value=i in cdata["Weapon"])
        configure_item(tag.prof.multi("Martial", i, suffix="text"), color=g.prof_color("Weapon", i))

    for i in q.w.prof("Armor"):
        configure_item(tag.prof.multi("Armor", i, suffix="toggle"), default_value=i in cdata["Armor"])
        configure_item(tag.prof.multi("Armor", i, suffix="text"), color=g.prof_color("Armor", i))

    for i in g.list_Job:
        configure_item(tag.prof.multi("Artisan", i, suffix="toggle"), default_value=i in cdata["Tool"])
        configure_item(tag.prof.multi("Artisan", i, suffix="text"), color=g.prof_color("Tool", i))

    for i in g.list_Game:
        configure_item(tag.prof.multi("Gaming", i, suffix="toggle"), default_value=i in cdata["Tool"])
        configure_item(tag.prof.multi("Gaming", i, suffix="text"), color=g.prof_color("Tool", i))

    for i in g.list_Music:
        configure_item(tag.prof.multi("Musical", i, suffix="toggle"), default_value=i in cdata["Tool"])
        configure_item(tag.prof.multi("Musical", i, suffix="text"), color=g.prof_color("Tool", i))

    for i in g.list_Lang:
        configure_item(tag.prof.multi("Languages", i, suffix="toggle"), default_value=i in cdata["Lang"])
        configure_item(tag.prof.multi("Languages", i, suffix="text"), color=g.prof_color("Lang", i))




def ui_upd_block():
    ui_upd_block_actions()
    ui_upd_features()
    ui_upd_spells()





def ui_upd_block_actions():
    clear_BLOC_Action()

    Hand_1 = q.db.Inventory.Equip["Hand_1"]
    Hand_2 = q.db.Inventory.Equip["Hand_2"]
    two_handed = Hand_1 in q.w.prop("Two-handed")
    Versatile = g.weapon_versatile()
    
    if Hand_1: populate_weapon_actions(Hand_1, 0)
    if not two_handed and not Versatile and Hand_2: populate_weapon_actions(Hand_2, 1)


def populate_weapon_actions(item, idx):
    cdata = g.weapon_action_sc(item)
    with group(parent=f"cell.Action.Weapon.Name.{idx}"): add_text(cdata.Name)
    with group(parent=f"cell.Action.Weapon.Range.{idx}"): add_text(cdata.Range)
    with group(parent=f"cell.Action.Weapon.Hit.{idx}"): 
        with group(horizontal=True):
            add_text(cdata.hSign)
            add_text(cdata.hNum, color=cdata.hColor)
    with group(parent=f"cell.Action.Weapon.Damage.{idx}"): 
        with group(horizontal=True):
            add_text(cdata.dDice)
            add_text(cdata.dSign)
            add_text(cdata.dNum, color=cdata.dColor)
    with group(parent=f"cell.Action.Weapon.Type.{idx}"): 
        add_text(cdata.dType, tag=f"text.Action.Weapon.Type.{idx}")
        item_delete(f"tooltip.Action.Weapon.Type.{idx}")
        with tooltip(f"text.Action.Weapon.Type.{idx}", tag=f"tooltip.Action.Weapon.Type.{idx}"):
            add_text(g.dict_weapon_dtype_description[cdata.dType])

    with group(parent=f"cell.Action.Weapon.Notes.{idx}"):
        with group(horizontal=True):
            for i in cdata.Prop: 
                add_text(g.dict_weapon_prop[i]["SC"], tag=f"text.wprop.{i}.{idx}")
                item_delete(f"tooltip.wprop.{i}.{idx}")
                with tooltip(f"text.wprop.{i}.{idx}", tag=f"tooltip.wprop.{i}.{idx}"):
                    add_text(i, color=c_h1)
                    add_text(g.dict_weapon_prop[i]["Desc"], wrap=240)

def clear_BLOC_Action():
    for atr in g.list_weapon_attributes:
        delete_item(f"cell.Action.Weapon.{atr}.0", children_only=True)
        delete_item(f"cell.Action.Weapon.{atr}.1", children_only=True)





#ANCHOR - SPELLS
def ui_upd_spells():
    w1 = size.w_block - 16
    w2 = w1 - 18
    h1 = size.w_block - 40
    h2 = h1 - 95
    if g.valid_spellclass():
        if not does_item_exist(tag.spell.tabbar()):
            with tab(label="Spell", tag=tag.spell.tab(), parent=tag.block.tabbar()):
                with child_window(auto_resize_y=True, width=w1, height=h1, no_scrollbar=True, border=True):
                    with tab_bar():
                        with tab(label="Cast"):
                            with child_window(auto_resize_y=True, width=w2, height=45, no_scrollbar=True, border=True, tag=tag.scast.sub()):
                                with group(horizontal=True):
                                    add_button(label="Abil", enabled=False, width=40)
                                    add_text("", color=c_h2, tag=tag.spell.text("Abil"))
                                    add_button(label="Atk", enabled=False, width=40)
                                    add_text("", color=c_h2, tag=tag.spell.text("atk"))
                                    add_button(label="DC", enabled=False, width=40)
                                    add_text("", color=c_h2, tag=tag.spell.text("dc"))
                            add_child_window(auto_resize_y=True, width=w2, height=h2, no_scrollbar=True, border=True, tag=tag.scast.main())
                        with tab(label="Learn"):
                            with child_window(auto_resize_y=True, width=w2, height=45, no_scrollbar=True, border=True, tag=tag.slearn.sub()):
                                with group(horizontal=True):
                                    add_text("Cantrips", color=c_h1)
                                    add_text("", color=c_text, tag=tag.slearn.known("cantrip"))
                                    add_text("/", color=c_text)
                                    add_text("", color=c_text, tag=tag.slearn.available("cantrip"))
                                    add_text("Spells", color=c_h1)
                                    add_text("", color=c_text, tag=tag.slearn.known("spell"))
                                    add_text("/", color=c_text)
                                    add_text("", color=c_text, tag=tag.slearn.available("spell"))
                            with child_window(auto_resize_y=True, width=w2, height=h2, no_scrollbar=True, border=True, tag=tag.slearn.main()):
                                with tab_bar():
                                    for i in [1,2,3,4,5,6,7,8,9]:
                                        with tab(label=f"Level {i}"):
                                            add_child_window(auto_resize_y=True, width=w2-20, height=h2-40, no_scrollbar=True, border=True, tag=tag.slearn.wlevel(i))
                        with tab(label="Prepare"):
                            with child_window(auto_resize_y=True, width=w2, height=45, no_scrollbar=True, border=True, tag=tag.sprepare.sub()):
                                with group(horizontal=True):
                                    add_text("Prepared", color=c_h1)
                                    add_text("", color=c_text, tag=tag.sprepare.current())
                                    add_text("/", color=c_text)
                                    add_text("", color=c_text, tag=tag.sprepare.available())
                            with child_window(auto_resize_y=True, width=w2, height=h2, no_scrollbar=True, border=True, tag=tag.sprepare.main()):
                                with tab_bar():
                                    for i in [1,2,3,4,5,6,7,8,9]:
                                        with tab(label=f"Level {i}"):
                                            add_child_window(auto_resize_y=True, width=w2-20, height=h2-40, no_scrollbar=True, border=True, tag=tag.sprepare.wlevel(i))
        ui_upd_spells_learn()
        ui_upd_spells_prepare()  
        ui_upd_spells_cast()
    else: item_delete(tag.spell.tab())

def ui_upd_spells_learn():
    ui_upd_spells_learn_sub()
    ui_upd_spells_learn_main()
    
def ui_upd_spells_prepare():
    ui_upd_spells_prepare_sub()
    ui_upd_spells_prepare_main()
    
def ui_upd_spells_cast():
    ui_upd_spells_cast_sub()
    ui_upd_spells_cast_main()

    
def ui_upd_spells_cast_sub():
    cdata = q.pc.Class.spell_data
    configure_item(tag.spell.text("abil"), default_value=cdata["abil"])
    configure_item(tag.spell.text("atk"), default_value=cdata["atk"])
    configure_item(tag.spell.text("dc"), default_value=cdata["dc"])

def ui_upd_spells_cast_main():
    
    item_clear(tag.scast.main())
    with group(parent=tag.scast.main()):
        for level in range(0, q.pc.Class.spell_data["max_spell_level"] + 1):
            spell_list = q.db.Spell["Book"][0] if level == 0 else q.db.Spell["Prepared"][level]
            if not spell_list: continue
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text(g.list_spell_header[level], color=c_h1)
                    if level > 0:
                        for idx, value in enumerate(q.db.Spell["Slot"][level]): 
                            add_checkbox(default_value=value, enabled=False, tag=tag.scast.toggle(level,idx))

                    button_label = "Cast" if level > 0 else "Will"

                for spell in spell_list:
                    with group(horizontal=True):
                        add_button(label=button_label, width=50, user_data=["Spell Cast", level, spell], callback=cbh, tag=tag.scast.button(level,spell))
                        add_text(spell, color=c_h2, tag=tag.scast.text(level,spell))
                        tooltip_tag = tag.scast.tooltip(level,spell)
                        item_delete(tooltip_tag)
                        with tooltip(tag.scast.text(level,spell), tag=tooltip_tag):
                            spell_detail(spell)
                
            add_separator()

# LEARN TAB FUNCTIONS


def ui_upd_spells_learn_sub():
    configure_item(tag.slearn.known("cantrip"), default_value=g.cantrips_known())
    configure_item(tag.slearn.available("cantrip"), default_value=q.pc.Class.spell_data["cantrips_available"])
    configure_item(tag.slearn.known("spell"), default_value=g.spells_known())
    configure_item(tag.slearn.available("spell"), default_value=q.pc.Class.spell_data["spells_available"])

def ui_upd_spells_learn_main():
    for level in range(1, q.pc.Class.spell_data["max_spell_level"] + 1):
        available_spells = g.List_Spells(q.pc.Class.spell_data["Caster"], level)
        item_clear(tag.slearn.wlevel(level))
        if not available_spells: continue
        with group(parent=tag.slearn.wlevel(level)):
            for spell in available_spells:
                is_known = spell in q.db.Spell["Book"][level]
                add_selectable(label=spell, default_value=is_known, width=680, user_data=["Spell Learn", spell, level], callback=cbh, tag=tag.slearn.toggle(level,spell))
                tooltip_tag = tag.slearn.tooltip(level,spell)
                item_delete(tooltip_tag)
                with tooltip(tag.slearn.toggle(level,spell), tag=tooltip_tag):
                    spell_detail(spell)




def ui_upd_spells_prepare_sub():
    configure_item(tag.slearn.current(), default_value=g.spells_prepared())
    configure_item(tag.sprepare.available(), default_value=q.pc.Class.spell_data["prepared_available"])

def ui_upd_spells_prepare_main():
    for level in range(1, q.pc.Class.spell_data["max_spell_level"] + 1):
        item_clear(tag.sprepare.wlevel(level))
        known_spells = q.db.Spell["Book"][level]
        if not known_spells: continue
        with group(parent=tag.sprepare.wlevel(level)):
            for spell in known_spells:
                is_prepared = spell in q.db.Spell["Prepared"][level]
                add_selectable(label=spell, default_value=is_prepared, width=680, user_data=["Spell Prepare", spell, level], callback=cbh, tag=tag.sprepare.toggle(level,spell))
                tooltip_tag = tag.sprepare.tooltip(level,spell)
                item_delete(tooltip_tag)
                with tooltip(tag.sprepare.toggle(level,spell), tag=tooltip_tag):
                    spell_detail(spell)

def ui_upd_spells_learn_Update():
    for level in range(0, q.pc.Class.spell_data["max_spell_level"] + 1):
        for spell in g.List_Spells(q.pc.Class.spell_data["Caster"], level):
            tag = tag.slearn.toggle(level,spell)
            if does_item_exist(tag): configure_item(tag, default_value=spell in q.db.Spell["Book"][level])

def ui_upd_spells_prepare_Update():
    """Update prepare checkboxes without rebuilding UI"""
    for level in range(1, q.pc.Class.spell_data["max_spell_level"] + 1):
        for spell in q.db.Spell["Book"][level]:
            tag = tag.sprepare.toggle(level,spell)
            if does_item_exist(tag): configure_item(tag, default_value=spell in q.db.Spell["Prepared"][level])

def ui_upd_spells_Update_Cast_Slots():
    """Update just the spell slot checkboxes"""
    for level in range(1, q.pc.Class.spell_data["max_spell_level"] + 1):
        for idx, slot_used in enumerate(q.db.Spell["Slot"][level]):
            tag = tag.scast.toggle(level,idx)
            if does_item_exist(tag): configure_item(tag, default_value=slot_used)

def ui_upd_spells_Update_Stats():
    """Update just the stat displays"""
    stats_map = {
        tag.scast.text("abil"): q.pc.Class.spell_data["abil"],
        tag.scast.text("atk"): q.pc.Class.spell_data["atk"], 
        tag.scast.text("dc"): q.pc.Class.spell_data["dc"]
    }
    for tag, value in stats_map.items():
        if does_item_exist(tag):
            configure_item(tag, default_value=str(value))


# #ANCHOR - Features and traits
def ui_upd_features():
    ui_upd_fMilestone()
    ui_upd_fRace()
    ui_upd_fClass()
    ui_upd_fBackground()

def ui_upd_fRace():
    ui_upd_fRace_sub()
    item_clear(tag.rfeature.main())
    globals()[f"ui_upd_Race_{g.Race()}"]()


def ui_upd_fRace_sub():
    configure_item(tag.rfeature.toggle("asi_0"), default_value = q.db.Race.Rasi[0])
    configure_item(tag.rfeature.toggle("asi_1"), default_value = q.db.Race.Rasi[1])

def ui_upd_fClass():
    ui_upd_fClass_sub()
    item_clear(tag.cfeature.main())
    globals()[f"ui_upd_Class_{q.db.Core.C}"]()

def ui_upd_fClass_sub():
    item_clear(tag.cfeature.sub())
    with group(parent=tag.cfeature.sub()):
        with group(horizontal=True):
            add_text("Skill Select", color=c_h1)
            for idx, key in enumerate(q.db.Class["Skill Select"]):
                add_combo(items=g.dict_Class_Skills[q.db.Core.C], default_value=key,  width=100, no_arrow_button=True, user_data=["Class Skill Select",idx], callback=cbh, tag=tag.cfeature.toggle("skill_select",idx))
            add_button(label = "Clear", user_data=["Class Skill Select", "Clear"], callback=cbh, tag=tag.cfeature.button("skill_select","Clear"))

def ui_upd_fMilestone():
    ui_upd_fMilestone_sub()
    item_clear(tag.mfeature.main())
    for feat in q.db.Milestone["Feat"]:
        if feat:
            func = f"ui_upd_Feat_{feat.replace(' ', '_')}"
            if func in globals():
                globals()[func]()

def ui_upd_fMilestone_sub():
    cdata = q.pc.milestone
    item_clear(tag.mfeature.sub())
    with group(parent=tag.mfeature.sub()):
        for i in range(q.pc.milestone_count):
            with group(horizontal=True):
                add_text(f"Milestone {i}: ", color=c_h1)
                data = cdata["Select"][i]
                add_combo(items=["Feat", "Asi", "Clear"], default_value=data,  width=50, no_arrow_button=True, user_data=["Milestone Level Select", i], callback=cbh, tag=tag.mfeature.select("level", i))
                if data == "Feat":
                    cdata = cdata["Feat"][i]
                    add_combo(items=g.list_Feat, default_value=cdata,  width=150, no_arrow_button=True, user_data=["Milestone Feat Select", i], callback=cbh, tag=tag.mfeature.select("feat", i))
                elif data == "Asi":
                    cdata = cdata["Asi"][i]
                    add_combo(items=g.list_Atr, default_value=cdata[0],  width=50, no_arrow_button=True, user_data=["Milestone Asi Select", i, 0], callback=cbh, tag=tag.mfeature.select("asi_0", i))
                    add_combo(items=g.list_Atr, default_value=cdata[1],  width=50, no_arrow_button=True, user_data=["Milestone Asi Select", i, 1], callback=cbh, tag=tag.mfeature.select("asi_1", i))

# #ANCHOR - FT Background
def ui_upd_fBackground():
    ui_upd_fBackground_sub()
    ui_upd_fBackground_main()

def ui_upd_fBackground_sub():
    item_clear(tag.bfeature.sub())
    data = q.db.Background["Prof"]
    with group(parent=tag.bfeature.sub()):
        with group(horizontal=True):
            add_text("Proficiency Select", color=c_h1)
            for key in data:
                for idx, val in enumerate(data[key]["Select"]):
                    tag_combo = tag.bfeature.select(key,idx)
                    add_combo(items=["Clear"] + g.dict_Background_Skills[q.db.Core.BG], default_value=val, width=100, no_arrow_button=True, user_data=["Background Prof Select", key, idx], callback=cbh, tag=tag_combo)

def ui_upd_fBackground_main():
    item_clear(tag.bfeature.main())
    Background_Feature_Map = {
        "Empty": ["No Feature", "You have no special feature from your background."],
        "Acolyte": ["Shelter of the Faithful", "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for Spell. Those who share your religion will support you (but only you) at a modest lifestyle. You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple."],
        "Charlatan": ["False Identity", "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy"],
        "Criminal": ["Criminal Contact", "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminalq.pc. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."],
        "Entertainer": ["By Popular Demand", "You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you."],
        "FolkHero": ["Rustic Hospitality", "Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you."],
        "GuildArtisan": ["Guild Membership", "As an established and respected member of a guild, you can rely on certain benefits that membership provideq.pc. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelingq.pc. Guilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can bemade for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild's cofferq.pc. You must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild's good graceq.pc."],
        "Hermit": ["Discovery", "The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion. It might be a great truth about the cosmos, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that has long been forgotten, or unearthed some relic of the past that could rewrite history. It might be information that would be damaging to the people who or consigned you to exile, and hence the reason for your return to society."],
        "Noble": ["Position of Privilege", "Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to."],
        "Outlander": ["Wanderer", "You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth."],
        "Sage": ["Researcher", "When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign."],
        "Sailor": ["Ship's Passage", "When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companionq.pc. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you're calling in a favor, you can't be certain of a schedule or route that will meet your every need. Your Dungeon Master will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage."],
        "Soldier": ["Military Rank", "You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized."],
        "Urchin": ["City Secrets", "You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would misq.pc. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow."]
    }
    
    data = Background_Feature_Map[q.db.Core.BG]
    name = data[0]
    desc = data[1]
    
    
    with group(parent=tag.bfeature.main()):
        tag_text = tag.bfeature.text("main","name")
        tag_tooltip = tag.bfeature.tooltip("main","name")
        add_text(name, color=c_h1, tag=tag_text)
        item_delete(tag_tooltip)
        with tooltip(tag_text, tag=tag_tooltip):
            add_text(desc, color=c_text, wrap=size.gwrap)





# #------------------------------------------------


# #ANCHOR - FEATS

def ui_upd_Feat_Actor():
    feat = "Actor"
    tag = feat
    d1 = "Gain advantage on Deception and Performance checks when trying to pass yourself off as a different person."
    d2 = f"You can mimic the speech of another person or the sounds made by other creature. You must have heard the person speaking, or heard the creature make the sound, for at least 1 minute. A successful Wisdom Insight check contested by your {q.db.Skill['Deception']['Mod']:+d} Deception check allows a listener to determine that the effect is faked."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Alert():
    feat = "Alert"
    tag = feat
    d1 = "You can't be surprised while you are consciouse."
    d2 = "Other creatures don't gain advantage on attack rolls against you as a result of being unseen by you."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Athlete():
    feat = "Athlete"
    tag = feat
    d1 = "When you are prone, standing up uses only 5 feet of your movement."
    d2 = "Climbing doesn't cost you extra movement."
    d3 = "You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than 10 feet."
    t1_header = tag.mfeature.header(tag)
    tag_popup = tag.mfeature.popup(tag)
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=t1_header)
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))
        item_delete(tag_popup)
        with popup(t1_header, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=tag_popup):
            with group(horizontal=False):
                add_combo(items=["Clear"]+g.dict_Feat_Lists[feat], default_value=q.db.Milestone.Data[feat]["Select"][0], width=50, no_arrow_button=True, user_data=["Milestone Feat Choice",feat, 0], callback=cbh, tag=tag.mfeature.select(tag,"0"))

def ui_upd_Feat_Charger():
    feat = "Charger"
    tag = feat
    d1 = "When you use your action to Dash, you can use a bonus action to make one melee weapon attack or shove a creature, and if you moved at least 10 feet in a straight line immediately before taking this bonus action, you gain a +5 bonus to the attack's damage roll or push the target with extra force."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))

def ui_upd_Feat_Crossbow_Expert():
    feat = "Crossbow Expert"
    tag = feat.replace(" ", "_")
    d1 = "You ignore the loading quality of crossbows with which you are proficient."
    d2 = "Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rollq.pc."
    d3 = "When you use the Attack action and attack with a one-handed weapon, you can use a bonus action to fire a hand crossbow you are holding."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Defensive_Duelist():
    feat = "Defensive Duelist"
    tag = feat.replace(" ", "_")
    d1 = "When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can use your reaction to add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))

def ui_upd_Feat_Dual_Wielder():
    feat = "Dual Wielder"
    tag = feat.replace(" ", "_")
    d1 = "You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand."
    d2 = "You can use two-weapon fighting even when the one-handed melee weapons you are wielding aren't light."
    d3 = "You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Dungeon_Delver():
    feat = "Dungeon Delver"
    tag = feat.replace(" ", "_")
    d1 = "You have advantage on Wisdom (Perception) and Intelligence (Investigation) checks made to detect the presence of secret doorq.pc."
    d2 = "You have advantage on saving throws made to avoid or resist trapq.pc."
    d3 = "You take no damage from traps that would normally deal half damage on a successful save."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Durable():
    feat = "Durable"
    tag = feat
    d1 = f"When you roll a Hit Die to regain hit points, the minimum number of hit points you regain from the roll equals {q.db.Atr['CON']['Mod'] * 2}."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))

def ui_upd_Feat_Elemental_Adept():
    feat = "Elemental Adept"
    tag = "ElementalAdept"
    value = q.db.Milestone["Data"][tag]["Select"][0]
    d1 = f"Spells you cast ignore resistance to {value} damage."
    d2 = f"When you roll damage for a spell you cast that deals {value} damage, you treat any 1 on a damage die as a 2."
    t1_header = tag.mfeature.header(tag)
    tag_popup = tag.mfeature.popup(tag)
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=t1_header)
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        item_delete(tag_popup)
        with popup(t1_header, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=tag_popup):
            with group(horizontal=False):
                add_combo(items=g.dict_Feat_Lists[tag], default_value=value, width=100, no_arrow_button=True, user_data=["Milestone Feat Choice", tag, 0], callback=cbh, tag=tag.mfeature.select(tag,"0"))

def ui_upd_Feat_Grappler():
    feat = "Grappler"
    tag = feat
    d1 = "You have advantage on attack rolls against a creature you are grappling."
    d2 = "You can use your action to try to pin a creature grappled by you. To do so, make another grapple check. If you succeed, you and the creature are both restrained until the grapple endq.pc."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Great_Weapon_Master():
    feat = "Great Weapon Master"
    tag = feat.replace(" ", "_")
    d1 = "On your turn, when you score a critical hit with a melee weapon or reduce a creature to 0 hit points with one, you can make one melee weapon attack as a bonus action."
    d2 = "Before you make a melee attack with a heavy weapon you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Healer():
    feat = "Healer"
    tag = feat
    d1 = "When you use a healer's kit to stabilize a dying creature, that creature also regains 1 hit point."
    d2 = "As an action, you can spend one use of a healer's kit to tend to a creature and restore 1d6 + 4 hit points to it, plus additional hit points equal to the creature's maximum number of Hit Dice. The creature can't regain hit points from this feat again until it finishes a short or long rest."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Heavily_Armored():
    feat = "Heavily Armored"
    tag = feat.replace(" ", "_")
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))

def ui_upd_Feat_Heavy_Armor_Master():
    feat = "Heavy Armor Master"
    tag = feat.replace(" ", "_")
    d1 = "Prerequisite: Proficiency with heavy armor"
    d2 = "While you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from nonmagical attacks is reduced by 3."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Inspiring_Leader():
    feat = "Inspiring Leader"
    tag = feat.replace(" ", "_")
    d1 = f"You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, choose up to six friendly creatures (which can include yourself) within 30 feet of you who can see or hear you and who can understand you. Each creature gains temporary hit points equal to your level + {q.db.Atr['CHA']['Mod']}."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))

def ui_upd_Feat_Keen_Mind():
    feat = "Keen Mind"
    tag = feat.replace(" ", "_")
    d1 = "You always know which way is north."
    d2 = "You always know the number of hours left before the next sunrise or sunset."
    d3 = "You can accurately recall anything you have seen or heard within the past month."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Lightly_Armored():
    feat = "Lightly Armored"
    tag = "LightlyArmored"
    t1_header = tag.mfeature.header(tag)
    tag_popup = tag.mfeature.popup(tag)
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=t1_header)
        item_delete(tag_popup)
        with popup(t1_header, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=tag_popup):
            with group(horizontal=False):
                add_combo(items=g.dict_Feat_Lists[tag], default_value=q.db.Milestone["Data"][tag]["Select"][0], width=50, no_arrow_button=True, user_data=["Milestone Feat Choice", tag, 0], callback=cbh, tag=tag.mfeature.select(tag,"0"))

def ui_upd_Feat_Lucky():
    feat = "Lucky"
    tag = feat
    use = q.db.Milestone["Data"][feat]["Use"]
    d1 = "You have 3 luck pointq.pc. Whenever you make an attack roll, an ability check, or a saving throw, you can spend one luck point to roll an additional d20. You can choose to spend one of your luck points after you roll the die, but before the outcome is determined. You choose which of the d20s is used for the attack roll, ability check, or saving throw."
    d2 = "You can also spend one luck point when an attack roll is made against you. Roll a d20, and then choose whether the attack uses the attacker's roll or yourq.pc. If more than one creature spends a luck point to influence the outcome of a roll, the points cancel each other out; no additional dice are rolled."
    with group(parent=tag.mfeature.main()):
        with group(horizontal=True):
            add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
            for idx, val in enumerate(use):
                add_checkbox(default_value=val, enabled=True, user_data=["Milestone Feat Use", feat, idx], callback=cbh, tag=f"checkbox.fMilestone.{tag}.Use.{idx}")
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Mage_Slayer():
    feat = "Mage Slayer"
    tag = feat.replace(" ", "_")
    d1 = "When a creature within 5 feet of you casts a spell, you can use your reaction to make a melee weapon attack against that creature."
    d2 = "When you damage a creature that is concentrating on a spell, that creature has disadvantage on the saving throw it makes to maintain its concentration."
    d3 = "You have advantage on saving throws against spells cast by creatures within 5 feet of you."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Medium_Armor_Master():
    feat = "Medium Armor Master"
    tag = feat.replace(" ", "_")
    d1 = "Wearing medium armor doesn't impose disadvantage on your Dexterity (Stealth) checkq.pc."
    d2 = "When you wear medium armor, you can add 3, rather than 2, to your AC if you have a Dexterity of 16 or higher."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Mobile():
    feat = "Mobile"
    tag = feat
    d1 = "When you use the Dash action, difficult terrain doesn't cost you extra movement on that turn."
    d2 = "When you make a melee attack against a creature, you don't provoke opportunity attacks from that creature for the rest of the turn, whether you hit or not."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Moderately_Armored():
    feat = "Moderately Armored"
    tag = feat.replace(" ", "_")
    t1_header = tag.mfeature.header(tag)
    tag_popup = tag.mfeature.popup(tag)
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=t1_header)
        item_delete(tag_popup)
        with popup(t1_header, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=tag_popup):
            with group(horizontal=False):
                add_combo(items=g.dict_Feat_Lists[tag], default_value=q.db.Milestone["Data"][tag]["Select"][0], width=50, no_arrow_button=True, user_data=["Milestone Feat Choice", tag, 0], callback=cbh, tag=tag.mfeature.select(tag,"0"))

def ui_upd_Feat_Mounted_Combatant():
    feat = "Mounted Combatant"
    tag = feat.replace(" ", "_")
    d1 = "You have advantage on melee attack rolls against any unmounted creature that is smaller than your mount."
    d2 = "You can force an attack targeted at your mount to target you instead."
    d3 = "If your mount is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it failq.pc."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Polearm_Master():
    feat = "Polearm Master"
    tag = feat.replace(" ", "_")
    d1 = "When you take the Attack action and attack with only a glaive, halberd, quarterstaff, or spear, you can use a bonus action to make a melee attack with the opposite end of the weapon. This attack uses the same ability modifier as the primary attack. The weapon's damage die for this attack is a d4, and it deals bludgeoning damage."
    d2 = "While you are wielding a glaive, halberd, pike, quarterstaff, or spear, other creatures provoke an opportunity attack from you when they enter the reach you have with that weapon."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))

def ui_upd_Feat_Resilient():
    feat = "Resilient"
    tag = feat
    t1_header = tag.mfeature.header(tag)
    tag_popup = tag.mfeature.popup(tag)
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=t1_header)
        item_delete(tag_popup)
        with popup(t1_header, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=tag_popup):
            with group(horizontal=False):
                add_combo(items=g.dict_Feat_Lists[feat], default_value=q.db.Milestone["Data"][feat]["Select"][0], width=50, no_arrow_button=True, user_data=["Milestone Feat Choice", feat, 0], callback=cbh, tag=tag.mfeature.select(tag,"0"))

def ui_upd_Feat_Savage_Attacker():
    feat = "Savage Attacker"
    tag = feat.replace(" ", "_")
    d1 = "Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon's damage dice and use either total."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))

def ui_upd_Feat_Sentinel():
    feat = "Sentinel"
    tag = feat
    d1 = "When you hit a creature with an opportunity attack, the creature's speed becomes 0 for the rest of the turn."
    d2 = "Creatures provoke opportunity attacks from you even if they take the Disengage action before leaving your reach."
    d3 = "When a creature within 5 feet of you makes an attack against a target other than you (and that target doesn't have this feat), you can use your reaction to make a melee weapon attack against the attacking creature."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Sharp_shooter():
    feat = "Sharpshooter"
    tag = feat
    d1 = "Attacking at long range doesn't impose disadvantage on your ranged weapon attack rollq.pc."
    d2 = "Your ranged weapon attacks ignore half cover and three-quarters cover."
    d3 = "Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Shield_Master():
    feat = "Shield Master"
    tag = feat.replace(" ", "_")
    d1 = "If you take the Attack action on your turn, you can use a bonus action to try to shove a creature within 5 feet of you with your shield."
    d2 = "If you aren't incapacitated, you can add your shield's AC bonus to any Dexterity saving throw you make against a spell or other harmful effect that targets only you."
    d3 = "If you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you can use your reaction to take no damage if you succeed on the saving throw, interposing your shield between yourself and the source of the effect."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Skulker():
    feat = "Skulker"
    tag = feat
    d1 = "You can try to hide when you are lightly obscured from the creature from which you are hiding."
    d2 = "When you are hidden from a creature and miss it with a ranged weapon attack, making the attack doesn't reveal your position."
    d3 = "Dim light doesn't impose disadvantage on your Wisdom (Perception) checks that rely on sight."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Tavern_Brawler():
    feat = "Tavern Brawler"
    tag = feat.replace(" ", "_")
    d1 = f"You are proficient with improvised Weapon. Your unarmed strike uses a d4 for damage. When you hit a creature with an unarmed strike or an improvised weapon on your turn, you can use a bonus action to attempt to grapple the target."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))

def ui_upd_Feat_Tough():
    feat = "Tough"
    tag = feat
    d1 = "Your hit point maximum increases by an amount equal to twice your level when you gain this feat. Whenever you gain a level thereafter, your hit point maximum increases by an additional 2 hit pointq.pc."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))

def ui_upd_Feat_War_Caster():
    feat = "War Caster"
    tag = feat
    d1 = "You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage."
    d2 = "You can perform the somatic components of spells even when you have weapons or a shield in one or both handq.pc."
    d3 = "When a hostile creature's movement provokes an opportunity attack from you, you can use your reaction to cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of 1 action and must target only that creature."
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=tag.mfeature.header(tag))
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        add_text(d2, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"1"))
        add_text(d3, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"2"))

def ui_upd_Feat_Weapon_Master():
    feat = "Weapon Master"
    tag = feat.replace(" ", "_")
    select = q.db.Milestone["Data"][tag]["Select"]
    d1 = "You gain proficiency with four weapons of your choice."
    t1_header = tag.mfeature.header(tag)
    tag_popup = tag.mfeature.popup(tag)
    with group(parent=tag.mfeature.main()):
        add_text(feat, color=c_h1, tag=t1_header)
        add_text(d1, color=c_text, wrap=size.gwrap, tag=tag.mfeature.text(tag,"0"))
        item_delete(tag_popup)
        with popup(t1_header, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=tag_popup):
            with group(horizontal=False):
                for i in [0,1,2,3]:
                    add_combo(items=g.dict_Feat_Lists[tag], default_value=select[i], width=100, no_arrow_button=True, user_data=["Milestone Feat Choice", tag, i], callback=cbh, tag=tag.mfeauture.select(tag,i))

# #------------------------------------------------




def spell_detail(spell):
    data = g.Grimoir[spell]
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


# #----------------------------------------------------

# #ANCHOR - RACE


# Fixed Race UI Functions with Proper Naming

def ui_upd_Race_Empty():
    parent = "empty"
    pass

def ui_upd_Race_Human():
    parent = "human"
    pass

def ui_upd_Race_Human_Standard():
    parent = "human_standard"
    pass

def ui_upd_Race_Human_Variant():
    parent = "human_variant"
    pass

def ui_upd_Race_Elf():
    parent = "elf"
    with group(parent=tag.rfeature.main()):
        a1 = "Fey Ancestry"
        t1 = a1.replace(" ", "_")
        d1 = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
        
        a2 = "Trance"
        t2 = a2.replace(" ", "_")
        d2 = "You don't need to sleep. Instead, you meditate deeply, remaining semiconscious, for 4 hours a day."
        
        add_text(a1, color=c_h1, wrap=size.gwrap)
        add_text(d1, color=c_text, wrap=size.gwrap)
        
        add_text(a2, color=c_h1, wrap=size.gwrap)
        add_text(d2, color=c_text, wrap=size.gwrap)
    if g.Subrace(): globals()[f"ui_upd_Race_{g.Race()}_{g.Subrace()}"]()

def ui_upd_Race_Elf_High():
    parent = "elf_high"
    with group(parent=tag.rfeature.main()):
        a1 = "Cantrip"
        cdata1=q.db.Race.Abil["Cantrip"]
        spell = cdata1["Select"][0]

        t1_header = tag.rfeature.header(parent, a1)
        tag_label = tag.rfeature.label(parent, a1)
        tag_tooltip = tag=tag.rfeature.tooltip(parent, a1)
        tag_popup = tag.rfeature.popup(parent, a1)
        tag_select = tag.rfeature.select(parent, a1)
        with group(horizontal=True):
            add_text(a1, color=c_h1, wrap=size.gwrap, tag=t1_header)
            add_text(spell, color=c_h2, wrap=size.gwrap, tag=tag_label)
            if spell:
                item_delete(tag_tooltip)
                with tooltip(tag_label, tag=tag_tooltip):
                    spell_detail(spell)
        item_delete(tag_popup)
        with popup(t1_header, mousebutton=mvMouseButton_Left, tag=tag_popup):
            add_combo(items=g.list_High_Elf_Cantrip, default_value=spell, width=120, no_arrow_button=True, user_data=["Race Spell Select","Cantrip"], callback=cbh, tag=tag_select)


def ui_upd_Race_Elf_Wood():
    parent = "elf_wood"
    with group(parent=tag.rfeature.main()):
        a1 = "Mask of the Wild"
        t1 = a1.replace(" ", "_")
        d1 = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
        add_text(a1, color=c_h1, wrap=size.gwrap)
        add_text(d1, color=c_text, wrap=size.gwrap)

def ui_upd_Race_Elf_Drow():
    parent = "elf_drow"
    with group(parent=tag.rfeature.main()):
        a1 = "Drow Magic"
        t1 = a1.replace(" ", "_")
        cdata=q.db.Race.Abil["Drow Magic"]
        
        tag_label = tag.rfeature.label(parent, a1, spell)
        tag_tooltip = tag.rfeature.tooltip(parent, a1, spell)
        add_text(a1, color=c_h1, wrap=300)
        for spell in cdata.keys():
            with group(horizontal=True):
                add_text(spell, color=c_h2, wrap=300, tag=tag.rfeature.label(parent, a1, spell))
                if "Use" in cdata[spell]:
                    tag_toggle = tag.rfeature.toggle(parent, t1, spell)
                    add_checkbox(default_value=cdata[spell]["Use"][0], enabled=True, user_data=["Race Spell Use",t1,spell], callback=cbh, tag=tag_toggle)
            item_delete(tag_tooltip)
            with tooltip(tag_label, tag=tag_tooltip): spell_detail(spell)



def ui_upd_Race_Elf_ShadarKai():
    parent = "elf_shadarkai"

    a1 = "Blessing of the Raven Queen"; t1 = a1.replace(" ", "_")
    cdata = q.db.Race.Abil[a1]
    t1_header = tag.rfeature.header(parent,t1)
    tag_text = tag.rfeature.text(parent,t1)
    
    if q.db.Core.L < 3:desc = "(Bonus Action) Teleport up to 30 ft to an unoccupied space you can see. You can use this a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."
    else:desc = "(Bonus Action) Teleport up to 30 ft to an unoccupied space you can see. You can use this a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. Immediately after you use it, you gain resistance to all damage until the start of your next turn."

    with group(parent=tag.rfeature.main()):
        with group(horizontal=False):
            with group(horizontal=True):
                add_text(a1, color=c_h1, wrap=size.gwrap, tag=t1_header)
                for idx, val in enumerate(cdata["Use"]):
                    tag_toggle = tag.rfeature.toggle(parent,t1,idx)
                    add_checkbox(default_value=val, enabled=True, user_data=["Race Use", a1, idx], callback=cbh, tag=tag_toggle)
            add_text(desc, color=c_text, wrap=size.gwrap, tag=tag_text)

def ui_upd_Race_Dwarf():
    parent = "dwarf"
    a1 = "Dwarven Resilience"; t1 = a1.replace(" ", "_")
    d1 = "You have advantage on saving throws against poison, and you have resistance against poison damage."
    a2 = "Stonecunning"; t2 = a2.replace(" ", "_")
    d2 = f"Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonuq.pc."
    
    t1_header = tag.rfeature.header(parent,t1)
    t1_text = tag.rfeature.text(parent,t1)

    t2_header = tag.rfeature.header(parent,t2)
    t2_text = tag.rfeature.text(parent,t2)
    with group(parent=tag.rfeature.main()):
        add_text(a1, color=c_h1, wrap=size.gwrap, tag=t1_header)
        add_text(d1, color=c_text, wrap=size.gwrap, tag=t1_text)
        add_text(a2, color=c_h1, wrap=size.gwrap, tag=t2_header)
        add_text(d2, color=c_text, wrap=size.gwrap, tag=t2_text)
    if g.Subrace(): globals()[f"ui_upd_Race_{g.Race()}_{g.Subrace()}"]()

def ui_upd_Race_Dwarf_Hill():
    parent = "dwarf_hill"
    

    a1 = "Dwarven Toughness"; t1 = a1.replace(" ", "_")
    d1 = "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."

    t1_header = tag.rfeature.header(parent,t1)
    t1_text = tag.rfeature.text(parent,t1)
    
    
    with group(parent=tag.rfeature.main()):
        add_text(a1, color=c_h1, wrap=size.gwrap, tag=t1_header)
        add_text(d1, color=c_text, wrap=size.gwrap, tag=t1_text)

def ui_upd_Race_Dwarf_Mountain():
    parent = "dwarf_mountain"
    pass

def ui_upd_Race_Halfling():
    parent = "halfling"
    
    a1 = "Lucky"; t1 = a1.replace(" ", "_")
    d1 = "When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll."

    a2 = "Brave"; t2 = a2.replace(" ", "_")
    d2 = "You have advantage on saving throws against being frightened."

    a3 = "Halfling Nimbleness"; t3 = a3.replace(" ", "_")
    d3 = "You can move through the space of any creature that is of a size larger than yours"
    
    t1_header = tag.rfeature.header(parent,t1)
    t1_text = tag.rfeature.text(parent,t1)

    t2_header = tag.rfeature.header(parent,t2)
    t2_text = tag.rfeature.text(parent,t2)

    t3_header = tag.rfeature.header(parent,t3)
    t3_text = tag.rfeature.text(parent,t3)
    
    with group(parent=tag.rfeature.main()):
        add_text(a1, color=c_h1, wrap=size.gwrap, tag=t1_header)
        add_text(d1, color=c_text, wrap=size.gwrap, tag=t1_text)
        add_text(a2, color=c_h1, wrap=size.gwrap, tag=t2_header)
        add_text(d2, color=c_text, wrap=size.gwrap, tag=t2_text)
        add_text(a3, color=c_h1, wrap=size.gwrap, tag=t3_header)
        add_text(d3, color=c_text, wrap=size.gwrap, tag=t3_text)
    if g.Subrace(): globals()[f"ui_upd_Race_{g.Race()}_{g.Subrace()}"]()

def ui_upd_Race_Halfling_Lightfoot():
    parent = "halfling_lightfoot"
    a1 = "Naturally Stealthy"; t1 = a1.replace(" ", "_")
    d1 = "You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."
    t1_header = tag.rfeature.header(parent, t1)
    t1_text = tag.rfeature.text(parent, t1)
    with group(parent=tag.rfeature.main()):
        add_text(a1, color=c_h1, wrap=size.gwrap, tag=t1_header)
        add_text(d1, color=c_text, wrap=size.gwrap, tag=t1_text)


def ui_upd_Race_Halfling_Stout():
    parent = "halfling_stout"
    a1 = "Stout Resilience"; t1 = a1.replace(" ", "_")
    d1 = "You have advantage on saving throws against poison, and you have resistance against poison damage."
    t1_header = tag.rfeature.header(parent, t1)
    t1_text = tag.rfeature.text(parent, t1)
    with group(parent=tag.rfeature.main()):
        add_text(a1, color=c_h1, wrap=size.gwrap, tag=t1_header)
        add_text(d1, color=c_text, wrap=size.gwrap, tag=t1_text)


def ui_upd_Race_Gnome():
    parent = "gnome"

    a1 = "Gnome Cunning"; t1 = a1.replace(" ", "_")
    d1 = "You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."

    t1_header = tag.rfeature.header(parent, t1)
    t1_text = tag.rfeature.text(parent, t1)

    with group(parent=tag.rfeature.main()):
        add_text(a1, color=c_h1, wrap=size.gwrap, tag=t1_header)
        add_text(d1, color=c_text, wrap=size.gwrap, tag=t1_text)
    if g.Subrace():globals()[f"ui_upd_Race_{g.Race()}_{g.Subrace()}"]()

def ui_upd_Race_Gnome_Forest():
    parent = "gnome_forest"
    
    a1 = "Speak with Small Beasts"; t1 = a1.replace(" ", "_")
    d1 = "Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts."

    a2 = "Natural Illusionist"; t2 = a2.replace(" ", "_")


    t1_header = tag.rfeature.header(parent, t1)
    t1_text = tag.rfeature.text(parent, t1)

    t2_header = tag.rfeature.header(parent, t2)
    t2_text = tag.rfeature.text(parent, t2)
    cdata = q.db.Race.Abil[a2]
    
    # with group(parent=tag.rfeature.main()):
    #     add_text(a1, color=c_h1, wrap=size.gwrap, tag=t1_header)
    #     add_text(d1, color=c_text, wrap=size.gwrap, tag=t1_text)
        
        
    #     with group(horizontal=True):
    #         add_text(a2, color=c_h1, wrap=size.gwrap, tag=t2_header)
            
    #         for spell in cdata.keys():
    #             with group(horizontal=True):
    #             add_text(spell, color=c_h2, wrap=300, tag=t2_text)
    #             item_delete(tag_spell_tip)
    #             with tooltip(tag_spell_name, tag=tag_spell_tip):
    #                 spell_detail(spell)

def ui_upd_Race_Gnome_Rock():
    pass
    parent = "gnome_rock"
    # with group(parent=tag.rfeature.main()):
    #     tinker_header_tag = "text.fRace.Gnome.Rock.Tinker.Header"
    #     tinker_tooltip_tag = "tooltip.fRace.Gnome.Rock.Tinker.Detail"
    #     add_text("Tinker", color=c_h1, tag=tinker_header_tag)
    #     item_delete(tinker_tooltip_tag)
    #     with tooltip(tinker_header_tag, tag=tinker_tooltip_tag):
    #         add_text("Tinker", color=c_h1)
    #         add_text("Using tinker's tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp)...", color=c_text, wrap=300)
    #     add_text("Artificer's Lore", color=c_h1, tag="text.fRace.Gnome.Rock.ArtificersLore.Header")
    #     add_text("Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply.", color=c_text, wrap=size.gwrap, tag="text.fRace.Gnome.Rock.ArtificersLore.Desc")

def ui_upd_Race_Dragonborn():
    pass
    # parent = "dragonborn"
    # if g.Subrace(): 
    #     ui_upd_Race_Dragonborn_subrace()

def ui_upd_Race_Dragonborn_subrace():
    #parent = f"dragonborn_{g.Subrace()}"
    pass
    
    # dnum_map = [0,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]
    # dnum = dnum_map[q.db.Core.L] if q.db.Core.L < len(dnum_map) else 5
    # type_map = {"Black": "Acid", "Blue": "Lightning", "Brass": "Fire", "Bronze": "Lightning", "Copper": "Acid", "Gold": "Fire", "Green": "Poison", "Red": "Fire", "Silver": "Cold", "White": "Cold"}
    # save_map = {"Acid": "DEX", "Lightning": "DEX", "Fire": "DEX", "Poison": "CON", "Cold": "CON"}
    # type = type_map.get(g.Subrace(), "Fire")
    # save = save_map.get(type, "DEX")
    # dc = 8 + q.db.Core.PB +q.db.Atr[save]['Mod']
    # breath_weapon_desc = f"(Action) Exhale destructive energy. Each creature in a 30ft line must make a DC {dc} {save} saving throw, taking {dnum}d6 {type.lower()} damage on a failed save, and half as much damage on a successful one."
    # draconic_resistance_desc = f"You have resistance to {type.lower()} damage."
    # with group(parent=tag.rfeature.main()):
    #     add_text("Draconic Resistance", color=c_h1, wrap=size.gwrap, tag="text.fRace.Dragonborn.DraconicResistance.Header")
    #     add_text(draconic_resistance_desc, color=c_text, wrap=size.gwrap, tag="text.fRace.Dragonborn.DraconicResistance.Desc")
    #     cdata = q.db.Race.Abil["Breath Weapon"]
    #     with group(horizontal=False):
    #         with group(horizontal=True):
    #             add_text("Breath Weapon", color=c_h1, wrap=size.gwrap, tag="text.fRace.Dragonborn.BreathWeapon.Header")
    #             add_checkbox(default_value=cdata["Use"][0], enabled=True, user_data=["Race Use", "Breath Weapon", 0], callback=cbh, tag="checkbox.fRace.Dragonborn.BreathWeapon.Use.0")
    #         add_text(breath_weapon_desc, color=c_text, wrap=size.gwrap, tag="text.fRace.Dragonborn.BreathWeapon.Desc")

def ui_upd_Race_HalfOrc():
    pass
    # parent = "halforc"
    # cdata = q.db.Race.Abil["Relentless Endurance"]
    # with group(parent=tag.rfeature.main()):
    #     with group(horizontal=True):
    #         add_text("Relentless Endurance", color=c_h1, wrap=size.gwrap, tag="text.fRace.HalfOrc.RelentlessEndurance.Header")
    #         add_checkbox(default_value=cdata["Use"][0], enabled=True, user_data=["Race Use", "Relentless Endurance", 0], callback=cbh, tag="checkbox.fRace.HalfOrc.RelentlessEndurance.Use.0")
    #     add_text("When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.", color=c_text, wrap=size.gwrap, tag="text.fRace.HalfOrc.RelentlessEndurance.Desc")
    #     add_text("Savage Attacks", color=c_h1, wrap=size.gwrap, tag="text.fRace.HalfOrc.SavageAttackq.pc.Header")
    #     add_text("When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit.", color=c_text, wrap=size.gwrap, tag="text.fRace.HalfOrc.SavageAttackq.pc.Desc")
    # if g.Subrace(): globals()[f"ui_upd_Race_{g.Race()}_{g.Subrace()}"]()

def ui_upd_Race_HalfOrc_Standard():
    #parent = "halforc_standard"
    pass

def ui_upd_Race_Tiefling():
    pass
    # parent = "tiefling"
    # tiefling_map={"Asmodeus": "Infernal Legacy","Baalzebul": "Legacy of Maladomini","Dispater": "Legacy of Dis","Fierna": "Legacy of Phlegethos","Glasya": "Legacy of Malbolge","Levistus": "Legacy of Stygia","Mammon": "Legacy of Minauros","Mephistopheles": "Legacy of Cania","Zariel": "Legacy of Avernus"}
    # if g.Subrace(): 
    #     legacy = tiefling_map.get(g.Subrace(), "Infernal Legacy")
    #     cdata=q.db.Race.Abil.get(legacy, {})
    #     if cdata:
    #         ui_upd_Race_Tiefling_subrace(cdata, legacy)

def ui_upd_Race_Tiefling_subrace(cdata,legacy):
    pass
    # parent = f"tiefling_{g.Subrace()}"
    # legacy_tag = legacy.replace(" ", "")
    # with group(parent=tag.rfeature.main()):
    #     add_text(legacy, color=c_h1, wrap=300, tag=f"text.fRace.Tiefling.{legacy_tag}.Header")
    #     for spell in cdata.keys():
    #         tag_spell_name = f"text.fRace.Tiefling.{legacy_tag}.{spell}.Name"
    #         tag_spell_tip = f"tooltip.fRace.Tiefling.{legacy_tag}.{spell}.Detail"
    #         with group(horizontal=True):
    #             add_text(spell, color=c_h2, wrap=300, tag=tag_spell_name)
    #             if "Use" in cdata[spell]:
    #                 add_checkbox(default_value=cdata[spell]["Use"][0], enabled=True, user_data=["Race Spell Use",legacy,spell], callback=cbh, tag=f"checkbox.fRace.Tiefling.{legacy_tag}.{spell}.Use")
    #         item_delete(tag_spell_tip)
    #         with tooltip(tag_spell_name, tag=tag_spell_tip):
    #             spell_detail(spell)

def ui_upd_Race_Harengon():
    pass
    # parent = "Harengon"
    # with group(parent=tag.rfeature.main()):
    #     add_text("Lucky Footwork", color=c_h1, wrap=size.gwrap, tag="text.fRace.Harengon.LuckyFootwork.Header")
    #     add_text("When you fail a Dexterity saving throw, you can use your reaction to roll a d4 and add it to the save, potentially turning the failure into a succesq.pc.", color=c_text, wrap=size.gwrap, tag="text.fRace.Harengon.LuckyFootwork.Desc")
    #     cdata = q.db.Race.Abil["Rabbit Hop"]
    #     with group(horizontal=True):
    #         add_text("Rabbit Hop", color=c_h1, wrap=size.gwrap, tag="text.fRace.Harengon.RabbitHop.Header")
    #         for idx, val in enumerate(cdata["Use"]):
    #             add_checkbox(default_value=val, enabled=True, user_data=["Race Use", "Rabbit Hop", idx], callback=cbh, tag=f"checkbox.fRace.Harengon.RabbitHop.Use.{idx}")
    #     add_text(f"As a bonus action, you can jump a number of feet equal to five times your proficiency bonus, without provoking opportunity attackq.pc.", color=c_text, wrap=size.gwrap, tag="text.fRace.Harengon.RabbitHop.Desc")
    # if g.Subrace(): globals()[f"ui_upd_Race_{g.Race()}_{g.Subrace()}"]()

def ui_upd_Race_Harengon_Standard():
    parent = "Harengon_standard"
    pass

# #-----------------------------------------------------------

# #ANCHOR - Class shit

def ui_upd_Class_Empty():
    pass
    
def ui_upd_Class_Fighter():
    data = q.db.Class["Abil"]
    with group(parent="cw.fClass.Main"):
        if "Fighting Style" in data:
            feat = "Fighting Style"
            tag = feat.replace(" ", "_")
            cdata = data["Fighting Style"]
            t1_header = f"text.fClass.Fighter.{tag}.Header"
            tag_popup = f"popup.fClass.Fighter.{tag}.Select"
            add_text("Fighting Style", color=c_h1, wrap=size.gwrap, tag=t1_header)
            item_delete(tag_popup)
            with popup(t1_header, mousebutton=mvMouseButton_Left, tag=tag_popup):
                for idx, value in enumerate(cdata["Select"]):
                    add_combo(items=g.list_Fighting_Styles, default_value=value, width=80, no_arrow_button=True, callback=cbh, user_data=["Class Select", "Fighting Style", idx], tag=f"combo.fClass.Fighter.{tag}.Choice.{idx}")
            for item in cdata["Select"]:
                if item != "":
                    add_text(item, color=c_h2, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Choice.{item}")
                    add_text(g.get_Fighting_Style(item), color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Choice.{item}.Desc")

        if "Second Wind" in data:
            ability = "Second Wind"
            tag = ability.replace(" ", "_")
            Second_Wind = f"(bonus) regain 1d10+{q.db.Core.L} HP"
            cdata = data["Second Wind"]
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Second Wind", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Header")
                    add_checkbox(default_value=cdata["Use"][0], enabled=True, callback=cbh, user_data=["Class Use", "Second Wind", 0], tag=f"checkbox.fClass.Fighter.{tag}.Use.0")
                add_text(Second_Wind, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Desc")
                
        if "Action Surge" in data:
            ability = "Action Surge"
            tag = ability.replace(" ", "_")
            Action_Surge = "(free) take one additional action."
            cdata = data["Action Surge"]
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Action Surge", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Header")
                    for idx, value in enumerate(cdata["Use"]):
                        add_checkbox(default_value=value, enabled=True, callback=cbh, user_data=["Class Use", "Action Surge", idx], tag=f"checkbox.fClass.Fighter.{tag}.Use.{idx}")
                add_text(Action_Surge, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Desc")

        if "Extra Attack" in data:
            ability = "Extra Attack"
            tag = ability.replace(" ", "_")
            extra_attack_num = [0,0,0,0,0,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4][q.db.Core.L]
            Extra_Attack = f"On Attack action, attack {extra_attack_num} times"
            with group(horizontal=True):
                add_text("Extra Attack", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Header")
                add_text(Extra_Attack, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Desc")

        if "Indomitable" in data:
            ability = "Indomitable"
            tag = ability.replace(" ", "_")
            Indomitable = "You can reroll a saving throw that you fail. If you do so, you must use the new roll"
            cdata = data["Indomitable"]
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Indomitable", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Header")
                    for idx, value in enumerate(cdata["Use"]):
                        add_checkbox(default_value=value, enabled=True, callback=cbh, user_data=["Class Use", "Indomitable", idx], tag=f"checkbox.fClass.Fighter.{tag}.Use.{idx}")
                add_text(Indomitable, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.{tag}.Desc")
    if q.db.Core.SC: globals()[f"ui_upd_Class_{q.db.Core.C}_{q.db.Core.SC}"]()

def ui_upd_Class_Fighter_Champion():
    data = q.db.Class["Abil"]
    with group(parent="cw.fClass.Main"):
        if "Improved Critical" in data:
            ability = "Improved Critical"
            tag = ability.replace(" ", "_")
            Improved_Critical = "weapon attacks crit on 18-20." 
            add_text("Improved Critical", color=c_h1, tag=f"text.fClass.Fighter.Champion.{tag}.Header")
            add_text(Improved_Critical, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.Champion.{tag}.Desc")

        if "Superior Critical" in data:
            ability = "Superior Critical"
            tag = ability.replace(" ", "_")
            Superior_Critical = "weapon attacks crit on 19-20."
            add_text("Superior Critical", color=c_h1, tag=f"text.fClass.Fighter.Champion.{tag}.Header")
            add_text(Superior_Critical, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.Champion.{tag}.Desc")
            
        if "Remarkable Athlete" in data:
            ability = "Remarkable Athlete"
            tag = ability.replace(" ", "_")
            Remarkable_Athlete = f"add +{math.ceil(q.db.Core.PB/2)} to any non proficient Str/Dex/Con check. On running long jump, increase distance by {q.db.Atr["STR"]["Mod"]} ft."
            add_text("Remarkable Athlete", color=c_h1, tag=f"text.fClass.Fighter.Champion.{tag}.Header")
            add_text(Remarkable_Athlete, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.Champion.{tag}.Desc")

        if "Survivor" in data:
            ability = "Survivor"
            tag = ability.replace(" ", "_")
            Survivor = f"At the start of your turn, regain {5 + q.db.Atr['CON']['Mod']} hp if at less then half HP and above 0 HP"
            add_text("Survivor", color=c_h1, tag=f"text.fClass.Fighter.Champion.{tag}.Header")
            add_text(Survivor, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.Champion.{tag}.Desc")

def ui_upd_Class_Fighter_BattleMaster():
    data = q.db.Class["Abil"]
    with group(parent="cw.fClass.Main"):
        if "Combat Superiority" in data:
            ability = "Combat Superiority"
            tag = ability.replace(" ", "_")
            die = [0,0,0,8,8,8,8,8,8,8,10,10,10,10,10,10,10,10,12,12,12][q.db.Core.L]
            cdata = data["Combat Superiority"]
            t1_header = f"text.fClass.Fighter.BattleMaster.{tag}.Header"
            tag_popup = f"popup.fClass.Fighter.BattleMaster.{tag}.Select"
            with group(horizontal=True):
                add_text(f"Combat Superiority (d{die})", color=c_h1, wrap=size.gwrap, tag=t1_header)
                item_delete(tag_popup)
                with popup(t1_header, mousebutton=mvMouseButton_Left, tag=tag_popup):
                    for idx, value in enumerate(cdata["Select"]): 
                        add_combo(items=g.list_Maneuvers, default_value=value, width=80, no_arrow_button=True, callback=cbh, user_data=["Class Select", "Combat Superiority", idx], tag=f"combo.fClass.Fighter.BattleMaster.{tag}.Choice.{idx}")
                for idx, value in enumerate(cdata["Use"]):
                    add_checkbox(default_value=value, enabled=True, callback=cbh, user_data=["Class Use", "Combat Superiority", idx], tag=f"checkbox.fClass.Fighter.BattleMaster.{tag}.Use.{idx}")
            for item in cdata["Select"]:
                if item:
                    item_tag = item.replace(" ", "_")
                    add_text(item, color=c_h2, wrap=size.gwrap, tag=f"text.fClass.Fighter.BattleMaster.{tag}.Maneuver.{item_tag}")
                    item_delete(f"tooltip.fClass.Fighter.BattleMaster.{tag}.Maneuver.{item_tag}")
                    with tooltip(f"text.fClass.Fighter.BattleMaster.{tag}.Maneuver.{item_tag}", tag=f"tooltip.fClass.Fighter.BattleMaster.{tag}.Maneuver.{item_tag}"):
                        add_text(g.dict_Maneuver_map[item], color=c_text, wrap=size.gwrap)
        
        if "Student of War" in data:
            ability = "Student of War"
            tag = ability.replace(" ", "_")
            cdata = data["Student of War"]
            t1_header = f"text.fClass.Fighter.BattleMaster.{tag}.Header"
            tag_popup = f"popup.fClass.Fighter.BattleMaster.{tag}.Select"
            add_text("Student of War", color=c_h1, wrap=size.gwrap, tag=t1_header)
            item_delete(tag_popup)
            with popup(t1_header, mousebutton=mvMouseButton_Left, tag=tag_popup):
                add_combo(items=g.list_Student_of_War_Profs, default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=cbh, user_data=["Class Select", "Student of War", 0], tag=f"combo.fClass.Fighter.BattleMaster.{tag}.Choice.0")
        
        if "Relentless" in data:
            ability = "Relentless"
            tag = ability.replace(" ", "_")
            Relentless = "When you roll initiative with 0 SD; gain 1 SD."
            with group(horizontal=True):
                add_text("Relentless", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.BattleMaster.{tag}.Header")
                add_text(Relentless, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.BattleMaster.{tag}.Desc")

def ui_upd_Class_Fighter_EldrichKnight():
    data = q.db.Class["Abil"]
    with group(parent="cw.fClass.Main"):
        if "Weapon Bond" in data:
            ability = "Weapon Bond"
            tag = ability.replace(" ", "_")
            Weapon_Bond_1 = "Learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond."
            Weapon_Bond_2 = "Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand."
            Weapon_Bond_3 = "You can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two."
            t1_header = f"text.fClass.Fighter.EldrichKnight.{tag}.Header"
            tag_tooltip = f"tooltip.fClass.Fighter.EldrichKnight.{tag}.Detail"
            add_text("Weapon Bond", color=c_h1, wrap=size.gwrap, tag=t1_header)
            item_delete(tag_tooltip)
            with tooltip(t1_header, tag=tag_tooltip):
                add_text(Weapon_Bond_1, color=c_text, wrap=size.gwrap)
                add_text(Weapon_Bond_2, color=c_text, wrap=size.gwrap)
                add_text(Weapon_Bond_3, color=c_text, wrap=size.gwrap)
                        
        if "War Magic" in data:
            ability = "War Magic"
            tag = ability.replace(" ", "_")
            War_Magic = "(action-cantrip) gain (bonus) make one weapon attack."
            add_text("War Magic", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.EldrichKnight.{tag}.Header")
            add_text(War_Magic, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.EldrichKnight.{tag}.Desc")
        
        if "Improved War Magic" in data:
            ability = "Improved War Magic"
            tag = ability.replace(" ", "_")
            Improved_War_Magic = "(action-spell) gain (bonus) make one weapon attack."
            add_text("Improved War Magic", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.EldrichKnight.{tag}.Header")
            add_text(Improved_War_Magic, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.EldrichKnight.{tag}.Desc")
        
        if "Eldrich Strike" in data:
            ability = "Eldrich Strike"
            tag = ability.replace(" ", "_")
            Eldrich_Strike = "When you hit a creature with a weapon attack, that creature has disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn."
            add_text("Eldrich Strike", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.EldrichKnight.{tag}.Header")
            add_text(Eldrich_Strike, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.EldrichKnight.{tag}.Desc")
        
        if "Arcane Charge" in data:
            ability = "Arcane Charge"
            tag = ability.replace(" ", "_")
            Arcane_Charge = "(Action Surge) Teleport up to 30 feet to an unoccupied space you can see, teleport before or after extra action"
            add_text("Arcane Charge", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.EldrichKnight.{tag}.Header")
            add_text(Arcane_Charge, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.EldrichKnight.{tag}.Desc")

def ui_upd_Class_Fighter_Samurai():
    data = q.db.Class["Abil"]
    with group(parent="cw.fClass.Main"):
        if "Bonus Proficiency" in data:
            ability = "Bonus Proficiency"
            tag = ability.replace(" ", "_")
            cdata = data[ability]
            t1_header = f"text.fClass.Fighter.Samurai.{tag}.Header"
            tag_popup = f"popup.fClass.Fighter.Samurai.{tag}.Select"
            add_text(ability, color=c_h1, wrap=size.gwrap, tag=t1_header)
            item_delete(tag_popup)
            with popup(t1_header, mousebutton=mvMouseButton_Left, tag=tag_popup):
                add_combo(items=g.list_Fighter_Samuri_Bonus_Proficiency, default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=cbh, user_data=["Class Select", ability, 0], tag=f"combo.fClass.Fighter.Samurai.{tag}.Choice.0")
        
        if "Fighting Spirit" in data:
            ability = "Fighting Spirit"
            tag = ability.replace(" ", "_")
            cdata = data[ability]
            Fighting_Spirit = "(Bonus Action) Advantage on weapon attacks and gain 5 temp HP until end of turn."
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Fighting Spirit", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Header")
                    for idx, value in enumerate(cdata["Use"]):
                        add_checkbox(default_value=value, enabled=True, callback=cbh, user_data=["Class Use", "Fighting Spirit", idx], tag=f"checkbox.fClass.Fighter.Samurai.{tag}.Use.{idx}")
                add_text(Fighting_Spirit, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Desc")
                
        if "Elegant Courtier" in data:
            ability = "Elegant Courtier"
            tag = ability.replace(" ", "_")
            Elegant_Courtier = f"Persuasion checks gain {q.db.Atr['WIS']['Mod']:+d}"
            with group(horizontal=True):
                add_text("Elegant Courtier", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Header")
                add_text(Elegant_Courtier, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Desc")
                
        if "Tireless Spirit" in data:
            ability = "Tireless Spirit"
            tag = ability.replace(" ", "_")
            Tireless_Spirit = "When you roll initiative and have no uses of Fighting Spirit remaining, regain one use."
            with group(horizontal=True):
                add_text("Tireless Spirit", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Header")
                add_text(Tireless_Spirit, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Desc")
        
        if "Rapid Strike" in data:
            ability = "Rapid Strike"
            tag = ability.replace(" ", "_")
            Rapid_Strike = "On Attack with advantage, you may remove advantage to gain +1 attack, 1/turn."
            with group(horizontal=True):
                add_text("Rapid Strike", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Header")
                add_text(Rapid_Strike, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Desc")
                
        if "Strength before Death" in data:
            ability = "Strength before Death"
            tag = ability.replace(" ", "_")
            cdata = data[ability]
            Strength_before_Death = "When reduced to 0 HP, take a full turn before falling unconsciouq.pc."
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Strength before Death", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Header")
                    add_checkbox(default_value=cdata["Use"][0], enabled=True, callback=cbh, user_data=["Class Use", "Strength before Death", 0], tag=f"checkbox.fClass.Fighter.Samurai.{tag}.Use.0")
                add_text(Strength_before_Death, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Fighter.Samurai.{tag}.Desc")
                
def ui_upd_Class_Wizard():
    data = q.db.Class["Abil"]
    with group(parent="cw.fClass.Main"):
        if "Spellcasting" in data:
            ability = "Spellcasting"
            tag = ability.replace(" ", "_")
            Spellcasting_1 = "Must be spell level you can prepare, Costs 50 gp + 2 hours per spell level"
            Spellcasting_2 = "Too backup own spellbook, Costs 10 gp + 1 hour per spell level"
            t1_header = f"text.fClass.Wizard.{tag}.Header"
            tag_tooltip = f"tooltip.fClass.Wizard.{tag}.Detail"
            add_text("Spellcasting", color=c_h1, wrap=size.gwrap, tag=t1_header)
            item_delete(tag_tooltip)
            with tooltip(t1_header, tag=tag_tooltip):
                add_text("Copying external spells", color=c_h1, wrap=size.gwrap)
                add_text(Spellcasting_1, color=c_text, wrap=size.gwrap)
                add_text("Copying internal spells", color=c_h1, wrap=size.gwrap)
                add_text(Spellcasting_2, color=c_text, wrap=size.gwrap)
                
        if "Arcane Recovery" in data:
            ability = "Arcane Recovery"
            tag = ability.replace(" ", "_")
            cdata = data["Arcane Recovery"]
            Arcane_Recovery = f"Regain Spell slots with a combined level of {math.ceil(q.db.Core.L/2)}, None highter then 6th level"
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Arcane Recovery", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.{tag}.Header")
                    for idx, value in enumerate(cdata["Use"]):
                        add_checkbox(default_value=value, enabled=True, callback=cbh, user_data=["Class Use", "Arcane Recovery", idx], tag=f"checkbox.fClass.Wizard.{tag}.Use.{idx}")
                add_text(Arcane_Recovery, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.{tag}.Desc")

        if "Spell Mastery" in data:
            ability = "Spell Mastery"
            tag = ability.replace(" ", "_")
            cdata = data["Spell Mastery"]
            t1_header = f"text.fClass.Wizard.{tag}.Header"
            tag_popup = f"popup.fClass.Wizard.{tag}.Select"
            add_text("Spell Mastery", color=c_h1, wrap=size.gwrap, tag=t1_header)
            item_delete(tag_popup)
            with popup(t1_header, mousebutton=mvMouseButton_Left, tag=tag_popup):
                add_combo(items=q.db.Spell["Book"][1], default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=cbh, user_data=["Class Select", "Spell Mastery", 0], tag=f"combo.fClass.Wizard.{tag}.Choice.0")
                add_combo(items=q.db.Spell["Book"][2], default_value=cdata["Select"][1], width=80, no_arrow_button=True, callback=cbh, user_data=["Class Select", "Spell Mastery", 1], tag=f"combo.fClass.Wizard.{tag}.Choice.1")
            for idx, spell in enumerate(cdata["Select"]):
                if spell != "":
                    spell_tag = spell.replace(" ", "_")
                    with group(horizontal=True):
                        add_text(spell, color=c_h2, tag=f"text.fClass.Wizard.{tag}.Spell.{spell_tag}")
                        add_checkbox(default_value=cdata["Use"][idx], enabled=True, callback=cbh, user_data=["Class Use", "Spell Mastery", idx], tag=f"checkbox.fClass.Wizard.{tag}.Use.{idx}")
                        item_delete(f"tooltip.fClass.Wizard.{tag}.Spell.{spell_tag}")
                        with tooltip(f"text.fClass.Wizard.{tag}.Spell.{spell_tag}", tag=f"tooltip.fClass.Wizard.{tag}.Spell.{spell_tag}"):
                            spell_detail(spell)
                            
        if "Signature Spells" in data:
            ability = "Signature Spells"
            tag = ability.replace(" ", "_")
            cdata = data["Signature Spells"]
            t1_header = f"text.fClass.Wizard.{tag}.Header"
            tag_popup = f"popup.fClass.Wizard.{tag}.Select"
            add_text("Signature Spells", color=c_h1, wrap=size.gwrap, tag=t1_header)
            item_delete(tag_popup)
            with popup(t1_header, mousebutton=mvMouseButton_Left, tag=tag_popup):
                add_combo(items=q.db.Spell["Book"][3], default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=cbh, user_data=["Class Select", "Signature Spells", 0], tag=f"combo.fClass.Wizard.{tag}.Choice.0")
                add_combo(items=q.db.Spell["Book"][3], default_value=cdata["Select"][1], width=80, no_arrow_button=True, callback=cbh, user_data=["Class Select", "Signature Spells", 1], tag=f"combo.fClass.Wizard.{tag}.Choice.1")
            for idx, spell in enumerate(cdata["Select"]):
                if spell != "":
                    spell_tag = spell.replace(" ", "_")
                    with group(horizontal=True):
                        add_text(spell, color=c_h2, tag=f"text.fClass.Wizard.{tag}.Spell.{spell_tag}")
                        add_checkbox(default_value=cdata["Use"][idx], enabled=True, callback=cbh, user_data=["Class Use", "Signature Spells", idx], tag=f"checkbox.fClass.Wizard.{tag}.Use.{idx}")
                        item_delete(f"tooltip.fClass.Wizard.{tag}.Spell.{spell_tag}")
                        with tooltip(f"text.fClass.Wizard.{tag}.Spell.{spell_tag}", tag=f"tooltip.fClass.Wizard.{tag}.Spell.{spell_tag}"):
                            spell_detail(spell)
        if q.db.Core.SC: globals()[f"ui_upd_Class_{q.db.Core.C}_{q.db.Core.SC}"]()

def ui_upd_Class_Wizard_Abjuration():
    data = q.db.Class["Abil"]
    with group(parent="cw.fClass.Main"):
        if "Abjuration Savant" in data:
            ability = "Abjuration Savant"
            tag = ability.replace(" ", "_")
            Abjuration_Savant = "Abjuration spells cost 25gp and 1 hour per spell level."
            add_text("Abjuration Savant", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Header")
            add_text(Abjuration_Savant, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Desc")
            
        if "Arcane Ward" in data:
            ability = "Arcane Ward"
            tag = ability.replace(" ", "_")
            Arcane_Ward = "On casting a 1st-level+ Abjuration spell, create a magical ward that lasts until a long rest. It can regain HP equal to twice the spell level on subsequent Abjuration spell castq.pc."
            cdata = data["Arcane Ward"]
            with group(horizontal=True):
                add_text("Arcane Ward", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Header")
                add_checkbox(default_value=cdata["Use"][0], enabled=True, callback=cbh, user_data=["Class Use", "Arcane Ward", 0], tag=f"checkbox.fClass.Wizard.Abjuration.{tag}.Use.0")
                add_button(label="Ward HP", enabled=False)
                add_button(label=f"{cdata["HP"]["Current"]} / {cdata["HP"]["Max"]}", enabled=False, tag=f"button.fClass.Wizard.Abjuration.{tag}.HP")
                add_button(label="-", user_data = ["Arcane Ward", -1], callback=cbh)
                add_button(label="+", user_data = ["Arcane Ward", 1], callback=cbh)
            add_text(Arcane_Ward, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Desc")
        
        if "Projected Ward" in data:
            ability = "Projected Ward"
            tag = ability.replace(" ", "_")
            Projected_Ward = "(reaction) When a creature within 30 ft is hit, use your Arcane Ward to absorb the damage."
            add_text("Projected Ward", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Header")
            add_text(Projected_Ward, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Desc")
            
        if "Improved Abjuration" in data:
            ability = "Improved Abjuration"
            tag = ability.replace(" ", "_")
            Improved_Abjuration = f"When an Abjuration spell requires you to make an ability check, add your proficiency bonus ({q.db.Core.PB}) to that check."
            add_text("Improved Abjuration", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Header")
            add_text(Improved_Abjuration, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Desc")
            
        if "Spell Resistance" in data:
            ability = "Spell Resistance"
            tag = ability.replace(" ", "_")
            Spell_Resistance = "Gain advantage on saving throws against spells and resistance to spell damage."
            add_text("Spell Resistance", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Header")
            add_text(Spell_Resistance, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Abjuration.{tag}.Desc")

def ui_upd_Class_Wizard_Conjuration():
    data = q.db.Class["Abil"]
    with group(parent="cw.fClass.Main"):
        if "Conjuration Savant" in data:
            ability = "Conjuration Savant"
            tag = ability.replace(" ", "_")
            Conjuration_Savant = "Conjuration spells cost 25gp and 1 hour per spell level."
            add_text("Conjuration Savant", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Header")
            add_text(Conjuration_Savant, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Desc")
            
        if "Minor Conjuration" in data:
            ability = "Minor Conjuration"
            tag = ability.replace(" ", "_")
            Minor_Conjuration = "(action) Conjure a non-magical item (up to 3ft, 10 lbs). It lasts for 1 hour or until it takes damage."
            add_text("Minor Conjuration", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Header")
            add_text(Minor_Conjuration, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Desc")
            
        if "Benign Transportation" in data:
            ability = "Benign Transportation"
            tag = ability.replace(" ", "_")
            Benign_Transportation = "(action) Teleport up to 30ft or swap places with a willing creature. Usable again after a long rest or casting a Level 1+ conjuration spell."
            add_text("Benign Transportation", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Header")
            add_text(Benign_Transportation, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Desc")
            
        if "Focused Conjuration" in data:
            ability = "Focused Conjuration"
            tag = ability.replace(" ", "_")
            Focused_Conjuration = "Your concentration on conjuration spells can't be broken as a result of taking damage."
            add_text("Focused Conjuration", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Header")
            add_text(Focused_Conjuration, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Desc")
            
        if "Durable Summons" in data:
            ability = "Durable Summons"
            tag = ability.replace(" ", "_")
            Durable_Summons = "Any creature you summon or create with a conjuration spell has 30 temporary hit pointq.pc."
            add_text("Durable Summons", color=c_h1, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Header")
            add_text(Durable_Summons, color=c_text, wrap=size.gwrap, tag=f"text.fClass.Wizard.Conjuration.{tag}.Desc")

# #ANCHOR - Inventory

def ui_upd_INVE():
    ui_upd_INVE_Equip()
    ui_upd_INVE_Backpack()


def ui_upd_INVE_Backpack():
    item_clear("cw.INVE.Backpack")
    with group(parent="cw.INVE.Backpack"):
        with table(header_row=True, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True, resizable=True):
            add_table_column(label="Item", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Slot", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="QTY", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Weight", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Cost", width_stretch=True, init_width_or_weight=0)
            
            for item in g.q.db.Inventory.Backpack:
                cdata = q.w.Item(item)
                qty = q.db.Inventory.Backpack[item][1]
                weight = int(w) if (w := round(float(cdata.Weight)*qty, 2)) == int(w) else w
                cost = int(c) if (c := round(float(cdata.Cost)*qty, 2)) == int(c) else c
                with table_row():
                    with table_cell():
                        add_text(g.iName(item), tag=f"text.BP.Label.{item}")
                    with table_cell():
                        add_text(cdata.Slot, tag=f"text.BP.Slot.{item}")
                    with table_cell():
                        with group(horizontal=True):
                            add_text(qty, tag=f"text.BP.qty.{item}")
                            add_button(label="<", small=True, user_data=["Backpack Mod Item", item, -1], callback=cbh)
                            add_button(label=">", small=True, user_data=["Backpack Mod Item", item, 1], callback=cbh)
                            add_button(label="X", small=True, user_data=["Backpack Mod Item", item, "Clear"], callback=cbh)
                    with table_cell():
                        add_text(weight, tag=f"text.BP.weight.{item}")
                    with table_cell():
                        add_text(cost, tag=f"text.BP.Cost.{item}")

                item_delete(f"tooltip.BP.{item}")
                with tooltip(f"text.BP.Label.{item}", tag=f"tooltip.BP.{item}"):
                    disp_item_detail(item)


def ensure_Backpack():
    for item in cdata:
        cdata = q.w.Item(item)
        qty = q.db.Inventory.Backpack[item][1]
        weight = 0
        cost = 0
        
        set_value(f"text.BP.Slot.{item}", cdata.Slot)
        set_value(f"text.BP.qty.{item}", qty)
        set_value(f"text.BP.weight.{item}", weight)
        set_value(f"text.BP.Cost.{item}", cost)

def ui_upd_INVE_Equip():
    backpack = set(q.db.Inventory.Backpack)
    two_handed = set(q.w.prop("Two-handed"))
    cEquip = q.db.Inventory.Equip
    main_hand_item = cEquip["Hand_1"]

    slots = [
        ("Face", q.w.slot("Face"), "combo.INVE.Equip.Face"),
        ("Throat", q.w.slot("Throat"), "combo.INVE.Equip.Throat"),
        ("Body", q.w.slot("Body"), "combo.INVE.Equip.Body"),
        ("Hands", q.w.slot("Hands"), "combo.INVE.Equip.Hands"),
        ("Waist", q.w.slot("Waist"), "combo.INVE.Equip.Waist"),
        ("Feet", q.w.slot("Feet"), "combo.INVE.Equip.Feet"),
        ("Armor", q.w.slot("Armor"), "combo.INVE.Equip.Armor"),
        ("Hand_1", q.w.slot("Weapon"), "combo.INVE.Equip.Hand_1"),
        ("Hand_2", q.w.list_off_hand, "combo.INVE.Equip.Hand_2"),
        ("Ring_1", q.w.slot("Ring"), "combo.INVE.Equip.Ring_1"),
        ("Ring_2", q.w.slot("Ring"), "combo.INVE.Equip.Ring_2"),
    ]

    for slot_name, source, tag in slots:
        items = [g.iName(i) for i in source if i in backpack]
        if slot_name == "Hand_2":
            if main_hand_item in two_handed: default_value = "Weapon Grip"
            elif g.weapon_versatile(): default_value = "Verse Grip"
            else: default_value = g.iName(cEquip["Hand_2"]) if cEquip["Hand_2"] in backpack else ""
        else:
            equipped = cEquip.get(slot_name, None)
            default_value = g.iName(equipped) if equipped in backpack else ""
        configure_item(tag, items=items, default_value=default_value)



def create_bazaar_button(item, category_type, parent):
    button_tag = f"button.Bazaar.add.{item}"
    tooltip_tag = f"tooltip.Bazaar.detail.{item}"
    
    add_button(label=g.isName(item), width=size.w_item, user_data=["Bazaar Add Item", category_type, item], callback=cbh, tag=button_tag, parent=parent)
    
    with tooltip(button_tag, tag=tooltip_tag):
        disp_item_detail(item)

def ui_upd_INVE_Bazaar():
    dict_struct = {
        "Weapon": [("Simple", "Melee"), ("Simple", "Ranged"), ("Martial", "Melee"), ("Martial", "Ranged")],
        "Armor": ["Light", "Medium", "Heavy"]
    }

    for equipment_type, categories in dict_struct.items():
        for rank in range(5):
            rarity = g.item_rarity(rank)
            parent_container = f"cw.Bazaar.{equipment_type}.{rarity}"

            if not does_item_exist(parent_container):continue

            # --- 1. Get Target Items ---
            target_set = set()
            is_weapon_type = isinstance(categories[0], tuple)
            for category_info in categories:
                if is_weapon_type:
                    tag1, tag2 = category_info
                    items = q.w.mcategory(rank, tag1, tag2)
                else:
                    items = q.w.mcategory(rank, category_info)
                target_set.update(items)

            # --- 2. Get Current Items ---
            current_items = set()
            if does_item_exist(parent_container):
                container_children = get_item_children(parent_container, 1)
                for group_id in container_children:
                    if get_item_info(group_id)['type'] == 'Group':
                        row_children = get_item_children(group_id, 1)
                        for button_id in row_children:
                            button_alias = get_item_alias(button_id)
                            if button_alias and button_alias.startswith("button.Bazaar.add."):
                                item_id = button_alias.replace("button.Bazaar.add.", "")
                                current_items.add(item_id)
            
            # --- 3. Compare and Rebuild if Necessary ---
            if target_set != current_items:
                item_clear(parent_container)

                with group(parent=parent_container):
                    for category_info in categories:
                        if is_weapon_type:
                            tag1, tag2 = category_info
                            label = f"{tag1} {tag2}"
                            items = q.w.mcategory(rank, tag1, tag2)
                            items.sort() # Sort the list alphabetically
                        else:
                            label = tag1 = category_info
                            items = q.w.mcategory(rank, tag1)
                            items.sort()
                        add_separator(label=label if rank == 0 else f"{label} (+{rank})")
                        for i in range(0, len(items), 4):
                            with group(horizontal=True):
                                horizontal_group_id = last_item()
                                for item in items[i:i+4]:
                                    create_bazaar_button(item, equipment_type, parent=horizontal_group_id)

def disp_item_detail(item):
    data=q.w.Item(item)
    if data.Slot == "Weapon": weapon_detail(data)
    if data.Slot == "Armor": armor_detail(data)


def weapon_detail(data):
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
        for prop in data.Prop: add_text(f"{prop}", color=c_text)
        add_text("Rarity", color=c_h1)
        add_text(g.item_rarity(data.Tier), color=c_rarity[f"{g.item_rarity(data.Tier)}"])
        add_text("Weight", color=c_h1)
        add_text(data.Weight, color=c_text)
        add_text("Cost", color=c_h1)
        add_text(data.Cost, color=c_h9)


def armor_detail(data):
    pass



























# def resize_window():
#     print("resizing_window")


