import logging
from selenium import webdriver


def test_print_logs():
    LOGGER = logging.getLogger(__name__)

    LOGGER.info("This is information logs")

#@pytest.mark.smoke
def test_open_vwologin():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome() #POST Request | Create the session
    driver.get("https://app.vwo.com") #GET Request to URL parameter
    print(driver.title)
    LOGGER.info(driver.title)
    assert driver.title == "Login - VWO"