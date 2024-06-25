from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get("file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/waits/page_with_slow_image.html")
my_image = driver.find_element('id',"the_slow_image")
my_image.click()
print("Found Image")
