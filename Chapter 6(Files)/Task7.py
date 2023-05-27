"""Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:0.8475

Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution."""

print("---------------------------Approach 1------------------------------------------")
try:
    fname = input("Enter file name Again: ")
    fhand = open(fname,"r")
except:
    print("Enter Correct File Name")
    quit()                                          #quit() same as exit()

count = 0
total = 0
for line in fhand:
    line2 = line.rstrip()                           #Removes the right-most non-printing characters "\n"
    if line2.find("X-DSPAM-Confidence") == -1:
        continue
    else:
        print(line2)
        count += 1
        extract_string = line2[19:]
        extract_float = float(extract_string)
        total = total + extract_float               #Running Total
        print(extract_string)

print("Total Number of Lines: %d" %count)
print("Sum of All Numbers: %g" %total)
print("-----Calculating Average-----")
avg = total/count
print("Average spam confidence:", avg)
fhand.close()


print("---------------------------Approach 2--------------------------------------")
try:
    fname = input("Enter file name Again: ")
    fh = open(fname,"r")
except:
    print("Enter Correct File Name")
    exit()                                          #exit() same as quit()

count = 0
total = 0
for line in fh:
    line2 = line.rstrip()
    if not line2.startswith("X-DSPAM-Confidence:"):  #"not" reverses the result
        continue
    else:
        print(line2)
        count += 1
        extract_string = line2[19:]
        extract_float = float(extract_string)
        total = total + extract_float

print("Total Number of Lines: %d" %count)
print("Sum of All Numbers: %g" %total)
print("-----Calculating Average-----")
avg = total/count
print("Average spam confidence:", avg)
fhand.close()
