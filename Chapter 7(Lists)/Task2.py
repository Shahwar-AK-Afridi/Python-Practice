"""Practicing List's Methods for adding items"""
"""1)Adding items in the list using append() method
   2)Adding an item at the specified index using insert() method
   3)Adding elements from another list to the current list using extend() method & (+) operator
   4)Creating an empty list and then add elements one by one to it using list() constructor & append() method
   5)Adding item in a list using slice[:] operator"""

#First
print("=>(1)Adding items in the list using append() method")
thislist = ["apple", "banana", "mango"]
print("Before Appending:", thislist)
thislist.append("dragon fruit")                                                 #append() adds item to the end of the list
print("After Appending:", thislist)
print("----------------------------------------------------------")

#Second
print("=>(2)Adding an item at the specified index using insert() method")
thislist = ["apple", "banana", "mango"]
print("Before Appending:", thislist)
thislist.insert(1,"Samsung")                                                    #insert() inserts an item at specified index
print("After Appending:", thislist)
print("----------------------------------------------------------")

#Third
print("=>(3)Adding elements from another list to the current list using extend() method & (+) operator")
print("-------------Approach 1 using extend() method--------------")
fruit = ["apple", "banana", "mango"]
print("Before:", fruit)
phone = ["Samsung", "apple", "Huawei", "ASUS"]                                  #phone remain unmodified
fruit.extend(phone)                                                             #extend() adds item to the end of the list
print("After:", fruit)

print("-------------Approach 2 using (+) operator----------------")
list1 = ["a","b","c"]
list2 = [1,2,3]
print("Before", list1)
list1 = list1 + list2
print("After:", list1)
print("----------------------------------------------------------")

#fourth
print("=>(4)Creating an empty list and then add elements one by one to it using list() constructor & append() method")
stuff = list()                                                                  #Creates an empty list
print("Before:", stuff)
stuff.append("Samsung")
stuff.append("Apple")
stuff.append("Huawei")
stuff.append("ASUS")
stuff.append("OPPO")
stuff.append("Vivo")
print("After:", stuff)
print("----------------------------------------------------------")

#Fifth
print("=>(5)Adding item in a list using slice[:] operator")

print("-------------Case 1 (item inserted = item replaced)--------------")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS", "Acer", "Samsung"]        #list is mutable
print("Before:", company)
company[0:3] = ["mango", "banana", "dragonfruit"]
print("After:", company)

print("-------------Case 2 (item inserted > item replaced)--------------")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS", "Acer", "Samsung"]        #list is mutable
print("Before:", company)
company[0:2] = ["mango", "banana", "dragonfruit"]
print("After:", company)

print("-------------Case 3 (item inserted < item replaced)--------------")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS", "Acer", "Samsung"]        #list is mutable
print("Before:", company)
company[0:6] = ["mango"]
print("After:", company)
