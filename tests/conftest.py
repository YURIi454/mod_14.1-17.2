from typing import Any

import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def category_fixture() -> Any:
    """Фикстура для класса категории."""
    return Category("car", "m_b", [])


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
            "description": "Any",
            "products": [
                {"name": "Zeekr 001 FR", "price": 6_250_000, "quantity": 1},
                {"name": "Voyah Free", "price": 4_360_000, "quantity": 3},
                {"name": "Geely Monjaro", "price": 3_230_000, "quantity": 14},
            ],
        },
        {
            "name": "Family car",
            "description": "Made in Germany",
            "products": [
                {"name": "BMW X7", "price": 16_450_777, "quantity": 2},
                {"name": "MB GLS MAY", "price": 46_777_777, "quantity": 1},
            ],
        },
    ]
