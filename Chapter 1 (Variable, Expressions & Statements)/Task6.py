#Question:

"""Write a Python program that calculates the area of a circle based on the radius entered by the user."""

#Code:
import math
try:
    radius= input("Enter The Radius: ")
except:
    print("Enter A Numeric Input:")

r = float(radius)
area = math.pi * (r**2)
print("Area of circle:", area)

#Sample Code

"""
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
"""
