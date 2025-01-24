from random import randint
luku = randint(1, 10)
arvaus = 0
while arvaus != luku:
    arvaus = int(input('Syötä luku 1-10 väliltä: '))
    if arvaus > luku:
        print('Liian suuri')
    if arvaus < luku:
        print('Liian pieni')
    if arvaus == luku:
        print('Oikein!')