from Modul import Sql
sql = Sql()
sql.select("SELECT sex, body_mass_g FROM little_penguins ORDER BY body_mass_g DESC")


