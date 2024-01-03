"""Practicing For Loop"""

#First
for i in [5,4,3,2,1]: #No Logical Condition to STOP
    print("i =",i)    #No of iteration = No of items in the list
print("Done")

print("------------------------------------------------")

#Second
for i in ["Apple", "Banana", "Mango"]:
    print("i =",i)  #Execute Only three times
print("Done")

print("------------------------------------------------")

#Third
string = "Hello World"
print("The string is %s" %string)
count = 0
for i in string:
    count = count + 1
print("The Length of string is %d" %count)

print("------------------------------------------------")
