"""Practicing List's Methods for sorting"""
"""1)Copying List using copy() method
   2)Copying List using list() constructor
   3)Using Built-in Functions on lists"""

#First
print("=>(1)Copying a list using copy() method")

print("--------PART A (Copying Alphabates)-----------")
thislist = ["z", "b", "m", "d", "y", "x", "q", "w", "a", "e", "s", "f", "g", "h", "j", "k", "l"]
print("Original List", thislist)
copy = thislist.copy()
print("Copied List:", copy)

print("--------PART B (Copying Numbers)-----------")
numbers = [8,4,0,2,66,44,87,34,22,97,54,100,34,65,1,48,73]
print("Original List:", numbers)
copy = numbers.copy()
print("Copied List:", copy)
print("----------------------------------------------------------")

#Second
print("=>(2)Copying a list using list constructor()")
phones = ["samsung", "apple", "blackberry", "huawei", "vivo"]
print("Original List:", phones)
laptop = list(phones)
print("Copied List:", laptop)
print("----------------------------------------------------------")

#Third
print("=>(3)Using Built-in Functions on lists")
numbers = [8,4,0,2,66,44,87,34,22,97,54,100,34,65,1,48,73]
print("The List:", numbers)
print("--------PART A (Calculating length using len() function)-----------")
length = len(numbers)
print("Length:", length)
print("--------PART B (Calculating maximum using max() function)-----------")
maximum = max(numbers)
print("Maximum:", maximum)
print("--------PART C (Calculating minimum using min() function)-----------")
minimum = min(numbers)
print("Minimum:", minimum)
print("--------PART D (Calculating minimum using sum() function)-----------")
total = sum(numbers)
print("Sum:",total)
