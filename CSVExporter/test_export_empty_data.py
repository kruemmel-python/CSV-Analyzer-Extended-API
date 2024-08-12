import unittest
import os
from csv_analyzer_extended import CSVExporter

class TestExportEmptyData(unittest.TestCase):
    def setUp(self):
        self.header = ['Column1', 'Column2', 'Column3']
        self.empty_data = []

    def test_export_empty_data_to_csv(self):
        print("Starting export empty data to CSV test...")
        exporter = CSVExporter(self.empty_data, self.header)
        file_path = 'empty_data_output.csv'
        exporter.export_to_csv(file_path)
        self.assertTrue(os.path.exists(file_path), f"File {file_path} was not created.")
        os.remove(file_path)
        print(f"Empty data exported to '{file_path}' successfully.")

if __name__ == '__main__':
    unittest.main()
