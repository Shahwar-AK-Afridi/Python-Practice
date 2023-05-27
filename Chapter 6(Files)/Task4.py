"""Practicing File Handling By Writing Only"""
"""1)Using mode (x, w, a)
   2)Using write() method
   3)Using close() method"""

"""
#First(file1.txt)
print("Create A New file using mode(x)")
fhand = open("file1.txt", "x")                                                    #Creates a new file, returns an error if the file exist
fhand.write("I am practicing File Handling\n")                                    #Create file and write data for one time only and if you want to edit then use "w" mode
fhand.write("I am creating my first file\n")
fhand.write("If I want to overwrite or append this file then I have to use mode(w)\n")
fhand.close()
print("----------------------------------------------------------") """

#Second(file2.txt)
print("Create file2.txt using mode(w)")
fhand = open("file2.txt", "w")
fhand.write("I have created file using (w) mode\n")
fhand.write("Mode (w) will create a new file, if it doesnot exist\n")
fhand.write("If file exists, it will overwrite the existing content\n")
fhand.close()                                                                    #Makes sure that data is written on the disk
print("----------------------------------------------------------")

#Third(file1.txt)
print("Overwriting file1.txt using mode(w)")
fhand = open("file1.txt", "w")
fhand.write("I have overwritten the file1 using mode(w)\n")
fhand.write("I am a software Engineer\n")
fhand.close()
print("----------------------------------------------------------")

#Fourth(file2.txt)
print("Appending a line in file2.txt using mode(a)")
fhand = open("file2.txt", "a")                                                   #(a) with append to the end of the file
fhand.write("----------------------------------------\n")                        #(a) creates a new file, if it doesn't exist
fhand.write("I have appended this line in file2.txt\n")
fhand.write("Appends add content to the end of the file\n")
fhand.write("File object keeps track of where it is, so if you write again it adds the new data to the end")
fhand.close()
print("----------------------------------------------------------")

#Fifth(file3.txt)
print("Creating file3.txt to delete it later on")
fhand = open("file3.txt", "w")
fhand.write("I am creating this file to delete it later on\n")
fhand.write("Import os module first and use function os.remove()\n")
fhand.close()
