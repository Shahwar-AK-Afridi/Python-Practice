import json
import sqlite3

with sqlite3.Connection('roster.sqlite') as conn:
    
    cur = conn.cursor()

    cur.executescript('''
            DROP TABLE IF EXISTS User;
            DROP TABLE IF EXISTS Course;
            DROP TABLE IF EXISTS Member;
                      
            CREATE TABLE User(
                id     INTEGER PRIMARY Key,     
                name   TEXT UNIQUE      
                );
                      
            CREATE TABLE Course(
                id     INTEGER PRIMARY KEY,      
                title  TEXT UNIQUE      
                );          
                      
             CREATE TABLE Member(
                user_id     INTEGER,
                course_id   INTEGER,
                role        INTEGER,
                PRIMARY KEY (user_id, course_id)      
                      )         
                      ''')


#fname = input("Enter File Name: ")
#if len(fname) < 1:
    
fname = "A:\\Coursera\\Python\\py4e\\Python-Practice\\Chapter 13 (Databases)\\Roster Example (Many-to-Many)\\roster_data.json"

with open(fname,'r') as fhand:
    str_data = fhand.read()
    #print(str_data)
    json_data = json.loads(str_data)
    #print(json_data)
    #print(type(json_data))

    for lst in json_data:
        #print(lst)

        name = lst[0]
        title = lst[1]
        role = lst[2]

        cur.execute("INSERT OR IGNORE INTO User(name) VALUES(?)",(name,))
        cur.execute("SELECT id from User where name = ?",(name,))
        user_id = cur.fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO Course(title) VALUES(?)",(title,))
        cur.execute("SELECT id from Course where title = ?",(title,))
        course_id = cur.fetchone()[0]

        cur.execute("INSERT OR REPLACE INTO MEMBER (user_id, course_id, role) VALUES (?,?,?)",(user_id,course_id, role))

        conn.commit()

#Query to test the code
'''SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;'''

#Result
'''
Zena|si106|0
Zaineddine|si110|0
'''
