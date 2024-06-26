from selenium import webdriver
from selenium.webdriver.common.by import By

#must be 'a' tag or it will fail

url = "http://demostore.supersqa.com/"

driver = webdriver.Chrome()
driver.get(url)

cart_elm_p = driver.find_element(By.PARTIAL_LINK_TEXT, "art")
print(cart_elm_p.text)

acct_elm_p = driver.find_element(By.PARTIAL_LINK_TEXT, "acc")
print(acct_elm_p.text)

footer_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Built with")
print(footer_link.text)

driver.quit()
