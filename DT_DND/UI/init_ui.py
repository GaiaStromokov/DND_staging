from ui.upd_helper_import import *
from path_helper import get_path


def create_attribute_row(stat: str):
    label_width=40
    value_width=30

    tSum = Tag.atr.sum(stat)
    tMod = Tag.atr.mod(stat)
    tCombo = Tag.atr.select(stat)

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
                tSource = Tag.atr.source(stat, source.lower())
                add_button(label="", enabled=False, width=25, tag=tSource)



def create_skill_row(skill: str):
    label_width = 113
    mod_width = 30

    tLabel = Tag.skill.label(skill)
    tToggle = Tag.skill.toggle(skill)
    tMod = Tag.skill.mod(skill)
    
    
    with group(horizontal=True): 
        add_button(label=skill, enabled=False, width=label_width, tag=tLabel)
        add_checkbox(default_value=False, enabled=False, user_data=[], callback=q.cbh, tag=tToggle)
        add_button(label="", enabled=False, width=mod_width, tag=tMod)
    with tooltip(tLabel):
        add_text(get.dict_Skill[skill]["Desc"])
        
    with tooltip(tToggle):
        for source in ["Player", "Race", "Class", "BG", "Feat"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=50)
                
                tSource = Tag.skill.source(skill, source)
                add_checkbox(default_value=False, enabled=False, user_data=[], callback=q.cbh, tag=tSource)


def create_pdescription():
    tLabel = Tag.pdesc.label()
    with popup(tLabel, mousebutton=mvMouseButton_Left):
        for item in get.list_Description: 
            tInput = Tag.pdesc.input(item)
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=sz.w_l_btn)
                add_input_text(default_value="", on_enter=True, width = 70, user_data=["Description", item], callback=q.cbh, tag=tInput)
    with tooltip(tLabel):
        for item in get.list_Description: 
            tText = Tag.pdesc.text(item)
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=sz.w_l_btn)
                add_text("", color=c_h2, wrap=400, tag=tText)




def create_ideals(name: str):
    name = name.lower()
    
    tLabel = Tag.char.label(name)
    tInput = Tag.char.input(name)
    tText = Tag.char.text(name)
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
                        tSelectable = Tag.prof.multi(category, item, suffix="toggle")
                        add_selectable(label=get.pName(item), default_value=False, user_data=["Player Prof Input", category, item], callback=q.cbh, tag=tSelectable)

    with tooltip(tLabel):
        with group(horizontal=True):
            for category, items in proficiency_map.items():
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    add_text(category)
                    add_separator()
                    for item in items:
                        tText = Tag.prof.multi(category, item, suffix="text")
                        add_text(get.pName(item), color=(0, 0, 0), tag=tText)





