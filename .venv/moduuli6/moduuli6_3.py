def galloonat(gal):
    return gal * 3.758

gal = 1
while gal > 0:
    gal = float(input('Syötä galloonat: '))

    if gal < 0:
        print('Ei sallittu.')
        break

    print(f'{gal} galloonaa on {round(galloonat(gal), 3)} litraa.')
