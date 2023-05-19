""""Practicing String Slicing"""

#First
print("Operator returns the slice of string from nth character to mth character")
first = "Monty Python"
print(first[0:4])                       #Upto but not including character at 4th index
print(first[6:7])                       #Character at 7th index is not included
print(first[6:20])                      #Here the value of 2nd index is more than the length of String
print("----------------------------------------------------------")

#Second
print("Omiting the first index")
second = "Hello world"
print(second[:7])                       #If we leave off the first number, it is assumed to be the "beginning" fo the string
print("----------------------------------------------------------")

#Third
print("Omiting the second index")
third = "Mango Apple"
print(third[2:])                        #If we leave off the second index, it is assumed to be the "End" of the string
print("----------------------------------------------------------")

#Fourth
print("Omiting Both the index")
fourth = "hello to the world"
print(fourth[:])                        #If we leave off both the index, it means it is going to print the "whole" string
print("----------------------------------------------------------")

#Fifth
print("First Index == Second Index")
fifth = "Strawberry"                    #The result is an "empty" string, however it is same as any other string
print(fifth[3:3])                       #Length of empty string = 0
print("----------------------------------------------------------")
