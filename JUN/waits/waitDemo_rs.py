import time

from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://rahulshettyacademy.com/seleniumPractise/#/"

driver = webdriver.Chrome()
driver.implicitly_wait(10) #10 seconds is the max timeout. If object displayed in less than 10 secs it will save time and proceed to next step in test. Global timeout.
driver.get(url)
driver.maximize_window()

search_bar = driver.find_element(By.CSS_SELECTOR,".search-keyword")
beetroot_atc_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[4]/div[3]/button')

beetroot_atc_btn.click()


search_bar.send_keys("ber")

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for product in results:
    product.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

driver.quit()
