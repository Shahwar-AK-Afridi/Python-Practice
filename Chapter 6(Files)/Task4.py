"""Practicing File Handling By Searching Only"""
"""1)Using read() method
   2)Using String Methods (Startswith(), strip())
   3)Using String Slicing"""

#First
print("Searching of the lines starting with (From) using startswith()")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if line.startswith("From"):                         #Only lines starting with "From" will be printed and others are skipped
        print(line)                                     #each line has "\n" at the end, \n is there but invisible to us
    else:
        continue
print("----------------------------------------------------------")

#Second
print("Checking whether string startswith (From) or not")
fhand = open("words.txt","r")
line = fhand.read()
line2 = line.startswith("From")                         #Returns "True" or "False"
print(line2)
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
print("----------------------------------------------------------")

#fourth
print("Searching of the lines starting with (From) using startswith() and removing whitespace with string slicing")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    if line.startswith("From"):
        extract = line[:-2]                             #newline is considered as "whitespace"
        print(extract)
    else:
        continue
print("----------------------------------------------------------")

#Fifth
