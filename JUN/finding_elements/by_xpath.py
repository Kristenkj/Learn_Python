from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://demostore.supersqa.com/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
"""
Relative XPATH -  Starts with //
    //tag[@attribute='value']
    //*[@attibute='value']

Absolute XPATH - Full path from the root. Unstable: Able to be broken easily. Starts with /
"""

cart = driver.find_element(By.XPATH, "//a[@class='cart-contents']")
home_btn = driver.find_element(By.XPATH, "//ul[@class='nav-menu']/li[1]")
album_atc_btn = driver.find_element(By.XPATH, "//a[@data-product_sku='woo-album']")
my_acct_btn = driver.find_element(By.XPATH, "//ul[@class='nav-menu']/li[4]")


#cart.click()
my_acct_btn.click()
driver.back()
home_btn.click()
#album_atc_btn.click()



driver.quit()
