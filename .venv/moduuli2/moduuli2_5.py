leiviskat_str = input('Anna leiviskät: ')
naulat_str = input('Anna naulat: ')
luodit_str = input('Anna luodit: ')

leiviskat = float(leiviskat_str)
naulat = float(naulat_str)
luodit = float(luodit_str)

luodit_g = luodit * 13.3
naulat_g = naulat * 32 * 13.3
leiviskat_g = leiviskat * 20 * 32 * 13.3

yht = leiviskat_g + naulat_g + luodit_g

kilot = int(yht / 1000)
grammat = round(yht % 1000, 2)

print('Massa nykymitoissa:', str(kilot), 'kg ja ', str(grammat), 'grammaa' )

