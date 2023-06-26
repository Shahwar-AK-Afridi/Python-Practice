"""Practicing Tuples for adding items & Changing Items"""
"""
   1)Convert Tuple => To List => append() to add items => Convert Back To Tuple
   2)Add tuple to tuple
   3)Convert Tuple => To List => bracket operator[] to change item => Convert Back To Tuple
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

#Third
print("=>(3)Convert Tuple => To List => bracket operator[] to change item => Convert Back To Tuple")

Vegatable = ("Lemon", "Tomato", "Cucumber", "Onion")
print("Tuple Before Changing:", fruit)

#Converting "Tuple" to "List"
lst = list(Vegatable)
print("Before Changing List:", lst)
lst[0] = 2
lst[1] = "Green Onion"
lst[2] = True
lst[3] = "Mango"
print("After Changing List:", lst)

#Converting "List" to "Tuple"
Vegatable = tuple(lst)
print("Tuple After Changing:", Vegatable)
print("----------------------------------------------------------")
