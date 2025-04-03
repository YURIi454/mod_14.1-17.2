from config import PATH_JSON
from src.file_handler import create_obj_from_json, read_json


def test_read_json() -> None:
    """Тест чтения файла."""

    assert read_json(PATH_JSON) == [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


def test_create_obj_from_json() -> None:
    """Тест создание объектов класса."""
    assert create_obj_from_json(read_json(PATH_JSON))[0][0].name == "Смартфоны"
    assert create_obj_from_json(read_json(PATH_JSON))[1][0].description == "256GB, Серый цвет, 200MP камера"
    assert create_obj_from_json(read_json(PATH_JSON))[1][0].quantity == 5
    assert create_obj_from_json(read_json(PATH_JSON))[1][0].price == 180000.0
