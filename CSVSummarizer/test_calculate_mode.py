import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestCalculateMode(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_calculate_mode(self):
        col = self.header[7]  # PLZ as an example
        mode_value, frequency = self.summarizer.calculate_mode(col)
        print(f"Mode of '{col}': {mode_value} with frequency {frequency}")
        self.assertIsNotNone(mode_value)

if __name__ == '__main__':
    unittest.main()
