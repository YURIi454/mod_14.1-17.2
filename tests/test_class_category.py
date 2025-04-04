from src.class_category import Category
from src.class_product import Product


def test_class_category(category_fixture) -> None:
    """Тест класса Category"""

    assert category_fixture.name == "phones"
    assert category_fixture.description == "new"
    assert category_fixture.products[0].name == "iphone"
    assert category_fixture.products[1].name == "samsung"


def test_counters(count_category_fixture) -> None:
    """Тест счётчиков класса Category"""

    old_categories_counter = Category.category_count
    old_products_counter = Category.product_count

    products = []
    for row in count_category_fixture:
        products.append(Product(**row))

    Category("phones", "new", products)
    Category("phones", "new", products)

    assert Category.category_count == old_categories_counter + 2
    assert Category.product_count == old_products_counter + 24
