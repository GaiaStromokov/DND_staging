from ui.upd_helper_import import *

class upd_backpack():
    def __init__(self):
        pass

    def whole(self):
        self.fill_backpack()
        self.populate_backpack()
        
    def fill_backpack(self):
        bdata = q.db.Inventory.Backpack
        item_count = len(bdata)
        table_tag = tag.backpack.table()
        
        # Count existing rows
        existing_rows = 0
        while does_item_exist(tag.backpack.row(existing_rows)):
            existing_rows += 1
        
        # Add more rows if needed
        for row_idx in range(existing_rows, item_count):
            with table_row(parent=table_tag, tag=tag.backpack.row(row_idx)):
                add_table_cell(tag=tag.backpack.cell("name", row_idx))
                add_table_cell(tag=tag.backpack.cell("slot", row_idx))
                add_table_cell(tag=tag.backpack.cell("qty", row_idx))
                add_table_cell(tag=tag.backpack.cell("weight", row_idx))
                add_table_cell(tag=tag.backpack.cell("cost", row_idx))
        
        # Delete excess rows if needed
        for row_idx in range(item_count, existing_rows):
            delete_item(tag.backpack.row(row_idx))

    def populate_backpack(self):
        """Populate the cells with actual item data"""
        bdata = q.db.Inventory.Backpack
        
        for row_idx, item in enumerate(bdata):
            cdata = q.w.Item(item)
            qty = bdata[item][1]
            weight = 0
            cost = 0
            
            # Clear cells
            item_clear(tag.backpack.cell("name", row_idx))
            item_clear(tag.backpack.cell("slot", row_idx))
            item_clear(tag.backpack.cell("qty", row_idx))
            item_clear(tag.backpack.cell("weight", row_idx))
            item_clear(tag.backpack.cell("cost", row_idx))
            
            # Populate cells
            add_text(get.iName(item), parent=tag.backpack.cell("name", row_idx))
            
            item_delete(tag.backpack.tooltip(row_idx))
            with tooltip(tag.backpack.cell("name", row_idx), tag=tag.backpack.tooltip(row_idx)):
                item_detail_handler(item)
                
            add_text(cdata.Slot, parent=tag.backpack.cell("slot", row_idx))
            
            with group(horizontal=True, parent=tag.backpack.cell("qty", row_idx)):
                add_text(qty, tag=tag.backpack.text(item, row_idx))
                add_button(label="<", callback=q.cbh, user_data=["Backpack Mod Item", item, -1], small=True)
                add_button(label=">", callback=q.cbh, user_data=["Backpack Mod Item", item, 1], small=True)
                add_button(label="X", callback=q.cbh, user_data=["Backpack Mod Item", item, "Clear"], small=True)
            
            add_text(weight, parent=tag.backpack.cell("weight", row_idx))
            add_text(cost, parent=tag.backpack.cell("cost", row_idx))