from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('11'), Decimal('5'), add, Decimal('16')),  # Tests addition
    (Decimal('17'), Decimal('10'), subtract, Decimal('7')),  # Tests subtraction
    (Decimal('6'), Decimal('6'), multiply, Decimal('36')),  # Tests multiplication
    (Decimal('65'), Decimal('5'), divide, Decimal('13')),  # Tests division 
    (Decimal('11.5'), Decimal('.5'), add, Decimal('12')),  # Tests addition with decimals numbers
    (Decimal('10.5'), Decimal('1.5'), subtract, Decimal('9')),  # Tests subtraction with decimal numbers
    (Decimal('25.5'), Decimal('2'), multiply, Decimal('51.0')),  # Tests multiplication with decimals numbers
    (Decimal('30'), Decimal('0.5'), divide, Decimal('60')),  # Tests division with decimals numbers
])
def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    calc = Calculation(a, b, operation)  # Create a Calculation instance with the provided operands and operation.
def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    
    This test verifies that the __repr__ method of a Calculation instance returns a string
    that accurately represents the state of the Calculation object, including its operands and operation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing.
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)  # Create a Calculation instance with a zero divisor.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
        calc.perform()  # Attempt to perform the calculation, which should trigger the ValueError.