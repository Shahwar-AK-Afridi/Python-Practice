"""Practicing Dictionaries"""
"""1)Creating Dictionaries
   2)Calculating the Length Of dictionaries using (len() & for loop)
   3)Type of dictionary using (type())
   4)Accessing dictionary items using bracket opertor[], get(), keys(), values(), item()
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
print("=>(4)Accessing dictionary items")

print("-------------Approach 1 using bracket operator[key name]-----------------")

car = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}
ford = car["Model"]
print("First Car:%s" %ford)
toyota = car["Model2"]
print("Second Car:%s" %toyota)

print("-------------Approach 2 using get() method-----------------")

car2 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}
model = car2.get("Ford")
print("First Model:%s" %model)
model2 = car2.get("asdf", "Not Available")
print("Second Model:%s" %model2)

print("-------------Approach 3 using keys() method-----------------")

car3 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":2019}

#before the change
list_keys = car3.keys()                        #keys() returns keys as type that can be converted into a list
print("Before Chnges:", list_keys)             #"dict_keys" are like "view" of dictionary,

#after the change
car3["Model3"] = "Suzuki"
list_keys = car3.keys()
print("After Chnages:", list_keys)            #making changes to the car3 will reflect changes into "dict_keys"

print("-------------Approach 4 using values() method-----------------")

car4 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}

#before changes
list_values = car4.values()                   #values() returns values as type that can be converted into a list
print("Before Changes:", list_values)         #dict_values are like "view" of dictionary

#after changes
car4["Model3"] = "Suzuki"
list_values = car4.values()
print("After Changes:", list_values)         #making changes to the car4 will reflect changes into "dict_values"

print("-------------Approach 5 using items() method-----------------")

car5 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}

#Before Changes
key_value = car5.items()                    #items() return key-value pair as a tuple
print("Before Changes:", key_value)         #dict_items are like "view" of dictionary

#After Changes
car5["Brand3"] = "Suzuki"
car5["Model3"] = "Alto"
car5["Year3"] = 2022
print("After Changes", key_value)           #making changes to the car4 will reflect changes into "dict_items"
print("----------------------------------------------------------")






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
