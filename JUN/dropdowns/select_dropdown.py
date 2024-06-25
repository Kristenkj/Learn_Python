import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/dropdowns/drop_down_example.html")
age_range = driver.find_element(By.ID, 'age-range-select')
dropdown_object = Select(age_range)
time.sleep(3)
dropdown_object.select_by_index(3)
time.sleep(3)
dropdown_object.select_by_value('21-40')
all_options = dropdown_object.options
for option in all_options:
    print(option.text)

time.sleep(5)

driver.quit()
