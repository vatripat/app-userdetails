from selenium.webdriver.common.by import By

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class Page(object):

    """
    This Class meant to provide following:
        - Locators of Web elements on Common Actions
        - Supporting Methods to interact on Page
    """

    VIEWUSER = (By.CSS_SELECTOR, "a[ui-sref='viewuser']")
    ADDUSER = (By.CSS_SELECTOR, "a[ui-sref='adduser']")
    SIGNOUT = (By.CSS_SELECTOR, "a[ui-sref='login']")

    def __init__(self, driver):
        self.driver = driver

    def goto_viewuser(self):
        from .view_user import ViewUser
        self.driver.find_element(*self.VIEWUSER).click()
        logger.info("Switching to ViewUser screen")
        return ViewUser(self.driver)

    def goto_adduser(self):
        from .add_user import AddUser
        self.driver.find_element(*self.ADDUSER).click()
        logger.info("Switching moved to AddUser screen")
        return AddUser(self.driver)

    def sign_out(self):
        from .login import Login
        self.driver.find_element(*self.SIGNOUT).click()
        logger.info("handle moved to Home Login screen")
        return Login(self.driver)
