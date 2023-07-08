"""Practicing Tuple's Questions"""
"""
    1)Write a Python program to create a tuple.
    2)Write a Python program to create a tuple with different data types.
    3)Write a Python program to create a tuple of numbers and print one item.
    4)Write a Python program to unpack a tuple into several variables.
    5)Write a Python program to add an item to a tuple.
    6)Write a Python program to convert a tuple to a string.
    7)Write a Python program to get the 4th element from the last element of a tuple.
    8)Write a Python program to create the colon of a tuple.(CHECK)
    9)Write a Python program to find repeated items in a tuple.
   10)Write a Python program to check whether an element exists within a tuple.
   11)Write a Python program to convert a list to a tuple.
   12)Write a Python program to remove an item from a tuple.
   13)Write a Python program to slice a tuple.
   14)Write a Python program to find the index of an item in a tuple
   15)Write a Python program to find the length of a tuple.
   16)Write a Python program to convert a tuple to a dictionary.
   17)Write a Python program to unzip a list of tuples into individual lists.(CHECK)
   18)Write a Python program to reverse a tuple.
   19)Write a Python program to convert a list of tuples into a dictionary.
   20)Write a Python program to print a tuple with string formatting.
   21)Write a Python program to replace the last value of tuples in a list.
   22)Write a Python program to remove an empty tuple(s) from a list of tuples.(CHECK)
   23)Write a Python program to sort a tuple by its float element.
   24)Write a Python program to count the elements in a list until an element is a tuple.
   25)Write a Python program to convert a given string list to a tuple.
"""
import random

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
collection = dict()

for item in thistuple:
    if thistuple.count(item) > 1:
        print("%s is repeated" %item)
        if item in collection:
            collection[item] = collection[item] + 1
        else:
            collection[item] = 1
    else:
        continue

print("Repeated Words:", collection)

print("----------------------------------------------------------")

#10
print("=>(10)Write a Python program to check whether an element exists within a tuple.")

thistuple = ("apple", "banana", "mango", "kiwi", "dragon fruit", "apple", "banana", "apple")

word1 = "kiwi"
word2 = "tomoto"

def checker(word):
    if word in thistuple:
        return True
    else:
        return False

result = checker(word2)
print(result)

print("----------------------------------------------------------")

#11
print("=>(11)Write a Python program to convert a list to a tuple.")

lst = ["apple", "banana", "mango", "kiwi", "dragon fruit", "apple", "banana", "apple"]
print("list:", lst)

thistuple = tuple(lst)

print("Tuple:", thistuple)
print("----------------------------------------------------------")

#12
print("=>(12)Write a Python program to remove an item from a tuple.")

thistuple = ("apple", "banana", "mango", "kiwi", "dragon fruit", "apple", "banana", "apple")

print("Tuple Before Removing:", thistuple)
lst = list(thistuple)
lst.remove("kiwi")
thistuple = tuple(lst)
print("Tuple After Removing:", thistuple)
print("----------------------------------------------------------")

#13
print("=>(13)Write a Python program to slice a tuple")

thistuple = ("apple", "banana", "mango", "kiwi", "dragon fruit", "apple", "banana", "apple")

slice1 = thistuple[:3]
print("Elements from 0th Index to 2nd Index:", slice1)

slice2 = thistuple[-4:]
print("Elements from -1 index to -4 index:", slice2)

slice3 = thistuple[::-1]                           #Tuple in Reverse Order
print("Tuple in Reverse Order:", slice3)

#tuple[start:stop:step]
slice4 = thistuple[2:5:2]                            #returns a tuple with a jump every 1 items
print(slice4)

slice5 = thistuple[5:2:-2]                         #when step is negative the jump is made back
print(slice5)
print("----------------------------------------------------------")

#14
print("=>(14)Write a Python program to find the index of an item in a tuple")

thistuple = ("apple", "banana", "mango", "apple", "dragon fruit", "apple", "banana", "apple")

word = "apple"
#finds the first occurance
print(thistuple.index(word))

#define the index from which you want to search
print(thistuple.index(word, 1))

#define the segment of the tuple to be searched
print(thistuple.index(word, 4, 7))
print("----------------------------------------------------------")

