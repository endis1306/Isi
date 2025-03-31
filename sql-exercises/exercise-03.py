from Modul import Sql
sql = Sql()
sql.select("SELECT DISTINCT island, species FROM ( SELECT island, species FROM penguins LIMIT 11 OFFSET 49 ) AS subquery")

