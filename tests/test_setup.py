import unittest
from includes import gc
from includes import config
from private import credentials
import main

class MyTestCase(unittest.TestCase):

    def test_gather_content_SETUP(self):
        test_obj = gc.GatherContent()
        test_obj.set_project(12345)
        self.assertEqual(test_obj.get_email(), credentials.MYEMAIL)
        self.assertEqual(test_obj.get_api_key(), credentials.APIKEY)
        self.assertEqual(test_obj.get_authorization_token(), credentials.authorization_token)
        self.assertEqual(test_obj.authorization_token, credentials.authorization_token)
        self.assertEqual(test_obj.get_header(), test_obj.get_header())
        self.assertEqual(test_obj.get_mime(), 'application/vnd.gathercontent.v2+json')
        self.assertEqual(test_obj.get_mime(), config.default_mime)
        self.assertEqual(test_obj.get_project(), 12345)
        self.assertEqual(test_obj, test_obj)

        # Updates
        test_obj_diff = gc.GatherContent()
        self.assertEqual(test_obj.get_email(), test_obj_diff.get_email())  # Test if equals

        test_obj_diff.set_api_key('thisIsANewKey.invalid')
        self.assertEqual(test_obj_diff.get_api_key(), 'thisIsANewKey.invalid')
        test_obj_diff.set_email('testemail@test-email.com')
        self.assertEqual(test_obj_diff.get_email(), 'testemail@test-email.com')
        # This object instance should not be equal now
        self.assertNotEqual(test_obj.get_email(), test_obj_diff.get_email(), 'emails are the same')

        # Subclass testing

        sub_test = gc.cgAPI()
        sub_test.get_template_query()
        sub_test.get_template()
        sub_test.api_get_template()
        sub_test.api_get_single_item()
        sub_test.api_get_single_file()
        sub_test.get_items_query()
        sub_test.api_get_items()
        sub_test.get_files_query()
        sub_test.api_get_files()
        sub_test.get_folders_query()
        sub_test.api_get_folders()

        # API test
        test_obj = gc.cgAPI()
        test_obj.set_project(credentials.project_id)
        test_obj.api_get_status_res(test_obj.get_template_query())
        self.assertEqual(test_obj.api_get_status_res(test_obj.get_template_query()), 200)
        self.assertEqual(test_obj.api_get_status_res(test_obj.get_items_query()), 200)
        self.assertEqual(test_obj.api_get_status_res(test_obj.get_folders_query()), 200)
        self.assertEqual(test_obj.api_get_status_res(test_obj.get_single_item_query(credentials.mock_item_id)), 200)
        self.assertEqual(test_obj.api_get_status_res(test_obj.get_single_file_query(credentials.mock_file_id)), 200)


# if __name__ == '__main__':
