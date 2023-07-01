"""
Sort the list of words from longest to shortest based on length
"""
new_lst = list()
final_list = list()

text = "but soft what light in yonder window breaks"

words = text.split()
print("List Of Words:", words)

for word in words:
    new_lst.append((len(word), word))

print("List Of Tuples:", new_lst)

#new_lst.sort(reverse = True)
arrange = sorted(new_lst, reverse = True)       #Both Ways can be used "sorted()" & "sort"
print("Sorted List Of Tuples:", arrange)

for length, word in arrange:                    #Coverting from "List of Tuples" to "List for words from longest to shortest"
    final_list.append(word)

print("List from Longest To Shortest:", final_list)
