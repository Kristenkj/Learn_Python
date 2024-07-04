from selenium import  webdriver

url="https://the-internet.herokuapp.com/iframe"
driver=webdriver.Edge()
driver.implicitly_wait(2)
driver.get(url)
driver.maximize_window()




driver.quit()
