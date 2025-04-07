import sqlite3
from tabulate import tabulate


def converter(rows):
    return [[cell if cell is not None else 'null' for cell in row] for row in rows]
conn = sqlite3.connect('./db/penguins.db')
cursor = conn.cursor()
sql = """
select
    flipper_length_mm / 10.0 as flipper_cm,
    body_mass_g / 1000.0 as weight_kg,
    island as where_found
from penguins
limit 5;
"""
cursor.execute(sql)
rows = cursor.fetchall()
rows_cleaned = converter(rows)
columns = [desc[0] for desc in cursor.description]

print(tabulate(rows_cleaned, headers=columns, tablefmt="grid"))

conn.close()
