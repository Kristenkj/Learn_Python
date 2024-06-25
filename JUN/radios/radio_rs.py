from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://rahulshettyacademy.com/AutomationPractice/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

radio_options = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radio_options))

#option 1 - Use when you don't know if the elements will stay the same
for radio in radio_options:
    if radio.get_attribute('value') == "radio3":
        radio.click()
        assert radio.is_selected()
        break

#Option 2 - Use if you know the elements will remain in the same index
radio_options[1].click()
assert radio_options[1].is_selected()

driver.quit()
