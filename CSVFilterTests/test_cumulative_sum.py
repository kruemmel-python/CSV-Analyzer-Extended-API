import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVFilter

class TestCumulativeSum(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header  # Dynamisch die verfügbaren Spalten ermitteln
        print("Available columns:", self.available_columns)

    def test_cumulative_sum(self):
        # Finde eine numerische Spalte für die Analyse
        numeric_columns = [col for col in self.available_columns if self._is_numeric_column(col)]
    
        if len(numeric_columns) > 0:
            col = numeric_columns[0]
            print(f"Starting cumulative sum test for column '{col}'...")
            cumulative_sum_data = CSVFilter(self.analyzer.data, self.analyzer.header).cumulative_sum(col)
            self._save_result_to_csv('cumulative_sum_results.csv', cumulative_sum_data)
            self.assertGreater(len(cumulative_sum_data), 0, f"Cumulative sum calculation for '{col}' failed")
            print(f"Cumulative sum for '{col}' exported to CSV.")
        else:
            print("No numeric columns available for cumulative sum test.")

    def _is_numeric_column(self, column_name):
        try:
            index = self.available_columns.index(column_name)
            for row in self.analyzer.data:
                float(row[index])
            return True
        except ValueError:
            return False

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
