import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/checkboxes/checkbox_example.html"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

#Verify the number of checkboxes and they are selected
expected_number_of_options = 4
all_checkboxes = driver.find_elements(By.NAME, "age-group-checkbox")
assert len(all_checkboxes) == expected_number_of_options, "Number of checkboxes is not 4 "


for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkbox with value '{value} 'is selectable")
    else:
        raise Exception(f"Value '{value}' is not selectable")


driver.quit()
