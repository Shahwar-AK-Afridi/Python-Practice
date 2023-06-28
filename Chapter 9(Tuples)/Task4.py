"""Practicing Tuples for comparing & sorting"""
"""
   1)Comparing Two Tuples
   2)Sorting tuples using => sorted()
   3)Sorting Dictionaries by converting to list of tuples using => items(), sorted(), append() for-loop
   4)Sorting tuples Alphanumerically or Ascending Order using => sorted()
   5)Sorting tuple in descending Order using => sorted() with keyword (reverse=True)
   6)Sorting tuple based on lowercase & uppercase letters using sorted() method (Case-sensitive Sort)
"""

#First
print("=>(1)Comparing Two Tuples")

print("--------PART A (First Element Are Different)-----------")

thistuple1 = (1,2,4)
thistuple2 = (0,67,20000)                           #Compares first Element Only, 1 & 0

if thistuple1 > thistuple2:
    print("Tuple 1 > Tuple 2")
else:
    print("Tuple 1 < Tuple 2")

print("--------PART B (First Element Are Same)-----------")

thistuple3 = (5,1000, 55)   	                   #Compares second element only, 1000 & 22
thistuple4 = (5,22,50000)

if thistuple3 > thistuple4:
    print("Tuple 3 > Tuple 4")
else:
    print("Tuple 3 < Tuple 4")

print("--------PART C (First Element Are Same)-----------")

thistuple5 = ("John", "Ben", "Charles")
thistuple6 = ("John", "Smith", "Cena")

if thistuple5 > thistuple6:                        # "Ben" & "Smith" are compared.
    print("Tuple 5 > Tuple 6")
else:
    print("Tuple 5 < Tuple 6")
print("----------------------------------------------------------")

#Second
print("=>(2)Sorting tuples using => sorted()")

print("--------PART A (Characters/String only)-----------")

alphabet = ("z","f","s","l","k","r","y","u","o","a","p","e")
sorted_list = sorted(alphabet)
print(sorted_list)

print("--------PART B (integers only)-----------")

numbers = (6,3,100,0,2,34,63,89,44,2,48,1,23,99)
sorted_list2 = sorted(numbers)
print(sorted_list2)

print("--------PART C (List of Tuples)-----------")

d = {"mango":4, "apple":7, "banana":11, "dragonfruit":12}
print("Dictionary:", d)
lst = d.items()
print("List Before Sorting:", lst)
sorted_list_of_tuples = sorted(lst)                            #Sorting is done based on keys/first element
print("List After Sorting:", sorted_list_of_tuples)
print("----------------------------------------------------------")

#Third
print("=>(3)Sorting Dictionaries by converting to list of tuples using => items(), sorted(), append(), for loop")

print("--------PART A (Sort By Keys)-----------")

d2 = {"mango":4, "apple":7, "banana":11, "dragonfruit":12}
temp = list()

for (key, val) in sorted(d.items()):                                 #items() return a list of tuples which is unsorted
    temp.append((key, val))

temp = sorted(temp)
print(temp)                                                        #sorted() uses keys to sort the list (Compare keys in tuples)

print("--------PART B (Sort By Values)-----------")

d2 = {"mango":4, "apple":7, "banana":11, "dragonfruit":12}
temp = list()

for (key, val) in d.items():                                        # key,val == (key, val)
    temp.append((val, key))                             #we will get new tuples, but in value:key form
print("Ascending Order:", temp)

temp = sorted(temp, reverse = True)                     #Sorted will compare first-element/values in list
print("Descending Order:", temp)                                             #in this case, if values come equal than sorted() sorts based on keys
print("----------------------------------------------------------")

#fourth
print("=>(4)Sorting tuples Alphanumerically or Ascending Order using sorted()")

alphabet = ("z","f","s","l","k","r","y","u","o","a","p","e")
sorted_list = sorted(alphabet)
print(sorted_list)
print("----------------------------------------------------------")


#Fifth
print("=>(5)Sorting tuple in descending Order using => sorted() with keyword (reverse=True)")

alphabet = ("r","f","s","l","k","z","y","u","o","a","p","e")
sorted_list2 = sorted(alphabet, reverse = True)
print(sorted_list2)
print("----------------------------------------------------------")

#Sixth
print("=>(6)Sorting tuple based on lowercase & uppercase letters using sorted() method (Case-sensitive Sort)")

alphabet = ("a", "Z", "f", "G", "k","L", "z", "w")
sorted_list3 = sorted(alphabet)
print(sorted_list3)
print("----------------------------------------------------------")
