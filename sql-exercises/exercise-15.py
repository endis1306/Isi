from Modul import Sql
sql = Sql()
sql.select("""SELECT body_mass_g, COUNT(*) AS num_penguins
FROM penguins
GROUP BY body_mass_g
ORDER BY body_mass_g;
""")

