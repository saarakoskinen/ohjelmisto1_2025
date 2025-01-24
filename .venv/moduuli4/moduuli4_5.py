kayttaja = input('Syötä käyttäjätunnus: ')
salasana = input('Syötä salasana: ')

kokeilut = 0

while kayttaja != 'python' and salasana != 'rules' and kokeilut < 4:
    print('Pääsy evätty.')
    kayttaja = input('Syötä käyttäjätunnus: ')
    salasana = input('Syötä salasana: ')
    kokeilut = kokeilut + 1
if kayttaja == 'python' and salasana == 'rules':
        print('Tervetuloa!')