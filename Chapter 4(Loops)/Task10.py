""""Search an item Using Boolean Variable"""

found = False
number = [9,41,12,3,74,15]
for obj in number:
    if obj == 3:
        found = True
        print("%f is Found: %s" %(obj, found))
    else:
        continue
