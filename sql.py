import sqlite3

def createUser(cursor: sqlite3.Cursor, email: str, fornavn: str, etternavn: str, passord: str) -> str:
    try:
        cursor.execute("INSERT INTO Bruker VALUES (:epost, :fornavn, :etternavn, :passord)", {"epost": email, "fornavn": fornavn, "etternavn": etternavn, "passord": passord})
        return true
    except Exception:
        return false
    return false

def login(cursor: sqlite3.Cursor, epost: str, passord: str) -> str:
    cursor.execute("SELECT epost, passord FROM Bruker WHERE epost = :epost", {"epost": epost})
    row = cursor.fetchone()
    if (row == None):
        return "Bruker ikke funnet"
    else if passord != row[1]:
        return "Feil passord"
    else
        return "Successful login"


