"""
This challenge automates the login process of a website
and asserts that when the user logs in they are taken to the appropriate page.
Within this challenge I also calculate how long it takes for the test to run.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://demo.applitools.com/"

driver = webdriver.Chrome()
driver.implicitly_wait(10)
start_time = time.time()
driver.get(url)

u_name = driver.find_element(By.ID, "username")
p_word = driver.find_element(By.ID, "password")
sign_in_btn = driver.find_element(By.ID, "log-in")
c_box = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
amt_spent = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) span")
sum = 0

#Login Page
u_name.send_keys("Admin")
p_word.send_keys("Password@123")
c_box.click()
sign_in_btn.click()



#Dashboard Page
for amount in amt_spent:
    print(amount.text)
    sum = sum + int(amount.text)

print(sum)

assert driver.current_url == "https://demo.applitools.com/app.html"

end_time = time.time()
driver.quit()

print(round((end_time - start_time), 3), " secs")
