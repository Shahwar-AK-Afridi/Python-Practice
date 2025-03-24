import sqlite3

with sqlite3.connect('tracks.sqlite') as conn:

    cur = conn.cursor()

    cur.executescript('''
        DROP TABLE IF EXISTS Artist;
        DROP TABLE IF EXISTS Album;
        DROP TABLE IF EXISTS Genre;
        DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
    ''')
fname = "A:\\Coursera\\Python\\py4e\\Python-Practice\\Chapter 13 (Databases)\\Counting Tracks from csv file\\tracks.csv"
with open(fname,"r") as fhand:
    for line in fhand:
        line = line.strip()
        pieces = line.split(",")
        
        name = pieces[0]
        artist = pieces[1]
        album = pieces[2]
        count = pieces[3]
        rating = pieces[4]
        length = pieces[5]
        genre = pieces[6]

        cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)",(artist,))

        cur.execute("SELECT id from Artist where name = ?",(artist,))

        artist_id = cur.fetchone()[0]

        cur.execute("INSERT or IGNORE INTO Album(title,artist_id) VALUES(?,?)",(album,artist_id))

        cur.execute("SELECT id from Album where title = ?", (album,))

        album_id = cur.fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO Genre(name) VALUES(?)",(genre,))

        cur.execute("SELECT id from Genre where name = ?",(genre,))

        genre_id = cur.fetchone()[0]

        cur.execute("INSERT OR REPLACE INTO Track(title, album_id, genre_id, len, rating, count) VALUES(?,?,?,?,?,?)",(name, album_id,genre_id,length,rating,count))

        conn.commit()



#Query to test the code
'''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name;'''

#Result
'''
Track	Artist	Album	Genre
Chase the Ace	AC/DC	Who Made Who	Rock
D.T.	AC/DC	Who Made Who	Rock
For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock'''