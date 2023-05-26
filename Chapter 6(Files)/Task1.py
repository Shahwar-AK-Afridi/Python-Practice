"""Practicing File Handling By Reading Only"""

#First
print("Using for loop to count the number of lines in the flat file")
fhand = open("mbox.txt", "r")                      #open() returns file handle "fhand"
                                                   #"fhand" is a variable used to perform operations on the file
count = 0
for line in fhand:                                 #"For loop" reads the data one line at a time
    count += 1                                     # Counting the number of lines in the flat file
print("Total Number Of Lines: %d" %count)
fhand.close()
print("----------------------------------------------------------")


#Second
print("Using for loop to print all lines the flat file")
fhand = open("mbox-short.txt", "r")
for line in fhand:                                 #"fhand" is treated as the sequence of lines in our for loop
    line2 = line.rstrip()                          # removes the non-printing characters from right-side
    #print(line2)
fhand.close()
print("----------------------------------------------------------")

#Third
print("Using read() method to read the whole file and print each line")
fhand = open("mbox-short.txt", "r")
file = fhand.read()                                #All characters, including lines and newline characters assigned to-
#print(file)                                        #-variable "file" as "one big string"
print("----------------------------------------------------------")

#fourth
print("Getting the length of one big string")
fhand = open("mbox.txt", "r")
file = fhand.read()
length = len(file)
print(length)
