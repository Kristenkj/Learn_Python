import time
from selenium.webdriver.common.by import By
from selenium import webdriver

url = "file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/multiple_windows_and_tabs/windows-and_tabs_example.html"
driver = webdriver.Chrome()

driver.get(url)

driver.find_element('xpath', '//*[@id="windows"]/a[1]').click()


print("Before switching focus: " + driver.title)

all_window_handles = driver.window_handles
original_window_handle = all_window_handles[0]
new_window = all_window_handles[1]
driver.switch_to.window(new_window)

print("After switching focus: " + driver.title)
print("Closing tab")
driver.close()
time.sleep(5)
print("Switching back to original")
time.sleep(5)

driver.switch_to.window(original_window_handle)
driver.find_element(By.XPATH, '//*[@id="windows"]/a[2]').click()
new_window2 = all_window_handles[2]
driver.switch_to.window(new_window2)
print("After switching focus: " + driver.title)
driver.close()
time.sleep(5)

driver.switch_to.window(original_window_handle)
print("After switching focus: " + driver.title)
time.sleep(5)

driver.quit()


