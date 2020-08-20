from pages.login import Login

import logging


logger = logging.getLogger()


class TestUserCrud(object):

    """
        This Class interacting with create_user and View_user Page.
        This Class Contains :
            - Test Cases
            - Test Data
    """

    testUser = "user1"
    testPassword = "password"

    user_data_1 = {'UserID': 'testuser001', 'First Name': 'first001', 'Last Name': 'last001', 'Password': 'Test@123'}

    user_data_2 = {'UserID': 'testuser002', 'First Name': 'first002', 'Last Name': 'last002', 'Password': 'Test@123'}

    password_hint = \
        "Password must conatin at least one lower case alphabet, one upper case alphabet, one number and one special character!"

    def test_notification_for_password_hint(self, driver):
        logger.info("====== Running TEST : test_notification_for_password_hint =====")

        login_page = Login(driver)

        add_user_page = login_page.login_with_valid_credentials()

        add_user_page.insert_invalid_credentials(self.testUser, self.testPassword)
        add_user_page.verify_password_hint_msg(self.password_hint)

    def test_user_created_successfully(self, driver):
        logger.info("====== Running TEST : test_user_created_successfully =====")

        login_page = Login(driver)

        add_user_page = login_page.login_with_valid_credentials()

        view_user_page = add_user_page.create_valid_user(self.user_data_1['UserID'], self.user_data_1['Password'],
                                                         self.user_data_1['First Name'], self.user_data_1['Last Name'])

        view_user_page.verify_user_present(self.user_data_1)

    def test_multiple_user_created_successfully(self, driver):
        logger.info("====== Running TEST : test_multiple_user_created_successfully =====")

        login_page = Login(driver)

        add_user_page = login_page.login_with_valid_credentials()

        view_user_page = add_user_page.create_valid_user(self.user_data_1['UserID'], self.user_data_1['Password'],
                                                         self.user_data_1['First Name'], self.user_data_1['Last Name'])

        view_user_page.verify_user_present(self.user_data_1)

        add_user_page = view_user_page.goto_adduser()

        add_user_page.\
            create_valid_user(self.user_data_2['UserID'], self.user_data_2['Password'],
                              self.user_data_2['First Name'], self.user_data_2['Last Name']).\
            verify_user_present(self.user_data_2)

    def test_create_user_with_duplicate_user(self, driver):
        logger.info("====== Running TEST : test_create_user_with_duplicate_user =====")

        login_page = Login(driver)

        add_user_page = login_page.login_with_valid_credentials()

        view_user_page = add_user_page.create_valid_user(self.user_data_1['UserID'], self.user_data_1['Password'],
                                                         self.user_data_1['First Name'], self.user_data_1['Last Name'])

        view_user_page.verify_user_present(self.user_data_1)

        add_user_page = view_user_page.goto_adduser()

        add_user_page.create_invalid_user(self.user_data_1['UserID'], self.user_data_1['Password'])\
            .verify_duplicate_user_error("This userid already exists. Please enter another userid.")

















