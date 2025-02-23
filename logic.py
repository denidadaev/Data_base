import sqlite3 
con = sqlite3.connect("tutorial.db") # соединение с базой данных, если бд нет, то файл создастся

cur = con.cursor()
data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]

cur.execute("CREATE TABLE movie(?, ?, ?)", data)

cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)

cur.execute("SELECT score, title FROM movie ORDER BY score")

cur.execute("UPDATE movie SET score=10 WHERE title="Monty Python and the Holy Grail"")

cur.execute(" DELETE FROM movie WHERE score < 8")

cur.execute("DROP TABLE movies")
con.commit()
con.close()

