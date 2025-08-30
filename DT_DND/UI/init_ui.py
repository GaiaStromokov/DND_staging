from ui.upd_helper_import import *
from path_helper import get_path
tag = Tag()

def create_attribute_row(stat: str):
    wLabel = 40
    wVal = 30
    with group(horizontal=True):
        add_button(label=stat, enabled=False, width=wLabel)
        add_button(label="", enabled=False, width=wVal, tag=tag.atr.sum(stat))
        add_button(label="", enabled=False, width=wVal, tag=tag.atr.mod(stat))
    with popup(tag.atr.sum(stat), mousebutton=mvMouseButton_Left):
        add_button(label="Base", enabled=False, width=wLabel)
        add_combo(items=get.list_Base_Atr, default_value="", width=wVal, no_arrow_button=True, user_data=["Base Atr", stat], callback=q.cbh, tag=tag.atr.select(stat))
    with tooltip(tag.atr.sum(stat)):
        for source in ["Base", "Race", "Feat"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=wLabel)
                add_button(label="", enabled=False, width=25, tag=tag.atr.source(stat, source))

def create_skill_row(skill: str):
    wLabel = 113
    wMod = 30
    with group(horizontal=True):
        add_button(label=skill, enabled=False, width=wLabel, tag=tag.skill.label(skill))
        add_checkbox(default_value=False, enabled=False, user_data=[], callback=q.cbh, tag=tag.skill.toggle(skill))
        add_button(label="", enabled=False, width=wMod, tag=tag.skill.mod(skill))
    with tooltip(tag.skill.label(skill)): add_text(get.dict_Skill[skill]["Desc"])
    with tooltip(tag.skill.toggle(skill)):
        for source in ["Player", "Race", "Class", "BG", "Feat"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=50)
                add_checkbox(default_value=False, enabled=False, user_data=[], callback=q.cbh, tag=tag.skill.source(skill, source))

def create_pdescription():
    wBtn = sz.wLbtn
    tLabel = tag.pdesc.label()
    with popup(tLabel, mousebutton=mvMouseButton_Left):
        for item in get.list_Description:
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=wBtn)
                add_input_text(default_value="", on_enter=True, width=70, user_data=["Description", item], callback=q.cbh, tag=tag.pdesc.input(item))
    with tooltip(tLabel):
        for item in get.list_Description:
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=wBtn)
                add_text("", color=c_h2, wrap=400, tag=tag.pdesc.text(item))

def create_ideals(name: str):
    with popup(tag.char.label(name), mousebutton=mvMouseButton_Left):
        add_input_text(default_value="", on_enter=True, user_data=["Characteristic", name], callback=q.cbh, tag=tag.char.input(name))
    with tooltip(tag.char.label(name)):
        add_text("", tag=tag.char.text(name), wrap=400)

def create_proficiency_addons(tLabel: str, proficiency_map: dict):
    with popup(tLabel, mousebutton=mvMouseButton_Left):
        with group(horizontal=True):
            for category, items in proficiency_map.items():
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    add_text(category)
                    add_separator()
                    for item in items:
                        tToggle = tag.prof.toggle(category,item)
                        add_selectable(label=get.pName(item), default_value=False, user_data=["Player Prof Input", category, item], callback=q.cbh, tag=tToggle)
    with tooltip(tLabel):
        with group(horizontal=True):
            for category, items in proficiency_map.items():
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    add_text(category)
                    add_separator()
                    for item in items:
                        tText = tag.prof.text(category,item)
                        add_text(get.pName(item), color=(0, 0, 0), tag=tText)

