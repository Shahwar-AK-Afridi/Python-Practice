"""Parsing Strings"""
"""1)From string to list of characters using list() constructor/function
   2)From string to list of words/parts using split() method
   3)From string to list of words/parts using split() method with delimiter
   4)From list of words/parts to string using join() method & delimiter"""


fname = input("Enter The File Name:")
fhand = open(fname)
x = list()  #x = [] same
for line in fhand:
    line2 = line.rstrip()
    words = line2.split()
    for element in words:                            # check every element in word
        if element in x:                             # if element is repeated
            continue                                 # do nothing
        else:                                        # else if element is not in the list
            x.append(element)                        # append
x.sort()
print(x)"""

print("-------------Approach 1--------------")
fname = input("Enter The File Name:")
fhand = open("mbox-short.txt")
count = 0

for line in fhand:
    if line.startswith("From "):
        line2 = line.rstrip().split()
        count = count + 1
        address = line2[1]
        print(address)
    else:
        continue
print("There were", count, "lines in the file with From as the first word")

print("-------------Approach 2--------------")
fname = input("Enter file name: ")
counter = 0
fh = open(fname)

for line in fh :
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        print (words[1])
        counter +=1

print ("There were", counter, "lines in the file with From as the first word")
