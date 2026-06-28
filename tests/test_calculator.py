"""Tests for calculator module."""

import pytest
from calculator import divide


def test_divide_positive_numbers():
    """Test division of two positive numbers."""
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0
    assert divide(7, 2) == 3.5


def test_divide_negative_numbers():
    """Test division with negative numbers."""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_with_zero_numerator():
    """Test division when numerator is zero."""
    assert divide(0, 5) == 0.0


def test_divide_by_zero_raises_error():
    """Test that division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_divide_floats():
    """Test division of floating point numbers."""
    result = divide(5.5, 2.0)
    assert result == pytest.approx(2.75)
