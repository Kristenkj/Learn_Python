import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Verify the trial has expired")
@allure.description("TC#1 - Verify that the trial period for the account has expired")
def test_idrive_360():
    #open site
    driver = webdriver.Chrome()
    driver.get("https://www.idrive.com/endpoint-backup/")

    #verify site url
    assert driver.current_url == "https://www.idrive.com/endpoint-backup/"
    time.sleep(3)

    #login to site
    login_element = driver.find_element(By.XPATH, "//a[@class='signup']")
    login_element.click()

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)

    #verify login page url
    assert driver.current_url == "https://www.idrive360.com/enterprise/login"
    time.sleep(10)

    #Enter acct details
    email_element = driver.find_element(By.XPATH, "//input[@id='username']")
    email_element.send_keys("augtest_040823@idrive.com")

    password_element = driver.find_element(By.XPATH, "//input[@name='password']")
    password_element.send_keys("123456")

    sign_in_button = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    sign_in_button.click()

    allure.attach(driver.get_screenshot_as_png(), name="Signin-screenshot", attachment_type=AttachmentType.PNG)

    time.sleep(5)
    #Verify URL and error message
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error Message 1"
    msg_element = driver.find_element(By.CLASS_NAME, "id-card-title")
    assert msg_element.text == "Your free trial has expired"

    allure.attach(driver.get_screenshot_as_png(), name="account_trial_expired-screenshot",
                  attachment_type=AttachmentType.PNG)

    driver.quit()
