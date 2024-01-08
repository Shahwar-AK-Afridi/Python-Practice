"""Practicing List's Questions"""
"""
   1)Write a Python program to sum all the items in a list.
   2)Write a Python program to multiply all the items in a list.
   3)Write a Python program to get the largest number from a list
   4)Write a Python program to get the smallest number from a list
   5)Write a Python program to count the number of strings from a given list of strings, which have length 2 or more and the first and last characters are the same
   6)Write a Python program to remove duplicates from a list
   7)Write a Python program to check if a list is empty or not
   8)Write a Python program to clone or copy a list
   9)Write a Python program to find the list of words that have length longer than the length of the list.
  10)Write a Python function that takes two lists and returns True if they have at least one common member
  11)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
  12)Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
  13)Write a Python program to print the numbers of a specified list after removing even numbers from it.
  14)Write a Python program to shuffle and print a specified list.
  15)Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
  16)Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
  17)Write a Python program to generate all permutations of a list in Python.
  18)Write a Python program to calculate the difference between the two lists.Write a Python program to access the index of a list.
  19)Write a Python program to access the index & corresponding value of a list
  20)Write a Python program to convert a list of characters into a string.
  21)Write a Python program to find the index of an item in a specified list
  22)Write a Python program to flatten a shallow list.
  23)Write a Python program to append a list to the second list.
  24)Write a Python program to select an item randomly from a list
  25)Write a Python program to check whether two lists are circularly identical. (CHECK)
  26)Write a Python program to find the second smallest number in a list.
  27)Write a Python program to find the second largest number in a list.
  28)Write a Python program to get unique values from a list
  29)Write a Python program to get the frequency of elements in a list.
  30)Write a Python program to count the number of elements in a list within a specified range.
"""
import random

#1
print("=>(1)Write a Python program to sum all the items in a list")

number = [22,44,76,98,56,33,75,11,23]

def total_sum(number):
    total = 0
    for item in number:                   #This line starts a loop that will iterate over each element in the items list, one at a time.
        total = total + item              #total = running total
    return total

total = total_sum(number)
print("Total Sum:%d" %total)
print("----------------------------------------------------------")

#2
print("=>(2)Write a Python program to multiply all the items in a list.")

number2 = [1,2,3,4,5,6]

def product(numbers2):
    product = 1                                            #initializes product = 1. This will be used to keep track of the running total of the product of the numbers in the list.
    for item in number2:
        product = product * item                           #This line multiplies the current value of num by the product variable
    return product

product = product(number2)
print("Product:%f" %product)
print("----------------------------------------------------------")

#3
print("=>(3)Write a Python program to get the largest number from a list")

number = [22,44,76,98,56,33,75,11,23]

print("----------Approach 1 using for loop to read only----------")
def largest(number):
    try:
        largest_so_far = number[0]                      #We assume the list is not empty. This line initializes a variable called "largest_so_far" to the first element of the list.
    except:
        print("Empty List, Please Enter Again!")
        quit()
    for item in number:
        if item > largest_so_far:
            largest_so_far = item
        else:
            continue
    return largest_so_far

largest_so_far = largest(number)
print("Largest Item:%d" %largest_so_far)

print("-------------Approach 2 using max() function--------------")

largest_so_far = max(number)
print("Largest Item:", largest_so_far)

print("----------------------------------------------------------")

#4
print("=>(4)Write a Python program to get the smallest number from a list")

number = [22,44,76,98,56,33,-1,11,23]

print("----------Approach 1 using for loop to read only----------")

def smallest(number):
    try:
        smallest_so_far = number[0]                          #We assume the list is not empty. This line initializes a variable called 'smallest_so_far' to the first element of the list.
    except:
        print("Empty List, Please Enter Again!")
        quit()
    for item in number:
        if item < smallest_so_far:
            smallest_so_far = item
        else:
            continue
    return smallest_so_far                                   #This line returns the final value of the 'smallest_so_far' variable after the loop has finished

smallest_so_far = smallest(number)
print("Smallest Item:", smallest_so_far)

print("-------------Approach 2 using min() function--------------")

smallest_so_far = min(number)
print("Smallest Item:", smallest_so_far)
print("----------------------------------------------------------")

#5
print("(5)Write a Python program to count the number of strings from a given list of strings, which have length 2 or more and the first and last characters are the same")
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

sample = ['abc', 'xyz', 'aba', '1221']

def match_words(sample):
    count = 0
    for item in sample:
        count += 1
    print("Length of list:", count)
    lis = list()
    same = 0
    for word in sample:
        if count > 1 and word[0] == word[-1]:                  #This line checks if the length of the current word is greater than 1 and if the first letter of the word is the same as the last letter of the word.
            same += 1                                          #If these conditions are both true, it means the word has the same first and last letter.
            lis.append(word)
        else:
            continue
    print("Elements with same First & Last Character:", lis)
    return same

