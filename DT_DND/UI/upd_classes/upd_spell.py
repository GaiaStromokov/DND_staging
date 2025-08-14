from ui.upd_helper_import import *

class upd_Cast:
    def __init__(self):
        self.spell_data = None

    def update(self):
        self.spell_data = q.pc.Class.spell_data
        self.update_stats()
        self.update_content()

    def update_stats(self):
        configure_item(tag.spell.text("Abil"), default_value=self.spell_data["abil"])
        configure_item(tag.spell.text("atk"), default_value=self.spell_data["atk"])
        configure_item(tag.spell.text("dc"), default_value=self.spell_data["dc"])

    def update_content(self):
        item_clear(tag.scast.main())
        with group(parent=tag.scast.main()):
            for level in range(0, self.spell_data["max_spell_level"] + 1):
                spell_list = q.db.Spell["Book"][0] if level == 0 else q.db.Spell["Prepared"][level]
                if not spell_list: continue
                with group(horizontal=False):
                    with group(horizontal=True):
                        add_text(get.list_spell_header[level], color=c_h1)
                        if level > 0:
                            for idx, value in enumerate(q.db.Spell["Slot"][level]):
                                add_checkbox(default_value=value, enabled=False, tag=tag.scast.toggle(level, idx))
                    
                    button_label = "Cast" if level > 0 else "Will"
                    for spell in spell_list:
                        with group(horizontal=True):
                            add_button(label=button_label, width=50, user_data=["Spell Cast", level, spell], callback=q.cbh, tag=tag.scast.button(level, spell))
                            add_text(spell, color=c_h2, tag=tag.scast.text(level, spell))
                            tooltip_tag = tag.scast.tooltip(level, spell)
                            item_delete(tooltip_tag)
                            with tooltip(tag.scast.text(level, spell), tag=tooltip_tag):
                                spell_detail(spell)
                    add_separator()

class upd_Learn:
    def __init__(self):
        self.spell_data = None

    def update(self):
        self.spell_data = q.pc.Class.spell_data
        self.update_stats()
        self.update_content()
        
    def update_stats(self):
        configure_item(tag.slearn.known("cantrip"), default_value=get.cantrips_known())
        configure_item(tag.slearn.available("cantrip"), default_value=self.spell_data["cantrips_available"])
        configure_item(tag.slearn.known("spell"), default_value=get.spells_known())
        configure_item(tag.slearn.available("spell"), default_value=self.spell_data["spells_available"])

    def update_content(self):
        for level in range(1, self.spell_data["max_spell_level"] + 1):
            available_spells = get.List_Spells(self.spell_data["Caster"], level)
            item_clear(tag.slearn.wlevel(level))
            if not available_spells: continue
            with group(parent=tag.slearn.wlevel(level)):
                for spell in available_spells:
                    is_known = spell in q.db.Spell["Book"][level]
                    add_selectable(label=spell, default_value=is_known, width=680, user_data=["Spell Learn", spell, level], callback=q.cbh, tag=tag.slearn.toggle(level, spell))
                    tooltip_tag = tag.slearn.tooltip(level, spell)
                    item_delete(tooltip_tag)
                    with tooltip(tag.slearn.toggle(level, spell), tag=tooltip_tag):
                        spell_detail(spell)

class upd_Prepare:
    def __init__(self):
        self.spell_data = None

    def update(self):
        self.spell_data = q.pc.Class.spell_data
        self.update_stats()
        self.update_content()

    def update_stats(self):
        configure_item(tag.sprepare.current(), default_value=get.spells_prepared())
        configure_item(tag.sprepare.available(), default_value=self.spell_data["prepared_available"])

    def update_content(self):
        for level in range(1, self.spell_data["max_spell_level"] + 1):
            item_clear(tag.sprepare.wlevel(level))
            known_spells = q.db.Spell["Book"][level]
            if not known_spells: continue
            with group(parent=tag.sprepare.wlevel(level)):
                for spell in known_spells:
                    is_prepared = spell in q.db.Spell["Prepared"][level]
                    add_selectable(label=spell, default_value=is_prepared, width=680, user_data=["Spell Prepare", spell, level], callback=q.cbh, tag=tag.sprepare.toggle(level, spell))
                    tooltip_tag = tag.sprepare.tooltip(level, spell)
                    item_delete(tooltip_tag)
                    with tooltip(tag.sprepare.toggle(level, spell), tag=tooltip_tag):
                        spell_detail(spell)

class upd_spell:
    def __init__(self):
        self.Cast = upd_Cast()
        self.Learn = upd_Learn()
        self.Prepare = upd_Prepare()

    def whole(self):
        if not get.valid_spellclass():
            item_delete(tag.spell.tab())
            return
        
        self.check_ui()
        self.Cast.update()
        self.Learn.update()
        self.Prepare.update()

    def check_ui(self):
        if does_item_exist(tag.spell.tab()):
            return

        w1 = size.w_block - 16
        w2 = w1 - 18
        h1 = size.h_block - 40
        h2 = h1 - 95

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
                                for i in range(1, 10):
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
                                for i in range(1, 10):
                                    with tab(label=f"Level {i}"):
                                        add_child_window(auto_resize_y=True, width=w2-20, height=h2-40, no_scrollbar=True, border=True, tag=tag.sprepare.wlevel(i))