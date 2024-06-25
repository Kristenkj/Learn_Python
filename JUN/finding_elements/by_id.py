from selenium.webdriver.common.by import By
from selenium import webdriver
import pdb



url = "http://demostore.supersqa.com"

driver = webdriver.Chrome()
driver.get(url)

cart = driver.find_element(By.ID, "site-header-cart")
cart.click()
driver.back()

driver.get('http://demostore.superqa.com/my-account/')
u_name = driver.find_element(By.ID, 'username')
u_name.send_keys("myusername")
pdb.set_trace() #able to manipulate site through terminal
#Note: to find available methods just do dir(<variable>)
#Example: dir(driver)
#Example: dir(cart)

driver.quit()
