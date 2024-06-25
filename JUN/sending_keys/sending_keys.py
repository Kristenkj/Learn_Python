from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com/my-account/")

u_name = driver.find_element(By.ID, "username")
u_name.send_keys('abcde')
p_name = driver.find_element(By.ID, 'password')
p_name.send_keys('abcds')
p_show_input = driver.find_element(By.CLASS_NAME, 'show-password-input')
p_show_input.click()
login_btn = driver.find_element(By.NAME, 'login')
login_btn.click()

driver.quit()


