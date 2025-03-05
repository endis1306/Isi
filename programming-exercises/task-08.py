import random
import string
from collections import Counter

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))

char_count = Counter(random_string)

char_count_list = list(char_count.items())

print(f"Losowy ciąg znaków: {random_string}")
print("\nSłownik z liczbą wystąpień znaków:")
print(char_count)
print("\nLista krotek (tupli):")
print(char_count_list)
