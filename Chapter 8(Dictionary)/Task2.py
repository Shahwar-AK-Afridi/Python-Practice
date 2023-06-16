"""Practicing Dictionary Methods for adding items
   1)Adding dictionary items using => bracket operator[]
   2)Adding dictionary items using => update() method
"""

#First
print("=>(1)Adding dictionary items using => bracket operator[]")

car = {"Brand":"Ford", "Model":"Mustang","Year":1964, "Brand2":"Toyota", "Model2":"Corolla","Year2":"2019"}

print("Before Adding:", car)
car["Brand5"] = "AUDI"
car["Model5"] = "A8"
car["Year5"] = 2023
print("After Adding:", car)
print("----------------------------------------------------------")

#Second
print("=>(2)Adding dictionary items using => update() method")

print("Before Adding:", car)
car.update({"Brand4":"Honda"})
car.update({"Model4":"Civic"})
car.update({"Year4":2023})
print("After Updating:", car)
print("----------------------------------------------------------")
