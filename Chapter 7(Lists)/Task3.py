"""Practicing List's Methods for removing and deleting items"""
"""1)Removing a specified item from the list using remove() method
   2)Removing item on specified index using pop() method
   3)Removing elements from the list using del keyword and slice[:] operator
   4)Removing ALL elements of list in one go using clear() method"""

#First
print("=>(1)Removing a specified item from the list using remove() method")
thislist = ["apple", "banana", "mango"]
print("Before Removing:", thislist)
thislist.remove("apple")                                                        #remove() removes the specified item when we don't know its index
print("After Removing:", thislist)

print("-------------Duplicate Elements in the List---------------")
thislist2 = ["apple","apple", "mango"]
print("Before Removing:", thislist2)
thislist2.remove("apple")
print("After Removing:", thislist2)                                             #remove() only removes the first matching element from the list
print("----------------------------------------------------------")

#Second
print("=>(2)Removing item on specified index using pop() method")
thislist = ["samsung", "apple", "blackberry", "huawei", "vivo"]
print("Before Removing:", thislist)
#pop() returns the element to phone
phone = thislist.pop(2)                                                         #pop() removes the element from index and assign it to "phone"
print("Item Removed:", phone)
print("After Removing:", thislist)

print("-------Removes last item if index is not defined---------")
thislist = ["apple", "banana", "mango"]
print("Before Removing:", thislist)
fruit = thislist.pop()                                                          #no index so last item will me removed and returned
print("Item Removed:", fruit)
print("After Removing:", thislist)
print("----------------------------------------------------------")

#Third
print("=>(3)Removing elements from the list using del keyword and slice[:] operator")

print("----PART A (deleting item on specified index)-----------")
thislist = ["john", "ben", "simon", "jack", "steve"]
print("Before Removing:", thislist)
del thislist[2]
print("After Removing:", thislist)

print("----PART B (deleting the list completely)--------------")
phones = ["samsung", "apple", "blackberry", "huawei", "vivo"]
print("Before Removing:", phones)
del phones

print("----PART C (deleting more than one element with slice operator)----")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS", "Acer", "Samsung"]        #list is mutable
print("Before Removing:", company)
del company[1:6]
print("After Removing:", company)
print("----------------------------------------------------------")

#fourth
print("=>(4)Removing ALL elements of list in one go using clear() method")
thislist = ["john", "ben", "simon", "jack", "steve"]
print("Before Removing:", thislist)
thislist.clear()
print("After Removing:", thislist)
