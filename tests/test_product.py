import pytest

from src.exception_handler import CustomError
from src.product import LawnGrass, Product, Smartphone


def test_class_product(product_fixture: Product) -> None:
    """Тест класса Product"""

    assert product_fixture.name == "phone"
    assert product_fixture.description == "black, 1024GB"
    assert product_fixture.price == 5600.0
    assert product_fixture.quantity == 23


def test_new_product() -> None:
    """Тест добавления продукта класса "Product" """

    assert (
        Product.new_product({"name": "Zeekr 001 FR", "description": "256GB", "price": 6_250_000, "quantity": 1}).name
        == "Zeekr 001 FR"
    )


def test_str_product(product_fixture: Product) -> None:
    """Тест магического метода класса "Product" """

    assert product_fixture.__str__() == "phone , 5600 руб. Остаток: 23 шт"


def test_add_product() -> None:
    """Тест магического метода класса "Product" """

    p1 = Product("phones", "black, 1024GB", 5900.0, 13)
    p2 = Product("phones", "black, 1024GB", 5100.0, 23)
    assert Product.__add__(p1, p2) == 194000.0


def test_class_phone(smartphone: Smartphone, grass: LawnGrass) -> None:
    """Тест магического метода класса "Product" """

    assert smartphone.color == "Серый"
    assert Smartphone.__add__(smartphone, smartphone) == 1800000.0
    with pytest.raises(CustomError):
        assert Smartphone.__add__(smartphone, grass) == CustomError()


def test_class_grass(smartphone: Smartphone, grass: LawnGrass) -> None:
    """Тест магического метода класса "Product" """

    assert grass.price == 450.0
    assert LawnGrass.__add__(grass, grass) == 13500.0
    with pytest.raises(CustomError):
        assert LawnGrass.__add__(grass, smartphone) == CustomError()
