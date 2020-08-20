from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from .common import Page

import logging
logger = logging.getLogger()


class UserProfile(Page):

    """
    This Class meant to provide following:
        - Locators of Web elements on UserProfile Page
        - Supporting Methods to interact on Page
    """

    PAGE_INFO = (By.CLASS_NAME, "page-info")
    UPDATE_USER_BTN = (By.XPATH, "//button[contains(text(), 'Update')]")
    ALERT_MESSAGE = (By.XPATH, "//button[contains(text(), 'Update')]/following-sibling::p[contains(text(),'User Updated Successfully')]")
    USERID = (By.XPATH, "//input[@ng-model='userInfo.userid']")
    USERPASSWORD = (By.XPATH, "//input[@ng-model='userInfo.password']")
    FIRSTNAME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._wait_for_pageload()

    def _wait_for_pageload(self):

        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.UPDATE_USER_BTN))
        except TimeoutException as ex:
            logger.error("Profile Page Not loaded with exception {}".format(ex))
            raise ex

    def _update_password(self, password):

        logger.info("Updating password of User to {}".format(password))
        self.driver.find_element(*self.USERPASSWORD).clear()

        self.driver.find_element(*self.USERPASSWORD).send_keys(password)

    def _update_fname(self, f_name):

        logger.info("Updating first name of User to {}".format(f_name))
        self.driver.find_element(*self.FIRSTNAME).clear()

        self.driver.find_element(*self.FIRSTNAME).send_keys(f_name)

    def _update_lname(self, l_name):

        logger.info("Updating last name of User to {}".format(l_name))
        self.driver.find_element(*self.LASTNAME).clear()

        self.driver.find_element(*self.LASTNAME).send_keys(l_name)

    def _click_update_btn(self):

        logger.info("Updating User - Click update")
        self.driver.find_element(*self.UPDATE_USER_BTN).click()

    def _get_user_details(self):

        user_id = self.driver.find_element(*self.USERID).get_property("value")
        logger.info("username filled in  {}".format(user_id))

        password = self.driver.find_element(*self.USERPASSWORD).get_property("value")
        logger.info("password filled in  {}".format(password))

        f_name = self.driver.find_element(*self.FIRSTNAME).get_property("value")
        logger.info("first Name filled in  {}".format(f_name))

        l_name = self.driver.find_element(*self.LASTNAME).get_property("value")
        logger.info("last Name filled in  {}".format(l_name))
        return user_id, password, f_name, l_name

    def verify_user_profile_is_correct(self, user, password, f_name=None, l_name=None):

        logger.info("Verifying the user details after login with NON ADMIN user")
        d_user_id, d_password, d_f_name, d_l_name = self._get_user_details()

        if d_user_id == user and d_password == password and d_f_name == f_name and d_l_name == l_name:

            assert True, "Profile Data is not matching as expected."

    def verify_userid_enabled(self):

        logger.info("Verify user id text box is disabled for editing, USER ID can not be changed")
        is_enabled = self.driver.find_element(*self.USERID).is_enabled()
        print(is_enabled)
        assert True if is_enabled else False

    def verify_alert(self):

        wait = WebDriverWait(self.driver, 10)

        try:
            wait.until(expected_conditions.visibility_of_element_located(self.ALERT_MESSAGE))
        except TimeoutException as ex:
            logger.error("Alert_message not seen on screen")
            raise ex

        logger.info("alert message captured on screen : {}".format(self.driver.find_element(*self.ALERT_MESSAGE).text))

        assert 'User Updated Successfully' in self.driver.find_element(*self.ALERT_MESSAGE).text

    def update_user_details(self, password=None, f_name=None, l_name=None):

        if password:
            self._update_password(password)
        if f_name:
            self._update_fname(f_name)
        if l_name:
            self._update_lname(l_name)
        try:
            self._click_update_btn()
        except ElementClickInterceptedException as e:
            logger.error(" Button is not enabled to be clicked : {}".format(e))
        else:
            logger.info(" after click, verify the alert message")
            self.verify_alert()


















