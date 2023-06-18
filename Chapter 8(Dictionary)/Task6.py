"""Practicing dictionary as a set of counters (Histogram)"""
"""
    1)From list to dictionary using => if-else
    2)From string to dictionary using => if-else
    3)From list to dictionary using => get() method
    4)From string to dictionary using => get() method
"""

print("=>(1)From list to dictionary using if-else")

words = ["apple", "mango", "banana", "pinapple", "mango", "banana", "banana", "apple", "kiwi", "banana", "kiwi", "mango" ,"strawberry"]
collection = dict()

for word in words:
    if word in collection:
        collection[word] = collection[word] + 1              #if key:value pair exist in the dictionary then add "1" to the current value
    else:
        collection[word] = 1                                 #if key doesnot exit in the dictionary the add "new key" and assign "1" to it

print(collection)                                            #prints histogram
print("----------------------------------------------------------")

print("=>(2)From string to dictionary using if-else")

characters = "afvvbkjsvbjkdfkjdfvnjsdvnsjvnad;;;;sjvnajdsvnasdlv"
collection2 = dict()

for char in characters:
    if char in collection2:
        collection2[char] = collection2[char] + 1           #if key = char exist, then add "1" to the value
    else:
        collection2[char] = 1                               #if key doesnot exist, then create new key and assign "1" to it

print(collection2)
print("----------------------------------------------------------")

print("=>(3)From list to dictionary using get() method")

words = ["apple", "mango", "banana", "pinapple", "mango", "banana", "banana", "apple", "kiwi", "banana", "kiwi", "mango" ,"strawberry"]
collection3 = dict()

for word in words:
    collection3[word] = collection3.get(word, 0) + 1

print(collection3)
print("----------------------------------------------------------")

print("=>(4)From string to dictionary using get() method")

characters = "afvvbkjsvbjkdfkjdfvnjsdvnsjvnad;;;;sjvnajdsvnasdlv"
collection4 = dict()

for char in characters:
    collection4[char] = collection4.get(char, 0) + 1        #get the current count/value of the name or "0" and then add "1" to it

print(collection4)
print("----------------------------------------------------------")
