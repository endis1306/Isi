import random
import string


def createPasswords(ilosc, dlugosc, plik):
    all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

    with open(plik, 'w') as f:
        for _ in range(ilosc):
            password = ''.join(random.choice(all_characters) for _ in range(dlugosc))
            f.write(password + '\n')


createPasswords(1000, 6, 'passwords.txt')
