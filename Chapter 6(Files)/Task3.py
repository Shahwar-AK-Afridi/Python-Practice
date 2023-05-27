"""Practicing File Handling By Taking Input from Users"""
"""1)Using input() to read user's data
   2)Using try & catch to deal with exceptions"""

#First(Same as Third One)
print("Asking user for file name and then searching for string (@uct.ac.za) in the file")
try:
    fname = input("Enter The File Name:")                           #We read filename from user and assigned it to variable "fname"
    fhand = open(fname, "r")                                        #Checks if file exist of not, if exist then returns "filehandler" to fhand
except:
    print("Incorrect File Name, Please Enter The File Name Again!")
    quit()

for line in fhand:
    if "@uct.ac.za" in line:
        line2 = line.rstrip()
        print(line2)
    else:
        continue
fhand.close()
print("----------------------------------------------------------")

#Second
print("Asking user for file name and then searching lines that starts with(From)")
try:
    fname = input("Enter The File Name:")
    fhand = open(fname,"r")
except:
    print("Incorrect File Name, Please Enter The File Name Again!")
    quit()
for line in fhand:
    if line.startswith("From"):
        line2 = line.rstrip()
        print(line2)
    else:
        continue
fhand.close()
print("----------------------------------------------------------")

#Third(Same as First One)
print("Asking user for file name and then searching lines that have (@uct.ac.za) in that")
try:
    fname = input("Enter The File Name:")
    fhand = open(fname, "r")
except:
    print("Incorrect File Name, Please Enter The File Name Again!")
    quit()
for line in fhand:
    if not line.find("@uct.ac.za") == -1:
        line2 = line.rstrip()
        print(line2)
    else:
        continue
fhand.close()
print("----------------------------------------------------------")

#fourth
print("Asking user for file name and then searching for (@) with read() method")
try:
    fname = input("Enter The File Name:")
    fhand = open(fname, "r")
except:
    print("Incorrect File Name, Please Enter The File Name Again!")
    quit()
inp = fhand.read()
at_sign_post = inp.find("@")
print(at_sign_post)
fhand.close()
print("----------------------------------------------------------")
