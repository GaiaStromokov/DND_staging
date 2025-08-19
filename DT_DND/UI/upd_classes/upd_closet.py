from ui.upd_helper_import import *

class upd_closet:
    def __init__(self):
        self.backpack = set()
        self.two_handed = set()
        self.cEquip = {}
        self.main_hand_item = None
    
    def load_data(self):
        self.backpack = set(q.db.Inventory.Backpack)
        self.two_handed = set(q.w.search(Prop="Two-handed"))
        self.cEquip = q.db.Inventory.Closet
        self.main_hand_item = self.cEquip.get("Hand_1", None)
    
    def get_slots(self):
        return [
            ("Face", q.w.search(Slot="Face"), tag.closet.select("Face")),
            ("Throat", q.w.search(Slot="Throat"), tag.closet.select("Throat")),
            ("Body", q.w.search(Slot="Body"), tag.closet.select("Body")),
            ("Hands", q.w.search(Slot="Hands"), tag.closet.select("Hands")),
            ("Waist", q.w.search(Slot="Waist"), tag.closet.select("Waist")),
            ("Feet", q.w.search(Slot="Feet"), tag.closet.select("Feet")),
            ("Armor", q.w.search(Slot="Armor"), tag.closet.select("Armor")),
            ("Hand_1", q.w.search(Slot="Weapon"), tag.closet.select("Hand_1")),
            ("Hand_2", q.w.search(Slot=["Weapon","Shield"], Prop={"not":"Two-handed"}), tag.closet.select("Hand_2")),
            ("Ring_1", q.w.search(Slot="Ring_1"), tag.closet.select("Ring_1")),
            ("Ring_2", q.w.search(Slot="Ring_2"), tag.closet.select("Ring_2")),
        ]
    
    def get_available_items(self, source):
        return [get.iName(i) for i in source if i in self.backpack]
    
    def get_default_value(self, slot_name):
        equipped = self.cEquip.get(slot_name)
        
        if slot_name == "Hand_2":
            if self.main_hand_item in self.two_handed:
                return "Weapon Grip"
            elif get.weapon_versatile():
                return "Verse Grip"
            return get.iName(equipped) if equipped in self.backpack else ""
        
        return get.iName(equipped) if equipped in self.backpack else ""
    
    def whole(self):
        self.load_data()
        for slot_name, source, select_tag in self.get_slots():
            
            items = self.get_available_items(source)
            default_value = self.get_default_value(slot_name)
            configure_item(select_tag, items=items, default_value=default_value)
