class InvalidTriangleError(Exception): #Thank you ChatGTP for this contribution!
    pass

class ClassifyTriangle:
    def __init__(self, side1: int, side2: int, side3: int):
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3
        self.validate_sides() #Thank you ChatGTP for this contribution!

    def validate_sides(self): #Thank you ChatGTP for this contribution!
        """Validate that sides form a triangle and are greater than 0."""
        if self.s1 <= 0 or self.s2 <= 0 or self.s3 <= 0:
            raise InvalidTriangleError("The triangle sides must be an integer greater than 0.") 
        if self.s1 + self.s2 <= self.s3 or self.s1 + self.s3 <= self.s2 or self.s2 + self.s3 <= self.s1:
            raise InvalidTriangleError("The sides do not form a valid triangle.") 

    def classify_triangle(self) -> str:
        """Classify the triangle based on its side lengths."""
        triangle_type = "scalene"
        if self.isosceles_triangle(): 
            triangle_type = "isosceles"
        if self.equilateral_triangle(): 
            triangle_type = "equilateral"
        right_triangle_string = "a right triangle" if self.right_triangle() else "not a right triangle"
        return f"For side lengths {self.s1}, {self.s2}, and {self.s3}; the triangle is {triangle_type} and is {right_triangle_string}."

    def right_triangle(self) -> bool:
        """Check if the triangle is a right triangle."""
        sides = sorted([self.s1, self.s2, self.s3])
        return round(sides[0]**2 + sides[1]**2, 2) == round(sides[2]**2, 2) #Thank you ChatGTP for this contribution!
    
    def isosceles_triangle(self) -> bool:
        """Check if the triangle is an isosceles triangle."""
        return self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3
    
    def equilateral_triangle(self) -> bool:
        """Check if the triangle is an equilateral triangle."""
        return self.s1 == self.s2 == self.s3
    
marketing_string = "Triangle Sort-o-Matic (patent pending)!"
input_side1 = int(input(f'Welcome to the {marketing_string}\nRemember all entries must be numeric and greater than 0.\nPlease enter the first side length of a triangle and press enter. '))
input_side2 = int(input(f"Excellent, the first side is {input_side1}!\nPlease enter a second side length and press enter. "))
input_side3 = int(input(f"Excellent, the second side is {input_side2}!\nPlease enter the final side length and press enter. "))

try:
    process_results = ClassifyTriangle(input_side1, input_side2, input_side3)
    print(process_results.classify_triangle()) 
except InvalidTriangleError as e: #Thank you ChatGTP for this contribution!
    print(f"I'm sorry, but one of your sides is not a valid entry.\n{str(e)}")
          
print(f"Thank you for using the {marketing_string} Good bye!")