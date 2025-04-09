from Modul import Sql
sql = Sql()

sql. create_table("""create table job (
    name text not null,
    billable real not null
);""")

sql. create_table("""create table work (
    person text not null,
    job text not null
);""")

sql.insert("""insert into job values
('calibrate', 1.5)""")

sql.insert("""insert into job values ('clean', 0.5);""")

sql.insert("""insert into work values
('mik', 'calibrate'),
('mik', 'clean'),
('mik', 'complain'),
('po', 'clean'),
('po', 'complain'),
('tay', 'complain');""")

sql.select("""select *
from work inner join job
on job = name;""")


