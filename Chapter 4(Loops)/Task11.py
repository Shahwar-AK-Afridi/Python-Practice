"""Practicing Conditional Statements and Loop Questions"""
"""
   1)Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)
   2)Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
   3)
   4)
   5)
   6)
   7)
   8)
   9)
  10)
"""
#1
print("Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)")

def divisor(start: int, end: int)->list:
    new = []
    for num in range(start,end):
        if num % 7 == 0 and num % 5 == 0:
            new.append(num)
    return new

print(divisor(1500,2701))

print("----------------------------------------------------------")

#2
print("Write a Python program to convert temperatures to and from Celsius and Fahrenheit.")
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
"""
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""
def cel_to_fh(temp: float, celsius = True)->int:
    if celsius == True:
        c = round((5 * (temp - 32))/9)
        return c
    elif celsius == False:
        f = round((temp * 9)/5 +32)
        return f

print(cel_to_fh(60, False))
print(cel_to_fh(45))
print("----------------------------------------------------------")
