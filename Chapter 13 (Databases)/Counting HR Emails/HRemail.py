import sqlite3

conn = sqlite3.connect("HRemail.sqlite")

curr = conn.cursor()

curr.execute("DROP TABLE IF EXISTS Email")

curr.execute("CREATE TABLE Email (Emails TEXT, Count INTEGER)")

file = "A:\Coursera\Python\py4e\Python-Practice\Chapter 13 (Databases)\HREmail.txt"
with open(file,"r") as fhand:
    for line in fhand:
        curr.execute("INSERT INTO Email(Emails, Count) VALUES (?,2)",(line,))

    #conn.commit()

curr.execute("SELECT * FROM Email")

for row in curr:
    print(row)

