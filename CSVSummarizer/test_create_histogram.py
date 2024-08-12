import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestCreateHistogram(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_create_histogram(self):
        col = self.header[7]  # PLZ as an example
        histogram = self.summarizer.create_histogram(col)
        print(f"Histogram for '{col}': {histogram}")
        self.assertIsNotNone(histogram)

if __name__ == '__main__':
    unittest.main()
