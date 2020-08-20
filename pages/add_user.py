from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .view_user import ViewUser
from .common import Page

import logging

logger = logging.getLogger()


class AddUser(Page):

    """
    This Class meant to provide following:
        - Locators of Web elements on AddUser Page
        - Supporting Methods to interact on Page
    """

    USERID = (By.XPATH, "//input[@ng-model='userInfo.userid']")
    USERPASSWORD = (By.XPATH, "//input[@ng-model='userInfo.password']")
    FIRSTNAME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")
    ADDUSER_BTN = (By.XPATH, "//button[contains(text(),'Add User')]")
    PWD_HINT = (By.CSS_SELECTOR, ".errormsg")
    DUP_USER_MSG = (By.CSS_SELECTOR, "p[ng-show='showDuplicateMssg']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._wait_for_pageload()

    def _wait_for_pageload(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.ADDUSER_BTN))
            logger.info("landed on add user page")
        except TimeoutException as ex:
            logger.error("AddUser Page Not loaded with exception {}".format(ex))
            raise ex

    def _enter_userid(self, user_id):

        logger.info("entering user id {}".format(user_id))
        self.driver.find_element(*self.USERID).clear()

        self.driver.find_element(*self.USERID).send_keys(user_id)

    def _enter_userpassword(self, password):

        logger.info("entering password  {}".format(password))

        self.driver.find_element(*self.USERPASSWORD).clear()

        self.driver.find_element(*self.USERPASSWORD).send_keys(password)

    def verify_password_hint_msg(self, error_msg):

        logger.info("verifying the message for password hint")
        assert error_msg in self._get_error_message(self.PWD_HINT)

    def verify_duplicate_user_error(self, error_msg):

        logger.info("verifying the error message for duplicate user ID")
        assert error_msg in self._get_error_message(self.DUP_USER_MSG)

    def _get_error_message(self, locator):

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(locator))

        #print(len(self.driver.find_elements(*locator)))
        message = self.driver.find_element(*locator).text
        logger.info(message)
        return message

    def _enter_fname(self, f_name):

        logger.info("entering first name of User :  {}".format(f_name))
        self.driver.find_element(*self.FIRSTNAME).clear()
        self.driver.find_element(*self.FIRSTNAME).send_keys(f_name)

    def _enter_lname(self, l_name):

        logger.info("entering Last name of User :  {}".format(l_name))
        self.driver.find_element(*self.LASTNAME).clear()
        self.driver.find_element(*self.LASTNAME).send_keys(l_name)

    def _click_add_user_button(self):

        logger.info("clicking add user button")
        self.driver.find_element(*self.ADDUSER_BTN).click()

    def insert_invalid_credentials(self, userid, password):

        logger.info("trying to login with Invalid Credentials ...")
        self._enter_userid(userid)
        self._enter_userpassword(password)

    def verify_adduser_page_loaded(self):

        logger.info("Verifying the window moved to add user page...")
        elements = self.driver.find_elements(*self.ADDUSER_BTN)
        return True if elements else False

    def create_valid_user(self, user_id, password, f_name=None, l_name=None):

        self._enter_userid(user_id)
        self._enter_userpassword(password)
        if f_name:
            self._enter_fname(f_name)
        if l_name:
            self._enter_lname(l_name)

        logger.info("Creating new user by clicking 'add user' button")
        self._click_add_user_button()

        return ViewUser(self.driver)

    def create_invalid_user(self, user_id, password, f_name=None, l_name=None):

        logger.info("Creating an invalid user")
        self._enter_userid(user_id)
        self._enter_userpassword(password)
        if f_name:
            self._enter_fname(f_name)
        if l_name:
            self._enter_lname(l_name)

        self._click_add_user_button()
        return self








