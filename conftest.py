import pytest
import json
from selenium import webdriver

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

@pytest.fixture
def driver():

    config_data = read_config_file()

    if "browser" not in config_data:
        logger.info("Assigning Firefox as a default browser")

        config_data["browser"] = "firefox"

    if "web_url" not in config_data:
        raise KeyError("No URL found in config.json")

    driver = init_driver(config_data["web_url"], config_data["browser"])

    yield driver
    if driver is not None:
        driver.quit()


def read_config_file():
    with open('config/default.json') as config_file:
        data = json.load(config_file)
        logger.info("getting the config data : {}".format(data))
    return data


def init_driver(url, browser):

    if browser.lower() == "firefox":

        """
        ** Different way to initaialize Browser ***
        
        #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        #get_driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        
        """
        get_driver = webdriver.Firefox()

    elif browser.lower() == "chrome":

        """
        # driver = webdriver.Chrome(executable_path=/usr/local/bin/chromedriver)
        """
        get_driver = webdriver.Chrome()

    else:
        raise Exception(f'"{browser}" is not a supported browser')

    get_driver.get(url)
    get_driver.set_page_load_timeout(10)
    get_driver.implicitly_wait(10)

    return get_driver





