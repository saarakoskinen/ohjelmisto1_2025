luvut = input('Syötä luku: ')
lista = []

while luvut != '':
    lista.append(luvut)
    luvut = input('Syötä luku: ')

lista.sort(reverse=True)

for n in range(5):
    print(lista[n])
