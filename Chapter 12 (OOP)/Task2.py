"""
    1)Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

"""

#1
print("(1)Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.")


class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area_of_circle = 3.142 * (self.radius ** 2)
        return area_of_circle
    
    def perimeter(self):
        perimeter_circle = 2 * 3.142 * self.radius
        return perimeter_circle
    
    def __str__(self):
        representation = "The is circle with radius {}".format(self.radius)
        return representation
    
circle1 = Circle(4)
print(circle1)
print(circle1.area())
print(circle1.perimeter())

print("----------------------------------------------------------")
