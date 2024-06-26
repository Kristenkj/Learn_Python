from selenium import webdriver
from selenium.webdriver.common.by import By

#must be 'a' tag or it will fail

url = "http://demostore.supersqa.com/"

driver = webdriver.Chrome()
driver.get(url)

cart_elm = driver.find_element(By.LINK_TEXT, "Cart")
print(cart_elm.text)

acct_elm = driver.find_element(By.LINK_TEXT, "My account")
print(acct_elm.text)

driver.quit()
