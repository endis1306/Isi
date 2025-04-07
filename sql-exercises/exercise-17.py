from Modul import Sql
sql = Sql()
sql.create_table("""Create table Notess (autor text, note text);""")
sql.insert("insert into Notess (autor, note) VALUES ('Kuba', 'cos')")
sql.insert("insert into Notess (autor, note) VALUES ('Pawel', 'cosasdsd')")
sql.insert("insert into Notess (autor, note) VALUES ('Alex', 'codsfsfds')")
sql.insert("insert into Notess (autor, note) VALUES ('Jacek', 'Album9')")
sql.select("select * from Notess")

