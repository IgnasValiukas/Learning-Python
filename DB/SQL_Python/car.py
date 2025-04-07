import sqlite3

# Antra uzduotis
conn = sqlite3.connect('car.db')
c = conn.cursor()

query = '''
CREATE TABLE IF NOT EXISTS car (
	id INTEGER PRIMARY KEY,
	make VARCHAR(50),
	model VARCHAR(50),
	color VARCHAR(50),
	model_year INTEGER,
	price REAL
);
'''
c.execute(query)

car_data = [
    ('Mitsubishi', 'Pajero', 'Fuscia', 1996, 4.19),
    ('Hyundai', 'Accent', 'Pink', 2011, 59.99),
    ('Chrysler', 'New Yorker', 'Khaki', 1992, 25.99),
    ('Nissan', 'Versa', 'Goldenrod', 2011, 49.99),
    ('Mercedes-Benz', 'S-Class', 'Mauv', 2003, 5.49),
    ('Ram', '2500', 'Khaki', 2012, 2.19)
]
# INSERT data
# with conn:
#     c.executemany("INSERT INTO car (make, model, color, model_year, price) VALUES(?,?,?,?,?)", car_data)

# Trecia uzduotis
print("Add car details (make, model, color, model_year, price)")
make = input("Add make: ")
model = input("Add model: ")
color = input("Add color: ")
model_year = int(input("Add model_year: "))
price = float(input("Add price: "))

with conn:
    c.execute("INSERT INTO car (make, model, color, model_year, price) VALUES(?,?,?,?,?)",
                  (make, model, color, model_year, price))

# search_parameter = input("Choose search parameter (make, model, color, model_year, price): ")
#
# with conn:
#     c.execute("SELECT ? FROM car", search_parameter)
#     print(c.fetchall())