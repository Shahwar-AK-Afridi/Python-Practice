"""Practicing Dictionaries"""
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

#Second
print("=>(2)Calculating the Length Of dictionaries using => len() & for loop")

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
print("=>(3)Type of dictionary using => type()")
intro = dict(Name = "Shahwar", Profession = "Software Engineer", Country = "Pakistan")
type = type(intro)
print(type)
print("----------------------------------------------------------")

#Fourth
print("=>(4)Accessing dictionary items using => bracket opertor[], get(), keys(), values(), item()")

print("-------------Approach 1 using bracket operator[key name]-----------------")

car = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}
ford = car["Model"]
print("First Car:%s" %ford)
toyota = car["Model2"]
print("Second Car:%s" %toyota)

print("-------------Approach 2 using get() method-----------------")

car2 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}
model = car2.get("Model")                       #get() returns "value" of the given "key"
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

#Fifth
print("=>(5)Changing dictionary items using => bracket operator[] , update()")

print("-------------Approach 1 using bracket operator[key name]-----------------")

car6 = {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 1964, 'Brand2': 'Toyota', 'Model2': 'Corolla', 'Year2': '2019', 'Brand3': 'Suzuki', 'Model3': 'Alto', 'Year3': 2022}

print("Before Changes:", car6)
car6["Year"] = 2023
print("After Changes:", car6)

print("-------------Approach 2 using update() method-----------------")

car7 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}

print("Before Update:", car7)
car7.update({"Brand2":"Audi"})          #update() takes key:value pair as argument
print("After Update:", car7)
print("----------------------------------------------------------")

#Sixth
print("=>(6)Traversing a dictionary using => for-loop to print keys")

car8 = {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 1964, 'Brand2': 'Toyota', 'Model2': 'Corolla', 'Year2': '2019', 'Brand3': 'Suzuki', 'Model3': 'Alto', 'Year3': 2022}

for key in car8:
    print("key:", key)
print("----------------------------------------------------------")

#Seventh
print("=>(7)Traversing a dictionary using => for-loop to print values")

car9 = {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 1964, 'Brand2': 'Toyota', 'Model2': 'Corolla', 'Year2': '2019', 'Brand3': 'Suzuki', 'Model3': 'Alto', 'Year3': 2022}

for key in car9:
    print("Value:", car9[key])
print("----------------------------------------------------------")

#Eighth
print("=>(8)Traversing a dictionary using => for-loop & values() method to print values")

car10 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}

for value in car10.values():
    print("Value:", value)
print("----------------------------------------------------------")

#Ninth
print("=>(9)Traversing a dictionary using => for-loop & keys() method to print keys")

car11 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}

for keys in car11.keys():
    print("Keys:", keys)
print("----------------------------------------------------------")

#Tenth
print("=>(10)Traversing a dictionary using => for-loop & item() method with both KEYS & VALUES")

car12 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}

for key, val  in car12.items():
    print("Tuple:",key,":", val)
print("----------------------------------------------------------")

print("=>(11)Searching for keys in a dictionary using => (in & not in) operator")

car13 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}

if "Model3" in car13:
    print("Yes, Model2 is in dictionary")
elif "Model3" not in car13:
    print("No, Mo is not in dictionary")
else:
    print("ok")
print("----------------------------------------------------------")

print("=>(12)Searching for values in a dictionary using => (in & not in) operator & values() method")

car14 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}

if "Ford" in car14.values():                        #first convert dictionary to a type where it can be converted into dictionary, then use "in" operator
    print("Yes, Ford is there")
elif "Ford" not in car14.values():
    print("No, Ford is not there")
else:
    print("ok")
print("----------------------------------------------------------")

print("=>(13)Creating Nested Dictionaries")

print("-------------Approach 1 Create 3 dictionaries, then add them to 1 big dictionary-----------------")

child1 = {                              #1st child Dictionary
    "name":"Shahwar Afridi",
    "year":1999
}

child2 = {                              #2nd child Dictionary
    "name":"Smith",
    "year": 2010
}

child3 = {                              #3rd child Dictionary
    "name":"John",
    "year":2000
}

myfamily = {                            #Parent Dictionary
    "kid1":child1,
    "kid2":child2,
    "kid3":child3
}
print(myfamily)

print("-------------Approach 2 creating nested dictionary from start-----------------")

myfamily2 = {
    "child1" :{
    "name":"Shahwar Afridi",
    "year":1999
    },
    "child2":{
    "name":"Smith",
    "year":2010
    },
    "child3":{
    "name":"pinapple",
    "year":2010
    }
}

print(myfamily2)
print("----------------------------------------------------------")

print("=>(14)Accessing dictionary items")

#Accessing from Approach 1
print("----------Accessing from Approach 1----------")
print(myfamily["kid1"])
print(myfamily["kid2"]["name"])

#Accessing from Approach 2
print("----------Accessing from Approach 2----------")
print(myfamily2["child1"])
print(myfamily2["child2"]["name"])
print("----------------------------------------------------------")
