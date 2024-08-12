import unittest
import os
from csv_analyzer_extended import CSVAnalyzer, CSVExporter

class TestExportToXML(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header
        self.exporter = CSVExporter(self.analyzer.data, self.available_columns)
        print("Available columns:", self.available_columns)

    def test_export_to_xml(self):
        if len(self.available_columns) > 0:
            print(f"Starting export to XML test...")
            output_file = 'output.xml'
            self.exporter.export_to_xml(output_file)
            self.assertTrue(os.path.exists(output_file), "Export to XML failed, file not found.")
            print(f"Data exported to XML file '{output_file}'.")

    def tearDown(self):
        # Remove the generated file after test
        if os.path.exists('output.xml'):
            os.remove('output.xml')

if __name__ == '__main__':
    unittest.main()
