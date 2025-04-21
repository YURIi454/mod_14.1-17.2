import json
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """Чтение  json файла по указанному пути."""

    with open(path, mode="r", encoding="UTF-8") as file:
        data = json.load(file)

        return data


def create_obj_from_json(path: str) -> Any:
    """Добавление новых объектов классов из файла."""

    with open(path, mode="r", encoding="UTF-8") as file:
        data = json.load(file)

    categories = []
    products = []

    for cat in data:
        for pro in cat["products"]:
            products.append(Product(**pro))
        cat["products"] = products
        categories.append(Category(**cat))

    return categories, products
