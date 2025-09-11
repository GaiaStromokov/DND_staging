from box import Box
import json
import sys
from colorist import *
from path_helper import get_path

def _load_json_data(file_path):
    try:
        with open(file_path, 'r') as f: return Box(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        red(f"[load_json_data] - (Can't load file path) {file_path}: {e}")
        sys.exit(1)

db = _load_json_data(get_path('dist', 'db.json'))

w = None
cbh = None
dbm = None

def EXIT_save_json():
    if db:
        db_path = get_path('dist', 'db.json')
        try:
            with open(db_path, 'w') as f:
                json.dump(db.to_dict(), f, indent=4)
                green("[save_json] [db]")
        except Exception as e:
            red(f"[save_json] [db] - {e}")