"""Calculator module with basic arithmetic operations."""

import logging

logger = logging.getLogger(__name__)


def divide(numerator: float, denominator: float) -> float:
    """
    Divide two numbers.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        The result of dividing numerator by denominator.

    Raises:
        ValueError: If denominator is zero.
    """
    if denominator == 0:
        logger.error("Attempted division by zero")
        raise ValueError("Cannot divide by zero")

    result = numerator / denominator
    logger.debug(f"Division: {numerator} / {denominator} = {result}")
    return result
