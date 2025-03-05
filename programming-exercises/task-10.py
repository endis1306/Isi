numer_albumu = "25116"

alfabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))

with open(f"alfabet1-{numer_albumu}.txt", "w") as file1:
    file1.write(alfabet)

with open(f"alfabet2-{numer_albumu}.txt", "w") as file2:
    for letter in alfabet:
        file2.write(letter + '\n')

print("Pliki zostały zapisane.")
