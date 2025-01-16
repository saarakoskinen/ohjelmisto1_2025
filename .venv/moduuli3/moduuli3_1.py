kuha = input('Syötä kuhan pituus senttimetreinä: ')
if kuha <= '36':
    print('Kuha on alamittainen, heitä takaisin.')
    print('Kuha on',37 - int(kuha),'cm liian lyhyt.')
else:
    print('Kuha on riittävän suuri.')