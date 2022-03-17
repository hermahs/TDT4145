import sqlite3
con = sqlite3.connect("database.db")

cursor = con.cursor()
cursor.execute('''INSERT INTO Bruker VALUES ('ola@nordmann.no', 'Ola', 'Nordmann', 'passord')''')
con.commit()
cursor.execute("SELECT * FROM Bruker")
rows = cursor.fetchall()
print("All rows in the table Bruker:")
print(rows)


con.close()