def init_window_skeleton():
    with window(no_title_bar=True, no_close=True, autosize=True, tag="window_main"):
        with group(horizontal=True):
            with group(horizontal=False):
                with group(horizontal=True):
                    with group(horizontal=False):
                        add_child_window(tag=Tag.core.window(), width=sz.w_core, height=sz.h_core, border=True, no_scrollbar=True)
                        add_child_window(tag=Tag.health.window(), width=sz.w_health, height=sz.h_health, border=True)
                        add_child_window(tag=Tag.prof.window(), width=sz.w_proficiencies, height=sz.h_proficiencies, border=True)
                        add_child_window(tag=Tag.char.window(), width=sz.w_character, height=sz.h_character, border=True)
                        add_child_window(tag=Tag.buffer1.window(), width=sz.w_buffer_2, height=sz.h_buffer_2, border=True, no_scrollbar=True)
                    with group(horizontal=False):
                        add_child_window(tag=Tag.atr.window(), width=sz.w_attributes, height=sz.h_attributes, border=True)
                        with group(horizontal=True):
                            add_child_window(tag=Tag.init.window(), width=sz.w_initiative, height=sz.h_initiative, border=True)
                            add_child_window(tag=Tag.ac.window(), width=sz.w_armor_class, height=sz.h_armor_class, border=True)
                        with group(horizontal=True):
                            add_child_window(tag=Tag.vision.window(), width=sz.w_vision, height=sz.h_vision, border=True)
                            add_child_window(tag=Tag.speed.window(), width=sz.w_speed, height=sz.h_speed, border=True)
                        add_child_window(tag=Tag.cond.window(), width=sz.w_conditions, height=sz.h_conditions, border=True)
                        add_child_window(tag=Tag.rest.window(), width=sz.w_rest, height=sz.h_rest, border=True)
                        add_child_window(tag=Tag.buffer2.window(), width=sz.w_buffer_1, height=sz.h_buffer_1, border=True, no_scrollbar=True)
                    with group(horizontal=False):
                        add_child_window(tag=Tag.skill.window(), width=sz.w_skill, height=sz.h_skill, border=True, no_scrollbar=True)
                with group(horizontal=False):
                    add_child_window(tag=Tag.inve.window(), width=sz.w_inventory, height=sz.h_inventory + 12, border=True, no_scrollbar=True)
            with group(horizontal=False):
                add_child_window(tag=Tag.block.window(), width=sz.w_block, height=sz.h_block, border=True, no_scrollbar=True)
                add_child_window(tag=Tag.wallet.window(), width=sz.w_wallet, height=sz.h_wallet, border=True, no_scrollbar=True)

def init_window_wallet():
    with group(parent=Tag.wallet.window()):
        with group(horizontal=True):
            for i in get.list_Coins:
                with group(horizontal=True):
                    add_button(label=i)
                    add_text("0", color=c_h9, tag=Tag.wallet.val(i))


def init_window_core():
    w_max=sz.w_core-16
    h_max=sz.h_core-16
    w_abtn=80
    w_combo = w_max-88
    with group(parent=Tag.core.window()):
        add_button(label="Character info", enabled=False, width=w_max, height = sz.h_header_1)
        with group(horizontal=True):
            add_button(label="Level", enabled=False, width=50)
            add_button(label="<", user_data=["Level Input", -1], callback=q.cbh)
            add_button(label="", width=25, tag=Tag.core.val("level"))
            add_button(label=">", user_data=["Level Input", 1], callback=q.cbh)
            add_button(label="", enabled=False, width=55, tag=Tag.core.val("pb"))
        with group(horizontal=True):
            add_button(label="Race", enabled=False, width=w_abtn)
            add_combo(width=w_combo, no_arrow_button=True, user_data=[f"Core Race"], callback = q.cbh, tag=Tag.core.select("race"))
        with group(horizontal=True):
            add_button(label="Subrace", enabled=False, width=w_abtn)
            add_combo(width=w_combo, no_arrow_button=True, user_data=[f"Core Subrace"], callback = q.cbh, tag=Tag.core.select("subrace"))
        with group(horizontal=True):
            add_button(label="Class", enabled=False, width=w_abtn)
            add_combo(width=w_combo, no_arrow_button=True, user_data=[f"Core Class"], callback = q.cbh, tag=Tag.core.select("class"))        
        with group(horizontal=True):
            add_button(label="Subclass", enabled=False, width=w_abtn)
            add_combo(width=w_combo, no_arrow_button=True, user_data=[f"Core Subclass"], callback = q.cbh, tag=Tag.core.select("subclass"))        
        with group(horizontal=True):
            add_button(label="Background", enabled=False, width=w_abtn)
            add_combo(width=w_combo, no_arrow_button=True, user_data=[f"Core Background"], callback = q.cbh, tag=Tag.core.select("background"))


                
def init_window_attributes():
    with group(parent=Tag.atr.window()):
        w_max=sz.w_attributes-16
        add_button(label="Attributes", enabled=False, width=w_max, height=sz.h_header_1)
        for stat in get.list_Atr:
            create_attribute_row(stat)



