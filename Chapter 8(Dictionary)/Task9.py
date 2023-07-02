"""Practicing Dictionaries's Questions"""
"""
    1)Write a Python script to sort (ascending and descending) a dictionary by value
    2)Write a Python script to add a key to a dictionary
    3)Write a Python script to concatenate the following dictionaries to create a new one.
    4)Write a Python script to check whether a given key already exists in a dictionary
    5)Write a Python program to iterate over dictionaries using for loops.


"""
#1
print("=>(1)Write a Python script to sort (ascending and descending) a dictionary by value")

thisdict = {"apple": 2, "mango": 4, "banana": 3, "pinapple": 1, "dragonfruit": 0}

print("----------------Approach 1-----------------------")

lst = list()
for key, val in thisdict.items():
    lst.append((val,key))

print("List Before Sorting:", lst)

lst_ascending = sorted(lst)
print("List In Ascending Order:", lst_ascending)
dict_ascending = dict(lst_ascending)
print("Dictionary In Ascending Order", dict_ascending)

lst_descending = sorted(lst, reverse = True)
print("List in Descending Order:", lst_descending)
dict_descending = dict(lst_descending)
print("Dictionary In Descending Order:", dict_descending)

print("----------------Approach 2-----------------------")

def sort_dict_by_values(thisdict, op):

    lst = list()

    for key, val in thisdict.items():
        lst.append((val,key))

    if op == True:
        lst_ascending = sorted(lst)
        dict_ascending = dict(lst_ascending)
        return dict_ascending
    elif op == False:
        lst_descending = sorted(lst, reverse = True)
        dict_descending = dict(lst_descending)
        return dict_descending
    else:
        return

dict_ascending = sort_dict_by_values(thisdict, True)
print("Dictionary In Ascending Order", dict_ascending)

dict_descending = sort_dict_by_values(thisdict, False)
print("Dictionary In Descending Order", dict_descending)
print("----------------------------------------------------------")

#2
print("=>(2)Write a Python script to add a key to a dictionary")

sample = {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

print("Before Adding Item:", sample)
sample.update({2:30})
print("After Adding Item:", sample)
print("----------------------------------------------------------")

#3
print("=>(3)Write a Python script to concatenate the following dictionaries to create a new one.")

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}

#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic4 = dict()
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print("Final Dictionary:", dic4)
print("----------------------------------------------------------")

#4
print("=>(4)Write a Python script to check whether a given key already exists in a dictionary")
"""
thisdict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = input("Enter The Name of the Fruit:")
num = int(key)

def is_key_present(thisdict,key):
    new_dict = thisdict
    if key in new_dict:
        return "Yes, Key exists"
    else:
        return "No, key doesnot exists"

ans = is_key_present(thisdict,num)
print(ans)"""
print("----------------------------------------------------------")

#5
print("=>(5)Write a Python program to iterate over dictionaries using for loops.")

thisdict = {"apple": 10, "mango": 20, "banana": 30, "dragonfruit": 40, "peach": 50, "kiwi": 60}

for key,val in thisdict.items():
    print("%s : %d" %(key, val))
