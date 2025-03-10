# gra.py

import random


def gra():
    tajna_liczba = random.randint(1, 100)

    proby = 0

    print("Witaj w grze! Spróbuj odgadnąć liczbę od 1 do 100.")

    while True:
        try:
            strona = int(input("Podaj liczbę: "))
            proby += 1

            if strona < tajna_liczba:
                print("Twoja liczba jest za mała! Spróbuj ponownie.")
            elif strona > tajna_liczba:
                print("Twoja liczba jest za duża! Spróbuj ponownie.")
            else:
                print(f"Brawo! Trafiłeś w liczbę {tajna_liczba} w {proby} próbach.")
                break

        except ValueError:
            print("Proszę podać liczbę!")

gra()
