liczby = []

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        liczby.append(i)

print("Liczby podzielne przez 3 lub 5:", liczby)
