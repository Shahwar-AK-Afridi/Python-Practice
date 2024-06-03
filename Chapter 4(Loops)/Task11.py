"""Practicing Conditional Statements and Loop Questions"""
"""
   1)Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)
   2)Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
   3)Write a Python program to guess a number between 1 and 9
   4)Write a Python program to construct the following pattern, using a nested for loop
   5)Write a Python program that accepts a word from the user and reverses it
   6)Write a Python program to count the number of even and odd numbers in a series of numbers
   7)Write a Python program that prints each item and its corresponding type from the following list
   8)Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
   9)Write a Python program to get the Fibonacci series between 0 and 50
  10)Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz"
  11)Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
  12)Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
  13)Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
  14)Write a Python program to check the validity of passwords input by users. 
  15)Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence
  """

import random
import string

#1
print("(1)Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)")

def divisor(start: int, end: int)->list:
    new = []
    for num in range(start,end):
        if num % 7 == 0 and num % 5 == 0:
            new.append(num)
    return new

print(divisor(1500,2701))

print("----------------------------------------------------------")

#2
print("(2)Write a Python program to convert temperatures to and from Celsius and Fahrenheit.")
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
"""
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""
def cel_to_fh(temp: float, celsius = True)->int:
    if celsius == True:
        c = round((5 * (temp - 32))/9)
        return c
    elif celsius == False:
        f = round((temp * 9)/5 +32)
        return f

print(cel_to_fh(60, False))
print(cel_to_fh(45))
print("----------------------------------------------------------")

#3
print("(3)Write a Python program to guess a number between 1 and 9")
""" Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
on successful guess, user will get a "Well guessed!" message, and the program will exit"""

def guess_game(num: int)->int:
    dice = random.randint(1,9)
    if dice == num:
        return "Well Guessed"
    else:
        return "You Lost"

num = 8
result = guess_game(num)
print(result)

print("----------------------------------------------------------")

#4
print("(4)Write a Python program to construct the following pattern, using a nested for loop")



print("----------------------------------------------------------")


#5
print("(5)Write a Python program that accepts a word from the user and reverses it")

#option 1

def reverse(word: str)->str:
    rev_string = word[::-1]
    return rev_string

print("Word Before Hello World")
print("Word After", reverse("welcome"))

#option 2

word = "Hello"
for char in range(len(word) - 1, -1, -1):
    # Print each character from the word in reverse order without a new line (end="")
    print(word[char], end="")

print("----------------------------------------------------------")

#6
print("(6)Write a Python program to count the number of even and odd numbers in a series of numbers")

def even_odd(lst:list)->tuple:
    even_so_far = 0
    odd_so_far = 0
    for item in lst:
        if item % 2 == 0:
            even_so_far += 1
        else:
            odd_so_far += 1
    return (even_so_far,odd_so_far)

result = even_odd((1,2,3,4,5,6,7,8,9))
print("Even Numbers:", result[0])
print("Odd Numbers", result[1])

print("----------------------------------------------------------")

#7
print("(7)Write a Python program that prints each item and its corresponding type from the following list")

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print("Type of {} is {}".format(item, type(item)))

print("----------------------------------------------------------")

#8
print("(8)Write a Python program that prints all the numbers from 0 to 6 except 3 and 6")

for num in range(0,7,1):
    if num != 3 and num != 6:
        print(num, end = "")

print("----------------------------------------------------------")

#9
print("(9)Write a Python program to get the Fibonacci series between 0 and 50")

def Fibonacci(num:int)->list:
    list_nums = [0, 1]
    x = None
    while True:
        x = list_nums[-1] + list_nums[-2]
        list_nums.append(x)
        if list_nums[-1] >= num:
            break
    return list_nums

print(Fibonacci(100))

print("----------------------------------------------------------")

#10
print("(10)Write a Python program that iterates the integers from 1 to 50. For multiples of three print ""Fizz"" instead of the number and for multiples of five print ""Buzz"". For numbers that are multiples of three and five, print ""FizzBuzz""")

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
print("----------------------------------------------------------")

#11
print("(11)Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.")

"""
Note :
i = 0,1.., m-1
j = 0,1, n-1.
"""

def matrix_generator(rows, columns):
    outer_array = []

    for x in range(rows):
        inner_array = []
        for y in range(columns):
            inner_array.append(x*y)
        outer_array.append(inner_array)
    return outer_array

print(matrix_generator(3,5))

print("----------------------------------------------------------")

#12
print("(12)Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).")

"""words = []

while True:
    word = input("Enter The Word: ")
    if word != "":
        words.append(word.lower())
    else:
        break

print(words)"""

print("----------------------------------------------------------")

#13
print("(13)Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence")

def character_checker(string):
    
    letter, number, others = (0,0,0)

    for char in string:
        if char.isalpha():
            letter += 1
        elif char.isdigit():
            number += 1
        else:
            others += 1
    representation = "Total Letters = {}, and Total Numbers = {}, Total Others = {}".format(letter,number,others)
    return representation

print(character_checker("Hello World 210"))
print("----------------------------------------------------------")

#14
print("Write a Python program to check the validity of passwords input by users.")

"""Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters."""

password = "helloPYthon1234*&^"

if len(password) >=6 and len(password) <= 16:
    for char in password:
        if char in list(string.ascii_lowercase):
            pass

print("----------------------------------------------------------")


#15
print("Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence")

def even_checker():
    num = 0
    even_lst = []
    for num in range(100,401):
        num_str = str(num)
        if num % 2 == 0:
            even_lst.append(num_str)
    result = ",".join(even_lst)
    return result

print(even_checker())

print("----------------------------------------------------------")
