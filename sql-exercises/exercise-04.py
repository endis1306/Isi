from Modul import Sql
sql = Sql()
sql.select("select body_mass_g from penguins where body_mass_g < 3000")

