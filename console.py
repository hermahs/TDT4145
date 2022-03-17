import sql
cursor = None
user = None

def main(cur):
    global cursor 
    cursor = cur

    print('Velkommen til kaffeDB\n')
    isLogin = input('Logg inn med eksisterende bruker? [y/n]: ')
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

    print("Logg inn:")
    email = input('Epost: ')
    password = input('Passord: ')
    user = sql.login(cursor, email, password)
    print(user)

def reviewCoffee():
    return


