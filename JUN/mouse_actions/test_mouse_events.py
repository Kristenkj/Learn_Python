import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pytest


def test_click():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")


def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    driver.maximize_window()

    actions = ActionChains(driver)
    element_a = driver.find_element(By.ID, "column-a")
    element_b = driver.find_element(By.ID, "column-b")

    actions.click_and_hold(element_a).move_to_element(element_b).release(element_b).perform()
    time.sleep(10)
    actions.click_and_hold(element_b).move_to_element(element_a).release(element_a).perform()
    time.sleep(10)

    driver.quit()

