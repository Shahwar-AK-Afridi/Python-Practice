"""Calculating Sum through For-loop"""

print("Calculating Sum through For-loop")
total = 0                           #Iteration variable = "Thing"
print("Sum Before:%d" %total)
for add in [9,41,12,3,74,15]:
    #Running Total = "total"
    total = total + add             #Inside Loop = we add actual number to the running total during each Iteration
    # total aka accumulator
print("Final Total :%f" %total)   #This total is called as "Overall total of the values"
print("-----------------------------------------------")

"""Calculating Sum of numbers through self-developed function"""

print("Calculating Sum of numbers through self-developed function")
def Summing(numbers):
    total = 0
    for add in numbers:
        total = total + add
    print("Total Sum: %f" %total)
    return

numbers = [9,41,12,3,74,15]
Summing(numbers)
print("-----------------------------------------------")

"""Calculating Sum through built-in function Sum()"""

print("Calculating Sum through built-in function Sum()")
num = [9,41,12,3,74,15]
total = sum(num)
print("Sum: %f" %total)
