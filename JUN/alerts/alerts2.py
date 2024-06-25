import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/alerts/alerts_example.html"

driver = webdriver.Chrome()
driver.get(url)

my_js_confirm_btn = driver.find_element(By.CSS_SELECTOR, 'div#jsConfirmExample button')
my_js_confirm_btn.click()
time.sleep(3)
my_confirm_alert = driver.switch_to.alert
time.sleep(3)
"""
my_confirm_alert.accept()
rs_message = driver.find_element(By.ID, 'userResponse1').text
assert rs_message == "Great! You will love it!", "Wrong message after accepting."
"""

my_confirm_alert.dismiss()
rs_message = driver.find_element(By.ID, 'userResponse1').text
assert rs_message == "Too bad!!! You would've loved it!", "Wrong message after accepting."
driver.quit()
