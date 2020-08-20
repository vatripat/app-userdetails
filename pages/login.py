from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .add_user import AddUser
from selenium.common.exceptions import TimeoutException
from .user_profile import UserProfile
import logging

logger = logging.getLogger()


class Login(object):

    """
    This Class meant to provide following:
        - Locators of Web elements on LOGIN Page
        - Supporting Methods to interact on Page
    """

    HEADER = (By.XPATH, "//div[@class='header ng-scope']/p")
    USERNAME = (By.CSS_SELECTOR, "#userid")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    REMEMBERME = (By.XPATH, "//input[@ng-model='rememberMe']")
    LOGIN = (By.XPATH, "//button[contains(text(),'Login')]")
    ERROR = (By.XPATH, "//p[@class='invalid-creds']")

    def __init__(self, driver):

        self.driver = driver
        try:
            self._verify_header()
        except TimeoutException as ex:
            logger.error("Login Page Not loaded with exception {}".format(ex))
            raise ex

    def _enter_username(self, username):

        logger.info("enter the user id : {}".format(username))
        self.driver.find_element(*self.USERNAME).clear()

        self.driver.find_element(*self.USERNAME).send_keys(username)

    def _enter_password(self, password):

        logger.info("enter the password  : {}".format(password))
        self.driver.find_element(*self.PASSWORD).clear()

        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def _select_rememberme_checkbox(self):

        logger.info("selecting chckbox 'Remember Me'")
        self.driver.find_element(*self.REMEMBERME).click()
        logger.info("checkbox 'Remember Me' selected")

    def _click_login_button(self):

        logger.info("hitting the login button")
        self.driver.find_element(*self.LOGIN).click()

    def _verify_header(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self.HEADER))
        logger.info("verify the Page Header for correctness of Page landed")
        assert "Account Login" in self.driver.find_element(*self.HEADER).text

    def verify_errormsg(self, error_msg):

        wait = WebDriverWait(self.driver, 10)
        try:
            logger.info("Check Error Message on Screen")
            wait.until(expected_conditions.visibility_of_element_located(self.ERROR))
        except TimeoutException as ex:
            logger.error("element {} not found".format(self.ERROR))
            raise ex

        logger.info("error message appeared on screen is : {}".format(self.driver.find_element(*self.ERROR).text))

        assert error_msg in self.driver.find_element(*self.ERROR).text

    def _enter_valid_credentials(self, username, password, remember):

        self._enter_username(username)
        self._enter_password(password)
        if remember:
            self._select_rememberme_checkbox()

    def login_with_valid_credentials(self, username='admin', password='Admin123#', remember=False):

        self._enter_valid_credentials(username, password, remember)

        self._click_login_button()

        if username != 'admin':
            logger.info("landing to User Profile page in case of NON ADMIN user")
            return UserProfile(self.driver)

        logger.info("landing to Add User page in case of ADMIN user")
        return AddUser(self.driver)

    def login_with_invalid_credentials(self, username, password, remember=False):
        self._enter_valid_credentials(username, password, remember)

        self._click_login_button()

        return self

    def _get_field_text(self, locator):

        wait = WebDriverWait(self.driver, 10)

        wait.until(expected_conditions.visibility_of_element_located(locator))

        text = self.driver.find_element(*locator).get_property("value")
        logger.info("Data fetched from locator is {}".format(text))

        return text

    def verify_username_already_filled_on_page(self, username):

        username_already_filled = self._get_field_text(self.USERNAME)

        logger.info("username filled in the input box {}  and username to verify  {}".format(username_already_filled, username))
        assert username == username_already_filled









