""""Summing in Loop"""
total = 0                           #Iteration variable = "Thing"
print("Sum Before:%d" %total)
for sum in [9,41,12,3,74,15]:
    #Running Total = "total"
    total = total + sum        #Inside Loop = we add actual number to the running total during each Iteration
    # total aka accumulator
    print(total)
print("Final Total :%d" %total)   #This total is called as "Overall total of the values"
