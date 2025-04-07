import pytest

from src.discount_calculator import DiscountCalculator


@pytest.fixture
def calculator():
    """Фикстура для создания объекта DiscountCalculator с базовыми параметрами"""
    return DiscountCalculator(base_price=100, quantity=5)


@pytest.fixture
def bulk_calculator():
    """Фикстура для создания объекта DiscountCalculator с большим количеством товаров"""
    return DiscountCalculator(base_price=100, quantity=20)
