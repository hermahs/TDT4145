import sqlite3
import console
con = sqlite3.connect("database.db")

cursor = con.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')
console.main(cursor)


