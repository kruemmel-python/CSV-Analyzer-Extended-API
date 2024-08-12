import unittest
import os
import csv  # Das csv-Modul wird hier importiert
from csv_analyzer_extended import CSVAnalyzer, CSVExporter

class TestExportLargeDataToJSON(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header
        self.exporter = CSVExporter(self.analyzer.data, self.available_columns)
        print("Available columns:", self.available_columns)

    def test_export_large_data_to_json(self):
        if len(self.available_columns) > 0:
            print(f"Starting export of large data to JSON...")
            output_file = 'large_data_output.json'
            self.exporter.export_to_json(output_file)
            self.assertTrue(os.path.exists(output_file), "Export to JSON failed, file not found.")
            print(f"Large data exported to JSON file '{output_file}'.")

    def tearDown(self):
        # Entferne die generierte Datei nach dem Test
        if os.path.exists('large_data_output.json'):
            os.remove('large_data_output.json')

if __name__ == '__main__':
    unittest.main()
