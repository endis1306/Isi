from Modul import Sql
sql = Sql()
sql.select("""SELECT 
AVG(body_mass_g) FILTER(WHERE body_mass_g > 4500) AS average_heavy_penguins,
AVG(body_mass_g) FILTER(WHERE body_mass_g < 3500) AS average_light_penguins
FROM penguins;
""")
