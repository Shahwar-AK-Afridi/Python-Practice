"""Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case. Use the file words.txt to produce the output below."""

try:
    fname = input("Enter the File Name:")
    fhand = open(fname)
except:
    print("Incorrect File Name, Please Enter The File Name Again!")
    quit()

for line in fhand:
    line2 = line.upper().rstrip()
    print(line2)
    
fhand.close()
print("--------------------------------------------------------------")
print("All done")
