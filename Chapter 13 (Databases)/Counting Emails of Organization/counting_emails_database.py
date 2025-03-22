import sqlite3

conn = sqlite3.connect('emailcount.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

#fname = input('Enter file name:')
fname = "A:\Coursera\Python\py4e\Python-Practice\Chapter 13 (Databases)\Counting Emails of Organization\mbox.txt"

if len(fname) < 1:
    fname = 'mbox-short.txt'

with open(fname,"r",encoding='cp1252') as fhand:
    lst_email = []
    dic = {}
    for line in fhand:
        if line.startswith("From"):
            data = line.split(" ")
            email = data[1]
            data2 = email.split("@")
            org = data2[-1]
            cur.execute('SELECT count from Counts where org = ?',(org,))
            row = cur.fetchone()
            #print(row)
            if row is None:
                cur.execute('INSERT INTO Counts(org, count) VALUES (?, 1)',(org,))
            else:
                cur.execute('UPDATE COUNTS SET count = count + 1 where org = ?',(org,))
    conn.commit()


sqlstr = 'SELECT org, count from Counts ORDER BY count DESC'
for row in cur.execute(sqlstr):
        print(row)

cur.close()
            




