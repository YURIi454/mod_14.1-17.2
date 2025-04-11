from src.class_product import Product


def test_class_product(product_fixture) -> None:
    """Тест класса Product"""

    assert product_fixture.name == "phone"
    assert product_fixture.description == "black, 1024GB"
    assert product_fixture.price == 5600.0
    assert product_fixture.quantity == 23


def test_new_product():
    assert (
        Product.new_product({"name": "Zeekr 001 FR", "description": "256GB", "price": 6_250_000, "quantity": 1}).name
        == "Zeekr 001 FR"
    )


def test_str_product(product_fixture):
    assert product_fixture.__str__() == "phone , 5600 руб. Остаток: 23 шт"


def test_add_product():
    p1 = Product("phones", "black, 1024GB", 5900.0, 13)
    p2 = Product("phones", "black, 1024GB", 5100.0, 23)
    assert Product.__add__(p1, p2) == 194000.0
