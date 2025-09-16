from ui.upd_helper_import import *
tag = Tag()

class upd_sheet:
    def __init__(self):
        pass

    def Core(self):
        cdata = q.dbm.Core.g.Visual
        
        configure_item(tag.core.val("Level"), label=cdata.Level)
        configure_item(tag.core.val("PB"), label = f"PB: +{cdata.PB}")
        configure_item(tag.core.select("Race"), items=get.list_Race, default_value=cdata.nRace)
        configure_item(tag.core.select("Subrace"), items=get.option_Race[cdata.nRace], default_value=cdata.nSubrace)
        configure_item(tag.core.select("Class"), items=get.list_Class, default_value=cdata.nClass)
        configure_item(tag.core.select("Subclass"), items=get.option_Class[cdata.nClass] if q.dbm.Class.Validate else [], default_value=cdata.nSubclass)
        configure_item(tag.core.select("Background"), items=get.list_Background, default_value=cdata.nBackground)
            
    def Attributes(self):
        data=q.db.Atr
        for atr in get.list_Atr:
            cdata=data[atr]
            configure_item(tag.atr.sum(atr), label = cdata.Val)
            configure_item(tag.atr.mod(atr), label = cdata.Mod)
            configure_item(tag.atr.select(atr), default_value = cdata.Base)
            configure_item(tag.atr.source(atr, "Base"), label = cdata.Base)
            configure_item(tag.atr.source(atr, "Race"), label = cdata.Rasi)
            configure_item(tag.atr.source(atr, "Feat"), label = cdata.Milestone)

    def Skills(self):
        data = q.dbm.Visual_Skill
        calc = q.dbm.Mod_Skill
        for skill in get.list_Skill:
            cdata=data[skill]
            configure_item(tag.skill.toggle(skill), default_value=cdata)
            configure_item(tag.skill.mod(skill), label=get.skill_text(calc[skill]))
            # configure_item(f"skill_Player_{skill}", default_value=skill in cdata["Player"])
            # configure_item(f"skill_Race_{skill}", default_value=skill in cdata["Race"])
            # configure_item(f"skill_Class_{skill}", default_value=skill in cdata["Class"])
            # configure_item(f"skill_BG_{skill}", default_value=skill in cdata["Background"])
            # configure_item(f"skill_Feat_{skill}", default_value=skill in cdata["Feat"])

    def Health(self):
        data = q.dbm.Health.g.Visual
        configure_item(tag.health.val("HP"), label = data.HP)
        configure_item(tag.health.val("Temp"), label = data.Temp)
        set_value(tag.health.val("Max"), data.Max)
        
    def Initiative(self):
        data = q.dbm.Initiative.g.Visual
        configure_item(tag.init.val(), label = data.Val)
        configure_item(tag.init.source("Dex"), label = data.Dex)
        configure_item(tag.init.source("Race"), label = data.Race)
        configure_item(tag.init.source("Class"), label = data.Class)
        configure_item(tag.init.source("Feat"), label = data.Milestone)
        
    def Vision(self):
        cdata = q.dbm.Collect_Vision
        configure_item(tag.vision.val(), label=cdata.Dark)
        for i in get.list_Vision:
            configure_item(tag.vision.source(i), label=cdata[i])

    def Speed(self):
        cdata = q.dbm.Collect_Speed
        configure_item(tag.speed.val(), label=cdata.Walk)
        for i in get.list_Speed:
            configure_item(tag.speed.source(i), label=cdata[i])


    def AC(self):
        data = q.dbm.Armor.g.Visual
        configure_item(tag.ac.val(), label = data.Sum)
        configure_item(tag.ac.source("base"), label = data.Base)
        configure_item(tag.ac.source("dex"), label = data.Dex)
        configure_item(tag.ac.source("shield"), label = data.Shield)

    def Conditions(self):
        for i in get.list_Condition:
            configure_item(tag.cond.toggle(i),default_value = q.db.Condition[i])
            configure_item(tag.cond.text(i), color = get.condition_color(i))

    def Char(self):
        cdata=q.db.Characteristic
        for i in get.list_Ideals:
            name = i.lower()
            configure_item(tag.char.input(name), default_value=cdata[i])
            configure_item(tag.char.text(name), default_value=cdata[i])
        
        cdata=q.db.Description
        for i in get.list_Description:
            configure_item(tag.pdesc.input(i), default_value=cdata[i])
            configure_item(tag.pdesc.text(i), default_value=cdata[i])

    def Prof(self):
        cdata = q.dbm.Collect_Prof
        for i in q.w.search(Tier=0, Slot="Weapon", Cat="Simple"):
            configure_item(tag.prof.toggle("Simple", i), default_value=i in cdata.Weapon)
            configure_item(tag.prof.text("Simple", i), color=get.prof_color("Weapon", i))

        for i in q.w.search(Tier=0, Slot="Weapon", Cat="Martial"):
            configure_item(tag.prof.toggle("Martial", i), default_value=i in cdata.Weapon)
            configure_item(tag.prof.text("Martial", i), color=get.prof_color("Weapon", i))

        for i in q.w.search(Tier=0, Slot=["Armor", "Shield"]):
            configure_item(tag.prof.toggle("Armor", i), default_value=i in cdata.Armor)
            configure_item(tag.prof.text("Armor", i), color=get.prof_color("Armor", i))

        for i in get.list_Job:
            configure_item(tag.prof.toggle("Artisan", i), default_value=i in cdata.Tool)
            configure_item(tag.prof.text("Artisan", i), color=get.prof_color("Tool", i))

        for i in get.list_Game:
            configure_item(tag.prof.toggle("Gaming", i), default_value=i in cdata.Tool)
            configure_item(tag.prof.text("Gaming", i), color=get.prof_color("Tool", i))

        for i in get.list_Music:
            configure_item(tag.prof.toggle("Musical", i), default_value=i in cdata.Tool)
            configure_item(tag.prof.text("Musical", i), color=get.prof_color("Tool", i))

        for i in get.list_Lang:
            configure_item(tag.prof.toggle("Languages", i), default_value=i in cdata.Lang)
            configure_item(tag.prof.text("Languages", i), color=get.prof_color("Lang", i))