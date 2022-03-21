import sqlite3
import console
import sql
con = sqlite3.connect("database.db")

cursor = con.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')
sql.init(cursor, con)
console.main()


