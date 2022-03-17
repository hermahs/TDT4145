import sqlite3
connection = None
cursor = None

def init(cur, con):
    global connection
    global cursor
    connection = con
    cursor = cur

def createUser(cursor: sqlite3.Cursor, email: str, fornavn: str, etternavn: str, passord: str) -> str:
    try:
        cursor.execute("INSERT INTO Bruker VALUES (:epost, :fornavn, :etternavn, :passord)", {"epost": email, "fornavn": fornavn, "etternavn": etternavn, "passord": passord})
        connection.commit()
        return "Laget bruker"
    except Exception:
        return "Epost er tatt"
    return "Noe gikk galt"

def login(cursor: sqlite3.Cursor, epost: str, passord: str) -> str:
    cursor.execute("SELECT epost, passord FROM Bruker WHERE epost = :epost;", {"epost": epost})
    row = cursor.fetchone()
    if (row == None):
        return "Bruker ikke funnet"
    elif (passord != row[1]):
        return "Feil passord"
    else:
        print("Logget inn")
        return row[0]


