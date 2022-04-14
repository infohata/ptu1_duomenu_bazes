import sqlite3


conn = sqlite3.connect("zmones/zmones.db")
c = conn.cursor()

draugai = [
    ('Linksmas', 'Penktadieninis', 'party@gmail.com'),
    ('Liudnas', 'Pirmadieninis', 'tipiskas@lietuvis.lt'),
    ('Grazi', 'Mergaite', 'grazuole@blondine.lt'),
]

with conn:
    c.executemany("INSERT INTO draugai (vardas, pavarde, email) VALUES (?, ?, ?)", draugai)