def init_window_skeleton():
    with window(no_title_bar=True, no_close=True, autosize=True, tag="Main Window"):
        with group(horizontal=True):
            with group(horizontal=False):
                with group(horizontal=True):
                    with group(horizontal=False):
                        add_child_window(tag=tag.core.window(), width=sz.wCore, height=sz.hCore, border=True, no_scrollbar=True)
                        add_child_window(tag=tag.health.window(), width=sz.wHealth, height=sz.hHealth, border=True)
                        add_child_window(tag=tag.prof.window(), width=sz.wProficiencies, height=sz.hProficiencies, border=True)
                        add_child_window(tag=tag.char.window(), width=sz.wCharacter, height=sz.hCharacter, border=True)
                        add_child_window(tag=tag.buffer1.window(), width=sz.wBuffer2, height=sz.hBuffer2, border=True, no_scrollbar=True)
                    with group(horizontal=False):
                        add_child_window(tag=tag.atr.window(), width=sz.wAttributes, height=sz.hAttributes, border=True)
                        with group(horizontal=True):
                            add_child_window(tag=tag.init.window(), width=sz.wInitiative, height=sz.hInitiative, border=True)
                            add_child_window(tag=tag.ac.window(), width=sz.wAC, height=sz.hAC, border=True)
                        with group(horizontal=True):
                            add_child_window(tag=tag.vision.window(), width=sz.wVision, height=sz.hVision, border=True)
                            add_child_window(tag=tag.speed.window(), width=sz.wSpeed, height=sz.hSpeed, border=True)
                        add_child_window(tag=tag.cond.window(), width=sz.wConditions, height=sz.hConditions, border=True)
                        add_child_window(tag=tag.rest.window(), width=sz.wRest, height=sz.hRest, border=True)
                        add_child_window(tag=tag.buffer2.window(), width=sz.wBuffer1, height=sz.hBuffer1, border=True, no_scrollbar=True)
                    with group(horizontal=False):
                        add_child_window(tag=tag.skill.window(), width=sz.wSkill, height=sz.hSkill, border=True, no_scrollbar=True)
                with group(horizontal=False):
                    add_child_window(tag=tag.inve.window(), width=sz.wInventory, height=sz.hInventory + 12, border=True, no_scrollbar=True)
            with group(horizontal=False):
                add_child_window(tag=tag.block.window(), width=sz.wBlock, height=sz.hBlock, border=True, no_scrollbar=True)
                add_child_window(tag=tag.wallet.window(), width=sz.wWallet, height=sz.hWallet, border=True, no_scrollbar=True)

def init_window_wallet():
    with group(parent=tag.wallet.window()):
        with group(horizontal=True):
            for coin in get.list_Coins:
                with group(horizontal=True):
                    add_button(label=coin)
                    add_text("", color=c_h9, tag=tag.wallet.val(coin))

def init_window_core():
    wMax=sz.wCore-16
    wBtn=80
    wCombo = wMax-88
    with group(parent=tag.core.window()):
        add_button(label="Character info", enabled=False, width=wMax, height = sz.hHeader1)
        with group(horizontal=True):
            add_button(label="Level", enabled=False, width=50)
            add_button(label="<", user_data=["Level Input", -1], callback=q.cbh)
            add_button(label="", width=25, tag=tag.core.val("Level"))
            add_button(label=">", user_data=["Level Input", 1], callback=q.cbh)
            add_button(label="", enabled=False, width=55, tag=tag.core.val("PB"))
        with group(horizontal=True):
            add_button(label="Race", enabled=False, width=wBtn)
            add_combo(width=wCombo, no_arrow_button=True, user_data=["Core Race"], callback = q.cbh, tag=tag.core.select("Race"))
        with group(horizontal=True):
            add_button(label="Subrace", enabled=False, width=wBtn)
            add_combo(width=wCombo, no_arrow_button=True, user_data=["Core Subrace"], callback = q.cbh, tag=tag.core.select("Subrace"))
        with group(horizontal=True):
            add_button(label="Class", enabled=False, width=wBtn)
            add_combo(width=wCombo, no_arrow_button=True, user_data=["Core Class"], callback = q.cbh, tag=tag.core.select("Class"))
        with group(horizontal=True):
            add_button(label="Subclass", enabled=False, width=wBtn)
            add_combo(width=wCombo, no_arrow_button=True, user_data=["Core Subclass"], callback = q.cbh, tag=tag.core.select("Subclass"))
        with group(horizontal=True):
            add_button(label="Background", enabled=False, width=wBtn)
            add_combo(width=wCombo, no_arrow_button=True, user_data=["Core Background"], callback = q.cbh, tag=tag.core.select("Background"))

