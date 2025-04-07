from Modul import Sql
sql = Sql()
sql.select("""SELECT *
FROM penguins
WHERE body_mass_g IS NULL
AND sex IS NOT NULL;
""")


