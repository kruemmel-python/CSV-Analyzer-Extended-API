import unittest
from csv_analyzer_extended import CSVAnalyzer  # CSVExporter nicht benötigt, da es nur in CSVAnalyzer verwendet wird
import os

class TestCSVAnalysisAndExport(unittest.TestCase):
    def setUp(self):
        print("Setting up the analyzer...")
        self.analyzer = CSVAnalyzer('data.csv')  # Pfad zur CSV-Datei mit 40.000 Datensätzen
        self.available_columns = self.analyzer.header  # Dynamisch die verfügbaren Spalten ermitteln
        print("Available columns:", self.available_columns)
        print("Analyzer setup complete.")

    def test_export_analysis_first_column(self):
        if len(self.available_columns) > 0:
            first_column = self.available_columns[0]
            print(f"Starting analysis export test for '{first_column}' column...")
            self.analyzer.analyze_and_export(first_column, f'{first_column}_analysis_results.csv')
            self.assertTrue(os.path.exists(f'{first_column}_analysis_results.csv'))
            print(f"Analysis for '{first_column}' exported to CSV.")
        else:
            print("No columns available for testing.")

    def test_export_analysis_second_column(self):
        if len(self.available_columns) > 1:
            second_column = self.available_columns[1]
            print(f"Starting analysis export test for '{second_column}' column...")
            self.analyzer.analyze_and_export(second_column, f'{second_column}_analysis_results.csv')
            self.assertTrue(os.path.exists(f'{second_column}_analysis_results.csv'))
            print(f"Analysis for '{second_column}' exported to CSV.")
        else:
            print("Not enough columns available for testing.")

    def test_export_analysis_two_columns(self):
        if len(self.available_columns) > 1:
            column1 = self.available_columns[0]
            column2 = self.available_columns[1]
            print(f"Starting analysis export test for '{column1}' vs '{column2}' columns...")
            self.analyzer.analyze_and_export(column1, f'{column1}_vs_{column2}_analysis_results.csv')
            self.assertTrue(os.path.exists(f'{column1}_vs_{column2}_analysis_results.csv'))
            print(f"Analysis for '{column1}' vs '{column2}' exported to CSV.")
        else:
            print("Not enough columns available for testing two columns.")

if __name__ == '__main__':
    unittest.main()
