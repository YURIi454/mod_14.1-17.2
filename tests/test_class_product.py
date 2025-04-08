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
