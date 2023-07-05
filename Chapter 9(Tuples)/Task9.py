"""Practicing Tuple's Questions"""
"""
    1)Write a Python program to create a tuple.
    2)Write a Python program to create a tuple with different data types.
    3)Write a Python program to create a tuple of numbers and print one item.
    4)Write a Python program to unpack a tuple into several variables.
    5)Write a Python program to add an item to a tuple.
    6)Write a Python program to convert a tuple to a string.
    7)Write a Python program to get the 4th element from the last element of a tuple.
    8)Write a Python program to create the colon of a tuple.
    9)Write a Python program to find repeated items in a tuple.
   10)Write a Python program to check whether an element exists within a tuple.
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

#6
print("=>(6)Write a Python program to convert a tuple to a string.")

character = ("a","p","p","l","e")

delimiter = ""
fruit = delimiter.join(character)
print("String:", fruit)

print("----------------------------------------------------------")

#7
print("=>(7)Write a Python program to get the 4th element from the last element of a tuple.")

thistuple = ("apple", "banana", "mango", "kiwi", "dragon fruit")

#Get item (4th element)of the tuple by index
item = thistuple[3]
print(item)
#Get item (4th element from last)by index negative
item1 = thistuple[-4]
print(item1)
print("----------------------------------------------------------")

#8
print("=>(8)Write a Python program to create the colon of a tuple.")




print("----------------------------------------------------------")

#9
print("=>(9)Write a Python program to find repeated items in a tuple.")

thistuple = ("apple", "banana", "mango", "kiwi", "dragon fruit", "apple", "banana", "apple")
lst = list()

for item in thistuple:
    if thistuple.count(item) > 1:
        lst.append(item)
    else:
        continue

print(lst)

print(lst)
print("----------------------------------------------------------")

#10
print("=>(10)Write a Python program to check whether an element exists within a tuple.")



print("----------------------------------------------------------")
