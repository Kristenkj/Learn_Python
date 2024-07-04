
from selenium.webdriver.common.by import By
from selenium import webdriver


url = "https://the-internet.herokuapp.com/windows"

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get(url)

click_here_operation = driver.find_element(By.LINK_TEXT, "Click Here").click()

#Get window name - Grabs all window handles that were opened and puts them into a list. Starts with 0 index
windows_opened = driver.window_handles

# Switch to specific window
driver.switch_to.window(windows_opened[1])
new_window_tag = driver.find_element(By.TAG_NAME, "h3").text
print(new_window_tag)
driver.close()
driver.switch_to.window(windows_opened[0])

driver.quit()
