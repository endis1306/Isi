from Modul import Sql
sql = Sql()
sql.select("select species ,sex from penguins  where body_mass_g < 3000")

