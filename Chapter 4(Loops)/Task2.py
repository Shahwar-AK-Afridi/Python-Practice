"""Print the name of user according to user input"""

name = input("Enter Your Name:")
times = input("Printing Number:")
num = int(times)
count = 0
while num > 0:
    print("Hello, %s" %name)
    num = num - 1
    count = count + 1
print("Thank You")
print("We printed Your name %d times" %count)
