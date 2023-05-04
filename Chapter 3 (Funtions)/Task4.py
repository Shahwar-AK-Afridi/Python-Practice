#First: Just Revoking or calling a function
def print_lyrics():          #Header
    print("Hello World")
    print("Hello World")
    return"hello"

# a will save the residual value and then prints it however print() function doesnot need to be returned
a = print_lyrics() #hello will be assigned to a
print(a)

#Second: Using function within function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    return

repeat_lyrics()
