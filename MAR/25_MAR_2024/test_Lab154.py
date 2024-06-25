# API Request - HTTP Request

import pytest  #pip install pytest
import requests  # pip install requests
import allure  # pip install allure


@allure.title("Create Booking CRUD")
@allure.description("TC#1 - Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive():
    # To make a request we need this data:
    #    1.URL
    #    2.Method
    #    3.Headers
    #   4. Payload/Data/Body
    #    5. Auth (No Auth in post
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Kristen",
        "lastname": "Jones",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-01",
            "checkout": "2024-05-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)

    #Response Body Verification
    #Headers
    #Status Code
    #JSON Schema
    #Validation
    #Time Response

    assert response.status_code == 200
    print(response.headers)
    response_json = response.json()
    booking_id = response_json()["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int
    firstname = response_json["booking"]["firstname"]
    lastname = response_json["booking"]["lastname"]
    checkin = response_json["booking"]["bookingdates"]["checkin"]
    assert firstname == "Kristen"
    assert lastname == "Jones"
    assert checkin == "2024-04-01"


@allure.title("Create Booking CRUD")
@allure.description("TC#2 - Verify the create booking with invalid data")
@pytest.mark.crud
@pytest.mark.negative
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 500
