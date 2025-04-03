def test_class_product(product_fixture) -> None:
    assert product_fixture.name == "phone"
    assert product_fixture.description == "black, 1024GB"
    assert product_fixture.price == 5600.0
    assert product_fixture.quantity == 23
