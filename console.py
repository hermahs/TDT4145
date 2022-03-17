import sql
import sys
cursor = None
user = None

def main(cur):
    global cursor 
    cursor = cur

    print('Velkommen til kaffeDB\n')
    isLogin = input('\nLogg inn med eksisterende bruker? [y/n]: ')
    if (isLogin == 'n'):
        print('Registrer en ny bruker:')
        email = input('Epost*: ')
        fName = input('Fornavn*: ')
        lName = input('Etternavn*: ')
        password = input('Passord*: ')
        msg = sql.createUser(cursor, email, fName, lName, password)
        print(msg)
        login()
    else:
        login()

def login():
    global user

    print("\nLogg inn:")
    email = input('Epost*: ')
    password = input('Passord*: ')
    user = sql.login(cursor, email, password)
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
    coffeName = input("Kaffenavn*: ")
    # TODO: sjekk om kaffenavn eksisterer og vis liste over kaffenavn, brennerinavn, brenneriID
    roastery = input("Velg ID til brenneri fra listen*: ")
    note = input("Et kort notat: ")
    score = input("Poengscore (0-10)*: ")
    date = input("Dato: ")
    # TODO: SQL insert
    options()

def getData():
    userStory = input("""\nHva vil du vite?\n
    (1) Brukere som har smakt flest unike kaffer i år\n
    (2) Kaffer som gir deg mest for pengene\n
    (3) Florale kaffer\n
    (4) Kaffer fra Rwanda og Colombia som ikke er vaskede\n""")

    if (userStory == "1"):
        print(2)
    elif (userStory == "2"):
        print(3)
    elif (userStory == "3"):
        print(4)
    elif (userStory == "4"):
        print(5)
    
    options()

def logout():
    sys.exit("Logget ut")


