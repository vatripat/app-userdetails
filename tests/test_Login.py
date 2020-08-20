from pages.login import Login

import logging

logger = logging.getLogger()


class TestLogin(object):

    """
        This Class interacting with home Login Page.
        This Class Contains :
            - Test cases
            - Test Data
    """

    def test_login_valid_admin_user(self, driver):
        logger.info("====== Running TEST : test_update_user_information ======")

        login_page = Login(driver)

        login_page.login_with_valid_credentials()

    def test_login_invalid_uid(self, driver):
        logger.info("===== Running TEST : test_login_invalid_uid =====")

        login_page = Login(driver)

        login_page.login_with_invalid_credentials("123-%", "Xyz@123")\
            .verify_errormsg("Invalid UserId. Please try again")
        
    def test_login_with_rememberme_selected(self, driver):
        logger.info("===== Running TEST : test_login_with_rememberme_selected =====")

        login_page = Login(driver)

        add_user_page = login_page.login_with_valid_credentials(remember=True)

        login_page = add_user_page.sign_out()

        login_page.verify_username_already_filled_on_page("admin")

    def test_login_invalid_pwd(self, driver):
        logger.info("===== Running TEST : test_login_invalid_pwd ======")

        login_page = Login(driver)

        login_page.login_with_invalid_credentials("admin", "Xyz@123")\
            .verify_errormsg("Invalid credentials. Please try again!")













