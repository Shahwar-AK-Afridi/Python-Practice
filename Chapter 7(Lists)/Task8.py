"""Parsing Strings"""
"""Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
                               From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
   You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
   Then print out a count at the end"""


print("-------------Approach 1--------------")
fname = input("Enter The File Name:")
fhand = open(fname)
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
fh = open(fname)
counter = 0

for line in fh :
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        print (words[1])
        counter +=1

print ("There were", counter, "lines in the file with From as the first word")


print("-------------Approach 3--------------")
fname = input("Enter The File Name:")
fhand = open(fname)
counter = 0

for line in fhand:
    line2 = line.rstrip()
    word = line2.split()
    #short circuiting is used & len(word) as guardian pattern
    if len(word) < 3 or word[0] != "From":
        continue
    else:
        counter = counter + 1
        print(word[1])
print ("There were", counter, "lines in the file with From as the first word")
