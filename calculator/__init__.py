from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a,b,add) # Pass the add function from calculator
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a,b,subtract) #Pass the subtract function
        return Calculation.get_result()
    def multiply (a,b):
        calculation = Calculation(a,b,multiply) #pass the multiply function
        return Calculation.get_result()
    def divide(a,b):
        calculation = Calculation(a,b,divide)
        return calculation.get_result()
