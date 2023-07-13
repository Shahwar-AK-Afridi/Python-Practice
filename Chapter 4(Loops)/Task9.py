""""Search an item Using Boolean Variable"""

number = [9,41,12,3,74,15,98,44,57,32,16]
for obj in number:
    found = False        #Boolean Variable
    if obj == 3:
        found = True
        print("Number is %d so Found: %s" %(obj, found))
    else:
        print("Number is %d so %s" %(obj, found))
