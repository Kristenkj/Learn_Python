import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com/")

search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('hoodie')
time.sleep(3)
search_field.send_keys(Keys.ENTER)

driver.quit()