import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVSorter

class TestMultiColumnSort(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header
        print("Available columns:", self.available_columns)

    def test_multi_column_sort(self):
        if len(self.available_columns) > 2:
            cols = self.available_columns[:2]
            print(f"Starting multi-column sort test for columns '{cols}'...")
            sorted_data = CSVSorter(self.analyzer.data, self.analyzer.header).multi_column_sort(cols)
            self._save_result_to_csv(f'multi_column_sort_results.csv', sorted_data)
            self.assertGreater(len(sorted_data), 0, f"No data found after sorting by '{cols}'")
            print(f"Sorted data by '{cols}' exported to CSV.")
        else:
            print("Not enough columns available for multi-column sort test.")

    def _save_result_to_csv(self, filename, data):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

if __name__ == '__main__':
    unittest.main()
