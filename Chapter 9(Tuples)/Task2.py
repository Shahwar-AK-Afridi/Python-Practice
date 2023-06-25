"""Practicing Tuples for adding items"""
"""
   1)Convert Tuple => To List => append() => Convert Back To Tuple
   2)Add tuple to tuple
"""

#First
print("=>(1)Convert Tuple => To List => append() => Convert Back To Tuple")

fruit = ("apple", "banana", "mango", "kiwi")
print("Tuple Before Adding:", fruit)

#Converting "Tuple" to "List"
lst = list(fruit)
print("Before Adding to List:", lst)
lst.append("dragonfruit")
print("After Adding to List:", lst)

#Converting "List" to "Tuple"
fruit = tuple(lst)
print("Tuple After Adding:", fruit)
print("----------------------------------------------------------")

#Second
print("=>(2)Add tuple to tuple")

name = ("John", "Smith", "Charles", "Harry")
print("Tuple Before Adding:", name)

add = ("cena",)

name = name + add
print("Tuple After Adding:", name)
print("----------------------------------------------------------")
