from Modul import Sql
sql = Sql()
sql.select("""SELECT COUNT(DISTINCT body_mass_g) AS unique_body_masses
FROM penguins;
""")

