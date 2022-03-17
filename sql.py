import sqlite3
from datetime import date

def createUser(cursor: sqlite3.Cursor, email: str, fornavn: str, etternavn: str, passord: str) -> str:
    try:
        cursor.execute("INSERT INTO Bruker VALUES (:epost, :fornavn, :etternavn, :passord);", {"epost": email, "fornavn": fornavn, "etternavn": etternavn, "passord": passord})
        return "Laget bruker"
    except Exception:
        return "Epost er tatt"
    return "Noe gikk galt"

def login(cursor: sqlite3.Cursor, epost: str, passord: str) -> str:
    cursor.execute("SELECT epost, passord FROM Bruker WHERE epost = :epost;", {"epost": epost})
    row = cursor.fetchone()
    if (row == None):
        return "Bruker ikke funnet"
    else if passord != row[1]:
        return "Feil passord"
    else
        return "Successful login"

def getMostCoffeeTastedThisYear(cursor: sqlite.Cursor) -> list: #fungerer kun for året 2022 :)
    cursor.execute("SELECT Fornavn, Etternavn, COUNT(*) AS Antall FROM Kaffesmaking AS K NATURAL INNER JOIN Bruker AS B WHERE Dato >= '2022-01-01') GROUP BY Epost ORDER BY Antall DESC;")
    rows = cursor.fetchall()
    return rows

def bestCoffeeByRatingMoney(cursor: sqlite3.Cursor) -> list:
    cursor.execute("SELECT B.Navn, K.KiloprisNOK, AVG(S.Poeng) AS Gjennomsnittscore FROM Kaffesmaking AS S INNER JOIN Ferdigbrentkaffe AS K ON (S.KaffeNavn = K.Navn AND S.BrenneriID = K.BrenneriID) INNER JOIN Kaffebrenneri AS B ON (B.ID = K.BrenneriID) GROUP BY B.Navn, K.Navn ORDER BY Gjennomsnittscore/K.KiloprisNOK DESC;")
    rows = cursor.fetchall()
    return rows

def searchByKeyword(cursor: sqlite3.Cursor, keyword: str) -> list:
    cursor.execute("SELECT DISTINCT S.Navn, K.Navn FROM (Kaffesmaking AS S NATURAL INNER JOIN Ferdigbrentkaffe AS K) INNER JOIN Kaffebrenneri AS B ON (K.BrenneriID = B.ID) WHERE S.Notat LIKE %:keyword% OR K.Beskrivelse LIKE %:keyword%;", {"keyword": keyword})
    rows = cursor.fetchall()
    return rows

def searchForNotWashedByCountry(cursor: sqlite3.Cursor, land: str) -> list:
    cursor.execute("SELECT DISTINCT B.Navn, K.Navn FROM (((FerdigbrentKaffe AS K INNER JOIN Kaffebrenneri AS B ON (K.BrenneriID = B.ID)) INNER JOIN Kaffeparti AS P ON (P.ID = K.PartiID)) INNER JOIN Foredlingsmetode AS M ON (P.ForedlingsNavn = M.Navn)) INNER JOIN (Region AS R INNER JOIN Gard as G ON (R.Navn = G.Region AND R.Land = G.Land)) ON (G.ID = P.GardID) WHERE M.Navn <> 'Vasket' AND R.Land = :land;", {"land": land})
    rows = cursor.fetchall()
    return rows
    
def createCoffeeTasting(cursor: sqlite3.Cursor, epost: str, brennriID: int, kaffeNavn: str, poeng: int, smaksNotat: str) -> str:
    try:
        cursor.execute("INSERT INTO Kaffesmaking VALUES (:epost, :kaffeNavn, :brenneriID, :smaksNotat, :poeng, :dato);", {"epost": epost, "kaffeNavn": kaffeNavn, "brenneriID": brenneriID, "smaksNotat": smaksNotat, "poeng": poeng, "dato": date.today().strftime("%Y-%m-%d")})
        return "Kaffesmaking lagt til"
    except Exception:
        return "noe gikk feil"

