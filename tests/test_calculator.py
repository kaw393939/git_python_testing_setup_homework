"""This is a test file for my calculator program""" 
from app import add

def test_addition():
    """The is a test of the addition function"""
    assert add(2,2) == 4
