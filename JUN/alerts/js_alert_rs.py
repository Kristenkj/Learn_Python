from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://rahulshettyacademy.com/AutomationPractice/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

name = "Kristen"
name_input = driver.find_element(By.ID, "name")
alert_btn = driver.find_element(By.ID, "alertbtn")

name_input.send_keys(name)
alert_btn.click()

alert = driver.switch_to.alert
alert_text = alert.text
assert name in alert_text
print(alert_text)
alert.accept()


driver.quit()
