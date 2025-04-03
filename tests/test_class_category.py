def test_class_category(category_fixture):
    assert category_fixture.name == "car"
    assert category_fixture.description == "m_b"
    assert category_fixture.products == []
