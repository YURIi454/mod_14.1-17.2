def test_custom_error(custom_error) -> None:
    """Тест вывода сообщения."""

    assert str(custom_error) == "Тест пройден успешно!"
