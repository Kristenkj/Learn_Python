import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/dropdowns/drop_down_example.html")
my_option = driver.find_element(By.ID, 'dropdownMenuButton')
my_option.click()
time.sleep(3)
my_acct = driver.find_element(By.LINK_TEXT, "My Account")
my_acct.click()
time.sleep(3)


driver.quit()