total = match_words(sample)
print("Total Elements:", total)
print("----------------------------------------------------------")

#6
print("(6)Write a Python program to remove duplicates from a list")

print("----------Approach 1 using for loop to read only----------")

sample = ["banana", "mango", "apple", "banana", "dragonfruit","orange", "peach", "avacado","apple", "orange", "watermelon", "banana", "peach","avacado"]
count = 0
count2 = 0
for word in sample:
    check = sample[count]
    print("Checker:", check)
    for words in sample:
        puss = sample[count2]
        #print(puss)
        if check == puss and count != count2:
            #print(sample[count2])
            del sample[count2]
        else:
            #print("Not same")
            count2 = count2 + 1
    count = count + 1
    count2 = 0
    print(sample)

print("-------------Approach 2 using (in) operator--------------")

sample = ["banana", "mango", "apple", "banana", "dragonfruit","orange", "peach", "avacado","apple", "orange", "watermelon", "banana", "peach","avacado"]

lis = list()
print("Original List:", sample)
print("Original Length:", len(sample))
for word in sample:
    if word in lis:
        continue
    else:
        lis.append(word)
print("Modified List:", lis)
print("Modified Length:", len(lis))
print("----------------------------------------------------------")

#7
print("(7)Write a Python program to check if a list is empty or not.")

empty = []
if len(empty) == 0:
    print("Empty List")
else:
    print("Full List")
print("----------------------------------------------------------")

#8
print("(8)Write a Python program to clone or copy a list")

print("----------Approach 1 using for loop to read only----------")

number = [22,44,76,98,56,33,-1,11,23]
clone = list()
print("Clone Before:", clone)
for item in number:
    clone.append(item)
print("Clone After:", clone)

print("---------------Approach 2 using copy()------------------")

sample = ['abc', 'xyz', 'aba', '1221']
clone2 = list()
print("Clone After:", clone2)
clone2 = sample.copy()
print("Clone After:", clone2)
print("----------------------------------------------------------")

#9
print("(9)Write a Python program to find the list of words that have length longer than the length of the list.")

sentence = "The quick brown fox jumps over the lazy dog"

def word_length(n, sentence):
    abc = sentence.split()
    item = []                                                           # Initialize an empty list called 'item'.
    for word in abc:
        if len(word) > n:
            item.append(word)
        else:
            continue
    return item                                                         #This line returns the "item" list, which contains all the words in the input string that have a length greater than n.

no_of_words = word_length(3, sentence)
print("Word With Length > n:", no_of_words)
print("----------------------------------------------------------")

#10
print("(10)Write a Python function that takes two lists and returns True if they have at least one common member")

list1 = [2,4,6,3,7,3,6,8,4,3,78]
list2 = [5,2,5,7,8,95,544,6,8,8]
list3 = []

def item_comparison(list1, list2):
    result = False                                                       #he function initializes a Boolean variable "result" to False.
    for item in range(len(list1)):
        for element in range(len(list2)):
            if list1[item] == list2[element]:
                result = True
                 #returns "None" if no element is comman
                return result                                           #If the current element in list1 is equal to the current element in list2, the function sets result to True and immediately returns the result using the return statement.
            else:                                                       #This means that the function will stop execution as soon as it finds a common element between the two lists.
                continue

bool = item_comparison(list1, list2)
print(bool)
bool2 = item_comparison(list1, list3)
print(bool2)
print("----------------------------------------------------------")

#11(Check)
print("=>(11)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.")

sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
print("List Before:", sample)
new = list()
for item in range(len(sample)):
    if item == 0:
        continue
    elif item == 4:
        continue
    elif item == 5:
        continue
    else:
        word = sample[item]
        new.append(word)
print("List After:", new)
print("----------------------------------------------------------")

#12
print("=>(12)Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.")

sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]")

new = list()
for key, val in sample:                                                #creating "new" list with value:key pairs
    new.append((val,key))

sample.clear()                                                         #clearing the elements of "sample" list

print("Before Sorting:", new)
new = sorted(new)                                                      #sorting based on "value"

for val, key in new:
    sample.append((key,val))                                           #appending the sorted list of tuples to the "sample"

print("After Sorting:", sample)
print("----------------------------------------------------------")

#13
print("=>(13)Write a Python program to print the numbers of a specified list after removing even numbers from it.")

num = [7,8,120,25,44,20,27]
new = list()

for item in num:
    if item % 2 == 0:                                                   #If an element is odd (i.e., its remainder when divided by 2 is not equal to zero), it is included in the new list.
        continue
    else:
        new.append(item)
print(new)
print("----------------------------------------------------------")

#14
print("=>(14)Write a Python program to shuffle and print a specified list.")

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
random.shuffle(color)                                                   #The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
print(color)
print("----------------------------------------------------------")

#15
print("=>(15)Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).")

i = 1
squared_num = list()
new = list()

