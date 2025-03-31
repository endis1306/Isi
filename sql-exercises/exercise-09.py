from Modul import Sql
sql = Sql()
sql.select("SELECT *, bill_length_mm / bill_depth_mm AS bill_ratio FROM penguins;")
