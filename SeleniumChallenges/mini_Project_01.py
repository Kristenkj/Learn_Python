"""
This challenge automates the booking process for a healthcare website.
"""

from selenium.webdriver.support.ui import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_open_demo_url():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    element = driver.find_element(By.ID, "btn-make-appointment")
    element.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)

    email_element = driver.find_element(By.NAME, "username")
    email_element.send_keys("John Doe")

    password_element = driver.find_element(By.ID, "txt-password")
    password_element.send_keys("ThisIsNotAPassword")

    button_element = driver.find_element(By.ID, "btn-login")
    button_element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

# Facility Dropdown Selector
    drop_down_element = driver.find_element(By.ID, "combo_facility")
    dropdown = Select(drop_down_element)
    dropdown.select_by_index(1)

#Healthcare Program Selector
    program_selector = driver.find_element(By.ID, 'radio_program_medicaid')
    program_selector.click()

#Calendar Date Selector
    date_element = driver.find_element(By.ID,"txt_visit_date")
    date_element.send_keys('25/02/2024')

    #Book Appointment Button
    book_button_element = driver.find_element(By.ID, "btn-book-appointment")
    book_button_element.click()

    driver.quit()
