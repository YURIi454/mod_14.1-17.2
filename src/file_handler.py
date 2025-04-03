import json
from typing import Any

from config import PATH_JSON
from src.class_category import Category
from src.class_product import Product


def read_json(path: str) -> Any:
    """Чтение  json"""
    with open(path, mode="r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def create_obj_from_json(data_file) -> Any:
    """Добавление новых объектов классов."""

    data_file = read_json(path=PATH_JSON)

    categories = []
    products = []

    for cat in data_file:
        for pro in cat["products"]:
            products.append(Product(**pro))
        cat["products"] = categories
        categories.append(Category(**cat))

    return categories, products
