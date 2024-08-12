import unittest
import os
from csv_analyzer_extended import CSVExporter, CSVAnalyzer

class TestExportToPDF(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header
        print("Available columns:", self.available_columns)

    def test_export_to_pdf(self):
        if len(self.available_columns) > 0:
            data_to_export = self.analyzer.data  # Die Daten direkt von der CSV-Datei verwenden
            exporter = CSVExporter(data_to_export, self.available_columns)
            exporter.export_to_pdf('output.pdf')
            self.assertTrue(os.path.exists('output.pdf'))
            print("Export to PDF completed successfully.")
        else:
            print("No columns available for export test.")

    def tearDown(self):
        if os.path.exists('output.pdf'):
            os.remove('output.pdf')

if __name__ == '__main__':
    unittest.main()
