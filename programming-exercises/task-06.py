import random
import string

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


slownik_25116 = {key: generate_random_string() for key in range(10, 21)}

print(slownik_25116)
