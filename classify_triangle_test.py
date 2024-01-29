import pytest
from classify_triangle import ClassifyTriangle, InvalidTriangleError

@pytest.mark.parametrize("side1, side2, side3", [(17,15,8), (3,4,5), (5,12,13)])
def test_right_triangle(side1, side2, side3):
    tst_classify_triangle = ClassifyTriangle(side1, side2, side3)
    is_right_triangle = tst_classify_triangle.right_triangle()
    assert is_right_triangle == True

def test_not_right_triangle():
    tst_classify_triangle = ClassifyTriangle(4, 5, 6)
    is_not_right_triangle = tst_classify_triangle.right_triangle()
    assert is_not_right_triangle == False

@pytest.mark.parametrize("side1, side2, side3", [(2,2,3), (2,3,2), (3,2,2)])
def test_isosceles_triangle(side1, side2, side3):
    tst_classify_triangle = ClassifyTriangle(side1, side2, side3)
    is_isosceles_triangle = tst_classify_triangle.isosceles_triangle()
    assert is_isosceles_triangle == True

'''
def test_equilateral_triangle():

def test_non_triangle_integers():
'''