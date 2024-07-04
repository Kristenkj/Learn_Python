from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

url = "https://rahulshettyacademy.com/AutomationPractice/"

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)

action = ActionChains(driver)
#Double Click: action.double_click(driver.find_element(By.ID))
# Right click: action.context_click().perform()
#action.drag_and_drop().perform()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() #moves to element and doesn't perform any operation
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
