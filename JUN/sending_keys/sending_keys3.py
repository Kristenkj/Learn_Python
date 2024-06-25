import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com/my-account/')
u_name = driver.find_element(By.ID, 'username')
u_name.send_keys('abcds')
u_name.send_keys(Keys.TAB)
time.sleep(3)
driver.quit()