def init_window_health():
    with group(parent=Tag.health.window()):
        w_max=sz.w_health-16
        h_max=sz.h_health-15
        add_button(label="Health", enabled=False, width=w_max, height=sz.h_header_1)
        with group(horizontal=False):
            with group(horizontal=True):
                add_button(label="+", width=sz.w_s_btn, user_data=["HP","HP", 1], callback=q.cbh)
                add_button(label="CUR / MAX", enabled=False, width=w_max-108, tag="health_label")
                add_button(label="TEMP", enabled=False, width=w_max-150)
                add_button(label="+", width=sz.w_s_btn, user_data=["HP","Temp", 1], callback=q.cbh)
            with group(horizontal=True):
                add_button(label="-", width=sz.w_s_btn, user_data=["HP","HP", -1], callback=q.cbh)
                add_button(label="", enabled=False, width=w_max-108, tag=Tag.health.val("hp"))
                add_button(label="", enabled=False, width=w_max-150, tag=Tag.health.val("temp"))
                add_button(label="-", width=sz.w_s_btn, user_data=["HP","Temp", -1], callback=q.cbh)
    
    with popup("health_label", mousebutton=mvMouseButton_Left):
        add_button(label="Max", width=sz.w_l_btn)
        add_input_int(default_value=0, width=90, user_data=["Player HP Mod"], callback=q.cbh, tag=Tag.health.max("hp"))
        

def init_window_skills():
    w_max=sz.w_skill-16
    h_max=sz.w_skill-15
    with group(parent=Tag.skill.window()):
        add_button(label="Skills", enabled=False, width=w_max, height=sz.h_header_1)
        for skill in get.list_Skill:
            create_skill_row(skill)


def init_window_initiatives():
    with group(parent=Tag.init.window()):
        add_button(label="Init", enabled=False, width=sz.w_m_btn, tag=Tag.init.label())
        add_button(label="", enabled=False, width=sz.w_m_btn, tag=Tag.init.val())
    with tooltip(Tag.init.label()):
        for source in ["Dex", "Race", "Class"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=40)
                add_button(label="", enabled=False, width=25, tag=Tag.init.source(source.lower()))

def init_window_armor():
    with group(parent=Tag.ac.window()):
        add_button(label="AC", enabled=False, width=sz.w_m_btn, tag=Tag.ac.label())
        add_button(label="", enabled=False, width=sz.w_m_btn, tag=Tag.ac.val())

        with tooltip(Tag.ac.label()):
            for label in ["Base", "Dex", "Shield"]:
                label_tag=label.lower()
                with group(horizontal=True):
                    add_button(label=label, enabled=False, width=50)
                    add_button(label="", enabled=False, width=40, tag=Tag.ac.source(label_tag))



def init_window_vision():
    with group(parent=Tag.vision.window()):
        add_button(label="Vision", enabled=False, width=sz.w_m_btn, tag = Tag.vision.label())
        add_button(label="", enabled=False, width=sz.w_m_btn, tag=Tag.vision.val())
    with tooltip(Tag.vision.label()):
        for i in get.list_Vision:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=Tag.vision.source(i))

def init_window_speed():
    with group(parent=Tag.speed.window()):
        add_button(label="Speed", enabled=False, width=sz.w_m_btn, tag = Tag.speed.label())
        add_button(label="", enabled=False, width=sz.w_m_btn, tag=Tag.speed.val())
    with tooltip(Tag.speed.label()):
        for i in get.list_Speed:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=Tag.speed.source(i))



def init_window_conditions():
    with group(parent=Tag.cond.window()):
        add_button(label="Conditions", enabled=False, width=sz.w_header_2-72, height=26, tag=Tag.cond.label())
    with popup(Tag.cond.label(), mousebutton=mvMouseButton_Left):
        with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
            for i in get.list_Condition:
                add_selectable(label=i, default_value=False, user_data=["Condition", i], callback=q.cbh, tag=Tag.cond.toggle(i))
    with tooltip(Tag.cond.label()):
        with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
            for i in get.list_Condition:
                add_text(i, color=(0, 0, 0), tag=Tag.cond.text(i))


