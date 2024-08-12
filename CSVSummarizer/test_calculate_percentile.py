import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestCalculatePercentile(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_calculate_percentile(self):
        col = self.header[7]  # PLZ as an example
        percentile = self.summarizer.calculate_percentile(col, 90)
        print(f"90th Percentile of '{col}': {percentile}")
        self.assertIsNotNone(percentile)

if __name__ == '__main__':
    unittest.main()
