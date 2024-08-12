import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVFilter
import os

class TestContainsText(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header  # Dynamisch die verfügbaren Spalten ermitteln
        print("Available columns:", self.available_columns)

    def test_contains_text(self):
        if len(self.available_columns) > 0:
            col = self.available_columns[0]
            print(f"Starting contains text test for column '{col}'...")
            text_data = CSVFilter(self.analyzer.data, self.analyzer.header).contains_text(col, 'Tonga')
            self._save_result_to_csv('contains_text_results.csv', text_data)
            self.assertGreater(len(text_data), 0, f"No data found containing 'Tonga' in '{col}'")
            print(f"Filtered data containing 'Tonga' in '{col}' exported to CSV.")
        else:
            print("No columns available for contains text test.")

    def _save_result_to_csv(self, filename, data):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if isinstance(data, list) and all(isinstance(item, list) for item in data):
                writer.writerows(data)
            else:
                writer.writerow([data])

    # def tearDown(self):
    #     # Entferne die erstellte Datei nach dem Test
    #     export_file = 'cumulative_sum_results.csv'
    #     if os.path.exists(export_file):
    #         os.remove(export_file)

if __name__ == '__main__':
    unittest.main()
