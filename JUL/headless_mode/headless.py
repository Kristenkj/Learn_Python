"""
Test runs in invisible mode. Will still use selected browser to run but will not see from the front end
Some consider it to be faster.
"""
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")



driver = webdriver.ChromeOptions(options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.quit()
