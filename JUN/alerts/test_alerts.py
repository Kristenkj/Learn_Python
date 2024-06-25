import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    js_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    assert js_alert_button.text == 'Click for JS Alert', "Button text for JS Alert is incorrect"
    js_alert_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == 'I am a JS Alert', "Alert text for JS Alert is incorrect"
    alert.accept()

    time.sleep(10)

    result = driver.find_element(By.ID, "result")
    print(result)

    driver.quit()


def test_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    js_prompt_button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    assert js_prompt_button.text == 'Click for JS Prompt', "Button text for JS Prompt is incorrect"
    js_prompt_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())  #Wait for the alert
    alert = driver.switch_to.alert  #Switch to the alert
    assert alert.text == 'I am a JS prompt', "Alert text for JS Prompt is incorrect"
    alert.send_keys("Kristen")  #If able to enter send input
    alert.accept()  #accept or dismiss the alert - alert.dismiss()

    time.sleep(10)

    result = driver.find_element(By.ID, 'result')
    print(result.text)
    assert "Kristen" in result.text

    driver.quit()
