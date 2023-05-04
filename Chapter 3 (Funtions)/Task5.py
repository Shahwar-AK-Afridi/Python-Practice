#Using arguments and parameters in Python

def print_twice(name): #"name" is the parameter over here
    print(name)
    print(name)
    return

def print_thrice(name):
    print(name)
    print(name)
    print(name)
    return

Fname = input("Enter Your Name: ")
print_twice(Fname) #"Fname" is the argument over here

lname = input("Enter Your last Name: ")
print_thrice(lname) #"lname" is the argument over here
