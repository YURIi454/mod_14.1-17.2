from src.class_product import Product


class Category:
    """Класс категории"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация класса категории"""

        self.name: str = name
        self.description: str = description
        self.__products: list = products

    def __str__(self) -> str:
        total_quantity = 0
        for product in self.__products:
            if self.name:
                total_quantity += product.quantity
        return f"{self.name},  количество продуктов: {total_quantity} шт"

    @property
    def products(self) -> str:
        product_info = ""
        for elem in self.__products:
            product_info += f"{elem.name}, {elem.price} руб. Остаток: {elem.quantity} шт.\n"
        return product_info

    def add_product(self, product: Product) -> None:

        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1

        else:
            raise TypeError
