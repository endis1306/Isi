def serch(ciag, chain):
    value = ciag.find(chain)
    print(value)

def main():
    ciag = input("Wpisz ciąg znaków do szukania: ")
    chain = input("Wpisz ciag do przeszukania")
    serch(ciag, chain)

main()