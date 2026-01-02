# апи скутера
scooter_URL = "https://5a69b3e4-0cf8-4171-ac9c-1d89cd70b648.serverhub.praktikum-services.ru/api/v1"

# эндпоинты апи: создание для post-запроса и трэкинг заказа для get-запроса
sc_ENDPOINTS = {
    "create_order": "/orders",
    "track_order":  "/orders/track",
}

order_body = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Пушкина, 10",
    "metroStation": 4,
    "phone": "+79998889988",
    "rentTime": 5,
    "deliveryDate": "2026-01-07",
    "comment": "Ыфыфыфыф",
    "color": ["BLACK"]
}

# имена параметров трэк-номера: в адресной строке для get-запроса по заказу и в json-теле ответа на post-запрос создания заказа
track_api_name = "t"
track_resp_name = "track"