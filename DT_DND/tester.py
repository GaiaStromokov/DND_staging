from dearpygui.dearpygui import *






# #ANCHOR - Window Skeleton

create_context()
create_viewport(title="rpg", width=1350, height=880)
set_viewport_pos((20, 20))
setup_dearpygui()



with window(no_title_bar=True, no_close=True, autosize=True, tag="w.Main"):
    add_button(label = "button", tag=bt / "button")





show_viewport()
start_dearpygui()
destroy_context()
stop_dearpygui()

