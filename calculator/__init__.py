"""Provides an arithmetic addition function"""
class Calculation:
    def __init__(self,a,b,operation):
        self.a = a
        self.b = b
        self.operation = operation # Store the operation function here

        def get_result(self):
            # Call the stored operation with a and b
class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a,b,add) # Pass the add function from calculator
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a,b,subtract) #Pass the subtract function
    """subtracts two numbers"""
    return a - b
def divide(a,b):
    """divides two numbers"""
    return a / b
