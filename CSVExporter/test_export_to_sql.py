import unittest
import sqlite3
import csv
import os
from csv_analyzer_extended import CSVFilter, CSVExporter

class TestExportToSQL(unittest.TestCase):
    def setUp(self):
        # Lade die CSV-Datei und lese den Header und die Daten
        with open('data.csv', newline='', encoding='ISO-8859-1') as file:  # Kodierung ISO-8859-1 für die Datei
            reader = csv.reader(file, delimiter=';')  # Angabe des richtigen Trennzeichens
            self.header = next(reader)  # Lese die Header-Zeile
            self.data = [row for row in reader]

        self.analyzer = CSVFilter(self.data, self.header)
        self.available_columns = self.analyzer.header

        # Überprüfe, ob self.available_columns wirklich eine Liste ist
        assert isinstance(self.available_columns, list), "available_columns should be a list"

        # SQLite-Datenbankverbindung einrichten
        self.connection = sqlite3.connect(':memory:')  # In-Memory-Datenbank für Tests
        self.cursor = self.connection.cursor()
        
        # Spaltennamen in Anführungszeichen setzen, um SQL-Kompatibilität sicherzustellen
        quoted_columns = [f'"{col}"' for col in self.available_columns]

        # Erstelle die SQL-Tabelle mit korrekten Spaltendatentypen
        self.cursor.execute(f'CREATE TABLE test_table ({", ".join(quoted_columns)})')

    def tearDown(self):
        self.connection.close()

    def test_export_to_sql(self):
        if len(self.available_columns) > 2:
            cols = self.available_columns[:2]
            print(f"Starting export to SQL test for columns '{cols}'...")
            selected_data = self.analyzer.select_columns(cols)
            exporter = CSVExporter(selected_data, cols)
            exporter.export_to_sql('test_table', self.cursor)
            self.cursor.execute('SELECT * FROM test_table')
            rows = self.cursor.fetchall()
            self.assertGreater(len(rows), 0, f"No data was exported to SQL for columns '{cols}'")
            print(f"Data for '{cols}' successfully exported to SQL.")
        else:
            print("Not enough columns available for export to SQL test.")

if __name__ == '__main__':
    unittest.main()
