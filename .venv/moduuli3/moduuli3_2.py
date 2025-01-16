print('Hyttiluokat: LUX, A, B ja C')
luokat = ['LUX', 'A', 'B', 'C']
hyttiluokka = input('Syötä hyttiluokka: ')

if hyttiluokka == luokat[0]:
    print('LUX on parvekkeellinen hytti yläkannella.')
elif hyttiluokka == luokat[1]:
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hyttiluokka == luokat[2]:
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hyttiluokka == luokat[3]:
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka.')