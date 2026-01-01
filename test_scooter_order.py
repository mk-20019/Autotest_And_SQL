# Михаил Тогалаков, 39-я когорта: Финальный проект. Инженер по тестированию плюс

import requests
import pytest

scooter_URL = "https://babe7e11-6013-446c-a98e-1750bd163b05.serverhub.praktikum-services.ru/api/v1"
# объявляю фикстуру, чтобы предварительно собрать вариабельные данные для теста: в нашем случае - это трэк-номер заказа для его последующей передачи в get-запросе
@pytest.fixture(scope="session")
def tracking_number():
    url = f"{scooter_URL}/orders" # тут можно задать переменную url и без f-строки, используя конкатенацию scooter_URL + /orders
    order_body = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Пушкина, 10",
        "metroStation": 4,
        "phone": "+79998889988",
        "rentTime": 5,
        "deliveryDate": "2026-01-03",
        "comment": "Ыфыфыфыф",
        "color": ["BLACK"]
    }
    resp = requests.post(url, json=order_body)
    assert resp.status_code == 201
    data = resp.json()
    tn = data.get("track") # api скутера использует "track" для хранения данных трэк-номера (tn - tracking number)
    assert tn is not None # дополнительная проверка, что в ответе на post-запрос передается искомое значение, например: "track": 1234
    return tn 
# объявляю проверку на получение заказа по его tn: критерий успеха - статус 200
def test_check_order_status(tracking_number):
    url = f"{scooter_URL}/orders/track" # согласно документации api скутера, через данный адрес сервер передает информацию по созданному заказу по его tn
    params = {"t": tracking_number} # объявляю параметры, чтобы питон прочитал get-запрос корректно в нашем api, т.е. в формате GET …/orders/track?t=1234
    resp = requests.get(url, params=params)
    assert resp.status_code == 200
