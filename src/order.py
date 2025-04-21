from abc import ABC, abstractmethod
from typing import Any

from src.exception_handler import CustomError
from src.product import Product


class OrderCat(ABC):
    """Абстрактный класс."""

    @abstractmethod
    def info_class(self) -> None:
        pass


class Order(OrderCat):
    """Класс для получения ссылки на заказ."""

    def info_class(self) -> None:
        """Информация о классе."""

        pass

    @staticmethod
    def get_info_order(product: Any, discount:float) -> Any:
        """Получение данных о заказе."""

        if not isinstance(product, Product):
            return CustomError()

        total_price = product.price

        if discount >= 0:
            total_price = product.price - (product.price * discount) / 100

        data_order = [
            {"Товар": product.name},
            {"Описание": product.description},
            {"Цена": product.price},
            {"Скидка": round(discount)},
            {"Со скидкой": total_price},
            {"Количество": product.quantity},
            {"Сумма": total_price * product.quantity},
            {"Без скидок": product.price * product.quantity},
        ]

        return data_order
