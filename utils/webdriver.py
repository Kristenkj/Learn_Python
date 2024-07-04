from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    @staticmethod
    def Chrome():
        return webdriver.Chrome(ChromeDriverManager().install())

    @staticmethod
    def Firefox():
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
