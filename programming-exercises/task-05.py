import math

sqrt_numbers = [int(math.sqrt(i)) for i in range(1, 257) if int(math.sqrt(i)) % 2 == 0]

print("Pierwiastki liczb od 1 do 256:", sqrt_numbers)
