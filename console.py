import sql
cursor = None
user = None

def main(cur):
    global cursor 
    cursor = cur

    print('Velkommen til kaffeDB\n')
    isLogin = input('\nLogg inn med eksisterende bruker? [y/n]: ')
    if (isLogin == 'n'):
        print('Registrer en ny bruker:')
        email = input('Epost: ')
        fName = input('Fornavn: ')
        lName = input('Etternavn: ')
        password = input('Passord: ')
        msg = sql.createUser(cursor, email, fName, lName, password)
        print(msg)
        login()
    else:
        login()

def login():
    global user

    print("\nLogg inn:")
    email = input('Epost: ')
    password = input('Passord: ')
    user = sql.login(cursor, email, password)
    next = input("\nHva vil du gjøre? (1) Registrer kaffesmaking, (2) Hent data: ")
    if (next == "1"):
        reviewCoffee()
    elif (next == "2"):
        getData()

def reviewCoffee():
    global user

    print("\nRegistrer kaffesmaking:")

def getData():
    print("\nHent data:")


