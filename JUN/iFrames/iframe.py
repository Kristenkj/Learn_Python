from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/iFrames/iFrames_example.html"
driver = webdriver.Chrome()
driver.get(url)
"""
#example outside of iFrame
driver.find_element(By.ID, 'btnOutFrame').click()
my_alert = driver.switch_to.alert
my_alert_text = my_alert.text
assert my_alert_text == 'Just Clicked Outside iFrame', "Should've gotten outside message"
my_alert.dismiss()
time.sleep(3)

#example of iFrame - using webelement
my_frame = driver.find_element(By.ID, 'myFrame1')
driver.switch_to.frame(my_frame)
driver.find_element(By.ID, 'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()
time.sleep(3)
driver.switch_to.default_content() #Goes back out of the iframe to the main page
driver.find_element(By.ID, 'btnOutFrame').click()
time.sleep(3)


#example of iFrame - using ID
driver.switch_to.frame('myFrame1')
driver.find_element(By.ID, 'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()
driver.switch_to.default_content()
"""
#example of iFrame using index
driver.switch_to.frame(0)
driver.find_element(By.ID, 'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(3)
driver.quit()
