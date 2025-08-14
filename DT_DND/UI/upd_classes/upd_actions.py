from ui.upd_helper_import import *



class upd_actions:
    def __init__(self):
        pass
    def main(self):
        self.weapon()
    def weapon(self):
        for atr in get.list_weapon_attributes:
            delete_item(tag.wactions.cell(atr,0), children_only=True)
            delete_item(tag.wactions.cell(atr,1), children_only=True)

        Hand_1 = q.db.Inventory.Equip["Hand_1"]
        Hand_2 = q.db.Inventory.Equip["Hand_2"]
        two_handed = Hand_1 in q.w.prop("Two-handed")
        Versatile = get.weapon_versatile()
        
        if Hand_1: 
            cdata = get.weapon_action_sc(Hand_1)
            idx = 0
        if not two_handed and not Versatile and Hand_2: 
            cdata = get.weapon_action_sc(Hand_2)
            idx = 1

        
        with group(parent=tag.wactions.cell("Name",idx)): add_text(cdata.Name)
        with group(parent=tag.wactions.cell("Range",idx)): add_text(cdata.Range)
        with group(parent=tag.wactions.cell("Hit",idx)): 
            with group(horizontal=True):
                add_text(cdata.hSign)
                add_text(cdata.hNum, color=cdata.hColor)
        with group(parent=tag.wactions.cell("Damage",idx)): 
            with group(horizontal=True):
                add_text(cdata.dDice)
                add_text(cdata.dSign)
                add_text(cdata.dNum, color=cdata.dColor)
        with group(parent=tag.wactions.cell("Type",idx)): 
            add_text(cdata.dType, tag=tag.wactions.text("Type",idx))
            item_delete(tag.wactions.tooltip("Type",idx))
            with tooltip(tag.wactions.text("Type",idx), tag=tag.wactions.tooltip("Type",idx)):
                add_text(get.dict_weapon_dtype_description[cdata.dType])

        with group(parent=tag.wactions.cell("Notes",idx)):
            with group(horizontal=True):
                for i in cdata.Prop: 
                    add_text(get.dict_weapon_prop[i]["SC"], tag=tag.wactions.text("wprop",i,idx))
                    item_delete(tag.wactions.tooltip("wprop",i,idx))
                    with tooltip(tag.wactions.text("wprop",i,idx), tag=tag.wactions.tooltip("wprop",i,idx)):
                        add_text(i, color=c_h1)
                        add_text(get.dict_weapon_prop[i]["Desc"], wrap=240)

    
