"""
Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
"""

try:
    num = input("Enter the Number: ")
    n = int(num)
except:
    print("Give Numeric Input!")

def prime():
   if n%n==0 and n%1==0:
       return "This is Prime number"
   else:
       return "Not A Prime Number"

apple = prime()
print(apple)
