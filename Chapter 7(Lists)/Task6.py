"""Practicing List's Methods for list and string conversion"""
"""1)From string to list of characters using list() constructor/function
   2)From string to list of words/parts using split() method
   3)From string to list of words/parts using split() method with delimiter
   4)From list of words/parts to string using join() method & delimiter"""

#First
print("=>(1)From string to list of characters using list() constructor/function")
phone = "Samsung Galaxy S9"
print("Original String:%s" %phone)
my_phone = list(phone)                                                          #list() return a list,it breaks the string into individual characters
print("List of Characters:", my_phone)
print("----------------------------------------------------------")

#Second
print("=>(2)From string to list of words/parts using split() method")
myself = "I am a software engineer, and I use samsung galaxy s9"
#delimiter = whitespace
words = myself.split()                                                          #split() method, breaks string into list of words/parts
print("List Of Words:", words)                                                  #split() used whitespace as a delimiter now
print("----------------------------------------------------------")

#Third
print("=>(3)From string to list of words/parts using split() method with delimiter")

print("--------PART A (delimiter = hyphen(-))-----------")
error = "spam-spam-spam-spam@gmail.com"
#delimiter = hyphen "-"
words = error.split("-")                                                        #delimiter is an argument we pass into split() method
print("List of Words:", words)                                                  #delimiter indicates where a string should split

print("--------PART B (delimiter = semicolon(;))--------")
line = "first;second;third"
#delimiter = hyphen ";"
string = line.split(";")
print("List of Words:", string)

print("--------PART C (delimiter = null)----------------")
line2 = "first;second;third"
string2 = line2.split()                                                         #Split() is looking for spaces as it finds none,
print("List of Words:", string2)                                                #hence it returns whole string as a single element
print("----------------------------------------------------------")

#fourth
print("=>(4)From list of words/parts to string using join() method & delimiter")
words_list = ['I', 'am', 'a', 'software', 'engineer,', 'and', 'I', 'use', 'samsung', 'galaxy', 's9']
print("List of words:", words_list)
#delimiter is space character
delimiter = " "                                                                 #join() puts space between words
myself2 = delimiter.join(words_list)                                            #join() is a string method
print("String:", myself2)                                                       #we have to invoke it on the delimiter & pass the list as a parameter
print("----------------------------------------------------------")
