import pytest
from functions import calculateBMI, calculateWeightClass

def returnSum(num):
    return (num + 1)

def test_Sum():
    assert returnSum(4) == 5