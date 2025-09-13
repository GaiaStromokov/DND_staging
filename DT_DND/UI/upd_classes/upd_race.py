from ui.upd_helper_import import *
tag = Tag()

class upd_race:
    def __init__(self):
        self.parent = tag.rfeature.main()

    def Whole(self):
        self.sub()
        self.main()
        
    def sub(self):
        configure_item(tag.rfeature.select("asi_0"), default_value = q.db.Race.Rasi[0])
        configure_item(tag.rfeature.select("asi_1"), default_value = q.db.Race.Rasi[1])
    
    def main(self):
        item_clear(self.parent)
        race, subrace = get.Race(), get.Subrace()

        for method in (race, f"{race}_{subrace}"):
            func = getattr(self, method, None)
            if callable(func):
                func()

    def standard(self, name, descriptions):
        a,t = tgen(name)
        t_header = tag.rfeature.header(t)
        desc_tags = [tag.rfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=sz.wrap, tag=desc_tags[i])

    def standard_choice(self, name, items_list):
        a,t = tgen(name)
        blue(t)
        selection = q.db.Race.Abil[t]["Select"][0]
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
                add_combo(items=items_list, default_value=selection, width=120, no_arrow_button=True, user_data=["Race Spell Select", t], callback=q.cbh, tag=t_select)

    def standard_spell_list(self, name):
        a,t = tgen(name)
        cdata = q.db.Race.Abil[t]
        t_header = tag.rfeature.header(t)

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            for spell in cdata.keys():
                t_label = tag.rfeature.label(t, spell)
                t_tooltip = tag.rfeature.tooltip(t, spell)
                with group(horizontal=True):
                    spell_name = spell.replace("_", " ")
                    add_text(spell_name, color=c_h2, tag=t_label)
                    if "Use" in cdata[spell]:
                        t_toggle = tag.rfeature.toggle(t, spell)
                        add_checkbox(default_value=cdata[spell]["Use"][0], enabled=True, user_data=["Race Spell Use", t, spell], callback=q.cbh, tag=t_toggle)
                
                item_delete(t_tooltip)
                with tooltip(t_label, tag=t_tooltip):
                    spell_detail(spell)

    def dragonborn_features(self, damage_type):
        save_map = {"Acid": "DEX", "Lightning": "DEX", "Fire": "DEX", "Poison": "CON", "Cold": "CON"}
        dnum_map = [0, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        dnum = dnum_map[q.db.Core.L] if q.db.Core.L < len(dnum_map) else 5
        
        save_ability = save_map.get(damage_type, "DEX")
        dc = 8 + q.db.Core.PB + q.db.Atr[save_ability]['Mod']

        Draconic_Resistance_descriptions = [f"You have resistance to {damage_type} damage."]
        
        self.standard("Draconic Resistance", Draconic_Resistance_descriptions)
        
        Breath_Weapon_descriptions = [
            f"(Action) Exhale destructive energy. Each creature in a 30ft line must make a DC {dc} {save_ability} saving throw, "
            f"taking {dnum}d6 {damage_type} damage on a failed save, and half as much damage on a successful one."
        ]
        self.standard_toggle("Breath Weapon", Breath_Weapon_descriptions)

    def standard_toggle(self, name, descriptions):
        a,t = tgen(name)
        t_header = tag.rfeature.header(t)
        desc_tags = [tag.rfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]
        use_data = q.db.Race.Abil[t]["Use"]

        with group(parent=self.parent):
            with group(horizontal=True):
                add_text(a, color=c_h1, tag=t_header)
                for idx, val in enumerate(use_data):
                    t_toggle = tag.rfeature.toggle(t, idx)
                    add_checkbox(default_value=val, enabled=True, user_data=["Race Use", t, idx], callback=q.cbh, tag=t_toggle)
            
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=sz.wrap, tag=desc_tags[i])

    def Empty(self):
        pass
    def Human(self):
        pass
    def Human_Standard(self):
        pass
    def Human_Variant(self):
        pass
    def Elf(self):
        fa = "Fey Ancestry"
        fa_d = ["You have advantage on saving throws against being charmed, and magic can't put you to sleep."]
        self.standard(fa, fa_d)

        t = "Trance"
        t_d = ["You don't need to sleep. Instead, you meditate deeply, remaining semiconscious, for 4 hours a day."]
        self.standard(t, t_d)

    def Elf_High(self):
        self.standard_choice("Cantrip", get.list_High_Elf_Cantrip)

    def Elf_Wood(self):
        motw = "Mask of the Wild"
        motw_d = ["You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."]
        self.standard(motw, motw_d)

    def Elf_Drow(self):
        dm = "Drow Magic"
        self.standard_spell_list(dm)
        
    def Elf_Shadar_Kai(self):
        if q.dbm.Core.g.L < 3: desc = "(Bonus Action) Teleport up to 30 ft to an unoccupied space you can see. You can use this a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."
        else: desc = "(Bonus Action) Teleport up to 30 ft to an unoccupied space you can see. You can use this a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. Immediately after you use it, you gain resistance to all damage until the start of your next turn."
        
        botrq = "Blessing of the Raven Queen"
        botrq_d = [desc]
        self.standard_toggle(botrq, botrq_d)

    def Dwarf(self):
        dr = "Dwarven Resilience"
        dr_d = ["You have advantage on saving throws against poison, and you have resistance against poison damage."]
        self.standard(dr, dr_d)

        sc = "Stonecunning"
        sc_d = [f"Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."]
        self.standard(sc, sc_d)

    def Dwarf_Hill(self):
        dt = "Dwarven Toughness"
        dt_d = ["Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."]
        self.standard(dt, dt_d)

    def Dwarf_Mountain(self):
        pass

    def Halfling(self):
        ly = "Lucky"
        ly_d = ["When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll."]
        self.standard(ly, ly_d)

        bv = "Brave"
        bv_d = ["You have advantage on saving throws against being frightened."]
        self.standard(bv, bv_d)

        hn = "Halfling Nimbleness"
        hn_d = ["You can move through the space of any creature that is of a size larger than yours."]
        self.standard(hn, hn_d)

    def Halfling_Lightfoot(self):
        ns = "Naturally Stealthy"
        ns_d = ["You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."]
        self.standard(ns, ns_d)

    def Halfling_Stout(self):
        sr = "Stout Resilience"
        sr_d = ["You have advantage on saving throws against poison, and you have resistance against poison damage."]
        self.standard(sr, sr_d)

    def Gnome(self):
        gc = "Gnome Cunning"
        gc_d = ["You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."]
        self.standard(gc, gc_d)

    def Gnome_Forest(self):
        swsb = "Speak with Small Beasts"
        swsb_d = ["Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts."]
        self.standard(swsb, swsb_d)


        a, t = tgen("Natural Illusionist")
        cdata = q.db.Race.Abil[t]
        with group(parent=self.parent):
            add_text(a, color=c_h1, wrap=sz.gwrap)
            for spell in cdata.keys():
                t_label = tag.rfeature.label(t, spell)
                t_tooltip = tag.rfeature.tooltip(t, spell)
                add_text(spell, color=c_h2, tag=t_label)

                item_delete(t_tooltip)
                with tooltip(t_label, tag=t_tooltip):
                    spell_detail(spell)
                    
    def Gnome_Rock(self):
        a, t = tgen("Tinker")
        t_header = tag.rfeature.header(t)
        t_tooltip = tag.rfeature.tooltip(t)
        description = "Using tinker's tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp)..."

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            item_delete(t_tooltip)
            with tooltip(t_header, tag=t_tooltip):
                add_text(a, color=c_h1)
                add_text(description, color=c_text, wrap=300)

        al = "Artificers Lore"
        al_d = ["Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply."]
        self.standard(al, al_d)

    def Dragonborn(self):
        pass
            
    def Dragonborn_Black(self):
        self.dragonborn_features("Acid")

    def Dragonborn_Blue(self):
        self.dragonborn_features("Lightning")

    def Dragonborn_Brass(self):
        self.dragonborn_features("Fire")

    def Dragonborn_Bronze(self):
        self.dragonborn_features("Lightning")

    def Dragonborn_Copper(self):
        self.dragonborn_features("Acid")

    def Dragonborn_Gold(self):
        self.dragonborn_features("Fire")

    def Dragonborn_Green(self):
        self.dragonborn_features("Poison")

    def Dragonborn_Red(self):
        self.dragonborn_features("Fire")

    def Dragonborn_Silver(self):
        self.dragonborn_features("Cold")

    def Dragonborn_White(self):
        self.dragonborn_features("Cold")
        
    def HalfOrc(self):
        re = "Relentless Endurance"
        re_d = ["When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest."]
        self.standard_toggle(re, re_d)

        sa = "Savage Attacks"
        sa_d = ["When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."]
        self.standard(sa, sa_d)

    def HalfOrc_Standard():
        pass

    def Tiefling(self):
        pass

    def Tiefling_Asmodeus(self):
        il = "Infernal Legacy"
        self.standard_spell_list(il)

    def Tiefling_Baalzebul(self):
        lom = "Legacy of Maladomini"
        self.standard_spell_list(lom)

    def Tiefling_Dispater(self):
        lod = "Legacy of Dis"
        self.standard_spell_list(lod)

    def Tiefling_Fierna(self):
        lop = "Legacy of Phlegethos"
        self.standard_spell_list(lop)

    def Tiefling_Glasya(self):
        lom = "Legacy of Malbolge"
        self.standard_spell_list(lom)

    def Tiefling_Levistus(self):
        los = "Legacy of Stygia"
        self.standard_spell_list(los)

    def Tiefling_Mammon(self):
        lom = "Legacy of Minauros"
        self.standard_spell_list(lom)

    def Tiefling_Mephistopheles(self):
        loc = "Legacy of Cania"
        self.standard_spell_list(loc)

    def Tiefling_Zariel(self):
        loa = "Legacy of Avernus"
        self.standard_spell_list(loa)

    def Harengon(self):
        lf = "Lucky Footwork"
        lf_d = ["When you fail a Dexterity saving throw, you can use your reaction to roll a d4 and add it to the save, potentially turning the failure into a success."]
        self.standard(lf, lf_d)

        rh = "Rabbit Hop"
        rh_d = [f"As a bonus action, you can jump a number of feet equal to five times your proficiency bonus, without provoking opportunity attacks."]
        self.standard_toggle(rh, rh_d)

    def Harengon_Standard():
        pass