from includes import gc
from includes import config
from includes import utilities
import json

gather_content = gc.cgAPI()
next_page = 0
items_found = 0
c = {"items": []}
c_position = 0
project_cycle = 1
max_cycles = config.maxcycles # we still need to figure out how to get this value
next_project = config.nextproject # we will need to retrieve this value too, this will allow the program to switch
# contexts.

while True:
    next_page = next_page + 1  # Starts at 1
    all_items = gather_content.api_get_items("?include=structure&page=" + str(next_page))
    full_response = all_items.json()
    if full_response['pagination']['count'] == 0:
        if project_cycle < max_cycles:
            print('Switching projects')
            print('Previous project was ' + str(gather_content.get_project()))
            gather_content.set_project(next_project)
            print('New project directory: ' + str(gather_content.get_project()))
            project_cycle = project_cycle + 1
            next_page = 0
        else:
            break
    else:
        print('\nCurrent page: ' + str(full_response['pagination']['current_page']) + '\n')
        print(utilities.esc('45;1;4') + 'processing ' + str(full_response['pagination']['count']) + ' items.' + utilities.esc(0))
        items_found = items_found + full_response['pagination']['count']
        for i in range(full_response['pagination']['count']):
            current_item = full_response['data'][i]['id']
            single_item_res = gather_content.api_get_single_item(current_item)
            item_data = single_item_res.json()
            content = item_data['data']
            output = gc.merge_item_data(full_response, content)
            c['items'].append({})
            # print('dictionary entry at position at: ' + str(c_position))
            c['items'][c_position] = output
            c_position = c_position + 1
            utilities.progress(i+1)
out_file = open("data/output/master.json", "w")
json.dump(c, out_file, indent=6)
out_file.close()
print("Total items found: " + str(items_found))
