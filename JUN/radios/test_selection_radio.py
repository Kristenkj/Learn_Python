import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_gender_female():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    gender_female = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sex-1"))
    )

    time.sleep(2)

    gender_female.click()

    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.element_located_to_be_selected((By.ID, "sex-1"))
    )
    time.sleep(2)
    if gender_female.is_selected():
        print("Female gender is selected.")
    assert gender_female.is_selected(), "Female gender should be selected"

    driver.quit()


def test_gender_male():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    gender_male = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sex-0"))
    )

    time.sleep(2)

    gender_male.click()

    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.element_located_to_be_selected((By.ID, "sex-0"))
    )
    time.sleep(2)
    if gender_male.is_selected():
        print("Male gender is selected.")
    assert gender_male.is_selected(), "Male gender should be selected."

    driver.quit()


def test_years_of_exp():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    try:
        years_of_experience = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "exp-3"))
        )

        time.sleep(2)

        years_of_experience.click()

        # Wait to ensure the click action is performed
        WebDriverWait(driver, 10).until(
            EC.element_located_to_be_selected((By.ID, "exp-3"))
        )

        time.sleep(2)

        # Assert that the correct radio button is selected based on its value
        selected_year = years_of_experience.get_attribute("value")
        expected_value = "4"  # Adjust the expected value as needed

        assert selected_year == expected_value, f"Expected value '{expected_value}', but got '{selected_year}'."

        # Print a confirmation message
        if selected_year == expected_value:
            print(f"{selected_year} years of experience is selected.")

        time.sleep(2)
    finally:
        driver.quit()
