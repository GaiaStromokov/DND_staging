from ui.upd_helper_import import *



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
            add_combo(items=get.list_Base_Atr, default_value="", width=value_width, no_arrow_button=True, user_data=["Base Atr", stat], callback=q.cbh, tag=tCombo)

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
        add_checkbox(default_value=False, enabled=False, user_data=[], callback=q.cbh, tag=tBool)
        add_button(label="", enabled=False, width=mod_width, tag=tMod)
    with tooltip(tLabel):
        add_text(get.dict_Skill[skill]["Desc"])
        
    with tooltip(tBool):
        for source in ["Player", "Race", "Class", "BG", "Feat"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=50)
                
                tSource = tag.skill.source(skill, source)
                add_checkbox(default_value=False, enabled=False, user_data=[], callback=q.cbh, tag=tSource)


def create_pdescription():
    tLabel = tag.pdesc.label()
    with popup(tLabel, mousebutton=mvMouseButton_Left):
        for item in get.list_Description: 
            tInput = tag.pdesc.input(item)
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=size.w_l_btn)
                add_input_text(default_value="", on_enter=True, width = 70, user_data=["Description", item], callback=q.cbh, tag=tInput)
    with tooltip(tLabel):
        for item in get.list_Description: 
            tText = tag.pdesc.text(item)
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=size.w_l_btn)
                add_text("", color=c_h2, wrap=400, tag=tText)




