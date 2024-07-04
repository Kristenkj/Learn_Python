import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


#service_obj = Service("C:\Users\jones\Documents\BrowserDrivers\chromedriver-win32.exe")
#webdriver.Chrome(service=service_obj)

url = "https://rahulshettyacademy.com"
driver = webdriver.Firefox()
driver.get(url)


time.sleep(3)
driver.quit()
