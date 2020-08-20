from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .common import Page

import logging

logger = logging.getLogger()

class ViewUser(Page):

    """
    This Class meant to provide following:
        - Locators of Web elements on ViewUser Page
        - Supporting Methods to interact on Page
    """

    SEARCHBOX = (By.XPATH, "//input[@ng-model='search']")

    USERTABLE = (By.ID, "userTable")

    DELETE_USER = [By.XPATH, "//tr/td[position()=1 and text()='{}']/following-sibling::td[last()]/span"]

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._wait_for_pageload()

    def _wait_for_pageload(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self.SEARCHBOX))

    def _search_user(self, user_initial):

        logger.info("Search Box : providing the String to Search out the Details in user table.")
        self.driver.find_element(*self.SEARCHBOX)

        self.driver.find_element(*self.SEARCHBOX).send_keys(user_initial)

    def read_user_table_data(self):

        logger.info("Getting the data from User table and storing it")
        table_data = []
        table = self.driver.find_element(*self.USERTABLE)
        header_data = []
        header = table.find_elements(By.TAG_NAME, "th")
        for name in header:
            header_data.append(name.text)
        rows = table.find_elements(By.XPATH, "//tbody/tr")
        for row in rows:
            row_data = {}
            cols = row.find_elements(By.TAG_NAME, "td")

            for index, col in enumerate(cols):
                row_data[header_data[index]] = col.text
            table_data.append(row_data)
        logger.info("user data found present on user table page: {}".format(table_data))
        return table_data

    def _compare_dict(self, d1, d2, ignore_keys=None):

        """"

        :param d1: dict
        :param d2: dict object to be checked for presense
        :param ignore_keys : keys to be ignore while comparison
        :return: Boolean - True if match else False
        """

        ignored = set(ignore_keys)
        for k1, v1 in d1.items():
            if k1 not in ignored and (k1 not in d2 or d2[k1] != v1):
                return False
        for k2, v2 in d2.items():
            if k2 not in ignored and k2 not in d1:
                return False
        return True

    def verify_user_present(self, user_data):

        """
        :param user_data: data is dictionary which contains the user information
        :return: Boolean : True/False as result Validation
        """
        table_data = self.read_user_table_data()
        counter = 0
        for data in table_data:
            if self._compare_dict(data, user_data, ['Action']):
                logging.info("user_data {} present in table_data {}".format(user_data, table_data))
                counter += 1

        if counter != 1:
            logging.error("expected user_data {} not present/ present more than once in table {}".\
                          format(user_data, table_data))
            assert False

    def _verify_user_not_present(self, userid):

        logger.info("Checking the user is deleted properly or not.")

        self.DELETE_USER[1] = self.DELETE_USER[1].format(userid)
        assert len(self.driver.find_elements(*self.DELETE_USER)) == 0

    def _delete_user(self, userid):

        self.DELETE_USER[1] = self.DELETE_USER[1].format(userid)
        elems = self.driver.find_elements(*self.DELETE_USER)
        if userid == "admin":
            logger.info("Admin user can not be deleted , Delete button not present")
            assert len(elems) == 0
        else:
            assert len(elems) == 1

            logger.info("Non Admin user : {} , Delete button is present".format(userid))
            self.driver.find_elements(elems[0]).click()
            logger.info("Deleting Non Admin user : {}".format(userid))
            self._verify_user_not_present(userid)













