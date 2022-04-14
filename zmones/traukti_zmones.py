import sqlite3


conn = sqlite3.connect("zmones/zmones.db")
c = conn.cursor()

with conn:
    c.execute(f"SELECT * FROM draugai") # WHERE rowid IN {tuple(range(0,7,2))}
    for irasas in c.fetchall():
        print(irasas)
    # viskas viename
    # print(c.fetchall())
    # vienas
    # print(c.fetchone())