def init_window_rest():
    with group(parent=Tag.rest.window()):
        add_button(label="Short Rest", width=sz.w_header_2-72, height=30, user_data=["Short Rest"], callback=q.cbh, tag=Tag.rest.button("short"))
        add_button(label="Long Rest", width=sz.w_header_2-72, height=30, user_data=["Long Rest"], callback=q.cbh, tag=Tag.rest.button("long"))


def init_window_buffer():
    pass


def init_window_proficienices():
    w_max=sz.w_proficiencies-16
    h_max=sz.w_proficiencies-15
    btn_w = w_max-101
    with group(parent=Tag.prof.window()):
        add_button(label="Proficiencies", enabled=False, width=w_max, height=sz.h_header_1)
        with group(horizontal=True):
            add_button(label="Weapons", width=btn_w, tag=Tag.prof.label("weapon"))
            add_button(label="Armor", width=btn_w, tag=Tag.prof.label("armor"))
        with group(horizontal=True):
            add_button(label="Tools", width=btn_w, tag=Tag.prof.label("tool"))
            add_button(label="Languages", width=btn_w, tag=Tag.prof.label("lang"))

    create_proficiency_addons(Tag.prof.label("weapon"), {k: q.w.search(Tier=0, Slot="Weapon", Cat=k) for k in ["Simple", "Martial"]})
    create_proficiency_addons(Tag.prof.label("armor"), {"Armor": q.w.search(Tier=0, Slot=["Armor", "Shield"])})
    create_proficiency_addons(Tag.prof.label("tool"), {"Artisan": get.list_Job, "Gaming": get.list_Game, "Musical": get.list_Music})
    create_proficiency_addons(Tag.prof.label("lang"), {"Languages": get.list_Lang})

def init_window_characteristics():
    w_max=sz.w_character-16
    h_max=sz.h_character-15
    btn_w = w_max-101
    with group(parent=Tag.char.window()):
        add_button(label="Characteristics", enabled=False, width=w_max, height=sz.h_header_1, tag=Tag.pdesc.label())
        with group(horizontal=True):
            add_button(label="Traits", width=btn_w, tag=Tag.char.label("traits"))
            add_button(label="Ideals", width=btn_w, tag=Tag.char.label("ideals"))
        with group(horizontal=True):
            add_button(label="Bonds", width=btn_w, tag=Tag.char.label("bonds"))
            add_button(label="Flaws", width=btn_w, tag=Tag.char.label("flaws"))
    for i in get.list_Ideals: create_ideals(i)
    create_pdescription()






def init_window_block():
    w1 = sz.w_block - 16
    w2 = w1 - 16
    h1 = sz.h_block - 40
    h2 = h1 - 15
    with group(parent=Tag.block.window()):
        with tab_bar(tag=Tag.block.tabbar()):
            with tab(label="Features/Traits"):
                with child_window(width=w1, height=h1, border=True):
                    add_separator(label="Race")
                    with child_window(auto_resize_y=True, width=w2, border=True, tag = Tag.rfeature.sub()):
                        with group(horizontal=True):
                            add_text("Ability Score Increase: +1/+2", color=c_h1)
                            add_combo(items=get.list_Atr, default_value="",  width=50, no_arrow_button=True, user_data=["Race Asi", 0], callback=q.cbh, tag=Tag.rfeature.select("asi_0"))
                            add_combo(items=get.list_Atr, default_value="",  width=50, no_arrow_button=True, user_data=["Race Asi", 1], callback=q.cbh, tag=Tag.rfeature.select("asi_1"))
                            add_button(label="Clear", enabled=True, width=50, user_data=["Race Asi","Clear"], callback=q.cbh, tag=Tag.rfeature.button("asi_clear"))
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=Tag.rfeature.main())
                    add_separator(label="Class")
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=Tag.cfeature.sub())
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=Tag.cfeature.main())
                    add_separator(label="Feat")
                    with child_window(auto_resize_y=True, width=w2, border=False):
                        with collapsing_header(label="Milestones"):
                            add_child_window(auto_resize_y=True, width=w2, border=True, tag=Tag.mfeature.sub())
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=Tag.mfeature.main())
                    add_separator(label="Background")
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=Tag.bfeature.sub())
                    add_child_window(auto_resize_y=True, width=w2, border=True, tag=Tag.bfeature.main())
            with tab(label="Actions"):
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    with child_window(auto_resize_y=True, width=w2, border=True, tag = Tag.wactions.window()):
                        add_separator(label="Weapons")



