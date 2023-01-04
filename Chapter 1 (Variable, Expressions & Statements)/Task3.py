"""
Write a program which prompt the user for a celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature
"""
celsius = input("Enter the temperature in celsius:")

try:
    cel = float(celsius)
except:
    print("Enter the value in numeric form")
    quit()

fahrenheit = (cel * 9/5) + 32
print("The temperature in fahrenheit:", fahrenheit)
