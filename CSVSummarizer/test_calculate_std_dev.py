import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestCalculateStdDev(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_calculate_std_dev(self):
        col = self.header[7]  # PLZ as an example
        std_dev = self.summarizer.calculate_std_dev(col)
        print(f"Standard Deviation of '{col}': {std_dev}")
        self.assertIsNotNone(std_dev)

if __name__ == '__main__':
    unittest.main()
