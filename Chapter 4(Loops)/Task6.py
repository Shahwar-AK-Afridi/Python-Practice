"""Find The Largest Number"""

#Writing program to get Maximum Value
largest_so_far = -1
print("Before %d" %largest_so_far)
for num in [9,41,12,3,74,15]:
    if num > largest_so_far:
        largest_so_far = num
    else:
        continue
print("Largest Number :%d" %largest_so_far)


#Using Max() Function to get Maximum Value
num = [9,41,12,3,74,15]
hello = max(num)
print(hello)
