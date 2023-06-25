"""Practicing Tuples"""
"""
   1)Creating Dictionaries using => bracket operator[], dict(), dict_name = {}
   2)Calculating the Length Of dictionaries using => len() & for loop
   3)Type of dictionary using => type()
   4)Accessing dictionary items using => bracket opertor[], get(), keys(), values(), item()
   5)Changing dictionary items using => bracket operator[] , update()
   6)Traversing a dictionary using => for-loop to print keys
   7)Traversing a dictionary using => for-loop to print values
   8)Traversing a dictionary using => for-loop & values() method to print values
   9)Traversing a dictionary using => for-loop & keys() method to print keys
  10)Traversing a dictionary using => for-loop & item() method with both KEYS & VALUES
  11)Searching for keys in a dictionary using => (in & not in) operator
  12)Searching for keys in a dictionary using => (in & not in) operator & values() method
  13)Creating Nested Dictionaries
  14)Accessing dictionary items
"""

#First
print("=>(1)Creating Dictionaries using => bracket operator[], dict(), dict_name = {}")

print("-------------Approach 1 using dict() constructor--------------")
intro = dict(Name = "Shahwar", Profession = "Software Engineer", Country = "Pakistan")     #Dictionary constant assigned to "intro"
print(intro)

print("-------------Approach 2 without dict() constructor--------------")
employee = {"Name":"Chuck", "Profession":"Software Engineer", "Country":"Canada"}
print(employee)

print("-------------Approach 3 one by one with bracket operator[]------")
stuff = dict()                                                                  #makes an empty dictionary object
stuff["pencil"] = 10
stuff["pen"] = 5
stuff["marker"] = 2                                                             #storing "2" under the label "marker"
print(stuff)
print("----------------------------------------------------------")
