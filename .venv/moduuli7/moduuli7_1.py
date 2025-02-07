kk = int(input('Anna kuukauden numero: '))
vuodenajat = ('kevät', 'kesä', 'syksy', 'talvi')
if kk in (12, 1, 2):
    print(vuodenajat[3])
elif kk in (3, 4, 5):
    print(vuodenajat[0])
elif kk in (6, 7, 8):
    print(vuodenajat[1])
elif kk in (9, 10, 11):
    print(vuodenajat[2])
else:
    print('Ei hyväksytty.')