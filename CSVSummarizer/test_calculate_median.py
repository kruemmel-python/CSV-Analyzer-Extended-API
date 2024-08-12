import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestCalculateMedian(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_calculate_median(self):
        col = self.header[7]  # PLZ as an example
        median_value = self.summarizer.calculate_median(col)
        print(f"Median of '{col}': {median_value}")
        self.assertIsNotNone(median_value)

if __name__ == '__main__':
    unittest.main()
