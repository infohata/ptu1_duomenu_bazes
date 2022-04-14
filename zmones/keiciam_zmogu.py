import sqlite3


conn = sqlite3.connect("zmones/zmones.db")
c = conn.cursor()

with conn:
    c.execute("UPDATE draugai SET vardas='Smagus' WHERE vardas='Snagys'")
    c.execute("SELECT * FROM draugai")
    for irasas in c.fetchall():
        print(irasas)
