"""Practicing dictionary's Methods for sorting"""
"""
   1)Sorting dictionary Alphanumerically or Ascending Order using => list() constructor, sort() method
   2)Sorting dictionary in descending Order using => sort() method with keyword (reverse=True)
   3)Sorting dictionary based on lowercase & uppercase letters => using sort() method (Case-sensitive Sort)
   4)Reversing the current order of dictionary => using reverse() method
"""

print("=>(1)Sorting dictionary Alphanumerically or Ascending Order using => list() constructor, sort() method")

collection1 = {'math': 45.50, 'science':35, 'computer': 41.30, 'english':55, 'history': 24}

keys = collection1.keys()                   #returns a type which can be converted into list
lst_of_keys1 = list(keys)
print("Before Sorting:",lst_of_keys1)

#sorting lst_of_keys1
lst_of_keys1.sort()
print("After Sorting:",lst_of_keys1)

for key in lst_of_keys1:
    print("%s:%d" %(key, collection1[key]))
print("----------------------------------------------------------")

print("=>(2)Sorting dictionary in descending Order using sort() method with keyword (reverse=True)")

collection2 = {'math': 45.50, 'science':35, 'computer': 41.30, 'english':55, 'history': 24,"zology":99}

keys = collection2.keys()
lst_of_keys2 = list(keys)
print("Before Sorting:", lst_of_keys2)

#sorting lst_of_keys
lst_of_keys2.sort(reverse = True)
print("After Sorting:", lst_of_keys2)

for key in lst_of_keys2:
    print("%s:%d" %(key, collection2[key]))
print("----------------------------------------------------------")

print("=>(3)Sorting dictionary based on lowercase & uppercase letters using sort() method (Case-sensitive Sort)")

collection3 = {"a":2,"b":4,"C":5,"d":4,"e":7,"F":2,"g":8,"A":9,"O":2,"p":55,"z":1}

keys = collection3.keys()
lst_of_keys3 = list(keys)
print("Before Sorting:", lst_of_keys3)

lst_of_keys3.sort()
print("After Sorting:", lst_of_keys3)

for key in lst_of_keys3:
    print("%s:%d" %(key, collection3[key]))
print("----------------------------------------------------------")

print("=>(4)Reversing the current order of dictionary using reverse() method")

collection4 = {"a":2,"b":4,"C":5,"d":4,"e":7,"F":2,"g":8,"A":9,"O":2,"p":55,"z":1}

keys = collection4.keys()
lst_of_keys4 = list(keys)
print("Before Reversing:", lst_of_keys4)

lst_of_keys4.reverse()
print("After Reversing:", lst_of_keys4)

for key in lst_of_keys4:
    print("%s:%d" %(key, collection4[key]))
print("----------------------------------------------------------")
