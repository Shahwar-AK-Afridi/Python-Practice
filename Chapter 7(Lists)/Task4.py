"""Practicing List's Methods for sorting"""
"""1)Sorting list Alphanumerically or Ascending Order
   2)Sorting list in descending Order using sort() method with keyword (reverse=True)
   3)Sorting list based on lowercase & uppercase letters using sort() method (Case-sensitive Sort)
   4)Reversing the current sorting of list using reverse() method"""

#First
print("=>(1)Sorting list Alphanumerically or Ascending Order using sort() method")

print("--------PART A (sorting alphabets in ascending order)-----------")
thislist = ["z", "b", "m", "d", "y", "x", "q", "w", "a", "e", "s", "f", "g", "h", "j", "k", "l"]
print("Before Sorting:", thislist)
thislist.sort()                                                                 #sort() sorts list alphabetically
print("After Sorting:", thislist)

print("--------PART B (sorting numbers in ascending order)-----------")
numbers = [8,4,0,2,66,44,87,34,22,97,54,100,34,65,1,48,73]                      #numbers is a list of integers
print("Before Sorting:", numbers)
numbers.sort()
print("After Sorting:", numbers)
print("----------------------------------------------------------")

#Second
print("=>(2)Sorting list in descending Order using sort() method with keyword (reverse=True)")

print("--------PART A (sorting alphabets in deascending order)-----------")
thislist = ["a", "b", "m", "d", "y", "x", "q", "w", "z", "e", "s", "f", "g", "h", "j", "k", "l"]
print("Before Sorting:", thislist)
thislist.sort(reverse = True)
print("After Sorting:", thislist)

print("--------PART B (sorting numbers in deascending order)-----------")
numbers = [8,4,0,2,66,44,87,34,22,97,54,100,34,65,1,48,73]                      #numbers is a list of integers
print("Before Sorting:", numbers)
numbers.sort(reverse = True)
print("After Sorting:", numbers)
print("----------------------------------------------------------")

#Third
print("=>(3)Sorting list based on lowercase & uppercase letters using sort() method (Case-sensitive Sort)")
alphabets = ["z", "D","V","a","g","A","Z","l","k","h","d","r"]
print("Before Sorting:", alphabets)
alphabets.sort()                                                                #Upper-case letters are sorted before lower-case letters
print("After Sorting:", alphabets)

#fourth
print("=>(4)Reversing the current sorting of list using reverse() method")
alphabets = ["z", "b", "m", "d", "y", "x", "q", "w", "a", "e", "s", "f", "g", "h", "j", "k", "l"]
print("Before Sorting:", alphabets)
alphabets.reverse()
print("After Reversing Sort:", alphabets)
