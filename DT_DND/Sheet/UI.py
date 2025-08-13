#ui_upd.py
from dearpygui.dearpygui import *
import q
from Sheet.getset import g
from UI.UI_imports import gen_abil, tag, size
from access_data.color_reference import *
import math as math

from colorist import *





#ANCHOR - Backend Import


        
#ANCHOR - Call Back Handler

    
    

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
                add_child_window(height=h-28, border=True, no_scrollbar=True, tag=tag.equip.window("equip"))
            with tab(label="Backpack"):
                add_child_window(height=h-80, border=True, no_scrollbar=True, tag=tag.backpack.window())
                add_child_window(height=h-294, border=True, tag=tag.backpack.window("totals"))
            with tab(label="Bazaar"):
                add_child_window(height=h-26, border=True, no_scrollbar=True,  tag=tag.bazaar.window("bazaar"))

def init_window_inventory_backpack():
    parent = tag.backpack.window()
    item_clear(parent)
    with group(parent=parent):
        with table(header_row=True, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True, resizable=True, tag=tag.backpack.table()):
            add_table_column(label="Item", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Slot", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="QTY", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Weight", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Cost", width_stretch=True, init_width_or_weight=0)
            

def init_window_inventory_bazaar():
    with group(parent=tag.inve.window("bazaar")):
        with tab_bar():
            for equipment_type in g.list_equip_type:
                with tab(label=equipment_type):
                    with tab_bar():
                        for rarity in range(5):
                            rank = g.item_rarity(rarity)
                            with tab(label=rank):
                                add_child_window(height=size.h_inventory - 85, border=True, no_scrollbar=True, tag=tag.bazaar.window(equipment_type, rank))
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

class ui_upd_Feat:
    def __init__(self):
        self.parent = tag.mfeature.main()

    def standard(self, name, descriptions):
        a, t = gen_abil(name, 1)
        t_header = tag.mfeature.header(t)
        desc_tags = [tag.mfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=size.gwrap, tag=desc_tags[i])

    def standard_popup(self, name, descriptions, num_choices=1):
        a, t = gen_abil(name, 1)
        t_header = tag.mfeature.header(t)
        desc_tags = [tag.mfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]
        t_popup = tag.mfeature.popup(t)
        
        item_delete(t_popup)

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=size.gwrap, tag=desc_tags[i])

        with popup(t_header, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=t_popup):
            with group(horizontal=False):
                for i in range(num_choices):
                    t_select = tag.mfeature.select(t, i)
                    add_combo(items=g.dict_Feat_Lists[a], default_value=q.db.Milestone.Data[a]["Select"][i], width=100, no_arrow_button=True, user_data=["Milestone Feat Choice", a, i], callback=cbh, tag=t_select)
                    add_button(label="X", user_data=["Milestone Feat Choice Clear", a, i], callback=cbh)

    def standard_toggle(self, name, descriptions):
        a, t = gen_abil(name, 1)
        t_header = tag.mfeature.header(t)
        desc_tags = [tag.mfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]
        use = q.db.Milestone["Data"][a]["Use"]

        with group(parent=self.parent):
            with group(horizontal=True):
                add_text(a, color=c_h1, tag=t_header)
                for idx, val in enumerate(use):
                    add_checkbox(default_value=val, enabled=True, user_data=["Milestone Feat Use", a, idx], callback=cbh, tag=f"checkbox.fMilestone.{t}.Use.{idx}")
            
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=size.gwrap, tag=desc_tags[i])


    def Actor(self):
        descriptions = [
            "Gain advantage on Deception and Performance checks when trying to pass yourself off as a different person.",
            f"You can mimic the speech of another person or the sounds made by other creature. You must have heard the person speaking, or heard the creature make the sound, for at least 1 minute. A successful Wisdom Insight check contested by your {q.db.Skill['Deception']['Mod']:+d} Deception check allows a listener to determine that the effect is faked."
        ]
        self.standard("Actor", descriptions)

    def Alert(self):
        descriptions = [
            "You can't be surprised while you are conscious.",
            "Other creatures don't gain advantage on attack rolls against you as a result of being unseen by you."
        ]
        self.standard("Alert", descriptions)

    def Athlete(self):
        descriptions = [
            "When you are prone, standing up uses only 5 feet of your movement.",
            "Climbing doesn't cost you extra movement.",
            "You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than 10 feet."
        ]
        self.standard_popup("Athlete", descriptions)

    def Charger(self):
        descriptions = [
            "When you use your action to Dash, you can use a bonus action to make one melee weapon attack or shove a creature, and if you moved at least 10 feet in a straight line immediately before taking this bonus action, you gain a +5 bonus to the attack's damage roll or push the target with extra force."
        ]
        self.standard("Charger", descriptions)

    def Crossbow_Expert(self):
        descriptions = [
            "You ignore the loading quality of crossbows with which you are proficient.",
            "Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack roll.",
            "When you use the Attack action and attack with a one-handed weapon, you can use a bonus action to fire a hand crossbow you are holding."
        ]
        self.standard("Crossbow Expert", descriptions)

    def Defensive_Duelist(self):
        descriptions = [
            "When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can use your reaction to add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you."
        ]
        self.standard("Defensive Duelist", descriptions)

    def Dual_Wielder(self):
        descriptions = [
            "You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand.",
            "You can use two-weapon fighting even when the one-handed melee weapons you are wielding aren't light.",
            "You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one."
        ]
        self.standard("Dual Wielder", descriptions)

    def Dungeon_Delver(self):
        descriptions = [
            "You have advantage on Wisdom (Perception) and Intelligence (Investigation) checks made to detect the presence of secret doors.",
            "You have advantage on saving throws made to avoid or resist traps.",
            "You take no damage from traps that would normally deal half damage on a successful save."
        ]
        self.standard("Dungeon Delver", descriptions)

    def Durable(self):
        descriptions = [
            f"When you roll a Hit Die to regain hit points, the minimum number of hit points you regain from the roll equals {q.db.Atr['CON']['Mod'] * 2}."
        ]
        self.standard("Durable", descriptions)

    def Elemental_Adept(self):
        v = q.db.Milestone.Data["Elemental_Adept"]["Select"][0]
        
        descriptions = [
            f"Spells you cast ignore resistance to {v} damage.",
            f"When you roll damage for a spell you cast that deals {v} damage, you treat any 1 on a damage die as a 2."
        ]
        self.standard_popup("Elemental Adept", descriptions)

    def Grappler(self):
        descriptions = [
            "You have advantage on attack rolls against a creature you are grappling.",
            "You can use your action to try to pin a creature grappled by you. To do so, make another grapple check. If you succeed, you and the creature are both restrained until the grapple ends."
        ]
        self.standard("Grappler", descriptions)

    def Great_Weapon_Master(self):
        descriptions = [
            "On your turn, when you score a critical hit with a melee weapon or reduce a creature to 0 hit points with one, you can make one melee weapon attack as a bonus action.",
            "Before you make a melee attack with a heavy weapon you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage."
        ]
        self.standard("Great Weapon Master", descriptions)

    def Healer(self):
        descriptions = [
            "When you use a healer's kit to stabilize a dying creature, that creature also regains 1 hit point.",
            "As an action, you can spend one use of a healer's kit to tend to a creature and restore 1d6 + 4 hit points to it, plus additional hit points equal to the creature's maximum number of Hit Dice. The creature can't regain hit points from this feat again until it finishes a short or long rest."
        ]
        self.standard("Healer", descriptions)

    def Heavily_Armored(self):
        self.standard_popup("Heavily Armored", [])

    def Heavy_Armor_Master(self):
        descriptions = [
            "Prerequisite: Proficiency with heavy armor",
            "While you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from nonmagical attacks is reduced by 3."
        ]
        self.standard("Heavy Armor Master", descriptions)

    def Inspiring_Leader(self):
        descriptions = [
            f"You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, choose up to six friendly creatures (which can include yourself) within 30 feet of you who can see or hear you and who can understand you. Each creature gains temporary hit points equal to your level + {q.db.Atr['CHA']['Mod']}."
        ]
        self.standard("Inspiring Leader", descriptions)

    def Keen_Mind(self):
        descriptions = [
            "You always know which way is north.",
            "You always know the number of hours left before the next sunrise or sunset.",
            "You can accurately recall anything you have seen or heard within the past month."
        ]
        self.standard("Keen Mind", descriptions)

    def Lightly_Armored(self):
        self.standard_popup("Lightly Armored", [])

    def Lucky(self):
        descriptions = [
            "You have 3 luck points. Whenever you make an attack roll, an ability check, or a saving throw, you can spend one luck point to roll an additional d20. You can choose to spend one of your luck points after you roll the die, but before the outcome is determined. You choose which of the d20s is used for the attack roll, ability check, or saving throw.",
            "You can also spend one luck point when an attack roll is made against you. Roll a d20, and then choose whether the attack uses the attacker's roll or yours. If more than one creature spends a luck point to influence the outcome of a roll, the points cancel each other out; no additional dice are rolled."
        ]
        self.standard_toggle("Lucky", descriptions)

    def Mage_Slayer(self):
        descriptions = [
            "When a creature within 5 feet of you casts a spell, you can use your reaction to make a melee weapon attack against that creature.",
            "When you damage a creature that is concentrating on a spell, that creature has disadvantage on the saving throw it makes to maintain its concentration.",
            "You have advantage on saving throws against spells cast by creatures within 5 feet of you."
        ]
        self.standard("Mage Slayer", descriptions)

    def Medium_Armor_Master(self):
        descriptions = [
            "Wearing medium armor doesn't impose disadvantage on your Dexterity (Stealth) checks.",
            "When you wear medium armor, you can add 3, rather than 2, to your AC if you have a Dexterity of 16 or higher."
        ]
        self.standard("Medium Armor Master", descriptions)

    def Mobile(self):
        descriptions = [
            "When you use the Dash action, difficult terrain doesn't cost you extra movement on that turn.",
            "When you make a melee attack against a creature, you don't provoke opportunity attacks from that creature for the rest of the turn, whether you hit or not."
        ]
        self.standard("Mobile", descriptions)

    def Moderately_Armored(self):
        self.standard_popup("Moderately Armored", [])

    def Mounted_Combatant(self):
        descriptions = [
            "You have advantage on melee attack rolls against any unmounted creature that is smaller than your mount.",
            "You can force an attack targeted at your mount to target you instead.",
            "If your mount is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails."
        ]
        self.standard("Mounted Combatant", descriptions)

    def Polearm_Master(self):
        descriptions = [
            "When you take the Attack action and attack with only a glaive, halberd, quarterstaff, or spear, you can use a bonus action to make a melee attack with the opposite end of the weapon. This attack uses the same ability modifier as the primary attack. The weapon's damage die for this attack is a d4, and it deals bludgeoning damage.",
            "While you are wielding a glaive, halberd, pike, quarterstaff, or spear, other creatures provoke an opportunity attack from you when they enter the reach you have with that weapon."
        ]
        self.standard("Polearm Master", descriptions)

    def Resilient(self):
        self.standard_popup("Resilient", [])

    def Savage_Attacker(self):
        descriptions = [
            "Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon's damage dice and use either total."
        ]
        self.standard("Savage Attacker", descriptions)

    def Sentinel(self):
        descriptions = [
            "When you hit a creature with an opportunity attack, the creature's speed becomes 0 for the rest of the turn.",
            "Creatures provoke opportunity attacks from you even if they take the Disengage action before leaving your reach.",
            "When a creature within 5 feet of you makes an attack against a target other than you (and that target doesn't have this feat), you can use your reaction to make a melee weapon attack against the attacking creature."
        ]
        self.standard("Sentinel", descriptions)

    def Sharpshooter(self):
        descriptions = [
            "Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls.",
            "Your ranged weapon attacks ignore half cover and three-quarters cover.",
            "Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage."
        ]
        self.standard("Sharpshooter", descriptions)

    def Shield_Master(self):
        descriptions = [
            "If you take the Attack action on your turn, you can use a bonus action to try to shove a creature within 5 feet of you with your shield.",
            "If you aren't incapacitated, you can add your shield's AC bonus to any Dexterity saving throw you make against a spell or other harmful effect that targets only you.",
            "If you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you can use your reaction to take no damage if you succeed on the saving throw, interposing your shield between yourself and the source of the effect."
        ]
        self.standard("Shield Master", descriptions)

    def Skulker(self):
        descriptions = [
            "You can try to hide when you are lightly obscured from the creature from which you are hiding.",
            "When you are hidden from a creature and miss it with a ranged weapon attack, making the attack doesn't reveal your position.",
            "Dim light doesn't impose disadvantage on your Wisdom (Perception) checks that rely on sight."
        ]
        self.standard("Skulker", descriptions)

    def Tavern_Brawler(self):
        descriptions = [
            "You are proficient with improvised weapons. Your unarmed strike uses a d4 for damage. When you hit a creature with an unarmed strike or an improvised weapon on your turn, you can use a bonus action to attempt to grapple the target."
        ]
        self.standard("Tavern Brawler", descriptions)

    def Tough(self):
        descriptions = [
            "Your hit point maximum increases by an amount equal to twice your level when you gain this feat. Whenever you gain a level thereafter, your hit point maximum increases by an additional 2 hit points."
        ]
        self.standard("Tough", descriptions)

    def War_Caster(self):
        descriptions = [
            "You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage.",
            "You can perform the somatic components of spells even when you have weapons or a shield in one or both hands.",
            "When a hostile creature's movement provokes an opportunity attack from you, you can use your reaction to cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of 1 action and must target only that creature."
        ]
        self.standard("War Caster", descriptions)

    def Weapon_Master(self):
        descriptions = [
            "You gain proficiency with four weapons of your choice."
        ]
        self.standard_popup("Weapon Master", descriptions, num_choices=4)



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


