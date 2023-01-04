"""
Write a program to prompt the user for hours and rate per hour to compute grosspay.
"""
hour = input("Enter the number of hours you worked:")
rate = input("Enter the rate given to you:")
try:
    h = int(hour)
    r = int(rate)
except:
    print("Enter a numeric input")
    quit()
grosspay = h * r
print("Grosspay:Rs", grosspay)
