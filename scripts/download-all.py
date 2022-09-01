from includes import gc
from pathlib import Path
import json

gather_content = gc.cgAPI()

file_name = 'test_all_items_with_structure.json'
dir_path = '../tmp/'
file_path = dir_path + file_name
path = Path(file_path)
response = gather_content.api_get_items('/?include=structure')
f = gc.write_to_file(file_path, response)
json.load(f)
