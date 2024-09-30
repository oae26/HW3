from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
'''Will test the opertaions from the calculator directory.'''

def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Decimal('12'), Decimal('3'), add)
    assert calculation.perform() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation(Decimal('15'), Decimal('10'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = Calculation(Decimal('35'), Decimal('2'), multiply)
    assert calculation.perform() == Decimal('70'), "Multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = Calculation(Decimal('35'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('7'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('22'), Decimal('0'), divide)
        calculation.perform()