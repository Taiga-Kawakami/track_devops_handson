from src.main import add


def test_add_integer_values():
    assert add(2, 3) == 5


def test_add_decimal_values():
    assert add(1.2, 3.5) == 4


def test_add_with_third_argument():
    assert add(1.2, 3.5, 2.8) == 6
