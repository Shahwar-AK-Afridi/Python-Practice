import statistics

"""Calculating Average through For loop"""

print("Calculating Average through loop")
total = 0
denominator = 0
for num in [9,41,12,3,74,15]:
    total = total + num
    denominator = denominator + 1
print("Total Sum: %d" %total)
print("Total Numbers: %d" %denominator)

Average = float(total/denominator)
print("Average: %f" %Average)
print("-----------------------------------------------")

"""Calculating Average through self-developed function"""

print("Calculating Average through self-developed function")
def average(number):
    total = 0
    denominator = 0
    for num in number:
        total = total + num
        denominator = denominator + 1
    print("Total Sum: %d" %total)
    print("Total Numbers: %d" %denominator)
    Average = float(total/denominator)
    print("Average: %f" %Average)
    return

number = [9,41,12,3,74,15]
average(number)
print("-----------------------------------------------")

"""Calculating Average through built-in function mean()"""

print("Calculating Average through built-in function mean()")
number = [9,41,12,3,74,15]
Average = statistics.mean(number)
print("Average: %f" %Average)
print("-----------------------------------------------")
