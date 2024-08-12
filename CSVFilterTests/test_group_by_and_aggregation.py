import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVFilter

class TestGroupByAndAggregation(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header  # Dynamisch die verfügbaren Spalten ermitteln
        print("Available columns:", self.available_columns)

    def test_group_by_and_aggregation(self):
        # Finde eine numerische Spalte für die Aggregation
        numeric_columns = [col for col in self.available_columns if self._is_numeric_column(col)]
    
        if len(numeric_columns) > 1:
            col = numeric_columns[0]  # Gruppieren nach der ersten numerischen Spalte
            print(f"Starting group by and aggregation test for column '{col}'...")
            group_by_data = CSVFilter(self.analyzer.data, self.analyzer.header).group_by(
                col, lambda rows: sum(float(row[self.analyzer.header.index(col)]) for row in rows))
            self._save_result_to_csv(f'group_by_{col}_results.csv', group_by_data)
            self.assertGreater(len(group_by_data), 0, f"Group by and aggregation for '{col}' failed")
            print(f"Group by and aggregation for '{col}' exported to CSV.")
        else:
            print("No numeric columns available for group by and aggregation test.")

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
    #     export_file = f'group_by_{self.available_columns[0]}_results.csv'
    #     if os.path.exists(export_file):
    #         os.remove(export_file)

if __name__ == '__main__':
    unittest.main()
