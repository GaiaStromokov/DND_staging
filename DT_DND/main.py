from dearpygui.dearpygui import *
import q
from colorist import *



from ui.call_back_handler import backend_manager

from manager.character import Character
from manager.dbm import dbm
from manager.components.Equipment_comp import Bazaar


from ui.init_ui import init_ui
from path_helper import get_path


def init_bullshit():
    if q.db is None:
        red("[init_pc] ERROR : Not loaded")
        return


    
    green("[init_pc] - player now exists")
    
    
def on_exit_callback():
    q.EXIT_save_json()
    save_init_file(get_path("utils", "config_save.ini"))
    stop_dearpygui()


def startup():
    inst_dbm = dbm()
    inst_backend = backend_manager()
    inst_bazaar = Bazaar()
    
    q.dbm = inst_dbm
    q.cbh = inst_backend.get_callback_handler()
    q.w = inst_bazaar


    q.dbm.Manager.startup()
    init_ui()
    inst_backend.Start()
    



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