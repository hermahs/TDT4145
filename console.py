cursor = None

def main(cur):
    cursor = cur
    print('Velkommen til kaffeDB\n')
    login = input('Logg inn med eksisterende bruker? [y/n]: ')
    if (login == 'n'):
        print('Registrer en ny bruker:')
        email = input('Epost: ')
        fName = input('Fornavn: ')
        lName = input('Etternavn: ')
        password = input('Passord: ')
        print(email, fName, lName, password)
        # TODO: kjør sql insert
    else:
        login()

def login():
    print("Logg inn:")
    email = input('Epost: ')
    password = input('password')
    # TODO: kjør sql

