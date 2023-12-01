"""Интернет-магазин осуществляет экспресс доставку для своих
товаров по цене 1000 рублей за первый товар и 120 рублей
за каждый последующий товар. Напишите функцию get_shipping_cost(quantity),
которая принимает в качестве аргумента натуральное число quantity – количество
товаров в заказе – и возвращает стоимость доставки."""
import pytest


def get_shipping_cost(quantity):
    cost = 1000 + ((quantity - 1) * 120)
    return cost

@pytest.mark.smoke
def test_one_good():
    assert get_shipping_cost(1) == 1000


@pytest.mark.smoke
def test_two_goods():
    assert get_shipping_cost(2) == 1120


@pytest.mark.smoke
def test_three_goods():
    assert get_shipping_cost(3) == 1240


@pytest.mark.smoke
def test_ten_goods():
    assert get_shipping_cost(10) == 2080


@pytest.mark.regression
def test_forty_one_goods():
    assert get_shipping_cost(41) == 5800


@pytest.mark.regression
def test_thousand_goods():
    assert get_shipping_cost(1000) == 120880


