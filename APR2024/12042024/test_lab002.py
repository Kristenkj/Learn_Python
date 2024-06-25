#Selenium - Automates Browsers
# Selenium 3 - 20% - JSON wire protocol
# Selenium 4 - 70% (migrated to Selenium 4) - W3C protocol
# pip install selenium --> 4.x --> You don't have to setup the browser drivers

from selenium import webdriver

def test_open_vwologin():
    driver = webdriver.Chrome() #Create a session - POST request
    driver.get("https://app.vwo.com") #GET Request to URL parameter
    assert driver.title == "Login - VWO"
    print(driver.title)

    # Python Interpretator --> If there is no command , I will stop the execution