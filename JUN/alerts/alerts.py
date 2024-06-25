import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/alerts/alerts_example.html"

driver = webdriver.Chrome()
driver.get(url)

alert1_btn = driver.find_element(By.CSS_SELECTOR, 'div#jsAlertExample button')
alert1_btn.click()

time.sleep(3)
my_alert = driver.switch_to.alert
assert my_alert.text == "I am a JavaScript Alert", "Unexpected text on alert"
my_alert.accept()
#my_alert.dismiss() #Can be used in place of accept

driver.quit()