#15
print("=>(15)Write a Python program to find the length of a tuple.")

thistuple = ("apple", "banana", "mango", "apple", "dragon fruit", "apple", "banana", "apple")

print("Length:", len(thistuple))
print("----------------------------------------------------------")

#16
print("=>(16)Write a Python program to convert a tuple to a dictionary.")

print("----------Type 1----------")
thistuple = ("apple", "banana", "mango", "apple", "dragon fruit", "apple", "banana", "apple","mango", "dragon fruit")
dic_seq = dict()

for item in thistuple:
    if item in dic_seq:
        dic_seq[item] = dic_seq[item] + 1
    else:
        dic_seq[item] = 1

print("Dictionary:", dic_seq)

print("----------Type 2----------")

tuplex = (("apple",3),("mango",5),("pinapple",4))
dic_seq = dict(tuplex)
print(dic_seq)
print("----------------------------------------------------------")

#17
print("=>(17)Write a Python program to unzip a list of tuples into individual lists.")

print("----------Zipping Values----------")
# initializing lists
name = ("John", "Smith", "Charles", "Simon")
marks = (30,65,22,80)
subject = ("maths", "computer", "physics", "chemistry")

# using zip() to map values
mapped = list(zip(name, subject, marks))
print("Zipped result:", mapped)

print("----------UnZipping Values----------")

# unzipping values
name, subject, marks = zip(*mapped)

print("Names:", name)
print("Marks:", marks)
print("Subject:", subject)
print("----------------------------------------------------------")

#18
print("=>(18)Write a Python program to reverse a tuple.")

thistuple = ("apple", "banana", "mango", "apple", "dragon fruit", "apple", "banana", "apple","mango", "dragon fruit")

reverse = thistuple[::-1]
print("Reversed Tuple:", reverse)

print("----------------------------------------------------------")

#19
print("=>(19)Write a Python program to convert a list of tuples into a dictionary.")

lst = [('John', 30), ('Smith', 65), ('Charles', 22), ('Simon', 80)]

dic = dict(lst)
print(dic)
print("----------------------------------------------------------")

#20
print("=>(20)Write a Python program to print a tuple with string formatting.")

Sample = (100, 200, 300)
#Output : This is a tuple (100, 200, 300)

print("This is a tuple {}".format(Sample))
print("----------------------------------------------------------")

#21
print("=>(21)Write a Python program to replace the last value of tuples in a list.")

sample = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

new = list()
for v1,v2,v3 in sample:
    v3 = 100
    new.append((v1,v2,v3))

print("List Of Tuples Modified:", new)
print("----------------------------------------------------------")

#22
print("=>(22)Write a Python program to remove an empty tuple(s) from a list of tuples.")

sample = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

print("----------Approach 1----------")
new = list()
for item in sample:
    if len(item) == 0:
        del item
    else:
        new.append(item)

print(new)

print("----------Approach 2----------")

new2 = list()
for element in sample:
    if bool(element) == True:
        new2.append(element)
    else:
        continue

print(new2)
print("----------------------------------------------------------")

#23
print("=>(23)Write a Python program to sort a tuple by its float element.")

sample = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
new3 = list()

for key, val in sample:
    new3.append((val,key))

new3 = sorted(new3, reverse = True)
sample.clear()

for val, key in new3:
    sample.append((key, val))

print("Finalized List of Tuples:", sample)
print("----------------------------------------------------------")

#24
print("=>(24)Write a Python program to count the elements in a list until an element is a tuple.")

num = [10,20,30,(10,20),40]
count = 0
for item in num:
    if isinstance(item, tuple):             #type(item) is tuple =>> same
        continue
    else:
        count = count + 1

print("Total Number of Integers:", count)
print("----------------------------------------------------------")

#25
print("=>(25)Write a Python program to convert a given string list to a tuple.")

string = "python 3.0"
#<class 'str'>
#expected output: ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')

tup = tuple()

for char in string:
    if char.isspace() == True:
        continue
    else:
        tup = tup + (char,)
print("Final Tuple:", tup)
print("----------------------------------------------------------")
