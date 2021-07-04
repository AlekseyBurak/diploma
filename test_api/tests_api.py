import requests
from json import dumps, loads
from test_api import api_urls
from test_api.headers import HEADERS


class TestAPIBooker:

    def test_health_check(self):
        health_check_response = requests.get(
            url=api_urls.PING
        )
        assert health_check_response.status_code == 201

    def test_auth(self, user_data):
        auth_response = requests.post(
            url=api_urls.AUTH_CREATE_TOKEN,
            headers=HEADERS,
            data=dumps(user_data)
        )
        assert auth_response.status_code == 200

    def test_get_booking_id_s(self):
        get_booking_id_s_response = requests.get(
            url=api_urls.GET_BOOKING,
            headers=HEADERS
        )
        assert get_booking_id_s_response.status_code == 200

    def test_get_booking_by_id(self, booking_id):
        get_booking_response = requests.get(
            url=api_urls.GET_BOOKING + f"/{booking_id}",
            headers=HEADERS
        )
        assert get_booking_response.status_code == 200

    def test_get_booking_by_name(self):
        get_booking_by_name_response = requests.get(
            url=api_urls.GET_BOOKING.format(lastname="Brown"),
            headers=HEADERS,
        )
        assert get_booking_by_name_response.status_code == 200

    def test_get_booking_by_date(self):
        get_booking_by_name_response = requests.get(
            url=api_urls.GET_BOOKING.format(checkin="2013-02-23"),
            headers=HEADERS,
        )
        assert get_booking_by_name_response.status_code == 200

    def test_create_booking(self, book_data):
        create_book_response = requests.post(
            url=api_urls.CREATE_BOOK,
            headers=HEADERS,
            data=dumps(book_data)
        )
        assert create_book_response.status_code == 200

    def test_update_booking(self, updated_book_data, booking_token, booking_id):
        update_boor_response = requests.put(
            url=api_urls.UPDATE_BOOKING + f"/{booking_id}",
            headers=booking_token,
            data=dumps(updated_book_data),
        )
        assert update_boor_response.status_code == 200
        get_booking_response = requests.get(
            url=api_urls.GET_BOOKING + f"/{booking_id}",
            headers=HEADERS
        )
        assert loads(get_booking_response.text) == updated_book_data

    def test_patch_booking(self, patch_book_data, booking_token, booking_id):
        update_boor_response = requests.patch(
            url=api_urls.UPDATE_BOOKING + f"/{booking_id}",
            headers=booking_token,
            data=dumps(patch_book_data),
        )
        assert update_boor_response.status_code == 200
        get_booking_response = requests.get(
            url=api_urls.GET_BOOKING + f"/{booking_id}",
            headers=HEADERS
        )
        patched_values = loads(get_booking_response.text)
        for ith in patch_book_data:
            assert patch_book_data[ith] == patched_values[ith]

    def test_delete_booking(self, booking_token, booking_id):
        delete_booking_response = requests.delete(
            url=api_urls.DELETE_BOOKING + f'/{booking_id}',
            headers=booking_token,
        )
        assert delete_booking_response.status_code == 201
        get_booking_response = requests.get(
            url=api_urls.GET_BOOKING + f"/{booking_id}",
            headers=HEADERS
        )
        assert get_booking_response.status_code == 404
