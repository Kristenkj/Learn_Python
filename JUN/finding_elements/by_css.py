from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
CSS is the best selector after ID. It is easy to write and fast after ID. Also, better than XPATH.
Use id or class as css locator
'.' is for class
'#' is for id

"""

url = "https://rahulshettyacademy.com/angularpractice/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

name = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
name.send_keys("Kristen")

email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
email.send_keys("sample@gmail.com")

password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password.send_keys("password1")

checkbox = driver.find_element(By.CSS_SELECTOR, "input[id='exampleCheck1']")
checkbox.click()

student_status = driver.find_element(By.CSS_SELECTOR, "#inlineRadio1")
student_status.click()

two_way_binding = driver.find_element(By.CSS_SELECTOR, "input[class='ng-untouched ng-pristine ng-valid']")
two_way_binding.send_keys("Hello World")
two_way_binding.clear()

time.sleep(3)
driver.quit()
