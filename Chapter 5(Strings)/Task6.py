"""Practise String Questions"""
"""
    1)Write a Python program to calculate the length of a string
    2)Write a Python program to count the number of characters (character frequency) in a string.
    3)Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
    4)Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
    5)Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
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
