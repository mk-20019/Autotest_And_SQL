-- Решил выполнить 1-ое задание двумя вариантами запросов вследствие неточной формулировки поставленной задачи
-- Задание 1: запрос на вывод инфы без агрегирования (списком)

SELECT c.login AS "Логин курьера",
       o.id AS "ID заказа"
FROM Couriers c
JOIN Orders o ON c.id = o.courierId
WHERE o.inDelivery = true;

-- Задание 1: запрос на вывод агрегированной инфы (сводка кол-ва заказов по каждому курьеру) 

SELECT c.login AS "Логин курьера",
COUNT(o.id) AS "Количество заказов в доставке"
FROM Couriers c
JOIN Orders o ON c.id = o.courierId
WHERE o.inDelivery = true
GROUP BY c.login;

-- Задание 2:

SELECT track AS "Трекер заказа",
    CASE 
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN inDelivery = true THEN 1
        ELSE 0
    END AS "Статус"
FROM Orders;