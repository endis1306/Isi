import sqlite3
from sqlite3 import Error
from tabulate import tabulate

class Sql:
    def __init__(self, db_file="C:/Users/25116/Desktop/SQL Exercises/Isi/sql-exercises/db/penguins.db"):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(f"Połączenie z bazą danych {db_file} zostało nawiązane.")
        except Error as e:
            print(f"Błąd połączenia z bazą danych: {e}")

    def close_connection(self):
        """Zamknięcie połączenia z bazą danych."""
        if self.conn:
            self.conn.close()
            print("Połączenie z bazą danych zostało zamknięte.")

    def select(self, sql_select):
        try:
            c = self.conn.cursor()
            c.execute(sql_select)
            
            # Pobieranie nazw kolumn
            column_names = [description[0] for description in c.description]
            
            # Pobieranie danych
            rows = c.fetchall()
            
            # Wyświetlanie wyników w tabeli
            print(tabulate(rows, headers=column_names, tablefmt="pretty"))
            
            return rows
        
        except Error as e:
            print(f"Błąd podczas wykonywania zapytania SELECT: {e}")

    def insert(self, sql_insert):
        try:
            c = self.conn.cursor()
            c.execute(sql_insert)
            self.conn.commit()
            print("Dane zostały wstawione do bazy.")
        except Error as e:
            print(f"Błąd podczas wykonywania zapytania INSERT: {e}")

    def update(self, sql_update):
        try:
            c = self.conn.cursor()
            c.execute(sql_update)
            self.conn.commit()
            print("Dane zostały zaktualizowane.")
        except Error as e:
            print(f"Błąd podczas wykonywania zapytania UPDATE: {e}")

    def delete(self, sql_delete):
        try:
            c = self.conn.cursor()
            c.execute(sql_delete)
            self.conn.commit()
            print("Dane zostały usunięte.")
        except Error as e:
            print(f"Błąd podczas wykonywania zapytania DELETE: {e}")
