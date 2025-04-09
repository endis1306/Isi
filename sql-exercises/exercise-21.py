from Modul import Sql
sql = Sql()
sql.select("""SELECT w.person, j.name AS job_name, MIN(j.billable) AS min_time
FROM work w
INNER JOIN job j ON w.job = j.name
GROUP BY w.person;
""")

