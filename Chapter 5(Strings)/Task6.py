"""Practise String Questions"""
"""
    1)Write a Python program to calculate the length of a string
    2)Write a Python program to count the number of characters (character frequency) in a string.
    3)Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
    4)Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
    5)Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
    6)Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
    7)Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
    8)Write a Python function that takes a list of words and return the longest word and the length of the longest one.
"""
#1
print("=>(1)Write a Python program to calculate the length of a string")

profession = "Software Engineer"
count = 0
for char in profession:
    count  = count + 1

print("Length Of String:", count)
print("Length From built-in Functions:", len(profession))

print("----------------------------------------------------------")

#2
print("=>(2)Write a Python program to count the number of characters (character frequency) in a string.")

sample = "google.com"
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

collection = dict()
for char in sample:
    if char in collection:
        collection[char] = collection[char] + 1
    else:
        collection[char] = 1

print("collection:", collection)

print("----------------------------------------------------------")

#3
print("=>(3)Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.")

"""
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""
string1 = "w3resource"

if len(string1) < 2:
    result = "Empty String"
else:
    result = string1[:2] + string1[-2:]

print("Result:",result)

print("----------------------------------------------------------")

#4
print("=>(4)Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.")

sample = 'restart thr computer'
#Expected Result : 'resta$t'

first_char = sample[0]

sample = sample.replace(first_char,"$")

sample = first_char + sample[1:]
print(sample)

print("----------------------------------------------------------")

#5
print("=>(5)Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string")

sample1 = 'software'
sample2 = 'computer'
#Expected Result : 'xyc abz'

new_sample1 = sample1[:2] + sample2[2:]
new_sample2 = sample2[:2] + sample1[2:]
combine = new_sample2 +" "+ new_sample1
print(combine)

print("----------------------------------------------------------")

#6
print("=>(6)Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged")
"""
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly
"""

words = ["apple","string","playing","mango","pi","pop","abc","pk","eat"]

def string_modifier(phrases: list)-> list:
    lst = []
    for item in phrases:
        if len(item) >= 3 and item[-3:] == "ing":
            item = item + "ly"
            lst.append(item)
        elif len(item) >= 3:
            item = item + "ing"
            lst.append(item)
        else:
            lst.append(item)
    return lst

print(string_modifier(words))

print("----------------------------------------------------------")

#7
print("Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.")

"""
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'
"""
phrase = "The lyrics is not that poor! you are not a good listener"

def not_poor_remover(string: str)-> str:
   
    pos_not = string.find("not")
    pos_poor = string.find("poor")

    if pos_poor > pos_not:
        new = string.replace(string[pos_not:pos_poor + 4], "good")
    return new

print(not_poor_remover(phrase))

print("----------------------------------------------------------")

#8
print("Write a Python function that takes a list of words and return the longest word and the length of the longest one.")

#Sample Output:
#Longest word: Exercises
#Length of the longest word: 9"

def longest_string(lst:list)->str:
    flag = lst[0]
    for item in lst:
        if len(item) > len(flag):
            flag = item
    return (flag, len(flag))   




lst = ["PHP", "Exercises", "Backend","Front-end "]

result = longest_string(lst)
print("{} is longest word with length {}".format(result[0],result[1]))
print("----------------------------------------------------------")
