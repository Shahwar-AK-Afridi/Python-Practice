""""String Methods and Library"""

#First
print("Lists the available methods/functions for string")
char = "Hello World"
print(type(char))
print(dir(char))                        #Shows bunch of methods in the class"str"
print("----------------------------------------------------------")

#Second
print("How to get documentation on a method")
help(char.strip)                         #Describe the use of find
print("----------------------------------------------------------")

#Third
print("Using lower() method:")
third = "HELLO WORLD"                   #Original string is not changed
zap = third.lower()                     #Makes a copy of "third" in lower case and store it into "zap"
print("zap: ",zap)
print("Original string is not changed :", third)
print("----------------------------------------------------------")

#Fourth
print("Using find() method")
fourth = "This is the python"
zap = fourth.find("e")                 #Finds the first occurance of "e"
print("Position of e is:", zap)
zap2 = fourth.find("pyt")
print("Position of substring:", zap2)  #It tells where the "pyt" is positioned within the string
zap3 = fourth.find("t", 11)
print("Start after the 11th index:", zap3)
print("----------------------------------------------------------")

#Fifth
print("Using upper() method")
fifth = "this is python language"       #Original string is not altered
print("Normal String:", fifth)
zap = fifth.upper()                     #Makes copy of altered string and store it into zap
print("String in Upper case:", zap)
print("----------------------------------------------------------")

#Sixth
print("Using lower() method")
sixth = "HELLO TO THE WORLD"           #Original string is not altered
print("Normal String:", sixth)
zap = sixth.lower()
print("String in Lower case:", zap)
print("----------------------------------------------------------")

#Seventh
print("Using replace() method")
seventh = "X-DSPAM-Confidence:0.8475"
print("Old String: %s" %seventh)
print("Replacing DSPAM from PYTHON")
zap = seventh.replace("DSPAM","PYTHON") #It replaces all the occurances of the search string with replacement string
print("New String: %s" %zap)
print("----------------------------------------------------------")

#Eighth
print("Using lstrip(), strip(), rstrip() to remove whitespaces")
eighth = "       Hello there is whitespaces        "
print(eighth)
zap = eighth.strip()
print("Removing from both start & end: %s" %zap)
zap2 = eighth.rstrip()
print("Removing from right side only: %s" %zap2)
zap3 = eighth.lstrip()
print("Removing from left side only: %s" %zap3)
print("----------------------------------------------------------")

#Ninth
print("Using startswith() method")
ninth = "Have a nice day"
print("Text: %s" %ninth)
zap = ninth.startswith("H")             #Requires case to match, therefore first convert the whole string using lower() method
print("Starts with H: %s" %zap)         # into lower case then use startswith()
zap = ninth.startswith("h")
print("Starts with h: %s" %zap)
zap = ninth.lower().startswith("h")     #here text is first converted into lower-case then "h" is searched
print("Coverted into lowercase so starts with h: %s" % zap)
zap = ninth.startswith("Have")
print("Starts with Have: %s" %zap)
print("----------------------------------------------------------")

#Tenth
print("Using Multiple methods call")
text = "Today we learned about methods used in strings"
zap = text.lower().startswith("today")  #Using multiple methods call in a single expression
print("Starts with a t: %s" %zap)
