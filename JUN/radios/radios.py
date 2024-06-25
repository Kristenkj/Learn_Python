from selenium import webdriver
from selenium.webdriver.common.by import By

import time


url = ("file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/radios/radios_example.html")

driver = webdriver.Chrome()
driver.get(url)

expected_default_value = '21-40'
locator_by_value = 'input[name="age-group-radio"][value="{value}"]'

#Example 1: Verify default is selected
default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format(value=expected_default_value))
assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected"



"""
to_select_value = "21-40"

my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
my_choice.click()
assert my_choice.is_selected(), f"After clicking value {to_select_value} it is not selected."
time.sleep(3)
"""

driver.quit()