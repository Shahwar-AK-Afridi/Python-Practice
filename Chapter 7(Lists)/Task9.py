"""Practicing List's Questions"""
"""1)Write a Python program to sum all the items in a list.
   2)Write a Python program to multiply all the items in a list.
   3)Write a Python program to get the largest number from a list
   4)Write a Python program to get the smallest number from a list
   5)Write a Python program to count the number of strings from a given list of strings, which have length 2 or more and the first and last characters are the same
   6)Write a Python program to remove duplicates from a list"""


#First
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

#Second
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

#Third
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

#fourth
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

#Fifth
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

#Sixth
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

print("(7)Write a Python program to check if a list is empty or not.")

empty = []
if len(empty) == 0:
    print("Empty List")
else:
    print("Full List")
print("----------------------------------------------------------")

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

print("(11)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.")

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
