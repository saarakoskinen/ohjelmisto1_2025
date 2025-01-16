sukupuoli = input('Syötä biologinen sukupuolesi: ')
hemogl = int(input('Syötä hemoglobiiniarvosi g/l: '))
vaihtoehdot = ['Nainen', 'Mies']

if sukupuoli == vaihtoehdot[0]:
    if hemogl <= 175 and hemogl >= 117:
        print('Hemoglobiiniarvo normaali')
    if hemogl >= 176:
        print('Hemoglobiiniarvo liian korkea')
    if hemogl <= 116:
        print('Hemoglobiiniarvo liian matala')

if sukupuoli == vaihtoehdot[1]:
    if hemogl <= 195 and hemogl >= 134:
        print('Hemoglobiiniarvo normaali')
    if hemogl >= 196:
        print('Hemoglobiiniarvo liian korkea')
    if hemogl <= 133:
        print('Hemoglobiiniarvo liian matala')