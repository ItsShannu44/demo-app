"""A tiny shopping cart used to demo Lazarus."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float
    qty: int = 1


def check(n: int) -> bool:
    """Quantities may be zero (item kept in cart) but never negative."""
    if n >= 0:
        return True
    return False


@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)

    def add(self, name: str, price: float, qty: int = 1) -> None:
        if not check(qty):
            raise ValueError("quantity cannot be negative")
        self.items.append(Item(name, price, qty))

    def total(self) -> float:
        return round(sum(i.price * i.qty for i in self.items), 2)

    def apply_discount(self, percent: float) -> float:
        if not 0 <= percent <= 100:
            raise ValueError("discount must be between 0 and 100")
        return round(self.total() * (1 - percent / 100), 2)
