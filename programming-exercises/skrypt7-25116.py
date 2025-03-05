from utils.obliczenia import pierwiastek, silnia, czyNan, logarytm
import math

x=9
y=1
z=3
w=float('nan')

print(f"Pierwiastek kwadratowy z {x}: {pierwiastek(x)}")
print(f"Logarytm naturalny z {y}: {logarytm(y)}")
print(f"Silnia z  {z}: {silnia(z)}")
print(f"Czy NAN {w}: {czyNan(w)}")