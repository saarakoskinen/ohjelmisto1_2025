setti = set([])
nimet = 'alku'
while nimet != '':
    nimet = input('Syötä nimi: ')

    if nimet in setti:
        print('Aiemmin syötetty nimi.')
    elif nimet == '':
        break
    else:
        print('Uusi nimi.')
    setti.add(nimet)
for p in setti:
    print(p)