def init_window_attributes():
    with group(parent=tag.atr.window()):
        wMax=sz.wAttributes-16
        add_button(label="Attributes", enabled=False, width=wMax, height=sz.hHeader1)
        for stat in get.list_Atr:
            create_attribute_row(stat)

def init_window_health():
    wBtn = sz.wSbtn
    with group(parent=tag.health.window()):
        wMax=sz.wHealth-16
        hMax=sz.hHealth-15
        add_button(label="Health", enabled=False, width=wMax, height=sz.hHeader1)
        with group(horizontal=False):
            with group(horizontal=True):
                add_button(label="+", width=wBtn, user_data=["HP","HP", 1], callback=q.cbh)
                add_button(label="CUR / MAX", enabled=False, width=wMax-108, tag=tag.health.label())
                add_button(label="TEMP", enabled=False, width=wMax-150)
                add_button(label="+", width=wBtn, user_data=["HP","Temp", 1], callback=q.cbh)
            with group(horizontal=True):
                add_button(label="-", width=wBtn, user_data=["HP","HP", -1], callback=q.cbh)
                add_button(label="", enabled=False, width=wMax-108, tag=tag.health.val("HP"))
                add_button(label="", enabled=False, width=wMax-150, tag=tag.health.val("Temp"))
                add_button(label="-", width=wBtn, user_data=["HP","Temp", -1], callback=q.cbh)
    with popup(tag.health.label(), mousebutton=mvMouseButton_Left):
        add_button(label="Max", width=sz.wLbtn)
        add_input_int(default_value=0, width=90, user_data=["Player HP Mod"], callback=q.cbh, tag=tag.health.val("Max"))

def init_window_skills():
    wMax=sz.wSkill-16
    hMax=sz.wSkill-15
    with group(parent=tag.skill.window()):
        add_button(label="Skills", enabled=False, width=wMax, height=sz.hHeader1)
        for skill in get.list_Skill:
            create_skill_row(skill)

def init_window_initiatives():
    with group(parent=tag.init.window()):
        add_button(label="Init", enabled=False, width=sz.wMbtn, tag=tag.init.label())
        add_button(label="", enabled=False, width=sz.wMbtn, tag=tag.init.val())
    with tooltip(tag.init.label()):
        for source in ["Dex", "Race", "Class"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=40)
                add_button(label="", enabled=False, width=25, tag=tag.init.source(source))

def init_window_armor():
    with group(parent=tag.ac.window()):
        add_button(label="AC", enabled=False, width=sz.wMbtn, tag=tag.ac.label())
        add_button(label="", enabled=False, width=sz.wMbtn, tag=tag.ac.val())
    with tooltip(tag.ac.label()):
        for source in ["Base", "Dex", "Shield"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=tag.ac.source(source))

def init_window_vision():
    with group(parent=tag.vision.window()):
        add_button(label="Vision", enabled=False, width=sz.wMbtn, tag=tag.vision.label())
        add_button(label="", enabled=False, width=sz.wMbtn, tag=tag.vision.val())
    with tooltip(tag.vision.label()):
        for i in ["Dark", "Blind", "Tremor", "Tru"]:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=tag.vision.source(i))

def init_window_speed():
    with group(parent=tag.speed.window()):
        add_button(label="Speed", enabled=False, width=sz.wMbtn, tag=tag.speed.label())
        add_button(label="", enabled=False, width=sz.wMbtn, tag=tag.speed.val())
    with tooltip(tag.speed.label()):
        for i in ["Walk", "Climb", "Swim", "Fly", "Burrow"]:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=tag.speed.source(i))

