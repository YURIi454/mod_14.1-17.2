from abc import ABC, abstractmethod
from typing import Any

from src.class_product import Product


class OrderCat(ABC):
    """Абстрактный класс."""

    @abstractmethod
    def info_class(self):
        pass


class Order(OrderCat):
    """Класс для получения ссылки на заказ."""

    def info_class(self):
        return f"{self.__class__.__name__}"

    @staticmethod
    def get_info_order(product, discount) -> Any:

        if not isinstance(product, Product):
            return TypeError

        total_price = product.price

        if discount >= 0:
            total_price = product.price - (product.price * discount) / 100

        data_order = [
            {"Товар": product.name},
            {"Описание": product.description},
            {"Цена": product.price},
            {"Скидка": int(discount)},
            {"Со скидкой": total_price},
            {"Количество": product.quantity},
            {"Сумма": total_price * product.quantity},
            {"Без скидок": product.price * product.quantity},
        ]

        return data_order
