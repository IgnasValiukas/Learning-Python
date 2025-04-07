import sqlite3

conn = sqlite3.connect('pirma_uzduotis.db')
c = conn.cursor()

# TABLE paskaitos
query = '''
CREATE TABLE IF NOT EXISTS paskaitos (
    pavadinimas VARCHAR(50),
    destytojas VARCHAR(50),
    trukme INTEGER
);
'''
c.execute(query)

with conn:
    # INSERT data
    c.execute("INSERT INTO paskaitos VALUES('Vadyba', 'Domantas', 40);")
    c.execute("INSERT INTO paskaitos VALUES('Python', 'Donatas', 80);")
    c.execute("INSERT INTO paskaitos VALUES('Java', 'Tomas', 80);")
    # SELECT data > 50
    c.execute("SELECT * FROM paskaitos WHERE trukme > 50")
    print(c.fetchall())
    # UPDATE data
    c.execute("UPDATE paskaitos SET pavadinimas = 'Python programavimas' WHERE pavadinimas = 'Python';")
    # DELETE data
    c.execute("DELETE FROM paskaitos WHERE destytojas = 'Tomas'")
    # SELECT all data
    c.execute("SELECT * FROM paskaitos")
    print(c.fetchall())