def init_window_conditions():
    with group(parent=tag.cond.window()):
        add_button(label="Conditions", enabled=False, width=sz.wHeader2-72, height=26, tag=tag.cond.label())
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
        add_button(label="Short Rest", width=sz.wHeader2-72, height=30, user_data=["Short Rest"], callback=q.cbh, tag=tag.rest.button("Short"))
        add_button(label="Long Rest", width=sz.wHeader2-72, height=30, user_data=["Long Rest"], callback=q.cbh, tag=tag.rest.button("Long"))

def init_window_buffer():
    pass

def init_window_proficienices():
    wMax = sz.wProficiencies - 16
    hMax = sz.wProficiencies - 15
    btn_w = wMax - 101
    tWeapon = tag.prof.label("Weapon")
    tArmor = tag.prof.label("Armor")
    tTool = tag.prof.label("Tool")
    tLang = tag.prof.label("Lang")
    with group(parent=tag.prof.window()):
        add_button(label="Proficiencies", enabled=False, width=wMax, height=sz.hHeader1)
        with group(horizontal=True):
            add_button(label="Weapons", width=btn_w, tag=tWeapon)
            add_button(label="Armor", width=btn_w, tag=tArmor)
        with group(horizontal=True):
            add_button(label="Tools", width=btn_w, tag=tTool)
            add_button(label="Languages", width=btn_w, tag=tLang)
    create_proficiency_addons(tWeapon, {k: q.w.search(Tier=0, Slot="Weapon", Cat=k) for k in ["Simple", "Martial"]})
    create_proficiency_addons(tArmor, {"Armor": q.w.search(Tier=0, Slot=["Armor", "Shield"])})
    create_proficiency_addons(tTool, {"Artisan": get.list_Job, "Gaming": get.list_Game, "Musical": get.list_Music})
    create_proficiency_addons(tLang, {"Languages": get.list_Lang})

def init_window_characteristics():
    wMax = sz.wCharacter - 16
    hMax = sz.hCharacter - 15
    btn_w = wMax - 101
    with group(parent=tag.char.window()):
        add_button(label="Characteristics", enabled=False, width=wMax, height=sz.hHeader1, tag=tag.pdesc.label())
        with group(horizontal=True):
            add_button(label="Traits", width=btn_w, tag=tag.char.label("traits"))
            add_button(label="Ideals", width=btn_w, tag=tag.char.label("ideals"))
        with group(horizontal=True):
            add_button(label="Bonds", width=btn_w, tag=tag.char.label("bonds"))
            add_button(label="Flaws", width=btn_w, tag=tag.char.label("flaws"))
    for i in get.list_Ideals: create_ideals(i)
    create_pdescription()