class ui_upd_Race:
    def __init__(self):
        self.parent = tag.rfeature.main()

    def standard(self, name, descriptions):
        a, t = gen_abil(name, 1)
        t_header = tag.rfeature.header(t)
        desc_tags = [tag.rfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=size.gwrap, tag=desc_tags[i])

    def standard_choice(self, name, items_list):
        a, t = gen_abil(name, 1)
        selection = q.db.Race.Abil[a]["Select"][0]
        t_header = tag.rfeature.header(t)
        t_label = tag.rfeature.label(t)
        t_tooltip = tag.rfeature.tooltip(t)
        t_popup = tag.rfeature.popup(t)
        t_select = tag.rfeature.select(t)

        with group(parent=self.parent):
            with group(horizontal=True):
                add_text(a, color=c_h1, tag=t_header)
                add_text(selection, color=c_h2, tag=t_label)
            
            item_delete(t_tooltip)
            with tooltip(t_label, tag=t_tooltip):
                spell_detail(selection)

            item_delete(t_popup)
            with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                add_combo(items=items_list, default_value=selection, width=120, no_arrow_button=True, user_data=["Race Spell Select", a], callback=cbh, tag=t_select)

    def standard_spell_list(self, name):
        a, t = gen_abil(name, 1)
        cdata = q.db.Race.Abil[a]
        t_header = tag.rfeature.header(t)

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            for spell in cdata.keys():
                t_label = tag.rfeature.label(t, spell)
                t_tooltip = tag.rfeature.tooltip(t, spell)
                with group(horizontal=True):
                    add_text(spell, color=c_h2, tag=t_label)
                    if "Use" in cdata[spell]:
                        t_toggle = tag.rfeature.toggle(t, spell)
                        add_checkbox(default_value=cdata[spell]["Use"][0], enabled=True, user_data=["Race Spell Use", t, spell], callback=cbh, tag=t_toggle)
                
                item_delete(t_tooltip)
                with tooltip(t_label, tag=t_tooltip):
                    spell_detail(spell)

    def standard_toggle(self, name, descriptions):
        a, t = gen_abil(name, 1)
        t_header = tag.rfeature.header(t)
        desc_tags = [tag.rfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]
        use_data = q.db.Race.Abil[a]["Use"]

        with group(parent=self.parent):
            with group(horizontal=True):
                add_text(a, color=c_h1, tag=t_header)
                for idx, val in enumerate(use_data):
                    t_toggle = tag.rfeature.toggle(t, idx)
                    add_checkbox(default_value=val, enabled=True, user_data=["Race Use", a, idx], callback=cbh, tag=t_toggle)
            
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=size.gwrap, tag=desc_tags[i])

    def Empty(self):
        pass
    def Human(self):
        pass
    def Human_Standard(self):
        pass
    def Human_Variant(self):
        pass
    def Elf(self):
        Fey_Ancestry_descriptions = ["You have advantage on saving throws against being charmed, and magic can't put you to sleep."]
        self.standard("Fey Ancestry", Fey_Ancestry_descriptions)

        Trance_descriptions = ["You don't need to sleep. Instead, you meditate deeply, remaining semiconscious, for 4 hours a day."]
        self.standard("Trance", Trance_descriptions)

    def Elf_High(self):
        self.standard_choice("Cantrip", g.list_High_Elf_Cantrip)

    def Elf_Wood(self):
        Mask_of_the_Wild_descriptions = ["You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."]
        self.standard("Mask of the Wild", Mask_of_the_Wild_descriptions)

    def Elf_Drow(self):
        self.standard_spell_list("Drow Magic")
        
    def Elf_Shadarkai(self):
        if q.db.Core.L < 3: desc = "(Bonus Action) Teleport up to 30 ft to an unoccupied space you can see. You can use this a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."
        else: desc = "(Bonus Action) Teleport up to 30 ft to an unoccupied space you can see. You can use this a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. Immediately after you use it, you gain resistance to all damage until the start of your next turn."
        
        Blessing_of_the_Raven_Queen_descriptions = [desc]
        self.standard_toggle("Blessing of the Raven Queen", Blessing_of_the_Raven_Queen_descriptions)

    def Dwarf(self):
        Dwarven_Resilience_descriptions = ["You have advantage on saving throws against poison, and you have resistance against poison damage."]
        self.standard("Dwarven Resilience", Dwarven_Resilience_descriptions)

        Stonecunning_descriptions = [f"Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."]
        self.standard("Stonecunning", Stonecunning_descriptions)

    def Dwarf_Hill(self):
        Dwarven_Toughness_descriptions = ["Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."]
        self.standard("Dwarven Toughness", Dwarven_Toughness_descriptions)

    def Dwarf_Mountain(self):
        pass

    def Halfling(self):
        Lucky_descriptions = ["When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll."]
        self.standard("Lucky", Lucky_descriptions)

        Brave_descriptions = ["You have advantage on saving throws against being frightened."]
        self.standard("Brave", Brave_descriptions)

        Halfling_Nimbleness_descriptions = ["You can move through the space of any creature that is of a size larger than yours."]
        self.standard("Halfling Nimbleness", Halfling_Nimbleness_descriptions)

    def Halfling_Lightfoot(self):
        Naturally_Stealthy_descriptions = ["You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."]
        self.standard("Naturally Stealthy", Naturally_Stealthy_descriptions)

    def Halfling_Stout(self):
        Stout_Resilience_descriptions = ["You have advantage on saving throws against poison, and you have resistance against poison damage."]
        self.standard("Stout Resilience", Stout_Resilience_descriptions)


    def Gnome(self):
        Gnome_Cunning_descriptions = ["You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."]
        self.standard("Gnome Cunning", Gnome_Cunning_descriptions)

    def Gnome_Forest(self):
        Speak_with_Small_Beasts_descriptions = ["Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts."]
        self.standard("Speak with Small Beasts", Speak_with_Small_Beasts_descriptions)

        a, t = gen_abil("Natural Illusionist", 1)
        cdata = q.db.Race.Abil[a]

        with group(parent=self.parent):
            add_text(a, color=c_h1, wrap=size.gwrap)
            for spell in cdata.keys():
                t_label = tag.rfeature.label(t, spell)
                t_tooltip = tag.rfeature.tooltip(t, spell)
                add_text(spell, color=c_h2, tag=t_label)

                item_delete(t_tooltip)
                with tooltip(t_label, tag=t_tooltip):
                    spell_detail(spell)
                    
    def Gnome_Rock(self):
        a, t = gen_abil("Tinker", 1)
        t_header = tag.rfeature.header(t)
        t_tooltip = tag.rfeature.tooltip(t)
        description = "Using tinker's tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp)..."

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            item_delete(t_tooltip)
            with tooltip(t_header, tag=t_tooltip):
                add_text(a, color=c_h1)
                add_text(description, color=c_text, wrap=300)

        Artificers_Lore_descriptions = ["Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply."]
        self.standard("Artificers Lore", Artificers_Lore_descriptions)

    def Dragonborn(self):
        pass
        
    def Dragonborn_subrace(self):
        # Calculate all dynamic values based on subrace and level
        dnum_map = [0, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        dnum = dnum_map[q.db.Core.L] if q.db.Core.L < len(dnum_map) else 5
        type_map = {"Black": "Acid", "Blue": "Lightning", "Brass": "Fire", "Bronze": "Lightning", "Copper": "Acid", "Gold": "Fire", "Green": "Poison", "Red": "Fire", "Silver": "Cold", "White": "Cold"}
        save_map = {"Acid": "DEX", "Lightning": "DEX", "Fire": "DEX", "Poison": "CON", "Cold": "CON"}
        
        damage_type = type_map.get(g.Subrace(), "Fire")
        save_ability = save_map.get(damage_type, "DEX")
        dc = 8 + q.db.Core.PB + q.db.Atr[save_ability]['Mod']

        # Use the standard helper for Draconic Resistance
        Draconic_Resistance_descriptions = [f"You have resistance to {damage_type.lower()} damage."]
        self.standard("Draconic Resistance", Draconic_Resistance_descriptions)

        # Use the standard_toggle helper for Breath Weapon
        Breath_Weapon_descriptions = [f"(Action) Exhale destructive energy. Each creature in a 30ft line must make a DC {dc} {save_ability} saving throw, taking {dnum}d6 {damage_type.lower()} damage on a failed save, and half as much damage on a successful one."]
        self.standard_toggle("Breath Weapon", Breath_Weapon_descriptions)

    def HalfOrc(self):
        Relentless_Endurance_descriptions = ["When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest."]
        self.standard_toggle("Relentless Endurance", Relentless_Endurance_descriptions)

        Savage_Attacks_descriptions = ["When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."]
        self.standard("Savage Attacks", Savage_Attacks_descriptions)

    def HalfOrc_Standard():
        pass

    def Tiefling(self):
        pass

    def Tiefling_Asmodeus(self):
        self.standard_spell_list("Infernal Legacy")

    def Tiefling_Baalzebul(self):
        self.standard_spell_list("Legacy of Maladomini")

    def Tiefling_Dispater(self):
        self.standard_spell_list("Legacy of Dis")

    def Tiefling_Fierna(self):
        self.standard_spell_list("Legacy of Phlegethos")

    def Tiefling_Glasya(self):
        self.standard_spell_list("Legacy of Malbolge")

    def Tiefling_Levistus(self):
        self.standard_spell_list("Legacy of Stygia")

    def Tiefling_Mammon(self):
        self.standard_spell_list("Legacy of Minauros")

    def Tiefling_Mephistopheles(self):
        self.standard_spell_list("Legacy of Cania")

    def Tiefling_Zariel(self):
        self.standard_spell_list("Legacy of Avernus")

    def Harengon(self):
        Lucky_Footwork_descriptions = ["When you fail a Dexterity saving throw, you can use your reaction to roll a d4 and add it to the save, potentially turning the failure into a success."]
        self.standard("Lucky Footwork", Lucky_Footwork_descriptions)

        Rabbit_Hop_descriptions = [f"As a bonus action, you can jump a number of feet equal to five times your proficiency bonus, without provoking opportunity attacks."]
        self.standard_toggle("Rabbit Hop", Rabbit_Hop_descriptions)

    def Harengon_Standard():
        pass

# #-----------------------------------------------------------

# #ANCHOR - Class shit



class ui_upd():
    FEAT = ui_upd_Feat()
    RACE = ui_upd_Race()
    CLASS = ui_upd_Class()
    
# #ANCHOR - Inventory

def ui_upd_INVE():
    ui_upd_INVE_Equip()
    ui_upd_INVE_Backpack()

class ui_upd_Backpack():
    def __init__(self):
        pass


    def fill_backpack():
        bdata = q.db.Inventory.Backpack
        item_count = len(bdata)
        table_tag = tag.backpack.table()
        
        # Count existing rows
        existing_rows = 0
        while does_item_exist(tag.backpack.row(existing_rows)):
            existing_rows += 1
        
        # Add more rows if needed
        for row_idx in range(existing_rows, item_count):
            with table_row(parent=table_tag, tag=tag.backpack.row(row_idx)):
                add_table_cell(tag=tag.backpack.cell("name", row_idx))
                add_table_cell(tag=tag.backpack.cell("slot", row_idx))
                add_table_cell(tag=tag.backpack.cell("qty", row_idx))
                add_table_cell(tag=tag.backpack.cell("weight", row_idx))
                add_table_cell(tag=tag.backpack.cell("cost", row_idx))
        
        # Delete excess rows if needed
        for row_idx in range(item_count, existing_rows):
            delete_item(tag.backpack.row(row_idx))

    def populate_backpack():
        """Populate the cells with actual item data"""
        bdata = q.db.Inventory.Backpack
        
        for row_idx, item in enumerate(bdata):
            cdata = q.w.Item(item)
            qty = bdata[item][1]
            weight = 0
            cost = 0
            
            # Clear cells
            item_clear(tag.backpack.cell("name", row_idx))
            item_clear(tag.backpack.cell("slot", row_idx))
            item_clear(tag.backpack.cell("qty", row_idx))
            item_clear(tag.backpack.cell("weight", row_idx))
            item_clear(tag.backpack.cell("cost", row_idx))
            
            # Populate cells
            add_text(g.iName(item), parent=tag.backpack.cell("name", row_idx))
            
            item_delete(tag.backpack.tooltip(row_idx))
            with tooltip(tag.backpack.cell("name", row_idx), tag=tag.backpack.tooltip(row_idx)):
                item_detail_handler(item)
                
            add_text(cdata.Slot, parent=tag.backpack.cell("slot", row_idx))
            
            with group(horizontal=True, parent=tag.backpack.cell("qty", row_idx)):
                add_text(qty, tag=tag.backpack.text(item, row_idx))
                add_button(label="<", callback=cbh, user_data=["Backpack Mod Item", item, -1], small=True)
                add_button(label=">", callback=cbh, user_data=["Backpack Mod Item", item, 1], small=True)
                add_button(label="X", callback=cbh, user_data=["Backpack Mod Item", item, "Clear"], small=True)
            
            add_text(weight, parent=tag.backpack.cell("weight", row_idx))
            add_text(cost, parent=tag.backpack.cell("cost", row_idx))


def backpack_contents():
    bdata = q.db.Inventory.Backpack
    """Update backpack contents without rebuilding the table"""
    table_tag = tag.backpack.table()
    
    # Clear existing rows (keep header)
    for child in get_item_children(table_tag, slot=1):
        delete_item(child)
    
    # Add current inventory items
    for row_idx, item in enumerate(bdata):
        cdata = q.w.Item(item)
        qty = bdata[item][1]
        weight = 0
        cost = 0
        
        with table_row(parent=table_tag):
            add_text(g.iName(item), tag=tag.backpack.row.name(row_idx))
            add_text(cdata.Slot, tag=tag.backpack.row.slot(row_idx))
            
            with group(horizontal=True):
                add_text(qty, tag=tag.backpack.row.qty(row_idx))
                add_button(label="<", callback=cbh, user_data=["Backpack Mod Item", item, -1], small=True)
                add_button(label=">", callback=cbh, user_data=["Backpack Mod Item", item, 1], small=True)
                add_button(label="X", callback=cbh, user_data=["Backpack Mod Item", item, "Clear"], small=True)
            
            add_text(weight, tag=tag.backpack.row.weight(row_idx))
            add_text(cost, tag=tag.backpack.row.cost(row_idx))
        
        # Add tooltip
        with tooltip(tag.backpack.row.name(row_idx)):
            item_detail_handler(item)
            
            


class ui_upd_equip:
    def __init__(self):
        self.backpack = None
        self.two_handed = None
        self.cEquip = None
        self.main_hand_item = None
    
    def load_data(self):
        self.backpack = set(q.db.Inventory.Backpack)
        self.two_handed = set(q.w.prop("Two-handed"))
        self.cEquip = q.db.Inventory.Equip
        self.main_hand_item = self.cEquip["Hand_1"]
    
    def get_slots(self):
        return [
            ("Face", q.w.slot("Face"), tag.equip.select("Face")),
            ("Throat", q.w.slot("Throat"), tag.equip.select("Throat")),
            ("Body", q.w.slot("Body"), tag.equip.select("Body")),
            ("Hands", q.w.slot("Hands"), tag.equip.select("Hands")),
            ("Waist", q.w.slot("Waist"), tag.equip.select("Waist")),
            ("Feet", q.w.slot("Feet"), tag.equip.select("Feet")),
            ("Armor", q.w.slot("Armor"), tag.equip.select("Armor")),
            ("Hand_1", q.w.slot("Weapon"), tag.equip.select("Hand_1")),
            ("Hand_2", q.w.list_off_hand, tag.equip.select("Hand_2")),
            ("Ring_1", q.w.slot("Ring"), tag.equip.select("Ring_1")),
            ("Ring_2", q.w.slot("Ring"), tag.equip.select("Ring_2")),
        ]
    
    def get_available_items(self, source):
        return [g.iName(i) for i in source if i in self.backpack]
    
    def get_default_value(self, slot_name):
        if slot_name == "Hand_2":
            if self.main_hand_item in self.two_handed:
                return "Weapon Grip"
            elif g.weapon_versatile():
                return "Verse Grip"
            else:
                return g.iName(self.cEquip["Hand_2"]) if self.cEquip["Hand_2"] in self.backpack else ""
        else:
            equipped = self.cEquip.get(slot_name, None)
            return g.iName(equipped) if equipped in self.backpack else ""
    
    def update(self):
        self.load_data()
        slots = self.get_slots()
        
        for slot_name, source, select_tag in slots:
            items = self.get_available_items(source)
            default_value = self.get_default_value(slot_name)
            configure_item(select_tag, items=items, default_value=default_value)



class ui_upd_bazaar:
    def __init__(self):
        self.dict_struct = {
            "Weapon": [("Simple", "Melee"), ("Simple", "Ranged"), ("Martial", "Melee"), ("Martial", "Ranged")],
            "Armor": ["Light", "Medium", "Heavy"]
        }
        
        
    def create_bazaar_button(self, item, category_type, parent):
        button_tag = tag.bazaar.button(item)
        tooltip_tag = tag.bazaar.tooltip(item)
        add_button(label=g.isName(item), width=size.w_item, user_data=["Bazaar Add Item", category_type, item], callback=cbh, tag=button_tag, parent=parent)
        with tooltip(button_tag, tag=tooltip_tag):
            item_detail_handler(item)

    def get_target_items(self, categories, rank):
        target_set = set()
        is_weapon_type = isinstance(categories[0], tuple)
        for category_info in categories:
            if is_weapon_type:
                tag1, tag2 = category_info
                items = q.w.mcategory(rank, tag1, tag2)
            else:
                items = q.w.mcategory(rank, category_info)
            target_set.update(items)
        return target_set

    def get_current_items(self, parent_container):
        current_items = set()
        if does_item_exist(parent_container):
            container_children = get_item_children(parent_container, 1)
            for group_id in container_children:
                if get_item_info(group_id)['type'] == 'Group':
                    row_children = get_item_children(group_id, 1)
                    for button_id in row_children:
                        button_alias = get_item_alias(button_id)
                        if button_alias and "bazaar" in button_alias and "add" in button_alias:
                            # Extract item from tag system instead of string parsing
                            current_items.add(button_id)
        return current_items

    def rebuild_category(self, categories, equipment_type, parent_container, rank):
        item_clear(parent_container)
        
        with group(parent=parent_container):
            for category_info in categories:
                is_weapon_type = isinstance(categories[0], tuple)
                if is_weapon_type:
                    tag1, tag2 = category_info
                    label = f"{tag1} {tag2}"
                    items = q.w.mcategory(rank, tag1, tag2)
                    items.sort()
                else:
                    label = tag1 = category_info
                    items = q.w.mcategory(rank, tag1)
                    items.sort()
                
                add_separator(label=label if rank == 0 else f"{label} (+{rank})")
                
                for i in range(0, len(items), 4):
                    with group(horizontal=True):
                        horizontal_group_id = last_item()
                        for item in items[i:i+4]:
                            self.create_bazaar_button(item, equipment_type, parent=horizontal_group_id)
    
    def update(self):
        for equipment_type, categories in self.dict_struct.items():
            for rank in range(5):
                rarity = g.item_rarity(rank)
                parent_container = tag.bazaar.container(equipment_type, rarity)

                if not does_item_exist(parent_container):
                    continue

                target_set = self.get_target_items(categories, rank)
                current_items = self.get_current_items(parent_container)
                
                if target_set != current_items:
                    self.rebuild_category(categories, equipment_type, parent_container, rank)



def item_detail_handler(item):
    data = q.w.Item(item)
    if data.Slot == "Weapon":
        item_detail_weapon(data)
    if data.Slot == "Armor":
        item_detail_armor(data)

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
            add_text(g.item_rarity(data.Tier), color=c_rarity[f"{g.item_rarity(data.Tier)}"])
            add_text("Weight", color=c_h1)
            add_text(data.Weight, color=c_text)
            add_text("Cost", color=c_h1)
            add_text(data.Cost, color=c_h9)
def item_detail_armor(data):
    pass












# def resize_window():
#     print("resizing_window")


