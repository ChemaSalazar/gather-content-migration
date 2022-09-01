from private import credentials
from includes import config
import requests


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
        self.set_email(credentials.MYEMAIL)
        self.set_api_key(credentials.APIKEY)
        self.set_authorization_token(credentials.authorization_token)
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

    def set_template(self, template=credentials.template_id):
        self.template_id = template

    def set_project(self, project=credentials.project_id):
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
    def get_template_query(self):
        return config.gc_url+'templates/'+str(self.template_id)

    def get_items_query(self):
        return config.gc_url+'projects/'+str(self.project_id)+'/items'

    def get_single_item_query(self, item_id):
        return config.gc_url+'items/'+str(item_id)

    def get_files_query(self):
        return config.gc_url+'projects/' + str(self.project_id)+'/files'

    def get_single_file_query(self, file_id):
        return config.gc_url+'projects/' + str(self.project_id)+'/files/'+str(file_id)

    def get_folders_query(self):
        return config.gc_url+'projects/'+str(self.project_id)+'/folders'

    def api_get_template(self):
        return requests.get(self.get_template_query(), headers=self.header).text

    def api_get_items(self):
        return requests.get(self.get_items_query(), headers=self.header).text

    def api_get_single_item(self, item_id=credentials.mock_item_id):
        return requests.get(self.get_single_item_query(item_id), headers=self.header).text

    def api_get_files(self):
        return requests.get(self.get_files_query(), headers=self.header).text

    def api_get_single_file(self, file_id=credentials.mock_file_id):
        return requests.get(self.get_single_file_query(file_id), headers=self.header).text

    def api_get_folders(self):
        return requests.get(self.get_folders_query(), headers=self.header).text

    def api_get_status_res(self, desired_query):
        x = requests.get(desired_query, headers=self.header)
        return x.status_code
