from selenium import webdriver
from selenium.webdriver.common.by import By

import time


url = ("file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/radios/radios_example.html")

driver = webdriver.Chrome()
driver.get(url)

expected_default_value = '21-40'
locator_by_value = 'input[name="age-group-radio"][value="{value}"]'

expected_values = ['21-40', '41-60', '61-80', '81+']
all_radios = driver.find_elements(By.NAME, 'age-group-radio')
assert len(all_radios) == len(expected_values), "The number of radios doesn't match the expected."\
                                                "Expected: {} , Actual: {}".format(len(expected_values), len(all_radios))
driver.quit()
