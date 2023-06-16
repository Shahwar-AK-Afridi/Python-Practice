"""Practicing Dictionary Methods for removing and deleting items"""
"""
   1)Removing a specified item from the dictionary using => pop() method
   2)Removing last item from the dictionary using => popitem() method
   3)Removing item from the dictionary using => del keyword
   4)Deleting a dictionary using => del keyword
   5)Removing all items of the dictionary using => clear() method
"""


car1 = {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 1964, 'Brand2': 'Toyota', 'Model2': 'Corolla', 'Year2': '2019', 'Brand5': 'AUDI', 'Model5': 'A8', 'Year5': 2023, 'Brand4': 'Honda', 'Model4': 'Civic', 'Year4': 2023}
print("Before Removing:", car1)

#First
print("=>(1)Removing a specified item from the dictionary using => pop() method")

pair1 = car1.pop("Brand")                         #pop() removes key:value pair and returns it
print("Item Removed:", pair1)
print("After Removing:", car1)
print("----------------------------------------------------------")

#Second
print("=>(2)Removing last item from the dictionary using => popitem() method")

pair2 = car1.popitem()
print("Item Removed:", pair2)                     #popitem() removes the last item and returns it
print("After Removing", car1)
print("----------------------------------------------------------")

#Third
print("=>(3)Removing item from the dictionary using => del keyword")

del car1["Model2"]                                #argument = key
print("After Removing:", car1)
print("----------------------------------------------------------")

#Fourth
print("=>(4)Deleting a dictionary using => del keyword")

car2 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":2019}
print("Before Deleting:", car2)
del car2
try:
    print(car2)
except:
    print("After Deleting: Dictionary car2 deleted.")
print("----------------------------------------------------------")

#Fifth
print("=>(5)Removing all items of the dictionary using => clear() method")

car3 = {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 1964, 'Brand2': 'Toyota', 'Model2': 'Corolla', 'Year2': '2019', 'Brand5': 'AUDI', 'Model5': 'A8', 'Year5': 2023, 'Brand4': 'Honda', 'Model4': 'Civic', 'Year4': 2023}
print("Before Clearing:", car3)
car3.clear()
print("After Clearing:", car3)
print("----------------------------------------------------------")
