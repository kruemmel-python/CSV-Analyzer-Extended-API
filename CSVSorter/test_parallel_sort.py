import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVSorter

class TestParallelSort(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header
        print("Available columns:", self.available_columns)

    def test_parallel_sort(self):
        if len(self.available_columns) > 0:
            col = self.available_columns[0]
            print(f"Starting parallel sort test for '{col}' column...")
            sorted_data = CSVSorter(self.analyzer.data, self.analyzer.header).parallel_sort(col, num_threads=4)
            self._save_result_to_csv(f'parallel_sort_{col}_results.csv', sorted_data)
            self.assertGreater(len(sorted_data), 0, f"No data found after parallel sorting by '{col}'")
            print(f"Parallel sorted data by '{col}' exported to CSV.")
        else:
            print("No columns available for parallel sort test.")

    def _save_result_to_csv(self, filename, data):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

if __name__ == '__main__':
    unittest.main()
