
from selenium import webdriver


url = ("https://rahulshettyacademy.com/AutomationPractice/")

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
driver.maximize_window()

#scrolls the length of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#take a screenshot
driver.get_screenshot_as_file("screen.png")

#driver.quit()