def create_ideals(name: str):
    name = name.lower()
    
    tLabel = tag.char.label(name)
    tInput = tag.char.input(name)
    tText = tag.char.text(name)
    with popup(tLabel, mousebutton=mvMouseButton_Left): add_input_text(default_value="", on_enter=True, user_data=["Characteristic", name], callback=q.cbh, tag=tInput)
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
                        add_selectable(label=get.pName(item), default_value=False, user_data=["Player Prof Input", category, item], callback=q.cbh, tag=tSelectable)

    with tooltip(tLabel):
        with group(horizontal=True):
            for category, items in proficiency_map.items():
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    add_text(category)
                    add_separator()
                    for item in items:
                        tText = tag.prof.multi(category, item, suffix="text")
                        add_text(get.pName(item), color=(0, 0, 0), tag=tText)





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
            for i in get.list_Coins:
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
            add_button(label="<", user_data=["Level Input", -1], callback=q.cbh)
            add_button(label="", width=25, tag=tag.core.val("level"))
            add_button(label=">", user_data=["Level Input", 1], callback=q.cbh)
            add_button(label="", enabled=False, width=55, tag=tag.core.val("pb"))
            with group(horizontal=True):
                add_button(label="Race", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Race"], callback = q.cbh, tag=tag.core.select("race"))
            with group(horizontal=True):
                add_button(label="Subrace", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Subrace"], callback = q.cbh, tag=tag.core.select("subrace"))
            with group(horizontal=True):
                add_button(label="Class", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Class"], callback = q.cbh, tag=tag.core.select("class"))        
            with group(horizontal=True):
                add_button(label="Subclass", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Subclass"], callback = q.cbh, tag=tag.core.select("subclass"))        
            with group(horizontal=True):
                add_button(label="Background", enabled=False, width=80)
                add_combo(width=w_max-88, no_arrow_button=True, user_data=[f"Core Background"], callback = q.cbh, tag=tag.core.select("background"))


                
def init_window_attributes():
    with group(parent=tag.atr.window()):
        w_max=size.w_attributes-16
        add_button(label="Attributes", enabled=False, width=w_max, height=size.h_header_1)
        for stat in get.list_Atr:
            create_attribute_row(stat)



def init_window_health():
    with group(parent=tag.health.window()):
        w_max=size.w_health-16
        h_max=size.h_health-15
        add_button(label="Health", enabled=False, width=w_max, height=size.h_header_1)
        with group(horizontal=False):
            with group(horizontal=True):
                add_button(label="+", width=size.w_s_btn, user_data=["HP","HP", 1], callback=q.cbh)
                add_button(label="CUR / MAX", enabled=False, width=w_max-108, tag="health_label")
                add_button(label="TEMP", enabled=False, width=w_max-150)
                add_button(label="+", width=size.w_s_btn, user_data=["HP","Temp", 1], callback=q.cbh)
            with group(horizontal=True):
                add_button(label="-", width=size.w_s_btn, user_data=["HP","HP", -1], callback=q.cbh)
                add_button(label="", enabled=False, width=w_max-108, tag=tag.health.val("hp"))
                add_button(label="", enabled=False, width=w_max-150, tag=tag.health.val("temp"))
                add_button(label="-", width=size.w_s_btn, user_data=["HP","Temp", -1], callback=q.cbh)
    
    with popup("health_label", mousebutton=mvMouseButton_Left):
        add_button(label="Max", width=size.w_l_btn)
        add_input_int(default_value=0, width=90, user_data=["Player HP Mod"], callback=q.cbh, tag=tag.health.max("hp"))
        

def init_window_skills():
    w_max=size.w_skill-16
    h_max=size.w_skill-15
    with group(parent=tag.skill.window()):
        add_button(label="Skills", enabled=False, width=w_max, height=size.h_header_1)
        for skill in get.list_Skill:
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
        for i in get.list_Vision:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=tag.vision.source(i))

def init_window_speed():
    with group(parent=tag.speed.window()):
        add_button(label="Speed", enabled=False, width=size.w_m_btn, tag = tag.speed.label())
        add_button(label="", enabled=False, width=size.w_m_btn, tag=tag.speed.val())
    with tooltip(tag.speed.label()):
        for i in get.list_Speed:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=tag.speed.source(i))



def init_window_conditions():
    with group(parent=tag.cond.window()):
        add_button(label="Conditions", enabled=False, width=size.w_header_2, height=26, tag=tag.cond.label())
    with popup(tag.cond.label(), mousebutton=mvMouseButton_Left):
        with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
            for i in get.list_Condition:
                add_selectable(label=i, default_value=False, user_data=["Condition", i], callback=q.cbh, tag=tag.cond.toggle(i))
    with tooltip(tag.cond.label()):
        with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
            for i in get.list_Condition:
                add_text(i, color=(0, 0, 0), tag=tag.cond.text(i))


def init_window_rest():
    with group(parent=tag.rest.window()):
        add_button(label="Short Rest", width=size.w_header_2, height=30, user_data=["Short Rest"], callback=q.cbh, tag=tag.rest.button("short"))
        add_button(label="Long Rest", width=size.w_header_2, height=30, user_data=["Long Rest"], callback=q.cbh, tag=tag.rest.button("long"))


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

    create_proficiency_addons(tag.prof.label("weapon"), {k: set(q.w.prof("Weapon")) & set(q.w.cat(k)) for k in ["Simple", "Martial"]})
    create_proficiency_addons(tag.prof.label("armor"), {"Armor": q.w.prof("Armor")})
    create_proficiency_addons(tag.prof.label("tool"), {"Artisan": get.list_Job, "Gaming": get.list_Game, "Musical": get.list_Music})
    create_proficiency_addons(tag.prof.label("lang"), {"Languages": get.list_Lang})

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
    for i in get.list_Ideals: create_ideals(i)
    create_pdescription()






def init_window_block():
    w1 = size.w_block - 16
    w2 = w1 - 16
    h1 = size.h_block - 40
    h2 = h1 - 15
    with group(parent=tag.block.window()):
        with tab_bar(tag=tag.block.tabbar()):
            with tab(label="Features/Traits"):
                with child_window(width=w1, height=h1, border=True):
                    add_separator(label="Race")
                    with child_window(auto_resize_y=True, width=w2, border=True, tag = tag.rfeature.sub()):
                        with group(horizontal=True):
                            add_text("Ability Score Increase: +1/+2", color=c_h1)
                            add_combo(items=get.list_Atr, default_value="",  width=50, no_arrow_button=True, user_data=["Race Asi", 0], callback=q.cbh, tag=tag.rfeature.select("asi_0"))
                            add_combo(items=get.list_Atr, default_value="",  width=50, no_arrow_button=True, user_data=["Race Asi", 1], callback=q.cbh, tag=tag.rfeature.select("asi_1"))
                            add_button(label="Clear", enabled=True, width=50, user_data=["Race Asi","Clear"], callback=q.cbh, tag=tag.rfeature.button("asi_clear"))
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
                    for j in get.list_weapon_attributes:
                        add_table_cell(tag=tag.wactions.cell(j,i))


def init_window_inventory():
    h=size.h_inventory
    with group(parent=tag.inve.window()):
        with tab_bar():
            with tab(label="Equip"):
                add_child_window(height=h-28, border=True, no_scrollbar=True, tag=tag.equip.window())
            with tab(label="Backpack"):
                add_child_window(height=h-80, border=True, no_scrollbar=True, tag=tag.backpack.window())
                add_child_window(height=h-294, border=True, tag=tag.backpack.window("totals"))
            with tab(label="Bazaar"):
                add_child_window(height=h-26, border=True, no_scrollbar=True, tag=tag.bazaar.window())

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
    with group(parent=tag.bazaar.window()):
        with tab_bar():
            for equipment_type in get.list_equip_type:
                with tab(label=equipment_type):
                    with tab_bar():
                        for rarity in range(5):
                            rank = get.item_rarity(rarity)
                            with tab(label=rank):
                                add_child_window(height=size.h_inventory - 85, border=True, no_scrollbar=True, tag=tag.bazaar.window(equipment_type, rank))
def load_icons():
    figure_w, figure_h, figure_channel, figure_data = load_image("DT_DND/image/Figure_Icon.png")
    armor_w, armor_h, armor_channel, armor_data = load_image("DT_DND/image/Armor_Icon.png")
    arms_w, arms_h, arms_channel, arms_data = load_image("DT_DND/image/Arms_Icon.png")
    body_w, body_h, body_channel, body_data = load_image("DT_DND/image/Body_Icon.png")
    face_w, face_h, face_channel, face_data = load_image("DT_DND/image/Face_Icon.png")
    hands_w, hands_h, hands_channel, hands_data = load_image("DT_DND/image/Hands_Icon.png")
    head_w, head_h, head_channel, head_data = load_image("DT_DND/image/Head_Icon.png")
    mainhand_w, mainhand_h, mainhand_channel, mainhand_data = load_image("DT_DND/image/MainHand_Icon.png")
    offhand_w, offhand_h, offhand_channel, offhand_data = load_image("DT_DND/image/OffHand_Icon.png")
    ring_w, ring_h, ring_channel, ring_data = load_image("DT_DND/image/Ring_Icon.png")
    shoulders_w, shoulders_h, shoulders_channel, shoulders_data = load_image("DT_DND/image/Shoulders_Icon.png")
    throat_w, throat_h, throat_channel, throat_data = load_image("DT_DND/image/Throat_Icon.png")
    waist_w, waist_h, waist_channel, waist_data = load_image("DT_DND/image/Waist_Icon.png")
    feet_w, feet_h, feet_channel, feet_data = load_image("DT_DND/image/Feet_Icon.png")

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
    
    with group(parent=tag.equip.window()):
        with group(horizontal=False):
            with group(horizontal=True):
                # Left side
                with group(horizontal=False):
                    for left_slot, right_slot in equipment_pairs:
                        with group(horizontal=True):
                            add_image_button(tag.icon(left_slot), callback=q.cbh, user_data=["Clear Equip", left_slot, "Clear"], tag=tag.img(left_slot))
                            with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                                add_combo(width=wbtn, no_arrow_button=True, user_data=["Equip Equip", left_slot], callback=q.cbh, tag=tag.equip_item(left_slot))
                # Center
                add_image(tag.icon("figure"))
                # Right side
                with group(horizontal=False):
                    for left_slot, right_slot in equipment_pairs:
                        with group(horizontal=True):
                            with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                                add_combo(width=wbtn, no_arrow_button=True, user_data=["Equip Equip", right_slot], callback=q.cbh, tag=tag.equip_item(right_slot))
                            add_image_button(tag.icon(right_slot), callback=q.cbh, user_data=["Clear Equip", right_slot, "Clear"], tag=tag.img(right_slot))



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