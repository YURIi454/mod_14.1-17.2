def test_class_category(category_fixture):
    assert category_fixture.name == "phones"
    assert category_fixture.description == "new"
    assert category_fixture.products[0].name == "iphone"
    assert category_fixture.products[1].name == "samsung"
    assert category_fixture.category_count == 1
    assert category_fixture.product_count == 2
