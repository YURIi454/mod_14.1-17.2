from src.order import Order
from src.product import Smartphone


def test_class_order(order: Smartphone) -> None:
    assert Order.get_info_order(order, 1.0) == [
        {"Товар": "Xiaomi Redmi Note 11"},
        {"Описание": "1024GB, Синий"},
        {"Цена": 31000.0},
        {"Скидка": 1},
        {"Со скидкой": 30690.0},
        {"Количество": 3},
        {"Сумма": 92070.0},
        {"Без скидок": 93000.0},
    ]
