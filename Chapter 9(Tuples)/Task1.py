"""Practicing Tuples"""
"""
   1)Creating tuples using => single item, with tuple() constructor & without tuple constructor
   2)Calculating the Length Of tuples using => len() & for loop
   3)Type of tuple using => type()
   4)Accessing tuples items using => bracket opertor[], slicing[:]
   5)Tuple Assignment => Packing Tuples
   6)Tuple Assignment => Unpacking Tuples
   7)Traversing a tuple using => for-loop, while-loop, range()
   8)Combining two tuples using (+) operator
   9)Repeats a tuple using (*) operator
  10)Searching for items in a tuple using => (in & not in) operator
"""

#First
print("=>(1)Creating tuples using => single item, with tuple() constructor & without tuple() constructor")

print("-------------Approach 1 with one item only--------------")

intro = ("Name",)                                                               #tuple constant assigned to "intro"
#must add comma "," if you are creating tuple with single item
print(intro)
print(type(intro))

print("-------------Approach 2 without tuple constructor--------------")

employee = ("John", "Charles", "Smith", "Ben")                                  #tuples can store multiple items in a single variable
print(employee)
print(type(employee))

print("-------------Approach 3 with tuple constructor--------------")

fruit = tuple(("apple", "banana", "mango", "kiwi"))
print(fruit)
print(type(fruit))

print("-------------Approach 4 tuple with different datatype--------------")

thistuple = ("apple", 45, True, "banana", 33, False)
print("Tuple with values of different datatype:", thistuple)
print("----------------------------------------------------------")

#Second
print("=>(2)Calculating the Length Of tuples using => len() & for loop")

print("-------------Approach 1 using len()--------------")
name = ("John", "Charles", "Smith", "Ben")
print("Length:", len(name))

print("-------------Approach 2 using for loop--------------")

name = ("John", "Charles", "Smith", "Ben")
count = 0
for item in name:
    count = count + 1
print("Length:", count)
print("----------------------------------------------------------")

#Third
print("=>(3)Type of tuple using => type()")

name = ("John", "Charles", "Smith", "Ben")
print(name)
print("Type:", type(name))
print("----------------------------------------------------------")

#Fourth
print("=>(4)Accessing tuples items using => bracket opertor[], slicing[:]")

print("-------------Approach 1 using bracket operator with positive indices--------------")

fruit = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")
f1 = fruit[0]
print("Index[0]:", f1)
f2 = fruit[4]
print("Index[4]:", f2)

print("-------------Approach 2 using bracket operator with negative indices--------------")

fruit = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")
f3 = fruit[-1]
print("Index[-1]:", f3)
f4 = fruit[-5]
print("Index[-5]:", f4)

print("-------------Approach 3 using slicing operator with positive indices--------------")

fruit2 = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")
f5 = fruit2[1:4]
print("Index[0:4]:", f5)
f6 = fruit2[3:]
print("Index[3:]:", f6)

print("-------------Approach 4 using slicing operator with negative indices--------------")

fruit2 = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")
f7 = fruit2[-4:-1]
print("Index[-4:-1]:", f7)
f8 = fruit2[-5:]
print("Index[-5:]", f8)
print("----------------------------------------------------------")

#Fifth
print("=>(5)Tuple Assignment => packing tuples")

#here we place tuple on the left-side of the assignment statement
#When we normally assign values to a tuple, this is called "Packing" a tuple.

print("-------------PART A (assigning multiple values to a single variable)--------------")

fruit3 = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")          #packing a tuple
print(fruit3)

print("-------------PART B (assigning multiple values to multiple variables)--------------")

#No of variables on left == No of values on right
(x,y) = (4, "fred")       # x = 4                                                  #AKA Simultaneous Assignment Statement
print("x:",x)             # y = "fred"
print("y:",y)

print("-------------PART C (assigning list to tuple of variable)--------------")

lst = ["apple", "mango", "orange"]
(f1,f2,f3) = lst
print("Fruit 1:", f1)               # f1 = lst[0]
print("Fruit 2:", f2)               # f2 = lst[1]
print("Fruit 3:", f3)               # f3 = lst[2]

print("-------------PART D (assigning expression to tuple of variable--------------")

address = "monty@python.org"
(uname, domain) = address.split("@")          #split returns a list ["monty", "python.org"]
print("User name:", uname)
print("Domain:", domain)
print("----------------------------------------------------------")

#Sixth
print("=>(6)Tuple Assignment => Unpacking tuples")

#When we extract values back into variables, this is called "Unpacking" a tuple.

print("-------------PART A (No of variable == No of values)--------------")

#left-Side = tuple of variables
#Right-Side = tuple of values

(f1,f2,f3) = ("apple", "banana", "mango")                                       #Unpacking a Tuple
#(f1,f2,f3) same as f1,f2,f3                                                    #we can avoid parenthesis
print("f1:", f1)
print("f2:", f2)
print("f3:", f3)

print("-------------PART B (No of variable < No of values)--------------")

print("---Adding Asterisk * to the last variable---")
(f1,f2,*f3) = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")
print("f1:", f1)
print("f2:", f2)
print("f3:", f3)                    #extra values are assigned to variable "f3" as a LIST

print("---Adding Asterisk * to another variable than the last variable---")
(f1,*f2,f3) = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")
print("f1:", f1)
print("f2:", f2)                    #assigned a list of values to "f2"
print("f3:", f3)
print("----------------------------------------------------------")

#Seventh
print("=>(7)Traversing a tuple using => for-loop, while-loop, range()")

print("-------------Approach 1 (for-loop)--------------")

fruit4 = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")
for item in fruit4:
    print(item)

print("-------------Approach 2 (for-loop & range())--------------")

fruit5 = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")
for item in range(len(fruit5)):
    print(fruit5[item])

print("-------------Approach 3 (while-loop)--------------")

fruit6 = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")
i = 0
while i < len(fruit6):
    print(fruit6[i])
    i = i + 1
print("----------------------------------------------------------")

#Eighth
print("=>(8)Combining two tuples using (+) operator")

name = ("John", "Smith", "Charles")
fruit7 = ("apple", "banana", "mango", "kiwi")

merge = name + fruit7
print("Merge Result:", merge)
print("----------------------------------------------------------")

#Ninth
print("=>(9)Repeats a tuple using (*) operator")

fruit8 = ("apple", "banana", "mango", "kiwi")

product = fruit8 * 3
print("Product:", product)
print("----------------------------------------------------------")

#Tenth
print("(10)Searching for items in a tuple using => (in & not in) operator")

fruit9 = ("apple", "banana", "mango", "kiwi", "appricot", "dragon fruit")

if "banana" in fruit9:
    print("Yes, Banana is there")
else:
    print("No, Banana is not there")

if "john" not in fruit9:
    print("John is not there")
else:
    print("No")
print("----------------------------------------------------------")
