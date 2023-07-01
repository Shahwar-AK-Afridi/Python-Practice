"""Find top 10 most common words in the file sample.txt"""

fhand = open("sample.txt", "r")

count = dict()
lst = list()

for line in fhand:
    lst_of_words = line.split()
    for word in lst_of_words:
        count[word] = count.get(word, 0) + 1

for key, val in count.items():
    lst.append((val, key))              #here we will get a list of tuple in "value:key" order

lst = sorted(lst, reverse = True)       #here we will get list sorted in descending order

for val, key in lst[:10]:               #returns a list of tuples with only 10 tuples
    print(key, val)
