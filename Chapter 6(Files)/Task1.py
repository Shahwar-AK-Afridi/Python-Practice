"""Practicing File Handling By Reading Only"""
"""1) Using for loop
    2) Using read() Method
    3) Using readline() Method"""

#First
print("Using for loop to count the number of lines in the flat file")
fhand = open("mbox.txt", "r")                      #open() returns file handle "fhand"
                                                   #"fhand" is a variable used to perform operations on the file
count = 0
#iteration variable "line" will be assigned each line one-by-one
for line in fhand:                                 #"For loop" reads the data one line at a time
    count += 1                                     # Counting the number of lines in the flat file
print("Total Number Of Lines: %d" %count)
fhand.close()
print("----------------------------------------------------------")


#Second
print("Using for loop to print all lines the flat file")
fhand = open("mbox-short.txt", "r")
for line in fhand:                                 #"fhand" is treated as the sequence of lines in our for loop
    line2 = line.rstrip()                          #"rstrip()" removes the non-printing characters from right-side
    #print(line2)
fhand.close()
print("----------------------------------------------------------")

#Third
print("Using read() method to read the whole file and print each line")
fhand = open("mbox-short.txt", "r")
file = fhand.read()                                #All characters, including lines and newline characters assigned to-
#print(file)                                       #-variable "file" as "one big string"
print("----------------------------------------------------------")

#fourth
print("Getting the length of one big string")
fhand = open("mbox.txt", "r")
file = fhand.read()
length = len(file)
print("Length: %d" %length)
fhand.close()
print("----------------------------------------------------------")

#Fifth
print("Getting length using for loop")
fhand = open("mbox.txt", "r")
file = fhand.read()
count = 0
for length in file:                             #Here "file" behaves as a "one big string"
    count += 1
print("Length: %d" %count)
fhand.close()
print("----------------------------------------------------------")

#Sixth
print("Printing Slice of string using for loop")
fhand = open("mbox-short.txt", "r")
for line in fhand:
    line2 = line.rstrip()
    extract = line2[:20]
    #print(extract)
print("----------------------------------------------------------")

#Seventh
print("Printing Slice of string using read() method")
fhand = open("mbox-short.txt", "r")
file = fhand.read()                             #"one big string" assigned to file
extract  = file[0:20]
print("Extracted String: %s" %extract)
print("----------------------------------------------------------")

#eighth
print("Reading one line at a time using readline() method")
fhand = open("mbox-short.txt", "r")
line1 = fhand.readline().rstrip()               #Using rstrip to remove non-printing charac for right-side
print("Line 1: %s" %line1)
line2 = fhand.readline()
print("Line 2: %s" %line2)
line3 = fhand.readline()
print("Line 3: %s" %line3)
print("----------------------------------------------------------")
