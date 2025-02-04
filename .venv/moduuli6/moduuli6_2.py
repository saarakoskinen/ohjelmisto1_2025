import random

tahkot = int(input("Tahkojen määrä: "))

def heitto(tahkot):
    return random.randint(1, tahkot)

noppa = 0
while noppa != tahkot:
    noppa = heitto(tahkot)
    print(noppa)