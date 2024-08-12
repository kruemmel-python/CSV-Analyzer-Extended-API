import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVExporter
import os

class TestExportAnalysisFirstColumn(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header  # Dynamisch die verfügbaren Spalten ermitteln
        print("Available columns:", self.available_columns)

    def test_export_analysis_first_column(self):
        if len(self.available_columns) > 0:
            first_column = self.available_columns[0]
            print(f"Starting analysis export test for '{first_column}' column...")
            self.analyzer.analyze_and_export(first_column, f'{first_column}_analysis_results.csv')
            self.assertTrue(os.path.exists(f'{first_column}_analysis_results.csv'))
            print(f"Analysis for '{first_column}' exported to CSV.")
        else:
            print("No columns available for testing.")

      # def tearDown(self):
    #     # Entferne die erstellte Datei nach dem Test
    #     export_file = 'cumulative_sum_results.csv'
    #     if os.path.exists(export_file):
    #         os.remove(export_file)

if __name__ == '__main__':
    unittest.main()
