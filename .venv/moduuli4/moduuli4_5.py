kayttaja = input('Syötä käyttäjätunnus: ')
salasana = input('Syötä salasana: ')

while kayttaja != 'python' and salasana != 'rules':
    print('Pääsy evätty.')
    kayttaja = input('Syötä käyttäjätunnus: ')
    salasana = input('Syötä salasana: ')
    if kayttaja == 'python' and salasana == 'rules':
        print('Tervetuloa!')