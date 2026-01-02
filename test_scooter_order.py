# Михаил Тогалаков, 39-я когорта: Финальный проект. Инженер по тестированию плюс

import requests
import pytest
import data

@pytest.fixture(scope="session")
def tracking_number():
    url = data.scooter_URL + data.sc_ENDPOINTS["create_order"]
    resp = requests.post(url, json=data.order_body)
    assert resp.status_code == 201
    body = resp.json()
    tn = body.get(data.track_resp_name)
    assert tn is not None
    return tn

def test_check_order_status(tracking_number):
    url = data.scooter_URL + data.sc_ENDPOINTS["track_order"]
    params = {data.track_api_name: tracking_number}
    resp = requests.get(url, params=params)
    assert resp.status_code == 200
