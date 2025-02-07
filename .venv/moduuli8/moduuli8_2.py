import mysql.connector
import numpy as np
import pandas as pd

iso_country = input('Syötä lentokentän maakoodi: ')
yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'username',
    password = 'salasana',
    autocommit = True,
    collation = 'utf8mb4_unicode_ci'
    )
tyyppi = []
def hae_maakoodi(iso_country):
    sql = "SELECT iso_country, type FROM airport "
    sql += "WHERE iso_country='" + iso_country + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            tyyppi.append(rivi[1])
        print(pd.value_counts(np.array(tyyppi)))
    return

hae_maakoodi(iso_country)