import sqlite3


conn = sqlite3.connect("zmones/zmones.db")
c = conn.cursor()

vardas = input("Ieskome pagal varda. Iveskite paieskos kriteriju: ")

with conn:
    # c.execute(f"SELECT * FROM draugai WHERE vardas LIKE '%{vardas}%'")
    c.execute("SELECT * FROM draugai WHERE vardas =?", (vardas,))
    res = c.fetchall()

if res:
    for irasas in res:
        print(irasas)
else:
    print('nieko neradom')
