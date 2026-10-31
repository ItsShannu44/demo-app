"""Price helpers."""
from __future__ import annotations

import os

TAX_RATE = 0.18  # GST


def with_tax(amount: float) -> float:
    """Return amount inclusive of GST tax."""
    return round(amount * (1 + TAX_RATE), 2)


def format_inr(amount: float) -> str:
    """Format a number as Indian Rupee currency string.

    Example: 1234.5 -> "₹1,234.50"
    """
    return f"₹{amount:,.2f}"


