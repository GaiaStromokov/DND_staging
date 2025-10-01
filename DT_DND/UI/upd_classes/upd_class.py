from ui.upd_helper_import import *

tag = Tag()
class upd_class:
    def __init__(self):
        self.parent = tag.cfeature.main()
    
    def Whole(self):
        self.sub()
        self.main()
        
    def main(self):
        item_clear(self.parent)
        Class = get.Class()
        Subclass = get.Subclass()
        
        if hasattr(self, Class):
            method_name = Class
            getattr(self, method_name)()

        if hasattr(self, f"{Class}_{Subclass}"):
            method_name = f"{Class}_{Subclass}"
            getattr(self, method_name)()
            
    def sub(self):
        item_clear(tag.cfeature.sub())
        with group(parent=tag.cfeature.sub()):
            with group(horizontal=True):
                add_text("Skill Select", color=c_h1)
                for idx, key in enumerate(q.db.Class["Skill Select"]):
                    add_combo(items=get.dict_Class_Skills[q.db.Core.C], default_value=key,  width=100, no_arrow_button=True, user_data=["Class Skill Select",idx], callback=q.cbh, tag=tag.cfeature.toggle("skill_select",idx))
                add_button(label = "Clear", user_data=["Class Skill Select", "Clear"], callback=q.cbh, tag=tag.cfeature.button("skill_select","Clear"))

    def standard(self, name, descriptions):
        gen = tgen(name)
        t_header = tag.cfeature.header(gen.tag)
        desc_tags = [tag.cfeature.text(gen.tag, f"{i+1}") for i, _ in enumerate(descriptions)]

        with group(parent=self.parent):
            add_text(gen.name, color=c_h1, tag=t_header)
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=sz.wrap, tag=desc_tags[i])

    def standard_toggle(self, name, descriptions):
        gen = tgen(name)
        cdata = q.db.Class["Abil"][gen.tag]
        t_header = tag.cfeature.header(gen.tag)
        desc_tags = [tag.cfeature.text(gen.tag, f"{i+1}") for i, _ in enumerate(descriptions)]

        with group(parent=self.parent):
            with group(horizontal=True):
                add_text(gen.name, color=c_h1, tag=t_header)
                for idx, val in enumerate(cdata["Use"]):
                    t_toggle = tag.cfeature.toggle(gen.tag, idx)
                    add_checkbox(default_value=val, enabled=True, user_data=["Class Use", gen.tag, idx], callback=q.cbh, tag=t_toggle)

            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=sz.wrap, tag=desc_tags[i])

    def standard_multi_choice(self, name):
        gen = tgen(name)
        cdata = q.db.Class["Abil"][gen.tag]
        t_header = tag.cfeature.header(gen.tag)
        t_popup = tag.cfeature.popup(gen.tag)

        with group(parent=self.parent):
            add_text(gen.name, color=c_h1, tag=t_header)

            item_delete(t_popup)
            with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                for idx, value in enumerate(cdata["Select"]):
                    t_select = tag.cfeature.select(gen.tag, idx)
                    add_combo(items=get.list_Fighting_Styles, default_value=value, width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Abil Select", gen.tag, idx], tag=t_select)

            for item in cdata["Select"]:
                if item != "":
                    add_text(item, color=c_h2)
                    add_text(get.get_Fighting_Style(item), color=c_text, wrap=sz.wrap)

    def Empty(self):
        pass

    def Fighter(self):
        data = q.dbm.Class.g.Abil
        
        ca = "Fighting_Style"
        if ca in data:
            self.standard_multi_choice(ca)

        ca = "Second_Wind"
        if ca in data:
            level = q.dbm.Core.g.L
            descriptions = [f"(bonus) regain 1d10+{level} HP"]
            self.standard_toggle(ca, descriptions)

        ca = "Action_Surge"
        if ca in data:
            descriptions = ["(free) take one additional action."]
            self.standard_toggle(ca, descriptions)

        ca = "Extra_Attack"
        if ca in data:
            level = q.dbm.Core.g.L
            extra_attack_num_map = [0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,4]
            extra_attack_num = extra_attack_num_map[level] if level < len(extra_attack_num_map) else 4
            descriptions = [f"You can attack {extra_attack_num+1} times whenever you take the Attack action on your turn."]
            self.standard(ca, descriptions)

        ca = "Indomitable"
        if ca in data:
            descriptions = ["You can reroll a saving throw that you fail. If you do so, you must use the new roll."]
            self.standard_toggle(ca, descriptions)

    def Fighter_Champion(self):
        data = q.dbm.Class.g.Abil

        ca = "Improved_Critical"
        if ca in data:
            descriptions = ["Your weapon attacks score a critical hit on a roll of 19 or 20."]
            self.standard(ca, descriptions)

        ca = "Superior_Critical"
        if ca in data:
            descriptions = ["Your weapon attacks score a critical hit on a roll of 18-20."]
            self.standard(ca, descriptions)

        ca = "Remarkable_Athlete"
        if ca in data:
            descriptions = [f"You can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier."]
            self.standard(ca, descriptions)

        ca = "Survivor"
        if ca in data:
            descriptions = [f"At the start of each of your turns, you regain {5 + q.db.Atr['CON']['Mod']} hit points if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points."]
            self.standard(ca, descriptions)

    def Fighter_BattleMaster(self):
        data = q.dbm.Class.Abil

        ca = "Combat_Superiority"
        if ca in data:
            gen = tgen(ca)
            cdata = data[gen.name]
            level = q.dbm.Core.g.L
            die = [0,0,0,8,8,8,8,8,8,10,10,10,10,10,10,10,10,12,12,12][level]
            t_header = tag.cfeature.header(gen.tag)
            t_popup = tag.cfeature.popup(gen.tag)

            with group(parent=self.parent):
                with group(horizontal=True):
                    add_text(f"{gen.name} (d{die})", color=c_h1, tag=t_header)
                    item_delete(t_popup)
                    with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                        for idx, value in enumerate(cdata["Select"]):
                            t_select = tag.cfeature.select(gen.tag, idx)
                            add_combo(items=get.list_Maneuvers, default_value=value, width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Abil Select", gen.tag, idx], tag=t_select)
                        for idx, value in enumerate(cdata["Use"]):
                            t_toggle = tag.cfeature.toggle(gen.tag, idx)
                            add_checkbox(default_value=value, enabled=True, callback=q.cbh, user_data=["Class Use", gen.tag, idx], tag=t_toggle)

                for item in cdata["Select"]:
                    if item:
                        item_tag = item.replace(" ", "_")
                        t_item = tag.cfeature.text(gen.tag, item_tag)
                        t_tooltip = tag.cfeature.tooltip(gen.tag, item_tag)
                        add_text(item, color=c_h2, tag=t_item)
                        item_delete(t_tooltip)
                        with tooltip(t_item, tag=t_tooltip):
                            add_text(get.dict_Maneuver_map[item], color=c_text, wrap=sz.wrap)

        ca = "Student_of_War"
        if ca in data:
            gen = tgen(ca)
            cdata = data[gen.tag]
            t_header = tag.cfeature.header(gen.tag)
            t_popup = tag.cfeature.popup(gen.tag)
            t_select = tag.cfeature.select(gen.tag, 0)
            with group(parent=self.parent):
                add_text(gen.name, color=c_h1, tag=t_header)
                item_delete(t_popup)
                with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                    add_combo(items=get.list_Student_of_War_Profs, default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Abil Select", gen.tag, 0], tag=t_select)

        ca = "Relentless"
        if ca in data:
            descriptions = ["When you roll initiative and have no superiority dice remaining, you regain 1 superiority die."]
            self.standard(ca, descriptions)

    def Fighter_EldritchKnight(self):
        data = q.db.Class["Abil"]

        ca = "Weapon_Bond"
        if ca in data:
            gen = tgen(ca)
            t_header = tag.cfeature.header(gen.tag)
            t_tooltip = tag.cfeature.tooltip(gen.tag)
            descriptions = [
                "Learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond.",
                "Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand.",
                "You can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two."
            ]
            with group(parent=self.parent):
                add_text(gen.name, color=c_h1, tag=t_header)
                item_delete(t_tooltip)
                with tooltip(t_header, tag=t_tooltip):
                    for desc in descriptions:
                        add_text(desc, color=c_text, wrap=sz.wrap)

        ca = "War_Magic"
        if ca in data:
            descriptions = ["When you use your action to cast a cantrip, you can make one weapon attack as a bonus action."]
            self.standard(ca, descriptions)

        ca = "Improved_War_Magic"
        if ca in data:
            descriptions = ["When you use your action to cast a spell, you can make one weapon attack as a bonus action."]
            self.standard(ca, descriptions)

        ca = "Eldritch_Strike"
        if ca in data:
            descriptions = ["When you hit a creature with a weapon attack, that creature has disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn."]
            self.standard(ca, descriptions)

        ca = "Arcane_Charge"
        if ca in data:
            descriptions = ["When you use your Action Surge, you can teleport up to 30 feet to an unoccupied space you can see. You can teleport before or after the additional action."]
            self.standard(ca, descriptions)

    def Fighter_Samurai(self):
        data = q.db.Class["Abil"]

        ca = "Bonus_Proficiency"
        if ca in data:
            gen = tgen(ca)
            cdata = data[gen.tag]
            t_header = tag.cfeature.header(gen.tag)
            t_popup = tag.cfeature.popup(gen.tag)
            t_select = tag.cfeature.select(gen.tag, 0)
            with group(parent=self.parent):
                add_text(gen.name, color=c_h1, tag=t_header)
                item_delete(t_popup)
                with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                    add_combo(items=get.list_Fighter_Samuri_Bonus_Proficiency, default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Abil Select", gen.tag, 0], tag=t_select)

        ca = "Fighting_Spirit"
        if ca in data:
            descriptions = ["As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of the current turn. When you do so, you also gain 5 temporary hit points."]
            self.standard_toggle(ca, descriptions)

        ca = "Elegant_Courtier"
        if ca in data:
            descriptions = [f"You can add your Wisdom modifier to Persuasion checks."]
            self.standard(ca, descriptions)

        ca = "Tireless_Spirit"
        if ca in data:
            descriptions = ["When you roll initiative and have no uses of Fighting Spirit remaining, you regain one use."]
            self.standard(ca, descriptions)

        ca = "Rapid_Strike"
        if ca in data:
            descriptions = ["If you take the Attack action on your turn and have advantage on an attack roll against one of the targets, you can forgo the advantage for that roll to make one additional weapon attack against that target, as part of the same action. You can do so no more than once per turn."]
            self.standard(ca, descriptions)

        ca = "Strength_before_Death"
        if ca in data:
            descriptions = ["If you take damage that would reduce you to 0 hit points, you can use your reaction to delay falling unconscious, and you can immediately take an extra turn, interrupting the current turn."]
            self.standard_toggle(ca, descriptions)
    def Wizard(self):
        data = q.db.Class["Abil"]

        ca = "Spellcasting"
        if ca in data:
            gen = tgen(ca)
            t_header = tag.cfeature.header(gen.tag)
            t_tooltip = tag.cfeature.tooltip(gen.tag)
            desc1 = "Must be spell level you can prepare, Costs 50 gp + 2 hours per spell level"
            desc2 = "To backup own spellbook, Costs 10 gp + 1 hour per spell level"
            with group(parent=self.parent):
                add_text(gen.name, color=c_h1, tag=t_header)
                item_delete(t_tooltip)
                with tooltip(t_header, tag=t_tooltip):
                    add_text("Copying External Spells", color=c_h1)
                    add_text(desc1, color=c_text, wrap=sz.wrap)
                    add_text("Copying Internal Spells", color=c_h1)
                    add_text(desc2, color=c_text, wrap=sz.wrap)

        ca = "Arcane_Recovery"
        if ca in data:
            descriptions = [f"Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher."]
            self.standard_toggle(ca, descriptions)

        ca = "Spell_Mastery"
        if ca in data:
            gen = tgen(ca)
            cdata = data[gen.tag]
            t_header = tag.cfeature.header(gen.tag)
            t_popup = tag.cfeature.popup(gen.tag)
            with group(parent=self.parent):
                add_text(gen.name, color=c_h1, tag=t_header)
                item_delete(t_popup)
                with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                    add_combo(items=q.db.Spell["Book"][1], default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", gen.tag, 0], tag=tag.cfeature.select(ca,0))
                    add_combo(items=q.db.Spell["Book"][2], default_value=cdata["Select"][1], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", gen.tag, 1], tag=tag.cfeature.select(ca,1))
                for idx, spell in enumerate(cdata["Select"]):
                    if spell != "":
                        spell_tag = spell.replace(" ", "_")
                        t_spell = tag.cfeature.text(ca, spell_tag)
                        t_tooltip = tag.cfeature.tooltip(ca, spell_tag)
                        with group(horizontal=True):
                            add_text(spell, color=c_h2, tag=t_spell)
                            add_checkbox(default_value=cdata["Use"][idx], enabled=True, callback=q.cbh, user_data=["Class Use", gen.tag, idx], tag=tag.cfeature.toggle(gen.tag,idx))
                        item_delete(t_tooltip)
                        with tooltip(t_spell, tag=t_tooltip):
                            spell_detail(spell)

        ca = "Signature_Spells"
        if ca in data:
            gen = tgen(ca)
            cdata = data[gen.tag]
            t_header = tag.cfeature.header(gen.tag)
            t_popup = tag.cfeature.popup(gen.tag)
            with group(parent=self.parent):
                add_text(gen.name, color=c_h1, tag=t_header)
                item_delete(t_popup)
                with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                    add_combo(items=q.db.Spell["Book"][3], default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", gen.tag, 0], tag=tag.cfeature.select(gen.tag,0))
                    add_combo(items=q.db.Spell["Book"][3], default_value=cdata["Select"][1], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", gen.tag, 1], tag=tag.cfeature.select(gen.tag,1))
                for idx, spell in enumerate(cdata["Select"]):
                    if spell != "":
                        spell_tag = spell.replace(" ", "_")
                        t_spell = tag.cfeature.text(ca, spell_tag)
                        t_tooltip = tag.cfeature.tooltip(ca, spell_tag)
                        with group(horizontal=True):
                            add_text(spell, color=c_h2, tag=t_spell)
                            add_checkbox(default_value=cdata["Use"][idx], enabled=True, callback=q.cbh, user_data=["Class Use", gen.tag, idx], tag=tag.cfeature.toggle(gen.tag,idx))
                        item_delete(t_tooltip)
                        with tooltip(t_spell, tag=t_tooltip):
                            spell_detail(spell)

    def Wizard_Abjuration(self):
        data = q.dbm.Class.g.Abil

        ca = "Abjuration_Savant"
        if ca in data:
            descriptions = ["The gold and time you must spend to copy an abjuration spell into your spellbook is halved."]
            self.standard(ca, descriptions)

        ca = "Arcane_Ward"
        if ca in data:
            gen = tgen(ca)
            cdata = data[gen.tag]
            description = "On casting a 1st-level+ Abjuration spell, create a magical ward that lasts until a long rest. It can regain HP equal to twice the spell level on subsequent Abjuration spell casts."
            t_header = tag.cfeature.header(gen.tag)
            t_hp = tag.cfeature.button(gen.tag, "HP")
            t_desc = tag.cfeature.text(gen.tag, "Desc")
            with group(parent=self.parent):
                with group(horizontal=True):
                    add_text(gen.name, color=c_h1, tag=t_header)
                    add_checkbox(default_value=cdata["Use"][0], enabled=True, callback=q.cbh, user_data=["Class Use", gen.tag, 0], tag=tag.cfeature.toggle(gen.tag, 0))
                    add_button(label="Ward HP", enabled=False)
                    add_button(label=f"{cdata['HP']['Current']} / {cdata['HP']['Max']}", enabled=False, tag=t_hp)
                    add_button(label="-", user_data=["Arcane Ward", -1], callback=q.cbh)
                    add_button(label="+", user_data=["Arcane Ward", 1], callback=q.cbh)
                add_text(description, color=c_text, wrap=sz.wrap, tag=t_desc)

        ca = "Projected_Ward"
        if ca in data:
            descriptions = ["(reaction) When a creature within 30 ft is hit, use your Arcane Ward to absorb the damage."]
            self.standard(ca, descriptions)

        ca = "Improved_Abjuration"
        if ca in data:
            descriptions = [f"When an Abjuration spell requires you to make an ability check, add your proficiency bonus ({q.db.Core.PB}) to that check."]
            self.standard(ca, descriptions)

        ca = "Spell_Resistance"
        if ca in data:
            descriptions = ["Gain advantage on saving throws against spells and resistance to spell damage."]
            self.standard(ca, descriptions)

    def Wizard_Conjuration(self):
        data = q.dbm.Class.g.Abil

        ca = "Conjuration_Savant"
        if ca in data:
            descriptions = ["The gold and time you must spend to copy a conjuration spell into your spellbook is halved."]
            self.standard(ca, descriptions)

        ca = "Minor_Conjuration"
        if ca in data:
            descriptions = ["(action) Conjure a non-magical item (up to 3ft, 10 lbs). It lasts for 1 hour or until it takes damage."]
            self.standard(ca, descriptions)

        ca = "Benign_Transportation"
        if ca in data:
            descriptions = ["(action) Teleport up to 30ft or swap places with a willing creature. Usable again after a long rest or casting a Level 1+ conjuration spell."]
            self.standard(ca, descriptions)

        ca = "Focused_Conjuration"
        if ca in data:
            descriptions = ["Your concentration on conjuration spells can't be broken as a result of taking damage."]
            self.standard(ca, descriptions)

        ca = "Durable_Summons"
        if ca in data:
            descriptions = ["Any creature you summon or create with a conjuration spell has 30 temporary hit points."]
            self.standard(ca, descriptions)
