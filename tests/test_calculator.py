'''Testing the Calculation function'''
from calculator import Calculator

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,7) == 9

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(3,2) == 1

def test_divide():
    '''Test that division function works '''    
    assert Calculator.divide(10,2) == 5

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculator.multiply(2,6) == 12
