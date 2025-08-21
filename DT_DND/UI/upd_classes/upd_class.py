from ui.upd_helper_import import *

tag = Tag()

class upd_class:
    def __init__(self):
        self.parent = tag.cfeature.main()
    
    def whole(self):
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
        a, t = gen_abil(name)
        t_header = tag.cfeature.header(t)
        desc_tags = [tag.cfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=sz.wrap, tag=desc_tags[i])

    def standard_toggle(self, name, descriptions):
        a, t = gen_abil(name)
        cdata = q.db.Class["Abil"][a]
        t_header = tag.cfeature.header(t)
        desc_tags = [tag.cfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]

        with group(parent=self.parent):
            with group(horizontal=True):
                add_text(a, color=c_h1, tag=t_header)
                for idx, val in enumerate(cdata["Use"]):
                    t_toggle = tag.cfeature.toggle(t, idx)
                    add_checkbox(default_value=val, enabled=True, user_data=["Class Use", a, idx], callback=q.cbh, tag=t_toggle)

            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=sz.wrap, tag=desc_tags[i])

    def standard_multi_choice(self, name):
        a, t = gen_abil(name)
        cdata = q.db.Class["Abil"][a]
        t_header = tag.cfeature.header(t)
        t_popup = tag.cfeature.popup(t)

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)

            item_delete(t_popup)
            with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                for idx, value in enumerate(cdata["Select"]):
                    t_select = tag.cfeature.select(t, idx)
                    add_combo(items=get.list_Fighting_Styles, default_value=value, width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", a, idx], tag=t_select)

            for item in cdata["Select"]:
                if item != "":
                    add_text(item, color=c_h2)
                    add_text(get.get_Fighting_Style(item), color=c_text, wrap=sz.wrap)

    def Empty(self):
        pass

    def Fighter(self):
        data = q.db.Class["Abil"]

        if "Fighting Style" in data:
            self.standard_multi_choice("Fighting Style")

        if "Second Wind" in data:
            Second_Wind_descriptions = [f"(bonus) regain 1d10+{q.db.Core.L} HP"]
            self.standard_toggle("Second Wind", Second_Wind_descriptions)

        if "Action Surge" in data:
            Action_Surge_descriptions = ["(free) take one additional action."]
            self.standard_toggle("Action Surge", Action_Surge_descriptions)

        if "Extra Attack" in data:
            extra_attack_num_map = [0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,4]
            extra_attack_num = extra_attack_num_map[q.db.Core.L] if q.db.Core.L < len(extra_attack_num_map) else 4
            Extra_Attack_descriptions = [f"You can attack {extra_attack_num+1} times whenever you take the Attack action on your turn."]
            self.standard("Extra Attack", Extra_Attack_descriptions)

        if "Indomitable" in data:
            Indomitable_descriptions = ["You can reroll a saving throw that you fail. If you do so, you must use the new roll."]
            self.standard_toggle("Indomitable", Indomitable_descriptions)

    def Fighter_Champion(self):
        data = q.db.Class["Abil"]

        if "Improved Critical" in data:
            Improved_Critical_descriptions = ["Your weapon attacks score a critical hit on a roll of 19 or 20."]
            self.standard("Improved Critical", Improved_Critical_descriptions)

        if "Superior Critical" in data:
            Superior_Critical_descriptions = ["Your weapon attacks score a critical hit on a roll of 18-20."]
            self.standard("Superior Critical", Superior_Critical_descriptions)

        if "Remarkable Athlete" in data:
            Remarkable_Athlete_descriptions = [f"You can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier."]
            self.standard("Remarkable Athlete", Remarkable_Athlete_descriptions)

        if "Survivor" in data:
            Survivor_descriptions = [f"At the start of each of your turns, you regain {5 + q.db.Atr['CON']['Mod']} hit points if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points."]
            self.standard("Survivor", Survivor_descriptions)

    def Fighter_BattleMaster(self):
        data = q.db.Class["Abil"]

        if "Combat Superiority" in data:
            a, t = gen_abil("Combat Superiority", 1)
            cdata = data[a]
            die = [0,0,0,8,8,8,8,8,8,10,10,10,10,10,10,10,10,12,12,12][q.db.Core.L]
            t_header = tag.cfeature.header(t)
            t_popup = tag.cfeature.popup(t)

            with group(parent=self.parent):
                with group(horizontal=True):
                    add_text(f"{a} (d{die})", color=c_h1, tag=t_header)
                    item_delete(t_popup)
                    with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                        for idx, value in enumerate(cdata["Select"]): 
                            t_select = tag.cfeature.select(t, idx)
                            add_combo(items=get.list_Maneuvers, default_value=value, width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", a, idx], tag=t_select)
                    for idx, value in enumerate(cdata["Use"]):
                        t_toggle = tag.cfeature.toggle(t, idx)
                        add_checkbox(default_value=value, enabled=True, callback=q.cbh, user_data=["Class Use", a, idx], tag=t_toggle)
                
                for item in cdata["Select"]:
                    if item:
                        item_tag = item.replace(" ", "_")
                        t_item = tag.cfeature.text(t, item_tag)
                        t_tooltip = tag.cfeature.tooltip(t, item_tag)
                        add_text(item, color=c_h2, tag=t_item)
                        item_delete(t_tooltip)
                        with tooltip(t_item, tag=t_tooltip):
                            add_text(get.dict_Maneuver_map[item], color=c_text, wrap=sz.wrap)
        
        if "Student of War" in data:
            a, t = gen_abil("Student of War", 1)
            cdata = data[a]
            t_header = tag.cfeature.header(t)
            t_popup = tag.cfeature.popup(t)
            t_select = tag.cfeature.select(t, 0)
            
            with group(parent=self.parent):
                add_text(a, color=c_h1, tag=t_header)
                item_delete(t_popup)
                with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                    add_combo(items=get.list_Student_of_War_Profs, default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", a, 0], tag=t_select)

        if "Relentless" in data:
            Relentless_descriptions = ["When you roll initiative and have no superiority dice remaining, you regain 1 superiority die."]
            self.standard("Relentless", Relentless_descriptions)
    def Fighter_EldritchKnight(self):
        data = q.db.Class["Abil"]

        if "Weapon Bond" in data:
            a, t = gen_abil("Weapon Bond", 1)
            t_header = tag.cfeature.header(t)
            t_tooltip = tag.cfeature.tooltip(t)
            
            Weapon_Bond_descriptions = [
                "Learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond.",
                "Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand.",
                "You can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two."
            ]
            
            with group(parent=self.parent):
                add_text(a, color=c_h1, tag=t_header)
                item_delete(t_tooltip)
                with tooltip(t_header, tag=t_tooltip):
                    for desc in Weapon_Bond_descriptions:
                        add_text(desc, color=c_text, wrap=sz.wrap)
        
        if "War Magic" in data:
            War_Magic_descriptions = ["When you use your action to cast a cantrip, you can make one weapon attack as a bonus action."]
            self.standard("War Magic", War_Magic_descriptions)

        if "Improved War Magic" in data:
            Improved_War_Magic_descriptions = ["When you use your action to cast a spell, you can make one weapon attack as a bonus action."]
            self.standard("Improved War Magic", Improved_War_Magic_descriptions)

        if "Eldritch Strike" in data:
            Eldritch_Strike_descriptions = ["When you hit a creature with a weapon attack, that creature has disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn."]
            self.standard("Eldritch Strike", Eldritch_Strike_descriptions)

        if "Arcane Charge" in data:
            Arcane_Charge_descriptions = ["When you use your Action Surge, you can teleport up to 30 feet to an unoccupied space you can see. You can teleport before or after the additional action."]
            self.standard("Arcane Charge", Arcane_Charge_descriptions)

    def Fighter_Samurai(self):
        data = q.db.Class["Abil"]

        if "Bonus Proficiency" in data:
            a, t = gen_abil("Bonus Proficiency", 1)
            cdata = data[a]
            t_header = tag.cfeature.header(t)
            t_popup = tag.cfeature.popup(t)
            t_select = tag.cfeature.select(t, 0)
            
            with group(parent=self.parent):
                add_text(a, color=c_h1, tag=t_header)
                item_delete(t_popup)
                with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                    add_combo(items=get.list_Fighter_Samuri_Bonus_Proficiency, default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", a, 0], tag=t_select)

        if "Fighting Spirit" in data:
            Fighting_Spirit_descriptions = ["As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of the current turn. When you do so, you also gain 5 temporary hit points."]
            self.standard_toggle("Fighting Spirit", Fighting_Spirit_descriptions)

        if "Elegant Courtier" in data:
            Elegant_Courtier_descriptions = [f"You can add your Wisdom modifier to Persuasion checks."]
            self.standard("Elegant Courtier", Elegant_Courtier_descriptions)

        if "Tireless Spirit" in data:
            Tireless_Spirit_descriptions = ["When you roll initiative and have no uses of Fighting Spirit remaining, you regain one use."]
            self.standard("Tireless Spirit", Tireless_Spirit_descriptions)

        if "Rapid Strike" in data:
            Rapid_Strike_descriptions = ["If you take the Attack action on your turn and have advantage on an attack roll against one of the targets, you can forgo the advantage for that roll to make one additional weapon attack against that target, as part of the same action. You can do so no more than once per turn."]
            self.standard("Rapid Strike", Rapid_Strike_descriptions)

        if "Strength before Death" in data:
            Strength_before_Death_descriptions = ["If you take damage that would reduce you to 0 hit points, you can use your reaction to delay falling unconscious, and you can immediately take an extra turn, interrupting the current turn."]
            self.standard_toggle("Strength before Death", Strength_before_Death_descriptions)
        
                    
    def Wizard(self):
        data = q.db.Class["Abil"]

        if "Spellcasting" in data:
            a, t = gen_abil("Spellcasting", 1)
            t_header = tag.cfeature.header(t)
            t_tooltip = tag.cfeature.tooltip(t)
            
            desc1 = "Must be spell level you can prepare, Costs 50 gp + 2 hours per spell level"
            desc2 = "To backup own spellbook, Costs 10 gp + 1 hour per spell level"

            with group(parent=self.parent):
                add_text(a, color=c_h1, tag=t_header)
                item_delete(t_tooltip)
                with tooltip(t_header, tag=t_tooltip):
                    add_text("Copying External Spells", color=c_h1)
                    add_text(desc1, color=c_text, wrap=sz.wrap)
                    add_text("Copying Internal Spells", color=c_h1)
                    add_text(desc2, color=c_text, wrap=sz.wrap)

        if "Arcane Recovery" in data:
            Arcane_Recovery_descriptions = [f"Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher."]
            self.standard_toggle("Arcane Recovery", Arcane_Recovery_descriptions)

        if "Spell Mastery" in data:
            a, t = gen_abil("Spell Mastery", 1)
            cdata = data[a]
            t_header = tag.cfeature.header(t)
            t_popup = tag.cfeature.popup(t)

            with group(parent=self.parent):
                add_text(a, color=c_h1, tag=t_header)
                item_delete(t_popup)
                with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                    add_combo(items=q.db.Spell["Book"][1], default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", a, 0], tag=tag.cfeature.select(t,0))
                    add_combo(items=q.db.Spell["Book"][2], default_value=cdata["Select"][1], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", a, 1], tag=tag.cfeature.select(t,1))
                
                for idx, spell in enumerate(cdata["Select"]):
                    if spell != "":
                        spell_tag = spell.replace(" ", "_")
                        t_spell = tag.cfeature.text(t, spell_tag)
                        t_tooltip = tag.cfeature.tooltip(t, spell_tag)
                        with group(horizontal=True):
                            add_text(spell, color=c_h2, tag=t_spell)
                            add_checkbox(default_value=cdata["Use"][idx], enabled=True, callback=q.cbh, user_data=["Class Use", a, idx], tag=tag.cfeature.toggle(t,idx))
                        item_delete(t_tooltip)
                        with tooltip(t_spell, tag=t_tooltip):
                            spell_detail(spell)

        if "Signature Spells" in data:
            a, t = gen_abil("Signature Spells", 1)
            cdata = data[a]
            t_header = tag.cfeature.header(t)
            t_popup = tag.cfeature.popup(t)
            
            with group(parent=self.parent):
                add_text(a, color=c_h1, tag=t_header)
                item_delete(t_popup)
                with popup(t_header, mousebutton=mvMouseButton_Left, tag=t_popup):
                    add_combo(items=q.db.Spell["Book"][3], default_value=cdata["Select"][0], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", a, 0], tag=tag.cfeature.select(t,0))
                    add_combo(items=q.db.Spell["Book"][3], default_value=cdata["Select"][1], width=80, no_arrow_button=True, callback=q.cbh, user_data=["Class Select", a, 1], tag=tag.cfeature.select(t,1))
                
                for idx, spell in enumerate(cdata["Select"]):
                    if spell != "":
                        spell_tag = spell.replace(" ", "_")
                        t_spell = tag.cfeature.text(t, spell_tag)
                        t_tooltip = tag.cfeature.tooltip(t, spell_tag)
                        with group(horizontal=True):
                            add_text(spell, color=c_h2, tag=t_spell)
                            add_checkbox(default_value=cdata["Use"][idx], enabled=True, callback=q.cbh, user_data=["Class Use", a, idx], tag=tag.cfeature.toggle(t,idx))
                        item_delete(t_tooltip)
                        with tooltip(t_spell, tag=t_tooltip):
                            spell_detail(spell)

    def Wizard_Abjuration(self):
        data = q.db.Class["Abil"]

        if "Abjuration Savant" in data:
            Abjuration_Savant_descriptions = ["The gold and time you must spend to copy an abjuration spell into your spellbook is halved."]
            self.standard("Abjuration Savant", Abjuration_Savant_descriptions)

        if "Arcane Ward" in data:
            a, t = gen_abil("Arcane Ward", 1)
            cdata = data[a]
            description = "On casting a 1st-level+ Abjuration spell, create a magical ward that lasts until a long rest. It can regain HP equal to twice the spell level on subsequent Abjuration spell casts."
            t_header = tag.cfeature.header(t)
            t_hp = tag.cfeature.button(t, "HP")
            t_desc = tag.cfeature.text(t, "Desc")

            with group(parent=self.parent):
                with group(horizontal=True):
                    add_text(a, color=c_h1, tag=t_header)
                    add_checkbox(default_value=cdata["Use"][0], enabled=True, callback=q.cbh, user_data=["Class Use", a, 0], tag=tag.cfeature.toggle(t, 0))
                    add_button(label="Ward HP", enabled=False)
                    add_button(label=f"{cdata['HP']['Current']} / {cdata['HP']['Max']}", enabled=False, tag=t_hp)
                    add_button(label="-", user_data=["Arcane Ward", -1], callback=q.cbh)
                    add_button(label="+", user_data=["Arcane Ward", 1], callback=q.cbh)
                add_text(description, color=c_text, wrap=sz.wrap, tag=t_desc)

        if "Projected Ward" in data:
            Projected_Ward_descriptions = ["(reaction) When a creature within 30 ft is hit, use your Arcane Ward to absorb the damage."]
            self.standard("Projected Ward", Projected_Ward_descriptions)

        if "Improved Abjuration" in data:
            Improved_Abjuration_descriptions = [f"When an Abjuration spell requires you to make an ability check, add your proficiency bonus ({q.db.Core.PB}) to that check."]
            self.standard("Improved Abjuration", Improved_Abjuration_descriptions)

        if "Spell Resistance" in data:
            Spell_Resistance_descriptions = ["Gain advantage on saving throws against spells and resistance to spell damage."]
            self.standard("Spell Resistance", Spell_Resistance_descriptions)

    def Wizard_Conjuration(self):
        data = q.db.Class["Abil"]

        if "Conjuration Savant" in data:
            Conjuration_Savant_descriptions = ["The gold and time you must spend to copy a conjuration spell into your spellbook is halved."]
            self.standard("Conjuration Savant", Conjuration_Savant_descriptions)

        if "Minor Conjuration" in data:
            Minor_Conjuration_descriptions = ["(action) Conjure a non-magical item (up to 3ft, 10 lbs). It lasts for 1 hour or until it takes damage."]
            self.standard("Minor Conjuration", Minor_Conjuration_descriptions)

        if "Benign Transportation" in data:
            Benign_Transportation_descriptions = ["(action) Teleport up to 30ft or swap places with a willing creature. Usable again after a long rest or casting a Level 1+ conjuration spell."]
            self.standard("Benign Transportation", Benign_Transportation_descriptions)

        if "Focused Conjuration" in data:
            Focused_Conjuration_descriptions = ["Your concentration on conjuration spells can't be broken as a result of taking damage."]
            self.standard("Focused Conjuration", Focused_Conjuration_descriptions)

        if "Durable Summons" in data:
            Durable_Summons_descriptions = ["Any creature you summon or create with a conjuration spell has 30 temporary hit points."]
            self.standard("Durable Summons", Durable_Summons_descriptions)

