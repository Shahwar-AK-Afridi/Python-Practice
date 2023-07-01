"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
                      From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

fhand = open("mbox-short.txt", "r")
lst = list()
count = dict()
hours = list()

for line in fhand:
    line2 = line.strip()
    line2 = line2.split()
    if len(line2) < 3 or line2[0] != "From":
        continue
    time = line2[5].split(":")
    hours.append(time[0])

for hour in hours:
    count[hour] = count.get(hour, 0) + 1

for key, val in count.items():
    lst.append((key, val))

lst = sorted(lst)

for key, val in lst:
    print(key, val)
