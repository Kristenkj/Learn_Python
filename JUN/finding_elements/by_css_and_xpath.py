from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "http://demostore.supersqa.com/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

cart = driver.find_element(By.CSS_SELECTOR, "#site-header-cart > li:nth-child(1) > a")
time.sleep(2)
cart.click()

my_acct = driver.find_element(By.XPATH, "//*[@id='site-navigation']/div[1]/ul/li[4]/a")
time.sleep(2)
my_acct.click()


driver.quit()
