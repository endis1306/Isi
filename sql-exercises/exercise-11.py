from Modul import Sql
sql = Sql()
sql.select("SELECT * FROM penguins WHERE body_mass_g IS NOT NULL AND sex IS NULL")

