luku = input('syötä luku: ')
lista = []
while luku != '':
    luku = input('syötä luku: ')
    if luku != '':
        lista.append(luku)
print('Ohjelma lopetettu')
print(min(lista) , max(lista))



