import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute("CREATE TABLE notes (autor TEXT, note TEXT);")
cursor.execute("INSERT INTO notes (autor, note) VALUES ('Alice', 'This is a note.');")
cursor.execute("INSERT INTO notes (autor, note) VALUES ('Bob', 'Another note.');")

conn.commit()

with open('notes.sql', 'w') as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")


conn_new = sqlite3.connect('fresh_notes.db')
cursor_new = conn_new.cursor()

with open('notes.sql', 'r') as f:
    sql_script = f.read()

cursor_new.executescript(sql_script)

conn_new.commit()
