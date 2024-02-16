"""
    1)Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
    2)Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age
    3)Write a Python program to create a calculator class. Include methods for basic arithmetic operations
    4)Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square
"""
import datetime, math

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
        today = datetime.date.today()
        born = today.year - self.date_of_birth.year
        if today < datetime.date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            born = born - 1
        return born
    
    def __str__(self):
        representation = "Your Name is {} and you are born in {} and your age is {}".format(self.name,self.country,self.date_of_birth)
        return representation

p1 = Person("Shahwar","Pakistan", datetime.date(1999, 11 ,27))
print(p1.age())

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

#4
print("(4)Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square")

class shape:

    def area(self):
        pass

    def perimeter(self):
        pass

class circle(shape):

    def __init__(self, radius):
        self.radius = radius

    #Method redefining or overriding
    def area(self):
        area_of_circle = math.pi * (self.radius ** 2)
        return area_of_circle
    
    #Method redefining or overriding
    def perimeter(self):
        perimeter_of_circle = 2 * math.pi * self.radius
        return perimeter_of_circle
    
class triangle(shape):

    def __init__(self, height, base, hyp):
        self.height = height
        self.base = base
        self.hyp = hyp
    
    def area(self):
        area_of_triangle = 0.5 * self.base * self.height
        return area_of_triangle
    
    def perimeter(self):
        perimeter_of_triangle = self.hyp + self.height + self.base
        return perimeter_of_triangle
    
class rectangle(shape):

    def __init__(self, height , width):
        self.height = height
        self.width = width

    def area(self):
        area_of_rectangle = self.height * self.width
        return area_of_rectangle
    
    def perimeter(self):
        perimeter_of_rectangle = (2 * self.height)+(2 * self.width)
        return perimeter_of_rectangle
    

circle1 = circle(7)
print("Circle Area = ",circle1.area())
print("Circle Perimeter = ",circle1.perimeter())

rectangle1 = rectangle(5,7)
print("Rectangle Area = ",rectangle1.area())
print("Rectangle Perimeter = ",rectangle1.perimeter())

triangle1 = triangle(4,5,3)
print("Triangle Area = ",triangle1.area())
print("Triangle Perimeter = ",triangle1.perimeter())
print("----------------------------------------------------------")
