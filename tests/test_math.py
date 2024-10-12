import pytest
from app.plugins.math import MathCommand
from unittest.mock import patch

# Use parametrize for cleaner test cases
@pytest.mark.parametrize("num1, num2, operator, expected_output", [
    (3, 5, '+', "Result: 8.0"),
    (10, 5, '-', "Result: 5.0"),
    (4, 5, '*', "Result: 20.0"),
    (10, 2, '/', "Result: 5.0"),
    (10, 0, '/', "Error: Division by zero is not allowed."),
    (10, 5, '%', "Invalid operator. Please use a valid one like '+', '-', '*', '/', 'add', 'subtract', 'multiply', or 'divide'."),
    ('a', 5, '+', "Invalid input. Please ensure you enter numeric values for the numbers."),
])
def test_math_command(capfd, num1, num2, operator, expected_output):
    with patch('builtins.input', side_effect=[num1, num2, operator]):
        command = MathCommand()
        command.execute()
        out, err = capfd.readouterr()
        assert out.strip() == expected_output