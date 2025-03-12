import csv
import random

def generateNameP(ilosc):
    znaki = 'ABCDEFGHIJKP'
    nazwa = 'P' + ''.join(random.choice(znaki) for _ in range(ilosc-1))
    return nazwa

with open('pc.csv', 'w') as csvf:
    csvwrite = csv.writer(csvf, delimiter=',')
    csvwrite.writerow(('pc_name', 'ip'))
    ipStaticChain = '172.30.2'
    for i in range(1, 101):
        name = generateNameP(6)
        ip = ipStaticChain + f'.{i}'
        csvwrite.writerow((name, ip))

print("Zakończono")

