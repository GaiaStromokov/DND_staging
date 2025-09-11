from ui.upd_helper_import import *
tag = Tag()


class upd_bazaar:
    def __init__(self):
        self.dict_struct = {
            "Weapon": [("Simple", "Melee"), ("Simple", "Ranged"), ("Martial", "Melee"), ("Martial", "Ranged")],
            "Armor": ["Light", "Medium", "Heavy", "Shield"]
        }
        
    def create_bazaar_button(self, item, category_type, parent):
        button_tag = tag.bazaar.button(item)
        tooltip_tag = tag.bazaar.tooltip(item)
        add_button(label=get.isName(item), width=sz.wItem, user_data=["Bazaar Add Item", category_type, item], callback=q.cbh, tag=button_tag, parent=parent)
        with tooltip(button_tag, tag=tooltip_tag):
            item_detail_handler(item)

    def get_target_items(self, categories, rank):
        target_set = set()
        is_weapon_type = isinstance(categories[0], tuple)
        for category_info in categories:
            if is_weapon_type:
                tag1, tag2 = category_info
                items = q.w.search(Tier=rank, Slot="Weapon", Cat=[tag1, tag2])
            else:
                slot = "Shield" if category_info == "Shield" else "Armor"
                items = q.w.search(Tier=rank, Slot=slot, Cat=category_info)
            target_set.update(items)
        return target_set

    def get_current_items(self, parent_container):
        current_items = set()
        if does_item_exist(parent_container):
            container_children = get_item_children(parent_container, 1)
            for group_id in container_children:
                if get_item_info(group_id)['type'] == 'Group':
                    row_children = get_item_children(group_id, 1)
                    for button_id in row_children:
                        button_alias = get_item_alias(button_id)
                        if button_alias and "bazaar" in button_alias and "add" in button_alias:
                            current_items.add(button_id)
        return current_items

    def rebuild_category(self, categories, equipment_type, parent_container, rank):
        item_clear(parent_container)
        
        with group(parent=parent_container):
            for category_info in categories:
                is_weapon_type = isinstance(categories[0], tuple)
                if is_weapon_type:
                    tag1, tag2 = category_info
                    label = f"{tag1} {tag2}"
                    items = q.w.search(Tier=rank, Slot="Weapon", Cat=[tag1, tag2])
                    items.sort()
                else:
                    label = category_info
                    slot = "Shield" if category_info == "Shield" else "Armor"
                    items = q.w.search(Tier=rank, Slot=slot, Cat=category_info)
                    items.sort()
                
                add_separator(label=label if rank == 0 else f"{label} (+{rank})")
                
                for i in range(0, len(items), 4):
                    with group(horizontal=True):
                        horizontal_group_id = last_item()
                        for item in items[i:i+4]:
                            self.create_bazaar_button(item, equipment_type, parent=horizontal_group_id)
    
    def Whole(self):
        for equipment_type, categories in self.dict_struct.items():
            for rank in range(5):
                rarity = get.item_rarity(rank)
                parent_container = tag.bazaar.window(equipment_type, rarity)

                if not does_item_exist(parent_container):
                    continue

                target_set = self.get_target_items(categories, rank)
                current_items = self.get_current_items(parent_container)
                
                if target_set != current_items:
                    self.rebuild_category(categories, equipment_type, parent_container, rank)