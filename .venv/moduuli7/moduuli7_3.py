lentokentat = {}

kysymys = ()
while kysymys != '':
    kysymys = input('Haluatko hakea, vai tallentaa tietoa? (H/T)')
    if kysymys == '':
        break
    while kysymys not in ['h', 'H', 't', 'T']:
        print('Ei hyväksytty.')
        kysymys = input('Haluatko hakea, vai tallentaa tietoa? (H/T)')
        if kysymys == '':
            break

    if kysymys in ['t', 'T']:
        talletus1 = input('Syötä ICAO-koodi: ')
        talletus2 = input('Syötä lentokentän nimi: ')
        lentokentat[talletus1] = talletus2
        print('Talletus onnistui.')

    elif kysymys in ['h', 'H'] and lentokentat == {}:
        print('Ei tallennettuja lentokenttiä.')

    elif kysymys in ['h', 'H']:
        haku = input('Syötä ICAO-koodi: ')
        while haku not in lentokentat:
            print('ICAO-koodi ei löydy.')
            haku = input('Syötä ICAO-koodi: ')
        print(f'Hakemasi kenttä on: {lentokentat[haku]}')