import os
from dotenv import load_dotenv
from includes import config
import requests
import json

load_dotenv()


# Gathercontent class & definitions
class GatherContent(object):
    api = ''
    email = ''
    mime = ''
    authorization_token = ''
    header = {}
    project_id = 0
    template_id = 0

    def __init__(self):
        self.set_email(os.environ["MYEMAIL"])
        self.set_api_key(os.environ["APIKEY"])
        self.set_authorization_token(os.environ["authorization_token"])
        self.set_mime()
        self.set_project()
        self.set_template()
        self.set_header()

    def get_api_key(self):
        return self.api

    def get_email(self):
        return self.email

    def get_mime(self):
        return self.mime

    def get_authorization_token(self):
        return self.authorization_token

    def get_header(self):
        return self.header

    def get_project(self):
        return self.project_id

    def get_template(self):
        return self.template_id

    def set_template(self, template=os.environ["template_id"]):
        self.template_id = template

    def set_project(self, project=os.environ["project_id"]):
        self.project_id = project

    def set_api_key(self, api):
        self.api = api

    def set_email(self, email):
        self.email = email

    def set_mime(self, mime=config.default_mime):
        self.mime = mime

    def set_authorization_token(self, token):
        self.authorization_token = token

    def set_header(self):
        self.header = {
            "Accept": self.mime,
            "Authorization": self.authorization_token
        }


class cgAPI(GatherContent):

    # QUERY Builders
    def get_template_query(self):
        return config.gc_url + 'templates/' + str(self.template_id)

    def get_items_query(self, params=''):
        return config.gc_url + 'projects/' + str(self.project_id) + '/items' + params

    def get_single_item_query(self, item_id):
        return config.gc_url + 'items/' + str(item_id)

    def get_files_query(self):
        return config.gc_url + 'projects/' + str(self.project_id) + '/files'

    def get_single_file_query(self, file_id):
        return config.gc_url + 'projects/' + str(self.project_id) + '/files/' + str(file_id)

    def get_folders_query(self):
        return config.gc_url + 'projects/' + str(self.project_id) + '/folders'

    def get_components_query(self):
        return config.gc_url + 'projects/' + str(self.project_id) + '/components'

    def get_single_component_query(self, component_id):
        return config.gc_url + 'components/' + str(component_id)

    # API GET Methods

    def api_get_template(self):
        return requests.get(self.get_template_query(), headers=self.header).text

    def api_get_items(self, params=''):
        return requests.get(self.get_items_query(params), headers=self.header)

    def api_get_single_item(self, item_id=os.environ.get("mock_item_id")):
        return requests.get(self.get_single_item_query(item_id), headers=self.header)

    def api_get_files(self):
        return requests.get(self.get_files_query(), headers=self.header).text

    def api_get_single_file(self, file_id=os.environ.get("mock_file_id")):
        return requests.get(self.get_single_file_query(file_id), headers=self.header).text

    def api_get_folders(self):
        return requests.get(self.get_folders_query(), headers=self.header).text

    def api_get_components(self):
        return requests.get(self.get_components_query(), headers=self.header).text

    def api_get_single_component(self, component_id=os.environ.get("mock_component_id")):
        return requests.get(self.get_single_component_query(component_id), headers=self.header).text

    def api_get_status_res(self, desired_query):
        x = requests.get(desired_query, headers=self.header)
        return x.status_code


# Static methods
def is_field_type_text(field):
    if field == config.field_type[0]:
        return True
    return False


def is_field_type_choice_checkbox(field):
    if field == config.field_type[1]:
        return True
    return False


def does_value_exist_in_list(custom_list, value):
    exist_count = custom_list.count(value)
    if exist_count > 0:
        return True
    else:
        return False


def does_value_exist_in_dict(dictionary, key, value):
    if dictionary.get(key, value) == value:
        return True
    else:
        return False


# write to file
def write_to_file(file_path, response, mode="w"):
    if mode == "r+":
        with open(file_path, "r+") as file:
            file_data = json.load(file)
            file_data["data"].append(response["data"])
            file.seek(0)
            json.dump(file_data, file, indent=4)
    else:
        with open(file_path, mode) as outfile:
            outfile.write(response)
        return open(file_path)


def merge_item_data(structure_data, content, item_id=os.environ.get("mock_item_id")):
    fields = structure_data['data'][0]['structure']['groups'][0]['fields']
    raw_field_list = []
    field_label_list = []
    valuelist = []
    tomasterdict = {}

    # We iterate the number of fields within this item
    for i in range(len(fields)):
        raw_field_list.append(fields[i]['uuid'])
        field_label_list.append(fields[i]['label'])

    for i in range(len(content['content'])):
        # setting variable for field content:
        current_field_content = content['content'][raw_field_list[i]]
        current_field_content_raw = content['content'][raw_field_list[i]]

        # print(field_label_list[i], " = ", content[raw_field_list[i]])
        valuelist.append(current_field_content)
        tomasterdict.update(dict(zip(field_label_list, valuelist)))

    field_label_list.append('id')
    valuelist.append(item_id)
    tomasterdict.update(dict(zip(field_label_list, valuelist)))
    return tomasterdict
