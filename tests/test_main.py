import pytest
from main import calculate_and_print

#creates the test functions to parameterize and cover different operations

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string",[
    ("9", "1", 'add', "The result of 9 add 1 is equal to 10"),
    ("10", "3", 'subtract', "The result of 10 subtract 3 is equal to 7"),
    ("7", "7", 'multiply', "The result of 7 multiply 7 is equal to 49"),
    ("20", "5", 'divide', "The result of 20 divide 5 is equal to 4"),
    ("7", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("9", "1", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("z", "8", 'add', "Invalid number input: z or 8 is not a valid number."),  # Testing invalid number input
    ("9", "b", 'subtract', "Invalid number input: 9 or b is not a valid number.")  # Testing another invalid number input)
])

def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string