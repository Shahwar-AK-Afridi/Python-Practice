"""Practicing Tuples for copying and built-in functions"""
"""1)Copying Tuples using => copy() method
   2)Copying Tuples using => tuples() constructor
   3)Using Built-in Functions on Tuples"""

#First
print("=>(1)Copying a tuple using copy() method")

thistuple = ("z", "b", "m", "d", "y", "x", "q", "w", "a", "e", "s", "f", "g", "h", "j", "k", "l")
print("Original Tuple:", thistuple)
thislist = list(thistuple)
print("Converted To List:", thislist)
new_list = thislist.copy()
print("Copied List:", new_list)
new_tuple = tuple(new_list)
print("Converted To Tuple:", new_tuple)
print("----------------------------------------------------------")

#Second
print("=>(2)Copying Tuples using => tuples() constructor")
phones = ("samsung", "apple", "blackberry", "huawei", "vivo")
print("Original Tuple:", phones)
laptop = tuple(phones)
print("Copied Tuple:", laptop)
print("----------------------------------------------------------")

#Third
print("=>(3)Using Built-in Functions on Tuples")
numbers = (8,4,0,2,66,44,87,34,22,97,54,100,34,65,1,48,73)
print("The Tuple:", numbers)
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
print("----------------------------------------------------------")
