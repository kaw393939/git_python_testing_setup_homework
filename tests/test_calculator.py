'''Testing the calculator class'''
from calculator import calculator

def test_calculator():
    '''Testing the calculator add function'''
    assert calculator.add(2,2) == 4

def test_calculator_subtract():
    '''Testing the calculator subtract function'''
    assert calculator.subtract(5, 3) == 2

def test_calculator_multiply():
    '''Testing the calculator multiply function'''
    assert calculator.multiply(3, 4) == 12

def test_calculator_divide():
    '''Testing the calculator divide function'''
    assert calculator.divide(8, 2) == 4
