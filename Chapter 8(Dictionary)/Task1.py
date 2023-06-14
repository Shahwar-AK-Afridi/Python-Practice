"""Practicing Dictionaries"""
"""1)Creating Dictionaries
   2)Calculating the Length Of dictionaries using (len() & for loop)
   3)Type of dictionary using (type())
   4)Accessing list elements using bracket/index operator[](Positive Index Value) & Slice[:] operator
   5)Accessing list elements using bracket/index operator[](Negative Index Value) & Slice[:] operator
   6)Changing list items using bracket/index[] operator & slice[:] operator
   7)Traversing a list using for-loop only to (READ only)
   8)Traversing a list using for-loop with range() & Len() function to (READ, UPDATE & WRITE)
   9)Searching for elements in a list using (in & not in) operator
   """
#First
print("=>(1)Creating dictionaries")

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

#Second
print("=>(2)Calculating the Length Of dictionaries using (len() & for loop)")

print("-------------Approach 1 using len()-----------------")
intro = dict(Name = "Shahwar", Profession = "Software Engineer", Country = "Pakistan")
length = len(intro)
print("Length:%d" %length)

print("-------------Approach 2 using for loop--------------")
employee = {"Name":"Chuck", "Profession":"Software Engineer", "Country":"Canada"}
count = 0
for item in employee:
    count += 1
print("Length:%d" %count)
print("----------------------------------------------------------")

#Third
print("=>(3)Type of list using (type())")
intro = dict(Name = "Shahwar", Profession = "Software Engineer", Country = "Pakistan")
type = type(intro)
print(type)
print("----------------------------------------------------------")

#Fourth
print("=>Accessing dictionary values using bracket operator[Key Name]")
car = {"Brand":"Ford", "Model":"Mustang","Year":1964}
brand = car["Brand"]
print(brand)
print(car["Year"])



"""name = input("Enter file:")
handle = open(name)
count = dict()
for line in handle:
    line2 = line.strip()
    if line2.startswith("From "):
        words = line2.split()
        words = words[1:2]
        #print(words)
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] = count[word] + 1
    else:
        continue
print(count)

bigcount = None
bigword = None
for key,value in count.items():
    if bigcount == None or value > bigcount:
        bigcount = value
        bigword = key
    else:
        continue
print(bigword, bigcount)
"""
