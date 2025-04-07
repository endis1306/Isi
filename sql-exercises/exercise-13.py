from Modul import Sql
sql = Sql()
sql.select("""SELECT AVG(body_mass_g) AS average_body_mass
FROM penguins
WHERE body_mass_g > 3000.0;
""")

