from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://rahulshettyacademy.com/AutomationPractice/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

element_displayed = driver.find_elements(By.CSS_SELECTOR, ".btn-style class2")
displayed_text = driver.find_element(By.NAME, "show-hide")

#Option 1
for element in element_displayed:
    if element.get_attribute('value') == "Show":
        element.click()
        assert displayed_text.is_displayed()
        break

#Option 2
assert displayed_text.is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not displayed_text.is_displayed()

driver.quit()
