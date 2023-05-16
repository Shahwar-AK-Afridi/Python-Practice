"""Using "Break" & "Continue" Statement"""
#Break statement exits the current loop and jumps to the statement immediately following the loop

while True:
    try:
        number = input("Enter The Number:")
        num = int(number)
    except:
        print("ERROR! ERROR! Enter A Numeric Input")
        continue
    if num > 10:
        print("Nice Work!")
        break
    elif num <= 10:
        print("Sorry")
    else:
        print("Enter The Correct Number")
print("Thank You")
