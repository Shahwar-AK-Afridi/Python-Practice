"""Parsing Strings"""
"""Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
   The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
   When the program completes, sort and print the resulting words in python sort() order as shown in the desired output."""


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
