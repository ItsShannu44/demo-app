"""Price helpers."""
from __future__ import annotations

import os

import os

TAX_RATE = 0.18  # GST


def with_tax(amount: float) -> float:
    return round(amount * (1 + TAX_RATE), 2)


def format_inr(amount: float) -> str:
    return f"₹{amount:,.2f}"
