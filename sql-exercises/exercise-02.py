from Modul import Sql
sql = Sql()
sql.select("select * from penguins limit 11 offset 49")

