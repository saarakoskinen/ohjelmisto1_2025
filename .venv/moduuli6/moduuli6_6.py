import math

def pizza(halkaisija, hinta):
    return hinta / (math.pi * math.pow((halkaisija / 2),2) / 10000)

pizza1 = float(input('Anna pizzan 1 halkaisija senttimetreinä: '))
pizza1e = float(input('Anna pizzan 1 hinta euroina: '))
pizza2 = float(input('Anna pizzan 2 halkaisija senttimetreinä: '))
pizza2e = float(input('Anna pizzan 2 hinta euroina: '))

pizza1_hinta = pizza(pizza1,pizza1e)
pizza2_hinta = pizza(pizza2, pizza2e)

print(f'Pizza 1: {pizza1_hinta:.2f} € / m²')
print(f'Pizza 2: {pizza2_hinta:.2f} € / m²')

if pizza1_hinta == pizza2_hinta:
    print('Pizzat ovat saman hintaisia.')
elif pizza1_hinta < pizza2_hinta:
    print('pizza 1 on halvempi.')
else:
    print('Pizza 2 on halvempi.')