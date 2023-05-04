#Fruitfull Functions with return statements

def print_twice(name): #"name" is the parameter over here
    print(name)
    print(name)
    return name #If we dont use return statement to return "name" then "result" will produce "None"

"""def print_twice(name): "result" will display "NONE" in this case.
    print(name)
    print(name)
    return
"""
result = print_twice("Bang") #"result" will display ""Bang
print(result)
