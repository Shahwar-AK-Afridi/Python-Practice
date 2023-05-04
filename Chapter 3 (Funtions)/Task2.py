# QUESTION:
"""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number
"""
#Code
try:
    hour = input("Enter Hour: ")
    hrs = float(hour)
    rate = input("Enter Rate: ")
    rat = float(rate)
except:
    print("Kindly Enter Numeric Input")
    quit()

def computepay(hrs, rat):
    if hrs <= 40:
        p = hrs*rat
        return p
    elif hrs > 40:
        less_40 = 40*rat
        more_40 = (hrs-40) * (1.5*rat)
        total = less_40 + more_40
        return total
    else:
        return "Hello"

pay = computepay(hrs,rat)
print("Pay: ", pay)
