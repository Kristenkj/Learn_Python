#Static Dropdown - Select tag signifies static and able to use Select class
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = "https://rahulshettyacademy.com/angularpractice/"

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Kristen")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text

driver.quit()
