import json
import os,sys
from collections import defaultdict

def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

class Item:
    def __init__(self, name, attributes):
        self.Name = name
        for key, value in attributes.items():
            setattr(self, key, value)

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __repr__(self):
        attributes = {k: v for k, v in self.__dict__.items()}
        attr_str = ', '.join(f"{k}={repr(v)}" for k, v in attributes.items())
        return f"Item({attr_str})"


class Bazaar:
    def __init__(self, filepath="DT_DND\dist\item_comp.json"):
        self.items = self._load_items(filepath)

        self._category_lookup = defaultdict(list)
        self._slot_lookup = defaultdict(list)
        self._property_lookup = defaultdict(list)
        self._tier_lookup = defaultdict(list)
        self._proficiency_lookup = defaultdict(list)

        for name, item in self.items.items():
            for category in item.get('Cat', []):
                self._category_lookup[category].append(name)
            
            if slot := item.get('Slot'):
                self._slot_lookup[slot].append(name)

            for prop in item.get('Prop', []):
                self._property_lookup[prop].append(name)

            if (tier := item.get('Tier')) is not None:
                self._tier_lookup[tier].append(name)

            if item.get('Tier') == 0:
                if item.get('Slot') == "Weapon":
                    self._proficiency_lookup["Weapon"].append(name)
                elif item.get('Slot') == "Armor":
                    self._proficiency_lookup["Armor"].append(name)
        
        hand_items = set(self._slot_lookup.get("Weapon", []))
        two_handed_items = set(self._property_lookup.get("Two-handed", []))
        self._off_hand_items = list(hand_items - two_handed_items)

    def _load_items(self, filepath):
        items_dict = {}
        with open(filepath, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            for name, attributes in data.items():
                items_dict[name] = Item(name, attributes)
        return items_dict


    def Item(self, name):
        return self.items.get(name)

    def cat(self, category):
        return self._category_lookup.get(category, [])

    def slot(self, slot):
        return self._slot_lookup.get(slot, [])

    def prop(self, prop):
        return self._property_lookup.get(prop, [])

    def tier(self, tier):
        return self._tier_lookup.get(tier, [])
        
    def prof(self, prof_type):
        return self._proficiency_lookup.get(prof_type, [])

    def mcategory(self, tier, *categories):
        if not categories:
            return self.by_tier(tier)

        item_sets = (set(self.cat(c)) for c in categories)
        items_in_all_categories = set.intersection(*item_sets)

        items_in_tier = set(self.tier(tier))
        return list(items_in_all_categories & items_in_tier)
    
    @property
    def list_off_hand(self):
        return self._off_hand_items

    def __repr__(self):
        return f"Bazaar(items={len(self.items)})"