from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/waits/page_with_slow_image.html")

my_image = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "the_slow_image")))

print("Found Image")

driver.quit()

