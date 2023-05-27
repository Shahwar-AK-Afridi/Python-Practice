"""Practicing File Handling By Searching Only"""
"""1)Using read() method
   2)Using String Methods (Startswith(), strip(), find())
   3)Using String Slicing
   4)Using operators(in , not)"""

#First
print("Searching of the lines starting with (From) using startswith()")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if line.startswith("From"):                         #Only lines starting with "From" will be printed and others are skipped
        print(line)                                     #each line has "\n" at the end, \n is there but invisible to us
    else:
        continue
fhand.close()
print("----------------------------------------------------------")

#Second
print("Checking whether string startswith (From) or not")
fhand = open("words.txt","r")
line = fhand.read()
line2 = line.startswith("From")                         #Returns "True" or "False"
print(line2)
fhand.close()
print("----------------------------------------------------------")

#Third
print("Searching of the lines starting with (From) using startswith() and removing whitespace with rstrip()")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if line.startswith("From"):
        line2 = line.rstrip()                           #removing newline character "\n" from the end of each line
        print(line2)
    else:
        continue
fhand.close()
print("----------------------------------------------------------")

#Fourth
print("Searching of the lines starting with (From) using startswith() and removing whitespace with string slicing")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if line.startswith("From"):
        extract = line[:-2]                             #newline is considered as "whitespace"
        print(extract)
    else:
        continue
fhand.close()
print("----------------------------------------------------------")

#Fifth
print("Searching for lines starting with (From) using startswith() and here we will use (not) operator")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if not line.startswith("From"):                     #if line doesnot starts with "From" so skip that line
        continue
    else:
        print(line)
fhand.close()
print("----------------------------------------------------------")

#Sixth
print("Searching for string anywhere in a line")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if "@uct.ac.za" in line:                            #"in" returns TRUE or FALSE
        line2 = line.rstrip()
        print(line2)
    else:
        continue
fhand.close()
print("----------------------------------------------------------")

#Seventh
print("Searching for string in a line using (not) operator")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if not "@uct.ac.za" in line:                        #it checks if a line have "@uct.ac.za" then it is printed otherwise skips it
        continue
    else:
        line2 = line.rstrip()
        print(line2)
fhand.close()
print("----------------------------------------------------------")

#Eighth
print("Searching for string in a line using find() method")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if line.find("@uct.ac.za") == -1:
        continue
    else:
        line2 = line.rstrip()
        print(line2)
fhand.close()
print("----------------------------------------------------------")

#Ninth
print("Searching for string in a line using find() method with (not) operator")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if not line.find("@uct.ac.za") == -1:
        line2 = line.rstrip()
        print(line2)
    else:
        continue
fhand.close()
print("----------------------------------------------------------")
