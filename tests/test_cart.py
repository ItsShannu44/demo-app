import pytest

from shop.cart import Cart, check
from shop.pricing import format_inr, with_tax


def test_check_allows_zero():
    assert check(0)


def test_check_rejects_negative():
    assert not check(-1)


def test_total():
    cart = Cart()
    cart.add("tea", 20.0, 2)
    cart.add("biscuit", 10.5)
    cart.add("sample", 99.0, 0)
    assert cart.total() == 50.5


def test_negative_qty_raises():
    with pytest.raises(ValueError):
        Cart().add("x", 1.0, -2)


def test_discount():
    cart = Cart()
    cart.add("book", 200.0)
    assert cart.apply_discount(10) == 180.0


def test_tax_and_format():
    assert with_tax(100) == 118.0
    assert format_inr(1234.5) == "₹1,234.50"
