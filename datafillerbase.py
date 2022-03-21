import json
import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

data = ""

def createDataBase():
    with open("data.json", "r") as f:
        data = json.load(f)

    for key in data.keys():
        for d in data[key]:
            e = [d[a] for a in d.keys()]
            print(f"INSERT INTO {key} VALUES {*e,};")
            #cursor.execute(f"INSERT INTO {key} VALUES ({[]})" 
    return

createDataBase()
