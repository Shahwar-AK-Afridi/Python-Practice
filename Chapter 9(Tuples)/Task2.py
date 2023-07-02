"""Practicing Tuples for adding items & Changing Items"""
"""
   1)Convert Tuple => To List => append() to add items => Convert Back To Tuple
   2)Add tuple to tuple using => + operator
   3)Convert Tuple => To List => bracket operator[] to change item => Convert Back To Tuple
   4)Adding more than one items in a single line
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

name = name + add                                        # name = name + ("cena",)
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

#Fourth
print("=>(4)Adding more than one items in a single line")

vegatable = ("Lemon", "Tomato", "Cucumber", "Onion")

vegetable = vegatable + ("mango", "banana", "watermelon")

print(vegetable)
print("----------------------------------------------------------")

#Fifth
print("=>(5)Adding items in a specific index")

sample = ('Lemon', 'Tomato', 'Cucumber', 'Onion', 'mango', 'banana', 'watermelon')

sample = sample[:2] + ("john", "Charles") + sample[2:]

print(sample)
