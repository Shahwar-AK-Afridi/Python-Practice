"""Practicing dictionary Methods for copying """
"""1)Copying dictionary items using => copy() method
   2)Copying dictionary items using => dict() constructor
"""

#First
print("=>(1)Copying dictionary items using => copy() method")

car12 = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":2019}

duplicate = car12.copy()
print("Copy:", duplicate)
print("----------------------------------------------------------")

#Second
print("=>(2)Copying dictionary items using => dict() constructor")

duplicate2 = dict(car12)
print("Copy2:", duplicate2)
print("----------------------------------------------------------")
