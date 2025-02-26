def digitChecker(char):
    if char.isdigit():
        print("Wprowadzony znak jest cyfrą.")
    else:
        print("Wprowadzony znak nie jest cyfrą.")

def instanceChecker(char):
    if isinstance(char, str) and char.isdigit():
        print("Wprowadzony znak jest cyfrą.")
    else:
        print("Wprowadzony znak nie jest cyfrą.")

def main():
    char = input("Wprowadź pojedynczy znak: ")[0]
    instanceChecker(char)

main()