import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVFilter
import os

class TestMultiColumnFilter(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header
        print("Available columns:", self.available_columns)

    def test_multi_column_filter(self):
        if len(self.available_columns) > 1:
            col1 = self.available_columns[0]  # Zum Beispiel 'Land'
            col2 = self.available_columns[1]  # Zum Beispiel 'Vorname'
            print(f"Starting multi-column filter test for '{col1}' and '{col2}' columns...")
            
            # Beispielbedingungen, die sicherstellen sollten, dass Ergebnisse zurückgegeben werden
            filter_conditions = [
                (col1, '==', 'Tonga'),
                (col2, '==', 'Anna-Marie')
            ]
            
            csv_filter = CSVFilter(self.analyzer.data, self.analyzer.header)
            filtered_data = csv_filter.filter_by_condition_chain(filter_conditions)
            
            self.assertGreater(len(filtered_data), 0, "No data returned by multi-column filter")
            print(f"Filtered data by multi-column conditions on '{col1}' and '{col2}' exported to CSV.")
        else:
            print("Not enough columns available for multi-column filter test.")

if __name__ == '__main__':
    unittest.main()
