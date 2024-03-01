import pytest
from functions import calculateBMI, calculateWeightClass

#Testing Height

def test_150lbs_underweight():
    assert calculateWeightClass(calculateBMI(80, 150)) == "Underweight"

def test_150lbs_normal():
    assert calculateWeightClass(calculateBMI(71, 150)) == "Normal Weight"

def test_150lbs_overweight():
    assert calculateWeightClass(calculateBMI(63, 150)) == "Overweight"

def test_150lbs_obese():
    assert calculateWeightClass(calculateBMI(50, 150)) == "Obese"

def test_150lbs_boundary_underweight_normal():
    assert calculateWeightClass(calculateBMI(77, 150)) == "Underweight"
    assert calculateWeightClass(calculateBMI(76, 150)) == "Normal Weight"
    assert calculateWeightClass(calculateBMI(75, 150)) == "Normal Weight"

def test_150lbs_boundary_normal_overweight():
    assert calculateWeightClass(calculateBMI(66, 150)) == "Normal Weight"
    assert calculateWeightClass(calculateBMI(65, 150)) == "Overweight"
    assert calculateWeightClass(calculateBMI(64, 150)) == "Overweight"

def test_150lbs_boundary_overweight_obese():
    assert calculateWeightClass(calculateBMI(61, 150)) == "Overweight"
    assert calculateWeightClass(calculateBMI(60, 150)) == "Obese"
    assert calculateWeightClass(calculateBMI(59, 150)) == "Obese"


# Testing Weights

def test_67inches_underweight():
    assert calculateWeightClass(calculateBMI(67, 110)) == "Underweight"

def test_67inches_normal():
    assert calculateWeightClass(calculateBMI(67, 120)) == "Normal Weight"

def test_67inches_overweight():
    assert calculateWeightClass(calculateBMI(67, 170)) == "Overweight"    

def test_67inches_obese():
    assert calculateWeightClass(calculateBMI(67, 200)) == "Obese"

def test_67inches_underweigh_normal():
    assert calculateWeightClass(calculateBMI(67, 115)) == "Underweight"
    assert calculateWeightClass(calculateBMI(67, 116)) == "Normal Weight"
    assert calculateWeightClass(calculateBMI(67, 117)) == "Normal Weight"

def test_67inches_normal_overweight(): 
    assert calculateWeightClass(calculateBMI(67, 155)) == "Normal Weight"
    assert calculateWeightClass(calculateBMI(67, 156)) == "Overweight"
    assert calculateWeightClass(calculateBMI(67, 157)) == "Overweight"

def test_67inches_overweight_obese():
    assert calculateWeightClass(calculateBMI(67, 187)) == "Overweight"
    assert calculateWeightClass(calculateBMI(67, 188)) == "Obese"
    assert calculateWeightClass(calculateBMI(67, 189)) == "Obese"    
