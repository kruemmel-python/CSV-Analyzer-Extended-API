import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestCalculateSum(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_calculate_sum(self):
        col = self.header[7]  # PLZ as an example
        total_sum = self.summarizer.calculate_sum(col)
        print(f"Sum of '{col}': {total_sum}")
        self.assertIsNotNone(total_sum)

if __name__ == '__main__':
    unittest.main()
