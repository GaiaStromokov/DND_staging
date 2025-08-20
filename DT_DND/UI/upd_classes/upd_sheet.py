from ui.upd_helper_import import *
tag = Tag()


class upd_sheet:
    def __init__(self):
        pass


    def core(self):
        cdata = q.db.Core
        configure_item(tag.core.val("level"), label=get.Level())
        configure_item(tag.core.val("pb"), label = f"PB: +{get.PB()}")
        configure_item(tag.core.select("race"), items=get.list_Race, default_value=get.Race())
        configure_item(tag.core.select("subrace"), items=get.option_Race[cdata.R], default_value=get.Subrace())
        configure_item(tag.core.select("class"), items=get.list_Class, default_value=get.Class())
        configure_item(tag.core.select("subclass"), items=get.option_Class[cdata.C] if get.valid_class() else [], default_value=get.Subclass())
        configure_item(tag.core.select("background"), items=get.list_Background, default_value=get.Background())
            


    def attributes(self):
        data=q.db.Atr
        for atr in get.list_Atr:
            cdata=data[atr]
            configure_item(tag.atr.sum(atr), label = cdata.Val)
            configure_item(tag.atr.mod(atr), label = cdata.Mod)
            configure_item(tag.atr.select(atr), default_value = cdata.Base)
            configure_item(tag.atr.source(atr, "base"), label = cdata.Base)
            configure_item(tag.atr.source(atr, "race"), label = cdata.Rasi)
            configure_item(tag.atr.source(atr, "feat"), label = cdata.Milestone)



    def skills(self):
        for skill in get.list_Skill:
            cdata=q.pc.Skill[skill]
            
            configure_item(tag.skill.toggle(skill), default_value=cdata)
            configure_item(tag.skill.mod(skill), label=get.skill_text(skill))
            # configure_item(f"skill_Player_{skill}", default_value=skill in cdata["Player"])
            # configure_item(f"skill_Race_{skill}", default_value=skill in cdata["Race"])
            # configure_item(f"skill_Class_{skill}", default_value=skill in cdata["Class"])
            # configure_item(f"skill_BG_{skill}", default_value=skill in cdata["Background"])
            # configure_item(f"skill_Feat_{skill}", default_value=skill in cdata["Feat"])
            
    def health(self):
        hp = q.db.HP
        configure_item(tag.health.val("hp"), label = f"{hp["Current"]} / {hp["Sum"]}")
        configure_item(tag.health.val("temp"), label = hp["Temp"])
        set_value(tag.health.max("hp"), hp["Player"])
        

        
    def initiative(self):
        configure_item(tag.init.val(), label = get.Initiative_text())
        configure_item(tag.init.source("dex"), label = q.db.Atr["DEX"]["Mod"])
        configure_item(tag.init.source("race"), label = q.db.Initiative["Race"])
        configure_item(tag.init.source("class"), label = q.db.Initiative["Class"])
        
    def vision(self):
        cdata=q.pc.Vision
        configure_item(tag.vision.val(),label = cdata["Dark"])
        for i in get.list_Vision:configure_item(tag.vision.source(i),label = cdata[i])

    def speed(self):
        cdata=q.pc.Speed
        configure_item(tag.speed.val(),label = cdata["Walk"])
        for i in get.list_Speed: configure_item(tag.speed.source(i),label = cdata[i])

    def armor_class(self):
        ac=q.db.AC
        configure_item(tag.ac.val(), label = ac.Sum)
        configure_item(tag.ac.source("base"), label = ac.Base)
        configure_item(tag.ac.source("dex"), label = ac.Dex)
        configure_item(tag.ac.source("shield"), label = ac.Shield)


    def conditions(self):
        for i in get.list_Condition:
            configure_item(tag.cond.toggle(i),default_value = q.db.Condition[i])
            configure_item(tag.cond.text(i), color = get.condition_color(i))

    def character(self):
        cdata=q.db.Characteristic
        for i in get.list_Ideals:
            name = i.lower()
            configure_item(tag.char.input(name), default_value=cdata[i])
            configure_item(tag.char.text(name), default_value=cdata[i])
        
        cdata=q.db.Description
        for i in get.list_Description:
            configure_item(tag.pdesc.input(i), default_value=cdata[i])
            configure_item(tag.pdesc.text(i), default_value=cdata[i])


def proficiencies(self):
    cdata = q.pc.Prof
    for i in q.w.search(Tier=0, Slot="Weapon", Cat="Simple"):
        configure_item(tag.prof.toggle("Simple", i), default_value=i in cdata["Weapon"])
        configure_item(tag.prof.text("Simple", i), color=get.prof_color("Weapon", i))

    for i in q.w.search(Tier=0, Slot="Weapon", Cat="Martial"):
        configure_item(tag.prof.toggle("Martial", i), default_value=i in cdata["Weapon"])
        configure_item(tag.prof.text("Martial", i), color=get.prof_color("Weapon", i))

    for i in q.w.search(Tier=0, Slot=["Armor", "Shield"]):
        configure_item(tag.prof.toggle("Armor", i), default_value=i in cdata["Armor"])
        configure_item(tag.prof.text("Armor", i), color=get.prof_color("Armor", i))

    for i in get.list_Job:
        configure_item(tag.prof.toggle("Artisan", i), default_value=i in cdata["Tool"])
        configure_item(tag.prof.text("Artisan", i), color=get.prof_color("Tool", i))

    for i in get.list_Game:
        configure_item(tag.prof.toggle("Gaming", i), default_value=i in cdata["Tool"])
        configure_item(tag.prof.text("Gaming", i), color=get.prof_color("Tool", i))

    for i in get.list_Music:
        configure_item(tag.prof.toggle("Musical", i), default_value=i in cdata["Tool"])
        configure_item(tag.prof.text("Musical", i), color=get.prof_color("Tool", i))

    for i in get.list_Lang:
        configure_item(tag.prof.toggle("Languages", i), default_value=i in cdata["Lang"])
        configure_item(tag.prof.text("Languages", i), color=get.prof_color("Lang", i))