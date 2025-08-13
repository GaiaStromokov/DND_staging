def gen_abil(name: str):
    an = name
    tn = name.replace(" ", "_")
    return an, tn

class tag:
    class Base:
        prefix = None

        @classmethod
        def build(cls, items=None, suffix=None):
            if cls.prefix is None: raise NotImplementedError("Subclasses must define prefix")
            if suffix is None: raise ValueError("Suffix must be provided")
            items_str = "_".join(items) if isinstance(items, (list, tuple)) else str(items) if items else ""
            return f"{cls.prefix}_{items_str}_{suffix}" if items_str else f"{cls.prefix}_{suffix}"

        
        @classmethod
        def select(cls, *items): return cls.build(items if items else None, "select")
        @classmethod
        def val(cls, *items): return cls.build(items if items else None, "val")
        @classmethod
        def label(cls, *items): return cls.build(items if items else None, "label")
        @classmethod
        def button(cls, *items): return cls.build(items if items else None, "button")
        @classmethod
        def source(cls, *items): return cls.build(items if items else None, "source")
        @classmethod
        def toggle(cls, *items): return cls.build(items if items else None, "toggle")
        @classmethod
        def max(cls, *items): return cls.build(items if items else None, "max")
        @classmethod
        def input(cls, *items): return cls.build(items if items else None, "input")
        @classmethod
        def text(cls, *items): return cls.build(items if items else None, "text")
        @classmethod
        def mod(cls, *items): return cls.build(items if items else None, "mod")
        @classmethod
        def sum(cls, *items): return cls.build(items if items else None, "sum")
        @classmethod
        def sub(cls, *items): return cls.build(items if items else None, "sub")
        @classmethod
        def main(cls, *items): return cls.build(items if items else None, "main")
        @classmethod
        def window(cls, *items): return cls.build(items if items else None, "window")
        @classmethod
        def tabbar(cls, *items): return cls.build(items if items else None, "tabbar")
        @classmethod
        def tab(cls, *items): return cls.build(items if items else None, "tab")
        @classmethod
        def known(cls, *items): return cls.build(items if items else None, "known")
        @classmethod
        def available(cls, *items): return cls.build(items if items else None, "available")
        @classmethod
        def current(cls, *items): return cls.build(items if items else None, "current")
        @classmethod
        def tooltip(cls, *items): return cls.build(items if items else None, "tooltip")
        @classmethod
        def popup(cls, *items): return cls.build(items if items else None, "popup")
        @classmethod
        def header(cls, *items): return cls.build(items if items else None, "header")
        @classmethod
        def table(cls, *items): return cls.build(items if items else None, "table")
        @classmethod
        def cell(cls, *items): return cls.build(items if items else None, "cell")
        @classmethod
        def row(cls, *items): return cls.build(items if items else None, "row")
        
        @classmethod
        def wlevel(cls, level): 
            if cls.prefix is None: raise NotImplementedError("Subclasses must define prefix")
            return f"{cls.prefix}_Level_{level}_window"



        @classmethod
        def element(cls, *, item=None, suffix=None):
            if cls.prefix is None:
                raise NotImplementedError("Subclasses must define prefix")
            if suffix is None:
                raise ValueError("Suffix must be provided")
            return f"{cls.prefix}_{item}_{suffix}" if item else f"{cls.prefix}_{suffix}"

        @classmethod
        def multi(cls, *parents, suffix):
            if cls.prefix is None:
                raise NotImplementedError("Subclasses must define prefix")
            return f"{cls.prefix}_{'_'.join(parents)}_{suffix}"

        @classmethod
        def gen(cls, parents, items, suffix):
            parts = []
            if parents: parts.extend(parents)
            if items: parts.extend(items)
            return "_".join(parts) + f"_{suffix}"

        @classmethod
        def bmenu(cls, equip_type, rank):
            if cls.prefix is None: raise NotImplementedError("Subclasses must define prefix")
            return f"{cls.prefix}_{equip_type}_{rank}"

        @classmethod
        def equip(cls, item):
            item = item.lower()
            return f"{item}_equip"

    @staticmethod
    def icon(item):
        item = item.lower()
        return f"{item}_icon"

    @staticmethod
    def img(item):
        item = item.lower()
        return f"{item}_img"
    class core(Base):      prefix = "core"
    class health(Base):    prefix = "health"
    class prof(Base):      prefix = "proficiencies"
    class char(Base):      prefix = "character"
    class pdesc(Base):     prefix = "pdescription"
    class buffer1(Base):   prefix = "buffer1"
    class buffer2(Base):   prefix = "buffer2"
    class atr(Base):       prefix = "attributes"
    class init(Base):      prefix = "initiative"
    class ac(Base):        prefix = "armor_class"
    class vision(Base):    prefix = "vision"
    class speed(Base):     prefix = "speed"
    class cond(Base):      prefix = "condition"
    class rest(Base):      prefix = "rest"
    class skill(Base):     prefix = "skills"
    class inve(Base):      prefix = "inventory"
    class block(Base):     prefix = "block"
    class wallet(Base):    prefix = "wallet"
    class rfeature(Base):  prefix = "block_feature_race"
    class cfeature(Base):  prefix = "block_feature_class"
    class mfeature(Base):  prefix = "block_feature_milestone"
    class bfeature(Base):  prefix = "block_feature_background"
    class wactions(Base):  prefix = "block_actions_weapon"
    class spell(Base):     prefix = "block_spells"
    class scast(Base):     prefix = "block_spells_cast"
    class slearn(Base):    prefix = "block_spells_learn"
    class sprepare(Base):  prefix = "block_spells_prepare"
    
    class equip(Base):  prefix = "inventory_equip"
    class backpack(Base):  prefix = "inventory_backpack"
    class bazaar(Base):  prefix = "inventory_bazaar"











class size:
    w_max = 1350
    h_max = 880

    w_block = w_max - 595
    h_block = h_max - 114

    h_header_1 = 20
    w_header_2 = 188
    w_header_3 = 116

    gwrap = 640

    w_s_btn = 20
    w_m_btn = 46
    w_l_btn = 90

    w_armor_class = 62
    h_armor_class = 58

    w_attributes = 132
    h_attributes = 174

    w_buffer_1 = 132
    h_buffer_1 = 17

    w_buffer_2 = 210
    h_buffer_2 = 13

    w_character = 210
    h_character = 82

    w_conditions = 132
    h_conditions = 42

    w_core = 210
    h_core = 174

    w_health = 210
    h_health = 82

    w_initiative = 62
    h_initiative = 58

    w_inventory = 552
    h_inventory = 340

    w_item = 117

    w_proficiencies = 210
    h_proficiencies = 82

    w_rest = 132
    h_rest = 80

    w_skill = 194
    h_skill = 449

    w_speed = 62
    h_speed = 58

    w_vision = 62
    h_vision = 58

    w_wallet = 412
    h_wallet = 35