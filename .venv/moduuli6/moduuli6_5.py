def luvut(parilliset):
    return [luku for luku in parilliset if luku % 2 == 0]

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parilliset_lista = luvut(lista)

    print(lista)
    print(parilliset_lista)

if __name__ == '__main__':
    main()