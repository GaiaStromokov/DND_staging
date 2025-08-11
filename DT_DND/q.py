from box import Box
import json
import sys
import os
from colorist import *

def get_db_path():
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
        return os.path.join(base_path, 'db.json')
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, 'dist', 'db.json')


def _load_json_data(file_path):
    try:
        with open(file_path, 'r') as f: return Box(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        red(f"[load_json_data] - (Can't load file path) {file_path}: {e}")
        sys.exit(1)

db = _load_json_data(get_db_path())

pc = None
w = None


def EXIT_save_json():
    if db:
        db_path = get_db_path()
        try:
            with open(db_path, 'w') as f:
                json.dump(db.to_dict(), f, indent=4)
                green("[save_json] [db]")
        except Exception as e:
            red(f"[save_json] [db] - {e}")
