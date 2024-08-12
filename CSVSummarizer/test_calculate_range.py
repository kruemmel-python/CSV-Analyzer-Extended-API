import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestCalculateRange(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_calculate_range(self):
        col = self.header[7]  # PLZ as an example
        range_value = self.summarizer.calculate_range(col)
        print(f"Range of '{col}': {range_value}")
        self.assertIsNotNone(range_value)

if __name__ == '__main__':
    unittest.main()
