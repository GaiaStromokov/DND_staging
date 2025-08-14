from ui.upd_helper_import import *



class upd_sheet:
    def __init__(self):
        pass


    def core():
        cdata = q.db.Core
        configure_item(tag.core.val("level"), label=get.Level())
        configure_item(tag.core.val("pb"), label = f"PB: +{get.PB()}")
        configure_item(tag.core.select("Race"), items=get.list_Race, default_value=get.Race())
        configure_item(tag.core.select("Subrace"), items=get.option_Race[cdata.R], default_value=get.Subrace())
        configure_item(tag.core.select("Class"), items=get.list_Class, default_value=get.Class())
        configure_item(tag.core.select("Subclass"), items=get.option_Class[cdata.C] if get.valid_class() else [], default_value=get.Subclass())
        configure_item(tag.core.select("Background"), items=get.list_Background, default_value=get.Background())
            


    def attributes():
        data=q.db.Atr
        for atr in get.list_Atr:
            cdata=data[atr]
            configure_item(tag.atr.sum(atr), label = cdata.Val)
            configure_item(tag.atr.mod(atr), label = cdata.Mod)
            configure_item(tag.atr.select(atr), default_value = cdata.Base)
            configure_item(tag.atr.source("Base"), label = cdata.Base)
            configure_item(tag.atr.source("Race"), label = cdata.Rasi)
            configure_item(tag.atr.source("feat"), label = cdata.Milestone)



    def skills():
        for skill in get.list_Skill:
            cdata=q.pc.Skill[skill]
            
            configure_item(tag.skill.toggle(skill), default_value=cdata)
            configure_item(tag.skill.mod(skill), label=get.skill_text(skill))
            # configure_item(f"skill_Player_{skill}", default_value=skill in cdata["Player"])
            # configure_item(f"skill_Race_{skill}", default_value=skill in cdata["Race"])
            # configure_item(f"skill_Class_{skill}", default_value=skill in cdata["Class"])
            # configure_item(f"skill_BG_{skill}", default_value=skill in cdata["Background"])
            # configure_item(f"skill_Feat_{skill}", default_value=skill in cdata["Feat"])
            
    def health():
        hp = q.db.HP
        configure_item(tag.health.val("hp"), label = f"{hp["Current"]} / {hp["Sum"]}")
        configure_item(tag.health.val("temp"), label = hp["Temp"])
        set_value(tag.health.max("hp"), hp["Player"])
        

        
    def initiative():
        configure_item(tag.init.val(), label = get.Initiative_text())
        configure_item(tag.init.source("dex"), label = q.db.Atr["DEX"]["Mod"])
        configure_item(tag.init.source("race"), label = q.db.Initiative["Race"])
        configure_item(tag.init.source("class"), label = q.db.Initiative["Class"])
        
    def vision():
        cdata=q.pc.Vision
        configure_item(tag.vision.val(),label = cdata["Dark"])
        for i in get.list_Vision:configure_item(tag.vision.source(i),label = cdata[i])

    def speed():
        cdata=q.pc.Speed
        configure_item(tag.speed.val(),label = cdata["Walk"])
        for i in get.list_Speed: configure_item(tag.speed.source(i),label = cdata[i])

    def armor_class():
        ac=q.db.AC
        configure_item(tag.ac.val(), label = ac.Sum)
        configure_item(tag.ac.source("base"), label = ac.Base)
        configure_item(tag.ac.source("dex"), label = ac.Dex)


    def conditions():
        for i in get.list_Condition:
            configure_item(tag.cond.toggle(i),default_value = q.db.Condition[i])
            configure_item(tag.cond.text(i), color = get.condition_color(i))

    def character():
        cdata=q.db.Characteristic
        for i in get.list_Ideals:
            configure_item(tag.char.input(i), default_value=cdata[i])
            configure_item(tag.char.test(i), default_value=cdata[i])
        
        cdata=q.db.Description
        for i in get.list_Description:
            configure_item(tag.pdesc.input(i), default_value=cdata[i])
            configure_item(tag.pdesc.test(i), default_value=cdata[i])


    def proficiencies():
        cdata = q.pc.Prof
        for i in set(q.w.prof("Weapon")) & set(q.w.cat("Simple")):
            configure_item(tag.prof.multi("Simple", i, suffix="toggle"), default_value=i in cdata["Weapon"])
            configure_item(tag.prof.multi("Simple", i, suffix="text"), color=get.prof_color("Weapon", i))

        for i in set(q.w.prof("Weapon")) & set(q.w.cat("Martial")):
            configure_item(tag.prof.multi("Martial", i, suffix="toggle"), default_value=i in cdata["Weapon"])
            configure_item(tag.prof.multi("Martial", i, suffix="text"), color=get.prof_color("Weapon", i))

        for i in q.w.prof("Armor"):
            configure_item(tag.prof.multi("Armor", i, suffix="toggle"), default_value=i in cdata["Armor"])
            configure_item(tag.prof.multi("Armor", i, suffix="text"), color=get.prof_color("Armor", i))

        for i in get.list_Job:
            configure_item(tag.prof.multi("Artisan", i, suffix="toggle"), default_value=i in cdata["Tool"])
            configure_item(tag.prof.multi("Artisan", i, suffix="text"), color=get.prof_color("Tool", i))

        for i in get.list_Game:
            configure_item(tag.prof.multi("Gaming", i, suffix="toggle"), default_value=i in cdata["Tool"])
            configure_item(tag.prof.multi("Gaming", i, suffix="text"), color=get.prof_color("Tool", i))

        for i in get.list_Music:
            configure_item(tag.prof.multi("Musical", i, suffix="toggle"), default_value=i in cdata["Tool"])
            configure_item(tag.prof.multi("Musical", i, suffix="text"), color=get.prof_color("Tool", i))

        for i in get.list_Lang:
            configure_item(tag.prof.multi("Languages", i, suffix="toggle"), default_value=i in cdata["Lang"])
            configure_item(tag.prof.multi("Languages", i, suffix="text"), color=get.prof_color("Lang", i))