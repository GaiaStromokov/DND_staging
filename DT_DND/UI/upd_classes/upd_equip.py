from ui.upd_helper_import import *


class upd_equip:
    def __init__(self):
        self.backpack = None
        self.two_handed = None
        self.cEquip = None
        self.main_hand_item = None
    
    def load_data(self):
        self.backpack = set(q.db.Inventory.Backpack)
        self.two_handed = set(q.w.prop("Two-handed"))
        self.cEquip = q.db.Inventory.Equip
        self.main_hand_item = self.cEquip["Hand_1"]
    
    def get_slots(self):
        return [
            ("Face", q.w.slot("Face"), tag.equip.select("Face")),
            ("Throat", q.w.slot("Throat"), tag.equip.select("Throat")),
            ("Body", q.w.slot("Body"), tag.equip.select("Body")),
            ("Hands", q.w.slot("Hands"), tag.equip.select("Hands")),
            ("Waist", q.w.slot("Waist"), tag.equip.select("Waist")),
            ("Feet", q.w.slot("Feet"), tag.equip.select("Feet")),
            ("Armor", q.w.slot("Armor"), tag.equip.select("Armor")),
            ("Hand_1", q.w.slot("Weapon"), tag.equip.select("Hand_1")),
            ("Hand_2", q.w.list_off_hand, tag.equip.select("Hand_2")),
            ("Ring_1", q.w.slot("Ring"), tag.equip.select("Ring_1")),
            ("Ring_2", q.w.slot("Ring"), tag.equip.select("Ring_2")),
        ]
    
    def get_available_items(self, source):
        return [get.iName(i) for i in source if i in self.backpack]
    
    def get_default_value(self, slot_name):
        if slot_name == "Hand_2":
            if self.main_hand_item in self.two_handed:
                return "Weapon Grip"
            elif get.weapon_versatile():
                return "Verse Grip"
            else:
                return get.iName(self.cEquip["Hand_2"]) if self.cEquip["Hand_2"] in self.backpack else ""
        else:
            equipped = self.cEquip.get(slot_name, None)
            return get.iName(equipped) if equipped in self.backpack else ""
    
    def whole(self):
        self.load_data()
        slots = self.get_slots()
        
        for slot_name, source, select_tag in slots:
            items = self.get_available_items(source)
            default_value = self.get_default_value(slot_name)
            configure_item(select_tag, items=items, default_value=default_value)