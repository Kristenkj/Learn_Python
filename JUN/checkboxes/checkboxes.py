import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/checkboxes/checkbox_example.html"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

to_select_value = "61-80"
locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'

my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
my_choice.click()
assert my_choice.is_selected(), f"After clicking value {to_select_value} it is not selected."
time.sleep(3)

driver.quit()
