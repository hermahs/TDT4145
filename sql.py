import sqlite3
from datetime import date
connection = None
cursor = None

def init(cur, con):
    global connection
    global cursor
    connection = con
    cursor = cur

def createUser(email: str, fornavn: str, etternavn: str, passord: str) -> str:
    try:
        cursor.execute("INSERT INTO Bruker VALUES (:epost, :fornavn, :etternavn, :passord)",
            {
                "epost": email, 
                "fornavn": fornavn, 
                "etternavn": etternavn, 
                "passord": passord
            })
        connection.commit()
        return "Laget bruker"
    except Exception:
        return "Epost er tatt"
    return "Noe gikk galt"

def login(epost: str, passord: str) -> str:
    cursor.execute("SELECT epost, passord FROM Bruker WHERE epost = :epost;", {"epost": epost})
    row = cursor.fetchone()
    if (row == None):
        print("Bruker ikke funnet")
        return None
    elif (passord != row[1]):
        print("Feil passord")
        return None
    else:
        print("Logget inn")
        return row[0]

def getCoffeesByName(name: str) -> list:
    query = ("SELECT B.ID, K.Navn, B.Navn "
            "FROM FerdigbrentKaffe AS K INNER JOIN Kaffebrenneri AS B ON (K.BrenneriID = B.ID) "
            "WHERE K.Navn=:name;"
            )
    cursor.execute(query, {"name": name})
    rows = cursor.fetchall()
    return rows

def getMostCoffeeTastedThisYear() -> list: #fungerer kun for året 2022 :)
    query = ("SELECT Fornavn, Etternavn, COUNT(*) AS Antall " 
            "FROM Bruker AS B NATURAL JOIN Kaffesmaking AS S "
            "WHERE Dato >= '2022-01-01' " 
            "GROUP BY B.Epost "
            "ORDER BY Antall DESC;"
            )
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def bestCoffeeByRatingMoney() -> list:
    query = ("SELECT B.Navn, K.Navn, K.KiloprisNOK, AVG(S.Poeng) AS Gjennomsnittscore "
            "FROM Kaffesmaking AS S "
            "INNER JOIN FerdigbrentKaffe AS K ON (S.KaffeNavn = K.Navn AND S.BrenneriID = K.BrenneriID) "
            "INNER JOIN Kaffebrenneri AS B ON (B.ID = K.BrenneriID) "
            "GROUP BY B.Navn, K.Navn "
            "ORDER BY Gjennomsnittscore/K.KiloprisNOK DESC;"
            )
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def getFloralCoffees() -> list:
    query = ("SELECT DISTINCT B.Navn, K.Navn "
            "FROM (Kaffesmaking AS S INNER JOIN FerdigbrentKaffe AS K ON (S.KaffeNavn = K.Navn AND S.BrenneriID = K.BrenneriID)) "
            "INNER JOIN Kaffebrenneri AS B ON (K.BrenneriID = B.ID) "
            "WHERE S.Notat LIKE '%floral%' OR K.Beskrivelse LIKE '%floral%';"
            )
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def getNotWashedRwandaColombia() -> list:
    query = ("SELECT DISTINCT B.Navn, K.Navn "
            "FROM (((FerdigbrentKaffe AS K INNER JOIN Kaffebrenneri AS B ON (K.BrenneriID = B.ID)) "
                "INNER JOIN Kaffeparti AS P ON (P.ID = K.PartiID)) "
                "INNER JOIN Foredlingsmetode AS M ON (P.ForedlingsNavn = M.Navn)) "
                "INNER JOIN (Region AS R INNER JOIN Gard as G ON (R.Region = G.Region AND R.Land = G.Land)) ON (G.ID = P.GardID) "
            "WHERE M.Navn <> 'Vasket' AND (R.Land = 'Rwanda' OR R.Land = 'Colombia');"
            )
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
    
def createCoffeeTasting(epost: str, brenneriID: int, kaffeNavn: str, poeng: int, smaksNotat: str, dato: str) -> str:
    try:
        cursor.execute("INSERT INTO Kaffesmaking VALUES (:epost, :kaffeNavn, :brenneriID, :smaksNotat, :poeng, :dato);",
            {
                "epost": epost,
                "kaffeNavn": kaffeNavn,
                "brenneriID": brenneriID, 
                "smaksNotat": smaksNotat, 
                "poeng": poeng, 
                "dato": dato if dato else date.today().strftime("%Y-%m-%d")
            })
        connection.commit()
        print("Kaffesmaking lagt til")
    except Exception as e:
        print("Noe gikk feil:", e)

