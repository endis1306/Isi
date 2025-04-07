import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute("CREATE TABLE notes (autor TEXT, note TEXT);")
cursor.execute("INSERT INTO notes (autor, note) VALUES ('Alice', 'This is a note.');")
cursor.execute("INSERT INTO notes (autor, note) VALUES ('Bob', 'Another note.');")

conn.commit()

backup_conn = sqlite3.connect('notes.db')

conn.backup(backup_conn)

backup_conn.close()
conn.close()

