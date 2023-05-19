"""Practising Strings"""

#First
print("Using index operator to display the character of a string")
fruit = "Banana"
letter = fruit[1]                      #"[]" = index operator
print(letter)
print("----------------------------------------------------------")


#Second
print("Using expression inside index operator and then assigning the character")
x = 5
letter = fruit[x-1]
print(letter)
print("----------------------------------------------------------")

#Third
print("Getting charaters of string using negative indices")
season = "summers"
letter = season[-1]
letter2 = season[-7]
print("Last character using index -1:", letter)
print("First charater using index -7:", letter2)
print("----------------------------------------------------------")

#Fourth (Indefinte Loop)
print("Using while loop to traverse through a string")
fruit = "Banana"
index = 0
while index < len(fruit):            #When index == len(fruit) the condition becomes FALSE
    letter = fruit[index]
    print("Letter:", letter)         #This loop traverses the string and displayes each letter on a line by itself
    index = index + 1
print("----------------------------------------------------------")

#Fifth (Definite Loop)
print("Using For Loop to traverse through a string")
fruit = "Apple"                     #Better than while loop to traverse the string
for char in fruit:
    print("Character:", char)
print("----------------------------------------------------------")

#Sixth
print("Count the number of times the letter (a) appear in a string")
fruit="banana"
count = 0
for char in fruit:
    if char == "a":
        count = count + 1
    else:
        continue
print("The character a appeared: %d" %count + " times")
