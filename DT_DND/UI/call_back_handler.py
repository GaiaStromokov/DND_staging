from Sheet.backend import (
    stage_Level, 
    
    stage_Race, stage_Subrace, 
    stage_Race_Asi, stage_Race_Use,
    stage_Race_Spell_Use, stage_Race_Spell_Select,
    
    stage_Class, stage_Subclass,
    stage_Class_Use, stage_Class_Skill_Select,
    stage_Class_select,
    
    stage_Background, 
    stage_Background_Prof_Select,
    
    stage_Milestone_Level_Select, 
    stage_Milestone_Feat_Select, stage_Milestone_Feat_Choice, stage_Milestone_Feat_Use,
    stage_Milestone_Asi_Select,
    
    stage_Atr_Base,

    stage_Spell_Learn,
    stage_Spell_Prepare, stage_Spell_Cast, 
    
    stage_Long_Rest, stage_Health_Mod, stage_Player_HP_Mod,
    
    stage_Arcane_Ward,
    
    stage_Player_Prof_Select, stage_Player_Condition,
    
    stage_Characteristic_Input, stage_Description_Input,
    
    
    stage_Bazaar_Add_Item, stage_Backpack_Mod_Item,
    
    stage_Equip_Equip
)



def cbh(sender, data, user_data):
    func_dict = {
        "Level Input":                  stage_Level,
        "Core Race":                    stage_Race,
        "Core Subrace":                 stage_Subrace,
        "Core Class":                   stage_Class,
        "Core Subclass":                stage_Subclass,
        "Core Background":              stage_Background,

        "Base Atr":                     stage_Atr_Base,

        "Race Asi":                     stage_Race_Asi,
        "Race Use":                     stage_Race_Use,
        "Race Spell Use":               stage_Race_Spell_Use,
        "Race Spell Select":            stage_Race_Spell_Select,

        
        "Milestone Level Select":       stage_Milestone_Level_Select,
        "Milestone Feat Select":        stage_Milestone_Feat_Select,
        "Milestone Feat Choice":        stage_Milestone_Feat_Choice,
        "Milestone Feat Use":           stage_Milestone_Feat_Use,
        "Milestone Asi Select":         stage_Milestone_Asi_Select,


        "Class Use":                    stage_Class_Use,
        "Class Skill Select":           stage_Class_Skill_Select,
        "Class Select":                 stage_Class_select,
        
        "Spell Learn":                  stage_Spell_Learn,
        "Spell Prepare":                stage_Spell_Prepare,
        "Spell Cast":                   stage_Spell_Cast,
        
        "Background Prof Select":       stage_Background_Prof_Select,
        
        "Long Rest":                    stage_Long_Rest,

        
        "HP":                           stage_Health_Mod,
        "Player HP Mod":                stage_Player_HP_Mod,
        
        "Arcane Ward":                  stage_Arcane_Ward,
        
        "Player Prof Input":            stage_Player_Prof_Select,
        
        "Condition":                    stage_Player_Condition,
        
        "Characteristic":               stage_Characteristic_Input,
        "Description":                  stage_Description_Input,
        
        "Bazaar Add Item":              stage_Bazaar_Add_Item,
        "Backpack Mod Item":            stage_Backpack_Mod_Item,
        
        "Equip Equip":                  stage_Equip_Equip,
        "Clear Equip":                  stage_Equip_Equip
    }
    key = user_data[0]
    user_data=user_data[1:]
    print(f"{key} updating {func_dict[key].__name__}, data={data}, user_data={user_data}")
    func_dict[key](sender, data, user_data, populate_Fields)