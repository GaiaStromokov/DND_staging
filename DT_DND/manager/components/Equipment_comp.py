import json
from path_helper import get_path

class Item:
    def __init__(self, name, attributes):
        self.name = name
        for key, value in attributes.items():
            setattr(self, key, value)


    def __str__(self):
        attr_lines = [f"  - {key}: {value}" for key, value in self.__dict__.items() if key != 'name']
        return f"{self.name}:\n" + "\n".join(attr_lines)

    def get(self, key, default=None):
        return getattr(self, key, default)

class Bazaar:
    def __init__(self, filepath=None):
        if filepath is None: filepath = get_path("dist", "item_comp.json")
        self.items = self._load_items(filepath)

    def _load_items(self, filepath):
        items_dict = {}
        with open(filepath, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            for name, attributes in data.items(): items_dict[name] = Item(name, attributes)
        return items_dict

    def dItem(self, name):
        return self.items.get(name)

    def search(self, **criteria):
        results = []
        for name, item in self.items.items():
            if self._item_matches(item, criteria):
                results.append(name)
        return results

    def _item_matches(self, item, criteria):
        for key, expected in criteria.items():
            item_value = item.get(key)
            if not self._values_match(item_value, expected):
                return False
        return True

    def _values_match(self, item_value, expected):
        if isinstance(expected, dict) and "not" in expected:
            not_value = expected["not"]
            if isinstance(item_value, list):
                return not (not_value in item_value)
            return item_value != not_value

        if isinstance(expected, dict):
            return self._matches_range(item_value, expected)

        if isinstance(expected, list) and isinstance(item_value, list):
            return all(exp in item_value for exp in expected)

        if isinstance(expected, list):
            return item_value in expected

        if isinstance(item_value, list):
            return expected in item_value

        return item_value == expected

    def _matches_range(self, value, range_dict):
        if value is None:
            return False
        for operator, target in range_dict.items():
            if operator == '>=' and not (value >= target):
                return False
            elif operator == '>' and not (value > target):
                return False
            elif operator == '<=' and not (value <= target):
                return False
            elif operator == '<' and not (value < target):
                return False
        return True

    def cat(self, category):
        return self.search(Cat=category)

    def slot(self, slot):
        return self.search(Slot=slot)

    def tier(self, tier):
        return self.search(Tier=tier)
