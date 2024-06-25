from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "file:///C:/Users/jones/Python-Programs/TTA2x/Python_Coding/JUN/presents_vs_displayed/present_vs_displayed.html"

driver.get(url)
my_btn1 = driver.find_element(By.ID, "btn1")
my_btn1_text = my_btn1.text
print("First button text: {}".format(my_btn1_text))

my_btn2 = driver.find_element(By.ID, "btn2")
my_btn2_text = my_btn2.text
print("First button text: {}".format(my_btn2_text))

my_btn3 = driver.find_element(By.ID, "btn3")
my_btn3_text = my_btn3.text
print("First button text: {}".format(my_btn3_text))

my_btn4 = driver.find_element(By.ID, "btn4")
my_btn4_text = my_btn4.text
print("First button text: {}".format(my_btn4_text))

if my_btn4.is_displayed():
    my_btn4.click()
else:
    raise Exception("Button 4 is not displayed")
