import pytest
from calculator import Calculator

calculator = Calculator()


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 5, 15),
    (-4, 4, 0),
    (-3, -7, -10),
    (2.5, 1.5, 4.0)
])
def test_add(a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (15, 3, 5),
    (7, 2, 3.5),
    (-10, 2, -5),
    (0, 5, 0)
])
def test_divide(a, b, expected):
    assert calculator.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, True),
    (7, True),
    (11, True),
    (4, False),
    (9, False),
    (1, False),
    (0, False),
    (-5, False)
])
def test_is_prime_number(number, expected):
    assert calculator.is_prime_number(number) == expected