import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_name_input():
    #Open the site
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    #Locate the first and last name input fields
    first_name_field = driver.find_element(By.NAME, "firstname")
    last_name_field = driver.find_element(By.NAME, "lastname")

    first_name = "Kristen"
    first_name_field.send_keys(first_name)
    last_name = "Jones"
    last_name_field.send_keys(last_name)

    assert first_name_field.get_attribute("value") == first_name, "First name input error"
    assert last_name_field.get_attribute("value") == last_name, "Last name input error"

    time.sleep(15)

    driver.quit()


def test_firstname_input_uppercase():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_name_field = driver.find_element(By.NAME, "firstname")
    last_name_field = driver.find_element(By.NAME, "lastname")

    first_name = "Issac"
    actions = ActionChains(driver)
    actions.click(first_name_field)
    for char in first_name:
        actions.key_down(Keys.SHIFT).send_keys(char).key_up(Keys.SHIFT)
    actions.perform()

    last_name = "Rob"
    last_name_field.send_keys(last_name)

    assert first_name_field.get_attribute("value") == first_name.upper(), "First name input error"
    assert last_name_field.get_attribute("value") == last_name, "Last name input error"

    time.sleep(20)

    driver.quit()


def test_both_name_input_upper():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_name_field = driver.find_element(By.NAME, "firstname")
    last_name_field = driver.find_element(By.NAME, "lastname")

    actions = ActionChains(driver)

    #Input the first name in uppercase
    actions.click(first_name_field).key_down(Keys.SHIFT).send_keys("rosie").key_up(Keys.SHIFT).perform()

    #Clear actions and prepare for the next input
    actions.reset_actions()

    #Input the last name in uppercase
    actions.click(last_name_field).key_down(Keys.SHIFT).send_keys("Parker").key_up(Keys.SHIFT).perform()

    assert first_name_field.get_attribute("value") == "ROSIE", "First name input error"
    assert last_name_field.get_attribute("value") == "PARKER", "Last name input error"

    time.sleep(7)

    driver.quit()
