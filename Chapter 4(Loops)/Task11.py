""""Find The Smallest Number
    1)Using for loop to read only
    2)Using min() function"""

number = [22,44,76,98,56,33,55,11,23]

print("----------Approach 1 using for loop to read only----------")
def smallest(number):
    try:
        smallest_so_far = number[0]                          #We assume the list is not empty. This line initializes a variable called 'smallest_so_far' to the first element of the list.
    except:
        print("Empty List, Please Enter Again!")
        quit()
    for item in number:
        if item < smallest_so_far:
            smallest_so_far = item
        else:
            continue
    return smallest_so_far                                   #This line returns the final value of the 'smallest_so_far' variable after the loop has finished

smallest_so_far = smallest(number)
print("Smallest Item:", smallest_so_far)

print("-------------Approach 2 using min() function--------------")

number = [22,44,76,98,56,33,55,3,23]
smallest_so_far = min(number)
print("Smallest Item:", smallest_so_far)