def init_window_block_actions_weapons():
    with group(parent=Tag.wactions.window()):
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
                        add_table_cell(tag=Tag.wactions.cell(j,i))


def init_window_inventory():
    h=sz.h_inventory
    with group(parent=Tag.inve.window()):
        with tab_bar():
            with tab(label="Closet"):
                add_child_window(height=h-28, border=True, no_scrollbar=True, tag=Tag.closet.window())
            with tab(label="Backpack"):
                add_child_window(height=h-80, border=True, no_scrollbar=True, tag=Tag.backpack.window())
                add_child_window(height=h-294, border=True, tag=Tag.backpack.window("totals"))
            with tab(label="Bazaar"):
                add_child_window(height=h-26, border=True, no_scrollbar=True, tag=Tag.bazaar.window())

def init_window_inventory_backpack():
    parent = Tag.backpack.window()
    item_clear(parent)
    with group(parent=parent):
        with table(header_row=True, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True, resizable=True, tag=Tag.backpack.table()):
            add_table_column(label="Item", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Slot", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="QTY", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Weight", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Cost", width_stretch=True, init_width_or_weight=0)
            

def init_window_inventory_bazaar():
    with group(parent=Tag.bazaar.window()):
        with tab_bar():
            for equipment_type in get.list_equip_type:
                with tab(label=equipment_type):
                    with tab_bar():
                        for rarity in range(5):
                            rank = get.item_rarity(rarity)
                            with tab(label=rank):
                                add_child_window(height=sz.h_inventory - 85, border=True, no_scrollbar=True, tag=Tag.bazaar.window(equipment_type, rank))
def load_icons():
    figure_w, figure_h, figure_channel, figure_data = load_image(get_path("Image", "Figure_Icon.png"))
    armor_w, armor_h, armor_channel, armor_data = load_image(get_path("Image", "Armor_Icon.png"))
    arms_w, arms_h, arms_channel, arms_data = load_image(get_path("Image", "Arms_Icon.png"))
    body_w, body_h, body_channel, body_data = load_image(get_path("Image", "Body_Icon.png"))
    face_w, face_h, face_channel, face_data = load_image(get_path("Image", "Face_Icon.png"))
    hands_w, hands_h, hands_channel, hands_data = load_image(get_path("Image", "Hands_Icon.png"))
    head_w, head_h, head_channel, head_data = load_image(get_path("Image", "Head_Icon.png"))
    hand1_w, hand1_h, hand1_channel, hand1_data = load_image(get_path("Image", "Hand1_Icon.png"))
    hand2_w, hand2_h, hand2_channel, hand2_data = load_image(get_path("Image", "Hand2_Icon.png"))
    ring1_w, ring1_h, ring1_channel, ring1_data = load_image(get_path("Image", "Ring_Icon.png"))
    ring2_w, ring2_h, ring2_channel, ring2_data = load_image(get_path("Image", "Ring_Icon.png"))
    shoulders_w, shoulders_h, shoulders_channel, shoulders_data = load_image(get_path("Image", "Shoulders_Icon.png"))
    throat_w, throat_h, throat_channel, throat_data = load_image(get_path("Image", "Throat_Icon.png"))
    waist_w, waist_h, waist_channel, waist_data = load_image(get_path("Image", "Waist_Icon.png"))
    feet_w, feet_h, feet_channel, feet_data = load_image(get_path("Image", "Feet_Icon.png"))

    with texture_registry(show=False):
        add_static_texture(width=figure_w, height=figure_h, default_value=figure_data, tag=Tag.closet.icon("Figure"))
        add_static_texture(width=armor_w, height=armor_h, default_value=armor_data, tag=Tag.closet.icon("Armor"))
        add_static_texture(width=arms_w, height=arms_h, default_value=arms_data, tag=Tag.closet.icon("Arms"))
        add_static_texture(width=body_w, height=body_h, default_value=body_data, tag=Tag.closet.icon("Body"))
        add_static_texture(width=face_w, height=face_h, default_value=face_data, tag=Tag.closet.icon("Face"))
        add_static_texture(width=hands_w, height=hands_h, default_value=hands_data, tag=Tag.closet.icon("Hands"))
        add_static_texture(width=head_w, height=head_h, default_value=head_data, tag=Tag.closet.icon("Head"))
        add_static_texture(width=hand1_w, height=hand1_h, default_value=hand1_data, tag=Tag.closet.icon("Hand_1"))
        add_static_texture(width=hand2_w, height=hand2_h, default_value=hand2_data, tag=Tag.closet.icon("Hand_2"))
        add_static_texture(width=ring1_w, height=ring1_h, default_value=ring1_data, tag=Tag.closet.icon("Ring_1"))
        add_static_texture(width=ring2_w, height=ring2_h, default_value=ring2_data, tag=Tag.closet.icon("Ring_2"))
        add_static_texture(width=shoulders_w, height=shoulders_h, default_value=shoulders_data, tag=Tag.closet.icon("Shoulders"))
        add_static_texture(width=throat_w, height=throat_h, default_value=throat_data, tag=Tag.closet.icon("Throat"))
        add_static_texture(width=waist_w, height=waist_h, default_value=waist_data, tag=Tag.closet.icon("Waist"))
        add_static_texture(width=feet_w, height=feet_h, default_value=feet_data, tag=Tag.closet.icon("Feet"))
        
def init_window_inventory_closet():
    wbtn = 98
    # Separate left and right equipment slots
    left_slots = ["Face", "Throat", "Body", "Hands", "Waist", "Feet", "Hand_1"]
    right_slots = ["Head", "Shoulders", "Armor", "Arms", "Ring_1", "Ring_2", "Hand_2"]
    with group(parent=Tag.closet.window()):
        with group(horizontal=False):
            with group(horizontal=True):
                # Left side
                with group(horizontal=False):
                    for slot in left_slots:
                        with group(horizontal=True):
                            add_image_button(Tag.closet.icon(slot), callback=q.cbh, user_data=["Closet Clear", slot, "Clear"], tag=Tag.closet.img(slot))
                            with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                                add_combo(width=wbtn, no_arrow_button=True, user_data=["Closet Equip", slot], callback=q.cbh, tag=Tag.closet.select(slot))
                # Center
                add_image(Tag.closet.icon("Figure"))
                # Right side
                with group(horizontal=False):
                    for slot in right_slots:
                        with group(horizontal=True):
                            with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                                add_combo(width=wbtn, no_arrow_button=True, user_data=["Closet Equip", slot], callback=q.cbh, tag=Tag.closet.select(slot))
                            add_image_button(Tag.closet.icon(slot), callback=q.cbh, user_data=["Closet Clear", slot, "Clear"], tag=Tag.closet.img(slot))

def init_ui():
    load_icons()
    init_window_skeleton()
    init_window_core()
    init_window_health()
    init_window_proficienices()
    init_window_characteristics()
    init_window_buffer()
    init_window_attributes()
    init_window_armor()
    init_window_initiatives()
    init_window_vision()
    init_window_speed()
    init_window_conditions()
    init_window_rest()
    init_window_skills()
    init_window_block()
    init_window_block_actions_weapons()
    init_window_inventory()
    init_window_inventory_backpack()
    init_window_inventory_bazaar()
    init_window_inventory_closet()
    init_window_wallet()