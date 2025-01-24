tuumat = float(input("Tuumat: "))
while tuumat >= 0:
    cm = tuumat * 2.54
    print(str(cm) + ' cm')
    tuumat = float(input("Tuumat: "))
if tuumat < 0:
    print('Negatiivinen arvo')