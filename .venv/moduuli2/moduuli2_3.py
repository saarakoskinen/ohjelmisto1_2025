kanta_str = input('Syötä suorakulman kanta: ')
kanta = float(kanta_str)

korkeus_str = input('Syötä suorakulman korkeus: ')
korkeus = float(korkeus_str)

piiri = kanta *2 + korkeus*2

pinta_ala = korkeus * kanta

print('Suorakulmion piiri on', str(piiri) + ' ja pinta-ala', str(pinta_ala))
