import sqlite3


conn = sqlite3.connect("zmones/zmones.db")
c = conn.cursor()

vardas = "Geras"
pavarde = "Zmogus"
email = "geras@zmogus.lt"
vienas = (vardas, pavarde, email,)

with conn:
    c.execute("INSERT INTO draugai (vardas, pavarde, email) VALUES (?, ?, ?)", vienas)