def init_window_block():
    w1 = sz.wBlock - 16
    w2 = w1 - 16
    h1 = sz.hBlock - 40
    h2 = h1 - 15
    with group(parent=tag.block.window()):
        with tab_bar(tag=tag.block.tabbar()):
            with tab(label="Features/Traits"):
                with child_window(width=w1, height=h1, border=True):
                    add_separator(label="Race")
                    with child_window(auto_resize_y=True, width=w2, border=True, tag=tag.rfeature.sub()):
                        with group(horizontal=True):
                            add_text("Ability Score Increase: +1/+2", color=c_h1)
                            add_combo(items=get.list_Atr, default_value="", width=50, no_arrow_button=True, user_data=["Race Asi", 0], callback=q.cbh, tag=tag.rfeature.select("asi_0"))
                            add_combo(items=get.list_Atr, default_value="", width=50, no_arrow_button=True, user_data=["Race Asi", 1], callback=q.cbh, tag=tag.rfeature.select("asi_1"))
                            add_button(label="Clear", enabled=True, width=50, user_data=["Race Asi", "Clear"], callback=q.cbh, tag=tag.rfeature.button("asi_clear"))
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
                    with child_window(auto_resize_y=True, width=w2, border=True, tag=tag.wactions.window()):
                        add_separator(label="Weapons")

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
    h=sz.hInventory
    with group(parent=tag.inve.window()):
        with tab_bar():
            with tab(label="Closet"):
                add_child_window(height=h-28, border=True, no_scrollbar=True, tag=tag.closet.window())
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
                                add_child_window(height=sz.hInventory - 85, border=True, no_scrollbar=True, tag=tag.bazaar.window(equipment_type, rank))

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
        add_static_texture(width=figure_w, height=figure_h, default_value=figure_data, tag=tag.closet.icon("Figure"))
        add_static_texture(width=armor_w, height=armor_h, default_value=armor_data, tag=tag.closet.icon("Armor"))
        add_static_texture(width=arms_w, height=arms_h, default_value=arms_data, tag=tag.closet.icon("Arms"))
        add_static_texture(width=body_w, height=body_h, default_value=body_data, tag=tag.closet.icon("Body"))
        add_static_texture(width=face_w, height=face_h, default_value=face_data, tag=tag.closet.icon("Face"))
        add_static_texture(width=hands_w, height=hands_h, default_value=hands_data, tag=tag.closet.icon("Hands"))
        add_static_texture(width=head_w, height=head_h, default_value=head_data, tag=tag.closet.icon("Head"))
        add_static_texture(width=hand1_w, height=hand1_h, default_value=hand1_data, tag=tag.closet.icon("Hand_1"))
        add_static_texture(width=hand2_w, height=hand2_h, default_value=hand2_data, tag=tag.closet.icon("Hand_2"))
        add_static_texture(width=ring1_w, height=ring1_h, default_value=ring1_data, tag=tag.closet.icon("Ring_1"))
        add_static_texture(width=ring2_w, height=ring2_h, default_value=ring2_data, tag=tag.closet.icon("Ring_2"))
        add_static_texture(width=shoulders_w, height=shoulders_h, default_value=shoulders_data, tag=tag.closet.icon("Shoulders"))
        add_static_texture(width=throat_w, height=throat_h, default_value=throat_data, tag=tag.closet.icon("Throat"))
        add_static_texture(width=waist_w, height=waist_h, default_value=waist_data, tag=tag.closet.icon("Waist"))
        add_static_texture(width=feet_w, height=feet_h, default_value=feet_data, tag=tag.closet.icon("Feet"))

def init_window_inventory_closet():
    wbtn = 98
    left_slots = ["Face", "Throat", "Body", "Hands", "Waist", "Feet", "Hand_1"]
    right_slots = ["Head", "Shoulders", "Armor", "Arms", "Ring_1", "Ring_2", "Hand_2"]
    with group(parent=tag.closet.window()):
        with group(horizontal=False):
            with group(horizontal=True):
                with group(horizontal=False):
                    for slot in left_slots:
                        with group(horizontal=True):
                            add_image_button(tag.closet.icon(slot), callback=q.cbh, user_data=["Closet Clear", slot, "Clear"], tag=tag.closet.img(slot))
                            with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                                add_combo(width=wbtn, no_arrow_button=True, user_data=["Closet Equip", slot, "Modify"], callback=q.cbh, tag=tag.closet.select(slot))
                add_image(tag.closet.icon("Figure"))
                with group(horizontal=False):
                    for slot in right_slots:
                        with group(horizontal=True):
                            with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                                add_combo(width=wbtn, no_arrow_button=True, user_data=["Closet Equip", slot, "Modify"], callback=q.cbh, tag=tag.closet.select(slot))
                            add_image_button(tag.closet.icon(slot), callback=q.cbh, user_data=["Closet Clear", slot, "Clear"], tag=tag.closet.img(slot))

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