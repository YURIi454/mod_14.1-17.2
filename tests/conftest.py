from typing import Any

import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def category_fixture() -> Any:
    """Фикстура для класса категории."""

    prod_1 = Product("iphone", "16 S max", 13_658, 7)
    prod_2 = Product("samsung", "A 564", 12_467, 9)

    return Category("phones", "new", [prod_1, prod_2])


@pytest.fixture
def product_fixture() -> Any:
    """Фикстура для класса продукт."""
    return Product("phone", "black, 1024GB", 5600.0, 23)


@pytest.fixture
def json_file_fixture() -> list:
    """Фикстура для проверки json."""
    return [
        {
            "name": "Car",
            "description": "Made in China",
            "products": [
                {"name": "Zeekr 001 FR", "price": 6_250_000, "quantity": 1},
                {"name": "Voyah Free", "price": 4_360_000, "quantity": 3},
                {"name": "Geely Monjaro", "price": 3_230_000, "quantity": 14},
                {"name": "Staria", "price": 5_250_000, "quantity": 10},
                {"name": "Lixiang L9", "price": 5_360_000, "quantity": 3},
                {"name": "TANK 700", "price": 7_230_000, "quantity": 4},
            ],
        },
        {
            "name": "Family car",
            "description": "Made in Germany",
            "products": [
                {"name": "BMW X7", "price": 16_450_777, "quantity": 2},
                {"name": "MB GLS MAY", "price": 46_777_777, "quantity": 1},
                {"name": "MB VIANO", "price": 6_450_777, "quantity": 6},
                {"name": "Maybach 62", "price": 86_777_777, "quantity": 1},
                {"name": "Audi TT", "price": 7_450_777, "quantity": 2},
                {"name": "MB GLS ", "price": 26_757_757, "quantity": 3},
            ],
        },
    ]
