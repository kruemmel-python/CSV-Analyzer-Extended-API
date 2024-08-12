import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVFilter, CSVSorter, CSVExporter
import os

class TestSortAndSelect(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header
        print("Available columns:", self.available_columns)

    def test_sort_and_select(self):
        if len(self.available_columns) > 0:
            print(f"Starting sort and select test for '{self.available_columns[0]}' column...")
            sorted_data = CSVSorter(self.analyzer.data, self.analyzer.header).sort_by_column(self.available_columns[0])
            filter_instance = CSVFilter(sorted_data, self.analyzer.header)
            selected_data = filter_instance.select_columns([self.available_columns[0]])
            self._save_result_to_csv('sort_and_select_results.csv', selected_data)
            self.assertGreater(len(selected_data), 0)
            print(f"Sorted and selected data for '{self.available_columns[0]}' exported to CSV.")
        else:
            print("No columns available for sort and select test.")

    def _save_result_to_csv(self, filename, data):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if isinstance(data, list) and all(isinstance(item, list) for item in data):
                writer.writerows(data)
            else:
                writer.writerow([data])

if __name__ == '__main__':
    unittest.main()
