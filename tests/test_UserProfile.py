import pytest
from pages.login import Login

import logging

logger = logging.getLogger()

class TestUserProfile(object):

    """
        This Class interacting with home Login Page.
        This Class Contains :
            - Test Cases
            - Test Data
    """

    testUser = "user1"
    testPassword = "password"

    user_data_1 = {'UserID': 'testuser003', 'First Name': 'first003', 'Last Name': 'last003', 'Password': 'Test@123'}

    user_data_2 = {'UserID': 'testuser003', 'First Name': 'first004', 'Last Name': 'last004', 'Password': 'Update@123'}

    @pytest.mark.xfail
    def test_update_user_information(self, driver):

        logger.info("====== Running TEST : test_update_user_information =====")

        login_page = Login(driver)

        add_user_page = login_page.login_with_valid_credentials()

        view_user_page = add_user_page.create_valid_user(self.user_data_1['UserID'], self.user_data_1['Password'],
                                                         self.user_data_1['First Name'], self.user_data_1['Last Name'])

        login_page = view_user_page.sign_out()

        user_profile = login_page.login_with_valid_credentials(self.user_data_1['UserID'], self.user_data_1['Password'])

        user_profile.verify_userid_enabled()

        user_profile.verify_user_profile_is_correct(self.user_data_1['UserID'], self.user_data_1['Password'],
                                                    self.user_data_1['First Name'], self.user_data_1['Last Name'])

        user_profile.update_user_details(password=self.user_data_2['Password'], f_name=self.user_data_2['First Name'])

        login_page = user_profile.sign_out()

        add_user_page = login_page.login_with_valid_credentials()

        add_user_page.goto_viewuser().verify_user_present(self.user_data_2)










