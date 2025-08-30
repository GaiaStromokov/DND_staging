from dearpygui.dearpygui import *
import q
from colorist import *



from ui.call_back_handler import backend_manager
from manager.character import init_pc
from ui.init_ui import init_ui
from path_helper import get_path


def on_exit_callback():
    q.EXIT_save_json()
    save_init_file(get_path("utils", "config_save.ini"))
    stop_dearpygui()

def startup():
    backend = backend_manager()
    q.cbh = backend.get_callback_handler()
    init_pc()
    q.pc.start_configuration()
    init_ui()
    backend.Start()
    


def main():
    
    #show_item_registry()
    create_context()
    with font_registry(): font_choice = add_font(get_path("utils", "Helvetica.ttf"), 13)
    configure_app(init_file=get_path("utils", "config_save.ini"), docking=True, docking_space=True)
    create_viewport(title="rpg", width=1350, height=880)
    set_viewport_pos((20, 20))
    set_exit_callback(on_exit_callback)
    bind_font(font_choice)
    setup_dearpygui()
    
    startup()
    
    show_viewport()
    start_dearpygui()
    destroy_context()

if __name__ == "__main__":
    main()