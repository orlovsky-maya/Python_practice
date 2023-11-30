import pytest


def is_divisible(num1, num2):
    if num1 % num2 == 0:
        return True
    return False


# write unit-test

def test_is_divisible():
    assert is_divisible(10, 2)


def test_is_not_divisible():
    assert not is_divisible(7, 3)


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        is_divisible(5, 0)
