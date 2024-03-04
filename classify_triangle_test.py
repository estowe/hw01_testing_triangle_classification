#!/bin/python3
"""
This is a class project for 2024S SSW 567-WS, Software Testing, Quality Assurance and Maintenance
Group members:
Estevan Stowe
Jacob Gelman-Funk
Tawnya Shannon
"""

from typing import Literal
import pytest
from classify_triangle import ClassifyTriangle, InvalidTriangleError


class TestClassifyTriangle:
    """
    Tests the ClassifyTriangle class.
    """
    def test_non_triangle_integers(self):
        """
        Test case for non-triangle integers.
        This test checks if the ClassifyTriangle class correctly raises an InvalidTriangleError
        when the sides do not form a triangle.
        """
        with pytest.raises(InvalidTriangleError):
            ClassifyTriangle(4,5,10)

    def test_zero_integers(self):
        """
        Test case for non-triangle integers.
        This test checks if the ClassifyTriangle class correctly raises an InvalidTriangleError
        when the sides do not form a triangle.
        """
        with pytest.raises(InvalidTriangleError):
            ClassifyTriangle(0,0,0)

    def test_negative_integers(self):
        """
        Test case for negative integers.
        This test checks if the ClassifyTriangle class correctly raises an InvalidTriangleError
        when the sides are negative.
        """
        with pytest.raises(InvalidTriangleError):
            ClassifyTriangle(-3,-4,-5)

    def test_non_integer_sides(self):
        """
        Test case for non-integer sides.
        This test checks if the ClassifyTriangle class correctly 
        raises a ValueError when the sides are not integers.
        """
        with pytest.raises(ValueError):
            ClassifyTriangle("a", "b", "c")

    @pytest.mark.parametrize("sides1, sides2, sides3", [(17,15,8), (3,4,5), (5,12,13)])
    def test_right_triangle(self, sides1: Literal[17, 3, 5],
                            sides2: Literal[15, 4, 12],
                            sides3: Literal[8, 5, 13]):
        """
        Test case for right triangles.
        This test checks if the ClassifyTriangle class correctly identifies a right triangle.
        """
        tst_classify_triangle = ClassifyTriangle(sides1, sides2, sides3)
        is_right_triangle = tst_classify_triangle.right_triangle()
        assert is_right_triangle is True

    def test_not_right_triangle(self):
        """
        Test case for non-right triangles.
        This test checks if the ClassifyTriangle class correctly identifies a non-right triangle.
        """
        tst_classify_triangle = ClassifyTriangle(5,4,5)
        is_not_right_triangle = tst_classify_triangle.right_triangle()
        assert is_not_right_triangle is False

    @pytest.mark.parametrize("sides1, sides2, sides3", [(2,2,3), (2,3,2), (3,2,2)])
    def test_isosceles_triangle(self, sides1: Literal[2, 3],
                                sides2: Literal[2, 3],
                                sides3: Literal[3, 2]):
        """
        Test case for isosceles triangles.
        This test checks if the ClassifyTriangle class correctly identifies an isosceles triangle.
        """
        tst_classify_triangle = ClassifyTriangle(sides1, sides2, sides3)
        is_isosceles_triangle = tst_classify_triangle.isosceles_triangle()
        assert is_isosceles_triangle is True

    def test_not_isosceles_triangle(self):
        """
        Test case for non-isosceles triangles.
        This test checks if the ClassifyTriangle class 
        correctly identifies a non-isosceles triangle.
        """
        tst_classify_triangle = ClassifyTriangle(4,5,6)
        is_not_isosceles_triangle = tst_classify_triangle.isosceles_triangle()
        assert is_not_isosceles_triangle is False

    @pytest.mark.parametrize("sides1, sides2, sides3", [(2,2,2), (4,4,4), (17,17,17)])
    def test_equilateral_triangle(self, sides1: Literal[2, 4, 17],
                                  sides2: Literal[2, 4, 17],
                                  sides3: Literal[2, 4, 17]):
        """
        Test case for equilateral triangles.
        This test checks if the ClassifyTriangle class correctly identifies an equilateral triangle.
        """
        tst_classify_triangle = ClassifyTriangle(sides1, sides2, sides3)
        is_equilateral_triangle = tst_classify_triangle.equilateral_triangle()
        assert is_equilateral_triangle is True

    def test_not_equilateral_triangle(self):
        """
        Test case for non-equilateral triangles.
        This test checks if the ClassifyTriangle class correctly 
        identifies a non-equilateral triangle.
        """
        tst_classify_triangle = ClassifyTriangle(2,2,3)
        is_not_equilateral_triangle = tst_classify_triangle.equilateral_triangle()
        assert is_not_equilateral_triangle is False

    def test_scalene_triangle(self):
        """
        Test case for scalene triangles.
        This test checks if the ClassifyTriangle class correctly identifies a scalene triangle.
        """
        tst_classify_triangle = ClassifyTriangle(3,4,5)
        triangle_type = tst_classify_triangle.classify_triangle()
        assert "scalene" in triangle_type

    def test_large_numbers(self):
        """
        Test case for large numbers.
        This test checks if the ClassifyTriangle class correctly 
        identifies an equilateral triangle when the sides are large numbers.
        """
        tst_classify_triangle = ClassifyTriangle(1000000, 1000000, 1000000)
        triangle_type = tst_classify_triangle.classify_triangle()
        assert "equilateral" in triangle_type

    def test_non_right_triangle_with_positive_integers(self):
        """
        Test case non-right triangles.
        This test checks if the ClassifyTriangle class correctly 
        identifies non-right triangles.
        """
        tst_classify_triangle = ClassifyTriangle(2, 3, 4)
        is_not_right_triangle = tst_classify_triangle.right_triangle()
        assert is_not_right_triangle is False

    def test_non_equilateral_triangle_with_positive_integers(self):
        """
        Test case for non-equilateral triangles.
        This test checks if the ClassifyTriangle class correctly 
        identifies non-equilateral triangles.
        """
        tst_classify_triangle = ClassifyTriangle(2, 2, 3)
        is_not_equilateral_triangle = tst_classify_triangle.equilateral_triangle()
        assert is_not_equilateral_triangle is False

    def test_non_isosceles_triangle_with_positive_integers(self):
        """
        Test case for non-isosceles triangles.
        This test checks if the ClassifyTriangle class correctly 
        identifies non-isosceles triangles.
        """
        tst_classify_triangle = ClassifyTriangle(2, 3, 4)
        is_not_isosceles_triangle = tst_classify_triangle.isosceles_triangle()
        assert is_not_isosceles_triangle is False

    def test_non_scalene_triangle_with_positive_integers(self):
        """
        Test case for non-scalene triangles.
        This test checks if the ClassifyTriangle class correctly 
        identifies non-scalene triangles.
        """
        tst_classify_triangle = ClassifyTriangle(2, 2, 2)
        triangle_type = tst_classify_triangle.classify_triangle()
        assert "scalene" not in triangle_type

if __name__ == "__main__":
    pytest.main()
