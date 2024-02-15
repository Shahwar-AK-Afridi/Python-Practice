"""
    1)Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
    2)Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age
    3)Write a Python program to create a calculator class. Include methods for basic arithmetic operations

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

#2
print("(2)Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age")

class Person:

    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):
        pass





print("----------------------------------------------------------")

#3
print("(3)Write a Python program to create a calculator class. Include methods for basic arithmetic operations")

class calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        addition = self.num1 + self.num2
        return addition
    
    def difference(self):
        subtract = self.num1 - self.num2
        return subtract
    
    def product(self):
        multiply = self.num1 * self.num2
        return multiply
    
    def divide(self):
        division = self.num1 / self.num2
        return division
    
    def __str__(self):
        representation = "num1 = {}, num2 = {}".format(self.num1, self.num2)
        return representation
    
numbers1 = calculator(10,5)
print(numbers1)
print(numbers1.add())
print(numbers1.difference())
print(numbers1.product())
print(numbers1.divide())




print("----------------------------------------------------------")

