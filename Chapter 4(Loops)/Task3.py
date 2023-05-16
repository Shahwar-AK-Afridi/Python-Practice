

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
    sexy = 7
    return sexy

yoyo = print_name(name,num)
print(yoyo)
