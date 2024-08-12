import unittest
import os
from csv_analyzer_extended import CSVAnalyzer, CSVExporter

class TestExportWithSpecialCharacters(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('special_characters_data.csv')
        self.available_columns = self.analyzer.header
        print("Available columns:", self.available_columns)

    def test_export_with_special_characters_to_csv(self):
        if len(self.available_columns) > 0:
            cols = self.available_columns  # Alle Spalten exportieren
            print(f"Starting export with special characters to CSV test...")
            selected_data = self.analyzer.select_columns(cols)
            exporter = CSVExporter(selected_data, cols)
            file_path = 'special_characters_output.csv'
            exporter.export_to_csv(file_path)
            self.assertTrue(os.path.exists(file_path), f"File {file_path} was not created.")
            os.remove(file_path)
            print(f"Data with special characters exported to '{file_path}' successfully.")

if __name__ == '__main__':
    unittest.main()
