import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVFilter

class TestSelectColumns(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header  # Dynamisch die verfügbaren Spalten ermitteln
        self.filter = CSVFilter(self.analyzer.data, self.analyzer.header)  # Verwende CSVFilter für die Methode

    def test_select_columns(self):
        if len(self.available_columns) > 2:
            selected_columns = self.available_columns[:3]  # Wähle die ersten drei Spalten
            print(f"Starting select columns test for columns: {selected_columns}...")
            selected_data = self.filter.select_columns(selected_columns)  # Verwende CSVFilter
            self._save_result_to_csv('select_columns_results.csv', selected_data)
            self.assertGreater(len(selected_data), 0)
            print(f"Selected columns data for {selected_columns} exported to CSV.")
        else:
            print("Not enough columns available for select columns test.")

    def _save_result_to_csv(self, filename, data):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if isinstance(data, list) and all(isinstance(item, list) for item in data):
                writer.writerows(data)
            else:
                writer.writerow([data])

if __name__ == '__main__':
    unittest.main()
