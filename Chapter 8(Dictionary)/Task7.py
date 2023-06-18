"""Practicing Dictionaries with Files"""
"""
    1)Counting word for (Single) line only using => split(), dict(), if-else, get() method
    2)Counting words in a file using => split(), dict(), if-else, get() method
"""
print("=>(1)Counting word for (Single) line only using => split(), dict(), if-else, get() method")

print("-----------------Approach 1 using (if-else) condition---------------------")

sentence = "My name is Shahwar Afridi, and i am a software engineer. Today i am Practicing Dictionaries"
lst = list()
collection = dict()

lst = sentence.split()                                     #returns a list of words
print("list of words:", lst)

for word in lst:
    if word in collection:
        collection[word] = collection[word] + 1
    else:
        collection[word] = 1

print("Dictionary:",collection)                            #Histogram


print("-----------------Approach 2 using get() method--------------------------")

sentence2 = "My name is Shahwar Afridi, and i am a software engineer. Today i am Practicing Dictionaries"
lst2 = list()
collection2 = dict()

lst2 = sentence2.split()
print("List Of Words:", lst2)

for word in lst2:
    collection2[word] = collection2.get(word, 0) + 1

print("Dictionary:", collection2)
print("----------------------------------------------------------")


print("=>(2)Counting words in a file using => split(), dict(), if-else, get() method")

print("-----------------Approach 1 using (if-else) condition---------------------")

try:
    fname = input("Enter The File Name:")
    fhand = open(fname)
except:
    print("File Not Present")
    quit()

collection3 = dict()

for line in fhand:                                          #Reads each line of the file
    list_of_words = line.split()                            #split() breaks each line into list of words
    for word in list_of_words:                              #loop through each of the words in the line
        if word in collection3:
            collection3[word] = collection3[word] + 1
        else:
            collection3[word] = 1

print("Dictionary:", collection3)

print("-------------------Approach 2 using get() method--------------------------")

try:
    fname = input("Enter The File Name:")
    fhand = open(fname)
except:
    print("File Not Present")
    quit()

collection4 = dict()

for line2 in fhand:
    list_of_words2 = line2.split()
    for word in list_of_words2:
        collection4[word] = collection4.get(word, 0) + 1

print("Dictionary:", collection4)
print("----------------------------------------------------------")
