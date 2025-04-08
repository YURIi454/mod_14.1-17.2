from src.class_category import Category
from src.class_product import Product


def test_class_category(category_fixture) -> None:
    """Тест класса Category"""

    assert category_fixture.name == "phones"
    assert category_fixture.description == "new"
    assert category_fixture.products == "iphone, 13658 руб. Остаток: 7 шт.\nsamsung, 12467 руб. Остаток: 9 шт.\n"


def test_counters(count_category_fixture) -> None:
    """Тест счётчиков класса Category"""

    old_categories_counter = Category.category_count
    old_products_counter = Category.product_count

    products = []
    for row in count_category_fixture:
        products.append(Product(**row))

    Category("phones", "new", products)
    Category("phones", "new", products)

    assert Category.product_count == old_categories_counter
    assert Category.product_count == old_products_counter


def test_price():
    prod = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    prod.price = 125
    assert prod.price == 125


def test_add_product():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert Category.add_product(category1, product3) == None
