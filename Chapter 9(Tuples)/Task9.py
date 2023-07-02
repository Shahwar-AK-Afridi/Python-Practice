"""Practicing Tuple's Questions"""
"""
    1)Write a Python program to create a tuple.
    2)Write a Python program to create a tuple with different data types.
    3)Write a Python program to create a tuple of numbers and print one item.
    4)Write a Python program to unpack a tuple into several variables.
    5)Write a Python program to add an item to a tuple.
"""

#1
print("=>(1)Write a Python program to create a tuple.")

thistuple = ("apple", "banana", "mango", "kiwi", "dragon fruit")
print("Tuple", thistuple)

print("----------------------------------------------------------")

#2
print("=>(2)Write a Python program to create a tuple with different data types.")

thistuple = ("apple", 90.5, True, "banana", 100, False)
print("Tuple:", thistuple)

print("----------------------------------------------------------")

#3
print("=>(3)Write a Python program to create a tuple of numbers and print one item.")

thistuple = (5,5,3,6,7,8,3,3,4,3,43,4,8)
print("One Item:", thistuple[4])
print("----------------------------------------------------------")

#4
print("=>(4)Write a Python program to unpack a tuple into several variables.")

thistuple = ("apple", "banana", "mango", "kiwi", "dragon fruit")           #packing a tuple

(fruit1, *fruit2, fruit3) = thistuple                                      #unpacking a tuple

print("Fruit 1:",fruit1)
print("Fruit 2:",fruit2)
print("Fruit 3:",fruit3)
print("----------------------------------------------------------")


#5
print("=>(5)Write a Python program to add an item to a tuple.")

print("--------------Approach 1--------------")

thistuple = ("apple", "banana", "mango", "kiwi", "dragon fruit")

thistuple = thistuple + ("peach",)
print("Modified Tuple:", thistuple)

print("--------------Approach 2--------------")

thistuple2 = ("apple", "banana", "mango", "kiwi", "dragon fruit")

lst = list(thistuple2)
lst.append("tomato")

thistuple2 = tuple(lst)
print("Modified Tuple:", thistuple2)
print("----------------------------------------------------------")
