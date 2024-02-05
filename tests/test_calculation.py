"""
This module contains tests for the calculator operations and Calculation class.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

# It's good practice to add a docstring at the beginning of the module explaining its purpose.

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
])
def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    Parameters:
        a (Decimal): The first operand.
        b (Decimal): The second operand.
        operation (function): The operation to perform.
        expected (Decimal): The expected result.
    """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """
    Test the string representation of the Calculation class.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
