from Modul import Sql
sql = Sql()      
sql.select("SELECT species || ' ' || island AS combined_info FROM penguins;")

