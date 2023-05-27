"""Practicing File Handling By Deleting Only"""
"""1)Using (os) module
   2)Using remove() function
   3)Using path() function
   4)Using exists() function"""

import os

#first
print("Checks if file3.txt exist or not")
check = os.path.exists("file3.txt")                                              #Checks if file exists or not
print("File Exists:%s" %check)                                                   #"os.path.exists" returns TRUE or FALSE
print("----------------------------------------------------------")

#Second
print("Deleting file3.txt")
os.remove("file3.txt")                                                           #Deletes the file3.txt
print("----------------------------------------------------------")
