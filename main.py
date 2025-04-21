from src.category import Category
from src.exception_handler import CustomError
from src.order import Order
from src.product import LawnGrass, Product, Smartphone

if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except CustomError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с "
            "нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3, grass1, grass2])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())

    print('\n * * Работа класса "Заказ" * * \n')

    ord_prod = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 3, 90.3, "Note 11", 1024, "Синий")
    ord_prod_1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    ord_prod_2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    ord_prod_3 = Category("Шина", "295/65R24", [])

    print(Order.get_info_order(ord_prod, 14.0))
    print(Order.get_info_order(ord_prod_1, 7.5))
    print(Order.get_info_order(ord_prod_2, 12.0))
    print(Order.get_info_order(ord_prod_3, 22.0))
