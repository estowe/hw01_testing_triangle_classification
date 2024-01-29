import pytest
from classify_triangle import ClassifyTriangle, InvalidTriangleError

def test_right_triangle():
    tst_classify_triangle = ClassifyTriangle(17, 15, 8)
    is_right_triangle = tst_classify_triangle.right_triangle()
    #additional parms 3, 4, 5; 5, 12, 13; 17,15,8
    assert is_right_triangle == True

def test_not_right_triangle():
    tst_classify_triangle = ClassifyTriangle(17, 15, 9)
    is_not_right_triangle = tst_classify_triangle.right_triangle()
    assert is_not_right_triangle == False

'''
def test_scalene_triangle():

def test_isosceles_triangle():

def test_equilateral_triangle():

def test_non_triangle_integers():
'''