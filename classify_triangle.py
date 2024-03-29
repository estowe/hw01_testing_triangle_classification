#!/bin/python3
"""
This is a class project for 2024S SSW 567-WS, Software Testing, Quality Assurance and Maintenance
Group members:
Estevan Stowe
Jacob Gelman-Funk
Tawnya Shannon
"""

class InvalidTriangleError(Exception):
    """Exception handler"""

class ClassifyTriangle:
    """Main Triangle Classification Routine"""
    def __init__(self, side1, side2, side3):
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3
        self.validate_sides()

    def validate_sides(self):
        """Validate that sides form a triangle and are greater than 0."""
        if not all(isinstance(side, int) for side in [self.s1, self.s2, self.s3]):
            raise ValueError("The triangle sides must be integers.")
        if self.s1 <= 0 or self.s2 <= 0 or self.s3 <= 0:
            raise InvalidTriangleError("The triangle sides must be an integer greater than 0.")
        if (self.s1 + self.s2 <= self.s3 or
            self.s1 + self.s3 <= self.s2 or
            self.s2 + self.s3 <= self.s1):
            raise InvalidTriangleError("The sides do not form a valid triangle.")

    def classify_triangle(self) -> str:
        """Classify the triangle based on its side lengths."""
        triangle_type = "scalene"
        if self.isosceles_triangle():
            triangle_type = "isosceles"
        if self.equilateral_triangle():
            triangle_type = "equilateral"
        right_triangle_string = ("a right triangle"
                                 if self.right_triangle()
                                 else "not a right triangle")
        return (
            f"For side lengths {self.s1}, {self.s2}, and {self.s3}; "
            f"The triangle is {triangle_type} and is {right_triangle_string}.")

    def right_triangle(self) -> bool:
        """Check if the triangle is a right triangle."""
        sides = sorted([self.s1, self.s2, self.s3])
        return round(sides[0]**2 + sides[1]**2, 2) == round(sides[2]**2, 2)

    def isosceles_triangle(self) -> bool:
        """Check if the triangle is an isosceles triangle."""
        return self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3

    def equilateral_triangle(self) -> bool:
        """Check if the triangle is an equilateral triangle."""
        return self.s1 == self.s2 == self.s3
