def najdluzszy_wyraz(plik):
    with open(plik, 'r') as file:
        najdluzszy = ''

        for linia in file:
            wyraz = linia.strip()

            if len(wyraz) > len(najdluzszy):
                najdluzszy = wyraz

        return najdluzszy


def wyrazy_dlugosci_10(plik):
    wyrazy_10 = []

    with open(plik, 'r') as file:
        for linia in file:
            wyraz = linia.strip()

            if len(wyraz) == 10:
                wyrazy_10.append(wyraz)

    return wyrazy_10


plik = 'wordlist_10000.txt'

najdluzszy = najdluzszy_wyraz(plik)
print(f"Najdłuższy wyraz w pliku to: {najdluzszy}")

wyrazy_10 = wyrazy_dlugosci_10(plik)
print(f"Wyrazy o długości 10: {wyrazy_10}")
