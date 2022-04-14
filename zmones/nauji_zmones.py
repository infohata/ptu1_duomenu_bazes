import sqlite3
# import os
# print(os.getcwd())

# prisijungiam prie duomenu bazes, jeigu neranda - sukuria
conn = sqlite3.connect("zmones/zmones.db")

# sukuriam duomenu baze
c = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS draugai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vardas VARCHAR(63),
    pavarde VARCHAR(63),
    email VARCHAR(127)
);
"""

c.execute(query)
conn.commit()
conn.close()
