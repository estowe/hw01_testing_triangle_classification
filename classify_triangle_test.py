#!/bin/python3
"""
This is a class project for 2024S SSW 567-WS, Software Testing, Quality Assurance and Maintenance
Group members:
Estevan Stowe
Jacob Gelman-Funk
Tawnya Shannon
"""

import pytest
from classify_triangle import ClassifyTriangle, InvalidTriangleError

def test_non_triangle_integers():
    with pytest.raises(InvalidTriangleError):
        tst_classify_triangle = ClassifyTriangle(4,5,10)

def test_zero_integers():
    with pytest.raises(InvalidTriangleError):
        tst_classify_triangle = ClassifyTriangle(0,0,0)

def test_negative_integers():
    with pytest.raises(InvalidTriangleError):
        tst_classify_triangle = ClassifyTriangle(-3,-4,-5)

@pytest.mark.parametrize("sides1, sides2, sides3", [(17,15,8), (3,4,5), (5,12,13)])
def test_right_triangle(sides1, sides2, sides3):
    tst_classify_triangle = ClassifyTriangle(sides1, sides2, sides3)
    is_right_triangle = tst_classify_triangle.right_triangle()
    assert is_right_triangle == True

def test_not_right_triangle():
    tst_classify_triangle = ClassifyTriangle(5,4,5)
    is_not_right_triangle = tst_classify_triangle.right_triangle()
    assert is_not_right_triangle == False

@pytest.mark.parametrize("sides1, sides2, sides3", [(2,2,3), (2,3,2), (3,2,2)])
def test_isosceles_triangle(sides1, sides2, sides3):
    tst_classify_triangle = ClassifyTriangle(sides1, sides2, sides3)
    is_isosceles_triangle = tst_classify_triangle.isosceles_triangle()
    assert is_isosceles_triangle == True

def test_not_isosceles_triangle():
    tst_classify_triangle = ClassifyTriangle(4,5,6)
    is_not_isosceles_triangle = tst_classify_triangle.isosceles_triangle()
    assert is_not_isosceles_triangle == False

@pytest.mark.parametrize("sides1, sides2, sides3", [(2,2,2), (4,4,4), (17,17,17)])
def test_equilateral_triangle(sides1, sides2, sides3):
    tst_classify_triangle = ClassifyTriangle(sides1, sides2, sides3)
    is_equilateral_triangle = tst_classify_triangle.equilateral_triangle()
    assert is_equilateral_triangle == True

def test_equilateral_triangle():
    tst_classify_triangle = ClassifyTriangle(2,2,3)
    is_not_equilateral_triangle = tst_classify_triangle.equilateral_triangle()
    assert is_not_equilateral_triangle == False