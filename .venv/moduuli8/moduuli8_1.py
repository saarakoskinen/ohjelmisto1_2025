import mysql.connector


ident = input('Syötä lentokentän ICAO-koodi: ')
yhteys = mysql.connector.connect(
    host='localhost',
    database='flight_game',
    user='username',
    password='salasana',
    autocommit=True,
    collation = 'utf8mb4_unicode_ci'
)

def haeICAO(ident):
    sql = f"SELECT ident, name FROM airport WHERE ident='{ident}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f'Hakemasi lentokentän nimi on: {rivi[1]}')
    return


haeICAO(ident)