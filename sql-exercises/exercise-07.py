from Modul import Sql
sql = Sql()
sql.select("select * from penguins where (sex = 'FEMALE' and island != 'Torgersen') or (sex = 'MALE' and island = 'Torgersen')")
