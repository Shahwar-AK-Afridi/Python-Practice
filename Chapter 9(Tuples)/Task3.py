"""Practicing Tuples for removing items"""
"""
   1)Convert Tuple => To List => remove()/del[]/pop() => Convert Back To Tuple
   2)Delete whole tuple using => del keyword
"""

#First
print("=>(1)Convert Tuple => To List => remove()/del[]/pop() => Convert Back To Tuple")

print("-------------Approach 1 using => remove()--------------")

fruit = ("apple", "banana", "mango", "kiwi")
print("Tuple Before Removing:", fruit)

#Converting "Tuple" to "List"
lst = list(fruit)
print("List Before Removing Item:", lst)
lst.remove("banana")
print("List After Removing Item:", lst)

#Converting "List" to "Tuple"
fruit = tuple(lst)
print("Tuple After Removing:", fruit)

print("-------------Approach 2 using => del[]--------------")

name = ("John", "Smith", "Charles", "Cena")
print("Tuple Before Removing:", name)

#Converting "Tuple" to "List"
lst = list(name)
print("List Before Removing Item:", lst)
del lst[1]
print("List After Removing Item:", lst)

#Converting "List" to "Tuple"
name = tuple(lst)
print("Tuple After Removing:", name)

print("-------------Approach 3 using => pop()--------------")

name2 = ("John", "Smith", "Charles", "Cena")
print("Tuple Before Removing:", name2)

#Converting "Tuple" to "List"
lst = list(name2)
print("List Before Removing Item:", lst)
eliminate = lst.pop(2)
print("List After Removing Item:", lst)

#Converting "List" to "Tuple"
name2 = tuple(lst)
print("Tuple After Removing:", name2)
print("----------------------------------------------------------")

#Second
print("=>(2)Delete whole tuple using => del keyword")

name3 = ("John", "Smith", "Charles", "Cena")
del name3
try:
    print(name3)
except:
    print("Tuple is Deleted")
print("----------------------------------------------------------")
