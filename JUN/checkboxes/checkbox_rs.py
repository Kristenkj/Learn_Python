from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://rahulshettyacademy.com/AutomationPractice/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

cb_options = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(cb_options))
for checkbox in cb_options:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


driver.quit()

