import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestCalculateMax(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_calculate_max(self):
        col = self.header[7]  # PLZ as an example
        max_value = self.summarizer.calculate_max(col)
        print(f"Max of '{col}': {max_value}")
        self.assertIsNotNone(max_value)

if __name__ == '__main__':
    unittest.main()
