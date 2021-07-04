import pytest
import requests
from json import dumps, loads
from test_api import api_urls
from test_api.headers import HEADERS


@pytest.fixture()
def user_data():
    data = {
        "username": "admin",
        "password": "password123"
    }
    return data


@pytest.fixture()
def book_data():
    book_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return book_data


@pytest.fixture()
def booking_token(user_data):
    auth_response = requests.post(
        url=api_urls.AUTH_CREATE_TOKEN,
        headers=HEADERS,
        data=dumps(user_data)
    )
    booking_token = loads(auth_response.text)["token"]
    assert auth_response.status_code == 200
    headers_token = {"Content-Type": "application/json",
                     'Cookie': f'token={booking_token}'}
    return headers_token


@pytest.fixture()
def updated_book_data():
    updated_book_data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Dinner"
    }
    return updated_book_data


@pytest.fixture()
def booking_id():
    get_booking_id_s_response = requests.get(
        url=api_urls.GET_BOOKING,
        headers=HEADERS
    )
    unique_booking_id_s = loads(get_booking_id_s_response.text)
    assert get_booking_id_s_response.status_code == 200

    booking_id = str(unique_booking_id_s[0]['bookingid'])
    return booking_id


@pytest.fixture()
def patch_book_data():
    patch_book_data = {
        "totalprice": 666,
        "additionalneeds": "Stop eating< sick bastard"
    }
    return patch_book_data
