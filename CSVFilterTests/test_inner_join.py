import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer, CSVFilter

class TestInnerJoin(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header  # Dynamisch die verfügbaren Spalten ermitteln
        print("Available columns:", self.available_columns)
        
        # Erstellen von other_data.csv für die Join-Tests
        other_data_content = [
            [self.available_columns[0], 'Code'],
            ['Deutschland', 'DE'],
            ['Kasachstan', 'KZ']
        ]
        with open('other_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(other_data_content)

    def test_inner_join(self):
        if len(self.available_columns) > 0:
            other_analyzer = CSVAnalyzer('other_data.csv')
            joined_data = CSVFilter(self.analyzer.data, self.analyzer.header).inner_join(other_analyzer, self.available_columns[0])
            self._save_result_to_csv('inner_join_results.csv', joined_data)
            self.assertGreater(len(joined_data), 0, f"Inner join using column '{self.available_columns[0]}' failed")
            print(f"Inner join result using column '{self.available_columns[0]}' exported to CSV.")
        else:
            print("No columns available for inner join test.")

    def _save_result_to_csv(self, filename, data):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if isinstance(data, list) and all(isinstance(item, list) for item in data):
                writer.writerows(data)
            else:
                writer.writerow([data])

    # def tearDown(self):
    #     # Entfernen der other_data.csv nach den Tests
    #     if os.path.exists('other_data.csv'):
    #         os.remove('other_data.csv')

if __name__ == '__main__':
    unittest.main()
