from ui.upd_helper_import import *
tag = Tag()

class build_atr:
    def __init__(self, stat):
        self.Sum = tag.atr.sum(stat)
        self.Mod = tag.atr.mod(stat)
        self.Select = tag.atr.select(stat)
        self.Base = tag.atr.source(stat, "Base")
        self.Race = tag.atr.source(stat, "Race")
        self.Feat = tag.atr.source(stat, "Feat")
        
class build_skill:
    def __init__(self, skill):
        self.Label = tag.skill.label(skill)
        self.Toggle = tag.skill.toggle(skill)
        self.Mod = tag.skill.mod(skill)
        self.Player = tag.skill.source(skill, "Player")
        self.Race = tag.skill.source(skill, "Race")
        self.Class = tag.skill.source(skill, "Class")
        self.BG = tag.skill.source(skill, "BG")
        self.Feat = tag.skill.source(skill, "Feat")

class build_pdesc:
    def __init__(self, item):
        self.Input = tag.pdesc.input(item)
        self.Text = tag.pdesc.text(item)

class build_ideals:
    def __init__(self, name):
        self.Label = tag.char.label(name)
        self.Input = tag.char.input(name)
        self.Text = tag.char.text(name)

class build_prof:
    def __init__(self, category, item):
        self.Toggle = tag.prof.toggle(category, item)
        self.Text = tag.prof.text(category, item)
        


class build_wallet:
    def __init__(self, coin):
        self.Val = tag.wallet.val(coin)

class build_skeleton:
    def __init__(self):
        self.Main = "window_main"
        self.Core = tag.core.window()
        self.Health = tag.health.window()
        self.Prof = tag.prof.window()
        self.Char = tag.char.window()
        self.Buffer1 = tag.buffer1.window()
        self.Atr = tag.atr.window()
        self.Init = tag.init.window()
        self.AC = tag.ac.window()
        self.Vision = tag.vision.window()
        self.Speed = tag.speed.window()
        self.Cond = tag.cond.window()
        self.Rest = tag.rest.window()
        self.Buffer2 = tag.buffer2.window()
        self.Skill = tag.skill.window()
        self.Inve = tag.inve.window()
        self.Block = tag.block.window()
        self.Wallet = tag.wallet.window()


class build_health:
    def __init__(self):
        self.Hp = tag.health.val("HP")
        self.Temp = tag.health.val("Temp")
        self.Max = tag.health.max("HP")
        self.Label = tag.health.label()

class build_initiative:
    def __init__(self):
        self.Label = tag.init.label()
        self.Val = tag.init.val()
        self.Race = tag.init.source("Race")
        self.Class = tag.init.source("Class")
        self.Dex = tag.init.source("Dex")


class build_armorclass:
    def __init__(self):
        self.Label = tag.ac.label()
        self.Val = tag.ac.val()
        self.Base = tag.ac.source("Base")
        self.Dex = tag.ac.source("Dex")
        self.Shield = tag.ac.source("Shield")
        
class build_vision:
    def __init__(self):
        self.Label = tag.vision.label()
        self.Val = tag.vision.val()
        self.Dark = tag.vision.source("Dark")
        self.Blind = tag.vision.source("Blind")
        self.Tremor = tag.vision.source("Tremor")
        self.Tru = tag.vision.source("Tru")

class build_speed:
    def __init__(self):
        self.Label = tag.speed.label()
        self.Val = tag.speed.val()
        self.Walk = tag.speed.source("Walk")
        self.Climb = tag.speed.source("Climb")
        self.Swim = tag.speed.source("Swim")
        self.Fly = tag.speed.source("Fly")
        self.Burrow = tag.speed.source("Burrow")
        
class build_condition:
    def __init__(self, condition):
        self.Toggle = tag.cond.toggle(condition)
        self.Text = tag.cond.text(condition)

class build_rest:
    def __init__(self):
        self.Short = tag.rest.button("Short")
        self.Long = tag.rest.button("Long")

class build_characteristics:
    def __init__(self):
        self.Label = tag.pdesc.label()
        self.Traits = tag.char.label("traits")
        self.Ideals = tag.char.label("ideals")
        self.Bonds = tag.char.label("bonds")
        self.Flaws = tag.char.label("flaws")


class build_block:
    def __init__(self):
        self.Pparent = tag.wactions.window()
        self.tabbar = tag.block.tabbar()
        self.rfs = tag.rfeature.sub()
        self.rfm = tag.rfeature.main()
        self.rfa0 = tag.rfeature.select("Asi_0")
        self.rfa1 = tag.rfeature.select("Asi_1")
        self.rfac = tag.rfeature.button("Asi_clear")
        
        self.cfs = tag.cfeature.sub()
        self.cfm = tag.cfeature.main()
        
        self.mfs = tag.mfeature.sub()
        self.mfm = tag.mfeature.main()
        
        self.bfs = tag.bfeature.sub()
        self.bfm = tag.bfeature.main()
        self.wactions = tag.wactions.window()

class build_core:
    def __init__(self):
        self.parent = tag.core.window()
        self.Race = tag.core.select("Race")
        self.Subrace = tag.core.select("Subrace")
        self.Class = tag.core.select("Class")
        self.Subclass = tag.core.select("Subclass")
        self.Background =  tag.core.select("Background")
        self.Level = tag.core.val("Level")
        self.PB = tag.core.val("PB")
        
        
        
        
class tui:
    Prof = {}

for stat in get.list_Atr: setattr(tui, stat, build_atr(stat))
for skill in get.list_Skill: setattr(tui, skill, build_skill(skill))
for item in get.list_Description: setattr(tui, item, build_pdesc(item))
for name in get.list_Ideals: setattr(tui, name, build_ideals(name))
for coin in get.list_Coins: setattr(tui, coin, build_wallet(coin))
tui.Skeleton = build_skeleton()
tui.Health = build_health()
tui.Initiative = build_initiative()
tui.Armorclass = build_armorclass()
tui.Vision = build_vision()
tui.Speed = build_speed()
for condition in get.list_Condition: setattr(tui, condition, build_condition(condition))
tui.Rest = build_rest()
tui.Characteristics = build_characteristics()
tui.Block = build_block()
tui.Core = build_core()
