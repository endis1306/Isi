from Modul import Sql
sql = Sql()
sql.select("select * from penguins where species is not 'Gentoo' ")
