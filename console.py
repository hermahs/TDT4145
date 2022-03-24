import sql
import sys
from tabulate import tabulate
user = None

def main():
    isLogin = input('\nLogg inn med eksisterende bruker? [y/n]: ')
    if (isLogin == 'n'):
        print('Registrer en ny bruker:')
        email = input('Epost*: ')
        fName = input('Fornavn*: ')
        lName = input('Etternavn*: ')
        password = input('Passord*: ')
        msg = sql.createUser(email, fName, lName, password)
        print(msg)
        main()
    else:
        login()

def login():
    global user

    print("\nLogg inn:")
    email = input('Epost*: ')
    password = input('Passord*: ')
    user = sql.login(email, password)
    if (user == None):
        main()
    else:
        options()

def options():
    correctInput = False
    while (not correctInput):
        correctInput = True
        next = input("\nHva vil du gjøre? (1) Registrer kaffesmaking, (2) Hent data, (3) Logg ut: ")
        if (next == "1"):
            reviewCoffee()
        elif (next == "2"):
            getData()
        elif (next == "3"):
            logout()
        else:
            print("Feil input")
            correctInput = False

def reviewCoffee():
    global user

    print("\nRegistrer kaffesmaking:")
    coffeeName = input("Kaffenavn*: ")

    result = sql.getCoffeesByName(coffeeName)

    print(tabulate(
        result, 
        headers=["BrenneriID", "Kaffenavn", "Brennerinavn"], 
        tablefmt="psql"))

    roastery = input("Velg ID til brenneri fra listen*: ")
    note = input("Et kort notat: ")
    score = input("Poengscore (0-10)*: ")
    date = input("Dato (YYYY-MM-DD): ")
    sql.createCoffeeTasting(user, roastery, coffeeName, score, note, date);
    options()

def getData():
    userStory = input("""\nHva vil du vite?\n
    (1) Brukere som har smakt flest unike kaffer i år\n
    (2) Kaffer som gir deg mest for pengene\n
    (3) Søk etter kaffer som er beskrevet med ordet "floral"\n
    (4) Søk etter kaffer som ikke er vasket fra Rwanda eller Colombia\n""")

    if (userStory == "1"):
        print(tabulate(
            sql.getMostCoffeeTastedThisYear(),
            headers=["Fornavn", "Etternavn", "Antall smakinger"], 
            tablefmt="psql"))
    elif (userStory == "2"):
        print(tabulate(
            sql.bestCoffeeByRatingMoney(), 
            headers=["Brennerinavn", "Kaffenavn", "KiloprisNOK", "Gjennomsnittscore"], 
            tablefmt="psql"))
    elif (userStory == "3"):
        print(
            tabulate(sql.getFloralCoffees(), 
            headers=["Brennerinavn", "Kaffenavn"], 
            tablefmt="psql"))
    elif (userStory == "4"):
        print(
            tabulate(sql.getNotWashedRwandaColombia(), 
            headers=["Brennerinavn", "Kaffenavn"], 
            tablefmt="psql"))
    
    options()

def logout():
    sys.exit("Logget ut")


