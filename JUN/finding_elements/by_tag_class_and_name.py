from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://demostore.supersqa.com/"

driver = webdriver.Chrome()
driver.get(url)

#Example: Class name
product = driver.find_element(By.CLASS_NAME, 'product') #only gives 1st product found
products = driver.find_elements(By.CLASS_NAME, 'product')#Provides list

print(product)
print('********************')
print(products)
print('********************')
#Example: Name
order_by = driver.find_element(By.NAME, 'orderby')
print(order_by.text)

#Example: tag
#Links on page
all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Found number of 'a' tag : {len(all_links)}")
all_li = driver.find_elements(By.TAG_NAME, 'li')
print(f"Found number of 'li' tag: {len(all_li)}")

driver.quit()
