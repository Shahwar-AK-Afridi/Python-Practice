"""Practicing Lists"""
"""1)Creating lists
   2)Calculating the Length Of List using (len() & for loop)
   3)Type of list using (type())
   4)Creating list using (list[] constructor)
   5)Combining list using (+) operator
   6)Repeats a list using (*) operator
   7)Accessing list elements using bracket/index operator[](Positive Index Value) & Slice[:] operator
   8)Accessing list elements using bracket/index operator[](Negative Index Value) & Slice[:] operator
   9)Changing list items using bracket/index[] operator & slice[:] operator
  10)Traversing a list using for-loop only to (READ only)
  11)Traversing a list using for-loop with range() & Len() function to (READ, UPDATE & WRITE)
  12)Searching for elements in a list using (in & not in) operator"""

#First
print("=>(1)Creating Lists")
thislist = ["apple", "banana", "mango"]                                         #Three different strings assigned to single variable
print("First:", thislist)

numbers = [1,10,100]
print("Second:", numbers)

empty = []
print("Third:", empty)                                                          #Empty List

nested = ["apple", "mango", [1,4,100],"pinapple"]                               #Nested List
print("Fourth:", nested)

fruit =["apple", "mango","banana"]                                              #fruit is now called list of strings
vegetable = ["potato", "onion", "green onion"]
print("Fifth:", fruit, vegetable)
print("----------------------------------------------------------")

#Second
print("=>(2)Calculating the Length Of List using (len() & for loop)")
print("-------------Approach 1 using Len() function--------------")
thislist = ["apple", "mango", "banana", "peach"]
length = len(thislist)                                                          #Len() function takes list as parameter and returns the number of elements in the list
print("Length:%d" %length)

print("------------Approach 2 using for loop---------------------")
count = 0
for i in thislist:
    count += 1
print("Length:%d" %count)
print("----------------------------------------------------------")

#Third
print("=>(3)Type of list using (type())")
vegetable = ["potato", "onion", "green onion"]
print("type:",type(vegetable))                                                  #list is a datatype
print("----------------------------------------------------------")

#fourth
print("=>(4)Creating list using (list[] constructor)")
hello = list(("Hp", "Lenovo", "Toshiba", "Dell"))
print(hello)
print("----------------------------------------------------------")

#Fifth
print("=>(5)Combining list using (+) operator")
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print("Concatinated List:", list3)
print("----------------------------------------------------------")

#Sixth
print("=>(6)Repeats a list using (*) operator")
list1 = ["mango"] * 5
print(list1)
list2 = [1,3,"apple"] * 5
print(list2)
print("----------------------------------------------------------")

#Seventh
print("=>(7)Accessing list elements using bracket/index operator[](Positive Index Value) & Slice[:] operator")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS"]
com1 = company[2]
print("Company:", com1)

#slicing lists
com2 = company[0:3]                                                             #company[3] is excluded
print("Companies:", com2)
print("----------------------------------------------------------")

#Eighth
print("=>(8)Accessing list elements using bracket/index operator[](Negative Index Value) & Slice[:] operator")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS"]
com3 = company[-1]                                                              #-1 refers to the last item
print("Company:", com3)

#slicing list using negative index
com4 = company[-4:-1]                                                           #company[-1] is excluded
print("Companies:", com4)
print("----------------------------------------------------------")

#Ninth
print("=>(9)Changing list items using bracket/index[] operator & slice[:] operator")
print("Change item value one by one")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS", "Acer", "Samsung"]        #list is mutable
print("Before:",company)
company[1] = "mango"                                                            #make a copy of list if you want to keep the original list unaltered
company[2] = "banana"
company[3] = "peach"
company[4] = "Dragon Fruit"
print("After:",company)

print("Change Range of item values using slice[:] operator")

print("----PART A (Equal items inserted and replaced)----")
phone = ["Samsung", "Blackberry", "Apple", "Oppo", "Vivo", "Huawei", "Amazon"]
print("Before", phone)
#Equal items inserted and replaced
phone[0:3] = ["Toyota", "Honda", "Suzuki"]
print("After:", phone)

print("----PART B (More items inserted than replaced)----")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS", "Acer", "Samsung"]        #list is mutable
print("Before:", company)
length_before = len(company)
print("Length Before:", length_before)
#More items inserted than replaced
company[0:3] = ["Toyota", "Honda", "Suzuki", "peugeot", "Hyundai"]              #
print("After:", company)
length_after = len(company)
print("Length After:", length_after)

print("----PART C(Less items inserted than replaced)----")
fruit = ["apple", "mango", "banana", "dragon fruit", "peach" ,"appricot"]
print("Before:", fruit)
length_before = len(fruit)
print("Length Before:", length_before)
#Less items inserted than replaced
fruit[1:6] = ["Watermelon"]
print("After:", fruit)
length_after = len(fruit)
print("Length After:", length_after)
print("----------------------------------------------------------")

#Tenth
print("=>(10)Traversing a list using for-loop only to (READ only)")
                                                                                #Good for "READING" the elements of list ONLY
for friend in ["joseph", "glenn", "sally"]:                                     #iteration variable "i" go-through the actual elements of the list
    print("Happy New Year:", friend)

print("=>Traversing A list using for loop")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS", "Acer", "Samsung"]
count = 0
for i in company:
    count += 1
    print("Company %d:%s" %(count, i))
print("Total companies in market: %d" %count)
print("----------------------------------------------------------")

#Eleventh
print("=>(11)Traversing a list using for-loop with range() & Len() function to (READ, UPDATE & WRITE)")
friends = ["John", "Simon", "Ben"]
#counted loop or index loop
for i in range(len(friends)):                                                   #Good for "READING", "WRITING", "UPDATING" the elements of list
    name = friends[i]                                                           #iteration variable "i" go-through the index of the list
    print("Hello:", name)

print("=>Traversing A list using for loop with range() & Len() function")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS", "Acer", "Samsung"]
for i in range(len(company)):                                                   #with the help of range() function we can correspond to index position of list.
    print("Company at index (%d): %s" %(i, company[i]))                         #length() returns the number of elements[7]
                                                                                #range() returns indices[0,1,2,3,4,5,6]
print("----------------------------------------------------------")

#Twelfth
print("=>(12)Searching for elements in a list using (in & not in) operator")
company = ["Hp", "Lenovo", "Toshiba", "Dell", "ASUS", "Acer", "Samsung"]
if "Hp" in company:
    print("Yes, Hp is in the list")
elif "apple" not in company:
    print("No, Apple is not in the list")
else:
    print("Try Again!")
print("----------------------------------------------------------")
