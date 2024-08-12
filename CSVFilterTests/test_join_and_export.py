import unittest
import csv
import os
from csv_analyzer_extended import CSVAnalyzer, CSVFilter, CSVExporter

class TestJoinAndExport(unittest.TestCase):
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

    def test_join_and_export(self):
        if len(self.available_columns) > 0:
            other_analyzer = CSVAnalyzer('other_data.csv')
            joined_data = CSVFilter(self.analyzer.data, self.analyzer.header).inner_join(other_analyzer, self.available_columns[0])
            export_file = f'{self.available_columns[0]}_join_export.csv'
            CSVExporter(joined_data, self.analyzer.header + other_analyzer.header).export_to_csv(export_file)
            self.assertTrue(os.path.exists(export_file), f"Join and export failed for column '{self.available_columns[0]}'")
            print(f"Join and export completed for column '{self.available_columns[0]}' exported to CSV.")

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
