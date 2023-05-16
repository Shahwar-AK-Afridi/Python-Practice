"""Write a Python program to calculate the length of a string."""


text ="X-DSPAM-Confidence:0.8475s"

#Using for loop and function
def string_length(text):
    count = 0
    for len in text:
        count = count + 1
    return count

num = string_length(text)
print(num)

#Using built-in function len()
length = len(text)
print("The length of string is %d" %length)
