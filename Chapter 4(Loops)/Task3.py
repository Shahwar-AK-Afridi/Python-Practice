"""Print user name the according to user input by using while loop and function print_name"""

name = input("Enter Your Name:")
times = input("Printing Number:")
num = int(times)

def print_name(name,num):
    count = 0
    while num > 0:
        print("Hello, %s" %name)
        num = num - 1
        count = count + 1
    print("Thank You")
    print("We printed Your name %d times" %count)
    return

print_name(name,num)
