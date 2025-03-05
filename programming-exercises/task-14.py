count = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 4 == 0:
        print(i)
        count += 1

print("Liczba liczb podzielnych przez 3 i 4:", count)
