"""Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
 The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
  The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""


print("--------------------Approach 1 using (if-else)------------------")
try:
    name = input("Enter file:")
    fhand = open(name)
except:
    print("Incorrect File Name!")
    quit()

count = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        words = words[1:2]
        #print(words)
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] = count[word] + 1
    else:
        continue
#print(count)                                                    #prints the histogram

bigcount = None
bigword = None
for key,value in count.items():
    if bigcount == None or value > bigcount:
        bigcount = value
        bigword = key
    else:
        continue

print("----------------------------------------------------------")
print("Most Mails Are Send By %s, sends %d times" %(bigword, bigcount))
print("----------------------------------------------------------")


print("----------------------Approach 2 using get() method--------------------------")

try:
    fname = input("Enter file:")
    fhand = open(fname)
except:
    print("Incorrect File Name!")
    quit()

count = dict()

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        words = words[1:2]
        for key in words:
            count[key] = count.get(key,0) + 1
    else:
        continue
#print(count)                                                   #prints the histogram

bigcount = None
bigword = None

lst = list()
lst = count.items()
for key, val in count.items():                                   #val > bigcount will give error bcz we cannot compare an integer with "NONE" so we used "bigcount == None" as erroe handler
    if bigcount == None or val > bigcount:                       #short-circuiting is applied here, for the first time "bigcount == none" will be correct so "val>bigcount" will not be checked
        bigcount = val                                           #once we assign an integer to the bigcount, then we can use the "val>bigcount" condition
        bigword  = key
    else:
        continue

print("----------------------------------------------------------")
print("Most Mails Are Send By %s, sends %d times" %(bigword, bigcount))
print("----------------------------------------------------------")
