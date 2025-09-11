from ui.upd_helper_import import *
tag = Tag()

class upd_milestone:
    def __init__(self):
        self.parent = tag.mfeature.main()

    def Whole(self):
        self.sub()
        self.main()


    def sub(self):
        cdata = q.db.Milestone
        item_clear(tag.mfeature.sub())
        with group(parent=tag.mfeature.sub()):
            for i in range(q.dbm.milestone_count):
                with group(horizontal=True):
                    add_text(f"Milestone {i}: ", color=c_h1)
                    data = cdata["Select"][i]
                    add_combo(items=["Feat", "Asi", "Clear"], default_value=data,  width=50, no_arrow_button=True, user_data=["Milestone Top Select", i], callback=q.cbh, tag=tag.mfeature.select("top", i))
                    if data == "Feat":
                        cdata = cdata["Feat"][i]
                        add_combo(items=get.list_Feat, default_value=cdata,  width=150, no_arrow_button=True, user_data=["Milestone Feat Select", i], callback=q.cbh, tag=tag.mfeature.select("feat", i))
                    elif data == "Asi":
                        cdata = cdata["Asi"][i]
                        add_combo(items=get.list_Atr + ["Clear"], default_value=cdata[0],  width=50, no_arrow_button=True, user_data=["Milestone Asi Select", i, 0], callback=q.cbh, tag=tag.mfeature.select("asi_0", i))
                        add_combo(items=get.list_Atr + ["Clear"], default_value=cdata[1],  width=50, no_arrow_button=True, user_data=["Milestone Asi Select", i, 1], callback=q.cbh, tag=tag.mfeature.select("asi_1", i))



    def main(self):
        item_clear(self.parent)
        for feat in q.db.Milestone["Feat"]:
            if feat:
                method_name = feat.replace(' ', '_')
                if hasattr(self, method_name):
                    getattr(self, method_name)()
                


    def standard(self, name, descriptions):
        a, t = gen_abil(name)
        t_header = tag.mfeature.header(t)
        desc_tags = [tag.mfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=sz.wrap, tag=desc_tags[i])

    def standard_popup(self, name, descriptions, num_choices=1):
        a, t = gen_abil(name)
        t_header = tag.mfeature.header(t)
        desc_tags = [tag.mfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]
        t_popup = tag.mfeature.popup(t)
        
        item_delete(t_popup)

        with group(parent=self.parent):
            add_text(a, color=c_h1, tag=t_header)
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=sz.wrap, tag=desc_tags[i])

        with popup(t_header, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=t_popup):
            with group(horizontal=False):
                for i in range(num_choices):
                    t_select = tag.mfeature.select(t, i)
                    add_combo(items=get.dict_Feat_Lists[t], default_value=q.db.Milestone.Data[t]["Select"][i], width=100, no_arrow_button=True, user_data=["Milestone Feat Modify","Modify", t, i], callback=q.cbh, tag=t_select)
                    add_button(label="X", user_data=["Milestone Feat Modify", "Clear", t, i], callback=q.cbh)

    def standard_toggle(self, name, descriptions):
        a, t = gen_abil(name)
        t_header = tag.mfeature.header(t)
        desc_tags = [tag.mfeature.text(t, f"{i+1}") for i, _ in enumerate(descriptions)]
        use = q.db.Milestone["Data"][t]["Use"]

        with group(parent=self.parent):
            with group(horizontal=True):
                add_text(a, color=c_h1, tag=t_header)
                for idx, val in enumerate(use):
                    box_tag = tag.mfeature.toggle(t,idx)
                    add_checkbox(default_value=val, enabled=True, user_data=["Milestone Feat Use", t, idx], callback=q.cbh, tag=box_tag)
            
            for i, desc in enumerate(descriptions):
                add_text(desc, color=c_text, wrap=sz.wrap, tag=desc_tags[i])


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



