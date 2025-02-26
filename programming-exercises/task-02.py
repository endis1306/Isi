
def chainChecker(chain):
    if len(chain) >= 2:
        if all(char.isdigit() for char in chain):
            print("Wprowadzony łańcuch jest liczbą.")
        else:
            print("Wprowadzony łańcuch nie jest liczbą.")
    else:
        print("Łańcuch musi mieć co najmniej 2 znaki.")

def main():
    input_str = input("Wprowadź łańcuch znakowy (min. 2 znaki): ")
    chainChecker(input_str)

main()