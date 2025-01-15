import math

sade_str = input('Syötä ympyrän säde: ')
sade = float(sade_str)
pinta_ala =  math.pi * sade ** 2
print('Ympyrän pinta-ala =', "{:.3f}".format(pinta_ala))
