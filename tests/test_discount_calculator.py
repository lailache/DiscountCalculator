import pytest

from src.discount_calculator import DiscountCalculator


# Тест на базовую стоимость без флагов
def test_calculate_base_price(calculator):
    assert calculator.calculate_total() == 500


# Тест на скидку для студента
def test_student_discount(calculator):
    total = calculator.calculate_total(is_student=True)
    assert total == 500 * 0.9


# Тест на скидку для праздников
def test_holiday_discount(calculator):
    total = calculator.calculate_total(is_holiday=True)
    assert total == 500 * 0.95


# Тест на скидку для оптового заказа
def test_bulk_order_discount(bulk_calculator):
    total = bulk_calculator.calculate_total(is_bulk_order=True)
    assert total == 100 * 20 * 0.8


# Тест на комбинацию скидок
def test_combined_discounts(calculator):
    total = calculator.calculate_total(is_student=True, is_first_purchase=True)
    assert total == 500 * 0.9 * 0.85


# Тест на обработку отрицательной цены
def test_negative_base_price():
    with pytest.raises(ValueError):
        DiscountCalculator(base_price=-10, quantity=5).calculate_total()


# Параметризованные тесты для различных флагов
@pytest.mark.parametrize("flags, expected", [
    ({"is_member": True}, 500 * 0.93),
    ({"is_express_delivery": True}, 500 * 1.1),
    ({"is_gift_wrapping": True}, 500 * 1.05),
    ({"is_peak_season": True}, 500 * 1.12),
    ({"has_coupon": True}, 500 - 50),
])
def test_various_flags(calculator, flags, expected):
    total = calculator.calculate_total(**flags)
    assert total == pytest.approx(expected, rel=1e-2)


# Тест на использование всех скидок и наценок одновременно
def test_all_flags(calculator):
    total = calculator.calculate_total(
        is_student=True,
        is_holiday=True,
        is_first_purchase=True,
        is_member=True,
        is_eco_friendly=True,
        is_referral=True,
        is_express_delivery=True,
        is_gift_wrapping=True,
        is_peak_season=True,
        has_coupon=True
    )
    # Ожидаем итоговую сумму, рассчитанную с учетом всех флагов
    expected = (
            100 * 5 * 0.9 * 0.95 * 0.85 * 0.93 * 0.97 * 0.92 * 1.1 * 1.05 * 1.12 - 50
    )
    assert total == pytest.approx(expected, rel=1e-2)
