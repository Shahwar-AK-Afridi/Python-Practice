"""
Rewrite your pay program using try and except so that your program
handles non-numeric input gracefully by printing a message and exiting the program.
"""
hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    print("Error, please enter numeric input")
    quit()

rate = input("Enter the rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h <= 40:
    grosspay = h*r
    print("Grosspay:", grosspay)
elif h > 40:
    pay_below_40 = 40*r
    remain = h - 40
    r = r*1.5
    pay_above_40 = remain*r
    sum = pay_above_40 + pay_below_40
    print(sum)
else:
    print("invalid input")