while i <= 30:
    square = i * i
    squared_num.append(square)
    i = i + 1

print("List Of Squared Number:", squared_num)

for item in squared_num:
    if item in squared_num[0:5] or item in squared_num[-5:]:
        new.append(item)

print("Final List with 5 Elements:", new)
print("----------------------------------------------------------")

#16
print("=>(16)Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.")

"""
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False
"""

lst = [1, 5, 3]
flag = True

for item in lst:
    if item == 1:
        flag = False
    elif item > 1:
        for divisor in range(2, item):
            if item % divisor == 0:
                flag = False
                break
            else:
                continue
    else:
        continue

if flag == True:
    print("All Numbers are prime Numbers")
elif flag == False:
    print("This list holds composite numbers")

print("----------------------------------------------------------")

#17
print("=>(17)Write a Python program to generate all permutations of a list in Python.")





print("----------------------------------------------------------")

#18
print("=>(18)Write a Python program to calculate the difference between the two lists.")

lst1 = [0, 3, 4, 7, 9]
lst2 = [3, 5, 7, 13, 15]


print("----------------------------------------------------------")

#19
print("=>(19)Write a Python program to access the index & corresponding value of a list")

lst = ["apple", "mango", "banana", "dragonfruit", "kiwi"]

for item in range(len(lst)):
    print("Index: %d value: %s" %(item, lst[item]))

print("----------------------------------------------------------")

#20
print("=>(20)Write a Python program to convert a list of characters into a string.")

lst_of_characters = ["m","y"," ","a","p","p","l","e"]
print("List of characters:", lst_of_characters)

delimiter = ""
fruit = delimiter.join(lst_of_characters)
print("String:", fruit)

print("----------------------------------------------------------")

#21
print("=>(21)Write a Python program to find the index of an item in a specified list")

lst = ["apple", "mango", "banana", "dragonfruit", "kiwi"]

ind = lst.index("banana")
print("Index of Banana:", ind)

print("----------------------------------------------------------")

#22
print("=>(22)Write a Python program to flatten a shallow list.")

print("----------Part A (Regular List of Lists)----------")

original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
flat_list = list()

for lst in original_list:
    for item in lst:
        flat_list.append(item)

print("Flat List:", flat_list)

print("----------Part A (Irregular List of Lists)----------")  #this code can be used for both regular and irregular shallow lists

original_list = [[2,4,3],[5,6], 9, [7]]
flat_list = list()

for lst in original_list:                  #type(lst) is list == isinstance(lst, list)
    if isinstance(lst, list):              # code to check whether object is a list or not
        for item in lst:
            flat_list.append(item)
    else:
        flat_list.append(lst)

print(flat_list)
print("----------------------------------------------------------")

#23
print("=>(23)Write a Python program to append a list to the second list.")

print("-------------Approach 1 using extend() method--------------")

fruit = ["apple", "mango", "dragonfruit"]
vegetable = ["tomoto", "onion", "potato"]

fruit.extend(vegetable)
print(fruit)

print("-------------Approach 2 using (+) operator----------------")

fruit = ["apple", "mango", "dragonfruit"]
vegetable = ["tomoto", "onion", "potato"]

final = fruit + vegetable
print(final)
print("----------------------------------------------------------")

#24
print("=>(24)Write a Python program to select an item randomly from a list")

num = [4,53,5,5,4,4,43,23,367,45,56,3,3,363,633,36]

random_num = random.choice(num)
print("Random Number:", random_num)
print("----------------------------------------------------------")

#25
print("=>(25)Write a Python program to check whether two lists are circularly identical.")


print("----------------------------------------------------------")

#26
print("=>(26)Write a Python program to find the second smallest number in a list.")



print("----------------------------------------------------------")

#27
print("=>(27)Write a Python program to find the second largest number in a list.")


print("----------------------------------------------------------")

#28
print("=>(28)Write a Python program to get unique values from a list")

my_list = [10, 20, 30, 40, 20, 50, 60, 40, 20, 50, 30]

def unique_item(lst:list)-> list:
    lst2 = []
    for item in lst:
        if item not in lst2:
            lst2.append(item)
    return lst2

print(unique_item(my_list))

print("----------------------------------------------------------")

#29
print("=>(29)Write a Python program to get the frequency of elements in a list.")

my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

frequency = {}

for item in my_list:
    if item not in frequency:
        frequency[item] = 0 
    frequency[item] += 1

print(frequency)

print("----------------------------------------------------------")

#30
print("=>(30)Write a Python program to count the number of elements in a list within a specified range.")

list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]

r1 = 20
r2 = 80

def count_in_range(lst: list, min: int, max: int)-> int:
    count_so_far = 0
    for item in list1:
        if item >= 20 and item <= 80:
            count_so_far += 1
    return count_so_far

print(count_in_range(list1, r1, r2))

print("----------------------------------------------------------")
