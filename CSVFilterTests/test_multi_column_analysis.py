import unittest
import csv
from csv_analyzer_extended import CSVAnalyzer

class TestMultiColumnAnalysis(unittest.TestCase):
    def setUp(self):
        self.analyzer = CSVAnalyzer('data.csv')
        self.available_columns = self.analyzer.header  # Dynamisch die verfügbaren Spalten ermitteln
        print("Available columns:", self.available_columns)

    def test_multi_column_analysis(self):
        # Finde eine numerische Spalte für die Analyse
        numeric_columns = [col for col in self.available_columns if self._is_numeric_column(col)]
        
        if len(numeric_columns) > 1:
            col1 = numeric_columns[0]
            col2 = numeric_columns[1]
            print(f"Starting multi-column analysis for '{col1}' and '{col2}' columns...")
            result = self.analyzer.calculate_correlation(col1, col2)
            self._save_result_to_csv('multi_column_analysis_results.csv', [f"Correlation between '{col1}' and '{col2}':", result])
        else:
            print("Not enough numeric columns available for multi-column analysis.")

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
    #     pass  # tearDown auskommentiert, um keine Aufräumarbeiten durchzuführen

if __name__ == '__main__':
    unittest.main()
