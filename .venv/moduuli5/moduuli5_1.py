import random

arpakuutiot = int(input('Syötä arpakuutioiden lukumäärä: '))
lista = []

for i in range(arpakuutiot):
    silmaluku = random.randint(1, 6)
    lista.append(silmaluku)

print(sum(lista))
